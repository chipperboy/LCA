import unittest
from unittest import mock

import numpy as np

from utils.yolo_engine import YOLOONNXEngine


class YoloEngineCaptureModeTests(unittest.TestCase):
    def test_plugin_mode_uses_plugin_capture_directly(self):
        engine = YOLOONNXEngine.__new__(YOLOONNXEngine)
        frame = np.zeros((4, 4, 3), dtype=np.uint8)

        with mock.patch("utils.yolo_engine.is_foreground_mode", side_effect=AssertionError("不应走原生前台判断")):
            with mock.patch.object(engine, "_plugin_capture", return_value=frame) as plugin_capture:
                result = engine._capture_window(123, "plugin")

        self.assertIs(result, frame)
        plugin_capture.assert_called_once_with(123)


if __name__ == "__main__":
    unittest.main()
