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


    def test_nonportable_names_are_counted_only_in_measurement(self):
        raw = b'openat(AT_FDCWD, "/lib/Con.olean", O_RDONLY) = 3</lib/Con.olean>\n'
        seen = set()
        with self.assertRaises(ValueError):
            probe.offline.parse_trace(raw, cwd=Path("/"))
        with self.assertRaises(ValueError):
            probe.offline.parse_trace(raw, cwd=Path("/"), nonportable_components=seen)
        paths = probe.offline.parse_trace(raw, cwd=Path("/"), measurement_only=True,
                                          nonportable_components=seen)
        self.assertEqual(len(paths), 1)
        self.assertEqual(seen, {"Con.olean"})
        with self.assertRaises(ValueError):
            probe.offline.destination(next(iter(paths)), Path("/tools"), {})
        target = probe.offline.destination(next(iter(paths)), Path("/tools"), {},
                                           nonportable_components=seen)
        self.assertEqual(str(target), "lib/Con.olean")
        with self.assertRaises(ValueError):
            probe.offline.destination(Path("/home/Con.olean"), Path("/tools"), {},
                                      nonportable_components=seen)

    def test_measurement_still_rejects_deleted_and_write_descriptors(self):
        for raw in (
            b'openat(AT_FDCWD, "/lib/a", O_RDONLY) = 3</lib/a (deleted)>\n',
            b'openat(AT_FDCWD, "/lib/Con.olean", O_RDWR) = 3</lib/Con.olean>\n',
        ):
            with self.assertRaises(ValueError):
                probe.offline.parse_trace(raw, cwd=Path("/"), measurement_only=True,
                                          nonportable_components=set())


class FixedProfileTests(unittest.TestCase):
    def test_scoped_profile_changes_only_imports(self):
        full = probe.fixture_source("full")
        scoped = probe.fixture_source("scoped")
        self.assertEqual(full, probe.SOURCE)
        self.assertEqual(scoped, probe.SCOPED_SOURCE)
        imports = "".join("import " + name + "\n" for name in probe.SCOPED_IMPORTS)
        self.assertTrue(scoped.startswith(imports))
        self.assertEqual(scoped[len(imports):], full.split("\n", 1)[1])
        self.assertNotIn("import Mathlib\n", scoped)
        self.assertEqual(len(set(probe.SCOPED_IMPORTS)), len(probe.SCOPED_IMPORTS))

    def test_unknown_profile_is_rejected(self):
        for profile in ("", "import Mathlib", "custom", None):
            with self.assertRaises(ValueError):
                probe.fixture_source(profile)


class ScopedFixtureCopyTests(unittest.TestCase):
    def test_only_header_changes(self):
        full = b"import Mathlib\n\ntheorem atlas_draft : True := by trivial\n\n#print axioms atlas_draft\n"
        scoped = probe.scoped_fixture_copy(full)
        self.assertEqual(scoped, probe.SCOPED_HEADER.encode("ascii") + full.split(b"\n", 1)[1])
        self.assertEqual(probe.full_fixture_copy(scoped), full)
        with self.assertRaises(ValueError):
            probe.full_fixture_copy(full)

    def test_invalid_fixture_shape_fails(self):
        for value in (None, "import Mathlib", b"import Aesop\n", b"import Mathlib\n",
                      b"import Mathlib\n" + b"x" * 66000 + b"\n#print axioms atlas_draft\n"):
            with self.assertRaises(ValueError):
                probe.scoped_fixture_copy(value)
