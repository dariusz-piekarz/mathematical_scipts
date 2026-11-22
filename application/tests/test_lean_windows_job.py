"""Windows Job Object launcher and fail-closed regression checks."""
from __future__ import annotations

import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from backend import lean_process, lean_windows_exec, lean_windows_job


class LeanWindowsJobTests(unittest.TestCase):
    def test_windows_job_flags_require_aggregate_memory_and_kill_on_close(self):
        flags = (lean_windows_job.JOB_OBJECT_LIMIT_JOB_MEMORY |
                 lean_windows_job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)
        self.assertEqual(flags, 0x2200)
        self.assertGreater(
            lean_windows_job.ExtendedLimitInformation.JobMemoryLimit.offset,
            lean_windows_job.ExtendedLimitInformation.BasicLimitInformation.offset)

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
