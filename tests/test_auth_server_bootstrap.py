import importlib.util
import os
import sys
import unittest
from pathlib import Path
from unittest import mock


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AUTH_SERVER_DIR = PROJECT_ROOT / "jw3-auth-server-ubuntu-deploy"
BOOTSTRAP_MODULES = (
    "runtime_env",
    "start_server",
    "auth_server",
    "market_models",
    "market_router",
    "market_schemas",
)


class AuthServerBootstrapTests(unittest.TestCase):
    def tearDown(self):
        for module_name in BOOTSTRAP_MODULES:
            sys.modules.pop(module_name, None)

    def _load_module(self, module_name: str, filename: str):
        sys.path.insert(0, str(AUTH_SERVER_DIR))
        try:
            module_path = AUTH_SERVER_DIR / filename
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            self.assertIsNotNone(spec)
            self.assertIsNotNone(spec.loader)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module
        finally:
            if sys.path and sys.path[0] == str(AUTH_SERVER_DIR):
                sys.path.pop(0)

    def test_build_default_database_url_points_to_data_dir(self):
        runtime_env = self._load_module("runtime_env", "runtime_env.py")

        self.assertEqual(
            runtime_env.build_default_database_url(str(AUTH_SERVER_DIR)),
            f"sqlite:///{(AUTH_SERVER_DIR / 'data' / 'jw3_auth.db').as_posix()}",
        )

    def test_resolve_security_environment_requires_explicit_values(self):
        runtime_env = self._load_module("runtime_env", "runtime_env.py")

        with self.assertRaisesRegex(RuntimeError, "SECRET_KEY"):
            runtime_env.resolve_security_environment({"ADMIN_PASSWORD": "unit-test-admin"})

        with self.assertRaisesRegex(RuntimeError, "ADMIN_PASSWORD"):
            runtime_env.resolve_security_environment({"SECRET_KEY": "x" * 24})

    def test_setup_environment_uses_shared_defaults(self):
        runtime_env = self._load_module("runtime_env", "runtime_env.py")
        start_server = self._load_module("start_server", "start_server.py")

        with mock.patch.dict(os.environ, {}, clear=True):
            start_server.setup_environment()

            self.assertEqual(
                os.environ["DATABASE_URL"],
                runtime_env.build_default_database_url(str(AUTH_SERVER_DIR)),
            )
            self.assertEqual(
                os.environ["SSL_KEYFILE"],
                str(AUTH_SERVER_DIR / "jw3.top" / "Nginx_PEM" / "jw3.top.key"),
            )
            self.assertEqual(
                os.environ["SSL_CERTFILE"],
                str(AUTH_SERVER_DIR / "jw3.top" / "Nginx_PEM" / "jw3.top.crt"),
            )

    def test_check_ssl_certificates_resolves_relative_paths_without_chdir(self):
        start_server = self._load_module("start_server", "start_server.py")
        expected_key = str((AUTH_SERVER_DIR / "certs" / "server.key").resolve())
        expected_cert = str((AUTH_SERVER_DIR / "certs" / "server.crt").resolve())

        with mock.patch.dict(
            os.environ,
            {"SSL_KEYFILE": "certs/server.key", "SSL_CERTFILE": "certs/server.crt"},
            clear=True,
        ), mock.patch.object(
            start_server.os.path,
            "exists",
            side_effect=lambda path: path in {expected_key, expected_cert},
        ):
            exists, key_path, cert_path = start_server.check_ssl_certificates()

        self.assertTrue(exists)
        self.assertEqual(key_path, expected_key)
        self.assertEqual(cert_path, expected_cert)

    def test_build_uvicorn_config_uses_app_dir_instead_of_chdir(self):
        start_server = self._load_module("start_server", "start_server.py")
        args = mock.Mock(host="127.0.0.1", port=9443, log_level="warning", reload=True)

        config = start_server.build_uvicorn_config(
            args,
            use_ssl=True,
            ssl_keyfile="key.pem",
            ssl_certfile="cert.pem",
        )

        self.assertEqual(config["app"], "auth_server:app")
        self.assertEqual(config["app_dir"], str(AUTH_SERVER_DIR))
        self.assertEqual(config["ssl_keyfile"], "key.pem")
        self.assertEqual(config["ssl_certfile"], "cert.pem")
        self.assertNotIn("os.chdir", (AUTH_SERVER_DIR / "start_server.py").read_text(encoding="utf-8"))

    def test_validate_security_environment_raises_without_admin_password(self):
        start_server = self._load_module("start_server", "start_server.py")

        with mock.patch.dict(os.environ, {"SECRET_KEY": "x" * 24}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "ADMIN_PASSWORD"):
                start_server.validate_security_environment()

    def test_auth_server_import_requires_security_environment(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "SECRET_KEY"):
                self._load_module("auth_server", "auth_server.py")

    def test_resolve_comm_auth_secret_requires_env_or_file(self):
        with mock.patch.dict(
            os.environ,
            {
                "SECRET_KEY": "x" * 24,
                "ADMIN_PASSWORD": "unit-test-admin-password",
                "AUTH_SECRET_KEY": "y" * 24,
            },
            clear=False,
        ):
            auth_server = self._load_module("auth_server", "auth_server.py")

        with mock.patch.dict(os.environ, {"AUTH_SECRET_KEY": ""}, clear=False), mock.patch.object(
            auth_server.os.path,
            "isfile",
            return_value=False,
        ):
            with self.assertRaisesRegex(RuntimeError, "AUTH_SECRET_KEY"):
                auth_server._resolve_comm_auth_secret()

    def test_resolve_comm_auth_secret_uses_script_relative_path_without_getcwd(self):
        with mock.patch.dict(
            os.environ,
            {
                "SECRET_KEY": "x" * 24,
                "ADMIN_PASSWORD": "unit-test-admin-password",
                "AUTH_SECRET_KEY": "y" * 24,
            },
            clear=False,
        ):
            auth_server = self._load_module("auth_server", "auth_server.py")

        secret_rel_path = "custom/secret.txt"
        expected_path = str((AUTH_SERVER_DIR / secret_rel_path).resolve())
        mocked_open = mock.mock_open(read_data="z" * 24)

        with mock.patch.dict(
            os.environ,
            {"AUTH_SECRET_KEY": "", auth_server._COMM_AUTH_SECRET_FILE_ENV: secret_rel_path},
            clear=False,
        ), mock.patch.object(
            auth_server.os,
            "getcwd",
            side_effect=AssertionError("should not read cwd"),
        ), mock.patch.object(
            auth_server.os.path,
            "isfile",
            side_effect=lambda path: path == expected_path,
        ), mock.patch(
            "builtins.open",
            mocked_open,
        ):
            self.assertEqual(auth_server._resolve_comm_auth_secret(), "z" * 24)

        mocked_open.assert_called_once_with(expected_path, "r", encoding="utf-8")

    def test_auth_server_main_block_delegates_to_start_server(self):
        source = (AUTH_SERVER_DIR / "auth_server.py").read_text(encoding="utf-8")

        self.assertIn("from start_server import main as start_server_main", source)
        self.assertIn("start_server_main()", source)


if __name__ == "__main__":
    unittest.main()
