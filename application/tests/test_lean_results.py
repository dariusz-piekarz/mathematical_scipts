"""Unit tests for persisted Lean diagnostics and their provenance fingerprints."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from backend.lean_results import fingerprint, last_run, save_run


class LeanResultsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = self.root / "results"
        self.code = self.root / "src" / "Example.lean"
        self.code.parent.mkdir()
        self.code.write_text("theorem sample : True := by trivial\n", encoding="utf-8")
        (self.root / "lean-toolchain").write_text("leanprover/lean4:v4.26.0\n", encoding="utf-8")
        (self.root / "lakefile.toml").write_text('name = "Test"\n', encoding="utf-8")
        self.source_sha = "a" * 64

    def fp(self):
        return fingerprint(self.source_sha, self.code, self.root)

    def test_latest_real_compilation_survives_reopen(self):
        fp = self.fp()
        self.assertEqual(last_run("sample", fp, results_root=self.output)["proof_status"], "not_run")
        record = save_run("sample", fp, proof_status="compiled", detail="exit 0",
                          log="#print axioms sample", results_root=self.output)
        reopened = last_run("sample", fp, results_root=self.output)
        self.assertEqual(reopened["proof_status"], "compiled")
        self.assertTrue(reopened["run_cached"])
        self.assertEqual(reopened["last_run_at"], record["finished_at"])
        self.assertIn("axioms", reopened["last_run_log"])
        self.assertFalse(reopened["certificate"])

    def test_invalidated_by_lean_source_and_reverted_on_restore(self):
        original = self.fp()
        save_run("sample", original, proof_status="compiled", detail="ok", results_root=self.output)
        self.code.write_text("theorem sample : True := by exact True.intro\n", encoding="utf-8")
        self.assertTrue(last_run("sample", self.fp(), results_root=self.output)["previous_run_outdated"])
        self.code.write_text("theorem sample : True := by trivial\n", encoding="utf-8")
        self.assertEqual(last_run("sample", self.fp(), results_root=self.output)["proof_status"], "compiled")

    def test_invalidated_by_document_hash(self):
        old = self.fp()
        save_run("sample", old, proof_status="failed", detail="bad", results_root=self.output)
        self.source_sha = "b" * 64
        new = last_run("sample", self.fp(), results_root=self.output)
        self.assertEqual(new["proof_status"], "not_run")
        self.assertTrue(new["previous_run_outdated"])

    def test_invalidated_by_toolchain_or_lockfile(self):
        old = self.fp()
        save_run("sample", old, proof_status="compiled", detail="ok", results_root=self.output)
        (self.root / "lake-manifest.json").write_text('{"packages": []}', encoding="utf-8")
        self.assertTrue(last_run("sample", self.fp(), results_root=self.output)["previous_run_outdated"])
        self.assertNotEqual(old["toolchain_sha256"], self.fp()["toolchain_sha256"])

    def test_corrupt_record_cannot_be_treated_as_success(self):
        self.output.mkdir()
        (self.output / "sample.json").write_text('{broken', encoding="utf-8")
        result = last_run("sample", self.fp(), results_root=self.output)
        self.assertEqual(result["proof_status"], "not_run")
        self.assertTrue(result["run_record_invalid"])
        self.assertFalse(result["run_cached"])

    def test_rejects_synthetic_status_and_unsafe_id(self):
        with self.assertRaises(ValueError):
            save_run("sample", self.fp(), proof_status="verified", detail="bad", results_root=self.output)
        with self.assertRaises(ValueError):
            save_run("../outside", self.fp(), proof_status="compiled", detail="bad", results_root=self.output)
        self.assertFalse(self.output.exists())

    def test_only_latest_execution_is_shown(self):
        fp = self.fp()
        save_run("sample", fp, proof_status="failed", detail="bad", results_root=self.output)
        save_run("sample", fp, proof_status="compiled", detail="ok", results_root=self.output)
        self.assertEqual(last_run("sample", fp, results_root=self.output)["proof_status"], "compiled")

    def test_oversize_log_is_truncated(self):
        fp = self.fp()
        save_run("sample", fp, proof_status="failed", detail="error", log="x" * 32000,
                 results_root=self.output)
        result = last_run("sample", fp, results_root=self.output)
        self.assertEqual(len(result["last_run_log"]), 16000)
        self.assertFalse(result["certificate"])


if __name__ == "__main__":
    unittest.main()
