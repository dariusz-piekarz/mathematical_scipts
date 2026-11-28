"""Mathematical citation regression: closed S^2 versus boundary CGB.

These assertions guard the reviewed TS^2 applications and the local boundary
argument in DG-14, which replaced the unavailable DG-26 theorem reference.
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

    def test_boundary_formula_uses_local_stokes_and_poincare_hopf_argument(self):
        text = next(DG.glob("14-*.tex")).read_text(encoding="utf-8-sig")
        boundary = text.split(r"\subsection*{Brzeg, niezwartość i nieparzysty wymiar}", 1)[1]
        self.assertNotIn(BOUNDARY, boundary)
        self.assertIn(r"\mathcal B_g=\nu^*\Psi_\nabla", boundary)
        self.assertIn(r"\mathrm d(s^*\Psi_\nabla)=-e_\nabla", boundary)
        self.assertIn(r"\int_{M\setminus\bigcup_j B_j}e_\nabla", boundary)
        self.assertIn(r"\atlasref{TOP-21::ch:poincare-hopf-v11}", boundary)
        self.assertIn(r"\label{eq:chern-gb-brzeg-idea}", text)


if __name__ == "__main__":
    unittest.main()
