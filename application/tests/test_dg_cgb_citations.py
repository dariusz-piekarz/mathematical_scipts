"""Mathematical citation regression: closed S^2 versus boundary CGB.

These assertions guard the three reviewed TS^2 applications while preserving
the genuine boundary theorem reference in DG-14. No rewriting occurs here.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
CLOSED = r"\ref{thm:chern-gauss-bonnet}"
BOUNDARY = r"\ref{thm:CGB-boundary-26}"


class GaussBonnetCitationTests(unittest.TestCase):
    def test_closed_theorem_is_defined_in_dg14(self):
        text = next(DG.glob("14-*.tex")).read_text(encoding="utf-8-sig")
        self.assertIn(r"\label{thm:chern-gauss-bonnet}", text)
        self.assertIn(r"\emph{bez brzegu}", text)

    def test_closed_sphere_examples_cite_closed_theorem(self):
        cases = {
            "16-*.tex": (r"\nu(\Delta,S^2\times S^2)", 1),
            "17-*.tex": (r"\begin{przyklad}[Zerowe klasy", 2),
        }
        for pattern, (context, expected_count) in cases.items():
            with self.subTest(pattern=pattern):
                text = next(DG.glob(pattern)).read_text(encoding="utf-8-sig")
                self.assertIn(context, text)
                self.assertEqual(text.count(BOUNDARY), 0)
                self.assertGreaterEqual(text.count(CLOSED), expected_count)

    def test_boundary_formula_still_cites_boundary_theorem(self):
        text = next(DG.glob("14-*.tex")).read_text(encoding="utf-8-sig")
        self.assertIn(BOUNDARY, text)
        self.assertIn(r"\label{eq:chern-gb-brzeg-idea}", text)


if __name__ == "__main__":
    unittest.main()
