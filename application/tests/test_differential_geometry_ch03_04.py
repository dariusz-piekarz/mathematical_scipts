"""Regression checks for the audit of DG-03/04 (tensor algebra, Grassmannians, spin)."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
BOOK = ROOT / "books" / "pl" / "differential_geometry_and_topology.tex"


class DifferentialGeometryThreeFourAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = {
            f"{i:02d}": next(DIR.glob(f"{i:02d}-*.tex"))
            for i in range(1, 6)
        }
        cls.text = {
            key: path.read_text(encoding="utf-8-sig")
            for key, path in cls.files.items()
        }

    def test_book_includes_both_audited_chapters(self):
        book = BOOK.read_text(encoding="utf-8-sig")
        for key in ("03", "04"):
            with self.subTest(chapter=key):
                name = self.files[key].name
                self.assertIn(
                    r"\input{../../chapters/pl/differential_geometry_and_topology/"
                    + name + "}", book
                )

    def test_labels_unique_and_all_references_resolve(self):
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}",
            "\n".join(self.text.values()),
        )
        self.assertEqual(len(labels), len(set(labels)))
        known = set(labels)
        for key in ("03", "04"):
            refs = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.text[key],
            )
            self.assertGreater(len(refs), 20)
            self.assertFalse(set(refs) - known, set(refs) - known)

    def test_balanced_environments_and_self_contained_illustrations(self):
        for key, min_figures in (("03", 8), ("04", 6)):
            src = self.text[key]
            opens = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            closes = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(opens, closes)
            self.assertGreaterEqual(opens["figure"], min_figures)
            self.assertGreaterEqual(opens["tikzpicture"], min_figures)
            for command in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_wedge_product_normalization_on_three_covectors(self):
        src = self.text["03"]
        self.assertIn(r"\label{prz:normalizacja-wedge-form}", src)
        self.assertIn(r"\label{eq:wedge-alt-forms}", src)

        def alpha(i, j):
            return 1 if (i, j) == (0, 1) else (
                -1 if (i, j) == (1, 0) else 0
            )

        def beta(k):
            return int(k == 2)

        def parity(p):
            inversions = sum(
                p[i] > p[j] for i in range(3) for j in range(i + 1, 3)
            )
            return (-1) ** inversions

        raw_sum = sum(
            parity(p) * alpha(p[0], p[1]) * beta(p[2])
            for p in permutations((0, 1, 2))
        )
        self.assertEqual(raw_sum, 2)
        self.assertEqual(raw_sum / 2, 1)   # 1/(2!1!)
        self.assertEqual(raw_sum / 6, 1 / 3)  # normalized Alt_3

    def test_cech_coboundary_squares_to_zero(self):
        src = self.text["04"]
        self.assertIn(r"H^2(\mathcal U;\Z/2)", src)
        self.assertIn(r"\delta^2=0", src)
        self.assertIn(r"w_2(E)=0", src)

        vertices = range(4)
        edges = list(combinations(vertices, 2))
        triangles = list(combinations(vertices, 3))
        for assignments in product((0, 1), repeat=len(edges)):
            b = dict(zip(edges, assignments))
            c = {
                (i, j, k):
                (b[i, j] + b[i, k] + b[j, k]) % 2
                for (i, j, k) in triangles
            }
            self.assertEqual(sum(c[t] for t in triangles) % 2, 0)


if __name__ == "__main__":
    unittest.main()
