import unittest
from unittest import mock

import requests

from app_core import client_identity


class ClientIdentityRetryTests(unittest.TestCase):
    def test_default_server_candidates_only_include_api_ports(self):
        candidates = client_identity._build_server_url_candidates("https://api.lcaa.top:8000")

        self.assertEqual(
            candidates,
            [
                "https://api.lcaa.top:8000",
                "https://www.lcaa.top:8000",
                "https://lcaa.top:8000",
            ],
        )
        self.assertNotIn("https://www.lcaa.top", candidates)
        self.assertNotIn("https://lcaa.top", candidates)

    def test_csrf_html_response_is_reported_as_invalid_response(self):
        response = mock.Mock()
        response.status_code = 200
        response.headers = {"content-type": "text/html; charset=utf-8"}
        response.text = '<script src="/_guard/auto.js"></script>'
        response.json.side_effect = ValueError("Expecting value")
        response.raise_for_status.return_value = None

        session = mock.Mock()
        session.get.return_value = response
        session.cookies = {}

        result = client_identity._attempt_client_registration_with_server(
            "a" * 64,
            session,
            "https://www.lcaa.top",
            True,
        )

        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "csrf_invalid_response")
        session.post.assert_not_called()

    def test_request_with_retry_retries_timeout_once_then_returns_response(self):
        response = mock.Mock()
        request_callable = mock.Mock(
            side_effect=[
                requests.exceptions.Timeout("slow"),
                response,
            ]
        )

        with mock.patch.object(client_identity.time, "sleep") as sleep_mock:
            result = client_identity._request_with_retry(
                request_callable,
                "CSRF 请求",
                attempts=2,
            )

        self.assertIs(result, response)
        self.assertEqual(request_callable.call_count, 2)
        sleep_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
