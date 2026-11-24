"""Chapter 30 source and finite-model regressions; not formal proof certification."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/30-miary-wektorowe-calka-bochnera-i-wlasnosc-radona-nikodyma.tex"

class Chapter30(unittest.TestCase):
    def test_mt30_001_measurable_representative_and_completeness(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for step in ("mierzalnego przedstawiciela", "Zbiór zbieżności jest mierzalny",
                     "dowolnego ciągu Cauchy'ego", "Zbieżność prawie wszędzie zostaje zachowana"):
            self.assertIn(step, s)

    def test_mt30_002_disjoint_approximation(self):
        sets = [{i for i,b in enumerate(bits) if b} for bits in product((0,1), repeat=3)]
        weights = [Q(0), Q(2,7), Q(5,7)]
        mass = lambda A: sum((weights[i] for i in A), Q(0))
        for A,B,P,T in product(sets, repeat=4):
            if not A & B:
                self.assertLessEqual(mass((T-P)^B), mass(T^B)+mass(P^A))
                self.assertFalse(P & (T-P))
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\nu(\{0\})=0", s)
        self.assertIn("Sprawdzamy najpierw skończoną addytywność", s)

    def test_mt30_003_change_of_measure(self):
        mu0 = [Q(1,2), Q(1,3), Q(1,6)]
        w = [Q(2), Q(0), Q(3)]
        g = [Q(-2), Q(999), Q(4)]
        mu = [a*b for a,b in zip(mu0,w)]
        for bits in product((0,1), repeat=3):
            self.assertEqual(sum(a*b*c for a,b,c in zip(mu0,[v*x for v,x in zip(w,g)],bits)),
                             sum(a*b*c for a,b,c in zip(mu,g,bits)))
        self.assertEqual(sum(a*abs(b*c) for a,b,c in zip(mu0,w,g)),
                         sum(a*abs(b) for a,b in zip(mu,g)))
        self.assertIn(r"\|s_jw-gw\|", SOURCE.read_text(encoding="utf-8"))

    def test_mt30_004_l1_counterexample_dyadic_averages(self):
        for n in range(1,9):
            parent = Q(1,2**n)
            child = parent/2
            jump = child*abs(1/child-1/parent)+child/parent
            self.assertEqual(jump,1)
            self.assertEqual(2**(n+1)*child*jump,1)

    def test_mt30_005_labels_and_notation(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertIn("thm:rnp-lipschitz-equiv-30",labels)
        self.assertNotRegex(s,r"\\(?:mathbf|mathbb)\{1\}_")

if __name__ == "__main__":
    unittest.main()
