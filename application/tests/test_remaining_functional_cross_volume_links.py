"""Regression for remaining functional analysis cross-volume references."""
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.latex_parser import build_database, module_id

from distribution_graph_migration import migrate_required

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "FA-17": {"ME-10::thm:cc-in-lp-10", "PDE-08::def:pde8-schwartz",
              "PDE-08::thm:pde8-inversion"},
    "FA-18": {"PDE-07::def:pde7-test", "KAT-08::def:colimit",
              "GT-04::thm:topog-koncowa-uniwersalnosc"},
    "FA-22": {"PDE-08::def:pde8-tempered", "PDE-08::def:pde8-distFT"},
    "FA-23": {"GT-07::thm:topog-zwartosc-sieci", "LA-10::thm:lin10-istnienie"},
    "FA-25": {"PDE-07::def:pde7-test", "KAT-09::cat:ex:tensor-rep"},
    "FA-26": {"LA-07::thm:lin7-bidualnosc", "ME-15::thm:uniform-convexity-15",
              "ME-15::thm:reflexive-lp-15"},
}


class RemainingFunctionalCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 15)
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        required = migrate_required(required, catalog)
        wanted = {src for src, _, _ in required} | {dst for _, _, dst in required}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "pl"
            copied = set()
            for book in catalog["books"]:
                for filename in book["chapters"]:
                    p = Path(filename)
                    mid = module_id(p)
                    if mid not in wanted:
                        continue
                    dest = root / p.parent.name / p.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / p, dest)
                    copied.add(mid)
            self.assertEqual(copied, wanted)
            db = Path(temp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                con.row_factory = sqlite3.Row
                found = {(r["source_document"], r["target_label"], r["target_document"])
                         for r in con.execute(
                             "SELECT source_document,target_label,target_document FROM references_tex "
                             "WHERE command='atlasref' AND status='external_resolved'")}
                self.assertFalse(required - found, required - found)
                domains = {r["id"]: r["domain"] for r in con.execute("SELECT id,domain FROM documents")}
                for left, right in sorted({tuple(sorted((domains[s], domains[t])))
                                           for s, _, t in required}):
                    pairs = {(s, t) if domains[s] == left else (t, s)
                             for s, _, t in required if {domains[s], domains[t]} == {left, right}}
                    for granularity in ("module", "section", "entity"):
                        for a, b in ((left, right), (right, left)):
                            graph = bipartite_graph(con, a, b, granularity, 1, 250)
                            nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                            actual = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                            if a != left:
                                actual = {(t, s) for s, t in actual}
                            self.assertFalse(pairs - actual, (a, b, granularity, pairs - actual))
