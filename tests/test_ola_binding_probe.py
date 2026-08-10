import unittest
from unittest import mock

from plugins.adapters.ola import multi_instance_manager as multi_instance_module


class _FakeOLA:
    def __init__(self, bind_results, login_response='{"Status": 1, "Message": "OK"}'):
        self._bind_results = list(bind_results)
        self._login_response = login_response
        self.bind_call_count = 0
        self.unbind_call_count = 0
        self.destroy_call_count = 0
        self.call_order = []
        self.login_args = None

    def CreateCOLAPlugInterFace(self):
        self.call_order.append("CreateCOLAPlugInterFace")
        return 1

    def SetPath(self, _path):
        return 1

    def SetConfigByKey(self, _key, _value):
        return 1

    def Login(self, _user_code, _soft_code, _feature_list, _soft_version, _dealer_code):
        self.call_order.append("Login")
        self.login_args = (_user_code, _soft_code, _feature_list, _soft_version, _dealer_code)
        return self._login_response

    def SetOcrConfig(self, _config):
        return 1

    def SetConfig(self, _config):
        return 1

    def SetWindowState(self, _hwnd, _state):
        return 1

    def GetLastError(self):
        return 0

    def GetLastErrorString(self):
        return ""

    def BindWindow(self, _hwnd, _display, _mouse, _keypad, _mode):
        self.bind_call_count += 1
        return self._bind_results.pop(0)

    def BindWindowEx(self, _hwnd, _display, _mouse, _keypad, _pubstr, _mode):
        self.bind_call_count += 1
        return self._bind_results.pop(0)

    def UnBindWindow(self):
        self.unbind_call_count += 1
        return 1

    def DestroyCOLAPlugInterFace(self):
        self.destroy_call_count += 1
        return 1


class OLABindingProbeTests(unittest.TestCase):
    def setUp(self):
        multi_instance_module.OLAMultiInstanceManager._instance = None
        multi_instance_module._manager_instance = None

    def tearDown(self):
        multi_instance_module.OLAMultiInstanceManager._instance = None
        multi_instance_module._manager_instance = None

    def test_probe_window_binding_reuses_formal_retry_strategy(self):
        manager = multi_instance_module.OLAMultiInstanceManager()
        fake_ola = _FakeOLA([0, 0, 1])
        manager._OLAPlugServer = lambda: fake_ola
        manager._OLA_AVAILABLE = True

        with mock.patch.object(manager, "_ensure_ola_imported", return_value=True), \
             mock.patch.object(manager, "_is_window_handle_valid", return_value=True), \
             mock.patch("plugins.adapters.ola.multi_instance_manager.time.sleep", return_value=None):
            ok = manager.probe_window_binding(
                2099184,
                {
                    "display_mode": "dx",
                    "mouse_mode": "windows3",
                    "keypad_mode": "windows",
                    "mode": 0,
                    "pubstr": "ola.bypass.guard",
                },
            )

        self.assertTrue(ok)
        self.assertEqual(fake_ola.bind_call_count, 3)
        self.assertEqual(manager.get_instance_count(), 1)
        self.assertLess(
            fake_ola.call_order.index("Login"),
            fake_ola.call_order.index("CreateCOLAPlugInterFace"),
        )
        manager.release_all()
        self.assertGreaterEqual(fake_ola.unbind_call_count, 1)
        self.assertEqual(fake_ola.destroy_call_count, 1)

    def test_probe_window_binding_uses_latest_runtime_registration_info(self):
        manager = multi_instance_module.OLAMultiInstanceManager()
        fake_ola = _FakeOLA([1])
        manager._OLAPlugServer = lambda: fake_ola
        manager._OLA_AVAILABLE = True

        with mock.patch.object(manager, "_ensure_ola_imported", return_value=True), \
             mock.patch.object(manager, "_is_window_handle_valid", return_value=True), \
             mock.patch("plugins.adapters.ola.auth.get_ola_registration_info", return_value=("user-x", "soft-y", "feature-z")), \
             mock.patch("plugins.adapters.ola.multi_instance_manager.time.sleep", return_value=None):
            ok = manager.probe_window_binding(2099184, {})

        self.assertTrue(ok)
        self.assertEqual(fake_ola.login_args, ("user-x", "soft-y", "feature-z", "", ""))
        self.assertEqual(manager.get_instance_count(), 1)

    def test_probe_window_binding_reuses_warmed_instance_on_next_probe(self):
        manager = multi_instance_module.OLAMultiInstanceManager()
        fake_ola = _FakeOLA([1])
        manager._OLAPlugServer = lambda: fake_ola
        manager._OLA_AVAILABLE = True

        with mock.patch.object(manager, "_ensure_ola_imported", return_value=True), \
             mock.patch.object(manager, "_is_window_handle_valid", return_value=True), \
             mock.patch("plugins.adapters.ola.multi_instance_manager.time.sleep", return_value=None):
            first_ok = manager.probe_window_binding(2099184, {"pubstr": "ola.bypass.guard"})
            second_ok = manager.probe_window_binding(2099184, {"pubstr": "ola.bypass.guard"})

        self.assertTrue(first_ok)
        self.assertTrue(second_ok)
        self.assertEqual(fake_ola.bind_call_count, 1)
        self.assertEqual(manager.get_instance_count(), 1)

    def test_probe_window_binding_stops_before_create_when_login_fails(self):
        manager = multi_instance_module.OLAMultiInstanceManager()
        fake_ola = _FakeOLA(
            [],
            login_response=(
                '{"Status": 0, "Message": "登陆失败: 服务器响应缺少 Time 字段,请检查系统时间"}'
            ),
        )
        manager._OLAPlugServer = lambda: fake_ola
        manager._OLA_AVAILABLE = True

        with mock.patch.object(manager, "_ensure_ola_imported", return_value=True), \
             mock.patch.object(manager, "_is_window_handle_valid", return_value=True):
            ok = manager.probe_window_binding(2099184, {})

        self.assertFalse(ok)
        self.assertEqual(fake_ola.bind_call_count, 0)
        self.assertNotIn("CreateCOLAPlugInterFace", fake_ola.call_order)
        self.assertEqual(
            manager.get_last_failure_detail(),
            "登陆失败: 服务器响应缺少 Time 字段,请检查系统时间",
        )


if __name__ == "__main__":
    unittest.main()
