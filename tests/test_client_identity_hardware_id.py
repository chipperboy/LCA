import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from app_core import client_identity


class _UnavailableWmiModule:
    def WMI(self):
        raise AssertionError("hardware sources should not be probed when cache is valid")


class _FakeWmiProduct:
    def __init__(self, uuid: str):
        self.UUID = uuid


class _FakeWmiClient:
    def __init__(self, uuid: str):
        self._uuid = uuid

    def Win32_ComputerSystemProduct(self):
        return [_FakeWmiProduct(self._uuid)]


class _FakeWmiModule:
    def __init__(self, uuid: str):
        self._uuid = uuid

    def WMI(self):
        return _FakeWmiClient(self._uuid)


class ClientIdentityHardwareIdTests(unittest.TestCase):
    def test_get_hardware_id_reuses_valid_saved_id_before_probe(self):
        saved_id = "a" * 64

        with tempfile.TemporaryDirectory() as temp_dir:
            hardware_path = Path(temp_dir) / "hardware_id.txt"
            hardware_path.write_text(saved_id, encoding="utf-8")

            with mock.patch.object(
                client_identity,
                "get_hardware_id_path",
                return_value=str(hardware_path),
            ), mock.patch.object(
                client_identity,
                "_WMI_LIB_AVAILABLE",
                True,
            ), mock.patch.object(
                client_identity,
                "wmi",
                _UnavailableWmiModule(),
            ):
                self.assertEqual(client_identity.get_hardware_id(), saved_id)

            self.assertEqual(hardware_path.read_text(encoding="utf-8"), saved_id)

    def test_get_hardware_id_replaces_invalid_saved_id_with_wmi_id(self):
        wmi_uuid = "123456781234123412341234567890ab"
        expected_id = hashlib.sha256(wmi_uuid.encode("utf-8")).hexdigest()

        with tempfile.TemporaryDirectory() as temp_dir:
            hardware_path = Path(temp_dir) / "hardware_id.txt"
            hardware_path.write_text("not-a-valid-id", encoding="utf-8")

            with mock.patch.object(
                client_identity,
                "get_hardware_id_path",
                return_value=str(hardware_path),
            ), mock.patch.object(
                client_identity.os,
                "name",
                "nt",
            ), mock.patch.object(
                client_identity,
                "_WMI_LIB_AVAILABLE",
                True,
            ), mock.patch.object(
                client_identity,
                "wmi",
                _FakeWmiModule(wmi_uuid),
            ):
                self.assertEqual(client_identity.get_hardware_id(), expected_id)

            self.assertEqual(hardware_path.read_text(encoding="utf-8"), expected_id)


if __name__ == "__main__":
    unittest.main()
