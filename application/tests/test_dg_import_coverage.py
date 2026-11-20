"""Identity and reference-status regression tests for DG import coverage."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.dg_import_coverage import coverage


class DgImportCoverageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "dg.db"
        with sqlite3.connect(self.db) as con:
            con.executescript("""
                CREATE TABLE documents (id TEXT);
                CREATE TABLE references_tex (
                    source_document TEXT, target_label TEXT,
                    command TEXT, status TEXT, line INTEGER, offset INTEGER
                );
            """)

    def tearDown(self):
        self.tmp.cleanup()

    def add_docs(self, names):
        with sqlite3.connect(self.db) as con:
            con.executemany("INSERT INTO documents (id) VALUES (?)",
                            [(name,) for name in names])

    def test_partial_import_reports_exact_missing_ids(self):
        self.add_docs(["DG-01", "DG-02", "DG-20", "ALG-01"])
        result = coverage(self.db)
        self.assertEqual(result["imported_chapters"], 3)
        self.assertEqual(result["not_yet_imported"], 33)
        self.assertIn("DG-21", result["missing_ids"])
        self.assertNotIn("DG-20", result["missing_ids"])
        self.assertFalse(result["scope_complete"])

    def test_thirty_six_documents_with_gap_is_not_complete(self):
        self.add_docs([f"DG-{i:02d}" for i in range(1, 36)] + ["DG-37"])
        result = coverage(self.db)
        self.assertEqual(result["imported_chapters"], 36)
        self.assertEqual(result["missing_ids"], ["DG-36"])
        self.assertEqual(result["unexpected_ids"], ["DG-37"])
        self.assertFalse(result["scope_complete"])

    def test_exact_thirty_six_is_complete(self):
        self.add_docs([f"DG-{i:02d}" for i in range(1, 37)])
        result = coverage(self.db)
        self.assertTrue(result["scope_complete"])
        self.assertEqual(result["missing_ids"], [])
        self.assertEqual(result["unexpected_ids"], [])

    def test_unknown_and_ambiguous_reference_statuses_are_unresolved(self):
        self.add_docs(["DG-01"])
        with sqlite3.connect(self.db) as con:
            con.executemany("""
                INSERT INTO references_tex
                (source_document, target_label, command, status, line, offset)
                VALUES (?, ?, 'ref', ?, 1, 0)
            """, [
                ("DG-01", "a", "missing"),
                ("DG-01", "b", "ambiguous"),
                ("DG-01", "c", "included_resolved"),
                ("DG-01", "d", "external_resolved"),
                ("ALG-01", "e", "missing"),
            ])
        result = coverage(self.db)
        self.assertEqual(result["unresolved_count"], 2)
        self.assertEqual(
            {r["target_label"] for r in result["unresolved_refs_in_imported_scope"]},
            {"a", "b"},
        )
        self.assertEqual(result["reference_status_counts"]["included_resolved"], 1)


if __name__ == "__main__":
    unittest.main()
