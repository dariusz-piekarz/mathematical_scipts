"""Regression: cross-volume reading links and graph resolution."""
import json
from pathlib import Path
import shutil
import sqlite3
from contextlib import closing
import tempfile
import unittest
from unittest.mock import patch

from backend.api import bipartite_graph, label_detail
from fastapi import HTTPException
from backend.generator import closure
from backend.label_registry import Owner, resolve
from backend.latex_parser import build_database, parse_document

ROOT = Path(__file__).resolve().parents[2]


class CrossVolumeReadingReferencesTest(unittest.TestCase):
    def test_real_birkhoff_fa_me_reading_links(self):
        # Build a small real-source index rather than testing only TeX strings.
        files = (
            ROOT / "chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex",
            ROOT / "chapters/pl/measure_theory/30-miary-wektorowe-calka-bochnera-i-wlasnosc-radona-nikodyma.tex",
        )
        expected = {
            ("FA-15B", "ME-30::sec:birkhoff-30"),
            ("FA-15B", "ME-30::thm:birkhoff-measure-30"),
            ("FA-15B", "ME-30::thm:birkhoff-seminorm-30"),
            ("ME-30", "FA-15B::sec:birkhoff15b"),
        }
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "pl"
            for path in files:
                dest = root / path.parent.name / path.name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, dest)
            db = Path(temp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                con.row_factory = sqlite3.Row
                rows = con.execute(
                    "SELECT source_document,target_label,target_document,"
                    "status,target_entity FROM references_tex "
                    "WHERE command='atlasref'"
                ).fetchall()
                actual = set()
                for row in rows:
                    key = (row["source_document"], row["target_label"])
                    if key not in expected:
                        continue
                    actual.add(key)
                    self.assertEqual(row["target_document"], key[1].split("::")[0])
                    self.assertIn(row["status"],
                                  {"resolved", "external_resolved", "alias_resolved"})
                    self.assertIsNotNone(row["target_entity"])
                self.assertEqual(actual, expected)
                with patch("backend.api.db_connection", return_value=con):
                    for source, target in sorted(expected):
                        owner, label = target.split("::", 1)
                        detail = label_detail(target, source)
                        self.assertEqual(detail["document_id"], owner)
                        self.assertEqual(detail["canonical_label"], label)
                # Reading links should remain navigation, not script dependencies.
                known = {row["id"]: dict(row) for row in con.execute(
                    "SELECT id,content FROM documents")}
                for source, target in (("FA-15B", "ME-30"), ("ME-30", "FA-15B")):
                    chosen = {source: {"spans": [(0, len(known[source]["content"]))]}}
                    closure(con, chosen, known, 1)
                    self.assertNotIn(target, chosen)

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
            with closing(sqlite3.connect(db)) as con, con:
                con.row_factory = sqlite3.Row
                rows = con.execute(
                    "SELECT r.source_document, r.target_label, r.target_document, r.status,"
                    " s.kind AS source_kind, t.kind AS target_kind"
                    " FROM references_tex r LEFT JOIN entities s ON r.source_entity=s.id"
                    " LEFT JOIN entities t ON r.target_entity=t.id"
                    " WHERE r.command='atlasref' AND r.source_document LIKE 'ALG-%'"
                ).fetchall()
                expected = {(s, dst + "::" + lab, dst) for s, labels in expected_labels.items()
                            for lab, dst in labels.items()}
                found = {(r["source_document"], r["target_label"], r["target_document"])
                         for r in rows}
                self.assertFalse(expected - found, expected - found)
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
            with closing(sqlite3.connect(db)) as con, con:
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


    def test_real_la_aa_module_and_tensor_links(self):
        expected = {
            "LA-01": {"AA-16::aa:tw:modules-free-universal"},
            "LA-02": {"AA-16::aa:def:modules-direct-sum",
                      "AA-16::aa:tw:modules-first-isomorphism"},
            "LA-03": {"AA-16::aa:tw:modules-first-isomorphism"},
            "LA-10": {"AA-18::aa:tw:tensor-universal",
                      "AA-18::aa:st:tensor-vspace-dimension",
                      "AA-18::aa:tw:tensor-right-exact"},
            "LA-19": {"AA-17::aa:tw:pid-structure",
                      "AA-17::aa:tw:smith-normal-form"},
            "LA-20": {"AA-17::aa:tw:pid-structure"},
        }
        modules = set(expected) | {lab.split("::", 1)[0]
                                   for labels in expected.values() for lab in labels}
        prefixes = {"linear_algebra": "LA", "abstract_algebra": "AA"}
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
            with closing(sqlite3.connect(db)) as con, con:
                con.row_factory = sqlite3.Row
                required = {(src, lab, lab.split("::", 1)[0])
                            for src, labels in expected.items() for lab in labels}
                actual = {(r["source_document"], r["target_label"], r["target_document"])
                          for r in con.execute(
                              "SELECT source_document,target_label,target_document FROM references_tex "
                              "WHERE command='atlasref' AND status='external_resolved'")}
                self.assertEqual(len(required), 10)
                self.assertTrue(required <= actual)
                for granularity in ("module", "section", "entity"):
                    graph = bipartite_graph(con, "algebra liniowa", "algebra abstrakcyjna",
                                            granularity, 1, 250)
                    nodes = {n["id"]: n["module"] for n in graph["nodes"]}
                    edges = {(nodes[e["source"]], nodes[e["target"]]) for e in graph["edges"]}
                    self.assertTrue({(src, dst) for src, _, dst in required} <= edges)


if __name__ == "__main__":
    unittest.main()
