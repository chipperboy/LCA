import unittest

from app_core.client_identity import sanitize_error_message
from utils.log_message_translator import translate_log_message


class LogMessageTranslatorTests(unittest.TestCase):
    def test_translate_server_disconnect_message(self):
        self.assertEqual(
            translate_log_message("Server disconnected without sending a response"),
            "服务端在返回数据前断开连接",
        )

    def test_translate_license_network_message(self):
        self.assertEqual(
            translate_log_message("network connectivity check failed: Connection refused"),
            "网络连通性检查失败： 连接被拒绝",
        )

    def test_translate_bind_request_message(self):
        self.assertEqual(
            translate_log_message("bind request failed: 500 - server error"),
            "绑定请求失败： 500 - 服务端 error",
        )

    def test_translate_function_address_message(self):
        self.assertEqual(
            translate_log_message("Failed to get function address for CreateABC"),
            "获取函数地址失败： CreateABC",
        )

    def test_sanitize_error_message_uses_translation(self):
        self.assertEqual(
            sanitize_error_message("Server disconnected without sending a response"),
            "服务端在返回数据前断开连接",
        )


if __name__ == "__main__":
    unittest.main()
