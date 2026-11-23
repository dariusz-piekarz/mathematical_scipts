"""Tests for same-host, read-only comparison of .olean path conversion."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import benchmark_lean_paths as paths


class LeanPathMicrobenchmarkTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "lean"
        (self.root / "src").mkdir(parents=True)
        (self.root / "src" / "Example.lean").write_text(
            "theorem id (p : Prop) : p → p := by intro h; exact h\n",
            encoding="utf-8",
        )
        (self.root / "manifest.json").write_text(
            json.dumps({"items": [{
                "id": "id",
                "lean_file": "src/Example.lean",
                "source_document_sha256": "a" * 64,
            }]}), encoding="utf-8")
        self.project = self.root / ".lake" / "build" / "lib" / "lean"
        self.mathlib = (self.root / ".lake" / "packages" / "mathlib"
                        / ".lake" / "build" / "lib" / "lean")
        for root, name in (
            (self.project, "A.olean"),
            (self.project, "nested/B.olean"),
            (self.project, "nested/Unicode_ż.olean"),
            (self.mathlib, "Mathlib/Z.olean"),
            (self.mathlib, ".olean"),
            (self.mathlib, "Ignore.olean.tmp"),
        ):
            file = root / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(name.encode("utf-8"))

    def test_paired_methods_use_exact_same_population_and_no_content_changes(self):
        before = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*") if p.is_file()
        }
        groups = paths.collect_names(self.root)
        legacy = paths.convert_names(groups, optimized=False)
        optimized = paths.convert_names(groups, optimized=True)
        self.assertEqual(legacy, optimized)
        self.assertEqual(len(legacy), 4)
        self.assertEqual(len(groups), 3)
        self.assertIn(("package/mathlib", "Mathlib/Z.olean"), legacy)
        self.assertIn(("project", "nested/Unicode_ż.olean"), legacy)

        result = paths.benchmark(self.root, samples=3, expected_candidates=4)
        self.assertFalse(result["certificate"])
        self.assertEqual(result["olean_candidates"], 4)
        self.assertEqual(result["populated_directories"], 3)
        self.assertEqual(result["legacy_relative_to_calls_per_sample"], 4)
        self.assertEqual(result["optimized_relative_to_calls_per_sample"], 3)
        self.assertEqual(result["samples_per_method"], 3)
        for label in ("legacy", "optimized"):
            self.assertEqual(len(result["samples_seconds"][label]), 3)
            self.assertGreaterEqual(result["median_seconds"][label], 0)
        after = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*") if p.is_file()
        }
        self.assertEqual(before, after)

    def test_relative_to_invocations_are_bounded_by_populated_directories(self):
        groups = paths.collect_names(self.root)
        original = Path.relative_to
        seen = []

        def observed(obj, *args, **kwargs):
            seen.append(obj)
            return original(obj, *args, **kwargs)

        with patch.object(Path, "relative_to", observed):
            paths.convert_names(groups, optimized=False)
            legacy_count = len(seen)
            seen.clear()
            paths.convert_names(groups, optimized=True)
            optimized_count = len(seen)
        self.assertEqual(legacy_count, 4)
        self.assertEqual(optimized_count, 3)

    def test_changing_expected_population_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "name population changed"):
            paths.benchmark(self.root, samples=2, expected_candidates=3)
        for value in (0, 1, 13, None, True, 2.0):
            with self.subTest(value=value):
                if value is None:
                    continue  # None is deliberately allowed as an omitted expectation
                with self.assertRaises(ValueError):
                    paths.benchmark(self.root, samples=value)
        for count in (-1, 2.5, True):
            with self.subTest(count=count), self.assertRaises(ValueError):
                paths.benchmark(self.root, expected_candidates=count)

    def test_symlinked_olean_is_rejected_without_following_it(self):
        path = self.project / "Bad.olean"
        try:
            path.symlink_to(self.project / "A.olean")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            paths.benchmark(self.root, samples=2)


if __name__ == "__main__":
    unittest.main()
