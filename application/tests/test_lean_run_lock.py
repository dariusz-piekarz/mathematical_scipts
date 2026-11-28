"""Cross-process regression checks for the local Lean compilation lock."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

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

    @unittest.skipUnless(os.name == "posix", "Windows cannot rename an open CRT lock file")
    def test_replaced_lock_file_during_open_is_rejected(self):
        # Models a race in the interval between os.open and file locking.
        original_open = os.open

        def swap_path(path, flags, mode=0o600):
            fd = original_open(path, flags, mode)
            current = Path(path)
            current.rename(current.with_name(".runner.old"))
            current.write_bytes(b"replacement")
            return fd

        with patch("backend.lean_run_lock.os.open", side_effect=swap_path):
            with self.assertRaises(lean_run_lock.RunnerLockUnavailable):
                with lean_run_lock.exclusive(self.root):
                    self.fail("redirected path must not acquire runner lock")
        lockfile = self.root.parent / "data" / "lean_runs" / ".runner.lock"
        self.assertEqual(lockfile.read_bytes(), b"replacement")
        with lean_run_lock.exclusive(self.root):
            pass

    @unittest.skipUnless(os.name == "nt", "Native Windows file-sharing contract")
    def test_windows_open_lock_file_cannot_be_renamed(self):
        lockfile = self.root.parent / "data" / "lean_runs" / ".runner.lock"
        moved = lockfile.with_name(".runner.renamed")
        with lean_run_lock.exclusive(self.root):
            with self.assertRaises(OSError):
                lockfile.rename(moved)
            self.assertTrue(lockfile.is_file())
            self.assertFalse(moved.exists())
        with lean_run_lock.exclusive(self.root):
            pass

    def test_linked_lock_directory_is_rejected_before_os_open(self):
        def link_detected(path):
            return Path(path).name == "lean_runs"

        with patch("backend.lean_run_lock._link_or_junction",
                   side_effect=link_detected), \
             patch("backend.lean_run_lock.os.open") as opening:
            with self.assertRaises(lean_run_lock.RunnerLockUnavailable):
                with lean_run_lock.exclusive(self.root):
                    self.fail("linked data directory must never be used")
        opening.assert_not_called()

    @unittest.skipUnless(os.name == "nt", "Native Windows junction test")
    def test_native_windows_junction_directory_is_rejected(self):
        parent = self.root.parent / "data"
        parent.mkdir()
        target = Path(self.tmp.name) / "redirected"
        target.mkdir()
        junction = parent / "lean_runs"
        proc = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(junction), str(target)],
            capture_output=True, text=True, timeout=10,
        )
        if proc.returncode != 0:
            self.skipTest("Windows junction creation unavailable: " + proc.stderr[:100])
        self.assertTrue(junction.is_junction())
        with self.assertRaises(lean_run_lock.RunnerLockUnavailable):
            with lean_run_lock.exclusive(self.root):
                self.fail("Windows junction cannot redirect the lock directory")
        self.assertFalse((target / ".runner.lock").exists())

    @unittest.skipUnless(os.name == "posix", "Requires POSIX directory symlinks")
    def test_actual_linked_lock_directory_is_rejected(self):
        parent = self.root.parent / "data"
        parent.mkdir()
        real = Path(self.tmp.name) / "redirected"
        real.mkdir()
        (parent / "lean_runs").symlink_to(real, target_is_directory=True)
        with self.assertRaises(lean_run_lock.RunnerLockUnavailable):
            with lean_run_lock.exclusive(self.root):
                self.fail("symlinked lock folder must never be used")
        self.assertFalse((real / ".runner.lock").exists())

    @unittest.skipUnless(os.name == "posix" and hasattr(os, "O_NOFOLLOW"),
                         "POSIX O_NOFOLLOW requirement")
    def test_symlinked_lock_file_fails_closed(self):
        path = self.root.parent / "data" / "lean_runs"
        path.mkdir(parents=True)
        target = Path(self.tmp.name) / "untouched"
        target.write_text("protected", encoding="utf-8")
        (path / ".runner.lock").symlink_to(target)
        with self.assertRaises(lean_run_lock.RunnerLockUnavailable):
            with lean_run_lock.exclusive(self.root):
                self.fail("symlink must not be followed")
        self.assertEqual(target.read_text(encoding="utf-8"), "protected")

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
