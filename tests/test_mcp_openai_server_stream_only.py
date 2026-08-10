import unittest
from unittest.mock import patch

from services.mcp import mcp_openai_server


class McpOpenaiServerStreamOnlyTests(unittest.TestCase):
    def setUp(self):
        mcp_openai_server._STREAM_ONLY_ENDPOINT_CACHE.clear()

    def tearDown(self):
        mcp_openai_server._STREAM_ONLY_ENDPOINT_CACHE.clear()

    def test_protocol_probe_uses_message_input_for_responses(self):
        with patch.object(mcp_openai_server, "_post_openai_json", return_value={"id": "resp_test"}) as mock_post:
            result = mcp_openai_server._openai_protocol_probe(
                api_base_url="https://example.com/openai",
                api_key="test-key",
                model="gpt-5.4",
                timeout_seconds=10.0,
                provider_mode="自定义OpenAI兼容",
                api_protocol="responses",
                api_url_mode="接口基地址",
            )

        payload = mock_post.call_args.kwargs["payload"]
        self.assertEqual(result["response_id"], "resp_test")
        self.assertIsInstance(payload["input"], list)
        self.assertEqual(payload["input"][0]["type"], "message")
        self.assertEqual(payload["input"][0]["content"][0]["type"], "input_text")

    def test_openai_raw_retries_stream_when_provider_requires_stream(self):
        stream_only_error = RuntimeError(
            "HTTP 400 for url 'https://example.com/openai/responses': only support stream"
        )
        with patch.object(mcp_openai_server, "_post_openai_json", side_effect=stream_only_error), patch.object(
            mcp_openai_server,
            "_post_openai_stream_text",
            return_value="OK",
        ) as mock_stream:
            result = mcp_openai_server._openai_raw(
                image_base64="ZmFrZQ==",
                prompt="Reply with exactly OK and nothing else.",
                api_base_url="https://example.com/openai",
                api_key="test-key",
                model="gpt-5.4",
                timeout_seconds=10.0,
                provider_mode="自定义OpenAI兼容",
                api_protocol="responses",
                api_url_mode="接口基地址",
                image_mime_type="image/png",
            )

        payload = mock_stream.call_args.kwargs["payload"]
        self.assertEqual(result["output_text"], "OK")
        self.assertIsInstance(payload["input"], list)
        self.assertEqual(payload["input"][0]["content"][0]["type"], "input_text")

    def test_openai_raw_skips_json_when_stream_only_cached(self):
        cache_key = mcp_openai_server._build_stream_only_cache_key(
            api_base_url="https://example.com/openai",
            api_protocol="responses",
            provider_mode="自定义OpenAI兼容",
            api_url_mode="接口基地址",
            model="gpt-5.4",
        )
        mcp_openai_server._STREAM_ONLY_ENDPOINT_CACHE[cache_key] = True

        with patch.object(mcp_openai_server, "_post_openai_json") as mock_post, patch.object(
            mcp_openai_server,
            "_post_openai_stream_text",
            return_value="OK",
        ):
            result = mcp_openai_server._openai_raw(
                image_base64="ZmFrZQ==",
                prompt="Reply with exactly OK and nothing else.",
                api_base_url="https://example.com/openai",
                api_key="test-key",
                model="gpt-5.4",
                timeout_seconds=10.0,
                provider_mode="自定义OpenAI兼容",
                api_protocol="responses",
                api_url_mode="接口基地址",
                image_mime_type="image/png",
            )

        mock_post.assert_not_called()
        self.assertEqual(result["output_text"], "OK")


if __name__ == "__main__":
    unittest.main()
