"""Regression tests for read-only missing-reference triage."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.triage_unresolved_refs import markdown, triage


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "references.db"
        with sqlite3.connect(self.db) as con:
            con.executescript("""
                CREATE TABLE documents(id TEXT PRIMARY KEY, path TEXT);
                CREATE TABLE references_tex(
                    source_document TEXT, command TEXT, target_label TEXT,
                    line INTEGER, offset INTEGER, status TEXT
                );
            """)
            con.executemany("INSERT INTO documents VALUES (?,?)", [
                ("DG-01", "chapters/pl/differential_geometry_and_topology/01.tex"),
                ("ALG-10", "chapters/pl/algebraic_geometry/10.tex"),
            ])
            con.executemany(
                "INSERT INTO references_tex VALUES (?,?,?,?,?,?)", [
                    ("DG-01", "ref", "missing-dg", 15, 0, "missing"),
                    ("ALG-10", "eqref", "ambiguous-alg", 20, 0, "ambiguous"),
                    ("ALG-10", "ref", "resolved-shared", 30, 0, "included_resolved"),
                    ("ALG-10", "ref", "resolved-local", 40, 0, "resolved"),
                ])

    def tearDown(self):
        self.tmp.cleanup()

    def test_outputs_only_unresolved_with_source_locations(self):
        result = triage(self.db)
        self.assertEqual(result["unresolved_occurrences"], 2)
        self.assertEqual(
            [(r["source_document"], r["line"], r["target_label"])
             for r in result["items"]],
            [("ALG-10", 20, "ambiguous-alg"), ("DG-01", 15, "missing-dg")])
        self.assertFalse(result["dg_scope_complete"])
        self.assertEqual(result["items"][1]["review_queue"],
                         "DG_incomplete_scope_manual_target_check")
        self.assertEqual(result["items"][0]["review_queue"],
                         "ambiguous_target_manual_review")
        self.assertIn("DG-01:15", markdown(result))

    def test_triage_does_not_change_index(self):
        before = self.db.read_bytes()
        triage(self.db)
        self.assertEqual(self.db.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
