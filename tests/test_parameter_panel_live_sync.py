import unittest

from ui.panels.core.parameter_panel_workflow_selector_thread_refresh_mixin import (
    ParameterPanelWorkflowSelectorThreadRefreshMixin,
)
from ui.panels.parameter_state.parameter_panel_parameter_apply_main_mixin import (
    ParameterPanelParameterApplyMainMixin,
)
from ui.panels.widget.parameter_panel_widget_basic_selector_hint_workflow_selector_mixin import (
    ParameterPanelWidgetBasicSelectorHintWorkflowSelectorMixin,
)
from ui.panels.widget.parameter_panel_widget_numeric_type_checkbox_mixin import (
    ParameterPanelWidgetNumericTypeCheckboxMixin,
)
from ui.panels.widget.parameter_panel_widget_numeric_type_selection_mixin import (
    ParameterPanelWidgetNumericTypeSelectionMixin,
)
from ui.panels.widget.parameter_panel_widget_variable_selector_hint_card_mixin import (
    ParameterPanelWidgetVariableSelectorHintCardMixin,
)


class _FakeSignal:
    def __init__(self):
        self.calls = []

    def emit(self, *args):
        self.calls.append(args)


class _FakeWidget:
    def __init__(self, data=None, text=""):
        self._data = data
        self._text = text

    def itemData(self, index):
        return self._data

    def currentText(self):
        return self._text

    def currentData(self):
        return self._data


class _DummyPanel(
    ParameterPanelWorkflowSelectorThreadRefreshMixin,
    ParameterPanelWidgetVariableSelectorHintCardMixin,
    ParameterPanelWidgetBasicSelectorHintWorkflowSelectorMixin,
    ParameterPanelWidgetNumericTypeCheckboxMixin,
    ParameterPanelWidgetNumericTypeSelectionMixin,
    ParameterPanelParameterApplyMainMixin,
):
    def __init__(self):
        self.current_card_id = 6
        self.current_task_type = "AI工具"
        self.current_parameters = {}
        self.parameters_changed = _FakeSignal()
        self.refresh_conditional_count = 0
        self.refresh_thread_selector_count = 0

    def _refresh_conditional_widgets(self):
        self.refresh_conditional_count += 1

    def _refresh_workflow_card_selector_options(self):
        self.refresh_thread_selector_count += 1

    @staticmethod
    def _normalize_operation_mode_value(value, fallback_task_type=""):
        return value


class ParameterPanelLiveSyncTests(unittest.TestCase):
    def test_numeric_select_change_syncs_card_parameters_immediately(self):
        panel = _DummyPanel()

        panel._handle_numeric_select_changed(
            0,
            _FakeWidget(data="自定义OpenAI兼容"),
            "provider_mode",
        )

        self.assertEqual(panel.current_parameters["provider_mode"], "自定义OpenAI兼容")
        self.assertEqual(panel.refresh_conditional_count, 1)
        self.assertEqual(
            panel.parameters_changed.calls,
            [(6, {"provider_mode": "自定义OpenAI兼容"})],
        )

    def test_workflow_selector_change_syncs_immediately(self):
        panel = _DummyPanel()

        panel._on_workflow_selector_changed(
            0,
            _FakeWidget(data="global"),
            "variable_scope",
        )

        self.assertEqual(panel.current_parameters["variable_scope"], "global")
        self.assertEqual(panel.refresh_conditional_count, 1)
        self.assertEqual(
            panel.parameters_changed.calls,
            [(6, {"variable_scope": "global"})],
        )

    def test_checkbox_change_syncs_related_reset_parameters(self):
        panel = _DummyPanel()

        panel._handle_numeric_checkbox_state_changed("search_region_enabled", 0)

        self.assertFalse(panel.current_parameters["search_region_enabled"])
        self.assertEqual(panel.current_parameters["search_region_x"], 0)
        self.assertEqual(panel.current_parameters["search_region_y"], 0)
        self.assertEqual(panel.current_parameters["search_region_width"], 0)
        self.assertEqual(panel.current_parameters["search_region_height"], 0)
        self.assertEqual(panel.refresh_conditional_count, 1)
        self.assertEqual(
            panel.parameters_changed.calls,
            [
                (
                    6,
                    {
                        "search_region_enabled": False,
                        "search_region_x": 0,
                        "search_region_y": 0,
                        "search_region_width": 0,
                        "search_region_height": 0,
                    },
                )
            ],
        )

    def test_variable_card_selector_change_syncs_immediately(self):
        panel = _DummyPanel()

        panel._on_variable_card_selector_changed(
            0,
            _FakeWidget(data=12),
            "source_card_id",
        )

        self.assertEqual(panel.current_parameters["source_card_id"], 12)
        self.assertEqual(panel.refresh_conditional_count, 1)
        self.assertEqual(
            panel.parameters_changed.calls,
            [(6, {"source_card_id": 12})],
        )

    def test_thread_target_selector_change_syncs_without_conditional_refresh(self):
        panel = _DummyPanel()

        panel._on_thread_target_selection_changed(
            "target_thread",
            _FakeWidget(data=3),
        )

        self.assertEqual(panel.current_parameters["target_thread"], 3)
        self.assertEqual(panel.refresh_conditional_count, 0)
        self.assertEqual(panel.refresh_thread_selector_count, 1)
        self.assertEqual(
            panel.parameters_changed.calls,
            [(6, {"target_thread": 3})],
        )


if __name__ == "__main__":
    unittest.main()
