import unittest
from unittest.mock import patch

from tasks import ai_tool_task


class AiToolRuntimeOptimizationTests(unittest.TestCase):
    def setUp(self):
        ai_tool_task._AI_PROTOCOL_SUPPORT_CACHE.clear()

    def tearDown(self):
        ai_tool_task._AI_PROTOCOL_SUPPORT_CACHE.clear()

    def test_probe_skips_network_when_no_cache_exists(self):
        with patch.object(ai_tool_task, "_call_mcp_tool", side_effect=AssertionError("should not probe")):
            result = ai_tool_task._probe_ai_protocol_support_if_needed(
                provider_mode="自定义OpenAI兼容",
                api_protocol="responses",
                api_url_mode="接口基地址",
                api_base_url="https://example.com/openai",
                api_key="test-key",
                model="gpt-5.4",
                timeout_seconds=10.0,
            )

        self.assertEqual(result, "")

    def test_execute_plan_local_applies_region_offset_after_scaling(self):
        captured = {}

        def _fake_click(step, execution_mode, target_hwnd, window_region):
            captured["step"] = dict(step)
            return {"task": "点击指定坐标", "success": True, "message": "ok", "next_card_id": None}

        with patch.object(ai_tool_task, "_execute_click_action_local", side_effect=_fake_click):
            result = ai_tool_task._execute_plan_local(
                steps=[
                    {
                        "action": "click",
                        "x": 0.5,
                        "y": 0.25,
                        "scale": 1,
                        "coordinate_mode": "客户区坐标",
                    }
                ],
                execution_mode="普通模式",
                target_hwnd=123,
                window_region=None,
                stop_on_failure=True,
                img_w=200,
                img_h=100,
                scale_mode="自动(推荐)",
                coordinate_offset=(10, 20),
            )

        self.assertTrue(result["success"])
        self.assertEqual(captured["step"]["x"], 110)
        self.assertEqual(captured["step"]["y"], 45)

    def test_execute_task_reports_requesting_and_parsing_status(self):
        statuses = []

        def _fake_update_runtime_parameter(param_name, value, card_id, executor):
            if param_name == "runtime_status":
                statuses.append(str(value))

        params = {
            "api_key": "test-key",
            "provider_mode": "自定义OpenAI兼容",
            "api_protocol": "chat_completions",
            "api_url_mode": "接口基地址",
            "api_base_url": "https://example.com/v1",
            "model": "gpt-5.4",
            "command_prompt": "根据当前截图点击发送按钮",
            "timeout_seconds": 10.0,
            "enable_retry": False,
        }

        with patch.object(ai_tool_task, "_clear_runtime_parameters"), \
             patch.object(ai_tool_task, "_update_runtime_parameter", side_effect=_fake_update_runtime_parameter), \
             patch.object(ai_tool_task, "_resolve_ai_api_base_url", return_value=("https://example.com/v1", "")), \
             patch.object(ai_tool_task, "_probe_ai_protocol_support_if_needed", return_value=""), \
             patch.object(ai_tool_task, "_capture_ai_frame", return_value={"screenshot": object(), "img_w": 100, "img_h": 100}), \
             patch.object(ai_tool_task, "_encode_image_to_base64", return_value=("abc", "image/png")), \
             patch.object(ai_tool_task, "_call_mcp_tool", return_value={"output_text": "{}"}), \
             patch.object(ai_tool_task, "_parse_and_validate_command_plan", return_value=({"status": "completed"}, [], "completed", "完成", "")), \
             patch.object(ai_tool_task, "handle_success_action", return_value=(True, "ok", None)):
            result = ai_tool_task.execute_task(
                params=params,
                counters={},
                execution_mode="普通模式",
                target_hwnd=123,
                window_region=None,
                card_id=6,
                executor=None,
                stop_checker=lambda: False,
            )

        self.assertTrue(result[0])
        self.assertTrue(any("请求AI中" in item for item in statuses))
        self.assertTrue(any("解析AI响应中" in item for item in statuses))

    def test_execute_task_routes_general_chat_to_direct_mode_without_window(self):
        statuses = []

        def _fake_update_runtime_parameter(param_name, value, card_id, executor):
            if param_name == "runtime_status":
                statuses.append(str(value))

        params = {
            "api_key": "test-key",
            "provider_mode": "自定义OpenAI兼容",
            "api_protocol": "chat_completions",
            "api_url_mode": "接口基地址",
            "api_base_url": "https://example.com/v1",
            "model": "gpt-5.4",
            "command_prompt": "简单介绍一下你自己",
            "timeout_seconds": 10.0,
            "enable_retry": False,
        }

        with patch.object(ai_tool_task, "_clear_runtime_parameters"), \
             patch.object(ai_tool_task, "_update_runtime_parameter", side_effect=_fake_update_runtime_parameter), \
             patch.object(ai_tool_task, "_update_runtime_output"), \
             patch.object(ai_tool_task, "_resolve_ai_api_base_url", return_value=("https://example.com/v1", "")), \
             patch.object(ai_tool_task, "_probe_ai_protocol_support_if_needed", return_value=""), \
             patch.object(ai_tool_task, "_request_text_response", return_value={"output_text": "我是助手"}), \
             patch.object(ai_tool_task, "handle_success_action", return_value=(True, "ok", None)):
            result = ai_tool_task.execute_task(
                params=params,
                counters={},
                execution_mode="普通模式",
                target_hwnd=None,
                window_region=None,
                card_id=6,
                executor=None,
                stop_checker=lambda: False,
            )

        self.assertTrue(result[0])
        self.assertTrue(any("直接对话请求AI中" in item for item in statuses))
        self.assertTrue(any("直接对话完成" in item for item in statuses))

    def test_execute_task_keeps_tool_mode_for_ui_command(self):
        params = {
            "command_prompt": "根据当前截图点击发送按钮",
        }

        with patch.object(ai_tool_task, "_clear_runtime_parameters"), \
             patch.object(ai_tool_task, "_update_runtime_parameter"), \
             patch.object(ai_tool_task, "_execute_continuous_command_mode", return_value=(True, "ok", None)) as mock_exec:
            result = ai_tool_task.execute_task(
                params=params,
                counters={},
                execution_mode="普通模式",
                target_hwnd=123,
                window_region=None,
                card_id=6,
                executor=None,
                stop_checker=lambda: False,
            )

        self.assertTrue(result[0])
        mock_exec.assert_called_once()

    def test_timeout_resolution_separates_chat_and_tool_defaults(self):
        params = {}

        self.assertEqual(
            ai_tool_task._resolve_direct_chat_timeout_seconds(params),
            ai_tool_task.DEFAULT_DIRECT_CHAT_TIMEOUT_SECONDS,
        )
        self.assertEqual(
            ai_tool_task._resolve_continuous_command_timeout_seconds(params),
            ai_tool_task.DEFAULT_CONTINUOUS_COMMAND_TIMEOUT_SECONDS,
        )

    def test_timeout_resolution_keeps_legacy_timeout_for_backward_compatibility(self):
        params = {"timeout_seconds": 35}

        self.assertEqual(ai_tool_task._resolve_direct_chat_timeout_seconds(params), 35.0)
        self.assertEqual(ai_tool_task._resolve_continuous_command_timeout_seconds(params), 35.0)

    def test_timeout_resolution_prefers_new_dedicated_fields(self):
        params = {
            "timeout_seconds": 35,
            "chat_timeout_seconds": 18,
            "tool_timeout_seconds": 70,
        }

        self.assertEqual(ai_tool_task._resolve_direct_chat_timeout_seconds(params), 18.0)
        self.assertEqual(ai_tool_task._resolve_continuous_command_timeout_seconds(params), 70.0)

    def test_disconnect_without_response_is_retryable(self):
        exc = RuntimeError("Server disconnected without sending a response")

        self.assertTrue(ai_tool_task._should_retry_exception(exc))

    def test_disconnect_without_response_is_formatted_in_chinese(self):
        exc = RuntimeError("Server disconnected without sending a response")

        self.assertEqual(
            ai_tool_task._format_ai_error_message(exc),
            "连接 OpenAI 服务失败：服务端在返回数据前断开连接。",
        )


if __name__ == "__main__":
    unittest.main()
