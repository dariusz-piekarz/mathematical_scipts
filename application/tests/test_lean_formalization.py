"""Regression tests of Lean selection, provenance, and trusted local execution."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
import subprocess

from fastapi import HTTPException
from backend import lean_formalization as lean


SOURCE = "\\begin{twierdzenie}\\label{thm:de-morgan-logic}\n"
SOURCE += "Dla dowolnych formuł p,q.\n\\end{twierdzenie}\n"
LABEL = "thm:de-morgan-logic"


class LeanFormalizationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "application" / "lean"
        (self.root / "src").mkdir(parents=True)
        (self.root / "src" / "Example.lean").write_text(
            "theorem sample (p : Prop) : p → p := by intro h; exact h\n", encoding="utf-8")
        (self.root / "lakefile.toml").write_text('name = "Test"\n', encoding="utf-8")
        (self.root / "lean-toolchain").write_text("leanprover/lean4:v4.26.0\n", encoding="utf-8")
        self.entry = {
            "id": "sample", "source_module": "LST-01", "source_label": LABEL,
            "lean_file": "src/Example.lean", "lean_theorem": "sample",
            "statement_status": "needs_review",
        }
        self.save_manifest()
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.addCleanup(self.con.close)
        self.con.executescript("""
            CREATE TABLE documents(id TEXT, title TEXT, sha256 TEXT, content TEXT);
            CREATE TABLE entities(id TEXT, document_id TEXT, kind TEXT, title TEXT,
              start_line INTEGER, end_line INTEGER, start_offset INTEGER, end_offset INTEGER);
            CREATE TABLE labels(name TEXT, entity_id TEXT, offset INTEGER);
        """)
        digest = hashlib.sha256(SOURCE.encode("utf-8")).hexdigest()
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)",
                         ("LST-01", "Logika", digest, SOURCE))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("LST-01/theorem/0001", "LST-01", "theorem", "De Morgan",
                          1, 3, 0, len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)",
                         (LABEL, "LST-01/theorem/0001", 18))
        self.con.commit()
        self.digest = digest

    def save_manifest(self):
        (self.root / "manifest.json").write_text(
            json.dumps({"schema_version": 1, "items": [self.entry]}), encoding="utf-8")

    def test_selected_theorem_has_code_but_no_false_certificate(self):
        result = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                               lean_root=self.root)
        self.assertEqual(result["formalization_status"], "draft")
        self.assertEqual(result["statement_status"], "needs_review")
        self.assertEqual(result["proof_status"], "not_run")
        self.assertIs(result["certificate"], False)
        self.assertIn("theorem sample", result["lean_code"])
        self.assertEqual(result["source_latex"], SOURCE)

    def test_complete_source_lines_match_and_partial_lines_do_not(self):
        a = lean.fragment(self.con, module_id="LST-01", start_line=1,
                          end_line=3, lean_root=self.root)
        self.assertEqual(a["formalization_id"], "sample")
        b = lean.fragment(self.con, module_id="LST-01", start_line=1,
                          end_line=1, lean_root=self.root)
        self.assertEqual(b["formalization_status"], "missing")
        self.assertIsNone(b["lean_code"])

    def test_adjacent_proof_can_open_its_theorem_formalization(self):
        proof = "\\begin{proof}\nDowód prawa de Morgana.\n\\end{proof}\n"
        updated_source = SOURCE + proof
        updated_sha = hashlib.sha256(updated_source.encode("utf-8")).hexdigest()
        self.con.execute("UPDATE documents SET content=?,sha256=? WHERE id='LST-01'",
                         (updated_source, updated_sha))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("LST-01/proof/0002", "LST-01", "proof", "Dowód",
                          4, 6, len(SOURCE), len(SOURCE) + len(proof)))
        self.con.commit()
        result = lean.fragment(self.con, entity_id="LST-01/proof/0002",
                               lean_root=self.root)
        self.assertEqual(result["source_linkage"], "proof_of_adjacent_theorem")
        self.assertEqual(result["formalization_id"], "sample")
        self.assertEqual(result["statement_status"], "needs_review")
        self.assertFalse(result["certificate"])

    def test_pinned_source_and_stale_source(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.entry["lean_theorems"] = ["sample"]
        self.save_manifest()
        a = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(a["formalization_status"], "ready")
        self.assertEqual(a["statement_status"], "approved")
        self.assertEqual(a["lean_theorems"], ["sample"])
        # A real change keeps the index internally consistent but invalidates
        # the version pinned in the reviewed manifest.
        revised_source = SOURCE + "% later editorial change\\n"
        revised_sha = hashlib.sha256(revised_source.encode("utf-8")).hexdigest()
        self.con.execute("UPDATE documents SET content=?,sha256=? WHERE id='LST-01'",
                         (revised_source, revised_sha))
        self.con.commit()
        b = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(b["formalization_status"], "stale")
        self.assertEqual(b["statement_status"], "needs_review")
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")

    def test_changed_canonical_tex_revokes_approval_without_reindex(self):
        file = Path(self.tmp.name) / "chapters" / "pl" / "unit" / "01.tex"
        file.parent.mkdir(parents=True)
        file.write_text(SOURCE, encoding="utf-8")
        self.entry["source_document_path"] = "chapters/pl/unit/01.tex"
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        current = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                lean_root=self.root)
        self.assertEqual(current["formalization_status"], "ready")
        self.assertEqual(current["statement_status"], "approved")
        file.write_text(SOURCE + "% source revised\n", encoding="utf-8")
        stale = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                              lean_root=self.root)
        self.assertEqual(stale["formalization_status"], "stale")
        self.assertEqual(stale["statement_status"], "needs_review")
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            blocked = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(blocked["proof_status"], "blocked")
        spawn.assert_not_called()

    def test_corrupted_index_is_refused_by_reader(self):
        self.con.execute("UPDATE documents SET sha256=? WHERE id='LST-01'",
                         ("f" * 64,))
        self.con.commit()
        with self.assertRaises(HTTPException) as caught:
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(caught.exception.status_code, 409)

    def test_nontext_source_is_rejected_for_entity_and_line_selection(self):
        self.con.execute("UPDATE documents SET content=NULL WHERE id='LST-01'")
        self.con.commit()
        for kwargs in ({"entity_id": "LST-01/theorem/0001"},
                       {"module_id": "LST-01", "start_line": 1, "end_line": 1}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(HTTPException) as caught:
                    lean.fragment(self.con, lean_root=self.root, **kwargs)
                self.assertEqual(caught.exception.status_code, 409)

    def test_runner_blocks_inconsistent_index_before_subprocess(self):
        # Simulate a stale SQLite SHA while the source bytes remain unchanged.
        self.con.execute("UPDATE documents SET sha256=? WHERE id='LST-01'",
                         ("0" * 64,))
        self.con.commit()
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertIn("SHA256", result["detail"])
        spawn.assert_not_called()

    def test_runner_rejects_nontext_index_content(self):
        self.con.execute("UPDATE documents SET content=NULL WHERE id='LST-01'")
        self.con.commit()
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_rejects_arbitrary_path(self):
        self.entry["lean_file"] = "../../backend/api.py"
        self.save_manifest()
        with self.assertRaises(HTTPException):
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)

    def test_missing_or_invalid_selection(self):
        with self.assertRaises(HTTPException):
            lean.fragment(self.con, entity_id="not-an-entity", lean_root=self.root)
        with self.assertRaises(HTTPException):
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          module_id="LST-01", lean_root=self.root)
        with self.assertRaises(HTTPException):
            lean.fragment(self.con, module_id="LST-01", start_line=1,
                          end_line=1000, lean_root=self.root)

    def test_local_execution_requires_explicit_opt_in(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "0"}):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])

    def test_lake_absent_is_reported(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value=None):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "toolchain_unavailable")

    def test_invalid_memory_limit_blocks_before_toolchain_process(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_MEMORY_MB": "invalid"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(state["ready"])
        self.assertIsNotNone(state["memory_limit_error"])
        spawn.assert_not_called()

    def test_unsupported_memory_limit_blocks_instead_of_running_unbounded(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_MEMORY_MB": "4096"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.memory_limit_supported",
                   return_value=False), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(state["ready"])
        self.assertFalse(state["memory_limit_enforced"])
        spawn.assert_not_called()

    def test_configured_memory_limit_is_forwarded_to_executor(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_MEMORY_MB": "4096"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.memory_limit_supported",
                   return_value=True), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "ok", False)) as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "compiled")
        self.assertFalse(result["certificate"])
        self.assertTrue(state["memory_limit_enforced"])
        self.assertEqual(state["memory_limit_mb"], 4096)
        self.assertEqual(spawn.call_args.kwargs["memory_limit_mb"], 4096)

    def test_compilation_success_is_not_semantic_certificate(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "ok", False)):
            output = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(output["proof_status"], "compiled")
        self.assertFalse(output["certificate"])
        self.assertTrue(output["run_record_saved"])
        # The same indexed theorem must show the last real execution after reopening.
        reopened = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(reopened["proof_status"], "compiled")
        self.assertTrue(reopened["run_cached"])
        self.assertFalse(reopened["certificate"])
        self.assertIn("ok", reopened["last_run_log"])

    def test_provenance_change_unsets_saved_success(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "accepted", False)):
            lean.run(self.con, "sample", lean_root=self.root)
        self.assertTrue(lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                      lean_root=self.root)["run_cached"])
        lean_source = self.root / "src" / "Example.lean"
        lean_source.write_text("theorem sample (p : Prop) : p → p := by exact id\n",
                               encoding="utf-8")
        invalidated = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                    lean_root=self.root)
        self.assertEqual(invalidated["proof_status"], "not_run")
        self.assertTrue(invalidated["previous_run_outdated"])
        self.assertFalse(invalidated["certificate"])

    def test_runner_persists_bounded_failure_log_without_certificate(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(1, "X" * 15980 + "diagnostic at end", False)):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "failed")
        self.assertFalse(result["certificate"])
        self.assertLessEqual(len(result["log"]), 16000)
        self.assertIn("diagnostic at end", result["log"])
        reopened = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(reopened["proof_status"], "failed")
        self.assertFalse(reopened["certificate"])

    def test_incomplete_descendant_cleanup_never_reports_compiled(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=RuntimeError("Lean stdout pipe was left open by a child process.")):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "failed")
        self.assertFalse(result["certificate"])
        self.assertIn("Niekompletny", result["detail"])

    def test_timeout_reported(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(None, "", True)):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "timeout")


class LeanFrontEndContractTests(unittest.TestCase):
    def test_reader_and_status_controls_present(self):
        frontend = Path(__file__).resolve().parents[1] / "frontend"
        page = (frontend / "index.html").read_text(encoding="utf-8")
        js = (frontend / "app.js").read_text(encoding="utf-8")
        for key in ("view-lean", "leanCode", "leanLatex", "leanStatuses", "leanRun",
                    "openLeanCurrent", "openLeanSelection"):
            self.assertIn('id="' + key + '"', page)
        self.assertIn('"/api/lean/fragment?"', js)
        self.assertIn('"/api/lean/run"', js)
        self.assertIn('textContent=result.lean_code', js)


if __name__ == "__main__":
    unittest.main()
