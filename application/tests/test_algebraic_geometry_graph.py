"""Canonical algebraic geometry reading link regression."""
import json
from pathlib import Path
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class AlgebraicGeometryGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("ALG-00", "AA-09", "aa:ch:pierscienie"),
            ("ALG-00", "AA-11", "aa:ch:wielomiany"),
            ("ALG-01", "AA-12", "aa:tw:radical-intersection-primes"),
            ("ALG-01", "AA-13", "aa:tw:hilbert-basis"),
            ("ALG-01", "AA-21", "aa:def:algebraic-closure"),
            ("ALG-03", "AA-12", "aa:def:localization"),
            ("ALG-03", "AA-14", "aa:tw:nakayama-minimal-generators"),
            ("ALG-03", "AA-40", "aa:prz:integral-cusp-normalization"),
            ("TOP-28", "ALG-05", "tw:ga5-smooth-center-model"),
            ("TOP-28", "ALG-09", "tw:ga9-hard-lefschetz"),
            ("TOP-28", "ALG-10", "tw:ga10-index"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        needed.update("ALG-%02d" % n for n in range(11))
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
                for source, target in (("TOP-28", "ALG-05"),
                                       ("TOP-28", "ALG-09"),
                                       ("TOP-28", "ALG-10")):
                    self.assertGreaterEqual(edges[(source, target)]["reading"], 1)
                legacy = con.execute(
                    "SELECT source_document,target_label FROM references_tex "
                    "WHERE command='atlasref' AND source_document LIKE 'ALG-%' "
                    "AND instr(target_label,'::')=0"
                ).fetchall()
                self.assertEqual(legacy, [])
