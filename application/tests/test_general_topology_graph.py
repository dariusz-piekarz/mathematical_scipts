"""Canonical general topology cross-domain graph regression."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class GeneralTopologyGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("GT-11", "FA-10", "thm:banach-steinhaus-lcs"),
            ("GT-11", "FA-11", "thm:open-mapping11"),
            ("GT-11", "FA-11", "thm:closed-graph11"),
            ("GT-23", "TOP-19", "thm:lefschetz-v10"),
            ("GT-04", "KAT-07", "cat:ex:top-pull-push"),
            ("KAT-07", "GT-04", "thm:topog-iloraz-uniwersalnosc"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        needed.update("GT-%02d" % n for n in range(1, 27))
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
                self.assertGreaterEqual(edges[("GT-11", "FA-11")]["reading"], 2)
                legacy = con.execute(
                    "SELECT source_document,target_label FROM references_tex "
                    "WHERE command='atlasref' AND source_document LIKE 'GT-%' "
                    "AND instr(target_label,'::')=0"
                ).fetchall()
                self.assertEqual(legacy, [])
