"""Real-process tests for the bounded local Lean runner (no Lean installation needed)."""
from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import time
import unittest

from unittest.mock import patch

from backend import lean_process


class LeanProcessTests(unittest.TestCase):
    def test_multi_megabyte_output_keeps_only_tail(self):
        code = (
            "import sys;"
            "sys.stdout.write('X'*3000000);sys.stdout.flush();"
            "sys.stderr.write('diagnostic at end')"
        )
        returncode, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], Path.cwd(), timeout=10)
        self.assertEqual(returncode, 0)
        self.assertFalse(timed_out)
        self.assertLessEqual(len(log.encode("utf-8")), lean_process.MAX_LOG_BYTES)
        self.assertTrue(log.endswith("diagnostic at end"))

    def test_memory_limit_config_rejects_invalid_values(self):
        for raw in ("0", "256", "65537", "not-an-integer", " 8192", "-1"):
            with self.subTest(raw=raw), patch.dict(os.environ, {"MATLIB_LEAN_MEMORY_MB": raw}):
                with self.assertRaises(ValueError):
                    lean_process.configured_memory_limit_mb()
        with patch.dict(os.environ, {"MATLIB_LEAN_MEMORY_MB": "8192"}):
            self.assertEqual(lean_process.configured_memory_limit_mb(), 8192)

    def test_requested_memory_limit_fails_closed_before_spawning_on_unsupported_host(self):
        with patch("backend.lean_process.memory_limit_supported", return_value=False), \
             patch("backend.lean_process.subprocess.Popen") as spawn:
            with self.assertRaises(lean_process.MemoryLimitUnavailable):
                lean_process.execute_registered(
                    [sys.executable, "-c", "print('must not execute')"],
                    Path.cwd(), timeout=3, memory_limit_mb=512)
        spawn.assert_not_called()

    @unittest.skipUnless(sys.platform.startswith("linux"), "Linux RLIMIT_AS only")
    def test_linux_memory_ceiling_is_inherited_by_exec_target(self):
        code = "import resource; print(resource.getrlimit(resource.RLIMIT_AS)[0])"
        returncode, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], Path.cwd(), timeout=10,
            memory_limit_mb=512)
        self.assertFalse(timed_out)
        self.assertEqual(returncode, 0, log)
        self.assertEqual(log.strip(), str(512 * 1024 * 1024))

    @unittest.skipUnless(sys.platform.startswith("linux"), "Linux RLIMIT_AS only")
    def test_linux_memory_ceiling_blocks_large_address_space_allocation(self):
        code = "a=bytearray(1200*1024*1024);print('allocated')"
        returncode, log, timed_out = lean_process.execute_registered(
            [sys.executable, "-c", code], Path.cwd(), timeout=10,
            memory_limit_mb=512)
        self.assertFalse(timed_out)
        self.assertNotEqual(returncode, 0)
        self.assertIn("MemoryError", log)

    @unittest.skipUnless(os.name == "posix", "POSIX process group behavior")
    def test_timeout_kills_descendant_not_just_parent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            started, survived = root / "started", root / "survived"
            child_code = (
                f"import time,pathlib;time.sleep(1.5);"
                f"pathlib.Path({str(survived)!r}).write_text('alive')"
            )
            parent_code = (
                "import sys,subprocess,time,pathlib;"
                f"subprocess.Popen([sys.executable,'-c',{child_code!r}]);"
                f"pathlib.Path({str(started)!r}).write_text('started');"
                "time.sleep(60)"
            )
            returncode, _, timed_out = lean_process.execute_registered(
                [sys.executable, "-c", parent_code], root, timeout=0.7)
            self.assertTrue(started.exists(), "Parent must actually spawn the child")
            self.assertIsNone(returncode)
            self.assertTrue(timed_out)
            time.sleep(1.7)
            self.assertFalse(survived.exists(), "Descendant must be terminated")

    @unittest.skipUnless(os.name == "posix", "POSIX process group behavior")
    def test_early_parent_exit_with_live_descendant_is_not_success(self):
        child_code = "import time;time.sleep(10)"
        parent_code = (
            "import sys,subprocess;"
            f"subprocess.Popen([sys.executable,'-c',{child_code!r}]);"
            "print('parent finished', flush=True)"
        )
        with self.assertRaisesRegex(RuntimeError, "left open"):
            lean_process.execute_registered(
                [sys.executable, "-c", parent_code], Path.cwd(), timeout=4)


if __name__ == "__main__":
    unittest.main()
