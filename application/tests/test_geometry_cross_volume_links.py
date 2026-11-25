"""Regression for geometry, exterior algebras and characteristic classes."""
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
    "DG-03": {"LA-10::thm:lin10-istnienie", "LA-11::thm:lin11-zew-uniwersalna",
              "LA-11::thm:lin11-det-wedge"},
    "DG-04": {"LA-29::thm:lin29-grass-atlas", "LA-30::thm:lin30-cliff-baza",
              "LA-31::def:lin31-struktura-spinowa"},
    "DG-10": {"LA-11::thm:lin11-formy-alt", "TOP-09::thm:de-rham"},
    "DG-17": {"TOP-11::thm:poincare-dualnosc-16", "TOP-13::thm:BG-general-v6"},
    "TOP-09": {"LA-11::thm:lin11-formy-alt", "DG-10::thm:stokes-formy"},
    "TOP-13": {"LA-29::def:lin29-grass-taut"},
    "TOP-17": {"DG-15::thm:transwersalny-przeciwobraz",
               "DG-16::thm:otoczenie-tubularne", "DG-17::thm:euler-thom-16"},
}


class GeometryCrossVolumeLinks(unittest.TestCase):
    def test_canonical_references_and_graph(self):
        required = {(src, lab, lab.split("::", 1)[0])
                    for src, labels in EXPECTED.items() for lab in labels}
        self.assertEqual(len(required), 16)
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
                # Both copies of these original labels must exist, and target
                # entity IDs must belong to the explicitly named chapter.
                for label, owners in [
                    ("thm:de-rham", {"DG-10", "TOP-09"}),
                    ("thm:stokes-formy", {"DG-10", "TOP-09"}),
                    ("thm:poincare-dualnosc-16", {"DG-17", "TOP-11"}),
                ]:
                    actual_owners = {r[0] for r in con.execute(
                        "SELECT document_id FROM label_occurrences WHERE name=?", (label,))}
                    self.assertTrue(owners <= actual_owners)
                for src, lab, dst in required:
                    targets = con.execute(
                        "SELECT e.document_id FROM references_tex r "
                        "JOIN entities e ON e.id=r.target_entity "
                        "WHERE r.source_document=? AND r.target_label=? "
                        "AND r.target_document=?", (src, lab, dst)).fetchall()
                    self.assertTrue(targets, (src, lab, dst))
                    self.assertEqual({r[0] for r in targets}, {dst})
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
