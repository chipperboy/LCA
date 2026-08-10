import importlib
import unittest


adapter_module = importlib.import_module("plugins.adapters.ola.adapter")


class _FakeOLA:
    def __init__(self):
        self.wheel_up_calls = 0
        self.wheel_down_calls = 0

    def WheelUp(self):
        self.wheel_up_calls += 1
        return 1

    def WheelDown(self):
        self.wheel_down_calls += 1
        return 1


class OLAAdapterMouseScrollTests(unittest.TestCase):
    def test_positive_delta_scrolls_up(self):
        adapter = adapter_module.OLAAdapter(use_multi_instance=True)
        fake_ola = _FakeOLA()
        adapter._bound_hwnd = 123
        adapter._get_ola_for_operation = lambda hwnd: fake_ola
        adapter._move_mouse = lambda x, y, ola, target_hwnd: True

        ok = adapter.mouse_scroll(10, 20, 120, hwnd=123)

        self.assertTrue(ok)
        self.assertEqual(fake_ola.wheel_up_calls, 1)
        self.assertEqual(fake_ola.wheel_down_calls, 0)

    def test_negative_delta_scrolls_down(self):
        adapter = adapter_module.OLAAdapter(use_multi_instance=True)
        fake_ola = _FakeOLA()
        adapter._bound_hwnd = 123
        adapter._get_ola_for_operation = lambda hwnd: fake_ola
        adapter._move_mouse = lambda x, y, ola, target_hwnd: True

        ok = adapter.mouse_scroll(10, 20, -240, hwnd=123)

        self.assertTrue(ok)
        self.assertEqual(fake_ola.wheel_up_calls, 0)
        self.assertEqual(fake_ola.wheel_down_calls, 2)


if __name__ == "__main__":
    unittest.main()
