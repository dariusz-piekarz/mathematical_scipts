"""Regression for remaining measure theory chapters and cross-volume references."""
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
    "ME-01": {"GT-19::def:topog-polskie-borel", "LST-08::def:image-preimage"},
    "ME-02": {"LST-03::def:set-liminf-limsup"},
    "ME-03": {"P1-02::ch:probability"},
    "ME-04": {"AM1-19::ma1:thm:cantor-properties", "LST-26::def:choice"},
    "ME-05": {"GT-04::def:topog-iloczyn", "GT-19::def:topog-polskie"},
    "ME-06": {"AM1-08::ma1:def:liminf-limsup"},
    "ME-07": {"P1-05::ch:expectation"},
    "ME-08": {"AM1-29::ma1:thm:riemann-darboux-equivalence"},
    "ME-10": {"GT-05::thm:topog-tietze", "DT-01::lem:cutoffs17"},
    "ME-11": {"AM1-32::ma1:thm:parameter-differentiation"},
    "ME-12": {"P1-02::ch:probability"},
    "ME-16": {"FA-12::def:banach12"},
    "ME-17": {"P3-08::ch:girsanov"},
    "ME-19": {"P4-01::ch:eksperyment"},
    "ME-24": {"LA-12::thm:lin12-cauchy-schwarz"},
    "ME-29": {"PDE-07::def:pde7-derivative", "DT-03::def:distribution19",
              "DG-11::ch:metryka-riemannowska"},
}


class RemainingMeasureCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 22)
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
