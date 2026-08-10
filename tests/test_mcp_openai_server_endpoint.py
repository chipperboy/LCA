import unittest

from services.mcp import mcp_openai_server


class McpOpenaiServerEndpointTests(unittest.TestCase):
    def test_compatible_mode_uses_custom_endpoint_as_is(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://capi.quan2go.com/openai",
            api_protocol="chat_completions",
            provider_mode="自定义OpenAI兼容",
            api_url_mode="完整请求地址",
        )

        self.assertEqual(endpoint, "https://capi.quan2go.com/openai")

    def test_compatible_mode_base_url_appends_chat_completions_path(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://capi.quan2go.com/openai",
            api_protocol="chat_completions",
            provider_mode="自定义OpenAI兼容",
            api_url_mode="接口基地址",
        )

        self.assertEqual(endpoint, "https://capi.quan2go.com/openai/chat/completions")

    def test_compatible_mode_base_url_appends_responses_path(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://capi.quan2go.com/openai",
            api_protocol="responses",
            provider_mode="自定义OpenAI兼容",
            api_url_mode="接口基地址",
        )

        self.assertEqual(endpoint, "https://capi.quan2go.com/openai/responses")

    def test_official_mode_appends_chat_completions_path(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://api.openai.com/v1",
            api_protocol="chat_completions",
            provider_mode="OpenAI官方",
        )

        self.assertEqual(endpoint, "https://api.openai.com/v1/chat/completions")

    def test_official_mode_appends_responses_path(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://api.openai.com/v1",
            api_protocol="responses",
            provider_mode="OpenAI官方",
        )

        self.assertEqual(endpoint, "https://api.openai.com/v1/responses")

    def test_official_mode_can_use_custom_endpoint_as_is(self):
        endpoint = mcp_openai_server._build_openai_endpoint(
            api_base_url="https://capi.quan2go.com/openai",
            api_protocol="chat_completions",
            provider_mode="OpenAI官方",
            api_url_mode="完整请求地址",
        )

        self.assertEqual(endpoint, "https://capi.quan2go.com/openai")


if __name__ == "__main__":
    unittest.main()
