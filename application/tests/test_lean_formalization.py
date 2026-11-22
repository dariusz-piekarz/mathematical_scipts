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
                         (LABEL, "LST-01/theorem/0001", SOURCE.index("\\label{")))
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

    def test_entity_metadata_corruption_blocks_reviewed_mapping(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        original = (0, len(SOURCE), 1, 3)
        broken = [
            (-1, len(SOURCE), 1, 3),
            (0, len(SOURCE) + 1, 1, 3),
            (len(SOURCE), len(SOURCE), 1, 3),
            (0, len(SOURCE), 2, 3),
            (0, len(SOURCE), 1, 2),
            (None, len(SOURCE), 1, 3),
        ]
        for offsets in broken:
            with self.subTest(offsets=offsets):
                self.con.execute(
                    "UPDATE entities SET start_offset=?,end_offset=?,"
                    "start_line=?,end_line=? WHERE id='LST-01/theorem/0001'",
                    offsets)
                self.con.commit()
                for selection in (
                    {"entity_id": "LST-01/theorem/0001"},
                    {"module_id": "LST-01", "start_line": 1, "end_line": 3},
                ):
                    with self.subTest(selection=selection):
                        # A valid document SHA must never excuse corrupt spans.
                        # No current/approved Lean mapping may be exposed.
                        with self.assertRaises(HTTPException) as caught:
                            lean.fragment(self.con, lean_root=self.root, **selection)
                        self.assertEqual(caught.exception.status_code, 409)
        self.con.execute(
            "UPDATE entities SET start_offset=?,end_offset=?,"
            "start_line=?,end_line=? WHERE id='LST-01/theorem/0001'",
            original)
        self.con.commit()
        result = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                               lean_root=self.root)
        self.assertEqual(result["formalization_status"], "ready")
        self.assertFalse(result["certificate"])

    def test_corrupt_adjacent_theorem_cannot_link_proof(self):
        proof = "\\begin{proof}\nDowód prawa de Morgana.\n\\end{proof}\n"
        source = SOURCE + proof
        digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
        self.con.execute("UPDATE documents SET content=?,sha256=? WHERE id='LST-01'",
                         (source, digest))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("LST-01/proof/0002", "LST-01", "proof", "Dowód",
                          4, 6, len(SOURCE), len(source)))
        self.con.execute(
            "UPDATE entities SET start_line=2 WHERE id='LST-01/theorem/0001'")
        self.con.commit()
        with self.assertRaises(HTTPException) as caught:
            lean.fragment(self.con, entity_id="LST-01/proof/0002",
                          lean_root=self.root)
        self.assertEqual(caught.exception.status_code, 409)

    def test_boolean_line_indices_are_not_valid_fragments(self):
        for a, b in ((True, 3), (1, True), (False, 3)):
            with self.subTest(first=a, last=b):
                with self.assertRaises(HTTPException) as caught:
                    lean.fragment(self.con, module_id="LST-01",
                                  start_line=a, end_line=b, lean_root=self.root)
                self.assertEqual(caught.exception.status_code, 400)

    def test_compiled_history_does_not_migrate_to_new_owner_with_same_tex_sha(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "real-process-interface", False)):
            initial = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(initial["proof_status"], "compiled")
        self.assertTrue(initial["run_record_saved"])
        original = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(original["proof_status"], "compiled")

        # The document and its hash do not change; only the label owner does.
        self.con.execute(
            "INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
            ("LST-01/theorem/0002", "LST-01", "theorem", "Other owner",
             1, 3, 0, len(SOURCE)))
        self.con.execute(
            "UPDATE labels SET entity_id=? WHERE name=?",
            ("LST-01/theorem/0002", LABEL))
        self.con.commit()
        moved = lean.fragment(self.con, entity_id="LST-01/theorem/0002",
                              lean_root=self.root)
        self.assertEqual(moved["formalization_id"], "sample")
        self.assertEqual(moved["source_document_sha256"], self.digest)
        self.assertEqual(moved["formalization_status"], "ready")
        self.assertEqual(moved["proof_status"], "not_run")
        self.assertTrue(moved["previous_run_outdated"])
        self.assertFalse(moved["certificate"])

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "new-process", False)):
            rerun = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(rerun["proof_status"], "compiled")
        refreshed = lean.fragment(self.con, entity_id="LST-01/theorem/0002",
                                  lean_root=self.root)
        self.assertEqual(refreshed["proof_status"], "compiled")
        self.assertIn("new-process", refreshed["last_run_log"])
        self.assertFalse(refreshed["certificate"])

    def test_wrong_label_offset_is_blocked_consistently_across_api_paths(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        self.con.execute("UPDATE labels SET offset=offset+1 WHERE name=?", (LABEL,))
        self.con.commit()
        from backend import lean_catalog
        catalog = lean_catalog.list_formalizations(self.con, lean_root=self.root)
        self.assertEqual(catalog["items"][0]["index_status"], "invalid_label_binding")
        self.assertEqual(catalog["items"][0]["formalization_status"], "stale")
        self.assertIsNone(catalog["items"][0]["source_entity_id"])
        with self.assertRaises(HTTPException) as caught:
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(caught.exception.status_code, 409)
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            response = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(response["proof_status"], "blocked")
        self.assertFalse(response["certificate"])
        spawn.assert_not_called()

    def test_cross_document_label_conflict_blocks_catalog_preview_and_runner(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        self.con.executescript("""
            CREATE TABLE label_conflicts(
                name TEXT, document_id TEXT, entity_id TEXT,
                offset INTEGER, line INTEGER, excerpt TEXT,
                PRIMARY KEY(name, document_id));
        """)
        # A duplicate in a different chapter invalidates even the first
        # globally indexed owner. Its source bytes/SHA remain unchanged.
        self.con.execute("INSERT INTO label_conflicts VALUES(?,?,?,?,?,?)",
                         (LABEL, "LST-99", "external-theorem", 0, 1, ""))
        self.con.commit()
        from backend import lean_catalog
        entry = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(entry["index_status"], "ambiguous_label")
        self.assertEqual(entry["formalization_status"], "stale")
        self.assertIsNone(entry["source_entity_id"])
        with self.assertRaises(HTTPException) as exc:
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(exc.exception.status_code, 409)
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_non_theorem_owner_is_rejected_across_catalog_preview_and_runner(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        self.con.execute(
            "UPDATE entities SET kind='section' WHERE id=?", ("LST-01/theorem/0001",))
        self.con.commit()
        from backend import lean_catalog
        record = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(record["index_status"], "invalid_label_binding")
        self.assertEqual(record["formalization_status"], "stale")
        with self.assertRaises(HTTPException) as caught:
            lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                          lean_root=self.root)
        self.assertEqual(caught.exception.status_code, 409)
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_indexed_label_changed_during_execution_blocks_persistence(self):
        self.entry["source_document_sha256"] = self.digest
        self.entry["statement_status"] = "approved"
        self.save_manifest()
        def change_label(*args, **kwargs):
            self.con.execute("UPDATE labels SET offset=offset+1 WHERE name=?", (LABEL,))
            self.con.commit()
            return (0, "Lean process succeeded", False)
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=change_label) as spawn:
            response = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(spawn.call_count, 1)
        self.assertEqual(response["proof_status"], "blocked")
        self.assertFalse(response["run_record_saved"])
        self.assertFalse(response["certificate"])

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

    def test_total_memory_limit_invalid_config_blocks_runner(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "invalid"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(state["ready"])
        self.assertIsNotNone(state["total_memory_limit_error"])
        spawn.assert_not_called()

    def test_total_memory_without_delegation_never_spawns(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "1024"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_cgroup.available",
                   return_value=False), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(state["ready"])
        self.assertFalse(state["total_memory_limit_supported"])
        spawn.assert_not_called()

    def test_total_memory_allocation_error_refuses_run(self):
        from backend import lean_cgroup
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "1024"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_cgroup.available",
                   return_value=True), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=lean_cgroup.CgroupUnavailable("permission denied")):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertIn("permission denied", result["detail"])

    def test_total_memory_cap_is_forwarded_without_certificate(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "1024"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_cgroup.available",
                   return_value=True), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "ok", False)) as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
            state = lean.availability(lean_root=self.root)
        self.assertEqual(result["proof_status"], "compiled")
        self.assertFalse(result["certificate"])
        self.assertEqual(state["total_memory_limit_mb"], 1024)
        self.assertTrue(state["total_memory_limit_supported"])
        self.assertEqual(spawn.call_args.kwargs["total_memory_mb"], 1024)

    def test_windows_job_available_routes_aggregate_limit_without_certificate(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "2048"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_cgroup.available",
                   return_value=False), \
             patch("backend.lean_formalization.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "ok", False)) as execute:
            state = lean.availability(lean_root=self.root)
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertTrue(state["total_memory_limit_supported"])
        self.assertEqual(state["total_memory_limit_mb"], 2048)
        self.assertEqual(execute.call_args.kwargs["total_memory_mb"], 2048)
        self.assertEqual(result["proof_status"], "compiled")
        self.assertFalse(result["certificate"])

    def test_windows_job_creation_failure_is_blocked(self):
        from backend import lean_windows_job
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1",
                                     "MATLIB_LEAN_TOTAL_MEMORY_MB": "2048"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_windows_job.available",
                   return_value=True), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=lean_windows_job.JobUnavailable(
                       "AssignProcessToJobObject refused")):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("AssignProcessToJobObject", result["detail"])
        self.assertFalse(result["certificate"])

    def test_busy_runner_does_not_spawn_or_replace_previous_success(self):
        from backend import lean_run_lock
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "first run", False)) as spawn:
            first = lean.run(self.con, "sample", lean_root=self.root)
            self.assertEqual(first["proof_status"], "compiled")
            self.assertEqual(spawn.call_count, 1)
            with lean_run_lock.exclusive(self.root):
                second = lean.run(self.con, "sample", lean_root=self.root)
            self.assertEqual(spawn.call_count, 1)
        self.assertEqual(second["proof_status"], "blocked")
        self.assertFalse(second["certificate"])
        self.assertIn("Inny proces", second["detail"])
        cached = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                               lean_root=self.root)
        self.assertEqual(cached["proof_status"], "compiled")
        self.assertIn("first run", cached["last_run_log"])
        self.assertFalse(cached["certificate"])

    def test_unverifiable_external_package_blocks_before_start(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_environment.external_packages_sha256",
                   side_effect=ValueError("modified Mathlib")), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertIn("modified Mathlib", result["detail"])
        spawn.assert_not_called()

    def test_index_change_during_lock_acquisition_blocks_before_spawn(self):
        from contextlib import contextmanager

        @contextmanager
        def mutate_while_waiting(root):
            self.con.execute("UPDATE labels SET offset=offset+1 WHERE name=?", (LABEL,))
            self.con.commit()
            yield

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_run_lock.exclusive",
                   side_effect=mutate_while_waiting), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("Powiązanie", result["detail"])
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_index_document_change_during_lock_acquisition_blocks_spawn(self):
        from contextlib import contextmanager

        @contextmanager
        def mutate_while_waiting(root):
            revised = SOURCE + "% reindexed while another runner holds the lock\\n"
            self.con.execute(
                "UPDATE documents SET content=?, sha256=? WHERE id='LST-01'",
                (revised, hashlib.sha256(revised.encode("utf-8")).hexdigest()))
            self.con.commit()
            yield

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_run_lock.exclusive",
                   side_effect=mutate_while_waiting), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("Indeks rozdziału", result["detail"])
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_external_dependency_change_during_lock_acquisition_blocks_spawn(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_environment.external_packages_sha256",
                   side_effect=["a" * 64, "b" * 64]), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("Pliki Lean", result["detail"])
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_registered_lean_file_change_during_lock_acquisition_blocks_spawn(self):
        from contextlib import contextmanager
        file = self.root / "src" / "Example.lean"

        @contextmanager
        def mutate_while_waiting(root):
            file.write_text("theorem sample (p : Prop) : p → p := by exact id\\n",
                            encoding="utf-8")
            yield

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_run_lock.exclusive",
                   side_effect=mutate_while_waiting), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("Pliki Lean", result["detail"])
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_manifest_change_during_lock_acquisition_blocks_spawn(self):
        from contextlib import contextmanager

        @contextmanager
        def mutate_while_waiting(root):
            manifest = self.root / "manifest.json"
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            payload["items"][0]["statement_status"] = "approved"
            manifest.write_text(json.dumps(payload), encoding="utf-8")
            yield

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_run_lock.exclusive",
                   side_effect=mutate_while_waiting), \
             patch("backend.lean_formalization.lean_process.execute_registered") as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertIn("Pliki Lean", result["detail"])
        self.assertFalse(result["certificate"])
        spawn.assert_not_called()

    def test_external_checkout_change_during_compile_blocks_success(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_environment.external_packages_sha256",
                   side_effect=["a" * 64, "a" * 64, "b" * 64]), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "successful exit", False)) as spawn:
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(spawn.call_count, 1)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["run_record_saved"])
        self.assertFalse(result["certificate"])
        cached = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                               lean_root=self.root)
        self.assertEqual(cached["proof_status"], "not_run")

    def test_checkout_becomes_unverifiable_after_compile(self):
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which",
                   return_value="/fake/lake"), \
             patch("backend.lean_environment.external_packages_sha256",
                   side_effect=["a" * 64, "a" * 64, ValueError("checkout dirty")]), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "successful exit", False)):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(result["run_record_saved"])
        self.assertIn("checkout dirty", result["run_record_warning"])

    def test_olean_artifact_modified_during_execution_revokes_compiled(self):
        build = self.root / ".lake" / "build" / "lib" / "lean"
        build.mkdir(parents=True)
        artifact = build / "Dependency.olean"
        artifact.write_bytes(b"original compiled module")

        def mutate_artifact(*args, **kwargs):
            artifact.write_bytes(b"updated compiled module")
            return (0, "success", False)

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=mutate_artifact):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        self.assertFalse(result["run_record_saved"])
        reopened = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(reopened["proof_status"], "not_run")
        self.assertFalse(reopened["run_cached"])

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

    def test_editing_other_local_module_revokes_saved_compilation(self):
        sibling = self.root / "src" / "ImportedHelper.lean"
        sibling.write_text("def helper : Nat := 1\n", encoding="utf-8")
        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   return_value=(0, "compiled", False)):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "compiled")
        cached = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                               lean_root=self.root)
        self.assertTrue(cached["run_cached"])
        sibling.write_text("def helper : Nat := 2\n", encoding="utf-8")
        outdated = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(outdated["proof_status"], "not_run")
        self.assertTrue(outdated["previous_run_outdated"])
        self.assertFalse(outdated["certificate"])

    def test_editing_other_module_during_execution_blocks_result_persistence(self):
        sibling = self.root / "src" / "ImportedHelper.lean"
        sibling.write_text("def helper : Nat := 1\n", encoding="utf-8")

        def edit_during_run(*args, **kwargs):
            sibling.write_text("def helper : Nat := 2\n", encoding="utf-8")
            return (0, "stale compilation", False)

        with patch.dict(os.environ, {"MATLIB_LEAN_RUN": "1"}), \
             patch("backend.lean_formalization.shutil.which", return_value="/fake/lake"), \
             patch("backend.lean_formalization.lean_process.execute_registered",
                   side_effect=edit_during_run):
            result = lean.run(self.con, "sample", lean_root=self.root)
        self.assertEqual(result["proof_status"], "blocked")
        self.assertFalse(result["certificate"])
        reopened = lean.fragment(self.con, entity_id="LST-01/theorem/0001",
                                 lean_root=self.root)
        self.assertEqual(reopened["proof_status"], "not_run")
        self.assertFalse(reopened["run_cached"])

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
        self.assertIn('"/api/lean/catalog"', js)
        self.assertIn('"/api/lean/dependencies?"', js)
        self.assertIn('"/api/lean/dependencies/inspect"', js)
        self.assertIn("renderLeanInspection(result)", js)
        for key in ("leanInspect", "leanInspection"):
            self.assertIn('id="' + key + '"', page)
        self.assertIn("loadLeanDependencies(result,epoch);", js)
        for key in ("leanDependencies", "leanDependencyGraph", "leanDependencyStatus",
                    "leanDependencyLimitations"):
            self.assertIn('id="' + key + '"', page)
        for key in ("leanCatalogSearch", "leanCatalogFilter", "leanCatalogList",
                    "leanCatalogRefresh"):
            self.assertIn('id="' + key + '"', page)

        self.assertIn('textContent=result.lean_code', js)


if __name__ == "__main__":
    unittest.main()
