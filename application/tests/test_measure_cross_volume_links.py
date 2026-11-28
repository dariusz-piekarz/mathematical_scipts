"""Regression for measure theory links to topology, analysis and integration."""
import json
from pathlib import Path
import shutil
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.latex_parser import build_database, module_id

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "ME-14": {"FA-12::thm:lp-banach12"},
    "ME-15": {"FA-08::def:slaba-gwiazdka", "FA-26::thm:reflexive-ball26",
              "FA-26::thm:eberlein-smulian26"},
    "ME-20": {"GT-19::def:topog-polskie-borel", "GT-19::def:topog-polskie",
              "GT-14::def:topog-baire-lokalna-zwartosc"},
    "ME-21": {"FA-12::thm:riesz-markov12"},
    "ME-22": {"FA-08::def:slaba-gwiazdka", "GT-19::def:topog-polskie"},
    "ME-23": {"GT-24::def:topog24-group", "GT-14::def:topog-baire-lokalna-zwartosc"},
    "ME-30": {"FA-15B::thm:bochner-criterion15b", "FA-15B::def:rnp15b"},
    "FA-15B": {"ME-30::def:bochner-30", "ME-08::thm:vitali-l1",
               "ME-12::thm:fubini-12", "ME-30::def:RNP-30"},
}


class MeasureCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 18)
        wanted = set(EXPECTED) | {dst for _, _, dst in required}
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
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
            with closing(sqlite3.connect(db)) as con, con:
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
