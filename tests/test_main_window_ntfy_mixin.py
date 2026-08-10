import unittest

from ui.main_window_parts.main_window_ntfy_mixin import MainWindowNtfyMixin


class _MainWindowNtfyStub(MainWindowNtfyMixin):
    def __init__(self):
        self.config = {}
        self._ntfy_notifier = None
        self._reset_ntfy_execution_context()


class MainWindowNtfyMixinTests(unittest.TestCase):
    def test_build_finish_context_skips_failure_lines_when_stopped(self):
        window = _MainWindowNtfyStub()
        window._ntfy_session_context_lines = ["任务: 测试工作流"]
        window._ntfy_failure_context_lines = ["失败详情: 不应出现在停止通知里"]

        context_lines = window._build_ntfy_finish_context_lines(False, "stopped")

        self.assertEqual(context_lines, ["任务: 测试工作流"])

    def test_build_finish_context_keeps_failure_lines_for_failed_result(self):
        window = _MainWindowNtfyStub()
        window._ntfy_session_context_lines = ["任务: 测试工作流"]
        window._ntfy_failure_context_lines = ["失败详情: 执行失败"]

        context_lines = window._build_ntfy_finish_context_lines(False, "failed")

        self.assertEqual(
            context_lines,
            ["任务: 测试工作流", "失败详情: 执行失败"],
        )


if __name__ == "__main__":
    unittest.main()
