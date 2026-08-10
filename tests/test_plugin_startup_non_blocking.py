import threading
import time
import unittest
from unittest import mock

from app_core import app_runtime_bootstrap
from app_core import plugin_bridge
from ui.main_window_parts.main_window_hotkey_plugin_mixin import (
    MainWindowHotkeyPluginMixin,
)


class _HotkeyWindowStub(MainWindowHotkeyPluginMixin):
    def __init__(self):
        self.config = {}
        self.original_mode_calls = 0

    def _update_hotkeys(self):
        pass

    def _update_hotkeys_original_mode(self):
        self.original_mode_calls += 1


class PluginStartupNonBlockingTests(unittest.TestCase):
    def tearDown(self):
        plugin_bridge.reset_plugin_manager_runtime_state(reset_config=False)

    def test_background_plugin_initialization_returns_immediately(self):
        worker_started = threading.Event()
        worker_release = threading.Event()

        def _fake_initialize_plugin_system():
            worker_started.set()
            worker_release.wait(timeout=2.0)

        with mock.patch(
            "app_core.plugin_bridge.initialize_plugin_system",
            side_effect=_fake_initialize_plugin_system,
        ), mock.patch(
            "app_core.plugin_bridge.start_authorization_check",
            return_value=None,
        ):
            start = time.perf_counter()
            plugin_thread = app_runtime_bootstrap.initialize_plugin_system_background(timeout_seconds=3.0)
            elapsed = time.perf_counter() - start

            self.assertIsNotNone(plugin_thread)
            self.assertLess(elapsed, 0.3)
            self.assertTrue(worker_started.wait(timeout=1.0))
            self.assertTrue(plugin_thread.is_alive())

            worker_release.set()
            plugin_thread.join(timeout=1.0)

    def test_get_plugin_manager_wait_false_does_not_block_during_running_init(self):
        plugin_bridge._set_plugin_manager_init_state("running")

        start = time.perf_counter()
        plugin_manager = plugin_bridge.get_plugin_manager(wait=False)
        elapsed = time.perf_counter() - start

        self.assertIsNone(plugin_manager)
        self.assertLess(elapsed, 0.1)

    def test_plugin_hotkey_update_defers_while_plugin_is_initializing(self):
        window = _HotkeyWindowStub()

        with mock.patch(
            "app_core.plugin_bridge.get_plugin_manager_initialization_state",
            return_value="running",
        ), mock.patch(
            "app_core.plugin_bridge.get_plugin_manager",
            return_value=None,
        ), mock.patch(
            "ui.main_window_parts.main_window_hotkey_plugin_mixin.QTimer.singleShot",
        ) as single_shot:
            window._update_hotkeys_plugin_mode()

        self.assertEqual(window.original_mode_calls, 0)
        single_shot.assert_called_once()
        self.assertTrue(window._plugin_hotkey_retry_pending)


if __name__ == "__main__":
    unittest.main()
