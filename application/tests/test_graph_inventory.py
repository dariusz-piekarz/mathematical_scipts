"""Graph coverage inventory and duplicate target regression tests."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage, reading_reference_issues
from backend.latex_parser import build_database


class GraphInventoryTest(unittest.TestCase):
    def test_inventory_distinguishes_internal_and_cross_domain_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "pl"
            sources = {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{shared}",
                "abstract_algebra/02-b.tex": r"\chapter{B}\label{other}\ref{shared}",
                "linear_algebra/01-c.tex": (
                    r"\chapter{C}\atlasref{AA-01::shared}{A}"
                    r"\atlasref{shared}{Legacy}"
                ),
                "general_topology/01-d.tex": r"\chapter{D}",
            }
            for relative, body in sources.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            catalog = base / "books.json"
            catalog.write_text(json.dumps({"books": [{"chapters": [
                "chapters/pl/" + p for p in sources if "general_topology" not in p
            ]}]}), encoding="utf-8")
            db = base / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                report = graph_coverage(con, catalog)
                self.assertEqual(report["reading_audit"]["invalid"], 0)
            inventory = report["reading_inventory"]
            self.assertEqual((inventory["total"], inventory["qualified"], inventory["legacy"]),
                             (2, 1, 1))
            self.assertEqual(len(inventory["legacy_references"]), 1)
            legacy = inventory["legacy_references"][0]
            self.assertEqual((legacy["source"], legacy["label"], legacy["target"]),
                             ("LA-01", "shared", "AA-01"))
            self.assertEqual(report["summary"]["cross_isolated_chapters"], 2)
            self.assertEqual(report["summary"]["isolated_chapters"], 1)
            self.assertEqual(report["summary"]["legacy_reading_references"], 1)
            chapters = {c["id"]: c for c in report["chapters"]}
            self.assertTrue(chapters["AA-02"]["cross_isolated"])
            self.assertFalse(chapters["AA-02"]["isolated"])
            self.assertTrue(chapters["GT-01"]["isolated"])
            domains = {d["domain"]: d for d in report["domain_coverage"]}
            aa = domains[chapters["AA-01"]["domain"]]
            self.assertEqual(aa["cross_isolated_ids"], ["AA-02"])
            self.assertEqual(aa["isolated_all_chapters"], 0)
            self.assertEqual([d["id"] for d in report["catalog"]["indexed_outside_catalog"]],
                             ["GT-01"])

    def test_duplicate_qualified_occurrence_cannot_pass_as_resolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "pl"
            for relative, body in {
                "abstract_algebra/01-a.tex": r"\chapter{A}\label{shared}",
                "linear_algebra/01-b.tex": r"\chapter{B}\atlasref{AA-01::shared}{A}",
            }.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding="utf-8")
            db = base / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                self.assertEqual(reading_reference_issues(con)["invalid"], 0)
                # Simulate a stale/corrupt index with a second source occurrence
                # attached to the same entity, while the old status stays resolved.
                con.execute("""
                    INSERT INTO label_occurrences
                        (occurrence_id,name,document_id,entity_id,line,offset,concept_id)
                    SELECT occurrence_id || ':duplicate',name,document_id,entity_id,
                           line+1000,offset+1000,concept_id
                    FROM label_occurrences WHERE document_id='AA-01' AND name='shared'
                """)
                audit = reading_reference_issues(con)
                self.assertEqual(audit["invalid"], 1)
                self.assertEqual(audit["issues"][0]["reason"],
                                 "qualified_occurrence_ambiguous")
