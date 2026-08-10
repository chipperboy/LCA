import unittest
from unittest import mock

from ui.system_parts import update_manager


class _DummySignal:
    def __init__(self):
        self.callbacks = []

    def connect(self, callback):
        self.callbacks.append(callback)


class _FakeTimer:
    def __init__(self, parent=None):
        self.parent = parent
        self.timeout = _DummySignal()
        self.started = []
        self.active = False
        self.deleted = False

    def start(self, interval_ms):
        self.started.append(interval_ms)
        self.active = True

    def stop(self):
        self.active = False

    def deleteLater(self):
        self.deleted = True

    def isActive(self):
        return self.active


class _FakeThread:
    def __init__(self):
        self.join_calls = []
        self._alive = True

    def is_alive(self):
        return self._alive

    def join(self, timeout=None):
        self.join_calls.append(timeout)
        self._alive = False


class UpdateManagerTests(unittest.TestCase):
    def setUp(self):
        self.update_enabled_patch = mock.patch.object(update_manager, "_CLIENT_SOFTWARE_UPDATE_ENABLED", True)
        self.update_enabled_patch.start()

    def tearDown(self):
        self.update_enabled_patch.stop()

    def test_check_now_starts_updater_when_needed(self):
        fake_thread = _FakeThread()
        with mock.patch("ui.system_parts.update_manager.QTimer", _FakeTimer), mock.patch(
            "ui.system_parts.update_manager.spawn_updater_process",
            return_value=fake_thread,
        ) as spawn_mock, mock.patch(
            "ui.system_parts.update_manager.check_update_now"
        ) as check_now_mock:
            integration = update_manager.UpdateIntegration(object())
            integration.check_now()

        spawn_mock.assert_called_once_with(check_interval=3600)
        check_now_mock.assert_called_once_with()
        self.assertTrue(integration._is_running)
        self.assertIsInstance(integration.status_timer, _FakeTimer)
        self.assertEqual(integration.status_timer.started, [update_manager.STATUS_POLL_INTERVAL_MS])

    def test_disabled_update_check_does_not_start_updater(self):
        with mock.patch.object(update_manager, "_CLIENT_SOFTWARE_UPDATE_ENABLED", False), mock.patch(
            "ui.system_parts.update_manager.spawn_updater_process"
        ) as spawn_mock, mock.patch("ui.system_parts.update_manager.check_update_now") as check_now_mock:
            integration = update_manager.UpdateIntegration(object())
            integration.check_now()

        spawn_mock.assert_not_called()
        check_now_mock.assert_not_called()
        self.assertFalse(integration._is_running)

    def test_ready_status_re_notifies_after_snooze(self):
        status_payload = {
            "status": update_manager.UPDATE_STATUS_READY,
            "data": {"new_version": "2.0.0", "changelog": ["fix"]},
        }
        with mock.patch(
            "ui.system_parts.update_manager.get_update_status",
            return_value=status_payload,
        ), mock.patch(
            "ui.system_parts.update_manager.UpdateNotificationDialog"
        ) as dialog_cls, mock.patch(
            "ui.system_parts.update_manager.time.time",
            side_effect=[0.0, 0.0, 5.0, 11.0, 11.0],
        ):
            dialog_cls.return_value.exec.side_effect = [
                int(update_manager.QDialog.DialogCode.Rejected),
                int(update_manager.QDialog.DialogCode.Rejected),
            ]
            integration = update_manager.UpdateIntegration(object())
            integration._check_interval = 10

            integration._poll_status()
            integration._poll_status()
            integration._poll_status()

        self.assertEqual(dialog_cls.call_count, 2)

    def test_install_request_relies_on_updater_status_instead_of_tasklist_probe(self):
        fake_thread = _FakeThread()
        with mock.patch("ui.system_parts.update_manager.QTimer", _FakeTimer), mock.patch(
            "ui.system_parts.update_manager.spawn_updater_process",
            return_value=fake_thread,
        ), mock.patch(
            "ui.system_parts.update_manager.request_install"
        ) as request_install_mock, mock.patch(
            "ui.system_parts.update_manager.QMessageBox.information"
        ) as info_mock:
            integration = update_manager.UpdateIntegration(object())
            integration._do_install()

        request_install_mock.assert_called_once_with()
        info_mock.assert_called_once()
        self.assertTrue(integration._pending_install_request)

        with mock.patch(
            "ui.system_parts.update_manager.get_update_status",
            return_value={"status": update_manager.UPDATE_STATUS_INSTALLING, "data": {}},
        ), mock.patch("ui.system_parts.update_manager.QApplication.quit") as quit_mock:
            integration._poll_status()

        quit_mock.assert_called_once_with()
        self.assertFalse(integration._pending_install_request)

    def test_install_timeout_shows_warning(self):
        integration = update_manager.UpdateIntegration(object())
        integration._pending_install_request = True
        integration._install_requested_at = 0.0

        with mock.patch(
            "ui.system_parts.update_manager.time.time",
            return_value=update_manager.INSTALL_START_TIMEOUT_SEC + 1,
        ), mock.patch(
            "ui.system_parts.update_manager.QMessageBox.warning"
        ) as warning_mock:
            integration._handle_install_timeout()

        warning_mock.assert_called_once()
        self.assertFalse(integration._pending_install_request)


if __name__ == "__main__":
    unittest.main()
