import logging
import unittest

from task_workflow.executor import WorkflowExecutor
from tasks.task_utils import resolve_step_action_result


class ExecutorCardNotificationTests(unittest.TestCase):
    def _build_executor(self):
        executor = WorkflowExecutor.__new__(WorkflowExecutor)
        executor._default_step_log_name = "测试工作流"
        executor.workflow_filepath = None
        executor.workflow_id = None
        executor.target_window_title = "测试窗口"
        executor.target_hwnd = 123
        executor._current_card_error_detail = ""
        executor._current_card_issue_logs = []
        executor._current_card_error_detail_level = logging.NOTSET
        executor._last_failure_card_id = None
        executor._last_failure_detail = ""
        executor._connections_map = {}
        return executor

    def test_card_push_includes_step_detail_and_task_detail(self):
        executor = self._build_executor()

        payload = executor._build_card_execution_notification_payload(
            card_id=1,
            task_type="OCR文字识别",
            card_obj={"id": 1, "task_type": "OCR文字识别"},
            card_params={
                "enable_card_ntfy_push": True,
                "card_ntfy_push_priority": "max",
            },
            success=True,
            next_card_id="工作流执行完成",
            task_detail="识别完成\n命中 3 个目标",
        )

        self.assertIsNotNone(payload)
        self.assertEqual("max", payload["priority"])
        self.assertEqual("card", payload["event_key"])
        message = payload["message"]
        self.assertIn("步骤详情: 执行成功: OCR文字识别 (ID: 1)，停止工作流", message)
        self.assertIn("执行明细: 识别完成", message)
        self.assertIn("命中 3 个目标", message)

    def test_card_push_uses_failure_detail_fallback(self):
        executor = self._build_executor()
        executor._current_card_error_detail = "窗口句柄失效"

        payload = executor._build_card_execution_notification_payload(
            card_id=2,
            task_type="点击",
            card_obj={"id": 2, "task_type": "点击"},
            card_params={
                "enable_card_ntfy_push": True,
                "card_ntfy_push_priority": "max",
            },
            success=False,
            next_card_id=None,
            task_detail="",
        )

        self.assertIsNotNone(payload)
        message = payload["message"]
        self.assertIn("步骤详情: 执行失败: 点击 (ID: 2)", message)
        self.assertIn("失败详情: 窗口句柄失效", message)

    def test_capture_failure_detail_only_during_card_execution(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = False
        executor._current_card_error_detail_level = logging.NOTSET

        executor._on_captured_error_log("不会被记录", logging.WARNING)
        self.assertEqual("", executor._current_card_error_detail)

        executor._capture_card_issue_logs = True
        executor._on_captured_error_log("未匹配到目标文字", logging.WARNING)
        self.assertIn("未匹配到目标文字", executor._current_card_error_detail)

        executor._on_captured_error_log("识别区域窗口不一致", logging.ERROR)
        self.assertIn("识别区域窗口不一致", executor._current_card_error_detail)

        executor._on_captured_error_log("较低等级警告不应覆盖错误", logging.WARNING)
        self.assertIn("识别区域窗口不一致", executor._current_card_error_detail)

    def test_generic_same_level_warning_does_not_override_specific_warning(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True
        executor._current_card_error_detail_level = logging.NOTSET

        executor._on_captured_error_log("未找到目标图片 test.png", logging.WARNING)
        executor._on_captured_error_log("点击失败，继续执行下一步", logging.WARNING)

        self.assertEqual("未找到目标图片 test.png", executor._current_card_error_detail)

    def test_info_level_failure_log_is_captured(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True
        executor._current_card_error_detail_level = logging.NOTSET

        executor._on_captured_error_log("开始执行模拟鼠标操作任务，模式: 找图功能", logging.INFO)
        self.assertEqual("", executor._current_card_error_detail)

        executor._on_captured_error_log("任务 '图片点击' (图片: '新版测试_8.bmp') 执行失败 (未找到或点击失败)。", logging.INFO)
        self.assertIn("图片点击失败：新版测试_8.bmp，原因：未找到或点击失败", executor._current_card_error_detail)

        executor._on_captured_error_log("[模板匹配] 分数: 0.3729, 阈值: 0.8000, 方法: local_engine", logging.INFO)
        executor._on_captured_error_log("[统一后台识别] 尝试 1: 未找到图片 (置信度 0.3729 < 阈值 0.8000)。", logging.INFO)
        self.assertIn("图片识别 尝试 1: 未找到图片 (置信度 0.3729 < 阈值 0.8000)。", executor._current_card_error_detail)
        self.assertIn("模板匹配分数 0.3729，要求至少 0.8000", executor._current_card_error_detail)

    def test_yolo_static_input_warning_is_not_captured_as_failure_detail(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True

        executor._on_captured_error_log("Input size override ignored: static model input shape", logging.WARNING)

        self.assertEqual("", executor._current_card_error_detail)

    def test_target_not_detected_is_normalized_for_display(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True

        executor._on_captured_error_log("Target not detected", logging.WARNING)

        self.assertEqual("未检测到目标", executor._current_card_error_detail)

    def test_internal_jump_parameters_are_not_exposed(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True
        executor._on_captured_error_log("跳转参数: 成功动作=执行下一步, 成功跳转ID=None, 失败动作=执行下一步, 失败跳转ID=None", logging.INFO)
        self.assertEqual("", executor._current_card_error_detail)

    def test_condition_control_internal_failure_message_is_simplified(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True
        executor._on_captured_error_log("条件不满足，执行失败操作: on_failure='执行下一步'", logging.INFO)
        self.assertEqual("条件不满足", executor._current_card_error_detail)

    def test_generic_task_failure_message_is_user_facing(self):
        executor = self._build_executor()
        executor._capture_card_issue_logs = True
        executor._on_captured_error_log("任务 '录制回放' 执行失败: 录制数据格式错误", logging.ERROR)
        self.assertEqual("录制回放失败：录制数据格式错误", executor._current_card_error_detail)

    def test_find_next_card_does_not_fallback_to_success_connection_when_failed(self):
        executor = self._build_executor()
        executor._connections_map = {
            4: [
                {"start_card_id": 4, "end_card_id": 5, "type": "success"},
            ]
        }

        next_card = executor._find_next_card(4, False)

        self.assertIsNone(next_card)

    def test_resolve_step_action_result_keeps_failure_detail(self):
        result = resolve_step_action_result(
            success=False,
            action="停止工作流",
            jump_id=None,
            card_id=16,
            detail="未匹配到目标文字",
        )
        self.assertEqual((False, "停止工作流", None, "未匹配到目标文字"), result)


if __name__ == "__main__":
    unittest.main()
