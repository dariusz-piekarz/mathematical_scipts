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
        # Retired CAL redirects no longer occur in the active graph.
        # Preserve their canonical targets as independent ownership checks.
        migrated_targets = (
            ("AM1-29", "ma1:thm:darboux-criterion"),
            ("AM1-29", "ma1:thm:riemann-darboux-equivalence"),
            ("AM1-40", "it:thm:rs-integrator-substitution"),
            ("AM1-36", "ma1:kh:thm:kh-hake"),
            ("AM1-39", "it:thm:perron-hk"),
            ("AM1-42", "tw:ks-cauchy"),
            ("AM1-37", "it:thm:mcshane-absolute"),
            ("AM1-38", "ma1:kh:thm:kh-acgstar-characterization"),
            ("AM1-41", "tw:denjoy-szeroka-ftc"),
            ("ME-26", "thm:hausdorff-borel-26"),
            ("ME-32", "ch:daniell-stone-32"),
            ("ME-32", "it:thm:daniell-stone"),
            ("ME-07", "ch:calkowanie-lebesgue"),
            ("ME-23", "thm:haar-main-23"),
            ("ME-23", "ch:haar-23"),
            ("ME-23", "cor:haar-finiteness-23"),
        )
        expected = (
            ("ME-07", "AM1-37", "it:thm:mcshane-lebesgue"),
            ("AM1-37", "ME-07", "thm:ae-integral-invariance"),
            ("ME-32", "ME-21", "thm:riesz-positive-21"),
            ("ME-21", "ME-32", "it:thm:daniell-stone"),
            ("ME-21", "ME-32", "it:thm:daniell-stone-general"),
            ("ME-21", "ME-32", "it:ex:daniell-cc"),
            ("ME-21", "ME-32", "it:thm:daniell-radon-comparison"),
            ("ME-32", "ME-03", "thm:caratheodory"),
            ("ME-23", "GT-24", "def:topog24-group"),
            ("ME-23", "GT-14", "def:topog-baire-lokalna-zwartosc"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        needed.update(doc for doc, _ in migrated_targets)
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
                for owner, label in migrated_targets:
                    with self.subTest(migrated_owner=owner, label=label):
                        rows = con.execute(
                            "SELECT document_id,entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?", (owner, label)
                        ).fetchall()
                        self.assertEqual(len(rows), 1)
                        self.assertIsNotNone(rows[0][1])
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
