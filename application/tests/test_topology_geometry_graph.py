"""Canonical topology/geometry reading link regression."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class TopologyGeometryGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("DG-06", "TOP-03", "thm:les-homologia"),
            ("TOP-03", "DG-06", "thm:les-homologia"),
            ("DG-07", "TOP-04", "thm:van-kampen"),
            ("TOP-04", "DG-07", "thm:van-kampen"),
            ("DG-08", "TOP-05", "thm:homotopia-singularna"),
            ("TOP-05", "DG-08", "thm:homotopia-singularna"),
            ("DG-09", "TOP-06", "thm:whitehead"),
            ("TOP-06", "DG-09", "thm:whitehead"),
            ("DG-10", "TOP-09", "thm:de-rham"),
            ("TOP-09", "DG-10", "thm:de-rham"),
            ("DG-10", "TOP-09", "thm:stokes-formy"),
            ("TOP-09", "DG-10", "thm:stokes-formy"),
            ("DG-18", "TOP-18", "thm:morse-lemma-v10"),
            ("TOP-18", "DG-18", "thm:lemat-morsea-17"),
            ("DG-18", "TOP-18", "thm:morse-singular-v10"),
            ("TOP-18", "DG-18", "thm:homologia-morse-17"),
            ("DG-17", "TOP-11", "thm:poincare-dualnosc-16"),
            ("TOP-11", "DG-17", "thm:poincare-dualnosc-16"),
            ("DG-15", "TOP-17", "lem:pt-regular-v9"),
            ("TOP-17", "DG-15", "thm:transwersalny-przeciwobraz"),
            ("DG-16", "TOP-17", "lem:pt-collapse-v9"),
            ("TOP-17", "DG-16", "thm:otoczenie-tubularne"),
            ("DG-17", "TOP-17", "thm:pt-pd-v9"),
            ("TOP-17", "DG-17", "thm:euler-thom-16"),
            ("DG-19", "TOP-17", "prop:bordism-group-v9"),
            ("TOP-17", "DG-19", "def:kobordyzm-18"),
            ("TOP-17", "DG-03", "thm:tensor-hom"),
            ("TOP-20", "DG-18", "ch:teoria-morsea"),
            ("TOP-23", "DG-03", "thm:tensor-istnienie"),
            ("TOP-25", "DG-03", "thm:tensor-istnienie"),
            ("TOP-30", "DG-01", "ch:rozmaitosci"),
            ("TOP-30", "DG-03", "ch:algebra-tensorowa"),
            ("TOP-30", "DG-15", "ch:sard-transwersalnosc"),
            ("TOP-30", "DG-16", "ch:wlozenia-otoczenia"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        catalog = json.loads((repository / "catalog" / "books.json").read_text(encoding="utf-8"))
        sources = {}
        for book in catalog["books"]:
            for relative in book["chapters"]:
                source_path = repository / relative
                chapter = module_id(source_path)
                if chapter in needed:
                    if chapter in sources:
                        self.assertEqual(sources[chapter], source_path)
                    sources[chapter] = source_path
        self.assertEqual(set(sources), needed)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for source_path in sources.values():
                dest = root / source_path.relative_to(canonical)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(source_path.read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                edges = {(e["source"], e["target"]): e for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        rows = con.execute(
                            "SELECT status,target_document,target_entity "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=?",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        status, owner, entity = rows[0]
                        self.assertEqual(status, "external_resolved")
                        self.assertEqual(owner, target)
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (target, label)
                        ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], 1)
                self.assertEqual(len([e for e in edges if e[0] == "TOP-30"
                                      and e[1].startswith("DG-")]), 4)
