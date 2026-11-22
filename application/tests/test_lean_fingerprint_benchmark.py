"""Tests of the read-only provenance timing utility, not Lean verification."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import benchmark_lean_fingerprint as perf


class LeanFingerprintBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "lean"
        (self.root / "src").mkdir(parents=True)
        (self.root / "src" / "Example.lean").write_text(
            "theorem demo (p : Prop) : p → p := by intro h; exact h\\n",
            encoding="utf-8")
        self.entry = {
            "id": "demo", "lean_file": "src/Example.lean",
            "source_document_sha256": "a" * 64,
        }
        self.save_manifest()

    def save_manifest(self):
        (self.root / "manifest.json").write_text(
            json.dumps({"items": [self.entry]}), encoding="utf-8")

    def test_real_hashes_of_local_fixture_are_repeatable_without_cache_or_history(self):
        prior = {file.relative_to(self.root): file.read_bytes()
                 for file in self.root.rglob("*") if file.is_file()}
        result = perf.benchmark(self.root, samples=3)
        self.assertFalse(result["certificate"])
        self.assertEqual(result["real_fingerprint_calls"], 3)
        self.assertEqual(len(result["samples_seconds"]), 3)
        self.assertGreaterEqual(result["total_seconds"], 0)
        after = {file.relative_to(self.root): file.read_bytes()
                 for file in self.root.rglob("*") if file.is_file()}
        self.assertEqual(prior, after)

    def test_environment_change_aborts_timing_not_cached(self):
        with patch.object(perf.lean_results, "fingerprint",
                          side_effect=[{"project_sources_sha256": "a"},
                                       {"project_sources_sha256": "b"}]) as probe:
            with self.assertRaisesRegex(RuntimeError, "changed during"):
                perf.benchmark(self.root, samples=2)
        self.assertEqual(probe.call_count, 2)

    def test_invalid_samples_and_manifest_paths_fail_closed(self):
        for value in (0, 7, True, None, 2.5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                perf.benchmark(self.root, samples=value)
        for path in ("../outside.lean", "src/../outside.lean",
                     "src/Example.txt", "src/\\\\unc.lean"):
            with self.subTest(path=path):
                self.entry["lean_file"] = path
                self.save_manifest()
                with self.assertRaises(ValueError):
                    perf.benchmark(self.root, samples=1)


if __name__ == "__main__":
    unittest.main()
