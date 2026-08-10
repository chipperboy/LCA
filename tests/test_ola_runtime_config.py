import importlib
import unittest


runtime_config = importlib.import_module("plugins.adapters.ola.runtime_config")


class OLABuntimeConfigTests(unittest.TestCase):
    def setUp(self):
        self._original_registration = runtime_config.get_ola_registration_info()
        self._original_sdk_dir = runtime_config.get_ola_sdk_dir()

    def tearDown(self):
        user_code, soft_code, feature_list = self._original_registration
        runtime_config.configure_ola_runtime(
            {
                "user_code": user_code,
                "soft_code": soft_code,
                "feature_list": feature_list,
                "sdk_dir": self._original_sdk_dir,
            }
        )

    def test_configure_ola_runtime_applies_registration_and_sdk_dir(self):
        runtime_config.configure_ola_runtime(
            {
                "user_code": "user-a",
                "soft_code": "soft-b",
                "feature_list": "feature-c",
                "dll_path": r"C:\custom\OLA\OLAPlug_x64.dll",
            }
        )

        self.assertEqual(
            runtime_config.get_ola_registration_info(),
            ("user-a", "soft-b", "feature-c"),
        )
        self.assertEqual(runtime_config.get_ola_sdk_dir(), r"C:\custom\OLA")


if __name__ == "__main__":
    unittest.main()
