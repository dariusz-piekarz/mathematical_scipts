"""Real-source regression for priority FA, GT, LST and LA chapter links."""
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
    "FA-02": {"GT-04::thm:topog-iloraz-uniwersalnosc",
              "LST-05::thm:lxv-quotient-factorization", "GT-04::ch:topog-konstrukcje"},
    "FA-03": {"GT-06::def:topog-siec-granica", "GT-06::thm:topog-sieci-filtry",
              "GT-12::def:topog-jednostajne-struktura",
              "GT-13::thm:topog-uzupelnienia-filtry-sieci",
              "GT-13::thm:topog-uzupelnienia-uniwersalnosc"},
    "FA-06": {"LST-26::thm:choice-zorn"},
    "FA-09": {"GT-07::thm:topog-tychonoff-iloczyny", "GT-07::thm:topog-zwartosc-sieci"},
    "FA-11": {"GT-11::thm:topog-baire-metryczne", "GT-11::def:topog-baire-zupelna-metryzowalnosc"},
    "FA-13": {"LA-12::thm:lin12-cauchy-schwarz", "LA-12::thm:lin12-riesz"},
    "DT-09": {"AA-18::aa:tw:tensor-universal"},
    "FA-27": {"LST-26::thm:choice-hamel-basis"},
    "LA-01": {"LST-26::thm:choice-hamel-basis"},
    "LA-17": {"AA-17::aa:tw:pid-structure"},
    "LA-21": {"AA-16::aa:def:modules-sub-hom"},
    "GT-04": {"LST-05::thm:lxv-quotient-factorization"},
    "GT-07": {"LST-26::thm:choice-zorn"},
}


class PriorityCrossVolumeLinks(unittest.TestCase):
    def test_real_links_resolve_and_graph_is_bidirectional(self):
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
                for left, right in sorted({(domains[s], domains[t]) for s, _, t in required}):
                    pairs = {(s, t) for s, _, t in required
                             if domains[s] == left and domains[t] == right}
                    for granularity in ("module", "section", "entity"):
                        for a, b in ((left, right), (right, left)):
                            graph = bipartite_graph(con, a, b, granularity, 1, 250)
                            nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                            actual = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                            if a != left:
                                actual = {(t, s) for s, t in actual}
                            self.assertFalse(pairs - actual, (a, b, granularity, pairs - actual))
