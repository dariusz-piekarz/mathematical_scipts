"""Canonical measure and integration theory graph regression."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class MeasureIntegrationGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("CAL-01", "AM1-29", "ma1:thm:darboux-criterion"),
            ("AM1-29", "CAL-01", "ma1:thm:darboux-criterion"),
            ("CAL-02", "AM1-29", "ma1:thm:riemann-darboux-equivalence"),
            ("AM1-29", "CAL-02", "ma1:thm:riemann-darboux-equivalence"),
            ("CAL-03", "AM1-36", "it:thm:rs-integrator-substitution"),
            ("AM1-36", "CAL-03", "it:thm:rs-integrator-substitution"),
            ("CAL-04", "AM1-36", "ma1:kh:thm:kh-hake"),
            ("AM1-36", "CAL-04", "ma1:kh:thm:kh-hake"),
            ("CAL-05", "AM1-36", "it:thm:perron-hk"),
            ("AM1-36", "CAL-05", "it:thm:perron-hk"),
            ("CAL-06", "AM1-36", "tw:ks-cauchy"),
            ("AM1-36", "CAL-06", "tw:ks-cauchy"),
            ("CAL-07", "AM1-36", "it:thm:mcshane-absolute"),
            ("AM1-36", "CAL-07", "it:thm:mcshane-absolute"),
            ("CAL-08", "AM1-36", "ma1:kh:thm:kh-acgstar-characterization"),
            ("AM1-36", "CAL-08", "ma1:kh:thm:kh-acgstar-characterization"),
            ("CAL-09", "AM1-36", "tw:denjoy-szeroka-ftc"),
            ("AM1-36", "CAL-09", "tw:denjoy-szeroka-ftc"),
            ("CAL-10", "ME-26", "thm:hausdorff-borel-26"),
            ("ME-26", "CAL-10", "thm:hausdorff-borel-26"),
            ("ME-07", "CAL-11", "it:thm:mcshane-lebesgue"),
            ("ME-21", "CAL-12", "it:thm:daniell-stone"),
            ("ME-23", "CAL-14", "tw:haar-automorfizm"),
            ("CAL-12", "ME-03", "thm:caratheodory"),
            ("CAL-11", "ME-07", "ch:calkowanie-lebesgue"),
            ("CAL-14", "ME-23", "thm:haar-main-23"),
            ("CAL-14", "ME-03", "thm:caratheodory"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        needed.update("ME-%02d" % n for n in range(1, 32))
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
                legacy = con.execute(
                    "SELECT source_document,target_label FROM references_tex "
                    "WHERE command='atlasref' AND source_document LIKE 'ME-%' "
                    "AND instr(target_label,'::')=0"
                ).fetchall()
                self.assertEqual(legacy, [])
