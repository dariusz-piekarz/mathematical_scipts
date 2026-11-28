"""Canonical logic, measure and model theory graph regression."""
import json
from pathlib import Path
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.graph_coverage import graph_coverage
from backend.latex_parser import build_database, module_id


class LogicMeasureModelGraphTest(unittest.TestCase):
    def test_exact_reading_edges(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        if not canonical.is_dir():
            self.skipTest("canonical repository chapters not available")
        expected = (
            ("LST-30", "ME-03", "thm:caratheodory"),
            ("LST-30", "ME-04", "thm:lebesgue-exists"),
            ("LST-30", "ME-04", "thm:lebesgue-outer-regular"),
            ("LST-30", "ME-04", "thm:lebesgue-inner-regular"),
            ("LST-30", "ME-04", "thm:lebesgue-completion"),
            ("LST-30", "GT-20", "def:topog20-analityczny"),
            ("MOD-22", "MOD-21", "thm:model-tarski-vaught"),
            ("MOD-23", "MOD-20", "thm:compactness"),
            ("MOD-23", "MOD-22", "thm:downward-ls"),
        )
        needed = {doc for source, target, _ in expected for doc in (source, target)}
        catalog = json.loads((repository / "catalog" / "books.json").read_text(encoding="utf-8"))
        migration = json.loads((repository / "catalog" / "logic_model_migration.json").read_text(encoding="utf-8"))
        logic = {module_id(Path(p)) for book in catalog["books"]
                 if book["id"] == "logic_and_set_theory" for p in book["chapters"]}
        models = {module_id(Path(p)) for book in catalog["books"]
                  if book["id"] == "model_theory" for p in book["chapters"]}
        nonclassical = {module_id(Path(p)) for book in catalog["books"]
                        if book["id"] == "nonclassical_logic" for p in book["chapters"]}
        meta = {module_id(Path(p)) for book in catalog["books"]
                if book["id"] == "metamathematics" for p in book["chapters"]}
        self.assertNotIn("LST-40", logic)
        self.assertIn("NCL-01", nonclassical)
        for moved in migration["metamathematics_moves"]:
            self.assertIn(moved["new_id"], meta)
            self.assertNotIn(moved["old_id"], logic)
        for moved in migration["moved_chapters"]:
            self.assertIn(moved["new_id"], models)
            self.assertNotIn(moved["old_id"], logic)
        self.assertNotIn("MOD-13", models)
        aliases = json.loads((repository / "application/config/ALIASY_PO_SCALENIACH.json").read_text(encoding="utf-8"))
        mappings = {(r["old_document"], r["old_label"], r["target_document"], r["target_label"])
                    for r in aliases["qualified_label_aliases"]}
        self.assertTrue({
            ("MOD-13", "res:14:5", "MOD-22", "thm:downward-ls"),
            ("MOD-13", "res:14:9", "MOD-23", "thm:upward-ls"),
            ("LST-23", "thm:downward-ls", "MOD-22", "thm:downward-ls"),
            ("LST-24", "thm:upward-ls", "MOD-23", "thm:upward-ls"),
        }.issubset(mappings))
        for moved in [migration["nonclassical_logic_move"],
                      *migration["metamathematics_moves"]]:
            old, new = moved["old_id"], moved["new_id"]
            self.assertTrue(any(a == old and c == new and b == d
                                for a, b, c, d in mappings), (old, new))
        needed.update(logic | models | nonclassical | meta)
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
                coverage = graph_coverage(con)
                edges = {(e["source"], e["target"]): e for e in coverage["edges"]}
                # A retired duplicate must not remain a live reading target.
                retired_targets = [issue for issue in coverage["reading_audit"]["issues"]
                                   if issue["label"].startswith("MOD-13::")]
                self.assertEqual(retired_targets, [])
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
                self.assertGreaterEqual(edges[("LST-30", "ME-04")]["reading"], 4)
                legacy = con.execute(
                    "SELECT source_document,target_label FROM references_tex "
                    "WHERE command='atlasref' AND source_document LIKE 'LST-%' "
                    "AND instr(target_label,'::')=0"
                ).fetchall()
                self.assertEqual(legacy, [])
