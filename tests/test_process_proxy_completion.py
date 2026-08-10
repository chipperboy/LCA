import queue
import unittest
from unittest.mock import patch

from PySide6.QtCore import QCoreApplication

from task_workflow.process_proxy import ProcessWorkflowExecutorProxy


class _FakeProcess:
    def __init__(self, poll_values):
        self._poll_values = list(poll_values)

    def poll(self):
        if len(self._poll_values) > 1:
            return self._poll_values.pop(0)
        if self._poll_values:
            return self._poll_values[0]
        return 0

    def wait(self, timeout=None):
        return self.poll()


class ProcessWorkflowExecutorProxyCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = QCoreApplication.instance() or QCoreApplication([])

    def _drain_messages(self, proxy):
        messages = []
        while True:
            try:
                messages.append(proxy._event_queue.get_nowait())
            except queue.Empty:
                break
        return messages

    def test_buffered_execution_finished_wont_be_overwritten_by_fallback(self):
        proxy = ProcessWorkflowExecutorProxy(payload={}, parent=None)
        proxy._process = _FakeProcess([0])
        proxy._running = True

        proxy._enqueue_message(
            {
                "type": "signal",
                "name": "execution_finished",
                "args": [True, "工作流执行完成"],
            }
        )
        proxy._on_process_stopped()

        messages = self._drain_messages(proxy)
        execution_finished_messages = [
            message
            for message in messages
            if message.get("type") == "signal" and message.get("name") == "execution_finished"
        ]

        self.assertEqual(len(execution_finished_messages), 1)
        self.assertEqual(execution_finished_messages[0].get("args"), [True, "工作流执行完成"])

    def test_reader_loop_stops_when_socket_channel_is_closed(self):
        proxy = ProcessWorkflowExecutorProxy(payload={}, parent=None)
        proxy._process = _FakeProcess([None])
        proxy._socket = object()
        proxy._running = True

        with patch("task_workflow.process_proxy.recv_message", return_value=None):
            with patch.object(ProcessWorkflowExecutorProxy, "_is_socket_peer_closed", return_value=True):
                proxy._reader_loop()

        messages = self._drain_messages(proxy)
        execution_finished_messages = [
            message
            for message in messages
            if message.get("type") == "signal" and message.get("name") == "execution_finished"
        ]

        self.assertEqual(len(execution_finished_messages), 1)
        self.assertEqual(execution_finished_messages[0].get("args"), [False, "工作流子进程已退出"])

    def test_reader_loop_keeps_draining_tail_messages_after_process_exit(self):
        proxy = ProcessWorkflowExecutorProxy(payload={}, parent=None)
        proxy._process = _FakeProcess([0, 0, 0])
        proxy._socket = object()
        proxy._running = True

        recv_side_effect = [
            None,
            {
                "type": "signal",
                "name": "execution_finished",
                "args": [True, "工作流执行完成"],
            },
            None,
        ]

        with patch("task_workflow.process_proxy.recv_message", side_effect=recv_side_effect):
            with patch.object(
                ProcessWorkflowExecutorProxy,
                "_is_socket_peer_closed",
                side_effect=[False, True],
            ):
                proxy._reader_loop()

        messages = self._drain_messages(proxy)
        execution_finished_messages = [
            message
            for message in messages
            if message.get("type") == "signal" and message.get("name") == "execution_finished"
        ]

        self.assertEqual(len(execution_finished_messages), 1)
        self.assertEqual(execution_finished_messages[0].get("args"), [True, "工作流执行完成"])

    def test_overlay_update_signal_is_dispatched(self):
        proxy = ProcessWorkflowExecutorProxy(payload={}, parent=None)
        payload = {
            "action": "update",
            "hwnd": 123,
            "detections": [{"x1": 1, "y1": 2, "x2": 3, "y2": 4, "class_name": "test", "confidence": 0.9}],
            "frame_shape": [720, 1280, 3],
        }
        received = []
        proxy.overlay_update_requested.connect(lambda data: received.append(data))

        proxy._dispatch_message(
            {
                "type": "signal",
                "name": "overlay_update_requested",
                "args": [payload],
            }
        )

        self.assertEqual(received, [payload])


if __name__ == "__main__":
    unittest.main()
