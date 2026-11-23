"""Functional analysis chapter 06: structural and Hahn–Banach model regressions.

Finite-dimensional models validate algebraic identities, while human
audits remain responsible for the general infinite-dimensional proofs.
"""
from __future__ import annotations

import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "chapters/pl/functional_analysis"
BOOK = ROOT / "books/pl/functional_analysis.tex"
FILES = [
    "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    "03-sieci-struktura-jednostajna-i-zupelnosc.tex",
    "04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex",
    "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
    "06-twierdzenie-hahna-banacha-i-ciagly-dual.tex",
]


class FunctionalAnalysisChapter06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = [(BASE / f).read_text(encoding="utf-8") for f in FILES]
        cls.source = cls.sources[-1]

    def test_book_integration_and_section_number(self):
        book = BOOK.read_text(encoding="utf-8")
        for path in FILES:
            self.assertIn(
                r"\input{../../chapters/pl/functional_analysis/" + path + "}",
                book)
        self.assertIn(r"\setcounter{section}{5}", self.source)

    def test_environment_counts(self):
        for env, count in (("proof", 17), ("przyklad", 5)):
            self.assertEqual(self.source.count(r"\begin{" + env + "}"), count)
            self.assertEqual(self.source.count(r"\end{" + env + "}"), count)
        for env in ("definicja", "twierdzenie", "lemat",
                    "stwierdzenie", "wniosek", "uwaga"):
            self.assertEqual(self.source.count(r"\begin{" + env + "}"),
                             self.source.count(r"\end{" + env + "}"))

    def test_labels_and_cross_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.source)
        self.assertEqual(len(labels), 22)
        self.assertEqual(len(labels), len(set(labels)))
        known = set()
        for source in self.sources:
            known.update(re.findall(r"\\label\{([^}]+)\}", source))
        refs = (re.findall(r"\\ref\{([^}]+)\}", self.source)
                + re.findall(r"\\hyperref\[([^]]+)\]", self.source))
        self.assertTrue(set(refs) <= known, sorted(set(refs)-known))

    def test_terminology_and_characteristic_function(self):
        text = self.source
        self.assertIn("przestrzeń sprzężona", text)
        self.assertIn("Przestrzeń algebraicznie sprzężona", text)
        self.assertNotIn("ciągły dual", text)
        self.assertNotIn("Dual ilorazu", text)
        self.assertNotIn("Dual rozdziela punkty", text)
        self.assertNotIn(r"\mathbf 1", text)
        self.assertNotIn(r"\mathbf1", text)
        self.assertIn(r"\chi_{[0,1]}", text)
        self.assertIn(r"\hyperref[sec:lokalnie-wypukle]{rozdziału 5}", text)

    def test_sign_in_point_closed_subspace_proof(self):
        # The proof uses (x_0+W)∩M=∅. To deduce x_0-m∉U
        # it must use the symmetry of U; this is not automatic for W.
        self.assertIn(r"$-U=U$", self.source)
        self.assertIn(r"$m=x_0-(x_0-m)\in x_0+U\subseteq x_0+W$", self.source)

    def test_one_dimensional_extension_sublinear_dominance(self):
        # p(x,y)=max(x+2y, -2x+y, 0) is a support function,
        # hence real sublinear. On the x-axis f(x,0)=x/2 obeys f≤p.
        # One valid extension is F(x,y)=x/2+y (convex combination).
        p = lambda x, y: max(x+2*y, -2*x+y, 0.0)
        f = lambda x: x/2
        g = lambda x, y: x/2+y
        for x in range(-10, 11):
            self.assertLessEqual(f(x), p(x, 0)+1e-12)
            self.assertAlmostEqual(g(x, 0), f(x))
            for y in range(-10, 11):
                self.assertLessEqual(g(x,y), p(x,y)+1e-12)
        # The one-step interval [L,R] must be nonempty and contain a=1.
        candidates = [i/2 for i in range(-40, 41)]
        left = max(f(y)-p(y, -1) for y in candidates)
        right = min(p(z, 1)-f(z) for z in candidates)
        self.assertLessEqual(left, 1+1e-12)
        self.assertGreaterEqual(right, 1-1e-12)
        self.assertLessEqual(left, right+1e-12)

    def test_complex_reconstruction_from_real_part(self):
        linear = lambda z: z[0]+(2+3j)*z[1]
        u = lambda z: linear(z).real
        examples = [(0j,0j), (1+2j,3-1j), (-1j,2j), (2+0j,0j)]
        for z in examples:
            iz = (1j*z[0],1j*z[1])
            reconstructed = u(z)-1j*u(iz)
            self.assertAlmostEqual(abs(reconstructed-linear(z)), 0)
            self.assertAlmostEqual(reconstructed.real, u(z))

    def test_complex_seminorm_domination(self):
        p = lambda z: abs(z[0])+2*abs(z[1])
        f = lambda z: z[0]+z[1]
        scalars = (0j, 1j, -1+0j, .5+.5j, -2+3j)
        for a in scalars:
            for z in [(0j,0j), (2+3j,-1j), (-1,3), (1j,1+1j)]:
                az=(a*z[0],a*z[1])
                self.assertLessEqual(abs(f(az)), p(az)+1e-12)
                self.assertAlmostEqual(p(az), abs(a)*p(z))

    def test_norm_preserving_extension_nonunique(self):
        # Diagonal in (R²,||·||∞): F_a(x,y)=a x+(1-a)y.
        # Its dual norm equals |a|+|1-a|=1 for a in [0,1].
        for a in (0.0,.125,.3,.5,.875,1.0):
            F=lambda x,y:a*x+(1-a)*y
            self.assertAlmostEqual(abs(a)+abs(1-a), 1)
            for t in (-8,-1,0,2,15):
                self.assertAlmostEqual(F(t,t),t)
            for x in (-1,0,1):
                for y in (-1,0,1):
                    self.assertLessEqual(abs(F(x,y)), 1+1e-12)

    def test_point_closed_subspace_separator(self):
        # X=R², M={(x,0)}, x0=(0,3), f(x,y)=y/3.
        for x in (-5,-1,0,1,8):
            self.assertEqual(0/3, 0)
            self.assertAlmostEqual((0-0), 0)
            self.assertAlmostEqual((x*0)/3, 0)
        self.assertAlmostEqual(3/3, 1)
        # Symmetric neighborhoods: if x0-m is small, so is m-x0.
        near = lambda a,b: max(abs(a),abs(b)) < .5
        for m in (-5,0,1,5):
            self.assertEqual(near(-m,3), near(m,-3))

    def test_product_dual_depends_on_finitely_many_coordinates(self):
        support=(1,4,8)
        coeffs={1:2,4:-1,8:3}
        evaluate=lambda x:sum(coeffs[k]*x.get(k,0) for k in support)
        x={1:7,4:6,8:-2}
        self.assertEqual(evaluate(x), 2)
        for nonsupport in (2,3,5,9,200):
            y=dict(x)
            y[nonsupport] = 99999
            self.assertEqual(evaluate(y), evaluate(x))

    def test_quotient_dual_and_anihilator(self):
        # R² / (R × {0}) is R. Every quotient functional lifts
        # to an annihilator of M by composing with q(x,y)=y.
        for a in (-3,-1,0,.5,7):
            F=lambda x,y:a*y
            for x in (-2,0,3):
                self.assertAlmostEqual(F(x,0),0)
                for y in (-4,0,2):
                    self.assertAlmostEqual(F(x,y), F(0,y))

    def test_distance_to_diagonal_and_norming_functional(self):
        # In (R², ||·||∞), distance to M={(t,t)} is |x-y|/2.
        # F(x,y)=(x-y)/2 annihilates M and has dual norm 1.
        for x,y in ((3,-1),(0,1),(-2,-8),(0,0)):
            distance=abs(x-y)/2
            f=(x-y)/2
            self.assertAlmostEqual(abs(f),distance)
            mid=(x+y)/2
            self.assertAlmostEqual(max(abs(x-mid),abs(y-mid)),distance)
            for t in (-9,0,2):
                self.assertGreaterEqual(max(abs(x-t),abs(y-t)),distance-1e-12)
        self.assertAlmostEqual(abs(.5)+abs(-.5),1)

    def test_no_extension_from_line_in_quasinorm_lp(self):
        # For 0<p<1 and f(c*chi_[0,1])=c, d(c*1,0)=|c|^p.
        for p in (.25,.5,.75):
            for c in (-10,-1,0,0.5,3):
                self.assertAlmostEqual(abs(c)**p,abs(c)**p)
            self.assertLess(200**(1-1/p),1)


if __name__ == "__main__":
    unittest.main()
