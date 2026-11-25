"""Canonical choice principles and their applications in the graph."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class ChoiceGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("LST-26", "LA-01", "thm:lin-istnienie-bazy-zorn"),
            ("LST-29", "GT-07", "thm:topog-tychonoff-iloczyny"),
            ("LST-29", "GT-11", "thm:topog-baire-metryczne"),
            ("GT-07", "LST-29", "thm:bpi-ultrafilter-equivalence"),
            ("GT-07", "LST-29", "thm:ac-full-tychonoff"),
            ("GT-07", "LST-29", "thm:bpi-tychonoff-hausdorff"),
            ("GT-11", "LST-29", "thm:weak-choice-baire-dc"),
            ("FA-06", "LA-01", "thm:lin-istnienie-bazy-zorn"),
            ("LA-01", "LST-26", "thm:choice-hamel-basis"),
            ("FA-06", "LST-26", "thm:choice-zorn"),
            ("GT-07", "LST-26", "thm:choice-zorn"),
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
                self.assertGreaterEqual(edges[("GT-07", "LST-29")]["reading"], 3)
