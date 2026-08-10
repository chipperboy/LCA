import unittest
from pathlib import Path
from unittest import mock

from app_core import plugin_bridge


ROOT_DIR = Path(__file__).resolve().parents[1]


class PluginBridgeHelperTests(unittest.TestCase):
    def test_normalize_similarity_clamps_to_expected_range(self):
        self.assertEqual(plugin_bridge._normalize_similarity(-1.0), 0.0)
        self.assertEqual(plugin_bridge._normalize_similarity(2.0), 1.0)
        self.assertEqual(plugin_bridge._normalize_similarity("0.75"), 0.75)
        self.assertEqual(plugin_bridge._normalize_similarity("bad", default=0.6), 0.6)

    def test_check_plugin_authorization_uses_shared_activation_service(self):
        activation_result = mock.Mock(
            success=True,
            validation_enabled=False,
            message="",
        )

        with mock.patch.object(
            plugin_bridge,
            "prepare_plugin_mode_activation",
            return_value=activation_result,
        ) as activation_mock, mock.patch.object(
            plugin_bridge,
            "get_hardware_id",
            return_value="a" * 64,
        ):
            allowed, status = plugin_bridge._check_plugin_authorization()

        activation_mock.assert_called_once_with("a" * 64)
        self.assertEqual((allowed, status), (True, "validation_disabled"))

    def test_plugin_bridge_has_single_definition_for_shared_helpers(self):
        text = (ROOT_DIR / "app_core" / "plugin_bridge.py").read_text(encoding="utf-8")

        self.assertEqual(text.count("def _normalize_similarity("), 1)
        self.assertEqual(text.count("def _check_plugin_authorization("), 1)

    def test_start_authorization_check_skips_when_plugin_mode_disabled(self):
        plugin_bridge._authorization_check_thread = None
        plugin_bridge._authorization_status = None

        with mock.patch.object(
            plugin_bridge,
            "get_cached_config",
            return_value={"plugin_settings": {"enabled": False}},
        ), mock.patch.object(plugin_bridge.threading, "Thread") as thread_mock:
            plugin_bridge.start_authorization_check()

        thread_mock.assert_not_called()
        self.assertIsNone(plugin_bridge._authorization_status)


if __name__ == "__main__":
    unittest.main()
