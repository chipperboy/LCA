import tempfile
import unittest
from pathlib import Path
from unittest import mock

from app_core import license_runtime
from app_core import license_store
from ui.dialogs.license_input_dialog import LicenseInputDialog
from utils.app_paths import get_license_cache_path, get_runtime_state_dir


ROOT_DIR = Path(__file__).resolve().parents[1]


def _read_repo_file(relative_path: str) -> str:
    return (ROOT_DIR / relative_path).read_text(encoding="utf-8")


class ArchitectureRuntimeCleanupTests(unittest.TestCase):
    def test_license_cache_path_is_under_runtime_state(self):
        license_path = Path(get_license_cache_path())
        runtime_state_dir = Path(get_runtime_state_dir())

        self.assertEqual(license_path.parent, runtime_state_dir)
        self.assertEqual(license_path.name, "license.dat")

    def test_main_no_longer_contains_removed_legacy_blocks(self):
        main_text = _read_repo_file("main.py")

        for marker in (
            "_legacy_cleanup_log_files_and_temp_unused",
            "_LegacyLogMaintenanceLoopUnused",
            "_legacy_setup_logging_and_cleanup_unused",
            "_legacy_load_config_unused",
            "_legacy_save_config_unused",
        ):
            self.assertNotIn(marker, main_text)

    def test_main_uses_shared_standalone_dispatch_helper(self):
        main_text = _read_repo_file("main.py")

        for removed_marker in (
            "if _IS_OCR_SUBPROCESS:",
            "if _IS_MATCH_SUBPROCESS:",
            "if _IS_WORKFLOW_SUBPROCESS:",
            "if _IS_MCP_SERVER:",
        ):
            self.assertNotIn(removed_marker, main_text)

        for required_marker in (
            "_STANDALONE_SUBPROCESS_SPECS",
            "run_standalone_subprocess(",
            "is_standalone_subprocess_active(",
        ):
            self.assertIn(required_marker, main_text)

    def test_runtime_helpers_no_longer_back_import_main_for_common_utilities(self):
        file_expectations = {
            "tasks/mouse_scroll_runtime.py": (
                "from main import mouse_move_fixer",
                "from app_core.mouse_runtime import mouse_move_fixer",
            ),
            "ui/dialogs/parameter_dialog.py": (
                "from main import find_window_by_title",
                "resolve_unique_window_hwnd",
            ),
            "ui/global_settings_parts/global_settings_dialog_visibility_mixin.py": (
                "from main import",
                "from ..dialogs.license_input_dialog import LicenseInputDialog",
            ),
        }

        for relative_path, (removed_marker, added_marker) in file_expectations.items():
            file_text = _read_repo_file(relative_path)
            self.assertNotIn(removed_marker, file_text, msg=relative_path)
            self.assertIn(added_marker, file_text, msg=relative_path)

        self.assertFalse((ROOT_DIR / "tasks" / "mouse_scroll.py").exists())

    def test_license_store_round_trip_uses_shared_cache_file(self):
        hardware_id = "a" * 64

        with tempfile.TemporaryDirectory() as temp_dir:
            license_path = str(Path(temp_dir) / "license.dat")
            with mock.patch.object(license_store, "LICENSE_FILE", license_path), mock.patch(
                "app_core.license_store.get_hardware_id",
                return_value=hardware_id,
            ):
                license_store.save_local_license("TEST-LICENSE-001")
                restored = license_store.load_local_license()

        self.assertEqual(restored, "TEST-LICENSE-001")

    def test_license_runtime_module_exposes_shared_validation_entrypoints(self):
        self.assertTrue(callable(license_runtime.enforce_online_validation))
        self.assertTrue(callable(license_runtime.validate_license_with_server_v2))
        self.assertTrue(callable(license_runtime.bind_license_to_hwid))

    def test_main_no_longer_registers_runtime_security_hooks(self):
        main_text = _read_repo_file("main.py")

        for marker in (
            "app_license_store.set_runtime_guard(",
            "app_license_runtime.set_runtime_guard(",
            "app_license_runtime.set_runtime_validator(",
            "app_runtime_security.configure_runtime_security(",
            "advanced_anti_decompile",
        ):
            self.assertNotIn(marker, main_text)

    def test_main_no_longer_keeps_anti_debug_startup_checks(self):
        main_text = _read_repo_file("main.py")

        for marker in (
            "IsDebuggerPresent",
            "反逆向检测通过",
            "未检测到调试器",
            "应用程序安全启动",
        ):
            self.assertNotIn(marker, main_text)

    def test_license_input_dialog_class_is_available(self):
        self.assertTrue(issubclass(LicenseInputDialog, object))

    def test_parameter_panel_constructor_no_longer_grabs_window_focus(self):
        panel_text = _read_repo_file("ui/panels/parameter_panel.py")

        self.assertNotIn("self.setFocus()", panel_text)
        self.assertNotIn("self.activateWindow()", panel_text)

    def test_parameter_dialog_no_longer_prints_stack_or_embeds_demo_main(self):
        dialog_text = _read_repo_file("ui/dialogs/parameter_dialog.py")

        self.assertNotIn("traceback.print_exc(", dialog_text)
        self.assertNotIn("if __name__ == '__main__':", dialog_text)

    def test_screenshot_tool_no_longer_keeps_demo_window_entrypoint(self):
        tool_text = _read_repo_file("ui/selectors/screenshot_tool.py")

        self.assertNotIn("window.show()", tool_text)
        self.assertNotIn("if __name__ == \"__main__\":", tool_text)

    def test_runtime_modules_no_longer_print_tracebacks_directly(self):
        for relative_path in (
            "ui/selectors/coordinate_selector.py",
            "ui/panels/selector/parameter_panel_selector_binding_result_mixin.py",
            "ui/workflow_parts/workflow_view_loading_mixin.py",
            "ui/workflow_parts/workflow_view_delete_card_mixin.py",
            "ui/workflow_parts/workflow_view_connection_core_mixin.py",
        ):
            file_text = _read_repo_file(relative_path)
            self.assertNotIn("traceback.print_exc(", file_text, msg=relative_path)

    def test_workflow_modules_reuse_shared_debug_helper(self):
        for relative_path in (
            "ui/workflow_parts/task_card.py",
            "ui/workflow_parts/connection_line.py",
            "ui/workflow_parts/workflow_view_common.py",
        ):
            file_text = _read_repo_file(relative_path)
            self.assertIn("from .workflow_debug_utils import debug_print", file_text, msg=relative_path)
            self.assertNotIn("def debug_print(", file_text, msg=relative_path)
            self.assertNotIn("DEBUG_ENABLED = False", file_text, msg=relative_path)

    def test_task_card_keeps_card_ntfy_push_param_append_chain(self):
        task_card_text = _read_repo_file("ui/workflow_parts/task_card.py")

        self.assertIn("def _append_card_ntfy_push_params(", task_card_text)
        self.assertIn("get_card_ntfy_push_param_definitions()", task_card_text)
        self.assertIn("self._append_card_ntfy_push_params()", task_card_text)

    def test_task_card_default_result_variable_name_is_not_mojibake(self):
        task_card_text = _read_repo_file("ui/workflow_parts/task_card.py")

        self.assertIn('return f"卡片{self.card_id}结果"', task_card_text)
        self.assertIn('re.fullmatch(r"卡片\\d+结果", text)', task_card_text)
        self.assertNotIn("鍗＄墖", task_card_text)

    def test_workflow_task_manager_no_longer_keeps_legacy_finalize_paths(self):
        manager_text = _read_repo_file("ui/workflow_parts/workflow_task_manager.py")

        self.assertNotIn("def _legacy_on_task_status_changed(", manager_text)
        self.assertNotIn("def _legacy_on_task_runtime_cleanup_finished(", manager_text)
        self.assertNotIn("def _legacy_finalize_execution_if_ready(", manager_text)
        self.assertIn("def _finalize_execution_if_ready(", manager_text)

    def test_parameter_dialog_no_longer_keeps_init_level_dead_debug_scaffolding(self):
        dialog_text = _read_repo_file("ui/dialogs/parameter_dialog.py")

        for marker in (
            "!!! ParameterDialog __init__",
            "搜索 设置按钮连接...",
            "!!! _create_widgets 开始执行 !!!",
            "!!! 即将调用 _create_widgets() !!!",
        ):
            self.assertNotIn(marker, dialog_text)

    def test_parameter_dialog_no_longer_keeps_dead_dbg_calls(self):
        dialog_text = _read_repo_file("ui/dialogs/parameter_dialog.py")

        self.assertNotIn("def _dbg(", dialog_text)
        self.assertNotIn("_dbg(", dialog_text)
        self.assertNotIn("logger.info(", dialog_text)
        self.assertNotIn("logger.debug(", dialog_text)


if __name__ == "__main__":
    unittest.main()
