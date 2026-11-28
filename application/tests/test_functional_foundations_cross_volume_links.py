"""Regression for functional analysis foundations and distribution references."""
import json
from pathlib import Path
import shutil
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.latex_parser import build_database, module_id

from distribution_graph_migration import migrate_required

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "FA-01": {"GT-24::def:topog24-group", "GT-05::def:topog-t0-t1-t2",
              "GT-04::thm:topog-iloczyn-uniwersalnosc"},
    "FA-04": {"GT-24::thm:topog24-birkhoff-kakutani",
              "GT-18::def:topog-odwzorowania-jednostajna-zwarte"},
    "FA-05": {"GT-10::def:topog-pseudometryka-metryka",
              "GT-13::thm:topog-uzupelnienia-filtry-sieci"},
    "FA-07": {"AM1-25::ma1:thm:convex-support"},
    "FA-08": {"GT-04::thm:topog-poczatkowa-uniwersalnosc", "LA-07::def:lin7-dual"},
    "FA-10": {"GT-11::thm:topog-baire-metryczne"},
    "FA-12": {"ME-14::thm:riesz-fischer-14", "ME-15::thm:dual-lp-15",
              "ME-21::thm:compact-riesz-21"},
    "FA-14": {"AM1-20::ma1:thm:linear-approximation"},
    "FA-15": {"LA-08::def:lin8-wieloliniowe", "AM1-23::ma1:thm:taylor-peano"},
    "FA-15A": {"AM1-29::ma1:def:riemann-sum"},
    "FA-16": {"AM1-25::ma1:def:convex-function"},
    "FA-19": {"PDE-07::def:pde7-distribution"},
    "FA-20": {"PDE-07::def:pde7-derivative"},
    "FA-21": {"PDE-07::thm:pde7-mollify"},
}


class FunctionalFoundationsCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 22)
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
