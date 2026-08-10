import unittest

from PySide6.QtWidgets import QApplication

from tasks import get_task_modules
from ui.workflow_parts.connection_line import ConnectionLine
from ui.workflow_parts.workflow_view import WorkflowView


class WorkflowConnectionLinePathsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = QApplication.instance() or QApplication([])

    def test_load_workflow_restores_non_empty_connection_paths(self):
        view = WorkflowView(task_modules=get_task_modules(), images_dir="images")
        workflow_data = {
            "cards": [
                {
                    "id": 1,
                    "task_type": "线程起点",
                    "pos_x": -300,
                    "pos_y": -120,
                    "parameters": {"next_step_card_id": 2},
                },
                {
                    "id": 2,
                    "task_type": "模拟鼠标操作",
                    "pos_x": 0,
                    "pos_y": -120,
                    "parameters": {},
                },
            ],
            "connections": [
                {"start_card_id": 1, "end_card_id": 2, "type": "sequential"},
            ],
        }

        view.load_workflow(workflow_data)

        self.assertEqual(len(view.connections), 1)
        connection = view.connections[0]
        self.assertIsInstance(connection, ConnectionLine)
        self.assertFalse(connection.path().isEmpty())


if __name__ == "__main__":
    unittest.main()
