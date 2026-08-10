import io
import json
import unittest

from tasks.ai_tool_task import _PersistentMcpToolClient


class _FakeProc:
    def __init__(self):
        self._buffer = io.BytesIO()
        self.stdin = io.TextIOWrapper(self._buffer, encoding="utf-8", newline="\n")

    def poll(self):
        return None

    def getvalue(self) -> str:
        self.stdin.flush()
        return self._buffer.getvalue().decode("utf-8")


class AiToolMcpTransportTests(unittest.TestCase):
    def test_transport_payload_serialization_escapes_invalid_surrogates(self):
        payload = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "openai_raw",
                "arguments": {
                    "prompt": "bad\udcaa",
                },
            },
        }

        serialized = _PersistentMcpToolClient._serialize_transport_payload(payload)

        self.assertIn("\\udcaa", serialized)
        self.assertEqual(json.loads(serialized)["params"]["arguments"]["prompt"], "bad\udcaa")

    def test_send_json_does_not_fail_on_invalid_surrogates(self):
        client = _PersistentMcpToolClient()
        fake_proc = _FakeProc()
        client._proc = fake_proc

        client._send_json(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"text": "bad\udcaa"},
            }
        )

        self.assertIn("\\udcaa", fake_proc.getvalue())

    def test_call_tool_does_not_retry_on_mcp_timeout(self):
        client = _PersistentMcpToolClient()
        ensure_started_calls = []

        def _fake_ensure_started(timeout):
            ensure_started_calls.append(timeout)
            client._proc = _FakeProc()
            client._response_queue = object()
            client._next_id = 2

        client._ensure_started = _fake_ensure_started
        client._send_json = lambda payload: None
        client._wait_for_response = lambda request_id, timeout: (_ for _ in ()).throw(RuntimeError("mcp call timeout"))
        client.close = lambda: None

        with self.assertRaisesRegex(RuntimeError, "mcp call timeout"):
            client.call_tool("openai_raw", {}, 20.0)

        self.assertEqual(len(ensure_started_calls), 1)

    def test_call_tool_retries_once_when_mcp_server_exits(self):
        client = _PersistentMcpToolClient()
        ensure_started_calls = []
        wait_calls = []

        def _fake_ensure_started(timeout):
            ensure_started_calls.append(timeout)
            client._proc = _FakeProc()
            client._response_queue = object()
            client._next_id = 2

        def _fake_wait_for_response(request_id, timeout):
            wait_calls.append(request_id)
            if len(wait_calls) == 1:
                raise RuntimeError("mcp server exited unexpectedly")
            return {"result": {"content": [{"text": "{\"ok\":true}"}]}}

        client._ensure_started = _fake_ensure_started
        client._send_json = lambda payload: None
        client._wait_for_response = _fake_wait_for_response
        client.close = lambda: None

        result = client.call_tool("openai_raw", {}, 20.0)

        self.assertEqual(result["ok"], True)
        self.assertEqual(len(ensure_started_calls), 2)


if __name__ == "__main__":
    unittest.main()
