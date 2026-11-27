"""Canonical Galois coverage after retirement of the standalone book."""
import json
import re
from pathlib import Path
import sqlite3
from contextlib import closing
import tempfile
import unittest

from backend.latex_parser import build_database, module_id


class GaloisGraphTest(unittest.TestCase):
    def test_migrated_equation_labels_do_not_conflict_in_amsmath(self):
        repository = Path(__file__).resolve().parents[2]
        folder = repository / "chapters/pl/abstract_algebra"
        aliases = {
            "44": (("aa:eq:liouville-form", "eq:liouville"),),
            "45": (("aa:eq:hyperexp-ode", "eq:hyperexp"),
                   ("aa:eq:elliptic-liouville-form", "eq:elliptic-liouville")),
        }
        for chapter, pairs in aliases.items():
            source = next(folder.glob(chapter + "-*.tex")).read_text(encoding="utf-8")
            equations = re.findall(r"\\begin\{equation\}(.*?)\\end\{equation\}",
                                   source, re.S)
            for equation in equations:
                self.assertLessEqual(len(re.findall(r"\\label\{", equation)), 1)
            for canonical, historical in pairs:
                self.assertEqual(source.count(r"\label{" + canonical + "}"), 1)
                self.assertEqual(source.count(r"\label{" + historical + "}"), 1)
                equation = next(e for e in equations if
                                r"\label{" + canonical + "}" in e)
                tail = source.split(equation + r"\end{equation}", 1)[1]
                self.assertIn(r"\label{" + historical + "}",
                              tail.split(r"\endgroup", 1)[0])
                self.assertIn(r"\protected@edef\@currentlabel{\p@equation\theequation}",
                              tail.split(r"\endgroup", 1)[0])

    def test_retired_galois_book_and_canonical_targets(self):
        repository = Path(__file__).resolve().parents[2]
        canonical = repository / "chapters" / "pl"
        catalog = json.loads((repository / "catalog/books.json").read_text(encoding="utf-8"))
        self.assertNotIn("galois_theory", {b["id"] for b in catalog["books"]})
        self.assertFalse((canonical / "galois_theory").exists())
        self.assertFalse((repository / "books/pl/galois_theory.tex").exists())
        expected = (
            ("GA-00", "AA-20", "aa:ch:field-extensions"),
            ("GA-01", "AA-20", "aa:ch:field-extensions"),
            ("GA-01", "AA-21", "aa:ch:embeddings-normal-separable"),
            ("GA-02", "AA-22", "aa:ch:galois-correspondence"),
            ("GA-03", "AA-24", "aa:ch:radical-solvability"),
            ("GA-04", "AA-36", "aa:ch:generic-polynomial"),
            ("GA-04", "AA-24", "aa:ch:radical-solvability"),
            ("GA-05", "AA-30", "aa:ch:constructibility"),
            ("GA-06", "AA-29", "aa:ch:finite-fields-structure"),
            ("GA-06", "AA-35", "aa:ch:frobenius-reduction"),
            ("GA-07", "AA-43", "aa:ch:differential-fields"),
            ("GA-07", "AA-44", "aa:ch:liouville-elementary-integration"),
            ("GA-08", "AA-45", "aa:ch:nonelementary-integrals"),
            ("GA-09", "AA-46", "aa:ch:picard-vessiot"),
        )
        targets = {(target, label) for _, target, label in expected}
        targets |= {
            ("AA-43", "eq:trace-norm"), ("AA-44", "eq:liouville"),
            ("AA-45", "eq:hyperexp"), ("AA-45", "eq:elliptic-liouville"),
            ("AA-46", "eq:airy-riccati"),
            ("AA-35", "aa:lem:hensel-simple"),
        }
        needed = {target for target, _ in targets}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            book = next(b for b in catalog["books"] if b["id"] == "abstract_algebra")
            for relative in book["chapters"]:
                path = repository / relative
                if module_id(path) in needed:
                    dest = root / path.relative_to(canonical)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(path.read_bytes())
            db = Path(tmp) / "index.db"
            build_database(root, db, recursive=True)
            with closing(sqlite3.connect(db)) as con:
                for target, label in targets:
                    with self.subTest(target=target, label=label):
                        rows = con.execute(
                            "SELECT document_id FROM label_occurrences WHERE name=?",
                            (label,),
                        ).fetchall()
                        self.assertEqual(rows, [(target,)])
                self.assertEqual(con.execute(
                    "SELECT id FROM documents WHERE id LIKE 'GA-%'"
                ).fetchall(), [])
