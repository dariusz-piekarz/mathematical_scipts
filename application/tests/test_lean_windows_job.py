"""Windows Job Object launcher and fail-closed regression checks."""
from __future__ import annotations

import io
import ctypes
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import MagicMock, patch

from backend import lean_process, lean_windows_exec, lean_windows_job


class LeanWindowsJobTests(unittest.TestCase):
    def test_windows_job_flags_require_aggregate_memory_and_kill_on_close(self):
        flags = (lean_windows_job.JOB_OBJECT_LIMIT_JOB_MEMORY |
                 lean_windows_job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)
        self.assertEqual(flags, 0x2200)
        # Win32 class 8 expects a larger BasicAndIoAccounting structure;
        # the BasicAccountingInformation structure requires class 1.
        self.assertEqual(lean_windows_job.JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION, 1)
        self.assertGreater(
            lean_windows_job.ExtendedLimitInformation.JobMemoryLimit.offset,
            lean_windows_job.ExtendedLimitInformation.BasicLimitInformation.offset)

    def test_native_api_contract_limits_before_assignment_and_closes_handle(self):
        kernel = MagicMock()
        kernel.CreateJobObjectW.return_value = 421
        kernel.SetInformationJobObject.return_value = 1
        kernel.OpenProcess.return_value = 422
        kernel.AssignProcessToJobObject.return_value = 1
        kernel.CloseHandle.return_value = 1
        memory_limit = 1024 * 1024 * 1024
        flags = (lean_windows_job.JOB_OBJECT_LIMIT_JOB_MEMORY |
                 lean_windows_job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)

        def set_limit(handle, info_class, pointer, size):
            self.assertEqual(handle, 421)
            self.assertEqual(info_class, 9)
            info = ctypes.cast(pointer, ctypes.POINTER(
                lean_windows_job.ExtendedLimitInformation)).contents
            self.assertEqual(info.JobMemoryLimit, memory_limit)
            self.assertEqual(info.BasicLimitInformation.LimitFlags, flags)
            return 1

        def query(handle, info_class, pointer, size, _):
            if info_class == 9:
                info = ctypes.cast(pointer, ctypes.POINTER(
                    lean_windows_job.ExtendedLimitInformation)).contents
                info.JobMemoryLimit = memory_limit
                info.BasicLimitInformation.LimitFlags = flags
            else:
                self.assertEqual(info_class, lean_windows_job.JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION)
                info = ctypes.cast(pointer, ctypes.POINTER(
                    lean_windows_job.BasicAccountingInformation)).contents
                info.ActiveProcesses = 2
            return 1

        kernel.SetInformationJobObject.side_effect = set_limit
        kernel.QueryInformationJobObject.side_effect = query
        with patch("backend.lean_windows_job._kernel", return_value=kernel):
            job = lean_windows_job.ProcessJob.create(1024)
        stream = MagicMock()
        process = MagicMock(pid=555, stdin=stream)
        job.start(process)
        kernel.AssignProcessToJobObject.assert_called_once_with(421, 422)
        stream.write.assert_called_once_with(b"START\n")
        stream.flush.assert_called_once()
        self.assertTrue(job.kill_and_close())
        self.assertEqual(kernel.CloseHandle.call_args_list[-1].args, (421,))

    def test_failed_assignment_never_sends_start_token_and_closes_process_handle(self):
        kernel = MagicMock()
        kernel.OpenProcess.return_value = 422
        kernel.AssignProcessToJobObject.return_value = 0
        kernel.CloseHandle.return_value = 1
        job = lean_windows_job.ProcessJob(421, kernel)
        stream = MagicMock()
        process = MagicMock(pid=555, stdin=stream)
        with self.assertRaisesRegex(
            lean_windows_job.JobUnavailable, "AssignProcessToJobObject"
        ):
            job.start(process)
        stream.write.assert_not_called()
        stream.flush.assert_not_called()
        kernel.CloseHandle.assert_called_once_with(422)

    def test_invalid_limit_rejected_before_any_windows_api_call(self):
        with patch("backend.lean_windows_job._kernel") as kernel:
            for value in (0, 511, 65537, True, "1024", None):
                with self.subTest(value=value), self.assertRaises(ValueError):
                    lean_windows_job.ProcessJob.create(value)
            kernel.assert_not_called()

    def test_job_setup_failure_closes_handle_without_starting_lake(self):
        kernel = MagicMock()
        kernel.CreateJobObjectW.return_value = 421
        kernel.SetInformationJobObject.return_value = 0
        with patch("backend.lean_windows_job._kernel", return_value=kernel):
            with self.assertRaises(lean_windows_job.JobUnavailable):
                lean_windows_job.ProcessJob.create(1024)
        kernel.CloseHandle.assert_called_once_with(421)
        kernel.QueryInformationJobObject.assert_not_called()

    def test_launcher_requires_explicit_start_token(self):
        argv = ["lean_windows_exec.py", "--", "lake", "env", "lean", "test.lean"]
        for token in (b"", b"BAD\n", b"START anything\n"):
            with self.subTest(token=token), \
                 patch.object(sys, "argv", argv), \
                 patch.object(sys, "stdin", io.TextIOWrapper(io.BytesIO(token))), \
                 patch("backend.lean_windows_exec.subprocess.run") as spawn:
                self.assertEqual(lean_windows_exec.main(), 125)
                spawn.assert_not_called()

        done = subprocess.CompletedProcess(args=["lake"], returncode=0)
        with patch.object(sys, "argv", argv), \
             patch.object(sys, "stdin", io.TextIOWrapper(io.BytesIO(b"START\n"))), \
             patch("backend.lean_windows_exec.subprocess.run",
                   return_value=done) as spawn:
            self.assertEqual(lean_windows_exec.main(), 0)
        spawn.assert_called_once_with(
            ["lake", "env", "lean", "test.lean"],
            stdin=subprocess.DEVNULL, check=False)

    def test_real_launch_will_not_start_before_gate_is_opened(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "launched.txt"
            helper = Path(lean_process.__file__).with_name("lean_windows_exec.py")
            source = (
                "from pathlib import Path;"
                f"Path({str(destination)!r}).write_text('ran')"
            )
            argv = [sys.executable, str(helper), "--",
                    sys.executable, "-c", source]

            def allow(process):
                self.assertFalse(destination.exists())
                process.stdin.write(b"START\n")
                process.stdin.flush()
                process.stdin.close()

            status, log, timed_out = lean_process._execute_process(
                argv, Path(tmp), timeout=10, log_limit=16000, startup=allow)
            self.assertEqual(status, 0, log)
            self.assertFalse(timed_out)
            self.assertEqual(destination.read_text(), "ran")
            destination.unlink()

            def deny(process):
                self.assertFalse(destination.exists())
                raise lean_windows_job.JobUnavailable("assignment rejected")

            with self.assertRaisesRegex(
                lean_windows_job.JobUnavailable, "assignment rejected"
            ):
                lean_process._execute_process(
                    argv, Path(tmp), timeout=10, log_limit=16000, startup=deny)
            self.assertFalse(destination.exists())

    def test_missing_job_permission_refuses_before_launch(self):
        with patch("backend.lean_process.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_process.lean_windows_job.ProcessJob.create",
                   side_effect=lean_windows_job.JobUnavailable("access denied")), \
             patch("backend.lean_process._execute_process") as spawn:
            with self.assertRaisesRegex(
                lean_windows_job.JobUnavailable, "access denied"
            ):
                lean_process.execute_registered(
                    ["lake", "env", "lean", "src/Test.lean"],
                    Path.cwd(), timeout=10, total_memory_mb=1024)
            spawn.assert_not_called()

    def test_windows_job_wiring_and_cleanup_including_failures(self):
        job = MagicMock()
        job.kill_and_close.return_value = False
        with patch("backend.lean_process.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_process.lean_windows_job.ProcessJob.create",
                   return_value=job), \
             patch("backend.lean_process._execute_process",
                   return_value=(0, "ok", False)) as execute:
            self.assertEqual(lean_process.execute_registered(
                ["lake", "env", "lean", "src/Test.lean"],
                Path.cwd(), timeout=10, total_memory_mb=1024), (0, "ok", False))
            self.assertTrue(
                execute.call_args.args[0][1].endswith("lean_windows_exec.py"))
            self.assertIs(execute.call_args.kwargs["startup"], job.start)
        job.kill_and_close.assert_called_once()

        job.kill_and_close.reset_mock()
        job.kill_and_close.return_value = True
        with patch("backend.lean_process.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_process.lean_windows_job.ProcessJob.create",
                   return_value=job), \
             patch("backend.lean_process._execute_process",
                   return_value=(0, "", False)):
            with self.assertRaises(lean_windows_job.JobUnavailable):
                lean_process.execute_registered(
                    ["lake"], Path.cwd(), timeout=10, total_memory_mb=1024)
        job.kill_and_close.assert_called_once()

        job.kill_and_close.reset_mock()
        job.kill_and_close.return_value = False
        with patch("backend.lean_process.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_process.lean_windows_job.ProcessJob.create",
                   return_value=job), \
             patch("backend.lean_process._execute_process",
                   side_effect=OSError("subprocess failed")):
            with self.assertRaises(OSError):
                lean_process.execute_registered(
                    ["lake"], Path.cwd(), timeout=10, total_memory_mb=1024)
        job.kill_and_close.assert_called_once()

    @unittest.skipUnless(sys.platform == "win32", "Native Windows Job Objects test")
    def test_native_nested_windows_jobs_preserve_inner_limit(self):
        # The outer, already limited interpreter creates a second Job Object.
        # This covers the common case of a launcher already running in a job.
        app_dir = Path(__file__).resolve().parents[1]
        code = (
            "from pathlib import Path;"
            "import sys;"
            "from backend import lean_process;"
            "rc,log,to=lean_process.execute_registered("
            "[sys.executable,'-c',\"print('nested-job-ok')\"],"
            "Path.cwd(),timeout=8,total_memory_mb=512);"
            "assert rc==0 and not to and 'nested-job-ok' in log,(rc,log,to);"
            "print('outer-job-ok')"
        )
        status, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], app_dir,
            timeout=15, total_memory_mb=2048)
        self.assertFalse(timed_out)
        self.assertEqual(status, 0, log)
        self.assertIn("outer-job-ok", log)

    @unittest.skipUnless(sys.platform == "win32", "Native Windows Job Objects test")
    def test_native_windows_timeout_terminates_descendants(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "survived"
            started = Path(tmp) / "started"
            child = (
                "import time,pathlib;time.sleep(2);"
                f"pathlib.Path({str(destination)!r}).write_text('survived')"
            )
            parent = (
                "import subprocess,sys,pathlib,time;"
                f"subprocess.Popen([sys.executable,'-c',{child!r}]);"
                f"pathlib.Path({str(started)!r}).write_text('spawned');"
                "time.sleep(60)"
            )
            code, log, timed_out = lean_process.execute_registered(
                [sys.executable, "-c", parent], Path(tmp),
                timeout=0.9, total_memory_mb=512)
            self.assertTrue(started.exists(), log)
            self.assertTrue(timed_out)
            self.assertIsNone(code)
            time.sleep(2.4)
            self.assertFalse(destination.exists())

    @unittest.skipUnless(sys.platform == "win32", "Native Windows Job Objects test")
    def test_native_windows_job_memory_restriction(self):
        code = "x=bytearray(1200*1024*1024);print('unexpected allocation success')"
        status, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], Path.cwd(),
            timeout=15, total_memory_mb=512)
        self.assertFalse(timed_out)
        self.assertNotEqual(status, 0)
        self.assertNotIn("unexpected allocation success\n", log)


if __name__ == "__main__":
    unittest.main()
