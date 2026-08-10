import unittest
from types import SimpleNamespace
from unittest import mock

from ui.workflow_parts.workflow_view_loading_mixin import WorkflowViewLoadingMixin
from ui.workflow_parts.workflow_view_connection_sequence_mixin import WorkflowViewConnectionSequenceMixin


class _FakeCard:
    def __init__(self, card_id: int, task_type: str):
        self.card_id = card_id
        self.task_type = task_type
        self.parameters = {}
        self.param_definitions = {}
        self.custom_name = None

    def set_custom_name(self, custom_name):
        self.custom_name = custom_name


class _FakeScene:
    def items(self):
        return []

    def setSceneRect(self, *_args, **_kwargs):
        return None


class _FakeWorkflowView(WorkflowViewLoadingMixin):
    def __init__(self):
        self.cards = {}
        self.connections = []
        self.scene = _FakeScene()
        self._loading_workflow = False
        self._sync_called = False
        self._cleanup_called = False
        self._sequence_update_args = []
        self._added_connections = []

    def clear_workflow(self):
        self.cards = {}
        self.connections = []

    def add_task_card(self, x, y, task_type="未知", card_id=None):
        card = _FakeCard(card_id, task_type)
        self.cards[card_id] = card
        return card

    def add_connection(self, start_card, end_card, line_type, skip_duplicate_check=False):
        connection = {
            "start": start_card.card_id,
            "end": end_card.card_id,
            "type": line_type,
            "skip_duplicate_check": bool(skip_duplicate_check),
        }
        self.connections.append(connection)
        self._added_connections.append(connection)
        return connection

    def update_card_sequence_display(self, skip_jump_rebuild=False):
        self._sequence_update_args.append(bool(skip_jump_rebuild))

    def _update_card_render_cache_policy(self):
        return None

    def _register_result_placeholders_after_load(self):
        return None

    def _refresh_container_layouts(self):
        return None

    def _validate_and_cleanup_jump_targets(self):
        return None

    def _refresh_thread_start_custom_names(self):
        return None

    def _sync_connections_with_scene(self):
        self._sync_called = True

    def cleanup_all_duplicate_connections(self):
        self._cleanup_called = True

    def setTransform(self, *_args, **_kwargs):
        return None

    def _notify_zoom_level_changed(self):
        return None


class _FakeSequenceWorkflowView(WorkflowViewConnectionSequenceMixin):
    def __init__(self):
        self.cards = {}
        self.connections = []
        self.scene = _FakeScene()
        self._added_connections = []

    def add_connection(self, start_card, end_card, line_type, skip_duplicate_check=False):
        connection = {
            "start": start_card.card_id,
            "end": end_card.card_id,
            "type": line_type,
            "skip_duplicate_check": bool(skip_duplicate_check),
        }
        self.connections.append(connection)
        self._added_connections.append(connection)
        return connection


class WorkflowViewLoadingConnectionsTests(unittest.TestCase):
    def _load(self, workflow_data):
        view = _FakeWorkflowView()
        with mock.patch(
            "task_workflow.workflow_context.import_global_vars",
            return_value=None,
        ), mock.patch(
            "task_workflow.workflow_context.prune_orphan_vars",
            return_value=None,
        ), mock.patch(
            "ui.workflow_parts.workflow_view_loading_mixin.QMessageBox.warning",
            return_value=None,
        ):
            view.load_workflow(workflow_data)
        return view

    def test_load_workflow_restores_serialized_jump_connections_without_rebuild(self):
        workflow_data = {
            "cards": [
                {"id": 1, "task_type": "线程起点", "pos_x": 0, "pos_y": 0, "parameters": {"next_step_card_id": 2}},
                {"id": 2, "task_type": "模拟鼠标操作", "pos_x": 100, "pos_y": 0, "parameters": {"成功时": "跳转到步骤", "success_jump_target_id": 3}},
                {"id": 3, "task_type": "OCR文字识别", "pos_x": 200, "pos_y": 0, "parameters": {}},
            ],
            "connections": [
                {"start_card_id": 1, "end_card_id": 2, "type": "sequential"},
                {"start_card_id": 2, "end_card_id": 3, "type": "success"},
            ],
        }

        view = self._load(workflow_data)

        self.assertIn(
            {"start": 2, "end": 3, "type": "success", "skip_duplicate_check": True},
            view._added_connections,
        )
        self.assertEqual(view._sequence_update_args, [True])

    def test_load_workflow_falls_back_to_jump_rebuild_when_file_has_no_jump_lines(self):
        workflow_data = {
            "cards": [
                {"id": 1, "task_type": "线程起点", "pos_x": 0, "pos_y": 0, "parameters": {"next_step_card_id": 2}},
                {"id": 2, "task_type": "模拟鼠标操作", "pos_x": 100, "pos_y": 0, "parameters": {"on_success": "跳转到步骤", "success_jump_target_id": 3}},
                {"id": 3, "task_type": "OCR文字识别", "pos_x": 200, "pos_y": 0, "parameters": {}},
            ],
            "connections": [
                {"start_card_id": 1, "end_card_id": 2, "type": "sequential"},
            ],
        }

        view = self._load(workflow_data)

        self.assertEqual(view._sequence_update_args, [False])

    def test_single_card_jump_refresh_allows_self_loop_connections(self):
        view = _FakeSequenceWorkflowView()
        card = _FakeCard(2, "模拟鼠标操作")
        card.parameters = {
            "on_success": "跳转到步骤",
            "success_jump_target_id": 2,
            "on_failure": "跳转到步骤",
            "failure_jump_target_id": 2,
        }
        view.cards = {2: card}

        view.update_single_card_jump_connections(2)

        self.assertIn(
            {"start": 2, "end": 2, "type": "success", "skip_duplicate_check": False},
            view._added_connections,
        )
        self.assertIn(
            {"start": 2, "end": 2, "type": "failure", "skip_duplicate_check": False},
            view._added_connections,
        )


if __name__ == "__main__":
    unittest.main()
