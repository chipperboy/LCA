import importlib
import unittest


adapter_module = importlib.import_module("plugins.adapters.ola.adapter")


class _FakeMultiInstanceManager:
    def __init__(self, valid_hwnds=None):
        self.valid_hwnds = set(valid_hwnds or set())
        self.release_calls = []

    def _is_window_handle_valid(self, hwnd):
        return hwnd in self.valid_hwnds

    def release_instance(self, hwnd):
        self.release_calls.append(hwnd)


class OLAAdapterUnbindTests(unittest.TestCase):
    def test_multi_instance_unbind_keeps_cached_instance_for_valid_window(self):
        adapter = adapter_module.OLAAdapter(use_multi_instance=True)
        adapter._multi_instance_manager = _FakeMultiInstanceManager(valid_hwnds={67120})
        adapter._bound_hwnd = 67120
        adapter._bound_display_mode = "gdi"
        adapter._bound_mouse_mode = "windows3"
        adapter._bound_keypad_mode = "windows"
        adapter._bound_mode = 1
        adapter._bound_pubstr = "ola.bypass.guard"
        adapter._mouse_move_with_trajectory = True
        adapter.ola = object()

        ok = adapter.unbind_window(67120)

        self.assertTrue(ok)
        self.assertEqual(adapter._multi_instance_manager.release_calls, [])
        self.assertIsNone(adapter._bound_hwnd)
        self.assertEqual(adapter._bound_display_mode, "normal")
        self.assertEqual(adapter._bound_mouse_mode, "normal")
        self.assertEqual(adapter._bound_keypad_mode, "normal")
        self.assertEqual(adapter._bound_mode, 0)
        self.assertEqual(adapter._bound_pubstr, "")
        self.assertFalse(adapter._mouse_move_with_trajectory)
        self.assertIsNone(adapter.ola)

    def test_multi_instance_unbind_releases_cached_instance_for_invalid_window(self):
        adapter = adapter_module.OLAAdapter(use_multi_instance=True)
        adapter._multi_instance_manager = _FakeMultiInstanceManager(valid_hwnds=set())
        adapter._bound_hwnd = 67120
        adapter.ola = object()

        ok = adapter.unbind_window(67120)

        self.assertTrue(ok)
        self.assertEqual(adapter._multi_instance_manager.release_calls, [67120])
        self.assertIsNone(adapter._bound_hwnd)
        self.assertIsNone(adapter.ola)


if __name__ == "__main__":
    unittest.main()
