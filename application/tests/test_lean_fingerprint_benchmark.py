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
        self.assertEqual(
            set(result["component_samples_seconds"]),
            {"local_sources", "external_packages", "olean_artifacts", "tool_executables"})
        self.assertEqual(
            set(result["component_median_seconds"]),
            set(result["component_samples_seconds"]))
        for name, measurements in result["component_samples_seconds"].items():
            with self.subTest(component=name):
                self.assertEqual(len(measurements), 3)
                self.assertTrue(all(0 <= value <= result["max_seconds"]
                                    for value in measurements))
        self.assertEqual(len(result["other_work_samples_seconds"]), 3)
        self.assertTrue(all(value >= 0 for value in result["other_work_samples_seconds"]))
        after = {file.relative_to(self.root): file.read_bytes()
                 for file in self.root.rglob("*") if file.is_file()}
        self.assertEqual(prior, after)

    def install_olean(self, data=b"compiled mathlib artifact"):
        path = self.root / ".lake" / "build" / "lib" / "lean" / "Local" / "Example.olean"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def test_olean_subprofile_counts_real_file_io_without_a_second_digest(self):
        content = b"an actual compiled artifact"
        self.install_olean(content)
        original = perf.lean_results.lean_environment.compiled_artifacts_sha256
        uninstrumented = original(self.root)
        instrumented, details = perf._profile_olean_substeps(original, self.root)
        self.assertEqual(instrumented, uninstrumented)
        self.assertEqual(details["counts"]["content_bytes_read"], len(content))
        # Path.lstat() delegates to Path.stat() in Python 3.13. The
        # operation counters may include both calls; their nested durations
        # must be counted once so buckets never exceed elapsed wall time.
        self.assertLessEqual(sum(details["seconds"].values()),
                             details["total_seconds"] + 1e-7)
        with patch.object(perf.lean_results.lean_environment,
                          "compiled_artifacts_sha256", wraps=original) as digest:
            report = perf.benchmark(self.root, samples=2)
        # The timing process executes ONE genuine digest per fingerprint,
        # never a replacement, pre-scan or additional .olean verification.
        self.assertEqual(digest.call_count, 2)
        self.assertEqual(len(report["olean_subprofile_total_seconds"]), 2)
        self.assertEqual(set(report["olean_breakdown_samples_seconds"]),
                         set(perf.OLEAN_TIME_BUCKETS))
        self.assertEqual(set(report["olean_breakdown_median_seconds"]),
                         set(perf.OLEAN_TIME_BUCKETS))
        for timing in report["olean_breakdown_samples_seconds"].values():
            self.assertEqual(len(timing), 2)
            self.assertTrue(all(v >= 0 for v in timing))
        for observed in report["olean_io_samples"]:
            self.assertEqual(set(observed), set(perf.OLEAN_IO_COUNTERS))
            self.assertEqual(observed["olean_files_opened"], 1)
            self.assertEqual(observed["content_bytes_read"], len(content))
            self.assertGreaterEqual(observed["content_read_calls"], 1)
            self.assertGreaterEqual(observed["directories_visited"], 1)
            self.assertEqual(observed["walk_files_seen"], 1)
            self.assertEqual(observed["olean_name_candidates"], 1)
            self.assertEqual(observed["non_olean_names_skipped"], 0)
            self.assertGreaterEqual(observed["stat_calls"], 2)
            self.assertGreaterEqual(observed["fstat_calls"], 1)

    def test_olean_filename_counters_measure_real_skipped_names(self):
        """Mixed on-disk files are counted without altering actual SHA256."""
        artifact = self.install_olean(b"hash this artifact")
        ignored = ("not-lean.txt", ".olean", "copy.olean.old",
                   "module.olean.tmp", ".other")
        for name in ignored + ("nested/Example.olean",):
            path = artifact.parent / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(name.encode("utf-8"))
        original = perf.lean_results.lean_environment.compiled_artifacts_sha256
        baseline = original(self.root)
        fingerprint, details = perf._profile_olean_substeps(original, self.root)
        self.assertEqual(fingerprint, baseline)
        counts = details["counts"]
        self.assertEqual(counts["walk_files_seen"], 7)
        self.assertEqual(counts["olean_name_candidates"], 2)
        self.assertEqual(counts["non_olean_names_skipped"], 5)
        self.assertEqual(counts["olean_files_opened"], 2)
        self.assertEqual(
            counts["walk_files_seen"],
            counts["olean_name_candidates"] + counts["non_olean_names_skipped"])
        self.assertEqual(counts["content_bytes_read"],
                         len(b"hash this artifact") + len(b"nested/Example.olean"))

    def test_olean_metadata_only_respects_real_hash_budget(self):
        self.install_olean(b"larger than the budget")
        with patch.object(perf.lean_results.lean_environment,
                          "MAX_OLEAN_HASH_BYTES", 1):
            result = perf.benchmark(self.root, samples=2)
        for observed in result["olean_io_samples"]:
            self.assertEqual(observed["olean_files_opened"], 0)
            self.assertEqual(observed["content_read_calls"], 0)
            self.assertEqual(observed["content_bytes_read"], 0)
            self.assertGreaterEqual(observed["stat_calls"], 1)

    def test_olean_probes_are_restored_on_rejected_symlink(self):
        target = self.root / "target"
        target.write_bytes(b"compiled")
        link = self.install_olean()
        link.unlink()
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Symbolic links are not available")
        before = (Path.stat, Path.lstat, Path.open, perf.os.walk, perf.os.fstat)
        with self.assertRaisesRegex(ValueError, "Symlinked"):
            perf.benchmark(self.root, samples=1)
        self.assertEqual(before,
                         (Path.stat, Path.lstat, Path.open, perf.os.walk, perf.os.fstat))

    def test_environment_change_aborts_timing_not_cached(self):
        # Keep the full production fingerprint running in both measurements,
        # changing just the dependency evidence without short-circuiting it.
        with patch.object(perf.lean_results.lean_environment,
                          "external_packages_sha256",
                          side_effect=["a" * 64, "b" * 64]) as probe:
            with self.assertRaisesRegex(RuntimeError, "changed during"):
                perf.benchmark(self.root, samples=2)
        self.assertEqual(probe.call_count, 2)

    def test_timing_instrumentation_is_removed_after_execution(self):
        original_sources = perf.lean_results._project_sources_sha256
        original_packages = perf.lean_results.lean_environment.external_packages_sha256
        original_artifacts = perf.lean_results.lean_environment.compiled_artifacts_sha256
        original_binaries = perf.lean_results.lean_environment.executable_toolchain_sha256
        perf.benchmark(self.root, samples=2)
        self.assertIs(perf.lean_results._project_sources_sha256, original_sources)
        self.assertIs(perf.lean_results.lean_environment.external_packages_sha256,
                      original_packages)
        self.assertIs(perf.lean_results.lean_environment.compiled_artifacts_sha256,
                      original_artifacts)
        self.assertIs(perf.lean_results.lean_environment.executable_toolchain_sha256,
                      original_binaries)

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
