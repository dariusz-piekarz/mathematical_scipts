import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage, reading_reference_issues
from backend.latex_parser import build_database


class GraphCoverageTest(unittest.TestCase):
    def test_isolated_chapters_missing_catalog_entries_and_direction(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "pl"
            sources = {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{aa:a}",
                "linear_algebra/01-b.tex": r"\chapter{B}\atlasref{AA-01::aa:a}{A}",
                "linear_algebra/02-c.tex": r"\chapter{C}\ref{missing}",
                "general_topology/01-d.tex": r"\chapter{D}",
            }
            for p, body in sources.items():
                dest = root / p
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            catalog = base / "books.json"
            catalog.write_text(json.dumps({"books": [{"chapters": [
                "chapters/pl/" + p for p in sources
            ] + ["chapters/pl/abstract_algebra/02-missing.tex"]}]}), encoding="utf-8")
            db = base / "test.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                report = graph_coverage(con, catalog)
            self.assertEqual(report["summary"]["indexed_chapters"], 4)
            self.assertEqual(report["summary"]["cross_linked_chapters"], 2)
            self.assertEqual(report["summary"]["isolated_chapters"], 2)
            self.assertEqual(report["summary"]["connected_domain_pairs"], 1)
            self.assertEqual(report["summary"]["domain_pairs"], 3)
            self.assertEqual(report["catalog"]["missing"][0]["id"], "AA-02")
            self.assertEqual(report["catalog"]["path_mismatches"], [])
            self.assertEqual(report["edges"], [
                {"source": "LA-01", "target": "AA-01", "weight": 1, "reading": 1}
            ])
            chapters = {c["id"]: c for c in report["chapters"]}
            self.assertEqual(chapters["LA-02"]["unresolved"], 1)
            self.assertTrue(chapters["GT-01"]["isolated"])
            self.assertEqual(chapters["AA-01"]["cross_incoming"], 1)
            self.assertEqual(chapters["LA-01"]["cross_outgoing"], 1)


    def test_reading_audit_rejects_missing_and_wrong_occurrence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for relative, body in {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{shared}",
                "abstract_algebra/02-b.tex": r"\chapter{B}\label{shared}",
                "linear_algebra/01-c.tex": (
                    r"\chapter{C}\atlasref{AA-01::shared}{A}"
                    r"\atlasref{AA-02::shared}{B}"
                    r"\atlasref{AA-03::shared}{Missing}"
                ),
            }.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                audit = reading_reference_issues(con)
                self.assertEqual(audit["checked"], 3)
                self.assertEqual(audit["invalid"], 1)
                self.assertEqual(audit["issues"][0]["reason"], "unresolved")
                wrong = con.execute(
                    "SELECT entity_id FROM label_occurrences "
                    "WHERE document_id='AA-02' AND name='shared'"
                ).fetchone()[0]
                con.execute(
                    "UPDATE references_tex SET target_document='AA-02', target_entity=? "
                    "WHERE target_label='AA-01::shared'", (wrong,))
                audit = reading_reference_issues(con)
                self.assertEqual(audit["invalid"], 2)
                self.assertEqual({i["reason"] for i in audit["issues"]},
                                 {"unresolved", "qualified_occurrence_mismatch"})
                self.assertEqual(graph_coverage(con)["summary"]["invalid_reading_references"], 2)
