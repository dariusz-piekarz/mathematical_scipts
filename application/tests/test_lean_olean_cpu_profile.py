"""Regressions for the optional, read-only Lean .olean CPU profiler."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from backend import lean_environment
from scripts import profile_lean_olean_cpu


class LeanOleanCpuProfileTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "lean"
        src = self.root / "src"
        src.mkdir(parents=True)
        (src / "Example.lean").write_text(
            "theorem demo (p : Prop) : p → p := by intro h; exact h\n",
            encoding="utf-8",
        )
        (self.root / "manifest.json").write_text(
            json.dumps({"items": [{
                "id": "demo",
                "lean_file": "src/Example.lean",
                "source_document_sha256": "a" * 64,
            }]}),
            encoding="utf-8",
        )
        artifacts = self.root / ".lake" / "build" / "lib" / "lean"
        artifacts.mkdir(parents=True)
        (artifacts / "Example.olean").write_bytes(b"actual compiled bytes")
        (artifacts / "ignore.log").write_bytes(b"unrelated file")
        self.artifacts = artifacts

    def test_profile_preserves_real_digest_without_extra_digest_pass(self):
        before = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*") if p.is_file()
        }
        expected = lean_environment.compiled_artifacts_sha256(self.root)
        with patch.object(
            profile_lean_olean_cpu.lean_environment,
            "compiled_artifacts_sha256",
            wraps=lean_environment.compiled_artifacts_sha256,
        ) as digest:
            result = profile_lean_olean_cpu.profile_olean_cpu(self.root, limit=5)
        self.assertEqual(digest.call_count, 1)
        self.assertEqual(result["compiled_artifacts_sha256"], expected)
        self.assertEqual(result["actual_digest_calls"], 1)
        self.assertFalse(result["certificate"])
        self.assertEqual(result["limits"]["top_entries"], 5)
        self.assertTrue(result["hotspots"])
        self.assertLessEqual(len(result["hotspots"]), 5)
        self.assertTrue(all(
            isinstance(row["function"], str)
            and isinstance(row["cumulative_seconds"], float)
            and row["total_calls"] >= row["primitive_calls"] >= 0
            for row in result["hotspots"]
        ))
        self.assertEqual(
            sorted(result["hotspots"],
                   key=lambda row: row["cumulative_seconds"], reverse=True),
            result["hotspots"],
        )
        after = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*") if p.is_file()
        }
        self.assertEqual(before, after)

    def test_compare_genuine_benchmark_with_profile_without_extra_digest(self):
        from scripts import benchmark_lean_fingerprint as perf
        evidence = perf.benchmark(self.root, samples=2)
        original = lean_environment.compiled_artifacts_sha256
        with patch.object(profile_lean_olean_cpu.lean_environment,
                          "compiled_artifacts_sha256", wraps=original) as digest:
            cpu = profile_lean_olean_cpu.profile_olean_cpu(self.root)
            profile_lean_olean_cpu.require_matching_benchmark(evidence, cpu)
        self.assertEqual(digest.call_count, 1)
        self.assertEqual(evidence["compiled_artifacts_sha256"],
                         cpu["compiled_artifacts_sha256"])
        changed = dict(evidence)
        changed["compiled_artifacts_sha256"] = "b" * 64
        with self.assertRaisesRegex(RuntimeError, "changed between"):
            profile_lean_olean_cpu.require_matching_benchmark(changed, cpu)

    def test_reject_forged_or_incomplete_comparison_evidence(self):
        from scripts import benchmark_lean_fingerprint as perf
        baseline = perf.benchmark(self.root, samples=1)
        cpu = profile_lean_olean_cpu.profile_olean_cpu(self.root)
        for bad in (
            None, {}, {"compiled_artifacts_sha256": "invalid"},
            {**baseline, "certificate": True},
            {**baseline, "real_fingerprint_calls": True},
            {**baseline, "real_fingerprint_calls": 0},
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                profile_lean_olean_cpu.require_matching_benchmark(bad, cpu)
        with self.assertRaises(ValueError):
            profile_lean_olean_cpu.require_matching_benchmark(
                baseline, {**cpu, "actual_digest_calls": 0})

    def test_invalid_limits_fail_before_scanning(self):
        for limit in (0, 21, True, None, 1.5):
            with self.subTest(limit=limit), patch.object(
                profile_lean_olean_cpu.lean_environment,
                "compiled_artifacts_sha256",
            ) as digest:
                with self.assertRaises(ValueError):
                    profile_lean_olean_cpu.profile_olean_cpu(
                        self.root, limit=limit)
                digest.assert_not_called()

    def test_missing_or_invalid_source_refuses_profiling(self):
        (self.root / "src" / "Example.lean").unlink()
        with patch.object(
            profile_lean_olean_cpu.lean_environment, "compiled_artifacts_sha256"
        ) as digest:
            with self.assertRaises(ValueError):
                profile_lean_olean_cpu.profile_olean_cpu(self.root)
            digest.assert_not_called()

    def test_rejected_olean_symlink_is_not_turned_into_a_report(self):
        target = self.root / "other.olean"
        target.write_bytes(b"external bytes")
        symlink = self.artifacts / "Alias.olean"
        try:
            symlink.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            profile_lean_olean_cpu.profile_olean_cpu(self.root)


if __name__ == "__main__":
    unittest.main()
