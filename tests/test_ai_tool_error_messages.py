import unittest

from tasks.ai_tool_task import _format_ai_error_message


class AiToolErrorMessageTests(unittest.TestCase):
    def test_404_error_includes_endpoint_hint(self):
        message = _format_ai_error_message(
            RuntimeError("HTTP 404 for url 'https://capi.quan2go.com/openai/chat/completions': Not Found")
        )

        self.assertIn("HTTP 404", message)
        self.assertIn("https://capi.quan2go.com/openai/chat/completions", message)
        self.assertIn("版本前缀", message)
        self.assertIn("协议路径", message)


if __name__ == "__main__":
    unittest.main()
