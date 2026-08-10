import unittest

from services.ai.provider_config import (
    OPENAI_API_PROTOCOL_OPTIONS,
    OPENAI_API_PROTOCOL_RESPONSES,
    OPENAI_API_URL_MODE_BASE,
    OPENAI_API_URL_MODE_OPTIONS,
    OPENAI_PROVIDER_MODE_COMPATIBLE,
)
from tasks import ai_tool_task


class AiToolParamsDefinitionTests(unittest.TestCase):
    def test_provider_mode_only_exposes_compatible_option(self):
        params = ai_tool_task.get_params_definition()
        self.assertEqual(params["provider_mode"]["options"], [OPENAI_PROVIDER_MODE_COMPATIBLE])
        self.assertEqual(params["provider_mode"]["default"], OPENAI_PROVIDER_MODE_COMPATIBLE)

    def test_api_base_url_default_is_empty(self):
        params = ai_tool_task.get_params_definition()
        self.assertEqual(params["api_base_url"]["default"], "")

    def test_protocol_and_url_mode_require_manual_selection(self):
        params = ai_tool_task.get_params_definition()
        self.assertEqual(
            params["api_protocol"]["options"],
            OPENAI_API_PROTOCOL_OPTIONS,
        )
        self.assertEqual(
            params["api_url_mode"]["options"],
            OPENAI_API_URL_MODE_OPTIONS,
        )
        self.assertEqual(params["api_protocol"]["default"], OPENAI_API_PROTOCOL_RESPONSES)
        self.assertEqual(params["api_url_mode"]["default"], OPENAI_API_URL_MODE_BASE)

    def test_ai_cli_dialog_switch_is_available(self):
        params = ai_tool_task.get_params_definition()
        self.assertIn("enable_ai_cli_dialog", params)
        self.assertEqual(params["enable_ai_cli_dialog"]["type"], "bool")
        self.assertFalse(params["enable_ai_cli_dialog"]["default"])

    def test_chat_and_tool_timeout_fields_are_available(self):
        params = ai_tool_task.get_params_definition()
        self.assertIn("chat_timeout_seconds", params)
        self.assertIn("tool_timeout_seconds", params)
        self.assertEqual(params["chat_timeout_seconds"]["type"], "float")
        self.assertEqual(params["tool_timeout_seconds"]["type"], "float")
        self.assertEqual(
            params["chat_timeout_seconds"]["default"],
            ai_tool_task.DEFAULT_DIRECT_CHAT_TIMEOUT_SECONDS,
        )
        self.assertEqual(
            params["tool_timeout_seconds"]["default"],
            ai_tool_task.DEFAULT_CONTINUOUS_COMMAND_TIMEOUT_SECONDS,
        )


if __name__ == "__main__":
    unittest.main()
