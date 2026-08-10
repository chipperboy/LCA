import unittest

from services.ai.command_routing import command_requires_tool_execution


class AiCommandRoutingTests(unittest.TestCase):
    def test_general_chat_does_not_require_tool_execution(self):
        self.assertFalse(command_requires_tool_execution("简单介绍一下你自己"))

    def test_screen_or_ui_action_requires_tool_execution(self):
        self.assertTrue(command_requires_tool_execution("根据当前截图点击发送按钮"))
        self.assertTrue(command_requires_tool_execution("在浏览器地址栏输入 https://openai.com"))


if __name__ == "__main__":
    unittest.main()
