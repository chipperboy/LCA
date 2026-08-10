import json
import unittest

from ui.main_window_parts.main_window_ai_cli_mixin import MainWindowAiCliMixin


class _SessionProcessStub:
    def __init__(self):
        self.terminated = False

    def poll(self):
        return None if not self.terminated else 0

    def terminate(self):
        self.terminated = True


class _CardStub:
    def __init__(self, task_type="AI工具", parameters=None, custom_name=""):
        self.task_type = task_type
        self.parameters = dict(parameters or {})
        self.custom_name = custom_name


class _WorkflowViewStub:
    def __init__(self, cards):
        self.cards = dict(cards)


class _WorkflowTabWidgetStub:
    def __init__(self, current_task_id, task_views):
        self._current_task_id = current_task_id
        self.task_views = dict(task_views)
        self.task_to_tab = {task_id: index for index, task_id in enumerate(task_views.keys())}
        self.current_index = self.task_to_tab.get(current_task_id, 0)

    def get_current_task_id(self):
        return self._current_task_id

    def currentIndex(self):
        return self.current_index

    def setCurrentIndex(self, index):
        self.current_index = index
        reverse_map = {value: key for key, value in self.task_to_tab.items()}
        if index in reverse_map:
            self._current_task_id = reverse_map[index]

    def set_current_task_id(self, task_id):
        self._current_task_id = task_id
        self.current_index = self.task_to_tab.get(task_id, self.current_index)

    def _rebuild_mappings(self):
        return None


class _TaskStub:
    def __init__(self, name):
        self.name = name


class _TaskManagerStub:
    def __init__(self, tasks):
        self._tasks = dict(tasks)

    def get_task(self, task_id):
        return self._tasks.get(task_id)


class _MainWindowAiCliStub(MainWindowAiCliMixin):
    def __init__(self, task_cards):
        task_views = {}
        tasks = {}
        for task_id, payload in task_cards.items():
            task_views[task_id] = _WorkflowViewStub(payload["cards"])
            tasks[task_id] = _TaskStub(payload["name"])
        first_task_id = next(iter(task_views.keys()))
        self._active_execution_task_id = first_task_id
        self.workflow_view = task_views[first_task_id]
        self.workflow_tab_widget = _WorkflowTabWidgetStub(first_task_id, task_views)
        self.task_manager = _TaskManagerStub(tasks)
        self.executor_thread = None
        self._execution_started_flag = False
        self.control_center = None
        self.logged_messages = []
        self.started_cards = []
        self._ai_cli_sessions = {}
        self._ai_cli_runtime_param_overrides = {}
        self._ai_cli_hub = {
            "log_path": "memory://hub",
            "input_path": "",
            "state_path": "",
            "process": _SessionProcessStub(),
            "input_offset": 0,
            "input_remainder": "",
            "last_state_json": "",
            "last_processed_command_id": "",
            "active_session_key": "",
        }

    def _init_ai_cli_dialog(self):
        self._ai_cli_sessions = {}
        self._ai_cli_runtime_param_overrides = {}
        self._ai_cli_hub = {
            "log_path": "memory://hub",
            "input_path": "",
            "state_path": "",
            "process": _SessionProcessStub(),
            "input_offset": 0,
            "input_remainder": "",
            "last_state_json": "",
            "last_processed_command_id": "",
            "active_session_key": "",
        }

    def _ensure_ai_cli_hub(self, start_if_missing=True):
        return self._ai_cli_hub

    def _append_ai_cli_log(self, session, text):
        self.logged_messages.append(str(text))

    def _sync_ai_cli_hub_state(self):
        return None

    def _handle_test_card_execution(self, card_id):
        self.started_cards.append((self.workflow_tab_widget.get_current_task_id(), int(card_id)))


class MainWindowAiCliMixinTests(unittest.TestCase):
    def test_card_started_creates_session_with_task_card_key_and_banner(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "测试工作流",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "看看群里在讨论什么"}, custom_name="群聊总结")
                    },
                }
            }
        )

        window._handle_ai_cli_card_started(6)

        self.assertIn("11:6", window._ai_cli_sessions)
        self.assertEqual(window._ai_cli_hub["active_session_key"], "11:6")
        self.assertIn("[会话] 11:6", window.logged_messages[-1])
        self.assertIn("群聊总结", window.logged_messages[-1])

    def test_multiple_sessions_share_single_hub_and_isolate_same_card_id(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "工作流A",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "A任务"}, custom_name="AI甲")
                    },
                },
                12: {
                    "name": "工作流B",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "B任务"}, custom_name="AI乙")
                    },
                },
            }
        )

        hub = window._ensure_ai_cli_hub()
        window._handle_ai_cli_card_started(6)
        window._active_execution_task_id = 12
        window.workflow_tab_widget.set_current_task_id(12)
        window.workflow_view = window.workflow_tab_widget.task_views[12]
        window._handle_ai_cli_card_started(6)

        self.assertIs(window._ensure_ai_cli_hub(), hub)
        self.assertIn("11:6", window._ai_cli_sessions)
        self.assertIn("12:6", window._ai_cli_sessions)
        self.assertEqual(len(window._ai_cli_sessions), 2)

    def test_list_and_use_commands_switch_active_session(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "工作流A",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "A任务"}, custom_name="AI甲")
                    },
                },
                12: {
                    "name": "工作流B",
                    "cards": {
                        7: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "B任务"}, custom_name="AI乙")
                    },
                },
            }
        )
        window._handle_ai_cli_card_started(6)
        window._active_execution_task_id = 12
        window.workflow_tab_widget.set_current_task_id(12)
        window.workflow_view = window.workflow_tab_widget.task_views[12]
        window._handle_ai_cli_card_started(7)

        window._handle_ai_cli_input_payload({"id": "1", "text": "/list"})
        window._handle_ai_cli_input_payload({"id": "2", "text": "/use 11:6"})

        self.assertIn("[会话列表]", window.logged_messages[-2])
        self.assertEqual(window._ai_cli_hub["active_session_key"], "11:6")
        self.assertIn("当前会话已切换为 11:6", window.logged_messages[-1])

    def test_send_routes_tool_command_to_active_session_and_preserves_original_prompt(self):
        card = _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "先看看群里在讨论什么"})
        window = _MainWindowAiCliStub({11: {"name": "测试工作流", "cards": {6: card}}})
        window._handle_ai_cli_card_started(6)

        window._handle_ai_cli_input_payload({"id": "cmd_1", "text": "/send 继续，根据当前截图把消息发出去"})
        window._drain_ai_cli_command_queue()

        self.assertEqual(window.started_cards, [(11, 6)])
        self.assertEqual(card.parameters["command_prompt"], "先看看群里在讨论什么")
        override = window._ai_cli_runtime_param_overrides["11:6"]["command_prompt"]
        self.assertIn("原始任务：", override)
        self.assertIn("继续，根据当前截图把消息发出去", override)
        self.assertEqual(window._ai_cli_runtime_param_overrides["11:6"]["ai_cli_route_mode"], "tool")

    def test_send_routes_general_chat_to_direct_chat_mode(self):
        card = _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "先看看群里在讨论什么"})
        window = _MainWindowAiCliStub({11: {"name": "测试工作流", "cards": {6: card}}})
        window._handle_ai_cli_card_started(6)

        window._handle_ai_cli_input_payload({"id": "cmd_1", "text": "/send 简单介绍一下你自己"})
        window._drain_ai_cli_command_queue()

        self.assertEqual(window.started_cards, [(11, 6)])
        override = window._ai_cli_runtime_param_overrides["11:6"]
        self.assertEqual(override["command_prompt"], "简单介绍一下你自己")
        self.assertEqual(override["ai_cli_route_mode"], "chat")
        self.assertEqual(override["ai_chat_history"], [])

    def test_local_model_query_is_answered_immediately(self):
        card = _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "测试", "model": "gpt-5.4"})
        window = _MainWindowAiCliStub({11: {"name": "测试工作流", "cards": {6: card}}})
        window._handle_ai_cli_card_started(6)

        window._handle_ai_cli_input_payload({"id": "cmd_1", "text": "/send 你是什么模型"})

        self.assertEqual(window.started_cards, [])
        self.assertFalse(window._ai_cli_sessions["11:6"]["pending_user_commands"])
        self.assertIn("当前会话使用的模型是 gpt-5.4。", window.logged_messages[-1])

    def test_runtime_override_is_isolated_by_task_and_card(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "工作流A",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "A任务"})
                    },
                },
                12: {
                    "name": "工作流B",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "B任务"})
                    },
                },
            }
        )
        window._ai_cli_runtime_param_overrides["11:6"] = {"command_prompt": "A覆盖"}
        window._ai_cli_runtime_param_overrides["12:6"] = {"command_prompt": "B覆盖"}

        window._active_execution_task_id = 11
        window.workflow_tab_widget.set_current_task_id(11)
        window.workflow_view = window.workflow_tab_widget.task_views[11]
        params_a = window._apply_ai_cli_runtime_parameter_overrides(6, {"command_prompt": "原始A"})

        window._active_execution_task_id = 12
        window.workflow_tab_widget.set_current_task_id(12)
        window.workflow_view = window.workflow_tab_widget.task_views[12]
        params_b = window._apply_ai_cli_runtime_parameter_overrides(6, {"command_prompt": "原始B"})

        self.assertEqual(params_a["command_prompt"], "A覆盖")
        self.assertEqual(params_b["command_prompt"], "B覆盖")

    def test_finish_clears_runtime_override_and_marks_dialog_suppression(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "测试工作流",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "测试"})
                    },
                }
            }
        )
        context = window._resolve_ai_cli_card_context(6)
        session = window._ensure_ai_cli_session(context)
        session["current_prompt_override"] = "继续执行"

        window._handle_ai_cli_card_started(6)
        self.assertTrue(session["suppress_completion_dialog"])

        window._handle_ai_cli_runtime_update(6, "response_format_hint", '{"status":"completed","ok":true}')
        window._handle_ai_cli_card_finished(6, True)

        self.assertNotIn("11:6", window._ai_cli_runtime_param_overrides)
        self.assertTrue(window._consume_ai_cli_completion_dialog_suppression())

    def test_continuous_output_is_summarized(self):
        text = _MainWindowAiCliStub._normalize_ai_cli_output_text(
            json.dumps(
                {
                    "mode": "continuous",
                    "status": "completed",
                    "reason": "已经把内容填进输入框",
                    "rounds": [{"round": 1}, {"round": 2}],
                },
                ensure_ascii=False,
            )
        )
        self.assertEqual(text, "状态: completed\n轮数: 2\n结论: 已经把内容填进输入框")

    def test_trace_text_is_compacted(self):
        compact = _MainWindowAiCliStub._compact_ai_cli_trace_text(
            "\n".join(
                [
                    "第1轮 规划状态: running | 阶段: 填入输入框 - 当前截图已经在目标群聊界面",
                    "第1轮 预期结果: 执行后输入框出现总结文本",
                    "第1轮 计划: 点击 消息输入框 @ 948,1146；输入 一大段非常非常长非常非常长非常非常长非常非常长非常非常长的内容",
                    "第1轮 执行: 第1步 点击指定坐标 成功(执行下一步)；第2步 模拟键盘操作 成功(执行下一步)",
                ]
            )
        )
        self.assertIn("第1轮 规划状态: running | 阶段: 填入输入框", compact)
        self.assertNotIn("预期结果", compact)
        self.assertIn("第1轮计划:", compact)
        self.assertIn("第1轮执行:", compact)

    def test_launch_script_uses_ascii_and_real_console(self):
        script = _MainWindowAiCliStub._build_ai_cli_launch_script("ai_cli_hub.ps1", "LCA AI CLI")

        script.encode("ascii")
        self.assertIn(r'"%SystemRoot%\System32\chcp.com" 65001>nul', script)
        self.assertIn(r'"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"', script)
        self.assertIn(r'"%~dp0ai_cli_hub.ps1"', script)

    def test_bridge_script_supports_multi_session_commands(self):
        script = _MainWindowAiCliStub._build_ai_cli_bridge_script("a.log", "a.inbox", "a.state.json")

        self.assertIn("/list", script)
        self.assertIn("/use", script)
        self.assertIn("/send", script)
        self.assertIn("active_prompt", script)
        self.assertIn("KeyAvailable", script)
        self.assertIn("Consume-Input", script)
        self.assertNotIn("Read-Host $prompt", script)

    def test_pending_activity_detects_running_session(self):
        window = _MainWindowAiCliStub(
            {
                11: {
                    "name": "测试工作流",
                    "cards": {
                        6: _CardStub(parameters={"enable_ai_cli_dialog": True, "command_prompt": "测试"})
                    },
                }
            }
        )

        window._handle_ai_cli_card_started(6)

        self.assertTrue(window._has_ai_cli_pending_activity())


if __name__ == "__main__":
    unittest.main()
