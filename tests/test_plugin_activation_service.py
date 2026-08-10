import unittest
from unittest import mock

from app_core import plugin_activation_service


class PluginActivationServiceTests(unittest.TestCase):
    def test_prepare_plugin_mode_activation_allows_valid_hardware_id_locally(self):
        with mock.patch.object(
            plugin_activation_service,
            "set_validation_session",
            return_value="local-token",
        ) as session_mock:
            result = plugin_activation_service.prepare_plugin_mode_activation("a" * 64)

        session_mock.assert_called_once_with()
        self.assertTrue(result.success)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.license_type, "LOCAL_ONLY")
        self.assertFalse(result.validation_enabled)
        self.assertFalse(result.requires_license_input)

    def test_prepare_plugin_mode_activation_rejects_invalid_hardware_id(self):
        result = plugin_activation_service.prepare_plugin_mode_activation("")

        self.assertFalse(result.success)
        self.assertEqual(result.title, plugin_activation_service.ERROR_TITLE)

    def test_validate_plugin_license_key_succeeds_locally(self):
        session = mock.Mock()

        with mock.patch.object(
            plugin_activation_service,
            "set_validation_session",
            return_value="local-token",
        ) as session_mock:
            result = plugin_activation_service.validate_plugin_license_key(
                "a" * 64,
                "KEY-001",
                session,
            )

        session_mock.assert_called_once_with()
        self.assertTrue(result.success)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.license_type, "LOCAL_ONLY")
        self.assertFalse(result.validation_enabled)

    def test_validate_plugin_license_key_still_requires_non_empty_input(self):
        result = plugin_activation_service.validate_plugin_license_key(
            "a" * 64,
            "",
            mock.Mock(),
        )

        self.assertFalse(result.success)
        self.assertEqual(result.title, plugin_activation_service.LICENSE_EMPTY_TITLE)


if __name__ == "__main__":
    unittest.main()
