"""Regression: the two Galois volumes share genuine, resolved graph edges."""
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest

from backend.api import bipartite_graph
from backend.generator import closure
from backend.latex_parser import build_database, parse_document

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "GA-00": {"AA-20"},
    "GA-01": {"AA-20", "AA-21"},
    "GA-02": {"AA-22"},
    "GA-03": {"AA-24"},
    "GA-04": {"AA-24", "AA-36"},
    "GA-05": {"AA-30"},
    "GA-06": {"AA-29", "AA-35"},
    "GA-07": {"AA-43", "AA-44"},
    "GA-08": {"AA-45"},
    "GA-09": {"AA-46"},
}


class CrossVolumeReadingReferencesTest(unittest.TestCase):
    def test_parser_ignores_comments_and_recognizes_real_link(self):
        source = r"""\chapter{Test}
\providecommand{\atlasref}[2]{#2}
% \atlasref{ignored}{Comment}
\atlasref{aa:ch:test}{AA-20: test}
"""
        doc = parse_document(source, "pl/galois_theory/00-test.tex")
        self.assertEqual(
            [(r.command, r.target) for r in doc.references],
            [("atlasref", "aa:ch:test")],
        )

    def test_real_ga_aa_sources_and_graph(self):
        books = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))["books"]
        targets = {m[3:] for values in EXPECTED.values() for m in values}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "pl"
            for book in books:
                if book["id"] not in {"galois_theory", "abstract_algebra"}:
                    continue
                for path in book["chapters"]:
                    p = Path(path)
                    if book["id"] == "abstract_algebra" and p.name.split("-", 1)[0] not in targets:
                        continue
                    dest = root / p.parent.name / p.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / p, dest)
            db = Path(temp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                con.row_factory = sqlite3.Row
                rows = con.execute(
                    "SELECT source_document,target_document,status FROM references_tex "
                    "WHERE command='atlasref'"
                ).fetchall()
                expected = {(s, t) for s, targets in EXPECTED.items() for t in targets}
                self.assertEqual(len(rows), len(expected))
                self.assertTrue(all(r["status"] in {"resolved", "external_resolved", "alias_resolved"} for r in rows))
                self.assertEqual({(r["source_document"], r["target_document"]) for r in rows}, expected)
                for left, right in [
                    ("teoria Galois", "algebra abstrakcyjna"),
                    ("algebra abstrakcyjna", "teoria Galois"),
                ]:
                    for granularity in ("module", "section", "entity"):
                        graph = bipartite_graph(con, left, right, granularity, 1, 250)
                        nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                        pairs = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                        self.assertTrue(expected <= (pairs if left == "teoria Galois" else {(b, a) for a, b in pairs}))
                # Reading links must not force a chapter into a generated script.
                known = {r["id"]: dict(r) for r in con.execute("SELECT id,content FROM documents")}
                chosen = {"GA-00": {"spans": [(0, len(known["GA-00"]["content"]))]}}
                closure(con, chosen, known, 1)
                self.assertNotIn("AA-20", chosen)


    def test_real_alg_aa_section_and_object_graph(self):
        expected_labels = {
            "ALG-00": {"aa:ch:pierscienie": "AA-09", "aa:ch:wielomiany": "AA-11"},
            "ALG-01": {"aa:tw:radical-intersection-primes": "AA-12",
                       "aa:tw:hilbert-basis": "AA-13", "aa:def:algebraic-closure": "AA-21"},
            "ALG-02": {"aa:ch:wielomiany": "AA-11"},
            "ALG-03": {"aa:def:localization": "AA-12",
                       "aa:tw:nakayama-minimal-generators": "AA-14",
                       "aa:prz:integral-cusp-normalization": "AA-40"},
            "ALG-04": {"aa:tw:localization-universal": "AA-12",
                       "aa:ch:modules-introduction": "AA-16",
                       "aa:ch:module-tensor-product": "AA-18",
                       "aa:ch:integral-extensions": "AA-40",
                       "aa:tw:noether-normalization": "AA-38",
                       "aa:def:krull-dimension": "AA-39",
                       "aa:tw:transcendence-degree": "AA-37"},
        }
        target_ids = {m[3:] for labels in expected_labels.values() for m in labels.values()}
        alg_ids = {m[4:] for m in expected_labels}
        books = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))["books"]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "pl"
            for book in books:
                if book["id"] not in {"algebraic_geometry", "abstract_algebra"}:
                    continue
                wanted = alg_ids if book["id"] == "algebraic_geometry" else target_ids
                for path in book["chapters"]:
                    p = Path(path)
                    if p.name.split("-", 1)[0] not in wanted:
                        continue
                    dest = root / p.parent.name / p.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / p, dest)
            db = Path(temp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                con.row_factory = sqlite3.Row
                rows = con.execute(
                    "SELECT r.source_document, r.target_label, r.target_document, r.status,"
                    " s.kind AS source_kind, t.kind AS target_kind"
                    " FROM references_tex r LEFT JOIN entities s ON r.source_entity=s.id"
                    " LEFT JOIN entities t ON r.target_entity=t.id"
                    " WHERE r.command='atlasref' AND r.source_document LIKE 'ALG-%'"
                ).fetchall()
                expected = {(s, lab, dst) for s, labels in expected_labels.items()
                            for lab, dst in labels.items()}
                found = {(r["source_document"], r["target_label"], r["target_document"])
                         for r in rows}
                self.assertTrue(expected <= found)
                for row in rows:
                    if (row["source_document"], row["target_label"], row["target_document"]) in expected:
                        self.assertIn(row["status"], {"resolved", "external_resolved", "alias_resolved"})
                        self.assertEqual(row["source_kind"], "section")
                        self.assertIsNotNone(row["target_kind"])
                pairs = {(s, dst) for s, _, dst in expected}
                for left, right in [("geometria algebraiczna", "algebra abstrakcyjna"),
                                    ("algebra abstrakcyjna", "geometria algebraiczna")]:
                    for granularity in ("module", "section", "entity"):
                        graph = bipartite_graph(con, left, right, granularity, 1, 250)
                        nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                        actual = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                        if left == "algebra abstrakcyjna":
                            actual = {(b, a) for a, b in actual}
                        self.assertTrue(pairs <= actual)


if __name__ == "__main__":
    unittest.main()
