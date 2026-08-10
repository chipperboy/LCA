import unittest
from unittest.mock import patch

from utils.ntfy_push import (
    CARD_NTFY_ENABLED_PARAM,
    CARD_NTFY_PRIORITY_PARAM,
    DEFAULT_CARD_NTFY_PRIORITY,
    NtfyExecutionNotifier,
    get_card_ntfy_push_param_definitions,
    normalize_card_ntfy_push_settings,
    normalize_ntfy_settings,
    publish_ntfy_message,
)


class NtfyPushTests(unittest.TestCase):
    def test_card_push_param_definitions_default_to_disabled(self):
        definitions = get_card_ntfy_push_param_definitions()

        self.assertIn(CARD_NTFY_ENABLED_PARAM, definitions)
        self.assertIn(CARD_NTFY_PRIORITY_PARAM, definitions)
        self.assertFalse(definitions[CARD_NTFY_ENABLED_PARAM]["default"])
        self.assertEqual(
            definitions[CARD_NTFY_PRIORITY_PARAM]["default"],
            DEFAULT_CARD_NTFY_PRIORITY,
        )
        self.assertEqual(
            definitions[CARD_NTFY_PRIORITY_PARAM]["condition"],
            {"param": CARD_NTFY_ENABLED_PARAM, "value": True},
        )

    def test_normalize_card_push_settings_uses_disabled_default(self):
        settings = normalize_card_ntfy_push_settings({})

        self.assertFalse(settings["enabled"])
        self.assertEqual(settings["priority"], DEFAULT_CARD_NTFY_PRIORITY)

    def test_normalize_card_push_settings_accepts_priority_alias(self):
        settings = normalize_card_ntfy_push_settings(
            {
                CARD_NTFY_ENABLED_PARAM: True,
                CARD_NTFY_PRIORITY_PARAM: "5",
            }
        )

        self.assertTrue(settings["enabled"])
        self.assertEqual(settings["priority"], "max")

    def test_normalize_ntfy_settings_drops_progress_priority(self):
        settings = normalize_ntfy_settings(
            {
                "enabled": True,
                "server_url": "https://ntfy.sh",
                "topic": "demo",
                "interval_seconds": 60,
                "priorities": {
                    "start": "high",
                    "progress": "max",
                    "success": "low",
                    "failure": "5",
                },
            }
        )

        self.assertNotIn("interval_seconds", settings)
        self.assertEqual(
            settings["priorities"],
            {
                "start": "high",
                "success": "low",
                "failure": "max",
            },
        )

    def test_execution_notifier_only_publishes_start_and_finish(self):
        notifier = NtfyExecutionNotifier({}, "主窗口")

        with patch.object(notifier, "_publish", return_value=True) as publish_mock:
            notifier.start_session("测试任务", intro_message="开始")
            notifier.record_detail("步骤一")
            notifier.finish_session(True, "执行完成")

        self.assertEqual(publish_mock.call_count, 2)
        self.assertEqual(publish_mock.call_args_list[0].kwargs["event_key"], "start")
        self.assertEqual(publish_mock.call_args_list[1].kwargs["event_key"], "success")

    def test_execution_notifier_stopped_session_uses_stopped_event(self):
        notifier = NtfyExecutionNotifier({}, "主窗口")

        with patch.object(notifier, "_publish", return_value=True) as publish_mock:
            notifier.start_session("测试任务", intro_message="开始")
            notifier.finish_session(False, "工作流已停止", result_type="stopped")

        self.assertEqual(publish_mock.call_count, 2)
        self.assertEqual(publish_mock.call_args_list[1].kwargs["event_key"], "stopped")
        self.assertIn("已停止", publish_mock.call_args_list[1].args[0])

    def test_publish_ntfy_message_uses_shared_enqueue_helper(self):
        with patch("utils.ntfy_push._enqueue_ntfy_message", return_value=True) as enqueue_mock:
            result = publish_ntfy_message(
                title="标题",
                message="内容",
                priority="max",
                config_ref={
                    "ntfy_settings": {
                        "enabled": True,
                        "topic": "demo",
                    }
                },
                event_key="card",
            )

        self.assertTrue(result)
        enqueue_mock.assert_called_once()
        self.assertEqual("max", enqueue_mock.call_args.kwargs["priority"])
        self.assertEqual("card", enqueue_mock.call_args.kwargs["event_key"])

    def test_execution_notifier_publish_uses_shared_enqueue_helper(self):
        notifier = NtfyExecutionNotifier(
            {
                "ntfy_settings": {
                    "enabled": True,
                    "topic": "demo",
                }
            },
            "主窗口",
        )

        with patch("utils.ntfy_push._enqueue_ntfy_message", return_value=True) as enqueue_mock:
            result = notifier._publish("标题", "内容", event_key="success")

        self.assertTrue(result)
        enqueue_mock.assert_called_once()
        self.assertEqual("success", enqueue_mock.call_args.kwargs["event_key"])
        self.assertIs(notifier._publisher, enqueue_mock.call_args.kwargs["publisher"])
        self.assertIs(notifier._limiter, enqueue_mock.call_args.kwargs["limiter"])


if __name__ == "__main__":
    unittest.main()
