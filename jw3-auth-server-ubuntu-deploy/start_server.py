#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JW3 授权验证服务启动脚本。"""

import argparse
import os
import sys
from pathlib import Path

from runtime_env import apply_default_environment, resolve_security_environment

SCRIPT_DIR = Path(__file__).resolve().parent


def resolve_runtime_path(raw_path: str) -> str:
    path_text = str(raw_path or "").strip()
    if not path_text:
        return ""
    path = Path(path_text)
    if not path.is_absolute():
        path = SCRIPT_DIR / path
    return str(path.resolve())


def setup_environment() -> None:
    """设置非敏感默认环境变量。"""
    apply_default_environment(str(SCRIPT_DIR))


def validate_security_environment() -> None:
    """校验安全相关环境变量。"""
    resolve_security_environment(os.environ)


def check_ssl_certificates() -> tuple[bool, str | None, str | None]:
    """检查 SSL 证书文件。"""
    ssl_keyfile = resolve_runtime_path(os.environ.get("SSL_KEYFILE", ""))
    ssl_certfile = resolve_runtime_path(os.environ.get("SSL_CERTFILE", ""))

    if ssl_keyfile and ssl_certfile:
        key_exists = os.path.exists(ssl_keyfile)
        cert_exists = os.path.exists(ssl_certfile)
        if key_exists and cert_exists:
            return True, ssl_keyfile, ssl_certfile

        print("警告: SSL证书文件不存在")
        print(f"  密钥文件: {ssl_keyfile} ({'存在' if key_exists else '不存在'})")
        print(f"  证书文件: {ssl_certfile} ({'存在' if cert_exists else '不存在'})")
        return False, None, None

    return False, None, None


def build_uvicorn_config(
    args: argparse.Namespace,
    use_ssl: bool,
    ssl_keyfile: str | None,
    ssl_certfile: str | None,
) -> dict:
    forwarded_allow_ips = str(os.environ.get("FORWARDED_ALLOW_IPS", "127.0.0.1,::1") or "").strip()
    config = {
        "app": "auth_server:app",
        "app_dir": str(SCRIPT_DIR),
        "host": args.host,
        "port": args.port,
        "log_level": args.log_level,
        "reload": args.reload,
        "proxy_headers": True,
        "forwarded_allow_ips": forwarded_allow_ips,
    }
    if use_ssl:
        config.update(
            {
                "ssl_keyfile": ssl_keyfile,
                "ssl_certfile": ssl_certfile,
            }
        )
    return config


def main() -> None:
    """主入口。"""
    parser = argparse.ArgumentParser(description="JW3 授权验证服务端")
    parser.add_argument("--host", default="0.0.0.0", help="绑定主机地址")
    parser.add_argument("--port", type=int, default=8000, help="绑定端口")
    parser.add_argument("--no-ssl", action="store_true", help="禁用SSL")
    parser.add_argument("--reload", action="store_true", help="启用自动重载（开发模式）")
    parser.add_argument("--log-level", default="info", choices=["debug", "info", "warning", "error"], help="日志级别")
    args = parser.parse_args()

    setup_environment()
    try:
        validate_security_environment()
    except RuntimeError as exc:
        print(f"错误: {exc}")
        sys.exit(1)

    use_ssl, ssl_keyfile, ssl_certfile = check_ssl_certificates()
    if args.no_ssl:
        use_ssl = False

    try:
        import uvicorn
    except ImportError:
        print("错误: 未安装 uvicorn，请先安装后再启动")
        sys.exit(1)

    config = build_uvicorn_config(args, use_ssl=use_ssl, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)

    if use_ssl:
        print(f"启动HTTPS服务器: https://{args.host}:{args.port}")
    else:
        print(f"启动HTTP服务器: http://{args.host}:{args.port}")
        print("警告: 未使用SSL加密，生产环境建议启用HTTPS")

    print(f"管理员账户: {os.environ.get('ADMIN_USERNAME')}")
    print(f"数据库: {os.environ.get('DATABASE_URL')}")
    print(f"自动重载: {'启用' if args.reload else '禁用'}")
    print("=" * 50)

    try:
        uvicorn.run(**config)
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as exc:
        print(f"服务器启动失败: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
