import unittest
from unittest import mock

from plugins.adapters.ola.auth import authorize_ola_instance, probe_ola_authorization


class _FakeOLA:
    def __init__(self, login_response, machine_code=""):
        self._login_response = login_response
        self._machine_code = machine_code
        self.login_args = None
        self.destroy_call_count = 0

    def Login(self, user_code, soft_code, feature_list, soft_version, dealer_code):
        self.login_args = (user_code, soft_code, feature_list, soft_version, dealer_code)
        return self._login_response

    def GetMachineCode(self):
        return self._machine_code

    def DestroyCOLAPlugInterFace(self):
        self.destroy_call_count += 1
        return 1


class OLAAuthorizationTests(unittest.TestCase):
    def test_authorize_ola_instance_accepts_successful_login(self):
        fake_ola = _FakeOLA('{"Status": 1, "Message": "OK"}')

        with mock.patch(
            "plugins.adapters.ola.auth.get_ola_registration_info",
            return_value=("user-a", "soft-b", "feature-c"),
        ):
            result = authorize_ola_instance(fake_ola)

        self.assertTrue(result.success)
        self.assertEqual(fake_ola.login_args, ("user-a", "soft-b", "feature-c", "", ""))

    def test_authorize_ola_instance_returns_login_message_on_failure(self):
        fake_ola = _FakeOLA(
            '{"Status": 0, "Message": "登陆失败: 服务器响应缺少 Time 字段,请检查系统时间"}'
        )

        with mock.patch(
            "plugins.adapters.ola.auth.get_ola_registration_info",
            return_value=("user-a", "soft-b", "feature-c"),
        ):
            result = authorize_ola_instance(fake_ola)

        self.assertFalse(result.success)
        self.assertEqual(result.message, "登陆失败: 服务器响应缺少 Time 字段,请检查系统时间")

    def test_authorize_ola_instance_extracts_machine_code_on_activation_failure(self):
        fake_ola = _FakeOLA(
            '{"Status": 0, "Message": "登陆失败:未激活：未找到授权信息，请先激活授权，当前机器码：94384eba7bc093c376785efa08535b39"}'
        )

        with mock.patch(
            "plugins.adapters.ola.auth.get_ola_registration_info",
            return_value=("user-a", "soft-b", "feature-c"),
        ):
            result = authorize_ola_instance(fake_ola)

        self.assertFalse(result.success)
        self.assertTrue(result.requires_activation)
        self.assertEqual(result.machine_code, "94384eba7bc093c376785efa08535b39")

    def test_probe_ola_authorization_returns_machine_code_and_closes_probe_instance(self):
        fake_ola = _FakeOLA(
            '{"Status": 0, "Message": "登陆失败:未激活：未找到授权信息，请先激活授权"}',
            machine_code="94384eba7bc093c376785efa08535b39",
        )

        with mock.patch(
            "plugins.adapters.ola.auth._create_ola_server_for_probe",
            return_value=fake_ola,
        ), mock.patch(
            "plugins.adapters.ola.auth.get_ola_registration_info",
            return_value=("user-a", "soft-b", "feature-c"),
        ):
            result = probe_ola_authorization({"dll_path": "OLA/OLAPlug_x64.dll"})

        self.assertFalse(result.success)
        self.assertTrue(result.requires_activation)
        self.assertEqual(result.machine_code, "94384eba7bc093c376785efa08535b39")
        self.assertEqual(fake_ola.destroy_call_count, 1)


if __name__ == "__main__":
    unittest.main()
