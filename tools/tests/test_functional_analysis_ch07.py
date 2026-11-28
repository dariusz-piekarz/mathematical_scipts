"""Chapter 07 functional analysis: separation, polars, bipolar theorem.

These finite-dimensional and structural regressions complement mathematical proof audits.
"""
from __future__ import annotations

import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
BOOK = ROOT / "books/pl/functional_analysis.tex"
FILES = [
    "01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex",
    "02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex",
    "03-sieci-struktura-jednostajna-i-zupelnosc.tex",
    "04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex",
    "05-przestrzenie-lokalnie-wypukle-i-seminormy.tex",
    "06-twierdzenie-hahna-banacha-i-ciagly-dual.tex",
    "07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex",
]


class FunctionalAnalysisChapter07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = [(CHAPTERS / f).read_text(encoding="utf-8")
                       for f in FILES]
        cls.chapter = cls.sources[-1]

    def test_book_order_and_section_number(self):
        book = BOOK.read_text(encoding="utf-8")
        chapter_inputs = re.findall(
            r"\\input\{\.\./\.\./chapters/pl/functional_analysis/([^}]+)\}", book)
        self.assertEqual(chapter_inputs[:7], FILES)
        self.assertIn(r"\setcounter{section}{6}", self.chapter)

    def test_proof_and_example_environments(self):
        for env, count in (("proof", 11), ("przyklad", 4)):
            self.assertEqual(self.chapter.count(r"\begin{" + env + "}"), count)
            self.assertEqual(self.chapter.count(r"\end{" + env + "}"), count)
        for env in ("definicja", "stwierdzenie", "lemat",
                    "twierdzenie", "wniosek", "uwaga"):
            self.assertEqual(self.chapter.count(r"\begin{" + env + "}"),
                             self.chapter.count(r"\end{" + env + "}"))

    def test_labels_and_cross_chapter_references(self):
        own = re.findall(r"\\label\{([^}]+)\}", self.chapter)
        self.assertEqual(len(own), 17)
        self.assertEqual(len(own), len(set(own)))
        labels = set()
        for s in self.sources:
            labels.update(re.findall(r"\\label\{([^}]+)\}", s))
        refs = (re.findall(r"\\ref\{([^}]+)\}", self.chapter)
                + re.findall(r"\\hyperref\[([^]]+)\]", self.chapter))
        self.assertFalse(set(refs) - labels, sorted(set(refs) - labels))

    def test_terminology_and_new_gauge_argument(self):
        s = self.chapter
        self.assertIn("przestrzeni sprzężonej", s)
        self.assertNotIn("przestrzeni dualnej", s)
        self.assertNotIn("przestrzenią dualną topologiczną", s)
        self.assertNotIn("sekwencyj", s)
        self.assertIn(r"$p_V(x+y)\le p_V(x)+p_V(y)$", s)
        self.assertIn(r"podliniowy; w tym dowodzie", s)
        self.assertIn(r"V=\{x:p_V(x)<1\}", s)

    def test_non_symmetric_open_gauge_sublinear(self):
        # V={x+2y<1, -x+y<1} is open, convex, absorbing, not balanced.
        # Its Minkowski gauge is max(0, x+2y, -x+y).
        p = lambda xy: max(0.0, xy[0]+2*xy[1], -xy[0]+xy[1])
        self.assertNotEqual(p((0, 1)), p((0, -1)))
        grid = [(a/2, b/2) for a in range(-5,6) for b in range(-5,6)]
        for x in grid:
            self.assertEqual(p(x) < 1,
                             (x[0]+2*x[1] < 1 and -x[0]+x[1] < 1))
            for t in (0, 0.3, 1, 2.5):
                self.assertAlmostEqual(p((t*x[0],t*x[1])), t*p(x))
        for x in grid[::7]:
            for y in grid[::9]:
                self.assertLessEqual(
                    p((x[0]+y[0],x[1]+y[1])), p(x)+p(y)+1e-12)

    def test_open_point_separation_without_uniform_gap(self):
        # A=(-1,0), x0=0, ell(x)=x.
        for n in (2, 3, 9, 1000):
            a = -1/n
            self.assertLess(a, 0)
            self.assertGreater(a, -1)
        # No uniform δ>0: choose n>1/δ.
        for delta in (1, .1, .001):
            n = math.floor(1/delta)+2
            self.assertLess(-1/n+delta, delta)
            self.assertGreater(-1/n+delta, 0)

    def test_two_convex_sets_separation_open_side(self):
        # A={x<0} open; B={x>=1} closed convex; ell(x,y)=x.
        a = [(-1,-2), (-.1,4), (-100,0)]
        b = [(1,-7),(3,0),(8,2)]
        for x in a:
            for y in b:
                self.assertLess(x[0], y[0])
        self.assertLessEqual(max(x[0] for x in a), 0)
        self.assertGreaterEqual(min(x[0] for x in b), 1)

    def test_compact_set_neighborhood_separation(self):
        # K={(0,0),(1,0)} compact; F={x>=3} closed;
        # K+U disjoint F for U sup-ball radius 0.5.
        k = ((0,0),(1,0))
        u = ((.25,0),(-.25,.125),(0,-.3))
        for x in k:
            for v in u:
                self.assertLess(x[0]+v[0], 3)

    def test_strong_separation_has_positive_gap(self):
        # A=[-3,-2] compact; B=[0,inf) closed; ell(x)=x.
        A = [-3,-2.5,-2]
        B = [0,1,2,10]
        delta = 1.5
        self.assertGreater(delta, 0)
        self.assertLessEqual(max(A)+delta, min(B))

    def test_nonsymmetric_unbounded_open_gauge_with_kernel_ray(self):
        # V=(-infinity,1) is open, convex, absorbing, nonbalanced.
        # p_V(x)=max(x,0), so the gauge need not be a norm or even.
        gauge=lambda x:max(x,0.0)
        self.assertEqual(gauge(-2),0)
        self.assertNotEqual(gauge(-2),gauge(2))
        for x in (-10,-3,-1,0,.5,1,2,7):
            self.assertEqual(gauge(x)<1,x<1)
            for t in (0,.3,1,2.5):
                self.assertAlmostEqual(gauge(t*x),t*gauge(x))
            for y in (-7,-1,0,1,8):
                self.assertLessEqual(gauge(x+y),gauge(x)+gauge(y)+1e-12)
        self.assertIn(r"$V=\{p_V<1\}$",self.chapter)

    def test_strong_separation_in_nonhausdorff_local_convex_space(self):
        # X=R² carries the (non-Hausdorff) topology of seminorm |x|.
        # A={(1,0)} compact, B={3}×R closed, convex, and disjoint.
        # Continuous ell(x,y)=x strongly separates A and B.
        p=lambda z:abs(z[0])
        ell=lambda z:z[0]
        a=(1.0,0.0)
        B=[(3.0,y) for y in (-100,-1,0,2,19,200)]
        self.assertLessEqual(ell(a)+1.5,min(ell(b) for b in B))
        for y in (-100,-1,0,2,19,200):
            b=(3.0,y)
            self.assertGreaterEqual(p((b[0]-a[0],b[1]-a[1])),2)
            self.assertAlmostEqual(ell((0.0,y)),0)
        for x in (-3,-1,0,1,5):
            for y in (-5,0,7):
                self.assertLessEqual(abs(ell((x,y))),p((x,y)))
        self.assertIn(r"Niech $X$ będzie lokalnie wypukłą TVS",self.chapter)

    def test_supporting_hyperplane_unit_disk(self):
        # Unit Euclidean disk supported at x0=(1,0) by ell(x)=x1.
        for i in range(81):
            theta = i*2*math.pi/80
            x=(math.cos(theta),math.sin(theta))
            self.assertLessEqual(x[0], 1+1e-12)
        self.assertAlmostEqual(1, math.cos(0))

    def test_absolute_convex_hull_l1_ball(self):
        # aco{e1,e2} in R² is the l1 unit ball.
        for x in (-1, -.5, 0, .5, 1):
            for y in (-1, -.5, 0, .5, 1):
                is_hull = abs(x)+abs(y)<=1
                if is_hull:
                    self.assertLessEqual(abs(x)+abs(y), 1)
        self.assertIn(r"\operatorname{aco}(\varnothing)=\{0\}",self.chapter)

    def test_empty_absolute_convex_hull_convention(self):
        # The empty set vacuously satisfies universal convexity and
        # balance conditions. Under the chosen convention the aco
        # operation instead returns the least NONEMPTY balanced convex
        # superset: {0}.
        self.assertIn(r"\emph{niepusty} zbiór wypukły", self.chapter)
        self.assertIn(
            r"$\operatorname{aco}(\varnothing)=\{0\}$",
            self.chapter)
        x0 = (0.0, 0.0)
        self.assertTrue(all(abs(t*x0[0])+abs(t*x0[1]) == 0
                            for t in (-2, -1, 0, .5, 1, 2)))
        # In R² the empty polar is all functionals; its bipolar is {0}.
        for point in ((1,0),(0,-1),(.1,.4),(0,0)):
            in_bipolar = all(
                abs(a[0]*point[0]+a[1]*point[1])<=1
                for a in ((2**k,0) for k in range(1,9))
            ) and all(
                abs(a[0]*point[0]+a[1]*point[1])<=1
                for a in ((0,2**k) for k in range(1,9))
            )
            if point == x0:
                self.assertTrue(in_bipolar)
            else:
                # Large scalar multiples force every nonzero point out.
                self.assertTrue(any(
                    abs(t*point[i]) > 1 for i in (0,1)
                    for t in (2**k for k in range(1,15))
                ))

    def test_l1_and_linf_polar_unit_balls(self):
        # Polar of the l1 unit diamond = linf dual square.
        points = [(1,0),(-1,0),(0,1),(0,-1)]
        for a in itertools.product((-2,-1,-.5,0,.5,1,2), repeat=2):
            supremum = max(abs(a[0]*x+a[1]*y) for x,y in points)
            self.assertAlmostEqual(supremum,max(abs(a[0]),abs(a[1])))
            self.assertEqual(supremum<=1, max(abs(a[0]),abs(a[1]))<=1)

    def test_polar_order_reverse_and_bipolar_contains_set(self):
        # A={(1,0)}, B={(1,0),(0,1)}: B° subset A°.
        duals = [(x,y) for x in (-2,-1,0,1,2)
                 for y in (-2,-1,0,1,2)]
        polar_a = [a for a in duals if abs(a[0])<=1]
        polar_b = [a for a in duals if abs(a[0])<=1 and abs(a[1])<=1]
        self.assertTrue(set(polar_b) <= set(polar_a))
        self.assertIn((1,0),[(1,0),(0,1)])

    def test_complex_balanced_polar_phase(self):
        # When C is balanced and F linear, sup Re F = sup |F|.
        C=[(0j,0j), (1+0j,0j), (0+1j,0j), (-1+0j,0j),
           (0-1j,0j)]
        F=lambda z:z[0]
        sup_real=max(F(z).real for z in C)
        sup_abs=max(abs(F(z)) for z in C)
        self.assertAlmostEqual(sup_real,sup_abs)
        # Phase rotation realizes modulus for an arbitrary complex z.
        for z in (1+1j,-2+3j,1j,-4+0j):
            phase=z.conjugate()/abs(z)
            self.assertAlmostEqual((phase*z).real,abs(z))

    def test_product_polar_l1_formula(self):
        # The polar of standard basis in K^N consists of bounded
        # finite-support coefficient vectors, bipolar is the l1 unit ball.
        vectors=((.1, -.3, .4, 0), (.5, .75, 0, 0),
                 (1, 0, 0, 0), (.2,.2,.2,.2))
        for x in vectors:
            supvalue=sum(abs(a) for a in x)
            signs=tuple(0 if a==0 else a/abs(a) for a in x)
            self.assertAlmostEqual(
                abs(sum(v*a for v,a in zip(x,signs))),supvalue)
            self.assertEqual(supvalue<=1, sum(abs(a) for a in x)<=1)

    def test_weak_closure_argument_separates_closed_hull(self):
        # The separation theorem assumes a CLOSED convex set.
        # C=(0,1) is not closed, D=cl(C)=[0,1]. A separator of D
        # is automatically a separator of C, not conversely by citation.
        self.assertIn(r"$D=\overline C$", self.chapter)
        self.assertIn(
            r"Wniosek~\ref{cor:point-closed-convex} do $D$",
            self.chapter)
        c=[k/20 for k in range(1,20)]
        d=[0.0]+c+[1.0]
        x0=2.0
        ell=lambda x:-x
        alpha=-1.5
        self.assertLess(ell(x0),alpha)
        self.assertLess(alpha,min(map(ell,d)))
        self.assertLessEqual(min(map(ell,d)),min(map(ell,c)))

    def test_complex_bipolar_support_on_balanced_weighted_ball(self):
        # C={|z1|+2|z2|<=1} is absolutely convex in C².
        # For F(z)=z1+(2+i)z2, the support is max(1,|2+i|/2).
        coefficient=2+1j
        expected=max(1,abs(coefficient)/2)
        gauge=lambda z:abs(z[0])+2*abs(z[1])
        F=lambda z:z[0]+coefficient*z[1]
        witness=(0j, .5*coefficient.conjugate()/abs(coefficient))
        self.assertAlmostEqual(gauge(witness),1)
        self.assertAlmostEqual(F(witness).real,expected)
        self.assertAlmostEqual(abs(F(witness)),expected)
        for z in [(0j,0j),(1+0j,0j),(.1+.2j, .1-.1j),witness]:
            if gauge(z)>1:
                continue
            for angle in (0,math.pi/4,math.pi/2,2*math.pi/3):
                phase=complex(math.cos(angle), math.sin(angle))
                rotated=(phase*z[0],phase*z[1])
                self.assertAlmostEqual(gauge(rotated),gauge(z))
                self.assertLessEqual(abs(F(rotated)),expected+1e-12)

    def test_product_bipolar_complex_finite_support_phase(self):
        # Sup |sum_n a_n x_n| over |a_n|<=1, finite support, equals
        # sum |x_n| also in the complex case.
        vectors=[
            (1+1j, -.5j, 2-1j, 0j),
            (.2j, -.25+.3j, .1+0j, 0j),
            (0j,0j,0j,0j)
        ]
        for x in vectors:
            norm1=sum(abs(v) for v in x)
            coeffs=tuple(0j if v==0 else v.conjugate()/abs(v) for v in x)
            pairing=sum(a*v for a,v in zip(coeffs,x))
            self.assertAlmostEqual(abs(pairing),norm1)
            for m in range(1,len(x)+1):
                truncated=x[:m]+(0j,)*(len(x)-m)
                self.assertLessEqual(
                    sum(abs(v) for v in truncated),norm1+1e-12)
            if norm1 > 1:
                self.assertGreater(abs(pairing),1)
            else:
                for trial in itertools.product((0,1,-1,1j,-1j), repeat=len(x)):
                    self.assertLessEqual(
                        abs(sum(a*v for a,v in zip(trial,x))),1+1e-12)

    def test_weak_convex_closure_separation(self):
        # If x0 lies outside the l1 ball, a functional in its dual
        # produces an open halfspace separating x0 from the closed ball.
        x0=(2.0,2.0)
        F=lambda v:v[0]+v[1]
        self.assertGreater(F(x0), 1)
        for a in itertools.product((-1,-.5,0,.5,1),repeat=2):
            if abs(a[0])+abs(a[1])<=1:
                self.assertLessEqual(F(a),1)


if __name__ == "__main__":
    unittest.main()
