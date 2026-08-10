import tempfile
import unittest
from pathlib import Path
from unittest import mock

from utils import updater


class UpdaterCliTests(unittest.TestCase):
    def test_configure_cli_logging_uses_file_handler_for_daemon_mode(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_ipc_dir = Path(temp_dir) / "ipc"
            fake_file_handler = mock.Mock()
            with mock.patch.object(updater, "IPC_DIR", temp_ipc_dir), mock.patch(
                "utils.updater.logging.FileHandler",
                return_value=fake_file_handler,
            ) as file_handler_mock, mock.patch(
                "utils.updater.logging.basicConfig"
            ) as basic_config_mock:
                updater.configure_cli_logging(True)

        file_handler_mock.assert_called_once_with(temp_ipc_dir / "updater.log", encoding="utf-8")
        basic_config_mock.assert_called_once_with(
            level=updater.logging.INFO,
            format=updater.UPDATER_LOG_FORMAT,
            handlers=[fake_file_handler],
        )

    def test_configure_cli_logging_uses_stream_handler_for_interactive_mode(self):
        fake_stream_handler = mock.Mock()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_ipc_dir = Path(temp_dir) / "ipc"
            with mock.patch.object(updater, "IPC_DIR", temp_ipc_dir), mock.patch(
                "utils.updater.logging.StreamHandler",
                return_value=fake_stream_handler,
            ) as stream_handler_mock, mock.patch(
                "utils.updater.logging.basicConfig"
            ) as basic_config_mock:
                updater.configure_cli_logging(False)

        stream_handler_mock.assert_called_once_with()
        basic_config_mock.assert_called_once_with(
            level=updater.logging.INFO,
            format=updater.UPDATER_LOG_FORMAT,
            handlers=[fake_stream_handler],
        )

    def test_main_uses_shared_daemon_flow(self):
        with mock.patch("utils.updater.configure_cli_logging") as configure_logging_mock, mock.patch(
            "utils.updater.start_updater_daemon"
        ) as start_daemon_mock:
            result = updater.main(["--daemon", "--interval", "15", "--main-pid", "42"])

        self.assertEqual(result, 0)
        configure_logging_mock.assert_called_once_with(True)
        start_daemon_mock.assert_called_once_with(check_interval=15, main_pid=42)

    def test_main_uses_shared_interactive_flow(self):
        with mock.patch("utils.updater.configure_cli_logging") as configure_logging_mock, mock.patch(
            "utils.updater.run_interactive_updater"
        ) as interactive_mock:
            result = updater.main([])

        self.assertEqual(result, 0)
        configure_logging_mock.assert_called_once_with(False)
        interactive_mock.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
