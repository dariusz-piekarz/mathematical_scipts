"""Canonical abstract algebra links to geometry and category theory."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class AbstractAlgebraGeometryCategoryGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("DG-05", "AA-16", "aa:tw:modules-first-isomorphism"),
            ("AA-16", "DG-05", "thm:modul-izomorfizm"),
            ("AA-12", "ALG-01", "tw:radical-correspondence"),
            ("AA-12", "KAT-09", "cat:ex:localization-rep"),
            ("AA-13", "ALG-01", "tw:hilbert-basis"),
            ("AA-14", "ALG-03", "tw:zariski-tangent-formula"),
            ("AA-16", "KAT-09", "cat:ex:free-module-rep"),
            ("ALG-01", "AA-12", "aa:tw:radical-intersection-primes"),
            ("ALG-01", "AA-13", "aa:tw:hilbert-basis"),
            ("ALG-03", "AA-14", "aa:tw:nakayama-minimal-generators"),
            ("KAT-09", "AA-12", "aa:tw:localization-universal"),
            ("KAT-09", "AA-16", "aa:tw:modules-free-universal"),
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
                for source, target, _ in expected:
                    self.assertGreaterEqual(edges[(target, source)]["reading"], 1)
