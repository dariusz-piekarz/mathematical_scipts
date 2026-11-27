"""Canonical measure and integration theory graph regression."""
import json
from contextlib import closing
from pathlib import Path
import re
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, masked_source, module_id


class MeasureIntegrationGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        # CAL is a donor script during redistribution. Retain its exact
        # outgoing links while requiring the current canonical AM1 owners,
        # not obsolete backlinks into the donor script.
        expected = (
            ("CAL-01", "AM1-29", "ma1:thm:darboux-criterion"),
            ("CAL-02", "AM1-29", "ma1:thm:riemann-darboux-equivalence"),
            ("CAL-03", "AM1-40", "it:thm:rs-integrator-substitution"),
            ("CAL-04", "AM1-36", "ma1:kh:thm:kh-hake"),
            ("CAL-05", "AM1-39", "it:thm:perron-hk"),
            ("CAL-06", "AM1-42", "tw:ks-cauchy"),
            ("CAL-07", "AM1-37", "it:thm:mcshane-absolute"),
            ("CAL-08", "AM1-38", "ma1:kh:thm:kh-acgstar-characterization"),
            ("CAL-09", "AM1-41", "tw:denjoy-szeroka-ftc"),
            ("CAL-10", "ME-26", "thm:hausdorff-borel-26"),
            ("ME-26", "CAL-10", "thm:hausdorff-borel-26"),
            ("ME-07", "CAL-07", "it:thm:mcshane-lebesgue"),
            ("ME-21", "ME-32", "it:thm:daniell-stone"),
            ("ME-21", "ME-32", "it:thm:daniell-stone-general"),
            ("ME-21", "ME-32", "it:ex:daniell-cc"),
            ("ME-21", "ME-32", "it:thm:daniell-radon-comparison"),
            ("CAL-12", "ME-03", "thm:caratheodory"),
            ("CAL-11", "ME-07", "ch:calkowanie-lebesgue"),
            ("CAL-14", "ME-23", "thm:haar-main-23"),
            ("CAL-14", "GT-24", "def:topog24-group"),
            ("CAL-14", "GT-14", "def:topog-baire-lokalna-zwartosc"),
            ("ME-23", "GT-24", "def:topog24-group"),
            ("ME-23", "GT-14", "def:topog-baire-lokalna-zwartosc"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        needed.update("ME-%02d" % n for n in range(1, 33))
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
            with closing(sqlite3.connect(db)) as con, con:
                edges = {(e["source"], e["target"]): e for e in graph_coverage(con)["edges"]}
                for source, target, label in expected:
                    with self.subTest(source=source, target=target, label=label):
                        # Repeated reading links are legitimate. Verify every
                        # source occurrence, including its line, rather than
                        # assuming a chapter can cite a result only once.
                        text = masked_source(sources[source].read_text(encoding="utf-8"))
                        pattern = r"\\atlasref\s*\{\s*" + re.escape(target + "::" + label) + r"\s*\}"
                        expected_lines = [text.count("\n", 0, match.start()) + 1
                                          for match in re.finditer(pattern, text)]
                        self.assertTrue(expected_lines, "Required reading link disappeared from source")
                        rows = con.execute(
                            "SELECT status,target_document,target_entity,line "
                            "FROM references_tex WHERE source_document=? "
                            "AND command='atlasref' AND target_label=? ORDER BY line,id",
                            (source, target + "::" + label),
                        ).fetchall()
                        self.assertEqual([row[3] for row in rows], expected_lines)
                        for status, owner, entity, _ in rows:
                            self.assertEqual(status, "external_resolved")
                            self.assertEqual(owner, target)
                            self.assertIsNotNone(entity)
                            self.assertEqual(con.execute(
                                "SELECT entity_id FROM label_occurrences "
                                "WHERE document_id=? AND name=?", (target, label)
                            ).fetchall(), [(entity,)])
                        self.assertGreaterEqual(edges[(source, target)]["reading"], len(rows))
                legacy = con.execute(
                    "SELECT source_document,target_label FROM references_tex "
                    "WHERE command='atlasref' AND source_document LIKE 'ME-%' "
                    "AND instr(target_label,'::')=0"
                ).fetchall()
                self.assertEqual(legacy, [])
