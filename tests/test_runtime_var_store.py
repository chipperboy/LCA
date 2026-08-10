import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from task_workflow import runtime_var_store


class RuntimeVarStoreTests(unittest.TestCase):
    def setUp(self):
        self._original_db_path_cache = runtime_var_store._DB_PATH_CACHE
        self._original_db_ready = runtime_var_store._DB_READY
        runtime_var_store._DB_PATH_CACHE = None
        runtime_var_store._DB_READY = False

    def tearDown(self):
        runtime_var_store._DB_PATH_CACHE = self._original_db_path_cache
        runtime_var_store._DB_READY = self._original_db_ready

    def _create_runtime_db(self, db_path: Path) -> None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(db_path))
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS runtime_vars (
                    task_key TEXT NOT NULL,
                    var_key TEXT NOT NULL,
                    var_value TEXT,
                    var_source INTEGER,
                    updated_at REAL NOT NULL,
                    PRIMARY KEY (task_key, var_key)
                )
                """
            )
            conn.execute(
                """
                INSERT OR REPLACE INTO runtime_vars(task_key, var_key, var_value, var_source, updated_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                ("task-1", "answer", "\"ok\"", None, 1.0),
            )
            conn.commit()
        finally:
            conn.close()

    def test_get_db_path_accepts_legacy_user_root_candidate_and_migrates_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            primary_db = temp_root / "runtime_data" / "workflow_runtime_vars.db"
            legacy_user_root_db = temp_root / "workflow_runtime_vars.db"
            temp_db = temp_root / "temp" / "workflow_runtime_vars.db"
            legacy_cwd_db = temp_root / "cwd" / "workflow_runtime_vars.db"

            self._create_runtime_db(legacy_user_root_db)

            with mock.patch.object(
                runtime_var_store,
                "_build_runtime_db_candidates",
                return_value=(
                    str(primary_db),
                    str(legacy_user_root_db),
                    str(temp_db),
                    str(legacy_cwd_db),
                ),
            ):
                resolved_path = runtime_var_store._get_db_path()

            self.assertEqual(Path(resolved_path), primary_db)
            self.assertEqual(runtime_var_store._safe_runtime_row_count(str(primary_db)), 1)


if __name__ == "__main__":
    unittest.main()
