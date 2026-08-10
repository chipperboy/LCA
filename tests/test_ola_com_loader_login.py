import importlib
import unittest
from unittest import mock

com_loader_module = importlib.import_module("OLA.OLAPlugCOMLoader")


class _FakeCOMObject:
    def __init__(self, result='{"Status": 1, "Message": "OK"}', should_raise=False):
        self._result = result
        self._should_raise = should_raise
        self.login_args = None
        self.machine_code_call_count = 0

    def Login(self, user_code, soft_code, feature_list, soft_version, dealer_code):
        if self._should_raise:
            raise RuntimeError("login boom")
        self.login_args = (user_code, soft_code, feature_list, soft_version, dealer_code)
        return self._result

    def GetMachineCode(self):
        self.machine_code_call_count += 1
        return "94384eba7bc093c376785efa08535b39"


class _FakeLoader:
    def __init__(self, com_object):
        self._com_object = com_object
        self.load_call_count = 0

    def load_com_object(self):
        self.load_call_count += 1
        return self._com_object

    def release(self):
        return None


class OLAPlugServerCOMLoginTests(unittest.TestCase):
    def test_login_loads_com_object_lazily(self):
        fake_com = _FakeCOMObject()
        fake_loader = _FakeLoader(fake_com)

        with mock.patch.object(com_loader_module, "get_ola_com_loader", return_value=fake_loader):
            ola = com_loader_module.OLAPlugServerCOM()
            result = ola.Login("user-a", "soft-b", "feature-c", "", "")

        self.assertEqual(result, '{"Status": 1, "Message": "OK"}')
        self.assertEqual(fake_loader.load_call_count, 1)
        self.assertEqual(fake_com.login_args, ("user-a", "soft-b", "feature-c", "", ""))

    def test_login_returns_empty_string_when_com_call_fails(self):
        fake_loader = _FakeLoader(_FakeCOMObject(should_raise=True))

        with mock.patch.object(com_loader_module, "get_ola_com_loader", return_value=fake_loader):
            ola = com_loader_module.OLAPlugServerCOM()
            result = ola.Login("user-a", "soft-b", "feature-c", "", "")

        self.assertEqual(result, "")
        self.assertEqual(fake_loader.load_call_count, 1)

    def test_get_machine_code_loads_com_object_lazily(self):
        fake_com = _FakeCOMObject()
        fake_loader = _FakeLoader(fake_com)

        with mock.patch.object(com_loader_module, "get_ola_com_loader", return_value=fake_loader):
            ola = com_loader_module.OLAPlugServerCOM()
            result = ola.GetMachineCode()

        self.assertEqual(result, "94384eba7bc093c376785efa08535b39")
        self.assertEqual(fake_loader.load_call_count, 1)
        self.assertEqual(fake_com.machine_code_call_count, 1)


if __name__ == "__main__":
    unittest.main()
