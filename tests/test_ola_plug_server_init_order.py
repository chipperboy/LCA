import importlib
import unittest
from unittest import mock

ola_server_module = importlib.import_module("OLA.OLAPlugServer")


class OLAPlugServerInitOrderTests(unittest.TestCase):
    def test_reg_can_run_before_create_and_create_is_idempotent(self):
        call_order = []
        created_pointer = 123456

        with mock.patch.object(
            ola_server_module.OLAPlugDLLHelper,
            "Reg",
            side_effect=lambda *_args: call_order.append("Reg") or 1,
        ), mock.patch.object(
            ola_server_module.OLAPlugDLLHelper,
            "CreateCOLAPlugInterFace",
            side_effect=lambda: call_order.append("CreateCOLAPlugInterFace") or created_pointer,
        ), mock.patch.object(
            ola_server_module.OLAPlugDLLHelper,
            "SetConfigByKey",
            side_effect=lambda instance, key, value: call_order.append(
                f"SetConfigByKey:{instance}:{key}:{value}"
            ) or 1,
        ), mock.patch.object(
            ola_server_module.OLAPlugDLLHelper,
            "DestroyCOLAPlugInterFace",
            return_value=1,
        ) as destroy_mock:
            ola = ola_server_module.OLAPlugServer()

            self.assertIsNone(ola.OLAObject)
            self.assertEqual(ola.Reg("user", "soft", "feature"), 1)

            self.assertEqual(ola.CreateCOLAPlugInterFace(), created_pointer)
            self.assertEqual(ola.OLAObject, created_pointer)
            self.assertEqual(ola.CreateCOLAPlugInterFace(), created_pointer)

            self.assertEqual(ola.DestroyCOLAPlugInterFace(), 1)
            self.assertIsNone(ola.OLAObject)
            destroy_mock.assert_called_once_with(created_pointer)

        self.assertEqual(call_order[0], "Reg")
        self.assertEqual(call_order[1], "CreateCOLAPlugInterFace")
        self.assertEqual(
            call_order[2],
            f"SetConfigByKey:{created_pointer}:DefaultEncoding:1",
        )
        self.assertEqual(call_order.count("CreateCOLAPlugInterFace"), 1)


if __name__ == "__main__":
    unittest.main()
