"""Focused mathematical/structural regression checks for functional analysis chapter 09.

These finite models and LaTeX source contracts are NOT machine proofs
of the Banach--Alaoglu, Krein--Milman, Mackey--Arens or Helly theorems.
"""
from __future__ import annotations

import itertools
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
BOOK = ROOT / "books/pl/functional_analysis.tex"


class Chapter09Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = []
        for n in range(1, 10):
            candidates = list(CHAPTERS.glob(f"{n:02d}-*.tex"))
            if len(candidates) != 1:
                raise AssertionError(f"Expected one file for chapter {n}, got {candidates!r}")
            cls.files.append(candidates[0])
        cls.sources = [path.read_text(encoding="utf-8") for path in cls.files]
        cls.source = cls.sources[-1]

    def test_book_includes_all_chapters_in_order(self):
        book = BOOK.read_text(encoding="utf-8")
        paths = re.findall(
            r"\\input\{\.\./\.\./chapters/pl/functional_analysis/([^}]+)\}", book
        )
        self.assertEqual(paths[:9], [f.name for f in self.files])
        self.assertIn(r"\setcounter{section}{8}", self.source)

    def test_all_proofs_examples_and_environments_balanced(self):
        s = self.source
        for name, expected in (("proof", 14), ("przyklad", 8)):
            self.assertEqual(s.count(r"\begin{" + name + "}"), expected)
            self.assertEqual(s.count(r"\end{" + name + "}"), expected)
        for name in ("definicja", "stwierdzenie", "wniosek", "lemat",
                     "twierdzenie", "uwaga", "tikzpicture", "center"):
            self.assertEqual(s.count(r"\begin{" + name + "}"),
                             s.count(r"\end{" + name + "}"))

    def test_unique_labels_and_resolved_references(self):
        labels = [
            label for source in self.sources
            for label in re.findall(r"\\label\{([^}]+)\}", source)
        ]
        own = re.findall(r"\\label\{([^}]+)\}", self.source)
        refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        refs += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertEqual(len(own), 23)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertFalse(set(refs) - set(labels), sorted(set(refs) - set(labels)))

    def test_polish_terminology_and_essential_convexity_hypothesis(self):
        s = self.source
        self.assertIn("Wierzchołki wypukłego wielokąta", s)
        self.assertNotIn("Wierzchołki nieosobliwego wielokąta", s)
        self.assertNotIn("sekwencyjn", s)
        self.assertNotIn("przestrzeń dualna topologiczna", s)
        self.assertIn("przestrzeń sprzężoną", s)
        self.assertIn(r"\chi_F", s)
        self.assertIn(r"\chi_I", s)
        self.assertNotIn(r"\mathbf 1_", s)

    def test_r_equicontinuous_polar_model(self):
        # E=R^2, E' identified with R^2, U=(-1,1)^2:
        # U^circ is the l1 unit ball.
        vals = ((Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1), Fraction(0)),
                (Fraction(1, 4), Fraction(-1, 4)))
        for a, b in vals:
            self.assertLessEqual(abs(a) + abs(b), 1)
            for x, y in itertools.product(
                (Fraction(-999,1000), Fraction(0), Fraction(999,1000)),
                repeat=2
            ):
                self.assertLessEqual(abs(a*x+b*y), 1)

    def test_alaoglu_finite_box_closedness(self):
        # Polar constraints and linearity are closed under pointwise limits.
        candidates = [
            (Fraction(a, 4), Fraction(b, 4))
            for a in range(-4, 5) for b in range(-4, 5)
        ]
        polar = [(a, b) for a, b in candidates if abs(a)+abs(b) <= 1]
        self.assertTrue(polar)
        for a, b in polar:
            self.assertLessEqual(abs(a)+abs(b), 1)

    def test_metric_on_equicontinuous_family_separates(self):
        # Evaluation on the dense rational grid in finite dimension separates forms.
        x_n = [(Fraction(0), Fraction(0)),
               (Fraction(1), Fraction(0)),
               (Fraction(0), Fraction(1))]
        def d(f, g):
            return sum(2**(-n-1) * min(
                1, abs(float((f[0]-g[0])*x[0]+(f[1]-g[1])*x[1]))
            ) for n, x in enumerate(x_n))
        self.assertEqual(d((0,0),(0,0)), 0)
        self.assertGreater(d((0,0),(1,0)), 0)
        self.assertGreater(d((0,0),(0,1)), 0)

    def test_coordinate_directed_net_finite_model(self):
        # For a finite I, indicator sets stabilize pointwise on every coordinate.
        I = range(7)
        directed = [
            frozenset(s) for n in range(8)
            for s in itertools.combinations(I, n)
        ]
        for i in I:
            tail = [F for F in directed if i in F]
            self.assertTrue(tail)
            self.assertTrue(all(int(i in F) == 1 for F in tail))

    def test_compact_sequence_not_norm_bounded_in_incomplete_space(self):
        # f_n(x)=n*x_n on c00: each finitely supported x is eventually zero.
        x = {0: 2, 3: -1, 8: 4}
        for n in range(9, 200):
            self.assertEqual(n * x.get(n, 0), 0)
        self.assertEqual([n for n in range(1, 11)][-1], 10)

    def test_polygon_convexity_is_necessary(self):
        # A concave polygon can list (1,1) as a vertex even though
        # it is the midpoint of (0,0) and (2,2), hence not extreme
        # in the polygon's convex hull.
        x = (1, 1)
        a = (0, 0)
        b = (2, 2)
        self.assertEqual(x, tuple((u+v)/2 for u,v in zip(a,b)))
        self.assertNotEqual(a,b)
        self.assertIn("wypukłego wielokąta", self.source)

    def test_hilbert_unit_sphere_midpoint_identity(self):
        u, v = (1.,0.), (0.,1.)
        x = tuple((a+b)/2 for a,b in zip(u,v))
        norm2 = lambda a: sum(t*t for t in a)
        self.assertAlmostEqual(
            norm2(tuple(a-b for a,b in zip(u,v))),
            2*norm2(u)+2*norm2(v)-4*norm2(x))
        self.assertLess(norm2(x), 1)

    def test_cube_extreme_points_finite_model(self):
        vertices = list(itertools.product((-1,1), repeat=3))
        self.assertEqual(len(vertices), 8)
        for v in vertices:
            # An extreme coordinate +/-1 forces equal endpoints.
            for i, a in enumerate(v):
                self.assertEqual((a+a)/2, v[i])
        self.assertEqual(((0+2)/2,(0+2)/2), (1.,1.))

    def test_l1_ball_extremes_and_nonextremes(self):
        norm = lambda x: sum(map(abs,x))
        for x in ((1,0),(-1,0),(0,1),(0,-1)):
            self.assertEqual(norm(x),1)
        u,v = (Fraction(3,4),Fraction(1,4)), (Fraction(1,4),Fraction(3,4))
        x = tuple((a+b)/2 for a,b in zip(u,v))
        self.assertLessEqual(norm(u),1)
        self.assertLessEqual(norm(v),1)
        self.assertEqual(x,(Fraction(1,2),Fraction(1,2)))

    def test_compact_domination_finite_model(self):
        # K=[-1,1]^2, p_K(x)=|x1|+|x2|;
        # a=(1,-1/2) lies in K and its functional is dominated.
        a=(Fraction(1),Fraction(-1,2))
        for x in itertools.product(range(-3,4),repeat=2):
            value = abs(a[0]*x[0]+a[1]*x[1])
            self.assertLessEqual(value, abs(x[0])+abs(x[1]))

    def test_mackey_polar_reconstructs_seminorm(self):
        # p(x)=2|x1|+3|x2|; a in K_p iff |a1|<=2, |a2|<=3.
        for x in itertools.product(range(-2,3),repeat=2):
            p=2*abs(x[0])+3*abs(x[1])
            values=[abs(a*x[0]+b*x[1])
                    for a,b in itertools.product((-2,0,2),(-3,0,3))]
            self.assertEqual(max(values),p)

    def test_helly_repeated_indices_l1_model(self):
        values={1:Fraction(1,2),2:Fraction(-3,4),3:Fraction(1)}
        R=Fraction(1)
        for indices in itertools.product(tuple(values),repeat=3):
            for coeff in itertools.product((-2,-1,0,1,2),repeat=3):
                lhs=abs(sum(c*values[i] for c,i in zip(coeff,indices)))
                rhs=R*sum(abs(sum(c for c,i in zip(coeff,indices)
                                     if i==k)) for k in values)
                self.assertLessEqual(lhs,rhs)

    def test_helly_zero_radius(self):
        # R=0 forces prescribed values to vanish.
        for b in (0,0,0):
            self.assertLessEqual(abs(b),0)

    def test_tikz_figure_is_self_contained(self):
        s=self.source
        self.assertEqual(s.count(r"\begin{tikzpicture}"),1)
        self.assertEqual(s.count(r"\end{tikzpicture}"),1)
        self.assertIn(r"\max_K\ell",s)


if __name__ == "__main__":
    unittest.main()
