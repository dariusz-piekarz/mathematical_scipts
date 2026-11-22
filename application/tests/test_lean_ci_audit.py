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

    def test_cli_nonzero_for_missing_real_log(self):
        self.log.unlink()
        result = main(["--manifest", str(self.manifest), "--lean-root", str(self.root),
                       "--logs-dir", str(self.logs)])
        self.assertEqual(result, 1)

    def test_cli_lists_registered_source(self):
        result = main(["--manifest", str(self.manifest), "--lean-root", str(self.root),
                       "--list-files"])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
