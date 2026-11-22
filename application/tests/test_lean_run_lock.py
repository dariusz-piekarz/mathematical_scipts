"""Cross-process regression checks for the local Lean compilation lock."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

from backend import lean_run_lock


class LeanRunLockTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "application" / "lean"
        self.root.mkdir(parents=True)

    def test_lock_releases_after_exception_without_reclassifying_os_errors(self):
        with self.assertRaisesRegex(OSError, "toolchain failure"):
            with lean_run_lock.exclusive(self.root):
                raise OSError("toolchain failure")
        with lean_run_lock.exclusive(self.root):
            pass

    def test_contention_between_threads_is_denied(self):
        # Separate opens in one process are distinct OS lock descriptions.
        with lean_run_lock.exclusive(self.root):
            with self.assertRaises(lean_run_lock.RunnerBusy):
                with lean_run_lock.exclusive(self.root):
                    self.fail("second invocation must not execute")
        with lean_run_lock.exclusive(self.root):
            pass

    def test_cross_process_contention_and_release(self):
        marker = Path(self.tmp.name) / "ready"
        child_code = (
            "from pathlib import Path;"
            "import time;"
            "from backend import lean_run_lock;"
            f"root=Path({str(self.root)!r});"
            f"ready=Path({str(marker)!r});"
            "\nwith lean_run_lock.exclusive(root):"
            "\n ready.write_text('locked');"
            "\n time.sleep(1.5)"
        )
        process = subprocess.Popen(
            [sys.executable, "-c", child_code], cwd=Path(__file__).resolve().parents[1],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        try:
            deadline = time.monotonic() + 5
            while not marker.is_file() and process.poll() is None and time.monotonic() < deadline:
                time.sleep(0.025)
            if not marker.is_file():
                _, errors = process.communicate(timeout=2)
                self.fail(f"child never acquired lock: {errors.decode(errors='replace')}")
            with self.assertRaises(lean_run_lock.RunnerBusy):
                with lean_run_lock.exclusive(self.root):
                    self.fail("cross-process simultaneous run")
            _, stderr = process.communicate(timeout=5)
            self.assertEqual(process.returncode, 0, stderr.decode(errors="replace"))
            with lean_run_lock.exclusive(self.root):
                pass
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate(timeout=5)

    def test_killed_owner_releases_os_lock_without_deleting_lockfile(self):
        child_code = (
            "from pathlib import Path;"
            "import os;"
            "from backend import lean_run_lock;"
            f"\nwith lean_run_lock.exclusive(Path({str(self.root)!r})):"
            "\n os._exit(0)"
        )
        done = subprocess.run(
            [sys.executable, "-c", child_code],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True, timeout=8
        )
        self.assertEqual(done.returncode, 0, done.stderr.decode(errors="replace"))
        with lean_run_lock.exclusive(self.root):
            self.assertTrue((self.root.parent / "data" / "lean_runs" / ".runner.lock").is_file())


if __name__ == "__main__":
    unittest.main()
