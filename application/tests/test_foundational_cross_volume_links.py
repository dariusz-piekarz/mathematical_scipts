"""Check the foundational cross-volume references against canonical sources."""
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
    "TOP-01": {"GT-04::thm:topog-iloraz-uniwersalnosc", "KAT-07::def:pushout"},
    "TOP-02": {"AA-02::aa:tw:izo-pierwsze", "AA-03::aa:tw:orbita-stabilizator",
               "AA-07::aa:tw:presentation-universal", "AA-09::aa:tw:ring-quotient",
               "AA-16::aa:tw:modules-first-isomorphism", "AA-18::aa:tw:tensor-universal",
               "AA-16::aa:def:modules-projective"},
    "TOP-03": {"AA-16::aa:def:modules-sub-hom", "AA-16::aa:def:modules-exact",
               "AA-16::aa:tw:modules-splitting", "KAT-03::def:funktor"},
    "TOP-04": {"KAT-03::def:funktor", "AA-07::aa:def:presentation", "KAT-07::def:pushout"},
    "TOP-08": {"KAT-03::def:hom-funktory", "AA-18::aa:tw:tensor-right-exact"},
    "AA-02": {"LST-05::thm:lxv-quotient-factorization"},
    "AA-07": {"KAT-14::def:adjunction"},
    "AA-16": {"TOP-03::thm:les-homologia", "KAT-06::cat:ex:module-indexed"},
    "AA-18": {"KAT-14::def:adjunction"},
    "MOD-21": {"AA-02::aa:def:hom", "KAT-02::def:mono-epi"},
}


class FoundationalCrossVolumeLinks(unittest.TestCase):
    def test_canonical_reference_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 25)
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
                # Both source directions can occur within a single domain pair.
                domain_pairs = {tuple(sorted((domains[s], domains[t]))) for s, _, t in required}
                for left, right in sorted(domain_pairs):
                    pairs = {(s, t) if domains[s] == left else (t, s)
                             for s, _, t in required
                             if {domains[s], domains[t]} == {left, right}}
                    for granularity in ("module", "section", "entity"):
                        for a, b in ((left, right), (right, left)):
                            graph = bipartite_graph(con, a, b, granularity, 1, 250)
                            nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                            actual = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                            if a != left:
                                actual = {(t, s) for s, t in actual}
                            self.assertFalse(pairs - actual, (a, b, granularity, pairs - actual))
