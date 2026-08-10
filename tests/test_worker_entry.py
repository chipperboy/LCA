import logging
import types
import unittest
from unittest import mock

from utils import worker_entry


class WorkerEntryTests(unittest.TestCase):
    def test_cli_argument_helpers_parse_text_and_int(self):
        argv = ["main.py", "--ocr-worker", "--process-id", "worker-1", "--port", "9527"]

        self.assertEqual(
            worker_entry.get_cli_argument_value(argv, "--process-id", "unknown"),
            "worker-1",
        )
        self.assertEqual(
            worker_entry.get_cli_argument_value(argv, "--missing", "fallback"),
            "fallback",
        )
        self.assertEqual(
            worker_entry.get_cli_int_argument_value(argv, "--port", 0),
            9527,
        )
        self.assertEqual(
            worker_entry.get_cli_int_argument_value(["main.py", "--port", "bad"], "--port", 3),
            3,
        )

    def test_run_standalone_subprocess_dispatches_matching_spec(self):
        logger = mock.Mock()
        startup_hook = mock.Mock()
        fake_runner = mock.Mock()
        fake_module = types.SimpleNamespace(run_worker=fake_runner)
        spec = worker_entry.StandaloneSubprocessSpec(
            flag="--ocr-worker",
            module_name="fake.module",
            callable_name="run_worker",
            logger_name="OCR_SUBPROCESS",
            error_label="OCR子进程",
            log_level=logging.DEBUG,
            args_factory=lambda argv: (
                worker_entry.get_cli_argument_value(argv, "--process-id", "unknown"),
                worker_entry.get_cli_int_argument_value(argv, "--port", 0),
            ),
            startup_hook=startup_hook,
        )
        argv = ["main.py", "--ocr-worker", "--process-id", "worker-1", "--port", "9527"]

        with mock.patch("utils.worker_entry.logging.basicConfig") as basic_config_mock, mock.patch(
            "utils.worker_entry.logging.getLogger",
            return_value=logger,
        ), mock.patch(
            "utils.worker_entry.importlib.import_module",
            return_value=fake_module,
        ) as import_module_mock:
            handled = worker_entry.run_standalone_subprocess(argv, (spec,))

        self.assertTrue(handled)
        basic_config_mock.assert_called_once()
        import_module_mock.assert_called_once_with("fake.module")
        startup_hook.assert_called_once_with(logger, tuple(argv), ("worker-1", 9527))
        fake_runner.assert_called_once_with("worker-1", 9527)

    def test_run_standalone_subprocess_can_skip_root_logging_preconfiguration(self):
        logger = mock.Mock()
        fake_runner = mock.Mock()
        fake_module = types.SimpleNamespace(run_worker=fake_runner)
        spec = worker_entry.StandaloneSubprocessSpec(
            flag="--workflow-worker",
            module_name="fake.workflow_module",
            callable_name="run_worker",
            logger_name="WORKFLOW_SUBPROCESS",
            error_label="WORKFLOW子进程",
            configure_root_logging=False,
        )

        with mock.patch("utils.worker_entry.logging.basicConfig") as basic_config_mock, mock.patch(
            "utils.worker_entry.logging.getLogger",
            return_value=logger,
        ), mock.patch(
            "utils.worker_entry.importlib.import_module",
            return_value=fake_module,
        ):
            handled = worker_entry.run_standalone_subprocess(
                ["main.py", "--workflow-worker"],
                (spec,),
            )

        self.assertTrue(handled)
        basic_config_mock.assert_not_called()
        fake_runner.assert_called_once_with()

    def test_run_standalone_subprocess_logs_runner_failure(self):
        logger = mock.Mock()
        fake_module = types.SimpleNamespace(
            run_worker=mock.Mock(side_effect=RuntimeError("boom"))
        )
        spec = worker_entry.StandaloneSubprocessSpec(
            flag="--match-worker",
            module_name="fake.module",
            callable_name="run_worker",
            logger_name="MATCH_SUBPROCESS",
            error_label="MATCH子进程",
        )

        with mock.patch("utils.worker_entry.logging.basicConfig"), mock.patch(
            "utils.worker_entry.logging.getLogger",
            return_value=logger,
        ), mock.patch(
            "utils.worker_entry.importlib.import_module",
            return_value=fake_module,
        ):
            handled = worker_entry.run_standalone_subprocess(
                ["main.py", "--match-worker"],
                (spec,),
            )

        self.assertTrue(handled)
        self.assertGreaterEqual(logger.error.call_count, 2)

    def test_is_standalone_subprocess_active_uses_single_spec_registry(self):
        specs = (
            worker_entry.StandaloneSubprocessSpec(
                flag="--workflow-worker",
                module_name="task_workflow.process_worker",
                callable_name="run_workflow_worker_standalone",
                logger_name="WORKFLOW_SUBPROCESS",
                error_label="WORKFLOW子进程",
            ),
        )

        self.assertTrue(
            worker_entry.is_standalone_subprocess_active(
                ["main.py", "--workflow-worker"],
                specs,
            )
        )
        self.assertFalse(
            worker_entry.is_standalone_subprocess_active(
                ["main.py"],
                specs,
            )
        )


if __name__ == "__main__":
    unittest.main()
