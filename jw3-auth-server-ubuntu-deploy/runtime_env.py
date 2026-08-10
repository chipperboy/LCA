#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JW3 授权服务运行时环境辅助。"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping


WEAK_SECRET_VALUES = frozenset(
    {
        "your-secret-key-change-in-production",
        "default-secret-key",
        "changeme",
    }
)
MIN_SECRET_KEY_LENGTH = 24


@dataclass(frozen=True)
class SecurityEnvironment:
    secret_key: str
    admin_password: str


def build_default_database_url(script_dir: str) -> str:
    database_path = (Path(script_dir).resolve() / "data" / "jw3_auth.db").as_posix()
    return f"sqlite:///{database_path}"


def apply_default_environment(script_dir: str) -> None:
    script_path = Path(script_dir).resolve()
    default_config = {
        "DATABASE_URL": build_default_database_url(str(script_path)),
        "ADMIN_USERNAME": "admin",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "SSL_KEYFILE": str(script_path / "jw3.top" / "Nginx_PEM" / "jw3.top.key"),
        "SSL_CERTFILE": str(script_path / "jw3.top" / "Nginx_PEM" / "jw3.top.crt"),
    }
    for key, value in default_config.items():
        os.environ.setdefault(key, value)


def _is_weak_secret(secret_key: str) -> bool:
    normalized = str(secret_key or "").strip()
    return len(normalized) < MIN_SECRET_KEY_LENGTH or normalized.lower() in WEAK_SECRET_VALUES


def resolve_security_environment(env: Mapping[str, str]) -> SecurityEnvironment:
    secret_key = str(env.get("SECRET_KEY", "") or "").strip()
    admin_password = str(env.get("ADMIN_PASSWORD", "") or "").strip()
    errors = []

    if _is_weak_secret(secret_key):
        errors.append(f"SECRET_KEY 未配置或不安全，请设置长度至少 {MIN_SECRET_KEY_LENGTH} 的安全值")

    if not admin_password:
        errors.append("ADMIN_PASSWORD 未配置，请显式设置管理员密码")

    if errors:
        raise RuntimeError("；".join(errors))

    return SecurityEnvironment(secret_key=secret_key, admin_password=admin_password)
