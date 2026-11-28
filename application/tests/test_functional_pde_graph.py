"""Canonical functional analysis and PDE graph regression."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


from distribution_graph_migration import active, migrated_source, migrated_target


class FunctionalPDEGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("PDE-07", "FA-19", "thm:distribution-estimate19"),
            ("PDE-07", "FA-20", "thm:dist-deriv-cont20"),
            ("PDE-07", "FA-21", "thm:strong-mollification21"),
            ("PDE-08", "FA-22", "thm:fourier-auto-tempered22"),
            ("PDE-12", "FA-30", "thm:fredholm-hilbert30"),
            ("PDE-12", "FA-33", "thm:selfadjoint-range33"),
            ("FA-19", "PDE-07", "def:pde7-distribution"),
            ("FA-20", "PDE-07", "def:pde7-derivative"),
            ("FA-21", "PDE-07", "thm:pde7-mollify"),
            ("FA-22", "PDE-08", "def:pde8-distFT"),
            ("FA-30", "PDE-12", "thm:pde12-general-fredholm"),
            ("FA-33", "PDE-12", "def:pde12-adjoint"),
        )
        catalog = json.loads((repository / "catalog" / "books.json").read_text(encoding="utf-8"))
        if active(catalog):
            expected = tuple((migrated_source(s, t + "::" + label),
                              migrated_target(t, label), label)
                             for s, t, label in expected)
        needed = {doc for source, target, _ in expected for doc in (source, target)}
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
