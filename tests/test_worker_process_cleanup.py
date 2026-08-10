import sys
import types
import unittest
from unittest import mock

from services import worker_process_cleanup


class _FakeProc:
    def __init__(self, pid, cmdline=None, exe="", cwd="", children=None):
        self.pid = pid
        self.info = {
            "pid": pid,
            "cmdline": list(cmdline or []),
            "exe": exe,
            "cwd": cwd,
        }
        self._children = list(children or [])

    def children(self, recursive=True):
        return list(self._children)

    def cmdline(self):
        return list(self.info.get("cmdline") or [])

    def exe(self):
        return self.info.get("exe") or ""

    def cwd(self):
        return self.info.get("cwd") or ""


class _FakePsutilModule:
    def __init__(self, parent_proc, iter_procs):
        self._parent_proc = parent_proc
        self._iter_procs = list(iter_procs)

    def Process(self, pid):
        return self._parent_proc

    def process_iter(self, attrs):
        return list(self._iter_procs)


class WorkerProcessCleanupTests(unittest.TestCase):
    def test_cleanup_matches_direct_child_worker_without_project_path_in_cmdline(self):
        current_pid = 900
        child_proc = _FakeProc(901, cmdline=["main.exe", "--ocr-worker"])
        parent_proc = _FakeProc(current_pid, children=[child_proc])
        fake_psutil = _FakePsutilModule(parent_proc, [])

        with mock.patch.dict(sys.modules, {"psutil": fake_psutil}), mock.patch(
            "services.worker_process_cleanup._kill_pid_tree",
            return_value=True,
        ) as kill_mock:
            cleaned = worker_process_cleanup.cleanup_worker_processes(
                worker_flags=("--ocr-worker",),
                project_root=r"C:\Users\LS\Desktop\LCA",
                main_pid=current_pid,
            )

        self.assertEqual(cleaned, 1)
        kill_mock.assert_called_once_with(901)

    def test_cleanup_matches_orphan_worker_by_executable_path_when_cmdline_lacks_project_root(self):
        current_pid = 900
        parent_proc = _FakeProc(current_pid, children=[])
        orphan_proc = _FakeProc(
            902,
            cmdline=["main.exe", "--ocr-worker"],
            exe=r"C:\Users\LS\Desktop\LCA\dist\main.exe",
        )
        unrelated_proc = _FakeProc(
            903,
            cmdline=["main.exe", "--ocr-worker"],
            exe=r"D:\OtherProject\dist\main.exe",
        )
        fake_psutil = _FakePsutilModule(parent_proc, [orphan_proc, unrelated_proc])

        with mock.patch.dict(sys.modules, {"psutil": fake_psutil}), mock.patch(
            "services.worker_process_cleanup._kill_pid_tree",
            return_value=True,
        ) as kill_mock:
            cleaned = worker_process_cleanup.cleanup_worker_processes(
                worker_flags=("--ocr-worker",),
                project_root=r"C:\Users\LS\Desktop\LCA",
                main_pid=current_pid,
            )

        self.assertEqual(cleaned, 1)
        kill_mock.assert_called_once_with(902)

    def test_cleanup_matches_dedicated_worker_executable_name(self):
        current_pid = 900
        dedicated_proc = _FakeProc(
            904,
            cmdline=[r"C:\Users\LS\Desktop\LCA\dist\workers\custom_worker\custom_worker.exe", "--input", "a"],
            exe=r"C:\Users\LS\Desktop\LCA\dist\workers\custom_worker\custom_worker.exe",
        )
        parent_proc = _FakeProc(current_pid, children=[dedicated_proc])
        fake_psutil = _FakePsutilModule(parent_proc, [])

        with mock.patch.dict(sys.modules, {"psutil": fake_psutil}), mock.patch(
            "services.worker_process_cleanup._kill_pid_tree",
            return_value=True,
        ) as kill_mock:
            cleaned = worker_process_cleanup.cleanup_worker_processes(
                worker_flags=("custom_worker.exe",),
                project_root=r"C:\Users\LS\Desktop\LCA",
                main_pid=current_pid,
            )

        self.assertEqual(cleaned, 1)
        kill_mock.assert_called_once_with(904)


if __name__ == "__main__":
    unittest.main()
