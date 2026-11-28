"""Synthetic inventory tests; real full-import observation is CI-only."""
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

from scripts import lean_full_import_probe as probe


class FullImportInventoryTests(unittest.TestCase):
    def test_sizes_and_missing_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "a.olean").write_bytes(b"abc")
            (root / "nested/b.olean").write_bytes(b"12345")
            row = probe.inventory(root, deadline=time.monotonic() + 10, remaining=10)
            self.assertEqual(row, dict(entries=3, files=2, bytes=8, largest_file=5,
                                       symlinks=0, missing=False))
            self.assertTrue(probe.inventory(root / "absent", deadline=time.monotonic() + 10,
                                            remaining=10)["missing"])

    def test_entry_and_time_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a").write_bytes(b"x")
            with self.assertRaises(ValueError):
                probe.inventory(root, deadline=time.monotonic() + 10, remaining=0)
            with self.assertRaises(ValueError):
                probe.inventory(root, deadline=time.monotonic() - 1, remaining=10)

    def test_does_not_follow_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "real").mkdir()
            (root / "real/a").write_bytes(b"x")
            try:
                (root / "alias").symlink_to(root / "real", target_is_directory=True)
            except (OSError, NotImplementedError):
                # Native Windows can lack symlink permission. Do not mark the
                # test skipped: exercise the same nonlinked inventory there.
                row = probe.inventory(root, deadline=time.monotonic() + 10, remaining=10)
                self.assertEqual(row["files"], 1)
                return
            row = probe.inventory(root, deadline=time.monotonic() + 10, remaining=10)
            self.assertEqual((row["files"], row["bytes"], row["symlinks"]), (1, 1, 1))


class FullImportTraceBudgetTests(unittest.TestCase):
    def test_measurement_does_not_change_default_trace_limit(self):
        raw = b'openat(AT_FDCWD, "/lib/libc.so.6", O_RDONLY) = 3</lib/libc.so.6>\n'
        with patch.object(probe.offline, "MAX_TRACE_BYTES", 1):
            with self.assertRaises(ValueError):
                probe.offline.parse_trace(raw, cwd=Path("/"))
            self.assertEqual(len(probe.offline.parse_trace(
                raw, cwd=Path("/"), measurement_only=True)), 1)
            with self.assertRaises(ValueError):
                probe.offline.parse_trace(raw, cwd=Path("/"))

    def test_measurement_entry_limit_is_separate_and_bounded(self):
        raw = b'openat(AT_FDCWD, "/lib/libc.so.6", O_RDONLY) = 3</lib/libc.so.6>\n'
        with patch.object(probe.artifacts, "MAX_ENTRIES", 0):
            with self.assertRaises(ValueError):
                probe.offline.parse_trace(raw, cwd=Path("/"))
            self.assertEqual(len(probe.offline.parse_trace(
                raw, cwd=Path("/"), measurement_only=True)), 1)
        with patch.object(probe.offline, "MEASUREMENT_TRACE_ENTRIES", 0):
            with self.assertRaises(ValueError):
                probe.offline.parse_trace(raw, cwd=Path("/"), measurement_only=True)
