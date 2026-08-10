import unittest
from unittest import mock

from app_core import license_runtime
from app_core import license_store
from app_core import runtime_security


class RuntimeSecurityTests(unittest.TestCase):
    def test_runtime_guard_is_noop_after_anti_debug_removal(self):
        guard = mock.Mock()

        runtime_security.configure_runtime_security(guard_cb=guard, validator_cb=None)
        encrypted = license_store.encrypt_license_key("KEY-001", "a" * 64)

        self.assertTrue(encrypted)
        guard.assert_not_called()

    def test_runtime_validator_no_longer_blocks_local_validation(self):
        validator = mock.Mock(return_value=False)

        runtime_security.configure_runtime_security(guard_cb=None, validator_cb=validator)
        result = license_runtime.validate_license_with_server_v2("a" * 64, "ANY-KEY")

        validator.assert_not_called()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 200)
        self.assertEqual(result[2], "LOCAL_ONLY")


if __name__ == "__main__":
    unittest.main()
