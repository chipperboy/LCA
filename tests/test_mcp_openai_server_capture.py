import base64
import unittest
from unittest import mock

import numpy as np

from services.mcp import mcp_openai_server


class McpOpenaiServerCaptureTests(unittest.TestCase):
    def test_capture_window_uses_plugin_capture_when_plugin_enabled(self):
        plugin_img = np.zeros((18, 28, 3), dtype=np.uint8)

        with mock.patch("app_core.plugin_bridge.is_plugin_enabled", return_value=True):
            with mock.patch("app_core.plugin_bridge.plugin_capture", return_value=plugin_img) as plugin_capture:
                with mock.patch.object(
                    mcp_openai_server,
                    "win32gui",
                    mock.Mock(GetClientRect=mock.Mock(return_value=(0, 0, 28, 18))),
                ):
                    result = mcp_openai_server._capture_window(321, client_area_only=True)

        plugin_capture.assert_called_once_with(hwnd=321, x1=0, y1=0, x2=28, y2=18)
        self.assertEqual(result["width"], 28)
        self.assertEqual(result["height"], 18)
        self.assertTrue(base64.b64decode(result["image_base64"]))


if __name__ == "__main__":
    unittest.main()
