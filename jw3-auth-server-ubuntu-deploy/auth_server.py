#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JW3 授权验证服务
JW3 authorization validation service for clients
基于FastAPI + SQLAlchemy + 现代化设计
"""

import os
import sys
import io
import logging
import secrets
import hashlib
import base64
import hmac
import json
import time
import glob
import re
import threading
from ipaddress import ip_address
from collections import deque
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, List, Tuple
from contextlib import asynccontextmanager
from urllib.parse import quote

import pytz
import requests
from passlib.context import CryptContext
from cryptography.fernet import Fernet, InvalidToken

# FastAPI相关导入
from fastapi import FastAPI, HTTPException, Depends, Request, Response, status, __version__ as fastapi_version

# 内存 Session 存储（避SQLite 并发
_admin_sessions: Dict[str, Dict[str, Any]] = {}
_market_author_sessions: Dict[str, Dict[str, Any]] = {}
_session_lock = threading.RLock()
_market_author_session_lock = threading.RLock()
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, "logs")
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
STATIC_DIR = os.path.join(SCRIPT_DIR, "static")
TEMPLATES_DIR = os.path.join(SCRIPT_DIR, "templates")
PROJECT_LOG_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "logs")

_SESSION_FILE = os.path.join(DATA_DIR, "admin_sessions.json")
_MARKET_AUTHOR_SESSION_TTL_SECONDS = 7 * 24 * 60 * 60
_secondary_delete_verified_sessions: Dict[str, datetime] = {}
_secondary_delete_verified_lock = threading.RLock()
_admin_login_failures: Dict[str, Dict[str, Any]] = {}
_admin_login_failures_lock = threading.RLock()
_rate_limit_records: Dict[str, List[float]] = {}
_rate_limit_lock = threading.RLock()
_request_nonce_expiry: Dict[str, int] = {}
_request_nonce_lock = threading.RLock()
_REQUEST_NONCE_DEFAULT_TTL_SECONDS = 600
_REQUEST_NONCE_MAX_RECORDS = 50000
_CLIENT_CSRF_TOKEN_TTL_SECONDS = 30 * 60
APP_VERSION = "1.0.0"
SERVER_START_MONOTONIC = time.monotonic()
SERVER_START_TIME_UTC = datetime.now(timezone.utc)
_CLIENT_ONLINE_UPDATE_ENABLED = str(os.getenv("ENABLE_CLIENT_ONLINE_UPDATE", "") or "").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

SYSTEM_SETTING_META: Dict[str, Dict[str, Any]] = {
    "server_name": {
        "default": "JW3授权验证服务端",
        "description": "服务器名称",
    },
    "max_clients": {
        "default": 1000,
        "description": "最大客户端数量",
    },
    "session_timeout_minutes": {
        "default": 60,
        "description": "管理员会话超时时间（分钟）",
    },
    "enable_logging": {
        "default": True,
        "description": "是否启用详细日志记录",
    },
    "max_login_attempts": {
        "default": 5,
        "description": "管理员登录最大尝试次数",
    },
    "lockout_duration_minutes": {
        "default": 30,
        "description": "管理员登录锁定时长（分钟）",
    },
    "enable_csrf": {
        "default": True,
        "description": "是否启用CSRF校验",
    },
    "enable_rate_limit": {
        "default": True,
        "description": "是否启用API速率限制",
    },
    "market_update_server_base": {
        "default": str(os.getenv("MARKET_UPDATE_SERVER_BASE", "") or "").strip(),
        "description": "共享平台包更新服务器基础地址",
    },
}

_runtime_flags_lock = threading.RLock()
_runtime_flags: Dict[str, bool] = {
    "enable_logging": bool(SYSTEM_SETTING_META["enable_logging"]["default"]),
    "enable_csrf": bool(SYSTEM_SETTING_META["enable_csrf"]["default"]),
    "enable_rate_limit": bool(SYSTEM_SETTING_META["enable_rate_limit"]["default"]),
}

_RATE_LIMIT_WINDOW_SECONDS = 60
_RATE_LIMIT_MAX_REQUESTS = 600
_RATE_LIMIT_EXCLUDED_PATHS = {
    "/api/admin/verify_session",
    "/api/admin/check_auth",
}
_TRUST_PROXY_HEADERS = str(os.getenv("TRUST_PROXY_HEADERS", "true") or "").strip().lower() not in {
    "0",
    "false",
    "no",
    "off",
}
_CLIENT_IP_HEADERS = (
    "cf-connecting-ip",
    "true-client-ip",
    "x-real-ip",
    "x-forwarded-for",
)


def _normalize_ip_candidate(value: Any) -> str:
    candidate = str(value or "").strip().strip('"').strip("'")
    if not candidate:
        return ""
    if candidate.startswith("[") and "]" in candidate:
        candidate = candidate[1:candidate.index("]")]
    elif candidate.count(":") == 1 and "." in candidate:
        candidate = candidate.rsplit(":", 1)[0]
    try:
        return str(ip_address(candidate))
    except ValueError:
        return ""


def get_client_ip(request: Request) -> str:
    if _TRUST_PROXY_HEADERS:
        for header_name in _CLIENT_IP_HEADERS:
            raw_value = request.headers.get(header_name)
            if not raw_value:
                continue
            for part in str(raw_value).split(","):
                normalized = _normalize_ip_candidate(part)
                if normalized:
                    return normalized

    if request.client and request.client.host:
        normalized = _normalize_ip_candidate(request.client.host)
        return normalized or str(request.client.host)
    return "unknown"


def generate_client_csrf_token() -> str:
    nonce = secrets.token_urlsafe(24)
    issued_at = int(time.time())
    payload = f"{nonce}.{issued_at}"
    signature = hmac.new(
        SECRET_KEY.encode("utf-8"),
        f"client-csrf|{payload}".encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return f"{payload}.{signature}"


def verify_client_csrf_token(token: Any) -> bool:
    token_text = str(token or "").strip()
    parts = token_text.split(".")
    if len(parts) != 3:
        return False
    nonce, issued_at_text, signature = parts
    if not validate_nonce_text(nonce, min_len=16, max_len=64):
        return False
    try:
        issued_at = int(issued_at_text)
    except Exception:
        return False
    now_ts = int(time.time())
    if issued_at > now_ts + 60 or now_ts - issued_at > _CLIENT_CSRF_TOKEN_TTL_SECONDS:
        return False
    expected = hmac.new(
        SECRET_KEY.encode("utf-8"),
        f"client-csrf|{nonce}.{issued_at}".encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(signature, expected)


def validate_client_registration_csrf(request: Request, endpoint_name: str) -> None:
    csrf_token_from_header = request.headers.get("X-CSRFToken")
    csrf_token_from_session = request.session.get("csrf_token")

    if not csrf_token_from_header:
        logger.warning("%s客户端注册失败: 请求头中缺少CSRF token", endpoint_name)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="请求头中缺少CSRF token"
        )

    if csrf_token_from_session and csrf_token_from_header == csrf_token_from_session:
        return

    if verify_client_csrf_token(csrf_token_from_header):
        return

    logger.warning("%s客户端注册失败: CSRF token校验失败", endpoint_name)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="CSRF token校验失败"
    )

def _session_token_key(session_token: str) -> str:
    """将会话token映射为固定长度安全键，避免明文落盘。"""
    token_text = str(session_token or "").strip()
    if not token_text:
        return ""
    return hmac.new(
        SECRET_KEY.encode("utf-8"),
        token_text.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

def _load_sessions():
    """从文件加载管理员会话。"""
    global _admin_sessions
    if os.path.exists(_SESSION_FILE):
        try:
            with open(_SESSION_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 恢复会话并过滤过期数据
                _admin_sessions = {}
                for token_key, sess_data in data.items():
                    if not isinstance(sess_data, dict):
                        continue
                    try:
                        expires = datetime.fromisoformat(str(sess_data['expires_at']))
                        created_at = datetime.fromisoformat(str(sess_data['created_at']))
                    except Exception:
                        continue
                    if expires <= datetime.utcnow():
                        continue

                    normalized_key = str(token_key or "").strip()
                    if not re.fullmatch(r"[0-9a-fA-F]{64}", normalized_key):
                        normalized_key = _session_token_key(normalized_key)
                    if not normalized_key:
                        continue

                    _admin_sessions[normalized_key] = {
                        'user_id': sess_data['user_id'],
                        'expires_at': expires,
                        'ip_address': sess_data.get('ip_address'),
                        'user_agent': sess_data.get('user_agent'),
                        'created_at': created_at
                    }
        except Exception as e:
            logger.warning(f"加载会话文件失败: {e}")

def _save_sessions():
    """将会话保存到文件"""
    try:
        with _session_lock:
            data = {}
            for token_key, sess_data in _admin_sessions.items():
                data[token_key] = {
                    'user_id': sess_data['user_id'],
                    'expires_at': sess_data['expires_at'].isoformat(),
                    'ip_address': sess_data.get('ip_address'),
                    'user_agent': sess_data.get('user_agent'),
                    'created_at': sess_data['created_at'].isoformat()
                }
        with open(_SESSION_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception as e:
        logger.warning(f"保存会话文件失败: {e}")
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 数据库相关
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Integer, Text, ForeignKey, case, or_, text, inspect
from sqlalchemy.orm import sessionmaker, Session, relationship, DeclarativeBase, selectinload
from sqlalchemy.sql import func

from market_models import register_market_models
from market_router import build_market_router
from market_schemas import MarketAuthorAuthResponse, MarketAuthorCredentialsRequest, MarketAuthorProfile
from runtime_env import build_default_database_url, resolve_security_environment

logger = logging.getLogger("jw3-auth-server")
_SERVER_LOGGING_CONFIG_LOCK = threading.RLock()
_SERVER_LOGGING_CONFIGURED = False
_RUNTIME_STORAGE_INIT_LOCK = threading.RLock()
_RUNTIME_STORAGE_INITIALIZED = False
_SERVER_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
_SERVER_LOG_FILE = os.path.join(LOG_DIR, "auth_server.log")

# Sanitize obvious mojibake log lines only.
_MOJIBAKE_MARKERS = {chr(cp) for cp in (0x9352, 0x93ba, 0x7481, 0x9428, 0x93b5, 0x93c8, 0x9359, 0x935a, 0x7f01, 0x7eef, 0x7ee0, 0x6960, 0x7609, 0x59dd, 0x9354, 0x95c2, 0x9350, 0x6d98, 0x6d63, 0x93b4, 0x7039, 0x93ad)}


def _looks_like_mojibake(text: str) -> bool:
    if not text:
        return False
    marker_count = sum(1 for ch in text if ch in _MOJIBAKE_MARKERS)
    if marker_count < 3:
        return False
    return (marker_count / max(len(text), 1)) >= 0.18


class _MojibakeSanitizerFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            message = record.getMessage()
        except Exception:
            return True
        if isinstance(message, str) and _looks_like_mojibake(message):
            record.msg = "日志文本已清理（检测到历史编码异常）"
            record.args = ()
        return True


_mojibake_sanitizer = _MojibakeSanitizerFilter()


def _normalize_abs_path(path: str) -> str:
    return os.path.normcase(os.path.abspath(str(path or "")))


def _ensure_runtime_directories() -> None:
    for runtime_path in (LOG_DIR, DATA_DIR, STATIC_DIR, TEMPLATES_DIR):
        try:
            os.makedirs(runtime_path, exist_ok=True)
        except Exception:
            continue


def _has_filter(target: Any, log_filter: logging.Filter) -> bool:
    return any(existing is log_filter for existing in getattr(target, "filters", ()))


def _install_mojibake_filter(target: Any) -> None:
    if _has_filter(target, _mojibake_sanitizer):
        return
    try:
        target.addFilter(_mojibake_sanitizer)
    except Exception:
        pass


def _has_log_file_handler(root_logger: logging.Logger) -> bool:
    expected_path = _normalize_abs_path(_SERVER_LOG_FILE)
    for handler in root_logger.handlers:
        handler_path = getattr(handler, "baseFilename", "")
        if handler_path and _normalize_abs_path(handler_path) == expected_path:
            return True
    return False


def _has_stdout_stream_handler(root_logger: logging.Logger) -> bool:
    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler):
            continue
        if isinstance(handler, logging.StreamHandler) and getattr(handler, "stream", None) is sys.stdout:
            return True
    return False


def _configure_server_logging() -> None:
    global _SERVER_LOGGING_CONFIGURED

    with _SERVER_LOGGING_CONFIG_LOCK:
        _ensure_runtime_directories()

        formatter = logging.Formatter(_SERVER_LOG_FORMAT)
        root_logger = logging.getLogger()

        if not _has_log_file_handler(root_logger):
            file_handler = logging.FileHandler(_SERVER_LOG_FILE, encoding="utf-8")
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)

        if not _has_stdout_stream_handler(root_logger):
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            root_logger.addHandler(stream_handler)

        root_logger.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)

        for handler in root_logger.handlers:
            _install_mojibake_filter(handler)
        _install_mojibake_filter(logger)

        _SERVER_LOGGING_CONFIGURED = True

# 时区配置
BEIJING_TZ = pytz.timezone('Asia/Shanghai')

def get_beijing_time():
    """获取北京时间"""
    return datetime.now(BEIJING_TZ)

def utc_to_beijing(utc_dt):
    """Convert UTC time to Beijing time."""
    if utc_dt is None:
        return None
    if utc_dt.tzinfo is None:
        utc_dt = pytz.utc.localize(utc_dt)
    return utc_dt.astimezone(BEIJING_TZ)

def beijing_to_utc(beijing_dt):
    """将北京时间转换为UTC时间"""
    if beijing_dt is None:
        return None
    if beijing_dt.tzinfo is None:
        beijing_dt = BEIJING_TZ.localize(beijing_dt)
    return beijing_dt.astimezone(pytz.utc)

# 配置
DATABASE_URL = os.getenv("DATABASE_URL", build_default_database_url(SCRIPT_DIR))
_security_environment = resolve_security_environment(os.environ)
SECRET_KEY = _security_environment.secret_key
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = _security_environment.admin_password


def detect_database_type(database_url: str) -> str:
    normalized = str(database_url or "").strip().lower()
    if normalized.startswith("sqlite"):
        return "SQLite"
    if normalized.startswith("postgresql"):
        return "PostgreSQL"
    if normalized.startswith("mysql"):
        return "MySQL"
    if normalized.startswith("mssql"):
        return "MSSQL"
    if normalized.startswith("oracle"):
        return "Oracle"
    return "Unknown"

# CORS allowed origins list; configure explicit domains in production.
_cors_raw = str(os.getenv("CORS_ORIGINS", "") or "").strip()
if not _cors_raw:
    CORS_ORIGINS = [
        "http://127.0.0.1",
        "http://localhost",
        "https://127.0.0.1",
        "https://localhost",
    ]
else:
    CORS_ORIGINS = [item.strip() for item in _cors_raw.split(",") if item.strip()]
if not CORS_ORIGINS:
    CORS_ORIGINS = [
        "http://127.0.0.1",
        "http://localhost",
        "https://127.0.0.1",
        "https://localhost",
    ]
CORS_ALLOW_CREDENTIALS = "*" not in CORS_ORIGINS

_COMM_AUTH_SECRET_FILE_RELATIVE = os.path.join("config", "build_auth_secret.b64x2")
_COMM_AUTH_SECRET_FILE_ENV = "LCA_AUTH_SECRET_FILE"



def _build_market_payload_fernet() -> Fernet:
    key_material = hashlib.sha256(f"market-payload|{SECRET_KEY}".encode("utf-8")).digest()
    return Fernet(base64.urlsafe_b64encode(key_material))


def encrypt_market_payload_key(payload_key: str) -> str:
    text_value = str(payload_key or "").strip()
    if not text_value:
        return ""
    return _build_market_payload_fernet().encrypt(text_value.encode("utf-8")).decode("utf-8")


def decrypt_market_payload_key(cipher_text: str) -> str:
    text_value = str(cipher_text or "").strip()
    if not text_value:
        return ""
    try:
        return _build_market_payload_fernet().decrypt(text_value.encode("utf-8")).decode("utf-8")
    except InvalidToken as exc:
        raise HTTPException(status_code=500, detail="market_payload_key_invalid") from exc


def get_market_upload_ticket_secret() -> str:
    secret_value = str(os.getenv("MARKET_UPLOAD_TICKET_SECRET", "") or "").strip()
    if secret_value:
        return secret_value
    token_value = get_market_update_server_token()
    if token_value:
        return token_value
    return ""


def _encode_urlsafe_json_bytes(payload: Dict[str, Any]) -> str:
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("utf-8").rstrip("=")


def build_market_upload_ticket(package_id: str, version: str, author_user_id: int, expires_in: int = 300) -> str:
    secret_value = get_market_upload_ticket_secret()
    if not secret_value:
        raise HTTPException(status_code=500, detail="market_upload_ticket_secret_not_configured")
    issued_at = int(time.time())
    expires_at = issued_at + max(60, int(expires_in or 300))
    payload = {
        "package_id": str(package_id or "").strip(),
        "version": str(version or "").strip(),
        "author_user_id": int(author_user_id or 0),
        "iat": issued_at,
        "exp": expires_at,
    }
    encoded_payload = _encode_urlsafe_json_bytes(payload)
    signature = hmac.new(
        secret_value.encode("utf-8"),
        encoded_payload.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    encoded_signature = base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")
    return f"{encoded_payload}.{encoded_signature}"


def _decode_b64x2(raw_text: str) -> str:
    text = str(raw_text or "").strip()
    if not text:
        return ""
    try:
        first = base64.b64decode(text).decode("utf-8")
        second = base64.b64decode(first).decode("utf-8")
        return str(second or "").strip()
    except Exception:
        return ""


def _is_weak_comm_auth_secret(secret_text: str) -> bool:
    secret_value = str(secret_text or "").strip()
    if len(secret_value) < 24:
        return True
    lowered = secret_value.lower()
    weak_values = {
        "default-secret-key-change-in-production",
        "default-secret-key",
        "changeme",
        "change-me",
        "123456",
        "password",
    }
    return lowered in weak_values


def _resolve_comm_auth_secret() -> str:
    env_secret = str(os.getenv("AUTH_SECRET_KEY", "") or "").strip()
    if not _is_weak_comm_auth_secret(env_secret):
        return env_secret

    candidate_paths = []

    env_path = str(os.getenv(_COMM_AUTH_SECRET_FILE_ENV, "") or "").strip()
    if env_path:
        if os.path.isabs(env_path):
            candidate_paths.append(os.path.abspath(env_path))
        else:
            candidate_paths.append(os.path.abspath(os.path.join(SCRIPT_DIR, env_path)))

    candidate_paths.extend(
        [
            os.path.join(SCRIPT_DIR, _COMM_AUTH_SECRET_FILE_RELATIVE),
            os.path.join(os.path.dirname(SCRIPT_DIR), _COMM_AUTH_SECRET_FILE_RELATIVE),
        ]
    )

    checked = set()
    for candidate in candidate_paths:
        abs_path = os.path.abspath(str(candidate or "").strip())
        normalized = os.path.normcase(abs_path)
        if not abs_path or normalized in checked:
            continue
        checked.add(normalized)
        if not os.path.isfile(abs_path):
            continue
        try:
            with open(abs_path, "r", encoding="utf-8") as secret_file:
                raw_secret = str(secret_file.read() or "").strip()
        except Exception:
            continue
        if not raw_secret:
            continue
        decoded_secret = _decode_b64x2(raw_secret)
        final_secret = decoded_secret if decoded_secret else raw_secret
        if not _is_weak_comm_auth_secret(final_secret):
            return final_secret

    raise RuntimeError("AUTH_SECRET_KEY 未配置且未找到可用通信密钥文件")


COMM_AUTH_SECRET_KEY = _resolve_comm_auth_secret()

# 数据库
if DATABASE_URL.startswith("sqlite"):
    # SQLite配置：添加并发锁处理和WAL模式
    from sqlalchemy import event
    from sqlalchemy.pool import StaticPool

    engine = create_engine(
        DATABASE_URL,
        echo=False,
        connect_args={"timeout": 60, "check_same_thread": False},
        poolclass=StaticPool,
        pool_pre_ping=True
    )

    # 启用SQLite WAL模式和优化
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA synchronous=NORMAL")
        cursor.execute("PRAGMA cache_size=10000")
        cursor.execute("PRAGMA temp_store=MEMORY")
        cursor.execute("PRAGMA busy_timeout=60000")  # 60秒超时
        cursor.execute("PRAGMA wal_autocheckpoint=5000")
        cursor.execute("PRAGMA locking_mode=NORMAL")
        cursor.close()
else:
    # PostgreSQL/MySQL配置
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 使用新式DeclarativeBase
class Base(DeclarativeBase):
    pass


MARKET_MODELS = register_market_models(Base)

# 密码哈希上下
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 数据库模
class User(Base):
    """用户"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    hardware_id = Column(String(64), index=True)  # 关联的硬件ID
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime)
    
    # 关系
    clients = relationship("Client", back_populates="user")

class AdminSession(Base):
    """管理员会话表"""
    __tablename__ = "admin_sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_token = Column(String(255), unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    ip_address = Column(String(45), nullable=True)  # 支持IPv6
    user_agent = Column(String(500), nullable=True)

    # 关系
    user = relationship("User")

class Client(Base):
    """客户备表"""
    __tablename__ = "clients"
    
    hardware_id = Column(String(64), primary_key=True, index=True)  # SHA256硬件ID
    user_id = Column(Integer, ForeignKey("users.id"))
    registration_date = Column(DateTime, default=func.now())
    last_seen = Column(DateTime)
    client_info = Column(Text)  # JSON格式的客户端信息
    is_active = Column(Boolean, default=True)
    
    # 关系
    user = relationship("User", back_populates="clients")
    license_keys = relationship("LicenseKey", back_populates="client")

class BannedHardwareId(Base):
    """Banned hardware ID record."""
    __tablename__ = "banned_hardware_ids"

    id = Column(Integer, primary_key=True, index=True)
    hardware_id = Column(String(64), unique=True, index=True, nullable=False)  # 被封禁的硬件ID
    reason = Column(Text)  # 封禁原因
    banned_at = Column(DateTime, default=func.now())  # 封禁时间
    banned_by = Column(String(50))  # 封禁操作员
    is_active = Column(Boolean, default=True)  # 是否生效
    expires_at = Column(DateTime)  # 封过期时间，None表示永久封
    notes = Column(Text)  # 备注信息

class LicenseKey(Base):
    """许可证密钥表"""
    __tablename__ = "license_keys"

    id = Column(Integer, primary_key=True, index=True)
    key_string = Column(String(50), unique=True, index=True, nullable=False)  # 许可证密钥
    key_type = Column(String(20), default="EDITOR")  # EDITOR, EXECUTOR等
    client_hardware_id = Column(String(64), ForeignKey("clients.hardware_id"))
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime)  # 过期时间，None表示永久
    is_active = Column(Boolean, default=True)
    max_activations = Column(Integer, default=1)  # 最大激活数量
    current_activations = Column(Integer, default=0)  # 当前激活数量
    parent_license_id = Column(Integer, index=True)  # 上级编辑器授权码ID（仅执行器授权码使用）
    # 关系
    client = relationship("Client", back_populates="license_keys")

class ActivationCard(Base):
    """活卡密表"""
    __tablename__ = "activation_cards"

    id = Column(Integer, primary_key=True, index=True)
    card_code = Column(String(50), unique=True, index=True, nullable=False)  # 卡密代码
    card_type = Column(String(20), default="EDITOR")  # 卡密类型：EDITOR, EXECUTOR等
    duration_days = Column(Integer, nullable=False)  # 有效期天数，0表示永久
    status = Column(String(20), default="unused")  # 状态：unused(未使用), used(已使用), expired(已过期), disabled(已禁用)
    created_at = Column(DateTime, default=func.now())  # 创建时间
    created_by = Column(String(50))  # Created by (admin username)
    used_at = Column(DateTime)  # 使用时间
    used_hardware_id = Column(String(64), ForeignKey("clients.hardware_id"))  # 使用的硬件ID
    generated_license_id = Column(Integer, ForeignKey("license_keys.id"))  # 生成的授权码ID
    parent_editor_license_id = Column(Integer, index=True)  # 绑定的上级编辑器授权码ID（执行器卡密可选）
    batch_id = Column(String(50))  # 批次ID，方便批量管理
    notes = Column(Text)  # 备注信息

    # 关系
    client = relationship("Client", foreign_keys=[used_hardware_id])
    license_key = relationship("LicenseKey", foreign_keys=[generated_license_id])

class SystemConfig(Base):
    """系统配置"""
    __tablename__ = "system_config"

    id = Column(Integer, primary_key=True, index=True)
    config_key = Column(String(100), unique=True, index=True, nullable=False)  # 配置键
    config_value = Column(Text, nullable=False)  # 配置值
    description = Column(Text)  # 配置说明
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # 更新时间
    updated_by = Column(String(50))  # 更新者

class SecondaryPassword(Base):
    """二级密码"""
    __tablename__ = "secondary_passwords"

    id = Column(Integer, primary_key=True, index=True)
    password_hash = Column(String(255), nullable=False)  # 二级密码哈希
    description = Column(Text)  # 密码说明
    created_at = Column(DateTime, default=func.now())
    created_by = Column(String(50))  # 创建
    is_active = Column(Boolean, default=True)  # 是否启用

class ClientSession(Base):
    """客户端在线会话表 - 用于限制硬件ID同时在线数量"""
    __tablename__ = "client_sessions"

    id = Column(Integer, primary_key=True, index=True)
    hardware_id = Column(String(64), index=True, nullable=False)  # 硬件ID
    license_key = Column(String(50), index=True, nullable=False)  # 许可证密钥
    session_token = Column(String(255), unique=True, index=True, nullable=False)  # 会话令牌
    created_at = Column(DateTime, default=func.now())  # 创建时间
    last_heartbeat = Column(DateTime, default=func.now())  # 最后心跳时间
    expires_at = Column(DateTime, nullable=False)  # 过期时间
    is_active = Column(Boolean, default=True)  # 是否活跃
    login_status = Column(String(20), default="offline")  # 登录状态: offline, online, authenticated
    client_info = Column(Text)  # Client info (JSON)

class ClientLoginHandshake(Base):
    """客户站录握手录表 - 用于追踪客户站录握手流"""
    __tablename__ = "client_login_handshakes"

    id = Column(Integer, primary_key=True, index=True)
    hardware_id = Column(String(64), index=True, nullable=False)  # 硬件ID
    session_token = Column(String(255), index=True, nullable=False)  # 会话令牌
    handshake_token = Column(String(255), unique=True, index=True, nullable=False)  # 握手令牌
    challenge = Column(String(255), nullable=False)  # 服务器发送的挑战值
    response = Column(String(255))  # 客户端的响应值
    handshake_status = Column(String(20), default="pending")  # 握手状态: pending, authenticated, failed, timeout
    created_at = Column(DateTime, default=func.now())  # 创建时间
    authenticated_at = Column(DateTime)  # 认证成功时间
    expires_at = Column(DateTime, nullable=False)  # 握手过期时间
    is_active = Column(Boolean, default=True)  # 是否有效


def is_client_online_update_enabled() -> bool:
    """Whether client online state writes are enabled."""
    return bool(_CLIENT_ONLINE_UPDATE_ENABLED)


def _client_online_fields_for_create() -> Dict[str, Any]:
    if not is_client_online_update_enabled():
        return {}
    return {"last_seen": func.now()}


def _touch_client_online(client: Optional[Client]) -> bool:
    if client is None or not is_client_online_update_enabled():
        return False
    client.last_seen = func.now()
    return True


def _set_client_session_online_status(session: Optional[ClientSession], login_status: str) -> bool:
    if session is None or not is_client_online_update_enabled():
        return False
    session.login_status = login_status
    return True


# 创建数据库表
def _normalize_market_update_server_base(base_url: Any) -> str:
    normalized = str(base_url or "").strip().rstrip("/")
    if normalized.lower().endswith("/market"):
        return normalized[:-7]
    return normalized


def get_market_update_server_base() -> str:
    env_value = _normalize_market_update_server_base(os.getenv("MARKET_UPDATE_SERVER_BASE", ""))
    if env_value:
        return env_value

    db = None
    try:
        db = SessionLocal()
        return _normalize_market_update_server_base(
            get_system_config(
                db,
                "market_update_server_base",
                _get_setting_default_raw("market_update_server_base"),
            )
        )
    except Exception:
        return ""
    finally:
        if db is not None:
            db.close()


def get_market_update_server_token() -> str:
    return str(os.getenv("MARKET_UPDATE_SERVER_TOKEN", "") or "").strip()


def promote_market_package_release(
    package_id: str,
    version: str,
    file_sha256: str = "",
    file_size: int = 0,
    storage_path: str = "",
) -> Dict[str, Any]:
    base_url = get_market_update_server_base()
    if not base_url:
        raise RuntimeError("market_update_server_base_not_configured")

    package_id_text = str(package_id or "").strip()
    version_text = str(version or "").strip()
    package_id_segment = quote(package_id_text, safe="")
    version_segment = quote(version_text, safe="")
    api_url = f"{base_url}/api/market/packages/{package_id_segment}/{version_segment}/release"

    headers: Dict[str, str] = {}
    token = get_market_update_server_token()
    if token:
        headers["X-Market-Update-Token"] = token

    payload = {
        "file_sha256": str(file_sha256 or "").strip(),
        "file_size": int(file_size or 0),
        "storage_path": str(storage_path or "").strip(),
    }
    response = requests.post(api_url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    result = response.json()
    if not isinstance(result, dict):
        raise RuntimeError("market_update_server_invalid_response")
    if result.get("success") is False:
        raise RuntimeError(str(result.get("detail") or result.get("message") or "market_update_server_release_failed"))
    return result


def delete_market_package_storage(package_id: str, version: str) -> Dict[str, Any]:
    base_url = get_market_update_server_base()
    package_id_text = str(package_id or "").strip()
    version_text = str(version or "").strip()
    if not base_url:
        return {"success": True, "package_id": package_id_text, "version": version_text}

    package_id_segment = quote(package_id_text, safe="")
    version_segment = quote(version_text, safe="")
    api_url = f"{base_url}/api/market/packages/{package_id_segment}/{version_segment}"

    headers: Dict[str, str] = {}
    token = get_market_update_server_token()
    if token:
        headers["X-Market-Update-Token"] = token

    response = requests.delete(api_url, headers=headers, timeout=30)
    if response.status_code == 404:
        return {"success": True, "package_id": package_id_text, "version": version_text}
    response.raise_for_status()
    result = response.json()
    if not isinstance(result, dict):
        raise RuntimeError("market_update_server_invalid_response")
    if result.get("success") is False:
        raise RuntimeError(str(result.get("detail") or result.get("message") or "market_update_server_delete_failed"))
    return result


def build_market_download_url(package_id: str, version: str) -> str:
    package_id_text = str(package_id or "").strip()
    version_text = str(version or "").strip()
    package_id_segment = quote(package_id_text, safe="")
    version_segment = quote(version_text, safe="")
    relative_path = f"/market/release/{package_id_segment}/{version_segment}/package.lca_market.zip"

    base_url = get_market_update_server_base()
    if not base_url:
        return relative_path
    return f"{base_url}{relative_path}"

def ensure_runtime_schema():
    """运时补齐关锭段，避免历史库缺列致服务崩"""
    try:
        inspector = inspect(engine)
        table_names = set(inspector.get_table_names())
        if "license_keys" not in table_names:
            return

        license_columns = {col["name"] for col in inspector.get_columns("license_keys")}
        alter_sqls = []

        if "parent_license_id" not in license_columns:
            alter_sqls.append("ALTER TABLE license_keys ADD COLUMN parent_license_id INTEGER")

        if "activation_cards" in table_names:
            card_columns = {col["name"] for col in inspector.get_columns("activation_cards")}
            if "parent_editor_license_id" not in card_columns:
                alter_sqls.append("ALTER TABLE activation_cards ADD COLUMN parent_editor_license_id INTEGER")

        if "market_packages" in table_names:
            market_package_columns = {col["name"] for col in inspector.get_columns("market_packages")}
            if "author_name" not in market_package_columns:
                alter_sqls.append("ALTER TABLE market_packages ADD COLUMN author_name VARCHAR(128) NOT NULL DEFAULT ''")
            if "owner_user_id" not in market_package_columns:
                alter_sqls.append("ALTER TABLE market_packages ADD COLUMN owner_user_id INTEGER")

        if "market_package_versions" in table_names:
            market_version_columns = {col["name"] for col in inspector.get_columns("market_package_versions")}
            if "protection_mode" not in market_version_columns:
                alter_sqls.append("ALTER TABLE market_package_versions ADD COLUMN protection_mode VARCHAR(64) NOT NULL DEFAULT ''")
            if "protection_payload_key" not in market_version_columns:
                alter_sqls.append("ALTER TABLE market_package_versions ADD COLUMN protection_payload_key TEXT NOT NULL DEFAULT ''")

        if alter_sqls:
            with engine.begin() as conn:
                for sql in alter_sqls:
                    conn.execute(text(sql))
            logger.info(f"数据库结构补齐完成，新字数量: {len(alter_sqls)}")
    except Exception as e:
        logger.error(f"数据库结构补齐失 {e}")
        raise


def _initialize_runtime_storage() -> None:
    global _RUNTIME_STORAGE_INITIALIZED

    with _RUNTIME_STORAGE_INIT_LOCK:
        if _RUNTIME_STORAGE_INITIALIZED:
            return

        _ensure_runtime_directories()
        Base.metadata.create_all(bind=engine)
        ensure_runtime_schema()
        _RUNTIME_STORAGE_INITIALIZED = True

# 依赖函数
def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)

def get_current_timestamp() -> int:
    """获取当前UTC时间戳（秒）"""
    return int(datetime.now(timezone.utc).timestamp())

def validate_client_timestamp(client_timestamp: int, tolerance: int = 300) -> Tuple[bool, str]:
    """
    Validate client timestamp.

    Args:
        client_timestamp: 客户端时间戳
        tolerance: 时间容差（

    Returns:
        (is_valid, error_message)
    """
    current_time = get_current_timestamp()
    time_diff = abs(current_time - client_timestamp)

    if time_diff > tolerance:
        return False, f"时间戳差异过大: {time_diff}秒，容差为{tolerance}秒"

    return True, ""


def validate_nonce_text(nonce: Any, min_len: int = 8, max_len: int = 128) -> bool:
    nonce_text = str(nonce or "").strip()
    if len(nonce_text) < int(min_len) or len(nonce_text) > int(max_len):
        return False
    return re.fullmatch(r"[0-9A-Za-z_-]+", nonce_text) is not None


def consume_request_nonce(scope: str, subject: str, nonce: str, ttl_seconds: int = _REQUEST_NONCE_DEFAULT_TTL_SECONDS) -> bool:
    """单次消费 nonce，返回 False 表示已使用（疑似重放）。"""
    scope_text = str(scope or "").strip().lower()
    subject_text = str(subject or "").strip()
    nonce_text = str(nonce or "").strip()
    if not scope_text or not subject_text or not nonce_text:
        return False

    now_ts = get_current_timestamp()
    expire_at = now_ts + max(30, int(ttl_seconds or _REQUEST_NONCE_DEFAULT_TTL_SECONDS))
    key_text = f"{scope_text}|{subject_text}|{nonce_text}"

    with _request_nonce_lock:
        if _request_nonce_expiry:
            expired_keys = [key for key, ts in _request_nonce_expiry.items() if int(ts or 0) <= now_ts]
            for expired_key in expired_keys:
                _request_nonce_expiry.pop(expired_key, None)

        if int(_request_nonce_expiry.get(key_text, 0) or 0) > now_ts:
            return False

        _request_nonce_expiry[key_text] = expire_at

        if len(_request_nonce_expiry) > _REQUEST_NONCE_MAX_RECORDS:
            overflow = len(_request_nonce_expiry) - _REQUEST_NONCE_MAX_RECORDS
            stale_keys = sorted(_request_nonce_expiry.items(), key=lambda item: int(item[1] or 0))[:overflow]
            for stale_key, _ in stale_keys:
                _request_nonce_expiry.pop(stale_key, None)

    return True

def generate_handshake_token() -> str:
    """生成握手令牌"""
    return secrets.token_urlsafe(32)

def generate_server_challenge() -> str:
    """生成服务器挑战"""
    return secrets.token_hex(32)

def generate_nonce() -> str:
    """生成nonce"""
    return secrets.token_hex(16)

def compute_handshake_hmac(
    handshake_token: str,
    hardware_id: str,
    server_timestamp: int,
    server_challenge: str,
    server_nonce: str,
    secret_key: str
) -> str:
    """
    计算握手令牌HMAC-SHA256签名

    Args:
        handshake_token: 握手令牌
        hardware_id: 硬件ID
        server_timestamp: 服务器时间戳
        server_challenge: 服务器挑
        server_nonce: 服务器nonce
        secret_key: 密钥

    Returns:
        HMAC-SHA256哈希值（十六进制
    """
    data = f"{handshake_token}|{hardware_id}|{server_timestamp}|{server_challenge}|{server_nonce}"
    return hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

def verify_handshake_hmac(
    handshake_token: str,
    hardware_id: str,
    server_timestamp: int,
    server_challenge: str,
    server_nonce: str,
    provided_hmac: str,
    secret_key: str
) -> bool:
    """
    验证握手令牌HMAC签名

    使用恒时间比较防止时序攻
    """
    expected_hmac = compute_handshake_hmac(
        handshake_token, hardware_id, server_timestamp,
        server_challenge, server_nonce, secret_key
    )
    return hmac.compare_digest(expected_hmac, provided_hmac)

def compute_client_response(
    server_challenge: str,
    license_key: str,
    server_nonce: str,
    client_nonce: str,
    server_timestamp: int,
    secret_key: str
) -> str:
    """
    Compute client handshake response HMAC-SHA256.

    Args:
        server_challenge: 服务器挑
        license_key: 许可证密钥
        server_nonce: 服务器nonce
        client_nonce: 客户端nonce
        server_timestamp: 服务器时间戳
        secret_key: 密钥

    Returns:
        客户端响应（HMAC-SHA256哈希值）
    """
    data = f"{server_challenge}|{license_key}|{server_nonce}|{client_nonce}|{server_timestamp}"
    return hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

def verify_client_response(
    server_challenge: str,
    license_key: str,
    server_nonce: str,
    client_nonce: str,
    server_timestamp: int,
    provided_response: str,
    secret_key: str
) -> bool:
    """
    Verify client handshake response.

    使用恒时间比较防止时序攻
    """
    expected_response = compute_client_response(
        server_challenge, license_key, server_nonce,
        client_nonce, server_timestamp, secret_key
    )
    return hmac.compare_digest(expected_response, provided_response)

def validate_hardware_id(hardware_id: str) -> bool:
    """验证硬件ID格式（SHA256）"""
    if not hardware_id or len(hardware_id) != 64:
        return False
    try:
        int(hardware_id, 16)  # 检查是否为有效的十六进制
        return True
    except ValueError:
        return False

def normalize_license_key_text(key: str) -> str:
    return str(key or "").strip().upper()


def extract_license_key_type(key: str) -> str:
    key_text = normalize_license_key_text(key)
    if not key_text:
        return ""

    editor_pattern = r'^ED-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}$'
    if re.match(editor_pattern, key_text, re.IGNORECASE):
        return "EDITOR"

    generic_pattern = r'^([A-Za-z][A-Za-z0-9_]*)-([0-9A-Fa-f]{32})$'
    matched = re.match(generic_pattern, key_text)
    if matched:
        return str(matched.group(1) or "").upper()

    return ""


def validate_license_key_format(key: str, expected_types: Optional[List[str]] = None) -> bool:
    """验证许可证密钥格"""
    key_type = extract_license_key_type(key)
    if not key_type:
        return False

    if not expected_types:
        return True

    allowed_types = {
        str(item or "").strip().upper()
        for item in expected_types
        if str(item or "").strip()
    }
    if not allowed_types:
        return True
    return key_type in allowed_types

def mask_sensitive_data(data: str, show_chars: int = 8) -> str:
    """達敏感数据"""
    if not data or len(data) <= show_chars:
        return "***"
    return f"{data[:show_chars]}***"

def format_beijing_time(dt: datetime) -> str:
    """Convert UTC time to Beijing time string."""
    if dt is None:
        return None

    # 纭繚鏄疷TC时间
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=pytz.UTC)

    # Convert to Beijing time
    beijing_time = dt.astimezone(BEIJING_TZ)

    return beijing_time.isoformat()

def get_system_config(db: Session, key: str, default: str = None) -> str:
    """获取系统配置"""
    # 强制从数捺重新加载配置,避免使用缓存的旧
    config = db.query(SystemConfig).filter(SystemConfig.config_key == key).first()
    if config:
        # 刷新对象以确保获取最新数
        db.refresh(config)
        return config.config_value
    return default

def set_system_config(db: Session, key: str, value: str, description: str = None, updated_by: str = None):
    """设置系统配置"""
    config = db.query(SystemConfig).filter(SystemConfig.config_key == key).first()
    if config:
        config.config_value = value
        config.updated_at = func.now()
        if description:
            config.description = description
        if updated_by:
            config.updated_by = updated_by
    else:
        config = SystemConfig(
            config_key=key,
            config_value=value,
            description=description,
            updated_by=updated_by
        )
        db.add(config)
    db.commit()
    return config


def _format_setting_storage_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _parse_bool_setting(value: Any, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = str(value or "").strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    return default


def _parse_int_setting(
    value: Any,
    default: int,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> int:
    try:
        parsed = int(str(value).strip())
    except Exception:
        parsed = default
    if minimum is not None:
        parsed = max(minimum, parsed)
    if maximum is not None:
        parsed = min(maximum, parsed)
    return parsed


def _require_int_setting(
    raw_value: Any,
    field_name: str,
    minimum: int,
    maximum: int,
) -> int:
    if isinstance(raw_value, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name}必须为整数",
        )
    try:
        value = int(str(raw_value).strip())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name}必须为整数",
        )
    if value < minimum or value > maximum:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name}必须在{minimum}到{maximum}之间",
        )
    return value


def _require_bool_setting(raw_value: Any, field_name: str) -> bool:
    if isinstance(raw_value, bool):
        return raw_value
    normalized = str(raw_value or "").strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"{field_name}必须为布尔值",
    )


def _get_setting_default_raw(setting_key: str) -> str:
    default_value = SYSTEM_SETTING_META[setting_key]["default"]
    return _format_setting_storage_value(default_value)


def get_runtime_system_settings(db: Session) -> Dict[str, Any]:
    server_name = str(
        get_system_config(
            db,
            "server_name",
            _get_setting_default_raw("server_name"),
        )
        or ""
    ).strip()
    if not server_name:
        server_name = str(SYSTEM_SETTING_META["server_name"]["default"])

    settings = {
        "server_name": server_name,
        "max_clients": _parse_int_setting(
            get_system_config(
                db,
                "max_clients",
                _get_setting_default_raw("max_clients"),
            ),
            int(SYSTEM_SETTING_META["max_clients"]["default"]),
            minimum=1,
            maximum=1000000,
        ),
        "session_timeout_minutes": _parse_int_setting(
            get_system_config(
                db,
                "session_timeout_minutes",
                _get_setting_default_raw("session_timeout_minutes"),
            ),
            int(SYSTEM_SETTING_META["session_timeout_minutes"]["default"]),
            minimum=5,
            maximum=1440,
        ),
        "enable_logging": _parse_bool_setting(
            get_system_config(
                db,
                "enable_logging",
                _get_setting_default_raw("enable_logging"),
            ),
            bool(SYSTEM_SETTING_META["enable_logging"]["default"]),
        ),
        "max_login_attempts": _parse_int_setting(
            get_system_config(
                db,
                "max_login_attempts",
                _get_setting_default_raw("max_login_attempts"),
            ),
            int(SYSTEM_SETTING_META["max_login_attempts"]["default"]),
            minimum=1,
            maximum=20,
        ),
        "lockout_duration_minutes": _parse_int_setting(
            get_system_config(
                db,
                "lockout_duration_minutes",
                _get_setting_default_raw("lockout_duration_minutes"),
            ),
            int(SYSTEM_SETTING_META["lockout_duration_minutes"]["default"]),
            minimum=1,
            maximum=1440,
        ),
        "enable_csrf": _parse_bool_setting(
            get_system_config(
                db,
                "enable_csrf",
                _get_setting_default_raw("enable_csrf"),
            ),
            bool(SYSTEM_SETTING_META["enable_csrf"]["default"]),
        ),
        "enable_rate_limit": _parse_bool_setting(
            get_system_config(
                db,
                "enable_rate_limit",
                _get_setting_default_raw("enable_rate_limit"),
            ),
            bool(SYSTEM_SETTING_META["enable_rate_limit"]["default"]),
        ),
        "market_update_server_base": str(
            get_system_config(
                db,
                "market_update_server_base",
                _get_setting_default_raw("market_update_server_base"),
            )
            or ""
        ).strip(),
    }
    return settings


def initialize_system_settings(db: Session) -> None:
    created_any = False
    for key, meta in SYSTEM_SETTING_META.items():
        exists = db.query(SystemConfig).filter(SystemConfig.config_key == key).first()
        if exists:
            continue
        created_any = True
        db.add(
            SystemConfig(
                config_key=key,
                config_value=_format_setting_storage_value(meta["default"]),
                description=str(meta["description"]),
                updated_by="system",
            )
        )
    if created_any:
        db.commit()


def apply_logging_setting(enable_logging: bool) -> None:
    level = logging.INFO if enable_logging else logging.WARNING
    logging.getLogger().setLevel(level)
    logger.setLevel(level)
    logging.getLogger("uvicorn.error").setLevel(level)


def refresh_runtime_flags(db: Session) -> Dict[str, Any]:
    settings = get_runtime_system_settings(db)
    with _runtime_flags_lock:
        _runtime_flags["enable_logging"] = bool(settings["enable_logging"])
        _runtime_flags["enable_csrf"] = bool(settings["enable_csrf"])
        _runtime_flags["enable_rate_limit"] = bool(settings["enable_rate_limit"])
    apply_logging_setting(bool(settings["enable_logging"]))
    return settings


def is_csrf_enabled(db: Session) -> bool:
    default_value = bool(SYSTEM_SETTING_META["enable_csrf"]["default"])
    return _parse_bool_setting(
        get_system_config(db, "enable_csrf", _get_setting_default_raw("enable_csrf")),
        default_value,
    )


def is_rate_limit_enabled() -> bool:
    with _runtime_flags_lock:
        return bool(_runtime_flags.get("enable_rate_limit", True))


def check_client_capacity_limit(db: Session) -> None:
    settings = get_runtime_system_settings(db)
    max_clients = int(settings["max_clients"])
    if max_clients <= 0:
        return
    total_clients = db.query(Client).count()
    if total_clients >= max_clients:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"客户端数量已达到上限({max_clients})，请联系管理员",
        )


def build_admin_settings_payload(db: Session) -> Dict[str, Any]:
    settings = get_runtime_system_settings(db)
    return {
        "serverName": settings["server_name"],
        "maxClients": settings["max_clients"],
        "sessionTimeout": settings["session_timeout_minutes"],
        "enableLogging": settings["enable_logging"],
        "maxLoginAttempts": settings["max_login_attempts"],
        "lockoutDuration": settings["lockout_duration_minutes"],
        "enableCSRF": settings["enable_csrf"],
        "enableRateLimit": settings["enable_rate_limit"],
        "marketUpdateServerBase": settings["market_update_server_base"],
    }

def is_license_validation_enabled(db: Session) -> bool:
    """查是否启用密钥验"""
    # 强制刷新会话以获取最新数
    db.expire_all()
    value = get_system_config(db, "license_validation_enabled", "true")
    return value.lower() == "true"


def get_executor_license_limit_per_hardware(db: Session) -> int:
    """Get executor license limit per hardware ID, 0 means unlimited."""
    raw_value = str(get_system_config(db, "executor_license_limit_per_hardware", "0") or "0").strip()
    try:
        limit = int(raw_value)
    except Exception:
        limit = 0
    return max(0, limit)


def get_editor_executor_limit(editor_license: Optional["LicenseKey"]) -> int:
    """获取某个编辑器授权码理的执器授权码数量上限"""
    if not editor_license:
        return 0
    try:
        limit = int(editor_license.max_activations or 0)
    except Exception:
        limit = 0
    return max(0, limit)


def resolve_license_key_type(db: Session, license_key: str, fallback_type: str = "") -> str:
    normalized_fallback = str(fallback_type or "").strip().upper()
    normalized_key = normalize_license_key_text(license_key)
    if not normalized_key:
        return normalized_fallback

    license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == normalized_key).first()
    if license_obj and str(license_obj.key_type or "").strip():
        return str(license_obj.key_type or "").strip().upper()

    parsed_type = extract_license_key_type(normalized_key)
    if parsed_type:
        return parsed_type.upper()

    return normalized_fallback


def is_editor_license_type(key_type: str) -> bool:
    return str(key_type or "").strip().upper() == "EDITOR"


def is_executor_license_type(key_type: str) -> bool:
    return str(key_type or "").strip().upper() == "EXECUTOR"


def count_active_managed_executor_licenses(
    db: Session,
    editor_license_id: int,
    exclude_license_id: Optional[int] = None,
) -> int:
    query = db.query(LicenseKey).filter(
        LicenseKey.parent_license_id == int(editor_license_id),
        func.upper(LicenseKey.key_type) == "EXECUTOR",
        LicenseKey.is_active == True,
        or_(LicenseKey.expires_at.is_(None), LicenseKey.expires_at > datetime.utcnow()),
    )
    if exclude_license_id:
        query = query.filter(LicenseKey.id != int(exclude_license_id))
    return int(query.count())


def resolve_editor_license(
    db: Session,
    editor_license_id: Optional[int] = None,
    editor_license_key: str = "",
) -> Optional["LicenseKey"]:
    """根据ID或密钥解析编辑器授权"""
    license_obj = None
    if editor_license_id is not None:
        try:
            editor_id = int(editor_license_id)
        except Exception:
            return None
        license_obj = db.query(LicenseKey).filter(LicenseKey.id == editor_id).first()
    elif str(editor_license_key or "").strip():
        key_text = normalize_license_key_text(editor_license_key)
        license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == key_text).first()

    if not license_obj:
        return None
    if not is_editor_license_type(license_obj.key_type):
        return None
    return license_obj


def require_active_editor_license_for_management(db: Session, editor_license_key: str) -> "LicenseKey":
    """校验父级编辑器授权码是否可用于子码管理。"""
    normalized_key = normalize_license_key_text(editor_license_key)
    if not normalized_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="父级编辑器授权码不能为空"
        )

    editor_license = resolve_editor_license(db, editor_license_key=normalized_key)
    if not editor_license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="父级编辑器授权码不存在或类型错误"
        )
    if not editor_license.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="父级编辑器授权码已禁用"
        )
    if editor_license.expires_at and editor_license.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="父级编辑器授权码已过期"
        )
    return editor_license


def compute_parent_scope_hash(parent_license_key: str) -> str:
    normalized_parent_key = normalize_license_key_text(parent_license_key)
    if not validate_license_key_format(normalized_parent_key, expected_types=["EDITOR"]):
        return ""
    sign_source = f"PARENT_SCOPE|{normalized_parent_key}"
    return hashlib.sha256(sign_source.encode("utf-8")).hexdigest().lower()


def resolve_parent_scope_hash(request: Request, data: Optional[Dict[str, Any]] = None) -> str:
    """从请求体/请求头提取父级授权范围哈希。"""
    payload = data if isinstance(data, dict) else {}

    hash_candidates = [
        payload.get("parent_scope_hash"),
        request.headers.get("X-Parent-Scope-Hash"),
    ]
    for raw_value in hash_candidates:
        candidate_hash = str(raw_value or "").strip().lower()
        if re.fullmatch(r"[0-9a-f]{64}", candidate_hash):
            return candidate_hash
    return ""


def enforce_executor_parent_scope_hash(
    db: Session,
    license_obj: Optional["LicenseKey"],
    expected_scope_hash: str,
) -> tuple[bool, int, str]:
    """强制校验执行器授权码所属父级范围哈希。"""
    normalized_scope_hash = str(expected_scope_hash or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", normalized_scope_hash):
        return False, status.HTTP_400_BAD_REQUEST, "父级授权范围参数无效"

    if not license_obj:
        return False, status.HTTP_404_NOT_FOUND, "许可证不存在"

    key_type = str(license_obj.key_type or "").strip().upper()
    if not is_executor_license_type(key_type):
        return False, status.HTTP_403_FORBIDDEN, "仅执行器授权码支持父级范围校验"

    if not license_obj.parent_license_id:
        return False, status.HTTP_403_FORBIDDEN, "执行器授权码未关联父级编辑器授权码"

    parent_editor = resolve_editor_license(db, editor_license_id=license_obj.parent_license_id)
    if not parent_editor:
        return False, status.HTTP_403_FORBIDDEN, "执行器授权码父级编辑器不存在"

    actual_scope_hash = compute_parent_scope_hash(parent_editor.key_string)
    if not actual_scope_hash:
        return False, status.HTTP_403_FORBIDDEN, "父级编辑器授权范围计算失败"
    if not hmac.compare_digest(actual_scope_hash, normalized_scope_hash):
        scope_fingerprint = actual_scope_hash[:8]
        return (
            False,
            status.HTTP_403_FORBIDDEN,
            f"子授权码不在导出授权范围内（所属父级ID:{int(parent_editor.id)}，范围指纹:{scope_fingerprint}）",
        )

    return True, status.HTTP_200_OK, ""


def enforce_license_binding_policy(db: Session, license_obj: LicenseKey, hardware_id: str) -> tuple[bool, int, str]:
    """统一的授权绑定策略"""
    if not license_obj:
        return False, status.HTTP_404_NOT_FOUND, "许可证不存在"

    if license_obj.client_hardware_id and license_obj.client_hardware_id != hardware_id:
        return False, status.HTTP_401_UNAUTHORIZED, "许可证已绑定到其他硬件ID"

    key_type = str(license_obj.key_type or "").strip().upper()

    if is_editor_license_type(key_type):
        existing_editor = db.query(LicenseKey).filter(
            LicenseKey.client_hardware_id == hardware_id,
            func.upper(LicenseKey.key_type) == "EDITOR",
            LicenseKey.id != license_obj.id,
            LicenseKey.is_active == True,
            or_(LicenseKey.expires_at.is_(None), LicenseKey.expires_at > datetime.utcnow()),
        ).first()
        if existing_editor:
            return False, status.HTTP_409_CONFLICT, "该硬件ID已绑定其他编辑器授权码"
        return True, status.HTTP_200_OK, ""

    if is_executor_license_type(key_type):
        if not license_obj.parent_license_id:
            return False, status.HTTP_409_CONFLICT, "执行器授权码未关联上级编辑器授权码"
        parent_editor = db.query(LicenseKey).filter(
            LicenseKey.id == int(license_obj.parent_license_id)
        ).first()
        if not parent_editor:
            return False, status.HTTP_409_CONFLICT, "上级编辑器授权码不存在"
        if not is_editor_license_type(parent_editor.key_type):
            return False, status.HTTP_409_CONFLICT, "上级授权码类型错误，必须是编辑器授权码"
        if not parent_editor.is_active:
            return False, status.HTTP_403_FORBIDDEN, "上级编辑器授权码已禁用"
        if parent_editor.expires_at and parent_editor.expires_at < datetime.utcnow():
            return False, status.HTTP_403_FORBIDDEN, "上级编辑器授权码已过期"
        return True, status.HTTP_200_OK, ""

    return True, status.HTTP_200_OK, ""

def cleanup_expired_sessions(db: Session):
    """清理过期的户会话"""
    try:
        expired_count = db.query(ClientSession).filter(
            ClientSession.expires_at < datetime.utcnow(),
            ClientSession.is_active == True
        ).update({"is_active": False})
        if expired_count > 0:
            db.commit()
            logger.info(f"清理{expired_count} 丿期户会话")
    except Exception as e:
        db.rollback()
        logger.error(f"清理过期会话失败: {e}")

def cleanup_expired_handshakes(db: Session):
    """清理过期的握手"""
    try:
        expired_count = db.query(ClientLoginHandshake).filter(
            ClientLoginHandshake.expires_at < datetime.utcnow(),
            ClientLoginHandshake.is_active == True,
            ClientLoginHandshake.handshake_status == "pending"
        ).update({"is_active": False, "handshake_status": "timeout"})
        if expired_count > 0:
            db.commit()
            logger.info(f"清理了 {expired_count} 个过期握手记录")
    except Exception as e:
        db.rollback()
        logger.error(f"清理过期握手记录失败: {e}")

def check_hardware_id_online_limit(
    db: Session,
    hardware_id: str,
    license_key: str = "",
    license_type: str = "",
) -> tuple[bool, str]:
    """
    Check whether hardware ID exceeds online limit.
    Returns: (is_limited, reason)
    """
    try:
        # 清理过期会话
        cleanup_expired_sessions(db)

        resolved_type = resolve_license_key_type(db, license_key, license_type)
        if not resolved_type:
            return False, ""
        if resolved_type and not is_editor_license_type(resolved_type):
            # Executor licenses do not limit concurrent sessions for the same hardware ID.
            return False, ""

        # 查询该硬件ID的活跃会话数
        active_sessions = db.query(ClientSession).filter(
            ClientSession.hardware_id == hardware_id,
            ClientSession.is_active == True,
            ClientSession.expires_at > datetime.utcnow()
        ).all()

        if not active_sessions:
            return False, ""

        session_keys = [normalize_license_key_text(session.license_key) for session in active_sessions if session.license_key]
        type_map: Dict[str, str] = {}
        if session_keys:
            for key_string, key_type in db.query(LicenseKey.key_string, LicenseKey.key_type).filter(
                LicenseKey.key_string.in_(session_keys)
            ).all():
                key_text = normalize_license_key_text(key_string)
                if key_text:
                    type_map[key_text] = str(key_type or "").strip().upper()

        for session in active_sessions:
            session_key = normalize_license_key_text(session.license_key)
            session_type = type_map.get(session_key) or extract_license_key_type(session_key)
            if is_editor_license_type(session_type):
                return True, f"该硬件ID已存在编辑器在线会话，会话令 {session.session_token[:16]}..."

        return False, ""
    except Exception as e:
        logger.error(f"查在线限制失 {e}")
        return False, ""

def create_client_session(db: Session, hardware_id: str, license_key: str, client_info: Dict = None) -> str:
    """
    Create client session.
    返回: 会话令牌
    """
    try:
        key_text = normalize_license_key_text(license_key)
        resolved_type = resolve_license_key_type(db, key_text)

        session_token = secrets.token_urlsafe(32)
        expires_at = datetime.utcnow() + timedelta(hours=24)  # 24小时过期

        if is_editor_license_type(resolved_type):
            active_sessions = db.query(ClientSession).filter(
                ClientSession.hardware_id == hardware_id,
                ClientSession.is_active == True
            ).all()

            session_keys = [normalize_license_key_text(item.license_key) for item in active_sessions if item.license_key]
            key_type_map: Dict[str, str] = {}
            if session_keys:
                for key_string, key_type in db.query(LicenseKey.key_string, LicenseKey.key_type).filter(
                    LicenseKey.key_string.in_(session_keys)
                ).all():
                    normalized = normalize_license_key_text(key_string)
                    if normalized:
                        key_type_map[normalized] = str(key_type or "").strip().upper()

            for session in active_sessions:
                session_key = normalize_license_key_text(session.license_key)
                session_type = key_type_map.get(session_key) or extract_license_key_type(session_key)
                if is_editor_license_type(session_type):
                    session.is_active = False
        else:
            # Executor licenses can coexist; replace only same hardware ID + same license session.
            db.query(ClientSession).filter(
                ClientSession.hardware_id == hardware_id,
                ClientSession.license_key == key_text,
                ClientSession.is_active == True
            ).update({"is_active": False}, synchronize_session=False)

        # 创建新会话
        session = ClientSession(
            hardware_id=hardware_id,
            license_key=key_text,
            session_token=session_token,
            expires_at=expires_at,
            is_active=True,
            client_info=json.dumps(client_info) if client_info else None
        )

        db.add(session)
        db.commit()
        logger.info(f"Create client session {mask_sensitive_data(hardware_id)} - token: {session_token[:16]}...")
        return session_token
    except Exception as e:
        db.rollback()
        logger.error(f"Create client session failed {e}")
        return None

def verify_client_session(db: Session, session_token: str) -> Optional[ClientSession]:
    """
    Verify client session.
    返回: 会话对象或None
    """
    try:
        session = db.query(ClientSession).filter(
            ClientSession.session_token == session_token,
            ClientSession.is_active == True,
            ClientSession.expires_at > datetime.utcnow()
        ).first()

        if session:
            # 更新后心跳时
            session.last_heartbeat = func.now()
            db.commit()
            return session

        return None
    except Exception as e:
        logger.error(f"Verify client session failed {e}")
        return None

def invalidate_client_session(db: Session, session_token: str):
    """
    使户会话失效
    """
    try:
        db.query(ClientSession).filter(
            ClientSession.session_token == session_token
        ).update({"is_active": False})
        db.commit()
        logger.info(f"使客户端会话失效: 令牌 {session_token[:16]}...")
    except Exception as e:
        db.rollback()
        logger.error(f"使会话失效失 {e}")


def build_runtime_bundle_key(
    hardware_id: str,
    session_token: str,
    license_key: str,
    request_nonce: str,
    issued_at: int,
) -> str:
    source = f"{hardware_id}|{session_token}|{license_key}|{request_nonce}|{issued_at}"
    return hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def build_export_runtime_key(seed_digest: str, expire_at: int) -> str:
    source = f"EXPORT|{seed_digest}|{expire_at}"
    return hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

def is_hardware_id_banned(db: Session, hardware_id: str) -> tuple[bool, str]:
    """
    Check whether hardware ID is banned.
    Returns: (is_banned, ban_reason)
    """
    if not hardware_id:
        return False, ""

    banned_record = db.query(BannedHardwareId).filter(
        BannedHardwareId.hardware_id == hardware_id,
        BannedHardwareId.is_active == True
    ).first()

    if not banned_record:
        return False, ""

    # 查是否有过期时间且已过期
    if banned_record.expires_at and banned_record.expires_at < datetime.utcnow():
        # 封已过期，臊解除
        banned_record.is_active = False
        db.commit()
        return False, ""

    return True, banned_record.reason or "硬件ID已被封禁"

def generate_editor_license_key() -> str:
    """生成编辑器可密钥"""
    # 生成ED-开头的编辑器密钥格式: ED-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX
    key_parts = ['ED']
    for _ in range(6):
        key_parts.append(secrets.token_hex(2).upper())
    return '-'.join(key_parts)


def generate_license_key_by_type(key_type: str) -> str:
    """根据授权码类型生成密钥。"""
    normalized_type = str(key_type or "").strip().upper()
    if normalized_type == "EDITOR":
        return generate_editor_license_key()
    if not normalized_type:
        normalized_type = "LICENSE"
    return f"{normalized_type}-{secrets.token_hex(16).upper()}"

def generate_activation_card_code() -> str:
    """生成活卡密代"""
    # 格式: CARD-XXXXXXXX-XXXXXXXX-XXXXXXXX (每段8个字符，容易输入)
    code_parts = ['CARD']
    for _ in range(3):
        code_parts.append(secrets.token_hex(4).upper())  # 4字节=8个16进制字符
    return '-'.join(code_parts)

def generate_session_token() -> str:
    """生成会话令牌"""
    return secrets.token_urlsafe(32)


def mark_secondary_delete_verified(session_token: str) -> None:
    if not session_token:
        return
    with _secondary_delete_verified_lock:
        _secondary_delete_verified_sessions[session_token] = datetime.utcnow()


def clear_secondary_delete_verified(session_token: str) -> None:
    if not session_token:
        return
    with _secondary_delete_verified_lock:
        _secondary_delete_verified_sessions.pop(session_token, None)


def is_secondary_delete_verified(session_token: str) -> bool:
    if not session_token:
        return False
    with _secondary_delete_verified_lock:
        return session_token in _secondary_delete_verified_sessions


def create_admin_session(db: Session, user_id: int, ip_address: str = None, user_agent: str = None) -> str:
    """Create admin session (in-memory storage)."""
    session_token = generate_session_token()
    token_key = _session_token_key(session_token)
    settings = get_runtime_system_settings(db)
    session_timeout_minutes = int(settings["session_timeout_minutes"])
    expires_at = datetime.utcnow() + timedelta(minutes=session_timeout_minutes)

    with _session_lock:
        _admin_sessions[token_key] = {
            "user_id": user_id,
            "expires_at": expires_at,
            "ip_address": ip_address,
            "user_agent": user_agent,
            "created_at": datetime.utcnow()
        }

    # Persist to file
    _save_sessions()
    clear_secondary_delete_verified(session_token)

    return session_token

def verify_admin_session(db: Session, session_token: str) -> User:
    """Verify admin session (in-memory storage)."""
    if not session_token:
        return None
    token_key = _session_token_key(session_token)
    if not token_key:
        return None

    with _session_lock:
        session_data = _admin_sessions.get(token_key)

    if not session_data:
        return None

    # Check expiration
    if session_data["expires_at"] < datetime.utcnow():
        with _session_lock:
            _admin_sessions.pop(token_key, None)
        clear_secondary_delete_verified(session_token)
        _save_sessions()
        return None

    # Query user
    user = db.query(User).filter(
        User.id == session_data["user_id"],
        User.is_admin == True
    ).first()
    if not user:
        with _session_lock:
            _admin_sessions.pop(token_key, None)
        clear_secondary_delete_verified(session_token)
        _save_sessions()
        return None

    return user

def get_current_admin_user(request: Request, db: Session = Depends(get_db)):
    """Get current admin user (dependency injection)."""
    return require_admin_auth(request, db)

def require_admin_auth(request: Request, db: Session = Depends(get_db)):
    """Admin authentication dependency."""
    session_token = request.cookies.get("admin_session")

    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="需要管理员权限"
        )

    return user




def _cleanup_market_author_sessions() -> None:
    now = datetime.utcnow()
    expired_keys = []
    with _market_author_session_lock:
        for token_key, session_data in list(_market_author_sessions.items()):
            expires_at = session_data.get("expires_at") if isinstance(session_data, dict) else None
            if not isinstance(expires_at, datetime) or expires_at <= now:
                expired_keys.append(token_key)
        for token_key in expired_keys:
            _market_author_sessions.pop(token_key, None)


def create_market_author_session(user_id: int, ip_address: str = None, user_agent: str = None) -> tuple[str, int]:
    session_token = generate_session_token()
    token_key = _session_token_key(session_token)
    expires_at = datetime.utcnow() + timedelta(seconds=_MARKET_AUTHOR_SESSION_TTL_SECONDS)
    with _market_author_session_lock:
        _market_author_sessions[token_key] = {
            "user_id": int(user_id),
            "expires_at": expires_at,
            "ip_address": ip_address,
            "user_agent": user_agent,
            "created_at": datetime.utcnow(),
        }
    return session_token, _MARKET_AUTHOR_SESSION_TTL_SECONDS


def revoke_market_author_session(session_token: str) -> None:
    token_key = _session_token_key(session_token)
    if not token_key:
        return
    with _market_author_session_lock:
        _market_author_sessions.pop(token_key, None)


def verify_market_author_session(db: Session, session_token: str) -> Optional[User]:
    if not session_token:
        return None
    token_key = _session_token_key(session_token)
    if not token_key:
        return None
    _cleanup_market_author_sessions()
    with _market_author_session_lock:
        session_data = _market_author_sessions.get(token_key)
    if not isinstance(session_data, dict):
        return None
    expires_at = session_data.get("expires_at")
    if not isinstance(expires_at, datetime) or expires_at <= datetime.utcnow():
        revoke_market_author_session(session_token)
        return None
    user_id = int(session_data.get("user_id", 0) or 0)
    if user_id <= 0:
        revoke_market_author_session(session_token)
        return None
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        revoke_market_author_session(session_token)
        return None
    return user


def _extract_bearer_token(request: Request) -> str:
    auth_header = str(request.headers.get("Authorization") or "").strip()
    if not auth_header or not auth_header.startswith("Bearer "):
        return ""
    return str(auth_header[7:] or "").strip()


def require_market_author_auth(request: Request, db: Session = Depends(get_db), required: bool = True):
    session_token = _extract_bearer_token(request)
    if not session_token:
        if required:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="\u9700\u8981\u4f5c\u8005\u767b\u5f55")
        return None
    user = verify_market_author_session(db, session_token)
    if not user:
        if required:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="\u4f5c\u8005\u4f1a\u8bdd\u65e0\u6548\u6216\u5df2\u8fc7\u671f")
        return None
    return user


def _build_market_author_auth_response(user: User, session_token: str, expires_in: int) -> MarketAuthorAuthResponse:
    return MarketAuthorAuthResponse(
        success=True,
        access_token=session_token,
        token_type="bearer",
        expires_in=int(expires_in or 0),
        user=MarketAuthorProfile(
            id=int(user.id),
            username=str(user.username or ""),
            is_admin=bool(user.is_admin),
        ),
    )


def should_use_secure_cookie(request: Request) -> bool:
    """根据请求协议判断是否应设置Secure Cookie。"""
    try:
        if str(request.url.scheme or "").lower() == "https":
            return True
    except Exception:
        pass

    forwarded_proto = str(request.headers.get("x-forwarded-proto", "") or "").strip().lower()
    if not forwarded_proto:
        return False
    proto = forwarded_proto.split(",")[0].strip()
    return proto == "https"


def _read_last_lines(file_path: str, max_lines: int) -> List[str]:
    """以内存友好的方式读取文件尾部N行。"""
    if max_lines <= 0:
        return []
    tail = deque(maxlen=max_lines)
    with open(file_path, "r", encoding="utf-8", errors="replace") as file_obj:
        for line in file_obj:
            tail.append(line)
    return list(tail)

# 应用生命周期管理
@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    _configure_server_logging()
    _initialize_runtime_storage()
    logger.info("正在启动JW3授权验证服务端...")

    # 加载管理员会话
    _load_sessions()

    # 初始化管理员账户与许可证验证配置
    db = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == ADMIN_USERNAME).first()
        if not admin_user:
            logger.info(f"创建初始管理员账户: {ADMIN_USERNAME}")
            admin_user = User(
                username=ADMIN_USERNAME,
                password_hash=get_password_hash(ADMIN_PASSWORD),
                is_admin=True
            )
            db.add(admin_user)
            db.commit()
            logger.info("初始管理员账户创建成功")
        else:
            logger.info(f"管理员账户已存在: {admin_user.username}")

        license_config = db.query(SystemConfig).filter(
            SystemConfig.config_key == "license_validation_enabled"
        ).first()
        if not license_config:
            logger.info("初始化许可证验证配置，默认启用")
            license_config = SystemConfig(
                config_key="license_validation_enabled",
                config_value="true",
                description="控制是否启用客户端许可证密钥验证",
                updated_by="system"
            )
            db.add(license_config)
            db.commit()
            logger.info("许可证验证配置初始化成功")
        else:
            logger.info(f"许可证验证配置已存在: {license_config.config_value}")

        initialize_system_settings(db)
        refresh_runtime_flags(db)

    except Exception as e:
        logger.error(f"初始化失败: {e}")
        db.rollback()
    finally:
        db.close()

    logger.info("JW3授权验证服务端启动完成")

    # 清理过期握手记录和会话
    cleanup_db = SessionLocal()
    try:
        cleanup_expired_sessions(cleanup_db)
        cleanup_expired_handshakes(cleanup_db)
    finally:
        cleanup_db.close()

    yield
    logger.info("JW3授权验证服务端正在关闭...")

# 创建FastAPI应用
app = FastAPI(
    title="JW3 授权验证服务端",
    description="专为客户端量身定制的授权验证系统",
    version=APP_VERSION,
    lifespan=lifespan
)

# 添加丗
# 添加Gzip压缩丗
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,  # 使用配置的来源列表
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    max_age=60 * 60 * 24,  # 24小时
)


app.include_router(
    build_market_router(
        get_db,
        MARKET_MODELS,
        build_download_url=build_market_download_url,
        admin_guard=require_admin_auth,
        release_package=promote_market_package_release,
        author_guard=require_market_author_auth,
        encrypt_payload_key=encrypt_market_payload_key,
        decrypt_payload_key=decrypt_market_payload_key,
        sign_upload_ticket=build_market_upload_ticket,
        delete_package_storage=delete_market_package_storage,
    )
)


@app.middleware("http")
async def api_rate_limit_middleware(request: Request, call_next):
    path = request.url.path or ""
    if (
        not path.startswith("/api/")
        or path.startswith("/api/admin/logs")
        or path in _RATE_LIMIT_EXCLUDED_PATHS
    ):
        return await call_next(request)

    if not is_rate_limit_enabled():
        return await call_next(request)

    client_ip = get_client_ip(request)
    bucket_key = f"{client_ip}:{path}"
    now_ts = time.time()
    allowed = True
    retry_after = 1

    with _rate_limit_lock:
        timestamps = _rate_limit_records.get(bucket_key, [])
        min_ts = now_ts - _RATE_LIMIT_WINDOW_SECONDS
        timestamps = [ts for ts in timestamps if ts >= min_ts]

        if len(timestamps) >= _RATE_LIMIT_MAX_REQUESTS:
            allowed = False
            if timestamps:
                retry_after = max(1, int(_RATE_LIMIT_WINDOW_SECONDS - (now_ts - timestamps[0])))
        else:
            timestamps.append(now_ts)
            _rate_limit_records[bucket_key] = timestamps

        # 控制内存增长：当记录较多时清理过期桶
        if len(_rate_limit_records) > 5000:
            stale_keys = []
            for key, key_timestamps in _rate_limit_records.items():
                if not any(ts >= min_ts for ts in key_timestamps):
                    stale_keys.append(key)
            for key in stale_keys:
                _rate_limit_records.pop(key, None)

    if not allowed:
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={
                "success": False,
                "detail": "请求过于频繁，请稍后重试",
            },
            headers={"Retry-After": str(retry_after)},
        )

    return await call_next(request)


# 添加缓存头中间件
@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)

    # 静资源缓
    if request.url.path.startswith("/static/"):
        # 静资源缓骞
        response.headers["Cache-Control"] = "public, max-age=31536000"
        # 动算过期时
        expires_time = datetime.utcnow() + timedelta(days=365)
        response.headers["Expires"] = expires_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

        # 设置字体文件的CORS头，允跨域访问
        if request.url.path.endswith(('.woff', '.woff2', '.ttf', '.eot')):
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "GET"

    # API响应缓存 - 敏感API不缓
    elif request.url.path.startswith("/api/"):
        # Authorization APIs must never be cached by browsers, proxies, or CDNs.
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0, s-maxage=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers["Surrogate-Control"] = "no-store"
        existing_vary = response.headers.get("Vary")
        vary_values = [value.strip() for value in str(existing_vary or "").split(",") if value.strip()]
        for vary_item in ("Authorization", "Cookie"):
            if not any(value.lower() == vary_item.lower() for value in vary_values):
                vary_values.append(vary_item)
        if vary_values:
            response.headers["Vary"] = ", ".join(vary_values)

    # HTML页面缓存
    elif request.url.path.endswith(('.html', '/')) or 'text/html' in response.headers.get('content-type', ''):
        # 管理页面不缓
        if '/admin' in request.url.path or '/login' in request.url.path or '/parent/licenses' in request.url.path:
            response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
        else:
            # 其他HTML页面缓存1小时
            response.headers["Cache-Control"] = "public, max-age=3600"

    return response

# 静文件和模板
app.mount("/static", StaticFiles(directory=STATIC_DIR, check_dir=False), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 安全认证
security = HTTPBearer()

# API路由
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """健康查"""
    now_utc = datetime.now(timezone.utc)
    uptime_seconds = max(0, int(time.monotonic() - SERVER_START_MONOTONIC))
    db_type = detect_database_type(DATABASE_URL)
    try:
        # 检查数据库连接
        db.execute(text("SELECT 1"))
        settings = get_runtime_system_settings(db)
        user_count = db.query(User).count()
        client_count = db.query(Client).count()
        license_count = db.query(LicenseKey).count()

        return {
            "server_name": settings["server_name"],
            "status": "正常",
            "database": "已连接",
            "database_connected": True,
            "database_type": db_type,
            "statistics": {
                "users": user_count,
                "clients": client_count,
                "licenses": license_count
            },
            "startup_time": SERVER_START_TIME_UTC.isoformat(),
            "uptime_seconds": uptime_seconds,
            "timestamp": now_utc.isoformat(),
            "server_time": now_utc.isoformat(),
            "version": app.version,
            "python_version": sys.version.split()[0],
            "fastapi_version": fastapi_version,
        }
    except Exception as e:
        logger.error(f"健康查失 {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "异常",
                "database": "异常",
                "database_connected": False,
                "database_type": db_type,
                "error": str(e),
                "startup_time": SERVER_START_TIME_UTC.isoformat(),
                "uptime_seconds": uptime_seconds,
                "timestamp": now_utc.isoformat(),
                "server_time": now_utc.isoformat(),
                "version": app.version,
                "python_version": sys.version.split()[0],
                "fastapi_version": fastapi_version,
            }
        )

@app.get("/api/get_csrf_for_client")
async def get_csrf_token(request: Request):
    """为客户端获取CSRF token"""
    csrf_token = generate_client_csrf_token()
    request.session["csrf_token"] = csrf_token

    return {
        "csrf_token": csrf_token,
        "expires_in": _CLIENT_CSRF_TOKEN_TTL_SECONDS,
        "message": "CSRF token generated successfully"
    }

@app.post("/api/v2/client/register")
async def register_client_v2(request: Request, db: Session = Depends(get_db)):
    """客户端注册API - v2版本，增强的安全性和状态同步"""

    if is_csrf_enabled(db):
        validate_client_registration_csrf(request, "v2")

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get('hardware_id')
    client_info = data.get('client_info', {})
    timestamp = data.get('timestamp')
    client_version = data.get('client_version', 'unknown')

    if not hardware_id or not validate_hardware_id(hardware_id):
        logger.warning(f"v2客户端注册失败: 无效的硬件ID格式 {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # 验证时间戳
    if timestamp:
        try:
            client_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            server_time = datetime.now(pytz.utc)
            time_diff = abs((server_time - client_time).total_seconds())
            if time_diff > 300:  # 5分钟
                logger.warning(f"v2客户端注册: 时间戳差异较大 ({time_diff}秒)")
        except ValueError:
            logger.warning("v2客户端注册: 时间戳格式无效")

    # 检查硬件ID是否被封禁
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"v2客户端注册失败: 硬件ID已被封禁 {mask_sensitive_data(hardware_id)} - {ban_reason}")
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "success": False,
                "error_code": "HARDWARE_BANNED",
                "is_banned": True,
                "message": f"硬件ID已被封禁: {ban_reason}"
            }
        )

    # 强制刷新配置状态
    license_validation_enabled = is_license_validation_enabled(db)

    # 检查客户端是否已存在
    existing_client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if existing_client:
        # 更新最后活动时间和客户端信息
        _touch_client_online(existing_client)
        if client_info:
            existing_client.client_info = json.dumps(client_info)
        db.commit()
        logger.info(f"v2客户端已存在，更新信息: {mask_sensitive_data(hardware_id)} - 版本: {client_version}")
        return {
            "success": True,
            "message": "客户端已注册",
            "already_registered": True,
            "is_banned": False,
            "license_validation_enabled": license_validation_enabled,
            "server_time": datetime.now(pytz.utc).isoformat(),
            "api_version": "2.0"
        }

    check_client_capacity_limit(db)

    # 创建新客户端
    new_client = Client(
        hardware_id=hardware_id,
        client_info=json.dumps(client_info),
        **_client_online_fields_for_create(),
    )

    try:
        db.add(new_client)
        db.commit()
        logger.info(f"v2新客户端注册成功: {mask_sensitive_data(hardware_id)} - 版本: {client_version}")
        return {
            "success": True,
            "message": "客户端注册成功",
            "already_registered": False,
            "is_banned": False,
            "license_validation_enabled": license_validation_enabled,
            "server_time": datetime.now(pytz.utc).isoformat(),
            "api_version": "2.0"
        }
    except Exception as e:
        db.rollback()
        logger.error(f"v2客户端注册失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="客户端注册失败"
        )

@app.post("/api/licensing/register_client")
async def register_client_v1(request: Request, db: Session = Depends(get_db)):
    """
    V1 client registration endpoint (full version).

    Keeps backward compatibility with legacy client response behavior.
    Includes CSRF check, timestamp validation, and ban checks.
    """
    if is_csrf_enabled(db):
        validate_client_registration_csrf(request, "v1")

    # 2. 解析请求数据
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get('hardware_id')
    timestamp = data.get('timestamp')  # V1可能包含时间戳

    # 3. 验证硬件ID格式
    if not hardware_id or not validate_hardware_id(hardware_id):
        logger.warning(f"v1客户端注册失败: 无效的硬件ID格式 {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # 4. 时间戳验证（如果提供
    if timestamp:
        try:
            client_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            server_time = datetime.now(pytz.utc)
            time_diff = abs((server_time - client_time).total_seconds())
            if time_diff > 300:  # 5分钟
                logger.warning(f"v1客户端注册: 时间戳差异较大 ({time_diff}秒)")
        except ValueError:
            logger.warning("v1客户端注册: 时间戳格式无效")

    # 5. Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"v1客户端注册失败: 硬件ID已被封禁 {mask_sensitive_data(hardware_id)} - {ban_reason}")
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "success": False,
                "is_banned": True,
                "ban_reason": ban_reason,
                "error": f"硬件ID已被封禁: {ban_reason}"
            }
        )

    # 6. 强制刷新配置状
    license_validation_enabled = is_license_validation_enabled(db)

    # 7. Check whether client already exists
    existing_client = db.query(Client).filter(Client.hardware_id == hardware_id).first()

    if existing_client:
        # Update last activity time and client info
        _touch_client_online(existing_client)
        # V1可能包含简单的client_info
        client_info = data.get('client_info', {})
        if client_info:
            existing_client.client_info = json.dumps(client_info)
        db.commit()
        logger.info(f"v1 client exists, updating info {mask_sensitive_data(hardware_id)}")

        # V1响应格式 - 使用409表示已存
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "success": True,
                "message": "客户端已注册",
                "is_banned": False,
                "license_validation_enabled": license_validation_enabled,
                "server_time": datetime.now(pytz.utc).isoformat()
            }
        )

    check_client_capacity_limit(db)

    # 8. 创建新客户端
    client_info = data.get('client_info', {})
    new_client = Client(
        hardware_id=hardware_id,
        client_info=json.dumps(client_info) if client_info else json.dumps({}),
        **_client_online_fields_for_create(),
    )

    try:
        db.add(new_client)
        db.commit()
        logger.info(f"v1新客户端注册成功: {mask_sensitive_data(hardware_id)}")

        # V1响应格式 - 使用201表示新注
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "客户端注册成功",
                "is_banned": False,
                "license_validation_enabled": license_validation_enabled,
                "server_time": datetime.now(pytz.utc).isoformat()
            }
        )
    except Exception as e:
        db.rollback()
        logger.error(f"v1客户端注册失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Client registration failed"
        )

@app.get("/api/ping_auth")
async def ping_auth(request: Request, db: Session = Depends(get_db)):
    """主的证- 兼客户"""
    # 获取认证信息
    hardware_id = request.headers.get('X-Hardware-ID')
    auth_header = request.headers.get('Authorization')
    expected_parent_scope_hash = resolve_parent_scope_hash(request)

    if not hardware_id or not auth_header:
        logger.warning("认证失败: 缺少必要的认证头部")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="缺少认证信息"
        )

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        logger.warning(f"认证失败: 无效的硬件ID格式 {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的硬件ID格式"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"认证失败: 硬件ID已被封禁 {mask_sensitive_data(hardware_id)} - {ban_reason}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"硬件ID已被封禁: {ban_reason}"
        )

    # Check whether hardware ID exceeds online limit
    preview_license_key = auth_header[7:] if str(auth_header or "").startswith("Bearer ") else ""
    is_online_limited, limit_reason = check_hardware_id_online_limit(
        db,
        hardware_id,
        license_key=preview_license_key,
    )
    if is_online_limited:
        logger.warning(f"认证失败: 硬件ID在线限制 {mask_sensitive_data(hardware_id)} - {limit_reason}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Hardware ID is already online; only one concurrent client is allowed per hardware ID"
        )

    # 解析Authorization头部
    if not auth_header.startswith('Bearer '):
        logger.warning("认证失败: 无效的Authorization头部格式")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的证格"
        )

    license_key = normalize_license_key_text(auth_header[7:])  # 移除 "Bearer " 前缀并标准化

    # 验证许可证密钥格
    if not validate_license_key_format(license_key):
        logger.warning(f"认证失败: 无效的许可证密钥格式 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的许可证密钥格式"
        )

    # 查找许可证密
    license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
    if not license_obj:
        logger.warning(f"认证失败: 许可证密钥不存在 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥不存在"
        )

    # Check availability
    if not license_obj.is_active:
        logger.warning(f"认证失败: 许可证密钥已禁用 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥已禁用"
        )

    # Check expiration
    if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
        logger.warning(f"认证失败: 许可证密钥已过期 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥已过期"
        )

    key_type = str(license_obj.key_type or "").strip().upper()
    if is_executor_license_type(key_type):
        if not expected_parent_scope_hash:
            logger.warning(f"认证失败: 执行器授权缺少父级范围参数 {mask_sensitive_data(license_key)}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="执行器授权码必须提供父级授权范围参数"
            )
        scope_ok, scope_status, scope_message = enforce_executor_parent_scope_hash(
            db,
            license_obj,
            expected_parent_scope_hash,
        )
        if not scope_ok:
            logger.warning(f"认证失败: 父级范围校验失败 {mask_sensitive_data(license_key)} - {scope_message}")
            raise HTTPException(status_code=scope_status, detail=scope_message)

    bind_ok, bind_status, bind_message = enforce_license_binding_policy(db, license_obj, hardware_id)
    if not bind_ok:
        logger.warning(f"认证失败: 绑定策略验证失败 {mask_sensitive_data(license_key)} - {bind_message}")
        raise HTTPException(status_code=bind_status, detail=bind_message)

    # 如果许可证未绑定，进行绑
    if not license_obj.client_hardware_id:
        # Register client if missing
        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            # 臊注册客户
            client = Client(
                hardware_id=hardware_id,
                **_client_online_fields_for_create(),
            )
            db.add(client)

        # 绑定许可证到客户
        license_obj.client_hardware_id = hardware_id
        license_obj.current_activations += 1

        try:
            db.commit()
            logger.info(f"许可证绑定成功: {mask_sensitive_data(license_key)} -> {mask_sensitive_data(hardware_id)}")
        except Exception as e:
            db.rollback()
            logger.error(f"许可证绑定失 {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="许可证绑定失"
            )

    # 更新客户竜后活动时
    client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if client:
        _touch_client_online(client)
        db.commit()

    # Create client session (used for concurrent online limit)
    session_token = create_client_session(db, hardware_id, license_key)
    if not session_token:
        logger.error(f"v1认证成功但创建会话失败: {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="会话创建失败"
        )

    # 返回成功响应（兼容户期望的格式）
    logger.info(f"认证成功: {mask_sensitive_data(license_key)} - {license_obj.key_type} - 会话: {session_token[:16]}...")
    return {
        "message": "认证成功",
        "license_type": license_obj.key_type.lower(),
        "expires_at": license_obj.expires_at.isoformat() if license_obj.expires_at else None,
        "session_token": session_token,
        "session_expires_in": 86400
    }

@app.post("/api/v2/auth/verify")
async def verify_auth_v2(request: Request, db: Session = Depends(get_db)):
    """新一代证- v2版本，支持更强的安全验证"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    # 获取认证信息
    hardware_id = data.get('hardware_id')
    license_key = normalize_license_key_text(data.get('license_key'))
    timestamp = data.get('timestamp')  # 客户端请求时间戳
    nonce = data.get('nonce')  # 随机数，防止重放攻击
    client_version = data.get('client_version', 'unknown')  # 客户端版本
    expected_parent_scope_hash = resolve_parent_scope_hash(request, data)
    executor_format_requested = validate_license_key_format(license_key, expected_types=["EXECUTOR"])

    # 验证必参数
    if not hardware_id or not license_key:
        logger.warning("v2认证失败: 缺少必要参数")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数"
        )

    client_time = None
    if timestamp:
        try:
            client_time = datetime.fromisoformat(str(timestamp).replace('Z', '+00:00'))
            if client_time.tzinfo is None:
                client_time = client_time.replace(tzinfo=timezone.utc)
            server_time = datetime.now(pytz.utc)
            time_diff = abs((server_time - client_time).total_seconds())

            if time_diff > 300:  # 5分钟
                logger.warning(f"v2认证失败: 时间戳过期 (差异: {time_diff}秒)")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="请求时间戳无"
                )
        except HTTPException:
            raise
        except Exception:
            logger.warning("v2认证失败: 时间戳格式无效")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="时间戳格式无"
            )

    nonce_text = str(nonce or "").strip()
    if nonce_text:
        if not validate_nonce_text(nonce_text):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="nonce格式无效"
            )
        if client_time is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="缺少请求时间戳"
            )
        if not consume_request_nonce("v2_auth_verify", hardware_id, nonce_text, ttl_seconds=600):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="检测到重复请求"
            )

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        logger.warning(f"v2认证失败: 无效的硬件ID格式 {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的硬件ID格式"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"v2认证失败: 硬件ID已被封禁 {mask_sensitive_data(hardware_id)} - {ban_reason}")
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "success": False,
                "error_code": "HARDWARE_BANNED",
                "message": f"硬件ID已被封禁: {ban_reason}",
                "is_banned": True
            }
        )

    # Check whether hardware ID exceeds online limit
    is_online_limited, limit_reason = check_hardware_id_online_limit(
        db,
        hardware_id,
        license_key=license_key,
    )
    if is_online_limited:
        logger.warning(f"v2认证失败: 硬件ID在线限制 {mask_sensitive_data(hardware_id)} - {limit_reason}")
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "success": False,
                "error_code": "HARDWARE_ONLINE_LIMIT",
                "message": f"Hardware ID is already online; only one concurrent client is allowed per hardware ID",
                "is_online_limit": True
            }
        )

    # 查是否启用密钥验证（强制刷新状）
    license_validation_enabled = is_license_validation_enabled(db)

    if not license_validation_enabled and not expected_parent_scope_hash:
        matched_license = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
        matched_is_executor = bool(
            matched_license and is_executor_license_type(str(matched_license.key_type or "").strip().upper())
        )
        if executor_format_requested or matched_is_executor:
            logger.warning(f"v2认证失败: 执行器授权缺少父级范围参数 {mask_sensitive_data(license_key)}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="执行器授权码必须提供父级授权范围参数"
            )
        # 如果关闭了密钥验证，仅验证硬件ID即可通过
        logger.info(f"v2认证成功(仅验证硬件ID): {mask_sensitive_data(hardware_id)} - 密钥验证已关闭")

        # Register client if missing
        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            client = Client(
                hardware_id=hardware_id,
                **_client_online_fields_for_create(),
            )
            db.add(client)
        else:
            _touch_client_online(client)

        db.commit()

        return {
            "success": True,
            "message": "认证成功",
            "validation_mode": "hardware_only",
            "license_validation_enabled": False,
            "license_type": "editor",
            "expires_at": None,
            "server_time": datetime.now(pytz.utc).isoformat()
        }

    # When key validation is enabled, validate license
    if not validate_license_key_format(license_key):
        logger.warning(f"v2认证失败: 无效的许可证密钥格式 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的许可证密钥格式"
        )

    # 查找许可证密
    license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
    if not license_obj:
        logger.warning(f"v2认证失败: 许可证密钥不存在 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥不存在"
        )

    # Check availability
    if not license_obj.is_active:
        logger.warning(f"v2认证失败: 许可证密钥已禁用 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥已禁用"
        )

    # Check expiration
    if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
        logger.warning(f"v2认证失败: 许可证密钥已过期 {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="许可证密钥已过期"
        )

    key_type = str(license_obj.key_type or "").strip().upper()
    if is_executor_license_type(key_type):
        if not expected_parent_scope_hash:
            logger.warning(f"v2认证失败: 执行器授权缺少父级范围参数 {mask_sensitive_data(license_key)}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="执行器授权码必须提供父级授权范围参数"
            )
        scope_ok, scope_status, scope_message = enforce_executor_parent_scope_hash(
            db,
            license_obj,
            expected_parent_scope_hash,
        )
        if not scope_ok:
            logger.warning(f"v2认证失败: 父级范围校验失败 {mask_sensitive_data(license_key)} - {scope_message}")
            raise HTTPException(status_code=scope_status, detail=scope_message)

    bind_ok, bind_status, bind_message = enforce_license_binding_policy(db, license_obj, hardware_id)
    if not bind_ok:
        logger.warning(f"v2认证失败: 绑定策略验证失败 {mask_sensitive_data(license_key)} - {bind_message}")
        raise HTTPException(status_code=bind_status, detail=bind_message)

    # 如果许可证未绑定，进行绑
    if not license_obj.client_hardware_id:
        # Register client if missing
        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            # 臊注册客户
            client = Client(
                hardware_id=hardware_id,
                **_client_online_fields_for_create(),
            )
            db.add(client)

        # 绑定许可证到客户
        license_obj.client_hardware_id = hardware_id
        license_obj.current_activations += 1

        try:
            db.commit()
            logger.info(f"v2许可证绑定成功: {mask_sensitive_data(license_key)} -> {mask_sensitive_data(hardware_id)}")
        except Exception as e:
            db.rollback()
            logger.error(f"v2许可证绑定失败: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="许可证绑定失"
            )

    # 更新客户竜后活动时
    client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if client:
        _touch_client_online(client)
        db.commit()

    # Create client session (used for concurrent online limit)
    session_token = create_client_session(
        db,
        hardware_id,
        license_key,
        {"client_version": client_version, "nonce": nonce_text}
    )
    if not session_token:
        logger.error(f"v2认证成功但创建会话失败: {mask_sensitive_data(license_key)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="会话创建失败"
        )

    # 返回v2格式的成功响
    logger.info(f"v2认证成功: {mask_sensitive_data(license_key)} - {license_obj.key_type} - 客户端版本: {client_version} - 会话: {session_token[:16]}...")

    # 计算剩余天数
    remaining_days = None
    if license_obj.expires_at:
        remaining_days = max(0, (license_obj.expires_at - datetime.utcnow()).days)

    return {
        "success": True,
        "message": "认证成功",
        "validation_mode": "full",
        "license_validation_enabled": True,
        "license_type": license_obj.key_type.lower(),
        "expires_at": license_obj.expires_at.isoformat() if license_obj.expires_at else None,
        "remaining_days": remaining_days,
        "is_permanent": license_obj.expires_at is None,
        "server_time": datetime.now(pytz.utc).isoformat(),
        "api_version": "2.0",
        "session_token": session_token,
        "session_expires_in": 86400
    }

@app.post("/api/licensing/verify_and_bind_editor")
async def verify_and_bind_editor_license(request: Request, db: Session = Depends(get_db)):
    """编辑器可验证和绑定API"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get('hardware_id')
    license_key = data.get('license_key')

    if not hardware_id or not license_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数"
        )

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": "无效的硬件ID格式"
            }
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"编辑器许可证验证失败: 硬件ID已被封禁 {mask_sensitive_data(hardware_id)} - {ban_reason}")
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "success": False,
                "message": f"硬件ID已被封禁: {ban_reason}"
            }
        )

    # Check whether hardware ID exceeds online limit
    is_online_limited, limit_reason = check_hardware_id_online_limit(
        db,
        hardware_id,
        license_key=license_key,
        license_type="EDITOR",
    )
    if is_online_limited:
        logger.warning(f"编辑器许可证验证失败: 硬件ID在线限制 {mask_sensitive_data(hardware_id)} - {limit_reason}")
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "success": False,
                "message": "Hardware ID is already online; only one concurrent client is allowed per hardware ID"
            }
        )

    # 验证编辑器密钥格
    if not license_key.upper().startswith('ED-') or not validate_license_key_format(license_key):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": "无效的编辑器许可证密钥格"
            }
        )

    # 查找许可
    license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
    if not license_obj:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "success": False,
                "message": "许可证密钥不存在"
            }
        )

    # 查可状
    if not license_obj.is_active:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": "许可证密钥已禁用"
            }
        )

    if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": "许可证密钥已过期"
            }
        )

    bind_ok, bind_status, bind_message = enforce_license_binding_policy(db, license_obj, hardware_id)
    if not bind_ok:
        return JSONResponse(
            status_code=bind_status,
            content={
                "success": False,
                "message": bind_message
            }
        )

    # Register client if missing
    client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if not client:
        client = Client(
            hardware_id=hardware_id,
            **_client_online_fields_for_create(),
        )
        db.add(client)

    # 绑定许可
    if not license_obj.client_hardware_id:
        license_obj.client_hardware_id = hardware_id
        license_obj.current_activations += 1

    # Update client activity time
    _touch_client_online(client)

    try:
        db.commit()

        # Create client session (used for concurrent online limit)
        session_token = create_client_session(db, hardware_id, license_key)
        if not session_token:
            logger.error(f"编辑器许可证验证成功但创建会话失败: {mask_sensitive_data(license_key)}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": "会话创建失败"
                }
            )

        logger.info(f"编辑器许可证验证绑定成功: {mask_sensitive_data(license_key)} -> {mask_sensitive_data(hardware_id)} - 会话: {session_token[:16]}...")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "编辑器许可证验证绑定成功",
                "license_type": "editor",
                "expires_at": license_obj.expires_at.isoformat() if license_obj.expires_at else None,
                "session_token": session_token,
                "session_expires_in": 86400
            }
        )
    except Exception as e:
        db.rollback()
        logger.error(f"编辑器许可证绑定失败: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "许可证绑定失"
            }
        )

@app.post("/api/licensing/create_license")
async def create_license(
    request: Request,
    db: Session = Depends(get_db),
    _admin_user: User = Depends(require_admin_auth),
):
    """创建许可证（支持执行器子码批量创建）"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    key_type = str(data.get("key_type", "EDITOR") or "EDITOR").strip().upper()
    raw_expires_days = data.get("expires_days")
    expires_days: Optional[int] = None
    create_count = 1

    if raw_expires_days not in (None, ""):
        if isinstance(raw_expires_days, bool):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        try:
            expires_days = int(str(raw_expires_days).strip())
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        if expires_days < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        if expires_days == 0:
            expires_days = None

    parent_editor: Optional[LicenseKey] = None
    parent_license_id: Optional[int] = None
    managed_executor_limit = 1

    if is_editor_license_type(key_type):
        raw_limit = data.get("managed_executor_limit")
        if raw_limit is not None:
            if isinstance(raw_limit, bool):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="managed_executor_limit必须为非负整数"
                )
            try:
                managed_executor_limit = int(str(raw_limit).strip())
            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="managed_executor_limit必须为非负整数"
                )
            if managed_executor_limit < 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="managed_executor_limit必须为非负整数"
                )

    if is_executor_license_type(key_type):
        raw_count = data.get("create_count")
        if raw_count in (None, ""):
            raw_count = data.get("batch_count")
        if raw_count in (None, ""):
            raw_count = data.get("count")
        if raw_count in (None, ""):
            raw_count = 1
        if isinstance(raw_count, bool):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="create_count必须为大于等于1的整数"
            )
        try:
            create_count = int(str(raw_count).strip())
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="create_count必须为大于等于1的整数"
            )
        if create_count < 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="create_count必须为大于等于1的整数"
            )
        if create_count > 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="单次批量创建数量不能超过200"
            )

        parent_id_raw = data.get("parent_license_id")
        parent_key_raw = data.get("parent_license_key", "")
        parent_editor = resolve_editor_license(
            db,
            editor_license_id=parent_id_raw,
            editor_license_key=parent_key_raw,
        )
        if not parent_editor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="创建执行器授权码时必须提供有效的上级编辑器授权码"
            )

        if not parent_editor.is_active:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="上级编辑器授权码已禁用，无法创建执行器授权码"
            )
        if parent_editor.expires_at and parent_editor.expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="上级编辑器授权码已过期，无法创建执行器授权码"
            )

        limit = get_editor_executor_limit(parent_editor)
        current_count = count_active_managed_executor_licenses(db, parent_editor.id)
        if limit > 0:
            remaining = max(limit - current_count, 0)
            if remaining <= 0:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"上级编辑器授权码可管理的执行器授权码数量已达上限({limit})"
                )
            if create_count > remaining:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"剩余可创建执行器授权码数量为 {remaining}，本次请求 {create_count} 个"
                )
        parent_license_id = parent_editor.id

    # 非执行器类型不允许批量创建，保持兼容默认单个
    if not is_executor_license_type(key_type):
        create_count = 1

    expires_at = None
    if expires_days:
        expires_at = datetime.utcnow() + timedelta(days=expires_days)

    def _generate_key() -> str:
        return generate_license_key_by_type(key_type)

    created_keys: List[str] = []
    new_licenses: List[LicenseKey] = []

    for _ in range(create_count):
        license_key = _generate_key()
        retry = 0
        while retry < 20:
            exists_in_batch = license_key in created_keys
            exists_in_db = db.query(LicenseKey.id).filter(LicenseKey.key_string == license_key).first() is not None
            if not exists_in_batch and not exists_in_db:
                break
            license_key = _generate_key()
            retry += 1
        if retry >= 20:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="生成许可证密钥失败，请重试"
            )

        new_licenses.append(
            LicenseKey(
                key_string=license_key,
                key_type=key_type,
                expires_at=expires_at,
                is_active=True,
                max_activations=managed_executor_limit if is_editor_license_type(key_type) else 1,
                parent_license_id=parent_license_id
            )
        )
        created_keys.append(license_key)

    try:
        db.add_all(new_licenses)
        db.commit()
        logger.info(f"许可证创建成功: {len(created_keys)}个 - {key_type}")
        return {
            "success": True,
            "message": ("批量创建许可证成功" if len(created_keys) > 1 else "许可证创建成功"),
            "license_key": created_keys[0] if created_keys else None,
            "created_count": len(created_keys),
            "created_license_keys": created_keys,
            "key_type": key_type,
            "expires_at": expires_at.isoformat() if expires_at else None,
            "parent_license_id": parent_license_id,
            "parent_license_key": parent_editor.key_string if parent_editor else None,
            "managed_executor_limit": managed_executor_limit if is_editor_license_type(key_type) else None
        }
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"许可证创建失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="许可证创建失败"
        )


def build_parent_managed_child_license_payload(child: LicenseKey) -> Dict[str, Any]:
    now_utc = datetime.utcnow()
    is_expired = bool(child.expires_at and child.expires_at < now_utc)
    if not child.is_active:
        status_text = "禁用"
    elif is_expired:
        status_text = "过期"
    else:
        status_text = "有效"

    return {
        "id": child.id,
        "key_string": child.key_string,
        "key_type": child.key_type,
        "client_hardware_id": child.client_hardware_id,
        "created_at": format_beijing_time(child.created_at),
        "expires_at": format_beijing_time(child.expires_at) if child.expires_at else None,
        "is_active": bool(child.is_active),
        "is_expired": is_expired,
        "status_text": status_text,
    }


@app.post("/api/parent/licenses/query")
async def query_parent_managed_licenses(request: Request, db: Session = Depends(get_db)):
    """父级授权码查询所辖全部子授权码。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    parent_license_key = str(data.get("parent_license_key", "") or "").strip()
    parent_editor = require_active_editor_license_for_management(db, parent_license_key)

    child_rows = db.query(LicenseKey).filter(
        LicenseKey.parent_license_id == int(parent_editor.id),
        func.upper(LicenseKey.key_type) == "EXECUTOR",
    ).order_by(LicenseKey.created_at.desc()).all()

    active_executor_count = count_active_managed_executor_licenses(db, parent_editor.id)
    managed_limit = get_editor_executor_limit(parent_editor)
    is_unlimited = managed_limit == 0
    remaining_count = None if is_unlimited else max(managed_limit - active_executor_count, 0)

    return {
        "success": True,
        "parent": {
            "id": parent_editor.id,
            "key_string": parent_editor.key_string,
            "managed_executor_limit": managed_limit,
            "active_executor_count": active_executor_count,
            "is_unlimited": is_unlimited,
            "remaining_count": remaining_count,
        },
        "children": [build_parent_managed_child_license_payload(item) for item in child_rows],
        "total_children": len(child_rows),
    }


@app.post("/api/parent/licenses/create")
async def create_parent_managed_executor_licenses(request: Request, db: Session = Depends(get_db)):
    """父级授权码新增所辖执行器子授权码。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    parent_license_key = str(data.get("parent_license_key", "") or "").strip()
    parent_editor = require_active_editor_license_for_management(db, parent_license_key)

    raw_count = data.get("create_count")
    if raw_count in (None, ""):
        raw_count = data.get("quantity")
    if raw_count in (None, ""):
        raw_count = 1
    if isinstance(raw_count, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="create_count必须为大于等于1的整数"
        )
    try:
        create_count = int(str(raw_count).strip())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="create_count必须为大于等于1的整数"
        )
    if create_count < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="create_count必须为大于等于1的整数"
        )
    if create_count > 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="单次新增数量不能超过200"
        )

    raw_expires_days = data.get("expires_days")
    expires_days: Optional[int] = None
    if raw_expires_days not in (None, ""):
        if isinstance(raw_expires_days, bool):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        try:
            expires_days = int(str(raw_expires_days).strip())
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        if expires_days < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="expires_days必须为非负整数"
            )
        if expires_days == 0:
            expires_days = None

    managed_limit = get_editor_executor_limit(parent_editor)
    active_executor_count = count_active_managed_executor_licenses(db, parent_editor.id)
    if managed_limit > 0:
        remaining = max(managed_limit - active_executor_count, 0)
        if remaining <= 0:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"可管理执行器授权码数量已达上限({managed_limit})"
            )
        if create_count > remaining:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"剩余可新增数量为 {remaining}，本次请求 {create_count} 个"
            )

    expires_at = datetime.utcnow() + timedelta(days=expires_days) if expires_days else None

    created_keys: List[str] = []
    new_licenses: List[LicenseKey] = []
    for _ in range(create_count):
        candidate_key = generate_license_key_by_type("EXECUTOR")
        retry = 0
        while retry < 20:
            exists_in_batch = candidate_key in created_keys
            exists_in_db = db.query(LicenseKey.id).filter(LicenseKey.key_string == candidate_key).first() is not None
            if not exists_in_batch and not exists_in_db:
                break
            candidate_key = generate_license_key_by_type("EXECUTOR")
            retry += 1
        if retry >= 20:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="生成执行器授权码失败，请重试"
            )

        new_licenses.append(
            LicenseKey(
                key_string=candidate_key,
                key_type="EXECUTOR",
                expires_at=expires_at,
                is_active=True,
                max_activations=1,
                parent_license_id=int(parent_editor.id),
            )
        )
        created_keys.append(candidate_key)

    try:
        db.add_all(new_licenses)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"父级新增子授权码失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="新增子授权码失败"
        )

    latest_active_count = count_active_managed_executor_licenses(db, parent_editor.id)
    latest_remaining = None if managed_limit == 0 else max(managed_limit - latest_active_count, 0)

    return {
        "success": True,
        "message": f"成功新增 {len(created_keys)} 个执行器授权码",
        "created_count": len(created_keys),
        "created_license_keys": created_keys,
        "parent": {
            "id": parent_editor.id,
            "key_string": parent_editor.key_string,
            "managed_executor_limit": managed_limit,
            "active_executor_count": latest_active_count,
            "is_unlimited": managed_limit == 0,
            "remaining_count": latest_remaining,
        }
    }


@app.post("/api/parent/licenses/delete")
async def delete_parent_managed_executor_license(request: Request, db: Session = Depends(get_db)):
    """父级授权码删除其所辖执行器子授权码。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    parent_license_key = str(data.get("parent_license_key", "") or "").strip()
    parent_editor = require_active_editor_license_for_management(db, parent_license_key)

    child_license_id_raw = data.get("child_license_id")
    child_license_key_raw = normalize_license_key_text(data.get("child_license_key"))
    child_license: Optional[LicenseKey] = None

    if child_license_id_raw is not None:
        try:
            child_license_id = int(child_license_id_raw)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="child_license_id必须为整数"
            )
        child_license = db.query(LicenseKey).filter(
            LicenseKey.id == child_license_id
        ).first()
    elif child_license_key_raw:
        child_license = db.query(LicenseKey).filter(
            LicenseKey.key_string == child_license_key_raw
        ).first()
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="必须提供child_license_id或child_license_key"
        )

    if not child_license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="子授权码不存在"
        )

    if not is_executor_license_type(child_license.key_type):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="仅允许删除执行器子授权码"
        )

    if int(child_license.parent_license_id or 0) != int(parent_editor.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="该子授权码不属于当前父级授权码"
        )

    deleted_child_id = int(child_license.id)
    deleted_child_key = child_license.key_string

    try:
        db.query(ActivationCard).filter(
            ActivationCard.generated_license_id == deleted_child_id
        ).update(
            {ActivationCard.generated_license_id: None},
            synchronize_session=False
        )
        db.query(ClientSession).filter(
            ClientSession.license_key == deleted_child_key
        ).delete(synchronize_session=False)
        db.delete(child_license)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"父级删除子授权码失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="删除子授权码失败"
        )

    managed_limit = get_editor_executor_limit(parent_editor)
    latest_active_count = count_active_managed_executor_licenses(db, parent_editor.id)
    latest_remaining = None if managed_limit == 0 else max(managed_limit - latest_active_count, 0)

    return {
        "success": True,
        "message": "子授权码删除成功",
        "deleted_child_id": deleted_child_id,
        "deleted_child_key": deleted_child_key,
        "parent": {
            "id": parent_editor.id,
            "key_string": parent_editor.key_string,
            "managed_executor_limit": managed_limit,
            "active_executor_count": latest_active_count,
            "is_unlimited": managed_limit == 0,
            "remaining_count": latest_remaining,
        }
    }


@app.get("/api/admin/check_auth")
async def check_admin_auth(request: Request, admin_user: User = Depends(require_admin_auth)):
    """Check admin authentication status."""
    return {
        "authenticated": True,
        "username": admin_user.username,
        "message": "认证有效"
    }

@app.get("/api/admin/licenses")
async def get_licenses(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Get license list (admin)."""
    try:
        licenses = db.query(LicenseKey).all()
        license_key_map = {item.id: item.key_string for item in licenses}
        active_executor_counts: Dict[int, int] = {}

        count_rows = db.query(
            LicenseKey.parent_license_id,
            func.count(LicenseKey.id)
        ).filter(
            LicenseKey.parent_license_id.is_not(None),
            func.upper(LicenseKey.key_type) == "EXECUTOR",
            LicenseKey.is_active == True,
            or_(LicenseKey.expires_at.is_(None), LicenseKey.expires_at > datetime.utcnow()),
        ).group_by(LicenseKey.parent_license_id).all()

        for parent_id, count_value in count_rows:
            if parent_id is not None:
                active_executor_counts[int(parent_id)] = int(count_value or 0)

        # 主列表仅显示顶层授权码；子授权码在父级详情中查看
        top_level_licenses = [item for item in licenses if item.parent_license_id is None]
        license_list = []

        for license_obj in top_level_licenses:
            parent_id = license_obj.parent_license_id
            is_editor_key = is_editor_license_type(license_obj.key_type)
            license_data = {
                "id": license_obj.id,
                "key_string": license_obj.key_string,  # 显示完整许可证密钥
                "key_type": license_obj.key_type,
                "client_hardware_id": license_obj.client_hardware_id,  # 显示完整硬件ID
                "created_at": format_beijing_time(license_obj.created_at),
                "expires_at": format_beijing_time(license_obj.expires_at) if license_obj.expires_at else None,
                "is_active": license_obj.is_active,
                "current_activations": license_obj.current_activations,
                "max_activations": license_obj.max_activations,
                "parent_license_id": parent_id,
                "parent_license_key": license_key_map.get(parent_id) if parent_id else None,
                "managed_executor_limit": get_editor_executor_limit(license_obj) if is_editor_key else None,
                "active_executor_count": active_executor_counts.get(int(license_obj.id), 0) if is_editor_key else None,
            }
            license_list.append(license_data)

        return {
            "success": True,
            "licenses": license_list,
            "total": len(license_list)
        }
    except Exception as e:
        logger.error(f"Get license list failed {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Get license list failed"
        )

@app.get("/api/admin/clients")
async def get_clients(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Get client list (admin)."""
    try:
        # Use selectinload to preload relations and avoid N+1 queries.
        clients = db.query(Client).options(selectinload(Client.license_keys)).all()
        client_list = []

        for client in clients:
            client_data = {
                "hardware_id": client.hardware_id,  # 显示完整硬件ID
                "registration_date": format_beijing_time(client.registration_date),
                "last_seen": format_beijing_time(client.last_seen) if client.last_seen else None,
                "is_active": client.is_active,
                "license_count": len(client.license_keys),
                "licenses": [lic.key_string for lic in client.license_keys]  # 显示完整许可证密钥
            }
            client_list.append(client_data)

        return {
            "success": True,
            "clients": client_list,
            "total": len(client_list)
        }
    except Exception as e:
        logger.error(f"Get client list failed {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Get client list failed"
        )

@app.get("/")
async def root():
    """根路- 重定向到管理界面"""
    return RedirectResponse(url="/admin")

@app.get("/login")
async def login_page(request: Request):
    """登录页面"""
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/api/admin/login")
async def admin_login(request: Request, db: Session = Depends(get_db)):
    """Admin login."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    username = str(data.get("username", "") or "").strip()
    password = str(data.get("password", "") or "")

    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名和密码不能为空"
        )

    settings = get_runtime_system_settings(db)
    max_login_attempts = int(settings["max_login_attempts"])
    lockout_duration_minutes = int(settings["lockout_duration_minutes"])
    session_timeout_minutes = int(settings["session_timeout_minutes"])
    client_ip = get_client_ip(request)
    attempt_key = f"{username.lower()}|{client_ip}"
    now = datetime.utcnow()

    with _admin_login_failures_lock:
        attempt_state = _admin_login_failures.get(attempt_key)
        if attempt_state:
            lock_until = attempt_state.get("lock_until")
            if isinstance(lock_until, datetime) and lock_until > now:
                remaining_seconds = max(1, int((lock_until - now).total_seconds()))
                remaining_minutes = max(1, (remaining_seconds + 59) // 60)
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail=f"登录失败次数过多，请 {remaining_minutes} 分钟后重试",
                )
            if isinstance(lock_until, datetime) and lock_until <= now:
                _admin_login_failures.pop(attempt_key, None)

    user = db.query(User).filter(
        User.username == username,
        User.is_admin == True
    ).first()

    if not user or not verify_password(password, user.password_hash):
        with _admin_login_failures_lock:
            current_state = _admin_login_failures.get(attempt_key, {})
            failed_count = int(current_state.get("failed_count", 0)) + 1
            lock_until = None
            if failed_count >= max_login_attempts:
                lock_until = now + timedelta(minutes=lockout_duration_minutes)
            _admin_login_failures[attempt_key] = {
                "failed_count": 0 if lock_until else failed_count,
                "lock_until": lock_until,
                "last_failed_at": now,
            }

        logger.warning(f"管理员登录失败: {username} - IP: {client_ip}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )

    with _admin_login_failures_lock:
        _admin_login_failures.pop(attempt_key, None)

    user_agent = request.headers.get("user-agent", "")
    session_token = create_admin_session(db, user.id, client_ip, user_agent)

    logger.info(f"管理员登录成功: {username} - IP: {client_ip}")

    response = JSONResponse(
        content={
            "success": True,
            "message": "登录成功",
            "session_timeout_seconds": session_timeout_minutes * 60,
            "user": {
                "id": user.id,
                "username": user.username,
                "is_admin": user.is_admin,
            },
        }
    )
    response.set_cookie(
        key="admin_session",
        value=session_token,
        max_age=session_timeout_minutes * 60,
        path="/",
        httponly=True,
        samesite="lax",
        secure=should_use_secure_cookie(request),
    )
    return response

@app.get("/api/admin/verify_session")
async def verify_session(request: Request, db: Session = Depends(get_db)):
    """验证会话"""
    session_token = request.cookies.get("admin_session")

    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    return {
        "success": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "is_admin": user.is_admin
        }
    }

@app.post("/api/admin/logout")
async def admin_logout(request: Request, db: Session = Depends(get_db)):
    """Admin logout."""
    session_token = request.cookies.get("admin_session")

    if session_token:
        token_key = _session_token_key(session_token)
        with _session_lock:
            _admin_sessions.pop(token_key, None)
        clear_secondary_delete_verified(session_token)
        _save_sessions()

    response = JSONResponse(content={"success": True, "message": "登出成功"})
    response.delete_cookie(
        key="admin_session",
        path="/",
        samesite="lax",
        secure=should_use_secure_cookie(request),
    )
    return response

@app.post("/api/market/account/register", response_model=MarketAuthorAuthResponse)
async def market_author_register(payload: MarketAuthorCredentialsRequest, request: Request, db: Session = Depends(get_db)):
    username = str(payload.username or "").strip()
    password = str(payload.password or "")
    if len(username) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="\u7528\u6237\u540d\u81f3\u5c11\u9700\u89813\u4e2a\u5b57\u7b26")
    if len(password) < 6:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="\u5bc6\u7801\u81f3\u5c11\u9700\u89816\u4e2a\u5b57\u7b26")
    if not re.fullmatch(r"[A-Za-z0-9_\-.]{3,50}", username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="\u7528\u6237\u540d\u4ec5\u652f\u6301\u5b57\u6bcd\u3001\u6570\u5b57\u3001\u4e0b\u5212\u7ebf\u3001\u4e2d\u5212\u7ebf\u548c\u70b9")
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="\u7528\u6237\u540d\u5df2\u5b58\u5728")

    now = datetime.utcnow()
    user = User(
        username=username,
        password_hash=get_password_hash(password),
        is_admin=False,
        created_at=now,
        last_login=now,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    client_ip = get_client_ip(request)
    user_agent = request.headers.get("user-agent", "")
    session_token, expires_in = create_market_author_session(user.id, client_ip, user_agent)
    logger.info(f"\u5e02\u573a\u4f5c\u8005\u6ce8\u518c\u6210\u529f: {username} - IP: {client_ip}")
    return _build_market_author_auth_response(user, session_token, expires_in)


@app.post("/api/market/account/login", response_model=MarketAuthorAuthResponse)
async def market_author_login(payload: MarketAuthorCredentialsRequest, request: Request, db: Session = Depends(get_db)):
    username = str(payload.username or "").strip()
    password = str(payload.password or "")
    if not username or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="\u7528\u6237\u540d\u548c\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a")
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef")

    user.last_login = datetime.utcnow()
    db.commit()

    client_ip = get_client_ip(request)
    user_agent = request.headers.get("user-agent", "")
    session_token, expires_in = create_market_author_session(user.id, client_ip, user_agent)
    logger.info(f"\u5e02\u573a\u4f5c\u8005\u767b\u5f55\u6210\u529f: {username} - IP: {client_ip}")
    return _build_market_author_auth_response(user, session_token, expires_in)


@app.get("/api/market/account/profile", response_model=MarketAuthorAuthResponse)
async def market_author_profile(request: Request, db: Session = Depends(get_db)):
    user = require_market_author_auth(request, db, required=True)
    session_token = _extract_bearer_token(request)
    return _build_market_author_auth_response(user, session_token, _MARKET_AUTHOR_SESSION_TTL_SECONDS)


@app.post("/api/market/account/logout")
async def market_author_logout(request: Request, db: Session = Depends(get_db)):
    _ = require_market_author_auth(request, db, required=True)
    session_token = _extract_bearer_token(request)
    if session_token:
        revoke_market_author_session(session_token)
    return {"success": True, "message": "\u9000\u51fa\u6210\u529f"}


@app.post("/api/admin/change_password")
async def change_admin_password(request: Request, db: Session = Depends(get_db)):
    """Update admin password."""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    old_password = data.get("old_password", "")
    new_password = data.get("new_password", "")

    if not old_password or not new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="旧密码和新密码不能为"
        )

    # 验证旧密
    if not verify_password(old_password, user.password_hash):
        logger.warning(f"Update password failed (old password mismatch) {user.username} - IP: {request.client.host}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="旧密码错"
        )

    # 更新密码
    user.password_hash = get_password_hash(new_password)
    db.commit()

    logger.info(f"管理员密码已修改: {user.username} - IP: {request.client.host}")

    return {
        "success": True,
        "message": "密码修改成功"
    }

@app.post("/api/admin/set_secondary_password")
async def set_secondary_password(request: Request, db: Session = Depends(get_db)):
    """设置二级密码（修改时要验证旧密码"""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    password = data.get("password", "")
    old_password = data.get("old_password", "")
    description = data.get("description", "二级密码")

    if not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="密码不能为空"
        )

    # 查是否已有二级密
    existing_secondary_pwd = db.query(SecondaryPassword).filter(
        SecondaryPassword.is_active == True
    ).first()

    # 如果已有二级密码，需要验证旧密码
    if existing_secondary_pwd:
        if not old_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="修改二级密码需要提供旧密码"
            )

        if not verify_password(old_password, existing_secondary_pwd.password_hash):
            logger.warning(f"修改二级密码失败（旧密码错误）: {user.username} - IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="旧的二级密码错误"
            )

        logger.info(f"旧二级密码验证通过: {user.username} - IP: {request.client.host}")

    # 禁用有旧的二级密
    db.query(SecondaryPassword).update({"is_active": False})

    # 创建新的二级密码
    secondary_pwd = SecondaryPassword(
        password_hash=get_password_hash(password),
        description=description,
        created_by=user.username,
        is_active=True
    )
    db.add(secondary_pwd)
    db.commit()

    action = "修改" if existing_secondary_pwd else "设置"
    logger.info(f"二级密码已{action}: {user.username} - IP: {request.client.host}")

    return {
        "success": True,
        "message": f"二级密码{action}成功"
    }

@app.get("/api/admin/check_secondary_password")
async def check_secondary_password(request: Request, db: Session = Depends(get_db)):
    """查是否已设置二级密码"""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    # Check whether an active secondary password exists
    existing_secondary_pwd = db.query(SecondaryPassword).filter(
        SecondaryPassword.is_active == True
    ).first()

    return {
        "success": True,
        "has_secondary_password": existing_secondary_pwd is not None
    }

@app.post("/api/admin/verify_secondary_password")
async def verify_secondary_password_api(request: Request, db: Session = Depends(get_db)):
    """验证二级密码"""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    password = data.get("password", "")

    if not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="密码不能为空"
        )

    # Get current active secondary password
    secondary_pwd = db.query(SecondaryPassword).filter(
        SecondaryPassword.is_active == True
    ).first()

    if not secondary_pwd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Secondary password"
        )

    # 验证密码
    if not verify_password(password, secondary_pwd.password_hash):
        logger.warning(f"二级密码验证失败: {user.username} - IP: {request.client.host}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="密码错误"
        )

    logger.info(f"二级密码验证成功: {user.username} - IP: {request.client.host}")

    return {
        "success": True,
        "message": "验证成功"
    }


async def require_secondary_password_for_delete(
    request: Request,
    db: Session,
    admin_user: Optional[User] = None,
    action_name: str = "删除操作",
) -> None:
    """删除类敏感操作统一二级密码校验"""
    session_token = request.cookies.get("admin_session")
    if is_secondary_delete_verified(session_token):
        return

    secondary_pwd = db.query(SecondaryPassword).filter(
        SecondaryPassword.is_active == True
    ).first()
    if not secondary_pwd:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"{action_name}需要先设置二级密码"
        )

    body_data: Dict[str, Any] = {}
    try:
        parsed = await request.json()
        if isinstance(parsed, dict):
            body_data = parsed
    except Exception:
        body_data = {}

    secondary_password = (
        str(body_data.get("secondary_password", "") or "").strip()
        or str(body_data.get("secondaryPassword", "") or "").strip()
        or str(request.headers.get("X-Secondary-Password", "") or "").strip()
    )
    if not secondary_password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"{action_name}需要先完成本次登录的二级密码验证"
        )

    if not verify_password(secondary_password, secondary_pwd.password_hash):
        if admin_user:
            logger.warning(f"{action_name}二级密码验证失败: {admin_user.username}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="二级密码错误"
        )

    mark_secondary_delete_verified(session_token)


@app.get("/api/admin/settings")
async def get_admin_settings(request: Request, db: Session = Depends(get_db)):
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    return {
        "success": True,
        "settings": build_admin_settings_payload(db)
    }


@app.post("/api/admin/settings")
async def save_admin_settings(request: Request, db: Session = Depends(get_db)):
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    server_name = str(data.get("serverName", "") or "").strip()
    if not server_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="服务器名称不能为空"
        )
    if len(server_name) > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="服务器名称长度不能超过100"
        )

    max_clients = _require_int_setting(data.get("maxClients"), "最大客户端数量", 1, 1000000)
    session_timeout = _require_int_setting(data.get("sessionTimeout"), "会话超时", 5, 1440)
    max_login_attempts = _require_int_setting(data.get("maxLoginAttempts"), "最大登录尝试次数", 1, 20)
    lockout_duration = _require_int_setting(data.get("lockoutDuration"), "锁定时长", 1, 1440)
    enable_logging = _require_bool_setting(data.get("enableLogging"), "日志开关")
    enable_csrf = _require_bool_setting(data.get("enableCSRF"), "CSRF开关")
    enable_rate_limit = _require_bool_setting(data.get("enableRateLimit"), "速率限制开关")
    market_update_server_base = str(
        data.get(
            "marketUpdateServerBase",
            get_runtime_system_settings(db).get("market_update_server_base", ""),
        )
        or ""
    ).strip()
    if len(market_update_server_base) > 500:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="共享平台更新服务器地址长度不能超过500",
        )

    setting_updates: Dict[str, Tuple[str, str]] = {
        "server_name": (
            server_name,
            SYSTEM_SETTING_META["server_name"]["description"],
        ),
        "max_clients": (
            str(max_clients),
            SYSTEM_SETTING_META["max_clients"]["description"],
        ),
        "session_timeout_minutes": (
            str(session_timeout),
            SYSTEM_SETTING_META["session_timeout_minutes"]["description"],
        ),
        "enable_logging": (
            "true" if enable_logging else "false",
            SYSTEM_SETTING_META["enable_logging"]["description"],
        ),
        "max_login_attempts": (
            str(max_login_attempts),
            SYSTEM_SETTING_META["max_login_attempts"]["description"],
        ),
        "lockout_duration_minutes": (
            str(lockout_duration),
            SYSTEM_SETTING_META["lockout_duration_minutes"]["description"],
        ),
        "enable_csrf": (
            "true" if enable_csrf else "false",
            SYSTEM_SETTING_META["enable_csrf"]["description"],
        ),
        "enable_rate_limit": (
            "true" if enable_rate_limit else "false",
            SYSTEM_SETTING_META["enable_rate_limit"]["description"],
        ),
        "market_update_server_base": (
            market_update_server_base,
            SYSTEM_SETTING_META["market_update_server_base"]["description"],
        ),
    }

    try:
        for key, (value, description) in setting_updates.items():
            config = db.query(SystemConfig).filter(SystemConfig.config_key == key).first()
            if config:
                config.config_value = value
                config.description = description
                config.updated_at = func.now()
                config.updated_by = user.username
            else:
                db.add(
                    SystemConfig(
                        config_key=key,
                        config_value=value,
                        description=description,
                        updated_by=user.username,
                    )
                )
        db.commit()
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.error("保存系统设置失败")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="保存系统设置失败"
        )

    refresh_runtime_flags(db)
    logger.info(f"系统设置已更新: {user.username} - IP: {request.client.host if request.client else 'unknown'}")
    return {
        "success": True,
        "message": "设置保存成功",
        "settings": build_admin_settings_payload(db)
    }


@app.post("/api/admin/toggle_license_validation")
async def toggle_license_validation(request: Request, db: Session = Depends(get_db)):
    """切换密钥验证状（关闭时需要二级密码验证）"""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    enabled = data.get("enabled")
    secondary_password = data.get("secondary_password")  # 获取二级密码

    if enabled is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少enabled参数"
        )

    # 查当前状
    current_status = is_license_validation_enabled(db)

    # 如果要关闪证，要验证二级密
    if current_status and not enabled:
        # Check whether secondary password is provided (without user_id filter)
        secondary_pwd = db.query(SecondaryPassword).filter(
            SecondaryPassword.is_active == True
        ).first()

        if not secondary_pwd:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="关闭授权验证需要先设置二级密码"
            )

        # 验证二级密码
        if not secondary_password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="关闭授权验证要提供二级密"
            )

        if not verify_password(secondary_password, secondary_pwd.password_hash):
            logger.warning(f"关闭授权验证失败 - 二级密码错误: {user.username} - IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Secondary password is incorrect; cannot disable license validation"
            )

        logger.info(f"Secondary password verified; disabling validation allowed {user.username} - IP: {request.client.host}")

    # 设置配置
    value = "true" if enabled else "false"
    set_system_config(
        db,
        "license_validation_enabled",
        value,
        description="是否启用密钥验证（true=需要验证密钥，false=仅验证硬件ID）",
        updated_by=user.username
    )

    status_text = "已启用" if enabled else "已关闭"
    logger.info(f"密钥验证{status_text}: {user.username} - IP: {request.client.host}")

    return {
        "success": True,
        "message": f"密钥验证{status_text}",
        "enabled": enabled
    }

@app.get("/api/admin/get_license_validation_status")
async def get_license_validation_status(request: Request, db: Session = Depends(get_db)):
    """获取密钥验证状"""
    # 验证会话
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    enabled = is_license_validation_enabled(db)

    return {
        "success": True,
        "enabled": enabled,
        "message": "密钥验证已启用" if enabled else "密钥验证已关闭（仅验证硬件ID）"
    }


@app.get("/api/admin/get_executor_license_limit")
async def get_executor_license_limit(request: Request, db: Session = Depends(get_db)):
    """获取执行器授权码管理上限"""
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    editor_license_id = request.query_params.get("editor_license_id")
    editor_license_key = request.query_params.get("editor_license_key", "")
    if editor_license_id or editor_license_key:
        editor_license = resolve_editor_license(
            db,
            editor_license_id=editor_license_id,
            editor_license_key=editor_license_key,
        )
        if not editor_license:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="指定的编辑器授权码不存在"
            )

        limit = get_editor_executor_limit(editor_license)
        active_count = count_active_managed_executor_licenses(db, editor_license.id)
        return {
            "success": True,
            "scope": "editor",
            "editor_license_id": editor_license.id,
            "editor_license_key": editor_license.key_string,
            "limit": limit,
            "active_executor_count": active_count,
            "remaining_executor_slots": (max(limit - active_count, 0) if limit > 0 else None),
            "message": "获取成功"
        }

    # 兼容旧接口：未指定编辑器时返回全局配置
    limit = get_executor_license_limit_per_hardware(db)
    return {
        "success": True,
        "scope": "global",
        "limit": limit,
        "executor_license_limit_per_hardware": limit,
        "message": "获取成功"
    }


@app.post("/api/admin/set_executor_license_limit")
async def set_executor_license_limit(request: Request, db: Session = Depends(get_db)):
    """设置执行器授权码管理上限"""
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    raw_limit = data.get("limit")
    if raw_limit is None:
        raw_limit = data.get("executor_license_limit_per_hardware")
    if raw_limit is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少limit参数"
        )

    if isinstance(raw_limit, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="limit必须为非负整"
        )

    try:
        limit = int(str(raw_limit).strip())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="limit必须为非负整"
        )

    if limit < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="limit必须为非负整"
        )

    editor_license_id = data.get("editor_license_id")
    editor_license_key = data.get("editor_license_key", "")
    has_editor_scope = editor_license_id is not None or bool(str(editor_license_key or "").strip())

    editor_license = resolve_editor_license(
        db,
        editor_license_id=editor_license_id,
        editor_license_key=editor_license_key,
    )

    if has_editor_scope and not editor_license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="指定的编辑器授权码不存在"
        )

    if editor_license:
        active_count = count_active_managed_executor_licenses(db, editor_license.id)
        if limit > 0 and limit < active_count:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"当前已有 {active_count} 个有效执行器授权码，不能设置更小上限"
            )

        try:
            editor_license.max_activations = limit
            db.commit()
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="保存配置失败"
            )

        return {
            "success": True,
            "scope": "editor",
            "editor_license_id": editor_license.id,
            "editor_license_key": editor_license.key_string,
            "limit": limit,
            "active_executor_count": active_count,
            "remaining_executor_slots": (max(limit - active_count, 0) if limit > 0 else None),
            "message": "设置成功"
        }

    # 兼容旧接口：未传编辑器时设置全局配置
    try:
        set_system_config(
            db,
            "executor_license_limit_per_hardware",
            str(limit),
            description="每个硬件ID可绑定的执行器授权码数量上限，0表示不限制",
            updated_by=user.username
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="保存配置失败"
        )

    return {
        "success": True,
        "scope": "global",
        "limit": limit,
        "executor_license_limit_per_hardware": limit,
        "message": "设置成功"
    }


@app.get("/admin")
async def admin_panel(request: Request, db: Session = Depends(get_db)):
    """管理界面"""
    # 查是否已登录
    session_token = request.cookies.get("admin_session")
    user = verify_admin_session(db, session_token)

    if not user:
        # Not logged in; redirect to login page
        return RedirectResponse(url="/login")

    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/management")
async def management_redirect():
    """管理入口重定"""
    return RedirectResponse(url="/admin")

@app.get("/apply")
async def apply_test_license_page(request: Request):
    """申测试授权码页"""
    return templates.TemplateResponse("apply.html", {"request": request})

@app.get("/activate")
async def activate_card_page(request: Request):
    """卡密活页"""
    return templates.TemplateResponse("activate.html", {"request": request})


@app.get("/parent/licenses")
async def parent_license_manager_page(request: Request):
    """父级授权码子码管理页面。"""
    return templates.TemplateResponse("parent_license_manager.html", {"request": request})


@app.get("/parent")
async def parent_license_manager_redirect():
    return RedirectResponse(url="/parent/licenses")

@app.post("/api/apply_test_license")
async def apply_test_license(request: Request, db: Session = Depends(get_db)):
    """申测试授权码API"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id", "")
    if not isinstance(hardware_id, str):
        hardware_id = str(hardware_id) if hardware_id is not None else ""
    hardware_id = hardware_id.strip()

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式，必须是64字符的SHA256值"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"Test license request failed: hardware ID banned {mask_sensitive_data(hardware_id)} - {ban_reason}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"硬件ID已被封禁，无法申请测试授权码: {ban_reason}"
        )

    # Check whether hardware ID is registered
    client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if not client:
        logger.warning(f"未注册硬件ID尝试申请测试授权码: {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Hardware ID is not registered; register client before requesting test license"
        )

    # Check whether a test key has ever been requested (including expired), enforce one-time rule
    existing_license = db.query(LicenseKey).filter(
        LicenseKey.client_hardware_id == hardware_id,
        LicenseKey.key_type == "EDITOR"  # 只检查编辑器类型的测试密钥
    ).first()

    if existing_license:
        # 查是否还在有效期内（永久密钥没有过期时间
        is_expired = False
        if existing_license.expires_at:
            # 有过期时间的密钥，查是否过
            is_expired = existing_license.expires_at <= datetime.utcnow()
        # 永久密钥（expires_at涓篘one）永远不过期

        if not is_expired and existing_license.is_active:
            # 密钥仍然有效，返回现有密钥信
            logger.info(f"硬件ID已有活跃密钥，返回现有密钥: {mask_sensitive_data(hardware_id)} - 类型: {existing_license.key_type}")

            # 更新客户竜后活动时
            _touch_client_online(client)
            db.commit()

            # Calculate remaining days (permanent key shows -1)
            if existing_license.expires_at:
                remaining_days = max(1, (existing_license.expires_at - datetime.utcnow()).days + 1)
                expires_at_str = format_beijing_time(existing_license.expires_at)
                message = f"您已有活跃的{existing_license.key_type.lower()}密钥"
            else:
                remaining_days = -1  # 永久密钥
                expires_at_str = None
                message = f"您已有永久的{existing_license.key_type.lower()}密钥"

            # 返回现有密钥信息
            return {
                "success": True,
                "message": message,
                "license_key": existing_license.key_string,
                "expires_at": expires_at_str,
                "valid_days": remaining_days,
                "key_type": existing_license.key_type,
                "is_permanent": existing_license.expires_at is None,
                "is_existing": True  # 标识这是现有的密钥
            }
        else:
            # Key expired or disabled; re-request not allowed
            logger.warning(f"硬件ID已申请过测试密钥，不允许再次申请: {mask_sensitive_data(hardware_id)} - 过期状态: {is_expired}")

            # 如果密钥已过期且仍标记为活跃，将其为非活跃状
            if is_expired and existing_license.is_active:
                existing_license.is_active = False
                db.commit()

            # 返回错信息
            if is_expired:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Your test key has expired. Only one test key per hardware ID is allowed. Contact admin for a formal license."
                )
            else:
                # Key expired and disabled
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Your test key is disabled. Contact admin."
                )

    # 注意：只允申次，过期后不能再次申

    try:
        # Generate test license (7-day validity, one-time)
        max_attempts = 5
        license_key = None
        for attempt in range(max_attempts):
            candidate_key = generate_editor_license_key()
            # 查是否已存在
            existing_key = db.query(LicenseKey).filter(LicenseKey.key_string == candidate_key).first()
            if not existing_key:
                license_key = candidate_key
                break

        if not license_key:
            raise Exception("无法生成唯一的授权码")

        expires_at = datetime.utcnow() + timedelta(days=7)

        # 创建许可证
        license_obj = LicenseKey(
            key_string=license_key,
            key_type="EDITOR",
            client_hardware_id=hardware_id,
            expires_at=expires_at,
            is_active=True,
            current_activations=1,
            max_activations=1
        )

        db.add(license_obj)

        # 更新客户竜后活动时
        _touch_client_online(client)

        # 提交有更
        db.commit()

        logger.info(f"测试授权码申请成功: {mask_sensitive_data(license_key)} - 硬件ID: {mask_sensitive_data(hardware_id)}")

        return {
            "success": True,
            "message": "测试授权码申请成功",
            "license_key": license_key,
            "expires_at": format_beijing_time(expires_at),
            "valid_days": 7,
            "is_existing": False  # 标识这是新创建的授权码
        }

    except Exception as e:
        db.rollback()
        logger.error(f"测试授权码申请失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="测试授权码申请失败，请稍后重"
        )

@app.post("/api/activate_card")
async def activate_card(request: Request, db: Session = Depends(get_db)):
    """激活卡密API - 用户使用卡密激活软件"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    card_code = str(data.get("card_code", "") or "").strip().upper()
    hardware_id = str(data.get("hardware_id", "") or "").strip()
    parent_license_id_raw = data.get("parent_license_id")
    parent_license_key_raw = str(data.get("parent_license_key", "") or "").strip()

    # 验证参数
    if not card_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="请输入卡密代码"
        )

    if not hardware_id or not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"Activation failed: hardware ID banned {mask_sensitive_data(hardware_id)} - {ban_reason}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"硬件ID已被封禁: {ban_reason}"
        )

    # 查找卡密
    card = db.query(ActivationCard).filter(ActivationCard.card_code == card_code).first()

    if not card:
        logger.warning(f"卡密激活失败: 卡密不存在 {mask_sensitive_data(card_code)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="卡密不存在，请检查输入"
        )

    # 查卡密状
    if card.status == "used":
        logger.warning(f"卡密激活失败: 卡密已使用 {mask_sensitive_data(card_code)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"卡密已被使用，使用时间: {format_beijing_time(card.used_at)}"
        )

    if card.status == "disabled":
        logger.warning(f"卡密激活失败: 卡密已禁用 {mask_sensitive_data(card_code)}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="卡密已被禁用，请联系客服"
        )

    if card.status == "expired":
        logger.warning(f"卡密激活失败: 卡密已过期 {mask_sensitive_data(card_code)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="卡密已过期"
        )

    card_type = str(card.card_type or "EDITOR").strip().upper()
    if card_type not in {"EDITOR", "EXECUTOR"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="卡密类型无效，无法激活"
        )

    parent_editor: Optional[LicenseKey] = None
    parent_license_id: Optional[int] = None
    if is_executor_license_type(card_type):
        if card.parent_editor_license_id is not None:
            parent_editor = resolve_editor_license(
                db,
                editor_license_id=card.parent_editor_license_id,
            )
            if not parent_editor:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="执行器卡密绑定的上级编辑器授权码不存在"
                )
        else:
            parent_editor = resolve_editor_license(
                db,
                editor_license_id=parent_license_id_raw,
                editor_license_key=parent_license_key_raw,
            )
            if not parent_editor:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="执行器卡密激活必须提供有效的上级编辑器授权码"
                )

        if not parent_editor.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="上级编辑器授权码已禁用，无法激活执行器卡密"
            )
        if parent_editor.expires_at and parent_editor.expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="上级编辑器授权码已过期，无法激活执行器卡密"
            )

        executor_limit = get_editor_executor_limit(parent_editor)
        active_executor_count = count_active_managed_executor_licenses(db, parent_editor.id)
        if executor_limit > 0 and active_executor_count >= executor_limit:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"上级编辑器授权码可管理的执行器授权码数量已达上限({executor_limit})"
            )
        parent_license_id = int(parent_editor.id)

    # Register client if missing
    client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
    if not client:
        # 自动注册客户端
        client = Client(
            hardware_id=hardware_id,
            **_client_online_fields_for_create(),
        )
        db.add(client)
        logger.info(f"自动注册新客户端: {mask_sensitive_data(hardware_id)}")

    try:
        # 生成许可证密钥
        max_attempts = 20
        license_key = None

        for _ in range(max_attempts):
            candidate_key = generate_license_key_by_type(card_type)
            existing_key = db.query(LicenseKey).filter(LicenseKey.key_string == candidate_key).first()
            if not existing_key:
                license_key = candidate_key
                break

        if not license_key:
            raise Exception("无法生成唯一的授权码")

        # 计算过期时间
        if card.duration_days == 0:
            # 永久授权
            expires_at = None
        else:
            expires_at = datetime.utcnow() + timedelta(days=card.duration_days)

        # 创建许可证
        license_obj = LicenseKey(
            key_string=license_key,
            key_type=card_type,
            client_hardware_id=hardware_id,
            expires_at=expires_at,
            is_active=True,
            current_activations=1,
            max_activations=1,
            parent_license_id=parent_license_id
        )

        db.add(license_obj)
        db.flush()  # 获取license_obj.id

        # 更新卡密状
        card.status = "used"
        card.used_at = func.now()
        card.used_hardware_id = hardware_id
        card.generated_license_id = license_obj.id

        # 更新客户竜后活动时
        _touch_client_online(client)

        db.commit()

        logger.info(f"卡密激活成功: {mask_sensitive_data(card_code)} -> 硬件ID: {mask_sensitive_data(hardware_id)}, 授权码: {mask_sensitive_data(license_key)}")

        return {
            "success": True,
            "message": "卡密激活成功",
            "license_key": license_key,
            "card_type": card_type,
            "duration_days": card.duration_days,
            "expires_at": format_beijing_time(expires_at) if expires_at else None,
            "is_permanent": expires_at is None,
            "parent_license_id": parent_license_id,
            "parent_license_key": parent_editor.key_string if parent_editor else None
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"卡密激活失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="卡密激活失败，请稍后重试"
        )

@app.get("/api/check_test_license/{hardware_id}")
async def check_test_license(hardware_id: str, db: Session = Depends(get_db)):
    """Query test license status for hardware ID."""
    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"硬件ID已被封禁: {ban_reason}"
        )

    # 查找任何编辑器类型的密钥（包拿期和非活跃的
    test_license = db.query(LicenseKey).filter(
        LicenseKey.client_hardware_id == hardware_id,
        LicenseKey.key_type == "EDITOR"
    ).first()

    if test_license:
        # 查是否还在有效期内（永久密钥没有过期时间
        is_expired = False
        if test_license.expires_at:
            # 有过期时间的密钥，查是否过
            is_expired = test_license.expires_at <= datetime.utcnow()
        # 永久密钥（expires_at涓篘one）永远不过期

        if not is_expired and test_license.is_active:
            # 密钥仍然有效
            if test_license.expires_at:
                remaining_days = max(1, (test_license.expires_at - datetime.utcnow()).days + 1)
                expires_at_str = format_beijing_time(test_license.expires_at)
            else:
                remaining_days = -1  # 永久密钥
                expires_at_str = None

            return {
                "success": True,
                "has_license": True,
                "license_key": test_license.key_string,
                "expires_at": expires_at_str,
                "valid_days": remaining_days,
                "key_type": test_license.key_type,
                "is_permanent": test_license.expires_at is None,
                "is_active": True,
                "can_apply": False
            }
        else:
            # Key expired or disabled; cannot request again
            # 如果密钥已过期且仍标记为活跃，将其为非活跃状
            if is_expired and test_license.is_active:
                test_license.is_active = False
                try:
                    db.commit()
                    logger.info(f"查询时发现过期密钥，设为非活跃: {mask_sensitive_data(hardware_id)} - 类型: {test_license.key_type}")
                except Exception as e:
                    # Commit may fail (possible concurrent update); rollback and continue
                    db.rollback()
                    logger.warning(f"设置过期密钥为非活跃时失败: {e}")

            return {
                "success": True,
                "has_license": True,
                "license_key": test_license.key_string,
                "expires_at": format_beijing_time(test_license.expires_at) if test_license.expires_at else None,
                "valid_days": 0,
                "key_type": test_license.key_type,
                "is_permanent": False,
                "is_active": False,
                "can_apply": False,  # 过期后不能再次申请
                "message": "Test key expired or disabled. Only one test key per hardware ID is allowed. Contact admin for a formal license."
            }

    # 没有找到任何测试密钥，可以申
    return {
        "success": True,
        "has_license": False,
        "can_apply": True,
        "message": "未找到测试授权码，可以申请新的测试授权码"
    }

# 添加一些实用的管理API
@app.get("/api/admin/license/{license_id}")
async def get_license_details(license_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """获取许可证"""
    license_obj = db.query(LicenseKey).filter(LicenseKey.id == license_id).first()
    if not license_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="许可证不存在"
        )

    # Get client info
    client_info = None
    if license_obj.client_hardware_id:
        client = db.query(Client).filter(Client.hardware_id == license_obj.client_hardware_id).first()
        if client:
            client_info = {
                "hardware_id": client.hardware_id,
                "registration_date": format_beijing_time(client.registration_date),
                "last_seen": format_beijing_time(client.last_seen) if client.last_seen else None,
                "is_active": client.is_active
            }

    parent_license_key = None
    if license_obj.parent_license_id:
        parent_license = db.query(LicenseKey).filter(
            LicenseKey.id == int(license_obj.parent_license_id)
        ).first()
        if parent_license:
            parent_license_key = parent_license.key_string

    active_executor_count = None
    child_licenses: List[Dict[str, Any]] = []
    if is_editor_license_type(license_obj.key_type):
        active_executor_count = count_active_managed_executor_licenses(db, license_obj.id)
        child_rows = db.query(LicenseKey).filter(
            LicenseKey.parent_license_id == license_obj.id
        ).order_by(LicenseKey.created_at.desc()).all()
        for child in child_rows:
            child_licenses.append({
                "id": child.id,
                "key_string": child.key_string,
                "key_type": child.key_type,
                "client_hardware_id": child.client_hardware_id,
                "created_at": format_beijing_time(child.created_at),
                "expires_at": format_beijing_time(child.expires_at) if child.expires_at else None,
                "is_active": child.is_active,
                "current_activations": child.current_activations,
                "max_activations": child.max_activations,
            })

    return {
        "success": True,
        "license": {
            "id": license_obj.id,
            "key_string": license_obj.key_string,  # 返回完整密钥用于编辑
            "key_type": license_obj.key_type,
            "client_hardware_id": license_obj.client_hardware_id,
            "created_at": format_beijing_time(license_obj.created_at),
            "expires_at": format_beijing_time(license_obj.expires_at) if license_obj.expires_at else None,
            "is_active": license_obj.is_active,
            "current_activations": license_obj.current_activations,
            "max_activations": license_obj.max_activations,
            "client_info": client_info,
            "parent_license_id": license_obj.parent_license_id,
            "parent_license_key": parent_license_key,
            "managed_executor_limit": get_editor_executor_limit(license_obj) if is_editor_license_type(license_obj.key_type) else None,
            "active_executor_count": active_executor_count,
            "child_licenses": child_licenses,
        }
    }

@app.put("/api/admin/license/{license_id}")
async def update_license(license_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """更新许可证信"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    license_obj = db.query(LicenseKey).filter(LicenseKey.id == license_id).first()
    if not license_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="许可证不存在"
        )

    try:
        license_key_type = str(license_obj.key_type or "").strip().upper()

        # 更新过期时间
        if 'expires_at' in data:
            if data['expires_at']:
                license_obj.expires_at = datetime.fromisoformat(data['expires_at'].replace('Z', '+00:00'))
            else:
                license_obj.expires_at = None

        # Update client binding
        if 'client_hardware_id' in data:
            new_hardware_id = data['client_hardware_id'].strip() if data['client_hardware_id'] else None
            if new_hardware_id and not validate_hardware_id(new_hardware_id):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="无效的硬件ID格式"
                )

            # 如果更改了绑定，要更新激活数
            if license_obj.client_hardware_id != new_hardware_id:
                if license_obj.client_hardware_id:  # 原来有绑定
                    license_obj.current_activations = max(0, license_obj.current_activations - 1)
                if new_hardware_id:  # 新绑定
                    license_obj.current_activations += 1

                license_obj.client_hardware_id = new_hardware_id

        # 更新其他字
        if 'is_active' in data:
            license_obj.is_active = bool(data['is_active'])

        if 'max_activations' in data:
            try:
                max_value = int(data['max_activations'])
            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="max_activations必须为整数"
                )

            if is_editor_license_type(license_key_type):
                if max_value < 0:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="编辑器可管理执行器数量不能为负数"
                    )
                active_count = count_active_managed_executor_licenses(db, license_obj.id)
                if max_value > 0 and max_value < active_count:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail=f"当前已有 {active_count} 个有效执行器授权码，不能设置更小上限"
                    )
                license_obj.max_activations = max_value
            else:
                license_obj.max_activations = max(1, max_value)

        if 'managed_executor_limit' in data:
            if not is_editor_license_type(license_key_type):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="仅编辑器授权码可设置执行器管理数量"
                )
            try:
                managed_limit = int(data['managed_executor_limit'])
            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="managed_executor_limit必须为非负整数"
                )
            if managed_limit < 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="managed_executor_limit必须为非负整数"
                )

            active_count = count_active_managed_executor_licenses(db, license_obj.id)
            if managed_limit > 0 and managed_limit < active_count:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"当前已有 {active_count} 个有效执行器授权码，不能设置更小上限"
                )
            license_obj.max_activations = managed_limit

        if 'parent_license_id' in data or 'parent_license_key' in data:
            if not is_executor_license_type(license_key_type):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="仅执行器授权码可设置上级编辑器授权码"
                )

            parent_editor = resolve_editor_license(
                db,
                editor_license_id=data.get('parent_license_id'),
                editor_license_key=data.get('parent_license_key', ''),
            )
            if not parent_editor:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="必须提供有效的上级编辑器授权码"
                )

            limit = get_editor_executor_limit(parent_editor)
            active_count = count_active_managed_executor_licenses(
                db,
                parent_editor.id,
                exclude_license_id=license_obj.id
            )
            if limit > 0 and active_count >= limit:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"目标编辑器授权码可管理的执行器数量已达上限({limit})"
                )
            license_obj.parent_license_id = int(parent_editor.id)

        db.commit()
        logger.info(f"许可证更新成功: {mask_sensitive_data(license_obj.key_string)}")

        return {
            "success": True,
            "message": "许可证更新成"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"许可证更新失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="许可证更新失"
        )

@app.delete("/api/admin/license/{license_id}")
async def delete_license(license_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """删除许可证"""
    await require_secondary_password_for_delete(request, db, admin_user, "删除许可证")
    license_obj = db.query(LicenseKey).filter(LicenseKey.id == license_id).first()
    if not license_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="许可证不存在"
        )

    try:
        deleted_child_count = 0
        if is_editor_license_type(license_obj.key_type):
            child_license_ids = [
                row[0]
                for row in db.query(LicenseKey.id).filter(
                    LicenseKey.parent_license_id == int(license_obj.id)
                ).all()
            ]
            deleted_child_count = len(child_license_ids)
            if child_license_ids:
                db.query(ActivationCard).filter(
                    ActivationCard.generated_license_id.in_(child_license_ids)
                ).update(
                    {ActivationCard.generated_license_id: None},
                    synchronize_session=False
                )
                db.query(LicenseKey).filter(
                    LicenseKey.id.in_(child_license_ids)
                ).delete(synchronize_session=False)

        key_string = license_obj.key_string
        db.query(ActivationCard).filter(
            ActivationCard.generated_license_id == license_obj.id
        ).update(
            {ActivationCard.generated_license_id: None},
            synchronize_session=False
        )
        db.delete(license_obj)
        db.commit()
        logger.info(f"许可证删除成功: {mask_sensitive_data(key_string)}")

        return {
            "success": True,
            "message": "许可证删除成功",
            "deleted_child_count": deleted_child_count
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"许可证删除失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="许可证删除失败"
        )

@app.post("/api/admin/license/{license_id}/toggle")
async def toggle_license_status(license_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """切换许可证状态（启用/禁用）"""
    license_obj = db.query(LicenseKey).filter(LicenseKey.id == license_id).first()
    if not license_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="许可证不存在"
        )

    license_obj.is_active = not license_obj.is_active

    try:
        db.commit()
        status_text = "启用" if license_obj.is_active else "禁用"
        logger.info(f"许可证状态切换: {mask_sensitive_data(license_obj.key_string)} - {status_text}")
        return {
            "success": True,
            "message": f"许可证已{status_text}",
            "is_active": license_obj.is_active
        }
    except Exception as e:
        db.rollback()
        logger.error(f"许可证状态切换失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="状切换失"
        )

# 封禁硬件ID管理API
@app.get("/api/admin/banned_hardware_ids")
async def get_banned_hardware_ids(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Get all banned hardware IDs (admin)."""
    try:
        banned_records = db.query(BannedHardwareId).all()
        banned_list = []

        for record in banned_records:
            banned_data = {
                "id": record.id,
                "hardware_id": record.hardware_id,  # 显示完整硬件ID用于前端匹配
                "reason": record.reason,
                "banned_at": format_beijing_time(record.banned_at),
                "banned_by": record.banned_by,
                "is_active": record.is_active,
                "expires_at": format_beijing_time(record.expires_at) if record.expires_at else None,
                "notes": record.notes
            }
            banned_list.append(banned_data)

        return {
            "success": True,
            "banned_hardware_ids": banned_list,
            "total": len(banned_list)
        }
    except Exception as e:
        logger.error(f"获取封禁硬件ID列表失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="获取封禁硬件ID列表失败"
        )

@app.post("/api/admin/ban_hardware_id")
async def ban_hardware_id(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Ban hardware ID (admin)."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id", "").strip()
    reason = data.get("reason", "").strip()
    expires_days = data.get("expires_days")  # None表示永久封禁
    notes = data.get("notes", "").strip()

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # 查是否已经存在封禁
    existing_ban = db.query(BannedHardwareId).filter(
        BannedHardwareId.hardware_id == hardware_id
    ).first()

    # 计算过期时间
    expires_at = None
    if expires_days and expires_days > 0:
        expires_at = datetime.utcnow() + timedelta(days=expires_days)

    if existing_ban:
        # 如果已经昴跃封禁，返回错
        if existing_ban.is_active:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="该硬件ID已封"
            )

        # 如果昝活跃封，重新激活并更新信息
        existing_ban.is_active = True
        existing_ban.reason = reason or "管理员封禁"
        existing_ban.banned_by = admin_user.username
        existing_ban.banned_at = func.now()
        existing_ban.expires_at = expires_at
        existing_ban.notes = notes
        ban_record = existing_ban
    else:
        # 创建新的封记录
        ban_record = BannedHardwareId(
            hardware_id=hardware_id,
            reason=reason or "管理员封禁",
            banned_by=admin_user.username,
            expires_at=expires_at,
            notes=notes
        )
        db.add(ban_record)

    try:
        db.commit()
        action = "重新封禁" if existing_ban else "封禁"
        logger.info(f"硬件ID{action}成功: {mask_sensitive_data(hardware_id)} - 操作员: {admin_user.username}")
        return {
            "success": True,
            "message": f"硬件ID{action}成功",
            "ban_id": ban_record.id
        }
    except Exception as e:
        db.rollback()
        logger.error(f"硬件ID封禁失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="硬件ID封禁失败"
        )

@app.post("/api/admin/unban_hardware_id/{ban_id}")
async def unban_hardware_id(ban_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Unban hardware ID (admin)."""
    ban_record = db.query(BannedHardwareId).filter(BannedHardwareId.id == ban_id).first()
    if not ban_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="封记录不存"
        )

    try:
        ban_record.is_active = False
        db.commit()
        logger.info(f"硬件ID解除封禁: {mask_sensitive_data(ban_record.hardware_id)} - 操作员: {admin_user.username}")
        return {
            "success": True,
            "message": "硬件ID解除封禁成功"
        }
    except Exception as e:
        db.rollback()
        logger.error(f"硬件ID解除封禁失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="硬件ID解除封禁失败"
        )

@app.post("/api/admin/toggle_ban/{ban_id}")
async def toggle_ban_status(ban_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Toggle ban status (admin)."""
    ban_record = db.query(BannedHardwareId).filter(BannedHardwareId.id == ban_id).first()
    if not ban_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="封记录不存"
        )

    try:
        ban_record.is_active = not ban_record.is_active
        db.commit()
        status_text = "启用" if ban_record.is_active else "禁用"
        logger.info(f"封禁状态切换: {mask_sensitive_data(ban_record.hardware_id)} - {status_text} - 操作员: {admin_user.username}")
        return {
            "success": True,
            "message": f"封禁状态已{status_text}",
            "is_active": ban_record.is_active
        }
    except Exception as e:
        db.rollback()
        logger.error(f"Toggle ban status failed {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Toggle ban status failed"
        )

@app.delete("/api/admin/ban/{ban_id}")
async def delete_ban_record(ban_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Delete ban record (admin)."""
    await require_secondary_password_for_delete(request, db, admin_user, "删除封禁记录")
    ban_record = db.query(BannedHardwareId).filter(BannedHardwareId.id == ban_id).first()
    if not ban_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="封记录不存"
        )

    try:
        hardware_id = ban_record.hardware_id
        db.delete(ban_record)
        db.commit()
        logger.info(f"封禁记录删除: {mask_sensitive_data(hardware_id)} - 操作员: {admin_user.username}")
        return {
            "success": True,
            "message": "封禁记录删除成功"
        }
    except Exception as e:
        db.rollback()
        logger.error(f"封禁记录删除失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="封禁记录删除失败"
        )


@app.get("/api/admin/logs")
async def get_system_logs(
    level: Optional[str] = None,
    limit: int = 100,
    admin_user: User = Depends(get_current_admin_user)
):
    """获取系统日志"""
    try:
        limit = int(limit)
    except Exception:
        limit = 100
    limit = max(1, min(limit, 1000))

    try:
        logger.info(f"获取系统日志请求 - 级别过滤: {level}, 限制: {limit}, 用户: {admin_user.username}")
        logs = []

        # 查找日志文件
        log_files = []
        # Find multiple log file patterns
        patterns = [
            "auth_server.log",  # 当前使用的日志文件
            "app_*.log",        # Possible app log files
            "*.log"             # 所有日志文件
        ]

        for pattern in patterns:
            found_files = []
            for search_dir in (LOG_DIR, PROJECT_LOG_DIR):
                found_files.extend(glob.glob(os.path.join(search_dir, pattern)))
            log_files.extend(found_files)

        # Deduplicate and sort by modified time, newest first
        log_files = list(set(log_files))
        log_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        logger.info(f"找到日志文件: {log_files}")

        # 读取日志文件
        for log_file in log_files[:3]:  # 只读取最近3个日志文件
            try:
                # 解析日志
                for line in reversed(_read_last_lines(log_file, limit)):  # 取最后limit行，倒序处理
                    line = line.strip()
                    if not line:
                        continue

                    # 解析日志格式: 2025-08-25 22:34:18,046 - jw3-auth-server - INFO - 消息
                    log_match = re.match(
                        r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (.*) - (\w+) - (.+)',
                        line
                    )

                    if log_match:
                        timestamp_str, logger_name, log_level, message = log_match.groups()

                        # 过滤日志级别
                        if level and log_level != level.upper():
                            continue

                        # Normalize timestamp format
                        try:
                            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")
                            timestamp_iso = timestamp.isoformat()
                        except:
                            timestamp_iso = timestamp_str

                        logs.append({
                            "timestamp": timestamp_iso,
                            "level": log_level,
                            "location": logger_name.strip() if logger_name else "",
                            "message": message.strip(),
                            "file": os.path.basename(log_file)
                        })

                        if len(logs) >= limit:
                            break

            except Exception as e:
                logger.error(f"读取日志文件失败 {log_file}: {e}")
                continue

            if len(logs) >= limit:
                break

        # 按时间排序，新的在前
        logs.sort(key=lambda x: x["timestamp"], reverse=True)

        return {
            "success": True,
            "logs": logs[:limit],
            "total": len(logs)
        }

    except Exception as e:
        logger.error(f"获取系统日志失败: {e}")
        raise HTTPException(status_code=500, detail="获取系统日志失败")


@app.delete("/api/admin/logs")
async def clear_system_logs(
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """清空系统日志"""
    await require_secondary_password_for_delete(request, db, admin_user, "清空日志")
    try:
        # 获取有日志文
        log_files = []
        patterns = ["auth_server.log", "app_*.log", "*.log"]
        for pattern in patterns:
            for search_dir in (LOG_DIR, PROJECT_LOG_DIR):
                log_files.extend(glob.glob(os.path.join(search_dir, pattern)))

        # 去重
        log_files = list(set(log_files))
        cleared_files = []

        for log_file in log_files:
            try:
                # Clear file content without deleting file
                with open(log_file, 'w', encoding='utf-8') as f:
                    f.write("")
                cleared_files.append(log_file)
                logger.info(f"日志文件已清空: {log_file} - 操作员: {admin_user.username}")
            except Exception as e:
                logger.error(f"清空日志文件失败 {log_file}: {e}")
                continue

        return {
            "success": True,
            "message": f"已清空 {len(cleared_files)} 个日志文件",
            "cleared_files": cleared_files
        }

    except Exception as e:
        logger.error(f"清空系统日志失败: {e}")
        raise HTTPException(status_code=500, detail="清空系统日志失败")


@app.get("/api/admin/recent_activity")
async def get_recent_activity(
    limit: int = 10,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """获取最近活动。"""
    try:
        limit = int(limit)
    except Exception:
        limit = 10
    limit = max(1, min(limit, 100))

    try:
        activities = []

        # Get recent client registrations
        recent_clients = db.query(Client).order_by(Client.registration_date.desc()).limit(5).all()
        for client in recent_clients:
            if client.registration_date:
                # Convert to Beijing time
                beijing_time = utc_to_beijing(client.registration_date)
                activities.append({
                    "type": "client_register",
                    "title": "新客户端注册",
                    "description": f"硬件ID: {mask_sensitive_data(client.hardware_id)}",
                    "timestamp": beijing_time.isoformat(),
                    "icon": "bi-pc-display",
                    "color": "primary"
                })

        # Get recent license creations
        recent_licenses = db.query(LicenseKey).order_by(LicenseKey.created_at.desc()).limit(5).all()
        for license_key in recent_licenses:
            if license_key.created_at:
                # Convert to Beijing time
                beijing_time = utc_to_beijing(license_key.created_at)
                activities.append({
                    "type": "license_create",
                    "title": "许可证创建",
                    "description": f"类型: {license_key.key_type.upper()}, 密钥: {mask_sensitive_data(license_key.key_string)}",
                    "timestamp": beijing_time.isoformat(),
                    "icon": "bi-key",
                    "color": "success"
                })

        # Get recent admin sessions
        recent_sessions = db.query(AdminSession).filter(
            AdminSession.created_at >= datetime.utcnow() - timedelta(hours=24)
        ).order_by(AdminSession.created_at.desc()).limit(3).all()

        for session in recent_sessions:
            user = db.query(User).filter(User.id == session.user_id).first()
            if user and session.created_at:
                # Convert to Beijing time
                beijing_time = utc_to_beijing(session.created_at)
                activities.append({
                    "type": "admin_login",
                    "title": "管理员登录",
                    "description": f"用户: {user.username}, IP: {session.ip_address or '未知'}",
                    "timestamp": beijing_time.isoformat(),
                    "icon": "bi-person-check",
                    "color": "info"
                })

        # 从日志中获取系统启动信息
        try:
            log_files = [os.path.join(LOG_DIR, "auth_server.log")]
            for log_file in log_files:
                if os.path.exists(log_file):
                    # Find recent startup logs
                    for line in reversed(_read_last_lines(log_file, 50)):  # 只检查最后50行
                        if "JW3授权验证服务端启动完成" in line:
                            # 解析时间
                            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})', line)
                            if match:
                                timestamp_str = match.group(1)
                                try:
                                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")
                                    # Assume local log time and convert with timezone
                                    beijing_time = BEIJING_TZ.localize(timestamp)
                                    activities.append({
                                        "type": "system_start",
                                        "title": "系统启动",
                                        "description": "JW3授权验证服务端启动完成",
                                        "timestamp": beijing_time.isoformat(),
                                        "icon": "bi-power",
                                        "color": "warning"
                                    })
                                    break  # 叏近一次启
                                except:
                                    continue
                    break
        except Exception as e:
            logger.error(f"读取启动日志失败: {e}")

        # 按时间排序，新的在前
        activities.sort(key=lambda x: x["timestamp"], reverse=True)

        # 不添加任何模拟数捼变示真实的活动数据

        # 限制数量
        activities = activities[:limit]

        logger.info(f"返回 {len(activities)} 条最近活动")

        return {
            "success": True,
            "activities": activities,
            "total": len(activities)
        }

    except Exception as e:
        logger.error(f"获取最近活动失败: {e}")
        raise HTTPException(status_code=500, detail="获取最近活动失败")


@app.delete("/api/admin/client/{hardware_id}")
async def delete_client(
    hardware_id: str,
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """删除客户"""
    await require_secondary_password_for_delete(request, db, admin_user, "删除客户端")
    try:
        # 查找客户
        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="客户端不存在")

        # 删除相关的可
        db.query(LicenseKey).filter(LicenseKey.client_hardware_id == hardware_id).delete(synchronize_session=False)

        # 删除相关的封禁
        db.query(BannedHardwareId).filter(BannedHardwareId.hardware_id == hardware_id).delete(synchronize_session=False)

        # 删除客户
        db.delete(client)
        db.commit()

        logger.info(f"管理员 {admin_user.username} 删除了客户端 {hardware_id}")

        return {
            "success": True,
            "message": "Client deleted successfully"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"删除客户端失败: {e}")
        raise HTTPException(status_code=500, detail="删除客户端失败")


# ==================== 激活卡密管理API ====================

@app.post("/api/admin/cards/generate")
async def generate_activation_cards(
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """批量生成激活卡密（管理员功能）"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    card_type = str(data.get("card_type", "EDITOR") or "EDITOR").strip().upper()
    raw_duration_days = data.get("duration_days", 30)
    raw_quantity = data.get("quantity", 1)
    notes = str(data.get("notes", "") or "").strip()

    if card_type not in {"EDITOR", "EXECUTOR"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="card_type 仅支持 EDITOR 或 EXECUTOR"
        )

    if isinstance(raw_duration_days, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="有效期天数必须为非负整数"
        )
    try:
        duration_days = int(str(raw_duration_days).strip())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="有效期天数必须为非负整数"
        )

    if isinstance(raw_quantity, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="生成数量必须为整数"
        )
    try:
        quantity = int(str(raw_quantity).strip())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="生成数量必须为整数"
        )

    # 验证参数
    if quantity < 1 or quantity > 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="生成数量必须在1-1000之间"
        )

    if duration_days < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="有效期天数不能为负数"
        )

    if len(notes) > 500:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="备注长度不能超过500字符"
        )

    parent_editor: Optional[LicenseKey] = None
    parent_editor_license_id: Optional[int] = None
    if is_executor_license_type(card_type):
        parent_editor = resolve_editor_license(
            db,
            editor_license_id=data.get("parent_license_id"),
            editor_license_key=data.get("parent_license_key", ""),
        )
        if not parent_editor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="生成执行器卡密必须提供有效的上级编辑器授权码"
            )
        if not parent_editor.is_active:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="上级编辑器授权码已禁用，无法生成执行器卡密"
            )
        if parent_editor.expires_at and parent_editor.expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="上级编辑器授权码已过期，无法生成执行器卡密"
            )

        executor_limit = get_editor_executor_limit(parent_editor)
        active_executor_count = count_active_managed_executor_licenses(db, parent_editor.id)
        if executor_limit > 0:
            remaining = max(executor_limit - active_executor_count, 0)
            if quantity > remaining:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"上级编辑器授权码剩余可管理执行器数量为 {remaining}，本次请求 {quantity} 张"
                )
        parent_editor_license_id = int(parent_editor.id)

    # 生成批次ID
    batch_id = f"BATCH-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{secrets.token_hex(4).upper()}"

    generated_cards = []
    failed_count = 0

    try:
        for i in range(quantity):
            # 生成唯一的卡密代码
            max_attempts = 5
            card_code = None

            for attempt in range(max_attempts):
                candidate_code = generate_activation_card_code()
                # 查是否已存在
                existing_card = db.query(ActivationCard).filter(
                    ActivationCard.card_code == candidate_code
                ).first()

                if not existing_card:
                    card_code = candidate_code
                    break

            if not card_code:
                failed_count += 1
                logger.warning(f"生成卡密失败，无法生成唯一代码（第{i+1}张）")
                continue

            # 创建卡密记录
            new_card = ActivationCard(
                card_code=card_code,
                card_type=card_type,
                duration_days=duration_days,
                status="unused",
                created_by=admin_user.username,
                parent_editor_license_id=parent_editor_license_id,
                batch_id=batch_id,
                notes=notes
            )

            db.add(new_card)
            generated_cards.append({
                "card_code": card_code,
                "card_type": card_type,
                "duration_days": duration_days,
                "parent_editor_license_id": parent_editor_license_id
            })

        db.commit()

        logger.info(f"管理员 {admin_user.username} 批量生成了 {len(generated_cards)} 张激活卡密，批次ID: {batch_id}")

        return {
            "success": True,
            "message": f"成功生成 {len(generated_cards)} 张激活卡密",
            "batch_id": batch_id,
            "cards": generated_cards,
            "failed_count": failed_count,
            "total": quantity,
            "parent_editor_license_id": parent_editor_license_id,
            "parent_editor_license_key": parent_editor.key_string if parent_editor else None
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"批量生成激活卡密失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="批量生成激活卡密失败"
        )


@app.get("/api/admin/cards")
async def get_activation_cards(
    request: Request,
    status_filter: Optional[str] = None,
    batch_id: Optional[str] = None,
    limit: int = 100,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get activation card list (admin)."""
    try:
        # 添加调试日志
        logger.info(f"获取卡密列表请求 - 用户: {admin_user.username}, 状态过滤: {status_filter}, 批次: {batch_id}, 限制: {limit}")

        query = db.query(ActivationCard)

        # 状过
        if status_filter:
            query = query.filter(ActivationCard.status == status_filter)

        # 批过滤
        if batch_id:
            query = query.filter(ActivationCard.batch_id == batch_id)

        # 按创建时间序
        query = query.order_by(ActivationCard.created_at.desc())

        # 限制数量
        cards = query.limit(limit).all()
        parent_ids = {
            int(card.parent_editor_license_id)
            for card in cards
            if card.parent_editor_license_id is not None
        }
        parent_key_map: Dict[int, str] = {}
        if parent_ids:
            parent_rows = db.query(LicenseKey.id, LicenseKey.key_string).filter(
                LicenseKey.id.in_(parent_ids)
            ).all()
            parent_key_map = {int(item_id): key for item_id, key in parent_rows}

        card_list = []
        for card in cards:
            parent_id = int(card.parent_editor_license_id) if card.parent_editor_license_id is not None else None
            card_data = {
                "id": card.id,
                "card_code": card.card_code,
                "card_type": card.card_type,
                "duration_days": card.duration_days,
                "status": card.status,
                "created_at": format_beijing_time(card.created_at),
                "created_by": card.created_by,
                "used_at": format_beijing_time(card.used_at) if card.used_at else None,
                "used_hardware_id": card.used_hardware_id,
                "parent_editor_license_id": parent_id,
                "parent_editor_license_key": parent_key_map.get(parent_id) if parent_id is not None else None,
                "batch_id": card.batch_id,
                "notes": card.notes
            }
            card_list.append(card_data)

        # 获取统信息
        total_count = db.query(ActivationCard).count()
        unused_count = db.query(ActivationCard).filter(ActivationCard.status == "unused").count()
        used_count = db.query(ActivationCard).filter(ActivationCard.status == "used").count()

        return {
            "success": True,
            "cards": card_list,
            "statistics": {
                "total": total_count,
                "unused": unused_count,
                "used": used_count,
                "displayed": len(card_list)
            }
        }

    except Exception as e:
        logger.error(f"获取活卡密列表失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="获取活卡密列表失"
        )


@app.get("/api/admin/cards/batches")
async def get_card_batches(
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get card batch summaries (admin)."""
    try:
        # Query all batch IDs and aggregate statistics
        batches = db.query(
            ActivationCard.batch_id,
            func.count(ActivationCard.id).label('total'),
            func.sum(case((ActivationCard.status == 'unused', 1), else_=0)).label('unused'),
            func.sum(case((ActivationCard.status == 'used', 1), else_=0)).label('used'),
            func.min(ActivationCard.created_at).label('created_at'),
            func.max(ActivationCard.created_by).label('created_by'),
            func.max(ActivationCard.duration_days).label('duration_days')
        ).group_by(ActivationCard.batch_id).order_by(ActivationCard.batch_id.desc()).all()

        batch_list = []
        for batch in batches:
            batch_list.append({
                "batch_id": batch.batch_id,
                "total": batch.total,
                "unused": batch.unused or 0,
                "used": batch.used or 0,
                "created_at": format_beijing_time(batch.created_at),
                "created_by": batch.created_by,
                "duration_days": batch.duration_days
            })

        return {
            "success": True,
            "batches": batch_list,
            "total": len(batch_list)
        }

    except Exception as e:
        logger.error(f"获取批次信息失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="获取批次信息失败"
        )


@app.delete("/api/admin/cards/{card_id}")
async def delete_activation_card(
    card_id: int,
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Delete activation card (admin)."""
    await require_secondary_password_for_delete(request, db, admin_user, "删除卡密")
    try:
        card = db.query(ActivationCard).filter(ActivationCard.id == card_id).first()
        if not card:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="卡密不存"
            )

        card_code = card.card_code
        db.delete(card)
        db.commit()

        logger.info(f"管理员 {admin_user.username} 删除了激活卡密: {card_code}")

        return {
            "success": True,
            "message": "卡密删除成功"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"删除活卡密失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="删除活卡密失"
        )


@app.delete("/api/admin/cards/batch/{batch_id}")
async def delete_card_batch(
    batch_id: str,
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """删除整个批的卡密（管理员功能）"""
    await require_secondary_password_for_delete(request, db, admin_user, "删除卡密批次")
    try:
        # 查找该批次的有卡
        cards = db.query(ActivationCard).filter(ActivationCard.batch_id == batch_id).all()

        if not cards:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="批次不存在或已被删除"
            )

        count = len(cards)

        # 删除有卡
        db.query(ActivationCard).filter(ActivationCard.batch_id == batch_id).delete(synchronize_session=False)
        db.commit()

        logger.info(f"管理员 {admin_user.username} 删除了批次 {batch_id}，共 {count} 张卡密")

        return {
            "success": True,
            "message": f"成功删除批次 {batch_id}，共 {count} 张卡密"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"删除批次失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="删除批次失败"
        )


# ==================== 增强握手协议 v2.1 ====================

@app.post("/api/v2.1/client/handshake/initiate")
async def initiate_handshake_v2_1(request: Request, db: Session = Depends(get_db)):
    """握手初始化 v2.1 版本（增强防重放与抗中间人攻击）。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id")
    client_nonce = data.get("client_nonce")
    client_timestamp = data.get("client_timestamp")

    if not all([hardware_id, client_nonce, client_timestamp]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数（需要: hardware_id, client_nonce, client_timestamp）"
        )

    try:
        client_timestamp = int(client_timestamp)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="客户端时间戳格式无效")

    if not validate_nonce_text(client_nonce):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="客户端nonce格式无效")

    if not validate_hardware_id(hardware_id):
        logger.warning(f"Handshake init v2.1 failed: invalid hardware ID {mask_sensitive_data(hardware_id)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无效的硬件ID格式")

    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"Handshake init v2.1 failed: hardware ID banned {mask_sensitive_data(hardware_id)}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"硬件ID已被封禁: {ban_reason}")

    is_valid, error_msg = validate_client_timestamp(client_timestamp)
    if not is_valid:
        logger.warning(f"握手初始化v2.1失败: 时间戳无效 - {error_msg}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)

    try:
        cleanup_expired_handshakes(db)
        server_challenge = generate_server_challenge()
        handshake_token = generate_handshake_token()
        server_nonce = generate_nonce()
        server_timestamp = get_current_timestamp()

        token_hmac = compute_handshake_hmac(
            handshake_token, hardware_id, server_timestamp,
            server_challenge, server_nonce, COMM_AUTH_SECRET_KEY
        )

        handshake_record = ClientLoginHandshake(
            hardware_id=hardware_id,
            session_token=generate_session_token(),
            handshake_token=handshake_token,
            challenge=server_challenge,
            handshake_status="pending",
            expires_at=datetime.utcnow() + timedelta(minutes=5),
            is_active=True,
        )
        db.add(handshake_record)
        db.commit()

        logger.info(
            f"握手初化v2.1成功: {mask_sensitive_data(hardware_id)}, "
            f"令牌: {handshake_token[:16]}..."
        )

        return {
            "success": True,
            "message": "握手令牌已生成",
            "handshake_token": handshake_token,
            "server_challenge": server_challenge,
            "server_nonce": server_nonce,
            "server_timestamp": server_timestamp,
            "client_nonce_echo": client_nonce,
            "token_hmac": token_hmac,
            "protocol_version": "2.1",
            "expires_in": 300
        }

    except Exception as e:
        db.rollback()
        logger.error(f"握手初化v2.1异常: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="握手初化失"
        )


@app.post("/api/v2.1/client/handshake/authenticate")
async def authenticate_handshake_v2_1(request: Request, db: Session = Depends(get_db)):
    """握手认证 v2.1版本 - 改进的安全性（HMAC验证、防重放）"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id")
    license_key = normalize_license_key_text(data.get("license_key"))
    handshake_token = data.get("handshake_token")
    server_challenge = data.get("server_challenge")
    server_nonce = data.get("server_nonce")
    server_timestamp = data.get("server_timestamp")
    client_response = data.get("client_response")
    client_timestamp = data.get("client_timestamp")
    client_nonce = data.get("client_nonce")
    token_hmac = data.get("token_hmac")
    expected_parent_scope_hash = resolve_parent_scope_hash(request, data)

    required_fields = [
        "hardware_id", "license_key", "handshake_token", "server_challenge",
        "server_nonce", "server_timestamp", "client_response", "client_timestamp",
        "client_nonce", "token_hmac"
    ]
    if not all(data.get(field) is not None for field in required_fields):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="缺少必要参数")

    try:
        server_timestamp = int(server_timestamp)
        client_timestamp = int(client_timestamp)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="时间戳参数格式无效")

    if not isinstance(handshake_token, str) or len(handshake_token) > 255:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="握手令牌格式无效")
    if not isinstance(server_challenge, str) or len(server_challenge) > 255:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="服务端挑战格式无效")
    if not isinstance(server_nonce, str) or len(server_nonce) > 128:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="服务端nonce格式无效")
    if not isinstance(client_nonce, str) or len(client_nonce) > 128:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="客户端nonce格式无效")
    if not isinstance(client_response, str) or len(client_response) > 255:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="客户端响应格式无效")
    if not isinstance(token_hmac, str) or len(token_hmac) > 128:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="握手签名格式无效")
    if not validate_nonce_text(server_nonce):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="服务端nonce格式无效")
    if not validate_nonce_text(client_nonce):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="客户端nonce格式无效")

    if not validate_hardware_id(hardware_id):
        logger.warning(f"握手认证v2.1失败: 无效硬件ID")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无效的硬件ID格式")

    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"握手认证v2.1失败: 硬件ID已被封禁")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"硬件ID已被封禁: {ban_reason}")

    cleanup_expired_handshakes(db)
    handshake_record = db.query(ClientLoginHandshake).filter(
        ClientLoginHandshake.handshake_token == handshake_token,
        ClientLoginHandshake.hardware_id == hardware_id,
        ClientLoginHandshake.handshake_status == "pending",
        ClientLoginHandshake.is_active == True,
        ClientLoginHandshake.expires_at > datetime.utcnow(),
    ).first()
    if not handshake_record:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="握手令牌无效、已过期或已使用")

    if handshake_record.challenge != server_challenge:
        handshake_record.handshake_status = "failed"
        handshake_record.is_active = False
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="握手挑战不匹配")

    try:
        if not verify_handshake_hmac(
            handshake_token, hardware_id, server_timestamp,
            server_challenge, server_nonce, token_hmac, COMM_AUTH_SECRET_KEY
        ):
            logger.warning(f"握手认证v2.1失败: 握手令牌HMAC验证失败")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="握手令牌被篡改")

        current_time = get_current_timestamp()
        if current_time - server_timestamp > 300:
            logger.warning(f"握手认证v2.1失败: 握手令牌已过期")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="握手令牌已过期")

        is_valid, error_msg = validate_client_timestamp(client_timestamp)
        if not is_valid:
            logger.warning(f"握手认证v2.1失败: 客户端时间戳无效 - {error_msg}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)

        if not validate_license_key_format(license_key, expected_types=["EXECUTOR"]):
            logger.warning("握手认证v2.1失败: 无效许可证密钥格式")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的许可证密钥格式")

        nonce_scope_value = f"{handshake_token}.{client_nonce}"
        if not consume_request_nonce("v2_1_handshake", hardware_id, nonce_scope_value, ttl_seconds=600):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="检测到重复握手请求")

        if not verify_client_response(
            server_challenge, license_key, server_nonce, client_nonce,
            server_timestamp, client_response, COMM_AUTH_SECRET_KEY
        ):
            logger.warning("握手认证v2.1失败: 客户端响应验证失败")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="握手验证失败，响应无效")

        is_online_limited, limit_reason = check_hardware_id_online_limit(
            db,
            hardware_id,
            license_key=license_key,
            license_type="EXECUTOR",
        )
        if is_online_limited:
            logger.warning(f"握手认证v2.1失败: 硬件ID在线限制 {limit_reason}")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="该硬件ID已在线")

        license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
        if not license_obj:
            logger.warning(f"握手认证v2.1失败: 许可证密钥不存在")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥不存在")

        key_type = str(license_obj.key_type or "").strip().upper()
        if key_type != "EXECUTOR":
            logger.warning(f"握手认证v2.1失败: 许可证类型不匹配 {key_type}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥不存在")

        if not license_obj.is_active:
            logger.warning(f"握手认证v2.1失败: 许可证已禁用")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥已禁用")

        if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
            logger.warning(f"握手认证v2.1失败: 许可证已过期")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥已过期")

        if not expected_parent_scope_hash:
            logger.warning("握手认证v2.1失败: 执行器授权缺少父级范围参数")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="执行器授权码必须提供父级授权范围参数"
            )
        scope_ok, scope_status, scope_message = enforce_executor_parent_scope_hash(
            db,
            license_obj,
            expected_parent_scope_hash,
        )
        if not scope_ok:
            logger.warning(f"握手认证v2.1失败: 父级范围校验失败 - {scope_message}")
            raise HTTPException(status_code=scope_status, detail=scope_message)

        bind_ok, bind_status, bind_message = enforce_license_binding_policy(db, license_obj, hardware_id)
        if not bind_ok:
            logger.warning(f"握手认证v2.1失败: 绑定策略验证失败 - {bind_message}")
            raise HTTPException(status_code=bind_status, detail=bind_message)

        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            client = Client(hardware_id=hardware_id, **_client_online_fields_for_create())
            db.add(client)

        if not license_obj.client_hardware_id:
            license_obj.client_hardware_id = hardware_id
            license_obj.current_activations += 1

        _touch_client_online(client)
        handshake_record.response = client_response
        handshake_record.handshake_status = "authenticated"
        handshake_record.authenticated_at = func.now()
        handshake_record.is_active = False
        db.commit()

        session_token = create_client_session(db, hardware_id, license_key)
        if not session_token:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="会话创建失败")

        logger.info(
            f"握手认证v2.1成功: {mask_sensitive_data(license_key)}, "
            f"会话: {session_token[:16] if session_token else 'None'}..."
        )

        remaining_days = None
        if license_obj.expires_at:
            remaining_days = max(0, (license_obj.expires_at - datetime.utcnow()).days)

        return {
            "success": True,
            "message": "握手认证成功",
            "session_token": session_token,
            "login_status": "authenticated",
            "expires_in": 86400,
            "protocol_version": "2.1",
            # 保留与v2.0兼容的响应字段，便于导出客户端统一解析
            "api_version": "2.1",
            "validation_mode": "full",
            "license_validation_enabled": True,
            "license_type": key_type.lower(),
            "expires_at": license_obj.expires_at.isoformat() if license_obj.expires_at else None,
            "remaining_days": remaining_days,
            "is_permanent": license_obj.expires_at is None,
            "session_expires_in": 86400,
            "server_time": datetime.now(timezone.utc).isoformat(),
        }

    except HTTPException as exc:
        if handshake_record and handshake_record.is_active:
            try:
                handshake_record.handshake_status = "failed"
                handshake_record.is_active = False
                db.commit()
            except Exception:
                db.rollback()
        raise exc
    except Exception as e:
        db.rollback()
        logger.error(f"握手认证v2.1异常: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="握手认证失败")


# ==================== 原握手协（已弃用，保留向后兼容） ====================

@app.post("/api/client/handshake/initiate")
async def initiate_handshake(request: Request, db: Session = Depends(get_db)):
    """Client handshake init: generate token and server challenge."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id")
    license_key = normalize_license_key_text(data.get("license_key"))

    # 验证必参数
    if not hardware_id or not license_key:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数"
        )

    # 验证硬件ID格式
    if not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID格式"
        )

    # Check whether hardware ID is banned
    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        logger.warning(f"Handshake init failed: hardware ID banned {mask_sensitive_data(hardware_id)}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"硬件ID已被封禁: {ban_reason}"
        )

    # 清理过期握手记录和会
    cleanup_expired_handshakes(db)
    cleanup_expired_sessions(db)

    # 注意: 不在初化时查在线状
    # Allow handshake in all cases; auth stage handles old sessions.
    # This avoids inability to re-login after client crash.

    try:
        # 生成握手令牌和服务器挑战
        handshake_token = secrets.token_urlsafe(32)
        challenge = secrets.token_hex(32)
        expires_at = datetime.utcnow() + timedelta(minutes=5)

        # 创建握手记录
        handshake = ClientLoginHandshake(
            hardware_id=hardware_id,
            session_token="",  # 临时为空，认证成功时填充
            handshake_token=handshake_token,
            challenge=challenge,
            handshake_status="pending",
            expires_at=expires_at,
            is_active=True
        )

        db.add(handshake)
        db.commit()

        logger.info(f"握手初始化成功: {mask_sensitive_data(hardware_id)} - 挑战令牌: {handshake_token[:16]}...")

        return {
            "success": True,
            "message": "握手令牌已生成",
            "handshake_token": handshake_token,
            "challenge": challenge,
            "expires_in": 300
        }

    except Exception as e:
        db.rollback()
        logger.error(f"握手初化失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="握手初化失"
        )


@app.post("/api/client/handshake/authenticate")
async def authenticate_handshake(request: Request, db: Session = Depends(get_db)):
    """Client handshake: verify response and create session."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id")
    license_key = data.get("license_key")
    handshake_token = data.get("handshake_token")
    response = data.get("response")
    expected_parent_scope_hash = resolve_parent_scope_hash(request, data)

    # 验证必参数
    if not all([hardware_id, license_key, handshake_token, response]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数"
        )

    handshake = None
    try:
        # 查找握手记录
        handshake = db.query(ClientLoginHandshake).filter(
            ClientLoginHandshake.handshake_token == handshake_token,
            ClientLoginHandshake.hardware_id == hardware_id,
            ClientLoginHandshake.handshake_status == "pending",
            ClientLoginHandshake.is_active == True,
            ClientLoginHandshake.expires_at > datetime.utcnow()
        ).first()

        if not handshake:
            logger.warning(f"握手认证失败: 握手记录不存在或已过{mask_sensitive_data(hardware_id)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="握手令牌无效或已过期"
            )

        # 验证响应（简单验证：response应是challenge的哈希）
        # 生成预期的响应
        expected_response = hashlib.sha256(
            (handshake.challenge + license_key).encode()
        ).hexdigest()

        if response != expected_response:
            handshake.handshake_status = "failed"
            handshake.is_active = False
            db.commit()
            logger.warning(f"握手认证失败: 响应验证失败 {mask_sensitive_data(hardware_id)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="握手验证失败，响应无"
            )

        license_key = normalize_license_key_text(license_key)
        if not validate_license_key_format(license_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="握手验证失败，响应无效"
            )

        license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
        if not license_obj:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="许可证密钥不存在"
            )

        if not license_obj.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="许可证密钥已禁用"
            )

        if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="许可证密钥已过期"
            )

        key_type = str(license_obj.key_type or "").strip().upper()
        if is_executor_license_type(key_type):
            if not expected_parent_scope_hash:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="执行器授权码必须提供父级授权范围参数"
                )
            scope_ok, scope_status, scope_message = enforce_executor_parent_scope_hash(
                db,
                license_obj,
                expected_parent_scope_hash,
            )
            if not scope_ok:
                raise HTTPException(status_code=scope_status, detail=scope_message)

        is_online_limited, limit_reason = check_hardware_id_online_limit(
            db,
            hardware_id,
            license_key=license_key,
            license_type=key_type,
        )
        if is_online_limited:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=limit_reason or "该硬件ID已在线，编辑器授权仅允户在线"
            )

        bind_ok, bind_status, bind_message = enforce_license_binding_policy(db, license_obj, hardware_id)
        if not bind_ok:
            raise HTTPException(status_code=bind_status, detail=bind_message)

        client = db.query(Client).filter(Client.hardware_id == hardware_id).first()
        if not client:
            client = Client(hardware_id=hardware_id, **_client_online_fields_for_create())
            db.add(client)

        if not license_obj.client_hardware_id:
            license_obj.client_hardware_id = hardware_id
            license_obj.current_activations += 1
        _touch_client_online(client)

        session_token = create_client_session(db, hardware_id, license_key)
        if not session_token:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="会话创建失败"
            )

        # 更新握手记录
        handshake.session_token = session_token
        handshake.response = response
        handshake.handshake_status = "authenticated"
        handshake.authenticated_at = func.now()
        handshake.is_active = False

        db.commit()

        logger.info(f"握手认证成功: {mask_sensitive_data(hardware_id)} - 会话令牌: {session_token[:16]}...")

        return {
            "success": True,
            "message": "握手认证成功",
            "session_token": session_token,
            "login_status": "authenticated",
            "expires_in": 86400,
            "server_time": datetime.now(pytz.utc).isoformat()
        }

    except HTTPException:
        if handshake and handshake.is_active:
            try:
                handshake.handshake_status = "failed"
                handshake.is_active = False
                db.commit()
            except Exception:
                db.rollback()
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"握手认证失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="握手认证失败"
        )


@app.post("/api/client/set_online")
async def set_client_online(request: Request, db: Session = Depends(get_db)):
    """Set client status to online."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    session_token = data.get("session_token")

    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少session_token参数"
        )

    try:
        # 查找会话
        session = db.query(ClientSession).filter(
            ClientSession.session_token == session_token,
            ClientSession.is_active == True,
            ClientSession.expires_at > datetime.utcnow()
        ).first()

        if not session:
            logger.warning("上线失败: 会话不存在或已过期")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="会话无效或已过期"
            )

        # 更新状为在线
        _set_client_session_online_status(session, "online")
        db.commit()

        logger.info(f"客户端上线: {mask_sensitive_data(session.hardware_id)} - 会话: {session_token[:16]}...")

        return {
            "success": True,
            "message": "客户端已上线",
            "login_status": "online",
            "session_token": session_token
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Set online failed {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Set online failed"
        )


@app.post("/api/client/offline")
async def client_offline(request: Request, db: Session = Depends(get_db)):
    """客户- 将在线状态改为"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    session_token = data.get("session_token")
    hardware_id = data.get("hardware_id")

    if not session_token or not hardware_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少必要参数"
        )

    try:
        # 查找会话
        session = db.query(ClientSession).filter(
            ClientSession.session_token == session_token,
            ClientSession.hardware_id == hardware_id,
            ClientSession.is_active == True
        ).first()

        if not session:
            logger.warning(f"离线失败: 会话不存{mask_sensitive_data(hardware_id)}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="会话不存"
            )

        # 更新状为离线
        _set_client_session_online_status(session, "offline")
        db.commit()

        logger.info(f"客户 {mask_sensitive_data(hardware_id)} - 会话: {session_token[:16]}...")

        return {
            "success": True,
            "message": "客户端已离线",
            "login_status": "offline"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"客户线失 {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="客户线失"
        )


@app.post("/api/client/heartbeat")
async def client_heartbeat(request: Request, db: Session = Depends(get_db)):
    """Client heartbeat: keep session active."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    session_token = data.get("session_token")
    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少session_token参数"
        )

    session = verify_client_session(db, session_token)
    if not session:
        logger.warning(f"心跳验证失败: 会话无效或已过期 {session_token[:16]}...")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效或已过期"
        )

    logger.debug(f"心跳更新: {mask_sensitive_data(session.hardware_id)}")
    return {
        "success": True,
        "message": "心跳已确认",
        "session_token": session_token,
        "expires_at": session.expires_at.isoformat()
    }

@app.post("/api/client/logout")
async def client_logout(request: Request, db: Session = Depends(get_db)):
    """客户站出"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    session_token = data.get("session_token")
    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="缺少session_token参数"
        )

    invalidate_client_session(db, session_token)
    logger.info(f"客户端登出: 令牌 {session_token[:16]}...")
    return {
        "success": True,
        "message": "登出成功"
    }


@app.post("/api/client/runtime_bundle_key")
async def get_runtime_bundle_key(request: Request, db: Session = Depends(get_db)):
    """返回客户端运行时主密钥（签名校验 + 防重放）。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无效的JSON数据")

    hardware_id = str(data.get("hardware_id") or request.headers.get("X-Hardware-ID") or "").strip()
    session_token = str(data.get("session_token") or "").strip()
    request_nonce = str(data.get("request_nonce") or "").strip()
    request_sig = str(data.get("request_sig") or "").strip()
    request_ts_raw = data.get("request_ts")
    expected_parent_scope_hash = resolve_parent_scope_hash(request, data)

    if not hardware_id or not session_token or not request_nonce or request_ts_raw is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="缺少必要参数")

    if not validate_hardware_id(hardware_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无效的硬件ID格式")

    if not validate_nonce_text(request_nonce):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="nonce格式无效")

    try:
        request_ts = int(request_ts_raw)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="请求时间戳格式无效")

    ts_ok, ts_error = validate_client_timestamp(request_ts, tolerance=300)
    if not ts_ok:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=ts_error)

    auth_header = str(request.headers.get("Authorization") or "").strip()
    if auth_header:
        if not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的Authorization头")
        header_token = str(auth_header[7:] or "").strip()
        if header_token != session_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="会话令牌不匹配")

    if not request_sig:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="缺少请求签名")

    sign_source = f"{hardware_id}|{session_token}|{request_nonce}|{request_ts}"
    expected_sig = hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        sign_source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(expected_sig.lower(), request_sig.lower()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="请求签名无效")

    if not consume_request_nonce("runtime_bundle_key", session_token, request_nonce, ttl_seconds=600):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="检测到重复请求")

    session = verify_client_session(db, session_token)
    if not session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="会话无效或已过期")
    if str(session.hardware_id or "").strip() != hardware_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="会话与硬件ID不匹配")

    is_banned, ban_reason = is_hardware_id_banned(db, hardware_id)
    if is_banned:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"硬件ID已被封禁: {ban_reason}")

    now_ts = get_current_timestamp()
    issued_at = now_ts
    expire_at = now_ts + 900
    license_key = normalize_license_key_text(session.license_key)
    license_obj = db.query(LicenseKey).filter(LicenseKey.key_string == license_key).first()
    if not license_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥不存在")
    if not license_obj.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥已禁用")
    if license_obj.expires_at and license_obj.expires_at < datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="许可证密钥已过期")

    key_type = str(license_obj.key_type or "").strip().upper()
    if is_executor_license_type(key_type):
        if not expected_parent_scope_hash:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="执行器授权码必须提供父级授权范围参数"
            )
        scope_ok, scope_status, scope_message = enforce_executor_parent_scope_hash(
            db,
            license_obj,
            expected_parent_scope_hash,
        )
        if not scope_ok:
            raise HTTPException(status_code=scope_status, detail=scope_message)

    runtime_key = build_runtime_bundle_key(hardware_id, session_token, license_key, request_nonce, issued_at)
    key_id = hashlib.sha256(f"{hardware_id}|{session_token}|{issued_at}".encode("utf-8")).hexdigest()[:24]

    response_source = f"{hardware_id}|{session_token}|{key_id}|{issued_at}|{expire_at}|{runtime_key}"
    response_sig = hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        response_source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return {
        "success": True,
        "message": "runtime bundle key issued",
        "online_master_key": runtime_key,
        "runtime_bundle_key": runtime_key,
        "bundle_key": runtime_key,
        "key_id": key_id,
        "issued_at": issued_at,
        "expire_at": expire_at,
        "request_nonce_echo": request_nonce,
        "request_ts_echo": request_ts,
        "sig": response_sig,
        "api_version": "2.1",
    }


@app.post("/api/client/export_runtime_key")
async def get_export_runtime_key(request: Request):
    """导出器在线运行时密钥接口（签名校验 + 防重放）。"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无效的JSON数据")

    seed_digest = str(data.get("seed_digest") or "").strip().lower()
    request_nonce = str(data.get("nonce") or "").strip()
    request_sig = str(data.get("sig") or "").strip()
    request_ts_raw = data.get("ts")

    if not seed_digest or not request_nonce or not request_sig or request_ts_raw is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="缺少必要参数")

    if re.fullmatch(r"[0-9a-f]{64}", seed_digest) is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="seed_digest格式无效")

    if not validate_nonce_text(request_nonce):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="nonce格式无效")

    try:
        request_ts = int(request_ts_raw)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="时间戳格式无效")

    ts_ok, ts_error = validate_client_timestamp(request_ts, tolerance=300)
    if not ts_ok:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=ts_error)

    if not consume_request_nonce("export_runtime_key", seed_digest, request_nonce, ttl_seconds=600):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="检测到重复请求")

    sign_source = f"{seed_digest}|{request_nonce}|{request_ts}"
    expected_sig = hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        sign_source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(expected_sig.lower(), request_sig.lower()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="签名校验失败")

    now_ts = get_current_timestamp()
    expire_at = now_ts + 900
    runtime_key = build_export_runtime_key(seed_digest, expire_at)
    key_id = hashlib.sha256(f"{seed_digest}|{expire_at}".encode("utf-8")).hexdigest()[:24]

    response_source = f"{seed_digest}|{key_id}|{expire_at}|{runtime_key}"
    response_sig = hmac.new(
        COMM_AUTH_SECRET_KEY.encode("utf-8"),
        response_source.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return {
        "success": True,
        "runtime_master_key": runtime_key,
        "online_master_key": runtime_key,
        "bundle_key": runtime_key,
        "key_id": key_id,
        "expire_at": expire_at,
        "request_nonce_echo": request_nonce,
        "request_ts_echo": request_ts,
        "sig": response_sig,
    }


@app.get("/api/admin/client_sessions")
async def get_client_sessions(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Get all active client sessions (admin)."""
    try:
        # 清理过期会话
        cleanup_expired_sessions(db)

        sessions = db.query(ClientSession).filter(
            ClientSession.is_active == True,
            ClientSession.expires_at > datetime.utcnow()
        ).all()

        session_list = []
        for session in sessions:
            session_data = {
                "id": session.id,
                "hardware_id": session.hardware_id,
                "license_key": mask_sensitive_data(session.license_key),
                "session_token": mask_sensitive_data(session.session_token),
                "created_at": format_beijing_time(session.created_at),
                "last_heartbeat": format_beijing_time(session.last_heartbeat),
                "expires_at": format_beijing_time(session.expires_at),
                "is_active": session.is_active
            }
            session_list.append(session_data)

        return {
            "success": True,
            "sessions": session_list,
            "total": len(session_list)
        }

    except Exception as e:
        logger.error(f"Get client session list failed {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Get client session list failed"
        )

@app.post("/api/admin/client_sessions/{session_id}/revoke")
async def revoke_client_session(session_id: int, request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """Revoke client session (admin)."""
    try:
        session = db.query(ClientSession).filter(ClientSession.id == session_id).first()
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="会话不存"
            )

        session.is_active = False
        db.commit()
        logger.info(f"管理员 {admin_user.username} 撤销了客户端会话: {mask_sensitive_data(session.hardware_id)}")

        return {
            "success": True,
            "message": "会话已撤销"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"撤销会话失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="撤销会话失败"
        )

@app.post("/api/admin/client_sessions/revoke_by_hardware")
async def revoke_sessions_by_hardware(request: Request, db: Session = Depends(get_db), admin_user: User = Depends(require_admin_auth)):
    """撤销某个硬件ID的所有会话（管理员功能）"""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    hardware_id = data.get("hardware_id")
    if not hardware_id or not validate_hardware_id(hardware_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的硬件ID"
        )

    try:
        count = db.query(ClientSession).filter(
            ClientSession.hardware_id == hardware_id,
            ClientSession.is_active == True
        ).update({"is_active": False})
        db.commit()

        logger.info(f"管理员 {admin_user.username} 撤销了硬件ID {mask_sensitive_data(hardware_id)} 的 {count} 个会话")

        return {
            "success": True,
            "message": f"已撤销 {count} 个会话",
            "revoked_count": count
        }

    except Exception as e:
        db.rollback()
        logger.error(f"撤销会话失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="撤销会话失败"
        )

@app.post("/api/admin/cards/export")
async def export_activation_cards(
    request: Request,
    admin_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Export activation cards (admin), supports TXT/CSV."""
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的JSON数据"
        )

    batch_id = data.get("batch_id")
    export_format = data.get("format", "txt").lower()  # txt 或 csv
    status_filter = data.get("status", "unused")  # 默认只导出未使用的

    if not batch_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="请指定批D"
        )

    try:
        # 查该批次的卡密
        query = db.query(ActivationCard).filter(ActivationCard.batch_id == batch_id)

        if status_filter:
            query = query.filter(ActivationCard.status == status_filter)

        cards = query.all()

        if not cards:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="未找到符合条件的卡密"
            )

        # 生成导出内
        if export_format == "csv":
            # CSV格式（io已在顶部导入
            output = io.StringIO()
            output.write("card_code,type,valid_days,status,created_at,notes\n")

            for card in cards:
                duration_text = "永久" if card.duration_days == 0 else f"{card.duration_days}天"
                created_time = format_beijing_time(card.created_at) if card.created_at else ""
                output.write(f"{card.card_code},{card.card_type},{duration_text},{card.status},{created_time},{card.notes or ''}\n")

            content = output.getvalue()
            output.close()
        else:
            # TXT格式 - 每不
            content = "\n".join([card.card_code for card in cards])

        logger.info(f"管理员 {admin_user.username} 导出了批次 {batch_id} 的卡密，共 {len(cards)} 张")

        return {
            "success": True,
            "content": content,
            "count": len(cards),
            "format": export_format,
            "batch_id": batch_id
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"导出卡密失败: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="导出卡密失败"
        )


if __name__ == "__main__":
    from start_server import main as start_server_main

    start_server_main()

