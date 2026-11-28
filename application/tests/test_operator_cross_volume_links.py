"""Regression for functional analysis operator theory across volumes."""
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.latex_parser import build_database, module_id

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "FA-28": {"GT-18::def:topog-odwzorowania-jednostajna-zwarte", "LA-03::def:lin3-rzad-nullity"},
    "FA-29": {"GT-07::thm:topog-zwartosc-sieci", "LA-07::thm:lin7-jadro-obraz-dualnego",
              "AA-15::aa:def:nc-ideals"},
    "FA-30": {"LA-03::thm:lin3-rzad-nullity", "LA-13::thm:lin13-kernel-image",
              "PDE-12::thm:pde12-general-fredholm"},
    "FA-31": {"LA-03::prop:lin3-end-algebra", "AA-09::aa:def:prime-max-ideal",
              "LA-18::thm:lin18-analytic-calculus"},
    "FA-32": {"LA-14::thm:lin14-normal-spectral", "ME-21::thm:riesz-complex-21",
              "LA-14::thm:lin14-spectral-projections", "LA-15::thm:lin15-polar"},
    "FA-33": {"PDE-12::def:pde12-adjoint", "PDE-12::thm:pde12-A-selfadjoint",
              "ME-07::def:integral-positive", "GT-24::def:topog24-group"},
}


class OperatorCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 19)
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
