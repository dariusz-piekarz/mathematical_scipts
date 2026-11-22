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

    def test_sibling_module_edit_addition_removal_and_rename_invalidate_cache(self):
        sibling = self.root / "src" / "Helper.lean"
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        sibling.write_text("def helper : Nat := 1\n", encoding="utf-8")
        self.assertTrue(last_run("sample", self.fp(),
                                 results_root=self.output)["previous_run_outdated"])
        changed = self.fp()
        self.assertNotEqual(original["project_sources_sha256"],
                            changed["project_sources_sha256"])
        sibling.write_text("def helper : Nat := 2\n", encoding="utf-8")
        self.assertNotEqual(changed["project_sources_sha256"],
                            self.fp()["project_sources_sha256"])
        sibling.rename(self.root / "src" / "Renamed.lean")
        self.assertNotEqual(changed["project_sources_sha256"],
                            self.fp()["project_sources_sha256"])
        (self.root / "src" / "Renamed.lean").unlink()
        self.assertEqual(original["project_sources_sha256"],
                         self.fp()["project_sources_sha256"])
        self.assertEqual(last_run("sample", self.fp(),
                                  results_root=self.output)["proof_status"], "compiled")

    def test_manifest_and_lakefile_lean_invalidate_declared_environment(self):
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        manifest = self.root / "manifest.json"
        manifest.write_text('{"items":[]}', encoding="utf-8")
        self.assertNotEqual(original["toolchain_sha256"], self.fp()["toolchain_sha256"])
        self.assertTrue(last_run("sample", self.fp(),
                                 results_root=self.output)["previous_run_outdated"])
        manifest.unlink()
        lakefile = self.root / "lakefile.lean"
        lakefile.write_text("import Lake\nopen Lake DSL\n", encoding="utf-8")
        self.assertNotEqual(original["toolchain_sha256"], self.fp()["toolchain_sha256"])

    def test_legacy_record_schema_is_not_accepted_as_current_compilation(self):
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        path = self.output / "sample.json"
        import json
        legacy = json.loads(path.read_text(encoding="utf-8"))
        legacy["schema_version"] = 1
        legacy.pop("project_sources_sha256", None)
        path.write_text(json.dumps(legacy), encoding="utf-8")
        result = last_run("sample", self.fp(), results_root=self.output)
        self.assertEqual(result["proof_status"], "not_run")
        self.assertTrue(result["run_record_invalid"])
        self.assertFalse(result["run_cached"])

    def test_symlinked_local_source_is_rejected(self):
        target = self.root / "module.lean"
        target.write_text("def external : Nat := 1\n", encoding="utf-8")
        link = self.root / "src" / "External.lean"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Symbolic links unavailable on this system")
        with self.assertRaises(ValueError):
            self.fp()

    def test_external_checkout_identity_change_revokes_saved_success(self):
        from unittest.mock import patch
        with patch("backend.lean_environment.external_packages_sha256",
                   return_value="a" * 64):
            old = self.fp()
        save_run("sample", old, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        with patch("backend.lean_environment.external_packages_sha256",
                   return_value="b" * 64):
            current = self.fp()
        self.assertNotEqual(old["external_packages_sha256"],
                            current["external_packages_sha256"])
        stale = last_run("sample", current, results_root=self.output)
        self.assertEqual(stale["proof_status"], "not_run")
        self.assertTrue(stale["previous_run_outdated"])

    def test_actual_toolchain_change_revokes_saved_success(self):
        from unittest.mock import patch
        with patch("backend.lean_environment.executable_toolchain_sha256",
                   return_value="a" * 64):
            old = self.fp()
        save_run("sample", old, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        with patch("backend.lean_environment.executable_toolchain_sha256",
                   return_value="b" * 64):
            current = self.fp()
        self.assertTrue(last_run("sample", current,
                                 results_root=self.output)["previous_run_outdated"])

    def test_previous_v2_schema_is_invalidated(self):
        import json
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        path = self.output / "sample.json"
        old = json.loads(path.read_text(encoding="utf-8"))
        old["schema_version"] = 2
        old.pop("external_packages_sha256")
        old.pop("executable_toolchain_sha256")
        path.write_text(json.dumps(old), encoding="utf-8")
        cached = last_run("sample", self.fp(), results_root=self.output)
        self.assertFalse(cached["run_cached"])
        self.assertTrue(cached["run_record_invalid"])

    def test_olean_artifact_edit_revokes_compilation_history(self):
        build = self.root / ".lake" / "build" / "lib" / "lean"
        build.mkdir(parents=True)
        artifact = build / "Auxiliary.olean"
        artifact.write_bytes(b"compiled module A")
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        artifact.write_bytes(b"compiled module B")
        current = self.fp()
        self.assertNotEqual(original["compiled_artifacts_sha256"],
                            current["compiled_artifacts_sha256"])
        state = last_run("sample", current, results_root=self.output)
        self.assertEqual(state["proof_status"], "not_run")
        self.assertTrue(state["previous_run_outdated"])
        self.assertFalse(state["run_cached"])

    def test_missing_to_populated_olean_tree_revokes_cached_result(self):
        original = self.fp()
        save_run("sample", original, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        build = self.root / ".lake" / "build" / "lib" / "lean"
        build.mkdir(parents=True)
        (build / "Example.olean").write_bytes(b"compiled")
        self.assertTrue(last_run("sample", self.fp(),
                                 results_root=self.output)["previous_run_outdated"])

    def test_previous_v3_schema_not_accepted(self):
        import json
        expected = self.fp()
        save_run("sample", expected, proof_status="compiled",
                 detail="real exit 0", results_root=self.output)
        record = self.output / "sample.json"
        old = json.loads(record.read_text(encoding="utf-8"))
        old["schema_version"] = 3
        old.pop("compiled_artifacts_sha256")
        record.write_text(json.dumps(old), encoding="utf-8")
        state = last_run("sample", self.fp(), results_root=self.output)
        self.assertEqual(state["proof_status"], "not_run")
        self.assertTrue(state["run_record_invalid"])
        self.assertFalse(state["run_cached"])

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
