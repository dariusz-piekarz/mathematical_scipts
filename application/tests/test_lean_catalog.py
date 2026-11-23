"""Read-only Lean catalog: integrity, navigation and fail-closed statuses."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from fastapi import HTTPException
from backend import lean_catalog
from backend import lean_chapter_report


SOURCE = "\\begin{twierdzenie}\\label{t:x}\nPrawa logiczne.\n\\end{twierdzenie}\n"


class LeanCatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "application" / "lean"
        (self.root / "src").mkdir(parents=True)
        (self.root / "src" / "T.lean").write_text(
            "theorem t (p : Prop) : p → p := by intro h; exact h\n",
            encoding="utf-8")
        self.digest = hashlib.sha256(SOURCE.encode("utf-8")).hexdigest()
        self.item = {
            "id": "t", "source_module": "LST-01", "source_label": "t:x",
            "lean_file": "src/T.lean", "lean_theorem": "t",
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
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)",
                         ("LST-01", "Test", self.digest, SOURCE))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("theorem-one", "LST-01", "theorem", "Test", 1, 3, 0, len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", ("t:x", "theorem-one", SOURCE.index("\\label{")))
        self.con.commit()

    def save_manifest(self):
        (self.root / "manifest.json").write_text(
            json.dumps({"schema_version": 1, "items": [self.item]}),
            encoding="utf-8")

    def test_draft_is_navigable_but_does_not_claim_proof(self):
        result = lean_catalog.list_formalizations(self.con, lean_root=self.root)
        self.assertEqual((result["total"], result["draft"], result["ready"]), (1, 1, 0))
        self.assertFalse(result["proof_status_included"])
        entry = result["items"][0]
        self.assertEqual(entry["source_entity_id"], "theorem-one")
        self.assertEqual(entry["index_status"], "ok")
        self.assertEqual(entry["statement_status"], "needs_review")
        self.assertNotIn("proof_status", entry)
        self.assertFalse(entry["certificate"])

    def test_pinned_mapping_becomes_stale_on_source_change(self):
        self.item.update(source_document_sha256=self.digest,
                         statement_status="approved")
        self.save_manifest()
        ready = lean_catalog.list_formalizations(self.con, lean_root=self.root)
        self.assertEqual(ready["items"][0]["formalization_status"], "ready")
        self.assertEqual(ready["items"][0]["statement_status"], "approved")
        changed = SOURCE + "% edited\n"
        self.con.execute("UPDATE documents SET content=?,sha256=?",
                         (changed, hashlib.sha256(changed.encode()).hexdigest()))
        self.con.commit()
        stale = lean_catalog.list_formalizations(self.con, lean_root=self.root)
        self.assertEqual(stale["stale"], 1)
        self.assertEqual(stale["items"][0]["statement_status"], "needs_review")

    def test_real_tex_change_without_reindex_invalidates_pinned_status(self):
        tex = Path(self.temp.name) / "chapters" / "pl" / "math" / "01.tex"
        tex.parent.mkdir(parents=True)
        tex.write_text(SOURCE, encoding="utf-8")
        self.item.update(source_document_sha256=self.digest,
                         source_document_path="chapters/pl/math/01.tex",
                         statement_status="approved")
        self.save_manifest()
        self.assertEqual(
            lean_catalog.list_formalizations(self.con, lean_root=self.root)["ready"], 1)
        tex.write_text(SOURCE + "% edit\n", encoding="utf-8")
        self.assertEqual(
            lean_catalog.list_formalizations(self.con, lean_root=self.root)["stale"], 1)

    def test_corrupt_and_ambiguous_index_never_show_current_mapping(self):
        self.con.execute("UPDATE documents SET sha256=?", ("0" * 64,))
        self.con.commit()
        broken = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(broken["index_status"], "corrupt_document")
        self.assertIsNone(broken["source_entity_id"])
        self.assertEqual(broken["formalization_status"], "stale")
        self.con.execute("UPDATE documents SET sha256=?", (self.digest,))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("theorem-two", "LST-01", "theorem", "Other", 1, 3, 0, len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", ("t:x", "theorem-two", 2))
        self.con.commit()
        ambiguous = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(ambiguous["index_status"], "ambiguous_label")
        self.assertIsNone(ambiguous["source_entity_id"])
        self.assertEqual(ambiguous["formalization_status"], "stale")

    def test_missing_label_and_document_are_stale(self):
        self.con.execute("DELETE FROM labels")
        self.con.commit()
        unlinked = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(unlinked["index_status"], "unlinked_label")
        self.con.execute("DELETE FROM documents")
        self.con.commit()
        missing = lean_catalog.list_formalizations(self.con, lean_root=self.root)["items"][0]
        self.assertEqual(missing["index_status"], "missing_document")
        self.assertEqual(missing["formalization_status"], "stale")

    def test_entry_limit_is_bounded(self):
        with patch.object(lean_catalog, "MAX_ENTRIES", 0):
            with self.assertRaises(HTTPException) as err:
                lean_catalog.list_formalizations(self.con, lean_root=self.root)
        self.assertEqual(err.exception.status_code, 503)


    def test_l14_chapter_report_ready_is_not_compilation(self):
        self.item.update(source_document_sha256=self.digest,
                         statement_status="approved")
        self.save_manifest()
        data = lean_chapter_report.chapter_report(self.con, "LST-01", lean_root=self.root)
        self.assertEqual(data["report_schema_version"], 1)
        self.assertEqual((data["total"], data["ready"], data["draft"],
                          data["stale"], data["statement_approved"]), (1, 1, 0, 0, 1))
        self.assertEqual(data["source_document_sha256"], self.digest)
        self.assertEqual(data["scope"], "manifest_and_index_only")
        self.assertFalse(data["run_history_checked"])
        self.assertFalse(data["dependency_fingerprint_checked"])
        self.assertFalse(data["proof_status_included"])
        self.assertFalse(data["certificate"])
        self.assertNotIn("proof_status", data["items"][0])

    def test_l14_chapter_report_fails_closed_on_corrupt_index(self):
        self.item.update(source_document_sha256=self.digest,
                         statement_status="approved")
        self.save_manifest()
        self.con.execute("UPDATE documents SET sha256=?", ("0" * 64,))
        self.con.commit()
        data = lean_chapter_report.chapter_report(self.con, "LST-01", lean_root=self.root)
        self.assertEqual(data["source_index_status"], "corrupt_document")
        self.assertIsNone(data["source_document_sha256"])
        self.assertEqual((data["ready"], data["stale"], data["statement_approved"]),
                         (0, 1, 0))
        self.assertEqual(data["items"][0]["statement_status"], "needs_review")
        self.assertFalse(data["certificate"])

    def test_l14_chapter_report_never_runs_fingerprint_or_history(self):
        from backend import lean_results
        with patch.object(lean_results, "fingerprint",
                          side_effect=AssertionError("Not a report dependency")), \
             patch.object(lean_results, "last_run",
                          side_effect=AssertionError("Not a report dependency")):
            data = lean_chapter_report.chapter_report(self.con, "LST-01",
                                                      lean_root=self.root)
        self.assertEqual(data["draft"], 1)
        self.assertFalse(data["run_history_checked"])

    def test_l14_chapter_report_rejects_unknown_and_unsafe_module(self):
        with self.assertRaises(HTTPException) as missing:
            lean_chapter_report.chapter_report(self.con, "LA-09",
                                               lean_root=self.root)
        self.assertEqual(missing.exception.status_code, 404)
        with self.assertRaises(HTTPException) as malformed:
            lean_chapter_report.chapter_report(self.con, "../LST-01",
                                               lean_root=self.root)
        self.assertEqual(malformed.exception.status_code, 400)

    def test_l14_chapter_report_empty_registered_module(self):
        source = "No registered Lean mapping."
        digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)",
                         ("LST-02", "Second", digest, source))
        self.con.commit()
        data = lean_chapter_report.chapter_report(self.con, "LST-02",
                                                  lean_root=self.root)
        self.assertEqual((data["total"], data["ready"], data["draft"], data["stale"]),
                         (0, 0, 0, 0))
        self.assertEqual(data["source_index_status"], "ok")
        self.assertFalse(data["certificate"])


    def test_l14_chapter_report_does_not_leak_future_cached_fields(self):
        current = lean_catalog.list_formalizations(self.con, lean_root=self.root)
        malicious = dict(current["items"][0], proof_status="compiled",
                         last_run_log="untrusted", certificate=True)
        with patch.object(lean_chapter_report.lean_catalog, "list_formalizations",
                          return_value={"items": [malicious]}):
            data = lean_chapter_report.chapter_report(self.con, "LST-01",
                                                      lean_root=self.root)
        self.assertEqual(data["total"], 1)
        self.assertNotIn("proof_status", data["items"][0])
        self.assertNotIn("last_run_log", data["items"][0])
        self.assertFalse(data["items"][0]["certificate"])
        self.assertFalse(data["proof_status_included"])


if __name__ == "__main__":
    unittest.main()
