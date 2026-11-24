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


    def test_mt30_006_atomic_decomposition(self):
        weights = [Q(1,6), Q(0), Q(1,3), Q(1,2)]
        nu = [Q(-1,6), Q(0), Q(1,6), Q(1,4)]
        density = [v/w if w else Q(0) for v,w in zip(nu,weights)]
        for bits in product((0,1), repeat=4):
            self.assertEqual(sum(b*v for b,v in zip(bits,nu)),
                             sum(b*w*d for b,w,d in zip(bits,weights,density)))
        self.assertEqual(sum(w*abs(d) for w,d in zip(weights,density)),sum(map(abs,nu)))

    def test_mt30_007_interval_coding_nonuniform_and_null_cells(self):
        weights = [Q(1,8), Q(0), Q(3,8), Q(1,6), Q(1,3)]
        values = [Q(1), Q(0), Q(-1), Q(1,2), Q(-1,2)]
        groups = [[0,1,2], [3,4]]
        parent = {i: sum(weights[j]*values[j] for j in group)/sum(weights[j] for j in group)
                  for group in groups for i in group}
        ends = [Q(0)]
        for w in weights:
            ends.append(ends[-1]+w)
        jump = sum(w*abs(v-parent[i]) for i,(w,v) in enumerate(zip(weights,values)))
        coded = sum((ends[i+1]-ends[i])*abs(v-parent[i]) for i,v in enumerate(values))
        self.assertEqual(jump,coded)
        self.assertEqual(ends[-1],1)
        for a in range(len(weights)+1):
            for b in range(a,len(weights)+1):
                self.assertLessEqual(abs(sum(weights[i]*values[i] for i in range(a,b))),ends[b]-ends[a])

    def test_mt30_008_maximal_and_partition_proof_steps(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for step in ("ogona zbieżnego szeregu miar", "sumę wszystkich otrzymanych zbiorów zerowych",
                     "porządek częściowy na klasach", "rzeczywiście rosnące zbiory",
                     "zbieżności całej sieci", "atomem dla", "niezależną od wyboru ciągu"):
            self.assertIn(step,s)
        self.assertIn(r"2\delta+M\omega_\phi(m_n)",s)


if __name__ == "__main__":
    unittest.main()
