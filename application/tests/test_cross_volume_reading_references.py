"""Regression: the two Galois volumes share genuine, resolved graph edges."""
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from backend.api import bipartite_graph, label_detail
from fastapi import HTTPException
from backend.generator import closure
from backend.label_registry import Owner, resolve
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


    def test_qualified_reference_never_guesses_duplicate_owner(self):
        owners = [Owner("TOP-11", "thm:example", "top"),
                  Owner("DG-17", "thm:example", "dg")]
        decision = resolve("ALG-10", "TOP-11::thm:example", owners)
        self.assertEqual(decision.status, "external_resolved")
        self.assertEqual(decision.owner.entity_id, "top")
        missing = resolve("ALG-10", "TOP-12::thm:example", owners)
        self.assertEqual(missing.status, "missing")
        self.assertIsNone(missing.owner)
        duplicate = resolve("ALG-10", "TOP-11::thm:example", owners + [owners[0]])
        self.assertEqual(duplicate.status, "ambiguous")
        self.assertIsNone(duplicate.owner)
        self.assertEqual(resolve("ALG-10", "thm:example", owners).status, "ambiguous")

    def test_real_advanced_alg_graph_qualified_targets(self):
        expected = {
            "ALG-05": {"AA-40::aa:prz:integral-cusp-normalization",
                       "AA-18::aa:def:flat-module",
                       "TOP-28::thm:xvii-blowup-general"},
            "ALG-06": {"TOP-11::thm:przeciecie-kubek-16",
                       "TOP-28::thm:xvii-canonical",
                       "TOP-28::thm:xvii-hodge-index"},
            "ALG-07": {"TOP-11::thm:przeciecie-kubek-16",
                       "TOP-11::sec:klasy-char-16",
                       "TOP-28::ch:xvii-topologia-odmian"},
            "ALG-08": {"AA-37::aa:tw:transcendence-degree",
                       "TOP-11::thm:forma-przeciecia-16",
                       "TOP-28::thm:xvii-blowup-general"},
            "ALG-09": {"TOP-23::def:sheaf-v12",
                       "TOP-23::def:sheaf-cohom-v12",
                       "TOP-25::thm:kahler-hodge-xiv"},
            "ALG-10": {"TOP-09::thm:de-rham",
                       "TOP-11::thm:poincare-dualnosc-16",
                       "TOP-28::ch:xvii-topologia-odmian",
                       "TOP-28::thm:xvii-blowup-general",
                       "TOP-28::thm:xvii-hard-lefschetz",
                       "TOP-25::def:nearby-vanishing-xiv",
                       "TOP-25::thm:picard-lefschetz-xiv"},
        }
        modules = set(expected) | {lab.split("::", 1)[0]
                                   for labels in expected.values() for lab in labels}
        prefixes = {"algebraic_geometry": "ALG", "abstract_algebra": "AA",
                    "algebraic_topology": "TOP"}
        books = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))["books"]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "pl"
            for book in books:
                prefix = prefixes.get(book["id"])
                if prefix is None:
                    continue
                for path in book["chapters"]:
                    p = Path(path)
                    if prefix + "-" + p.name.split("-", 1)[0] not in modules:
                        continue
                    dest = root / p.parent.name / p.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / p, dest)
            db = Path(temp) / "index.db"
            build_database(root, db, recursive=True)
            with sqlite3.connect(db) as con:
                con.row_factory = sqlite3.Row
                rows = con.execute(
                    "SELECT r.source_document,r.target_label,r.target_document,r.status,"
                    " s.kind AS source_kind,t.kind AS target_kind"
                    " FROM references_tex r LEFT JOIN entities s ON r.source_entity=s.id"
                    " LEFT JOIN entities t ON r.target_entity=t.id"
                    " WHERE r.command='atlasref' AND r.source_document LIKE 'ALG-%'"
                ).fetchall()
                required = {(src, lab, lab.split("::", 1)[0])
                            for src, labels in expected.items() for lab in labels}
                actual = {(r["source_document"], r["target_label"], r["target_document"])
                          for r in rows}
                self.assertEqual(len(required), 22)
                with patch("backend.api.db_connection", return_value=con):
                    for source in (None, "ALG-10"):
                        detail = label_detail("TOP-11::thm:poincare-dualnosc-16", source)
                        self.assertEqual(detail["document_id"], "TOP-11")
                        self.assertEqual(detail["canonical_label"], "thm:poincare-dualnosc-16")
                    with self.assertRaises(HTTPException) as error:
                        label_detail("TOP-12::thm:poincare-dualnosc-16", "ALG-10")
                    self.assertEqual(error.exception.status_code, 404)
                self.assertTrue(required <= actual)
                for r in rows:
                    if (r["source_document"], r["target_label"], r["target_document"]) in required:
                        self.assertEqual(r["status"], "external_resolved")
                        self.assertIn(r["source_kind"], {"section", "subsection"})
                        self.assertIsNotNone(r["target_kind"])
                for prefix, domain in [("AA", "algebra abstrakcyjna"),
                                       ("TOP", "topologia algebraiczna")]:
                    pairs = {(src, dst) for src, _, dst in required
                             if dst.startswith(prefix + "-")}
                    for left, right in [("geometria algebraiczna", domain),
                                        (domain, "geometria algebraiczna")]:
                        for granularity in ("module", "section", "entity"):
                            graph = bipartite_graph(con, left, right, granularity, 1, 250)
                            nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                            edges = {(nodes[e["source"]], nodes[e["target"]])
                                     for e in graph["edges"]}
                            if left == domain:
                                edges = {(b, a) for a, b in edges}
                            self.assertTrue(pairs <= edges)


if __name__ == "__main__":
    unittest.main()
