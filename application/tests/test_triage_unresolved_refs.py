"""Regression tests for read-only missing-reference triage."""
import sqlite3
from contextlib import closing, redirect_stdout
from io import StringIO
from unittest.mock import patch
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.triage_unresolved_refs import main, markdown, triage


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "references.db"
        with closing(sqlite3.connect(self.db)) as con, con:
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

    def test_exact_pending_targets_are_tracked_but_not_resolved(self):
        with closing(sqlite3.connect(self.db)) as con, con:
            con.executemany("INSERT INTO documents VALUES (?,?)", [
                ("AA-06", "abstract_algebra/06.tex"),
                ("AA-05", "abstract_algebra/05.tex"),
                ("LST-04", "logic_and_set_theory/04.tex"),
                ("DG-11", "differential_geometry_and_topology/11.tex"),
            ])
            con.executemany(
                "INSERT INTO references_tex VALUES (?,?,?,?,?,?)", [
                    ("AA-06", "ref", "aa:ch:grupy-abelowe", 11, 0, "missing"),
                    ("AA-05", "ref", "aa:ch:grupy-abelowe", 15, 0, "missing"),
                    ("LST-04", "ref", "ch:functions", 18, 0, "missing"),
                    ("DG-11", "ref", "prz:thur-dop-nil-kontakt", 20, 0, "missing"),
                    ("DG-11", "ref", "fabricated-dg-reference", 22, 0, "missing"),
                    ("AA-06", "ref", "aa:ch:grupy-abelowe", 25, 0, "ambiguous"),
                ]
            )
        report = triage(self.db)
        keyed = {(x["source_document"], x["target_label"], x["status"], x["line"]):
                 x for x in report["items"]}
        aa = keyed[("AA-06", "aa:ch:grupy-abelowe", "missing", 11)]
        self.assertTrue(aa["known_pending"])
        self.assertTrue(aa["requires_mathematical_review"])
        self.assertEqual(aa["review_queue"], "documented_future_chapter_not_yet_imported")
        self.assertEqual(aa["status"], "missing")
        self.assertTrue(keyed[("LST-04", "ch:functions", "missing", 18)]["known_pending"])
        self.assertTrue(keyed[("DG-11", "prz:thur-dop-nil-kontakt", "missing", 20)]["known_pending"])
        self.assertFalse(keyed[("AA-05", "aa:ch:grupy-abelowe", "missing", 15)]["known_pending"])
        self.assertFalse(keyed[("DG-11", "fabricated-dg-reference", "missing", 22)]["known_pending"])
        self.assertFalse(keyed[("AA-06", "aa:ch:grupy-abelowe", "ambiguous", 25)]["known_pending"])
        self.assertIn("Nowe / wymagające klasyfikacji", markdown(report))

    def test_dg_scope_completion_expires_incomplete_scope_baseline(self):
        with closing(sqlite3.connect(self.db)) as con, con:
            con.executemany(
                "INSERT INTO documents VALUES (?,?)",
                [(f"DG-{i:02d}", f"dg/{i:02d}.tex") for i in range(2, 37)]
            )
            con.execute(
                "INSERT INTO references_tex VALUES (?,?,?,?,?,?)",
                ("DG-11", "ref", "prz:thur-dop-nil-kontakt", 20, 0, "missing")
            )
        report = triage(self.db)
        self.assertTrue(report["dg_scope_complete"])
        row = next(x for x in report["items"] if x["source_document"] == "DG-11")
        self.assertFalse(row["known_pending"])
        self.assertEqual(row["review_queue"], "missing_target_manual_review")

    def test_cli_strict_mode_fails_for_unreviewed_missing_or_ambiguous(self):
        out = Path(self.tmp.name) / "triage_report"
        with patch.object(sys, "argv", [
            "triage_unresolved_refs.py", "--db", str(self.db),
            "--out", str(out), "--fail-on-unclassified"
        ]), redirect_stdout(StringIO()):
            self.assertEqual(main(), 3)
        self.assertTrue(out.with_suffix(".json").exists())
        self.assertTrue(out.with_suffix(".md").exists())
        with patch.object(sys, "argv", [
            "triage_unresolved_refs.py", "--db", str(self.db),
            "--out", str(out)
        ]), redirect_stdout(StringIO()):
            self.assertEqual(main(), 0)

    def test_triage_does_not_change_index(self):
        before = self.db.read_bytes()
        triage(self.db)
        self.assertEqual(self.db.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
