"""Offline preparation must not execute Lean, generate code or alter the index."""
from __future__ import annotations

import hashlib
import sqlite3
import unittest
from contextlib import contextmanager
from unittest.mock import patch

from fastapi.testclient import TestClient
from backend.api import app
from backend import lean_transcription

SOURCE = "\\begin{twierdzenie}\\label{thm:pilot}\nDla każdego p, p implikuje p.\n\\end{twierdzenie}\n"
EID = "LST-01/theorem/0001"
SHA = hashlib.sha256(SOURCE.encode()).hexdigest()


class LeanTranscriptionTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:", check_same_thread=False)
        self.con.row_factory = sqlite3.Row
        self.addCleanup(self.con.close)
        self.con.executescript("""
          CREATE TABLE documents(id TEXT, title TEXT, sha256 TEXT, content TEXT);
          CREATE TABLE entities(id TEXT, document_id TEXT, kind TEXT, title TEXT,
            start_line INTEGER, end_line INTEGER, start_offset INTEGER, end_offset INTEGER);
          CREATE TABLE labels(name TEXT, entity_id TEXT, offset INTEGER);
          CREATE TABLE label_conflicts(name TEXT);
        """)
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)", ("LST-01","Logika",SHA,SOURCE))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         (EID,"LST-01","theorem","Pilot",1,3,0,len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", ("thm:pilot",EID,SOURCE.index("\\label{")))
        self.con.commit()
        @contextmanager
        def connection():
            try:
                yield self.con
            finally:
                self.con.rollback()
        self.patcher = patch("backend.api.db_connection", connection)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.client = TestClient(app)
        self.addCleanup(self.client.close)

    def post(self, **kwargs):
        body = {"entity_id": EID, "expected_source_sha256": SHA, "consent": True}
        body.update(kwargs)
        return self.client.post("/api/lean/transcription/prepare", json=body)

    def test_prepare_is_deterministic_read_only_and_nonexecuting(self):
        before = self.con.total_changes
        with patch("backend.lean_formalization.run", side_effect=AssertionError("runner called")):
            a, b = self.post(), self.post()
        self.assertEqual(a.status_code, 200, a.text)
        self.assertEqual(a.json(), b.json())
        data = a.json()
        self.assertEqual(data["source_latex"], SOURCE)
        self.assertEqual(data["source_sha256"], SHA)
        self.assertEqual(data["source_document_sha256"], SHA)
        self.assertEqual(data["source_bytes"], len(SOURCE.encode()))
        self.assertEqual(data["source_label"], "thm:pilot")
        self.assertEqual(data["candidate_status"], "not_generated")
        self.assertEqual(data["source_scope"], "indexed_snapshot_only")
        self.assertEqual(data["proof_status"], "not_run")
        self.assertEqual(data["statement_status"], "unreviewed")
        self.assertIsNone(data["lean_code"])
        self.assertIsNone(data["external_provider"])
        self.assertEqual(data["license_status"], "unreviewed")
        self.assertEqual(data["external_cost_minor_units"], 0)
        for field in ("certificate", "external_transfer_allowed", "registry_written", "canonical_source_written"):
            self.assertIs(data[field], False)
        self.assertEqual(self.con.total_changes, before)

    def test_consent_must_be_explicit_boolean(self):
        self.assertEqual(self.post(consent=False).status_code, 400)
        self.assertEqual(self.post(consent="true").status_code, 422)
        self.assertEqual(self.post(consent=1).status_code, 422)

    def test_external_provider_and_client_code_rejected(self):
        for extra in ({"provider":"remote"}, {"lean_code":"#eval 1"}, {"source_latex":"other"}, {"budget":1}):
            self.assertEqual(self.post(**extra).status_code, 422)

    def test_changed_or_malformed_source_hash_rejected(self):
        self.assertEqual(self.post(expected_source_sha256="0"*64).status_code, 409)
        self.assertEqual(self.post(expected_source_sha256="x"*64).status_code, 422)
        self.con.execute("UPDATE documents SET sha256=?", ("0"*64,))
        self.con.commit()
        self.assertEqual(self.post().status_code, 409)

    def test_unknown_and_non_theorem_rejected(self):
        self.assertEqual(self.post(entity_id="unknown").status_code, 404)
        self.con.execute("UPDATE entities SET kind='proof'")
        self.con.commit()
        self.assertEqual(self.post().status_code, 400)

    def test_ambiguous_or_invalid_label_rejected(self):
        self.con.execute("INSERT INTO label_conflicts VALUES('thm:pilot')")
        self.con.commit()
        self.assertEqual(self.post().status_code, 409)
        self.con.execute("DELETE FROM label_conflicts")
        self.con.execute("UPDATE labels SET offset=0")
        self.con.commit()
        self.assertEqual(self.post().status_code, 409)

    def test_utf8_byte_budget_is_not_character_budget(self):
        with patch.object(lean_transcription, "MAX_SOURCE_BYTES", len(SOURCE.encode())-1):
            self.assertEqual(self.post().status_code, 413)
