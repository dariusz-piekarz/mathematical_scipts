"""Fail-closed and lifecycle checks for optional Linux cgroup v2 Lean runs."""
from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from backend import lean_cgroup, lean_cgroup_exec, lean_process


class LeanCgroupTests(unittest.TestCase):
    def test_total_limit_configuration_rejects_invalid_values(self):
        for raw in ("0", "256", "65537", "-1", "invalid", " 8192", "1024MB"):
            with self.subTest(value=raw), patch.dict(
                os.environ, {"MATLIB_LEAN_TOTAL_MEMORY_MB": raw}
            ):
                with self.assertRaises(ValueError):
                    lean_cgroup.configured_total_memory_mb()
        with patch.dict(os.environ, {"MATLIB_LEAN_TOTAL_MEMORY_MB": "8192"}):
            self.assertEqual(lean_cgroup.configured_total_memory_mb(), 8192)

    def test_missing_delegation_refuses_request(self):
        with patch("backend.lean_cgroup._delegated_parent",
                   side_effect=lean_cgroup.CgroupUnavailable("not delegated")):
            self.assertFalse(lean_cgroup.available())
            with self.assertRaises(lean_cgroup.CgroupUnavailable):
                lean_cgroup.ProcessGroup.create(1024)

    def test_missing_kernel_cgroup_kill_is_rejected_and_directory_cleaned(self):
        with tempfile.TemporaryDirectory() as tmp, \
             patch("backend.lean_cgroup._delegated_parent", return_value=Path(tmp)):
            with self.assertRaises(lean_cgroup.CgroupUnavailable):
                lean_cgroup.ProcessGroup.create(512)
            self.assertFalse(list(Path(tmp).iterdir()))

    def test_runner_does_not_spawn_without_delegated_group(self):
        with patch("backend.lean_cgroup.ProcessGroup.create",
                   side_effect=lean_cgroup.CgroupUnavailable("not writable")), \
             patch("backend.lean_process._execute_process") as spawn:
            with self.assertRaises(lean_cgroup.CgroupUnavailable):
                lean_process.execute_registered(
                    [sys.executable, "-c", "print('not run')"], Path.cwd(),
                    timeout=3, total_memory_mb=512)
            spawn.assert_not_called()

    def test_child_is_attached_before_exec(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = ["lean_cgroup_exec.py", tmp, "--", "tool", "--version"]
            with patch.object(sys, "argv", args), \
                 patch("backend.lean_cgroup_exec.os.execvp",
                       side_effect=RuntimeError("exec reached")) as execute:
                with self.assertRaisesRegex(RuntimeError, "exec reached"):
                    lean_cgroup_exec.main()
            self.assertEqual((Path(tmp) / "cgroup.procs").read_text(), str(os.getpid()))
            execute.assert_called_once_with("tool", ["tool", "--version"])

    def test_failed_attach_never_executes_toolchain(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = ["lean_cgroup_exec.py", str(Path(tmp) / "missing"), "--", "tool"]
            with patch.object(sys, "argv", args), \
                 patch("backend.lean_cgroup_exec.os.execvp") as execute:
                self.assertEqual(lean_cgroup_exec.main(), 125)
                execute.assert_not_called()

    def test_successful_group_cleanup_and_surviving_process_refusal(self):
        group = MagicMock()
        group.path = Path("/synthetic/test-group")
        group.kill_and_remove.return_value = False
        with patch("backend.lean_cgroup.ProcessGroup.create", return_value=group), \
             patch("backend.lean_process._execute_process",
                   return_value=(0, "ok", False)) as execute:
            result = lean_process.execute_registered(
                ["lake", "env", "lean", "src/Test.lean"], Path.cwd(),
                timeout=10, total_memory_mb=1024)
        self.assertEqual(result, (0, "ok", False))
        self.assertTrue(execute.call_args.args[0][1].endswith("lean_cgroup_exec.py"))
        self.assertEqual(execute.call_args.args[0][-4:],
                         ["lake", "env", "lean", "src/Test.lean"])
        group.kill_and_remove.assert_called_once()

        group.kill_and_remove.reset_mock()
        group.kill_and_remove.return_value = True
        with patch("backend.lean_cgroup.ProcessGroup.create", return_value=group), \
             patch("backend.lean_process._execute_process",
                   return_value=(0, "ok", False)):
            with self.assertRaises(lean_cgroup.CgroupUnavailable):
                lean_process.execute_registered(
                    ["lake"], Path.cwd(), timeout=10, total_memory_mb=1024)
        group.kill_and_remove.assert_called_once()

    def test_group_cleaned_even_when_spawn_fails(self):
        group = MagicMock()
        group.path = Path("/synthetic/test-group")
        group.kill_and_remove.return_value = False
        with patch("backend.lean_cgroup.ProcessGroup.create", return_value=group), \
             patch("backend.lean_process._execute_process",
                   side_effect=OSError("missing executable")):
            with self.assertRaises(OSError):
                lean_process.execute_registered(
                    ["lake"], Path.cwd(), timeout=10, total_memory_mb=1024)
        group.kill_and_remove.assert_called_once()

    @unittest.skipUnless(sys.platform.startswith("linux"), "Linux cgroup v2 only")
    def test_real_cgroup_is_used_when_delegated(self):
        if not lean_cgroup.available():
            self.skipTest("No delegated memory controller on this host")
        try:
            probe = lean_cgroup.ProcessGroup.create(512)
        except lean_cgroup.CgroupUnavailable:
            self.skipTest("No write access to delegated cgroup v2")
        probe.kill_and_remove()
        code = (
            "import pathlib;"
            "group=next(line[3:] for line in "
            "pathlib.Path('/proc/self/cgroup').read_text().splitlines() "
            "if line.startswith('0::'));"
            "print((pathlib.Path('/sys/fs/cgroup')/group.lstrip('/')/"
            "'memory.max').read_text().strip())"
        )
        status, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], Path.cwd(),
            timeout=10, total_memory_mb=512)
        self.assertEqual(status, 0, log)
        self.assertFalse(timed_out)
        self.assertEqual(log.strip(), str(512 * 1024 * 1024))


if __name__ == "__main__":
    unittest.main()
