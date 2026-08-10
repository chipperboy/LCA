import unittest
from unittest import mock

import numpy as np

from tasks import ai_tool_task


class AiToolPluginCaptureTests(unittest.TestCase):
    def test_capture_ai_frame_uses_plugin_aware_capture_chain(self):
        frame = np.zeros((24, 32, 3), dtype=np.uint8)

        with mock.patch("tasks.task_utils.capture_window_smart", return_value=frame) as capture_window_smart:
            result = ai_tool_task._capture_ai_frame({}, 123)

        capture_window_smart.assert_called_once_with(
            hwnd=123,
            client_area_only=True,
            use_cache=False,
            capture_timeout=4.0,
        )
        self.assertIs(result["screenshot"], frame)
        self.assertEqual(result["img_w"], 32)
        self.assertEqual(result["img_h"], 24)


if __name__ == "__main__":
    unittest.main()
