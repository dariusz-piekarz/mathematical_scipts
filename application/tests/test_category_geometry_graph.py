"""Canonical category/geometry graph regression."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class CategoryGeometryGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("KAT-04", "DG-10", "thm:de-rham"),
            ("DG-10", "KAT-04", "cat:ex:derham-natural"),
            ("KAT-04", "ALG-09", "tw:ga9-gaga"),
            ("ALG-09", "KAT-04", "cat:ex:gaga-natural"),
            ("ALG-09", "KAT-13", "def:equivalence"),
            ("KAT-07", "DG-15", "thm:transwersalne-przeciecie"),
            ("DG-15", "KAT-07", "cat:ex:manifold-pullback"),
            ("KAT-09", "ALG-04", "st:kahler"),
            ("ALG-04", "KAT-09", "cat:ex:kahler-rep"),
            ("KAT-09", "ALG-04", "tw:loc-up"),
            ("KAT-09", "AA-12", "aa:tw:localization-universal"),
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
                self.assertGreaterEqual(edges[("KAT-09", "ALG-04")]["reading"], 2)
