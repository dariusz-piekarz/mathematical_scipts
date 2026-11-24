"""Exact finite interval models and source guards for chapter 24."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/24-twierdzenia-pokryciowe-vitaliego-i-besicovitcha.tex"


def intersects(a, b):
    return abs(a[0]-b[0]) < a[1]+b[1]


def contains(b, x):
    return abs(b[0]-x) < b[1]


def select_5r(balls):
    if not balls:
        return []
    R = max(r for _, r in balls)
    selected = []
    pending = list(balls)
    while pending:
        scale = [(x,r) for x,r in pending if R/2 < r <= R]
        for B in scale:
            if not any(intersects(B,D) for D in selected):
                selected.append(B)
        pending = [B for B in pending if B not in scale]
        R /= 2
    return selected


def probes(balls):
    endpoints = sorted({x+s*r for x,r in balls for s in (-1,1)})
    return endpoints + [(a+b)/2 for a,b in zip(endpoints,endpoints[1:])]


class TestCoveringChapter24(unittest.TestCase):
    def test_5r_exact_interval_models(self):
        pool = [(Fraction(x), Fraction(r)) for x in (-2,0,2) for r in (1,2,4)]
        for mask in range(1 << len(pool)):
            balls = [B for i,B in enumerate(pool) if mask & (1 << i)]
            selected = select_5r(balls)
            self.assertTrue(all(not intersects(a,b) for a,b in combinations(selected,2)))
            for x,r in balls:
                self.assertTrue(any(abs(x-y)+r <= 5*s for y,s in selected))

    def test_finite_besicovitch_all_radius_assignments(self):
        from itertools import product
        for radii in product((1,2,4), repeat=5):
            balls = [(Fraction(x),Fraction(r)) for x,r in zip(range(-2,3),radii)]
            selected = []
            for B in sorted(balls,key=lambda b:-b[1]):
                if not any(contains(D,B[0]) for D in selected):
                    selected.append(B)
            self.assertTrue(all(any(contains(D,x) for D in selected) for x,_ in balls))
            for a,b in combinations(selected,2):
                self.assertFalse(contains(a,b[0]))
                self.assertFalse(contains(b,a[0]))
            for z in probes(selected):
                self.assertLessEqual(sum(contains(B,z) for B in selected),3)

    def test_multiscale_besicovitch_exact_interval_models(self):
        from itertools import product
        for radii in product((1,2,4,8), repeat=5):
            balls = [(Fraction(x),Fraction(r)) for x,r in zip(range(-2,3),radii)]
            R = max(radii)
            scales = []
            selected = []
            a = Fraction(R,2)
            while a >= Fraction(1,2):
                candidates = [B for B in balls if a < B[1] <= 2*a
                              and not any(contains(D,B[0]) for D in selected)]
                S = []
                for B in candidates:
                    if all(abs(B[0]-D[0]) >= a for D in S):
                        S.append(B)
                for B in candidates:
                    self.assertTrue(any(contains(D,B[0]) for D in S))
                scales.append(S)
                selected.extend(S)
                a /= 2
            self.assertTrue(all(any(contains(D,x) for D in selected) for x,_ in balls))
            for k,S in enumerate(scales):
                for T in scales[k+1:]:
                    for B in S:
                        for D in T:
                            self.assertFalse(contains(B,D[0]))
                            self.assertFalse(contains(D,B[0]))
            for z in probes(selected):
                counts = [sum(contains(B,z) for B in S) for S in scales]
                self.assertLessEqual(max(counts),5)
                self.assertLessEqual(sum(n>0 for n in counts),3)
                self.assertLessEqual(sum(counts),15)

    def test_exact_figure_geometry(self):
        D = (Fraction(0),Fraction(2,5))
        B = (Fraction(4,5),Fraction(1,2))
        other = (Fraction(39,10),Fraction(7,20))
        self.assertTrue(intersects(D,B))
        self.assertFalse(intersects(D,other))
        self.assertLess(abs(D[0]-B[0])+B[1],5*D[1])
        self.assertLess(B[1],2*D[1])

    def test_source(self):
        s = SOURCE.read_text(encoding="utf8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for token in (r"m=0",r"\lambda_d^*(Z)=0",r"\chi_{B(x_n,r_n)}",
                      r"twierdzenie Beppo Leviego",r"circle (2)",r"circle (0.4)",r"Z=\bigcup_{j\ge1}\partial B_j",r"2^{1-(\ell-k)}a_k"):
            self.assertIn(token,s)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",s):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertEqual(stack.pop(),m[2])
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
