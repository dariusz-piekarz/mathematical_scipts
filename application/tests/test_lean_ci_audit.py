"""Offline tests for the independent Lean 4 CI audit gate (no fake compilation)."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from scripts.lean_ci_audit import (
    audit, expected_theorems, inspect_log, main, registered_files,
)


class LeanAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()
        self.src = self.root / "src" / "Example.lean"
        self.src.write_text(
            "theorem pilotA : True := by trivial\n"
            "theorem pilotB : True := by trivial\n"
            "#print axioms pilotA\n#print axioms pilotB\n", encoding="utf-8")
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps({"items": [{
            "id": "pilot", "source_module": "LST-01",
            "source_label": "thm:example", "lean_file": "src/Example.lean",
            "lean_theorem": "pilotA", "statement_status": "needs_review"
        }]}), encoding="utf-8")
        self.logs = self.root / "logs"
        self.logs.mkdir()
        self.log = self.logs / "src_Example.lean.log"
        self.log.write_text(
            "src/Example.lean:4:0: info: 'pilotA' depends on axioms: [propext, Classical.choice]\n"
            "src/Example.lean:5:0: info: 'pilotB' does not depend on any axioms\n",
            encoding="utf-8")

    def test_success_is_always_non_semantic(self):
        result = audit(self.manifest, self.root, self.logs)
        self.assertEqual(result["files_checked"], 1)
        self.assertEqual(result["theorems_checked"], 2)
        self.assertFalse(result["certificate"])
        self.assertEqual(result["latex_semantics_status"], "not_certified")

    def test_rejects_sorry_axiom(self):
        with self.assertRaisesRegex(ValueError, "forbidden axioms"):
            inspect_log("'pilotA' depends on axioms: [propext, sorryAx]", ["pilotA"])

    def test_rejects_unrecognized_axiom(self):
        with self.assertRaisesRegex(ValueError, "forbidden axioms"):
            inspect_log("'pilotA' depends on axioms: [myNewAxiom]", ["pilotA"])

    def test_rejects_missing_axiom_output(self):
        with self.assertRaisesRegex(ValueError, "No actual"):
            inspect_log("'pilotA' depends on axioms: [propext]", ["pilotA", "pilotB"])

    def test_rejects_duplicate_axiom_output(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            inspect_log("'pilotA' does not depend on any axioms\n"
                        "'pilotA' depends on axioms: [propext]", ["pilotA"])

    def test_all_theorems_require_print_axioms(self):
        self.src.write_text("theorem pilotA : True := by trivial\n"
                            "theorem pilotB : True := by trivial\n"
                            "#print axioms pilotA\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "pilotB"):
            expected_theorems(self.src, ["pilotA"])

    def test_missing_manifest_theorem_fails(self):
        with self.assertRaisesRegex(ValueError, "missing from Lean source"):
            expected_theorems(self.src, ["unknown"])

    def test_disallow_directory_traversal(self):
        raw = json.loads(self.manifest.read_text(encoding="utf-8"))
        raw["items"][0]["lean_file"] = "src/../../etc/evil.lean"
        self.manifest.write_text(json.dumps(raw), encoding="utf-8")
        with self.assertRaises(ValueError):
            registered_files(self.manifest, self.root)

    def test_unregistered_auxiliary_lean_source_is_also_audited(self):
        auxiliary = self.root / "src" / "Extra.lean"
        auxiliary.write_text("theorem extra : True := by trivial\n"
                             "#print axioms extra\n", encoding="utf-8")
        entries = registered_files(self.manifest, self.root)
        self.assertIn("src/Extra.lean", entries)
        self.assertEqual(entries["src/Extra.lean"], [])
        with self.assertRaisesRegex(ValueError, "Missing or oversized"):
            audit(self.manifest, self.root, self.logs)
        (self.logs / "src_Extra.lean.log").write_text(
            "'extra' does not depend on any axioms\n", encoding="utf-8")
        result = audit(self.manifest, self.root, self.logs)
        self.assertEqual(result["files_checked"], 2)
        self.assertEqual(result["theorems_checked"], 3)
        self.assertFalse(result["certificate"])

    def test_registered_theorem_group_must_be_complete(self):
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        data["items"][0]["lean_theorems"] = ["pilotA", "missingGroupMember"]
        self.manifest.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Manifest theorem missing"):
            audit(self.manifest, self.root, self.logs)

    def test_rejects_approved_entry_without_source_digest(self):
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        data["items"][0]["statement_status"] = "approved"
        self.manifest.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "pinned source digest"):
            registered_files(self.manifest, self.root)

    def test_rejects_theorem_group_without_main_theorem(self):
        data = json.loads(self.manifest.read_text(encoding="utf-8"))
        data["items"][0]["lean_theorems"] = ["pilotB"]
        self.manifest.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Malformed theorem group"):
            registered_files(self.manifest, self.root)

    def test_cli_nonzero_for_missing_real_log(self):
        self.log.unlink()
        result = main(["--manifest", str(self.manifest), "--lean-root", str(self.root),
                       "--logs-dir", str(self.logs)])
        self.assertEqual(result, 1)

    def test_cli_lists_registered_source(self):
        result = main(["--manifest", str(self.manifest), "--lean-root", str(self.root),
                       "--list-files"])
        self.assertEqual(result, 0)



class LeanSourcePinTests(unittest.TestCase):
    def test_current_repo_approved_manifest_matches_canonical_tex(self):
        root = Path(__file__).resolve().parents[1] / "lean"
        registered = registered_files(root / "manifest.json", root)
        self.assertIn("src/LST01_SyntaxValuations.lean", registered)
        self.assertIn("lst01_syntax_modus_ponens",
                      registered["src/LST01_SyntaxValuations.lean"])

    def test_l13_lst02_candidates_match_real_labels(self):
        root = Path(__file__).resolve().parents[1] / "lean"
        repo = root.resolve().parents[1]
        registry = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        candidates = [item for item in registry["items"]
                      if item["source_module"] == "LST-02"]
        self.assertEqual(len(candidates), 4)
        self.assertEqual(len({item["source_label"] for item in candidates}), 4)
        canonical = "chapters/pl/logic_and_set_theory/02-kwantyfikatory-i-podstawowe-metody-dowodzenia.tex"
        source = (repo / canonical).read_text(encoding="utf-8")
        names = {
            "thm:negation-quantifiers",
            "thm:same-quantifier-order",
            "thm:swap-mixed",
            "thm:unique-expansion-xli",
        }
        self.assertEqual({item["source_label"] for item in candidates}, names)
        for item in candidates:
            self.assertEqual(item["statement_status"], "needs_review")
            self.assertNotIn("source_document_sha256", item)
            self.assertEqual(item["source_document_path"], canonical)
            self.assertEqual(source.count(r"\\label{" + item["source_label"] + "}"), 1)
            self.assertEqual(item["lean_file"], "src/LST02_Quantifiers.lean")
        registered = registered_files(root / "manifest.json", root)
        new_file = root / "src" / "LST02_Quantifiers.lean"
        parsed = expected_theorems(
            new_file, registered["src/LST02_Quantifiers.lean"])
        self.assertEqual(len(parsed), 7)
        self.assertIn("lst02_mixed_empty_counterexample", parsed)

    def test_digest_guard_rejects_modified_tex(self):
        import hashlib

        with tempfile.TemporaryDirectory() as temp:
            repository = Path(temp)
            lean_root = repository / "application" / "lean"
            (lean_root / "src").mkdir(parents=True)
            source = repository / "chapters" / "pl" / "unit" / "01.tex"
            source.parent.mkdir(parents=True)
            source.write_text("original source\\n", encoding="utf-8")
            (lean_root / "src" / "Example.lean").write_text(
                "theorem x : True := by trivial\\n#print axioms x\\n", encoding="utf-8")
            item = {"id": "x", "source_module": "X-01", "source_label": "thm:x",
                    "lean_file": "src/Example.lean", "lean_theorem": "x",
                    "lean_theorems": ["x"],
                    "statement_status": "approved",
                    "source_document_path": "chapters/pl/unit/01.tex",
                    "source_document_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
            manifest = lean_root / "manifest.json"
            manifest.write_text(json.dumps({"items": [item]}), encoding="utf-8")
            self.assertIn("src/Example.lean", registered_files(manifest, lean_root))
            source.write_text("changed source\\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "digest is outdated"):
                registered_files(manifest, lean_root)

    def test_rejects_path_traversal_for_approved_entries(self):
        import hashlib

        with tempfile.TemporaryDirectory() as temp:
            repository = Path(temp)
            lean_root = repository / "application" / "lean"
            (lean_root / "src").mkdir(parents=True)
            (lean_root / "src" / "Example.lean").write_text(
                "theorem x : True := by trivial\\n#print axioms x\\n", encoding="utf-8")
            item = {"id": "x", "source_module": "X-01", "source_label": "thm:x",
                    "lean_file": "src/Example.lean", "lean_theorem": "x",
                    "statement_status": "approved",
                    "source_document_path": "chapters/pl/../../../secret.tex",
                    "source_document_sha256": hashlib.sha256(b"test").hexdigest()}
            manifest = lean_root / "manifest.json"
            manifest.write_text(json.dumps({"items": [item]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Missing or untrusted"):
                registered_files(manifest, lean_root)

if __name__ == "__main__":
    unittest.main()
