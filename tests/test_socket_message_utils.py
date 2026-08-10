import os
import pickle
import socket
import unittest
from unittest import mock

from services import ocr_socket_message_utils
from services import socket_message_utils


class SocketMessageUtilsTests(unittest.TestCase):
    def _socketpair(self):
        if not hasattr(socket, "socketpair"):
            self.skipTest("socketpair unavailable")
        return socket.socketpair()

    def test_recv_message_bytes_with_status_round_trip(self):
        sender, receiver = self._socketpair()
        try:
            payload = {"type": "signal", "name": "ping", "args": [1, 2, 3]}

            self.assertTrue(
                socket_message_utils.send_message(
                    sender,
                    payload,
                    max_message_bytes=1024 * 1024,
                )
            )

            raw_payload, status = socket_message_utils.recv_message_bytes_with_status(
                receiver,
                timeout=1.0,
                max_message_bytes=1024 * 1024,
            )

            self.assertEqual(status, "ok")
            self.assertEqual(pickle.loads(raw_payload), payload)
        finally:
            sender.close()
            receiver.close()

    def test_ocr_send_message_rejects_oversized_payload(self):
        sender, receiver = self._socketpair()
        try:
            payload = {"data": "x" * (5 * 1024 * 1024)}
            logger = mock.Mock()

            with mock.patch.dict(os.environ, {"OCR_SOCKET_MAX_MESSAGE_MB": "4"}):
                result = ocr_socket_message_utils.send_message(
                    sender,
                    payload,
                    logger=logger,
                )

            self.assertFalse(result)
            logger.error.assert_called_once()
        finally:
            sender.close()
            receiver.close()

    def test_ocr_recv_message_uses_shared_message_reader(self):
        sender, receiver = self._socketpair()
        try:
            payload = {"type": "ocr", "text": "ok"}
            self.assertTrue(
                socket_message_utils.send_message(
                    sender,
                    payload,
                    max_message_bytes=1024 * 1024,
                )
            )

            with mock.patch.dict(os.environ, {"OCR_SOCKET_MAX_MESSAGE_MB": "4"}):
                result = ocr_socket_message_utils.recv_message(receiver, timeout=1.0)

            self.assertEqual(result, payload)
        finally:
            sender.close()
            receiver.close()


if __name__ == "__main__":
    unittest.main()
