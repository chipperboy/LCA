import unittest
from unittest import mock
import importlib.util
import sys
from pathlib import Path

from ui.panels.selector.parameter_panel_selector_picker_color_coordinate_dialog_mixin import (
    ParameterPanelSelectorPickerColorCoordinateDialogMixin,
)
from ui.panels.selector.parameter_panel_selector_picker_start_mixin import (
    ParameterPanelSelectorPickerStartMixin,
)


_GLOBAL_SETTINGS_MODULE_NAME = 'tests._global_settings_dialog_window_mixin'
_GLOBAL_SETTINGS_MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / 'ui'
    / 'global_settings_parts'
    / 'global_settings_dialog_window_mixin.py'
)
_global_settings_spec = importlib.util.spec_from_file_location(
    _GLOBAL_SETTINGS_MODULE_NAME,
    _GLOBAL_SETTINGS_MODULE_PATH,
)
_global_settings_module = importlib.util.module_from_spec(_global_settings_spec)
sys.modules[_GLOBAL_SETTINGS_MODULE_NAME] = _global_settings_module
assert _global_settings_spec.loader is not None
_global_settings_spec.loader.exec_module(_global_settings_module)
GlobalSettingsDialogWindowMixin = _global_settings_module.GlobalSettingsDialogWindowMixin


class _DummySignal:
    def __init__(self):
        self.connected = []

    def connect(self, callback):
        self.connected.append(callback)


class _DummyWindowHider:
    def __init__(self):
        self.calls = []

    def add_window(self, window, name, was_visible=False):
        self.calls.append((window, name, was_visible))


class _DummyOverlay:
    def __init__(self):
        self.window_hider = _DummyWindowHider()
        self.window_selected = _DummySignal()


class _DummyPanel(ParameterPanelSelectorPickerStartMixin):
    pass


class _DummyColorDialogHost(ParameterPanelSelectorPickerColorCoordinateDialogMixin):
    pass


class _DummyMainWindow:
    def __init__(self):
        self.parameter_panel = mock.Mock()

    def isVisible(self):
        return True

    def hide(self):
        pass

    def show(self):
        pass


class _DummySettingsDialog(GlobalSettingsDialogWindowMixin):
    def __init__(self):
        self._parent = _DummyMainWindow()
        self.window_picker_overlay = None

    def parent(self):
        return self._parent

    def isVisible(self):
        return True

    def hide(self):
        pass

    def show(self):
        pass

    def _current_window_binding_target(self):
        return 'native'

    def _on_window_picked(self, hwnd, title):
        _ = (hwnd, title)


class ActivationEntrypointsTests(unittest.TestCase):
    def test_picker_start_mixin_reuses_shared_overlay_launcher(self):
        host = _DummyPanel()
        overlay = mock.Mock()
        overlay.geometry.return_value = 'geometry'
        overlay.device_pixel_ratio = 1.0

        with mock.patch(
            'ui.panels.selector.parameter_panel_selector_picker_start_mixin.ParameterPanelPickerOverlay',
            return_value=overlay,
        ):
            with mock.patch(
                'ui.panels.selector.parameter_panel_selector_picker_start_mixin.show_and_activate_overlay',
            ) as show_and_activate_overlay:
                host._show_picker_overlay()

        self.assertIs(host._picker_overlay, overlay)
        show_and_activate_overlay.assert_called_once_with(
            overlay,
            log_prefix='元素拾取覆盖层',
            focus=True,
        )

    def test_color_coordinate_dialog_reuses_shared_overlay_launcher(self):
        host = _DummyColorDialogHost()
        dialog = mock.Mock()

        with mock.patch(
            'ui.panels.selector.parameter_panel_selector_picker_color_coordinate_dialog_mixin.show_and_activate_overlay',
        ) as show_and_activate_overlay:
            host._show_color_coordinate_dialog(dialog)

        show_and_activate_overlay.assert_called_once_with(
            dialog,
            log_prefix='颜色坐标对话框',
            focus=True,
        )

    def test_global_settings_window_picker_reuses_shared_overlay_helpers(self):
        host = _DummySettingsDialog()
        overlay = _DummyOverlay()

        with mock.patch.object(
            _global_settings_module,
            'WIN32_AVAILABLE_FOR_LIST',
            True,
        ):
            with mock.patch(
                'ui.selectors.window_picker.WindowPickerOverlay',
                return_value=overlay,
            ):
                with mock.patch.object(
                    _global_settings_module,
                    'show_and_activate_overlay',
                ) as show_and_activate_overlay:
                    with mock.patch.object(
                        _global_settings_module,
                        'schedule_overlay_activation_boost',
                    ) as schedule_overlay_activation_boost:
                        host._start_window_picker()

        self.assertIs(host.window_picker_overlay, overlay)
        self.assertEqual(len(overlay.window_selected.connected), 1)
        show_and_activate_overlay.assert_called_once_with(
            overlay,
            log_prefix='全局设置窗口选择覆盖层',
            focus=True,
        )
        schedule_overlay_activation_boost.assert_called_once_with(
            overlay,
            log_prefix='全局设置窗口选择覆盖层',
            intervals_ms=(50, 150, 300),
            focus=True,
        )

    def test_global_settings_window_picker_failure_reuses_shared_restore_helpers(self):
        host = _DummySettingsDialog()

        with mock.patch.object(
            _global_settings_module,
            'WIN32_AVAILABLE_FOR_LIST',
            True,
        ):
            with mock.patch(
                'ui.selectors.window_picker.WindowPickerOverlay',
                side_effect=RuntimeError('boom'),
            ):
                with mock.patch.object(
                    _global_settings_module,
                    'show_and_activate_overlay',
                ) as show_and_activate_overlay:
                    with mock.patch.object(
                        _global_settings_module,
                        'show_and_raise_widget',
                    ) as show_and_raise_widget:
                        with mock.patch.object(
                            _global_settings_module.QMessageBox,
                            'critical',
                        ) as critical:
                            host._start_window_picker()

        show_and_activate_overlay.assert_called_once_with(
            host,
            log_prefix='全局设置窗口恢复',
            focus=True,
        )
        show_and_raise_widget.assert_called_once_with(
            host.parent(),
            log_prefix='主窗口恢复',
        )
        critical.assert_called_once()


if __name__ == '__main__':
    unittest.main()
