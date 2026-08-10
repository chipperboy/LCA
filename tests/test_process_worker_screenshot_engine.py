import unittest
from unittest.mock import mock_open, patch

from task_workflow.process_payload import build_process_workflow_payload
from task_workflow.process_worker import _resolve_worker_screenshot_engine


class ProcessWorkerScreenshotEngineTests(unittest.TestCase):
    def test_payload_carries_screenshot_engine(self):
        payload = build_process_workflow_payload(
            cards_data={},
            connections_data=[],
            execution_mode="foreground_driver",
            screenshot_engine="dxgi",
            images_dir=None,
            workflow_id="demo",
            start_card_id=1,
        )

        self.assertEqual(payload.get("screenshot_engine"), "dxgi")

    def test_worker_prefers_payload_screenshot_engine(self):
        resolved = _resolve_worker_screenshot_engine({"screenshot_engine": "gdi"})

        self.assertEqual(resolved, "gdi")

    def test_worker_falls_back_to_config_screenshot_engine(self):
        config_text = '{"screenshot_engine":"dxgi"}'
        with patch("task_workflow.process_worker.os.path.exists", return_value=True):
            with patch("task_workflow.process_worker.open", mock_open(read_data=config_text)):
                with patch("task_workflow.process_worker.get_config_path", return_value="C:\\\\fake\\\\config.json"):
                    resolved = _resolve_worker_screenshot_engine({})

        self.assertEqual(resolved, "dxgi")


if __name__ == "__main__":
    unittest.main()
