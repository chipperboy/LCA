import importlib.util
import logging
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AUTH_SERVER_DIR = PROJECT_ROOT / "jw3-auth-server-ubuntu-deploy"
AUTH_SERVER_PATH = AUTH_SERVER_DIR / "auth_server.py"
AUTH_SERVER_MODULES = (
    "auth_server",
    "market_models",
    "market_router",
    "market_schemas",
)


class AuthServerRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.root_logger = logging.getLogger()
        self.original_root_handlers = list(self.root_logger.handlers)
        self.original_root_level = self.root_logger.level
        self.auth_logger = logging.getLogger("jw3-auth-server")
        self.original_auth_handlers = list(self.auth_logger.handlers)
        self.original_auth_filters = list(self.auth_logger.filters)
        self.original_auth_level = self.auth_logger.level
        self.original_auth_propagate = self.auth_logger.propagate

    def tearDown(self):
        for handler in self.root_logger.handlers:
            if handler not in self.original_root_handlers:
                try:
                    handler.close()
                except Exception:
                    pass
        self.root_logger.handlers = self.original_root_handlers
        self.root_logger.setLevel(self.original_root_level)

        for handler in self.auth_logger.handlers:
            if handler not in self.original_auth_handlers:
                try:
                    handler.close()
                except Exception:
                    pass
        self.auth_logger.handlers = self.original_auth_handlers
        self.auth_logger.filters = self.original_auth_filters
        self.auth_logger.setLevel(self.original_auth_level)
        self.auth_logger.propagate = self.original_auth_propagate

        for module_name in AUTH_SERVER_MODULES:
            sys.modules.pop(module_name, None)

    def _load_auth_server(self):
        env = {
            "SECRET_KEY": "unit-test-secret-key-0123456789",
            "ADMIN_PASSWORD": "unit-test-admin-password",
            "DATABASE_URL": "sqlite:///:memory:",
        }
        sys.path.insert(0, str(AUTH_SERVER_DIR))
        try:
            spec = importlib.util.spec_from_file_location("auth_server", AUTH_SERVER_PATH)
            self.assertIsNotNone(spec)
            self.assertIsNotNone(spec.loader)
            module = importlib.util.module_from_spec(spec)
            sys.modules["auth_server"] = module
            with mock.patch.dict(os.environ, env, clear=False):
                spec.loader.exec_module(module)
            return module
        finally:
            if sys.path and sys.path[0] == str(AUTH_SERVER_DIR):
                sys.path.pop(0)

    def test_import_has_no_runtime_side_effects(self):
        with mock.patch("logging.basicConfig") as basic_config_mock, mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all"
        ) as create_all_mock, mock.patch("os.makedirs") as makedirs_mock:
            module = self._load_auth_server()

        self.assertIsNotNone(module)
        basic_config_mock.assert_not_called()
        create_all_mock.assert_not_called()
        makedirs_mock.assert_not_called()

    def test_configure_server_logging_is_idempotent(self):
        module = self._load_auth_server()
        self.root_logger.handlers = []
        self.auth_logger.filters = []

        with tempfile.TemporaryDirectory() as temp_dir:
            module.LOG_DIR = os.path.join(temp_dir, "logs")
            module.DATA_DIR = os.path.join(temp_dir, "data")
            module.STATIC_DIR = os.path.join(temp_dir, "static")
            module.TEMPLATES_DIR = os.path.join(temp_dir, "templates")
            module._SERVER_LOG_FILE = os.path.join(module.LOG_DIR, "auth_server.log")
            module._SERVER_LOGGING_CONFIGURED = False

            module._configure_server_logging()
            module._configure_server_logging()

            file_handlers = [
                handler for handler in self.root_logger.handlers if getattr(handler, "baseFilename", "")
            ]
            stream_handlers = [
                handler
                for handler in self.root_logger.handlers
                if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler)
            ]

            self.assertEqual(len(file_handlers), 1)
            self.assertEqual(len(stream_handlers), 1)
            self.assertEqual(
                module._normalize_abs_path(file_handlers[0].baseFilename),
                module._normalize_abs_path(module._SERVER_LOG_FILE),
            )

            for handler in self.root_logger.handlers:
                self.assertEqual(
                    sum(existing is module._mojibake_sanitizer for existing in handler.filters),
                    1,
                )
            self.assertEqual(
                sum(existing is module._mojibake_sanitizer for existing in module.logger.filters),
                1,
            )

            for handler in list(self.root_logger.handlers):
                try:
                    handler.close()
                except Exception:
                    pass
            self.root_logger.handlers = []

    def test_initialize_runtime_storage_is_lazy_and_idempotent(self):
        module = self._load_auth_server()
        module._RUNTIME_STORAGE_INITIALIZED = False

        with mock.patch.object(module, "_ensure_runtime_directories") as ensure_dirs_mock, mock.patch.object(
            module.Base.metadata,
            "create_all",
        ) as create_all_mock, mock.patch.object(module, "ensure_runtime_schema") as ensure_schema_mock:
            module._initialize_runtime_storage()
            module._initialize_runtime_storage()

        ensure_dirs_mock.assert_called_once()
        create_all_mock.assert_called_once_with(bind=module.engine)
        ensure_schema_mock.assert_called_once()

    def test_static_and_template_paths_use_deploy_directory(self):
        module = self._load_auth_server()

        static_mount = next(route for route in module.app.routes if getattr(route, "path", "") == "/static")

        self.assertEqual(Path(module.STATIC_DIR), AUTH_SERVER_DIR / "static")
        self.assertEqual(Path(module.TEMPLATES_DIR), AUTH_SERVER_DIR / "templates")
        self.assertEqual(Path(static_mount.app.directory), AUTH_SERVER_DIR / "static")
        self.assertIn(str(AUTH_SERVER_DIR / "templates"), module.templates.env.loader.searchpath)


if __name__ == "__main__":
    unittest.main()
