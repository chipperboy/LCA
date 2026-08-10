import unittest

from services.ai.provider_config import (
    OPENAI_API_PROTOCOL_CHAT_COMPLETIONS,
    OPENAI_API_PROTOCOL_RESPONSES,
    OPENAI_API_URL_MODE_BASE,
    OPENAI_API_URL_MODE_ENDPOINT,
    OPENAI_DEFAULT_BASE_URL,
    OPENAI_PROVIDER_MODE_COMPATIBLE,
    normalize_ai_api_protocol,
    normalize_ai_api_url_mode,
    normalize_ai_provider_mode,
    resolve_ai_api_base_url,
)


class AiProviderConfigTests(unittest.TestCase):
    def test_provider_mode_defaults_to_compatible(self):
        self.assertEqual(normalize_ai_provider_mode(""), OPENAI_PROVIDER_MODE_COMPATIBLE)

    def test_official_legacy_value_keeps_backward_compatible_alias(self):
        self.assertEqual(normalize_ai_provider_mode("OpenAI官方"), "OpenAI官方")

    def test_legacy_official_mode_allows_custom_base_url(self):
        base_url, error = resolve_ai_api_base_url(
            {
                "provider_mode": "OpenAI官方",
                "api_base_url": "https://capi.quan2go.com/openai",
            }
        )

        self.assertEqual(base_url, "https://capi.quan2go.com/openai")
        self.assertEqual(error, "")

    def test_empty_base_url_falls_back_to_official_default(self):
        base_url, error = resolve_ai_api_base_url(
            {
                "provider_mode": "自定义OpenAI兼容",
                "api_base_url": "",
            },
            env_base_url="",
        )

        self.assertEqual(base_url, OPENAI_DEFAULT_BASE_URL)
        self.assertEqual(error, "")

    def test_legacy_auto_protocol_uses_responses_for_base_url(self):
        self.assertEqual(
            normalize_ai_api_protocol("自动", api_base_url="https://api.openai.com/v1"),
            OPENAI_API_PROTOCOL_RESPONSES,
        )

    def test_legacy_auto_protocol_uses_chat_for_chat_endpoint_url(self):
        self.assertEqual(
            normalize_ai_api_protocol("自动", api_base_url="https://api.openai.com/v1/chat/completions"),
            OPENAI_API_PROTOCOL_CHAT_COMPLETIONS,
        )

    def test_legacy_auto_url_mode_uses_base_for_base_url(self):
        self.assertEqual(
            normalize_ai_api_url_mode("自动", api_base_url="https://api.openai.com/v1"),
            OPENAI_API_URL_MODE_BASE,
        )

    def test_legacy_auto_url_mode_uses_endpoint_for_full_endpoint_url(self):
        self.assertEqual(
            normalize_ai_api_url_mode("自动", api_base_url="https://api.openai.com/v1/responses"),
            OPENAI_API_URL_MODE_ENDPOINT,
        )


if __name__ == "__main__":
    unittest.main()
