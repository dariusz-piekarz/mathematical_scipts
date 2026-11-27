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



    def test_mt30_009_variation_and_uniqueness(self):
        w = [Q(1,6), Q(0), Q(1,3), Q(1,2)]
        g = [Q(3), Q(999), Q(-2), Q(4)]
        h = [Q(-1), Q(-999), Q(5), Q(4)]
        for bits in product((0,1), repeat=4):
            vg = sum(b*m*abs(x) for b,m,x in zip(bits,w,g))
            vh = sum(b*m*abs(x) for b,m,x in zip(bits,w,h))
            vd = sum(b*m*abs(x-y) for b,m,x,y in zip(bits,w,g,h))
            self.assertLessEqual(abs(vg-vh),vd)
        same = [g[0], Q(-5), g[2], g[3]]
        self.assertEqual(sum(m*abs(x-y) for m,x,y in zip(w,g,same)),0)

    def test_mt30_010_hilbert_partition_energy(self):
        w = [Q(1,6), Q(0), Q(1,3), Q(1,2)]
        g = [(Q(1), Q(2)), (Q(99), Q(99)), (Q(-2), Q(1)), (Q(3), Q(-1))]
        norm2 = lambda v: sum(x*x for x in v)
        mean = lambda group: tuple(sum(w[i]*g[i][k] for i in group)/sum(w[i] for i in group) for k in range(2))
        for groups in ([[0,1,2,3]], [[0,1],[2,3]], [[0,1],[2],[3]]):
            coarse = sum(sum(w[i] for i in group)*norm2(mean(group)) for group in groups)
            fine = sum(m*norm2(v) for m,v in zip(w,g))
            diff = sum(w[i]*norm2(tuple(g[i][k]-mean(group)[k] for k in range(2))) for group in groups for i in group)
            self.assertEqual(fine-coarse,diff)
            self.assertLessEqual(coarse,fine)

    def test_mt30_011_complex_curve_and_source_steps(self):
        # F(t)=(2+3i)t: both real and imaginary scalar identities are needed.
        for a,b in [(Q(0),Q(1)),(Q(1,7),Q(5,6)),(Q(1,3),Q(1,3))]:
            self.assertEqual((2*b-2*a,3*b-3*a),(2*(b-a),3*(b-a)))
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for step in ("Nie potrzeba separowalności całego", "części rzeczywistej i urojonej",
                     "własności podsieci", "bez założenia separowalności", 
                     "Wszystkie odejmowane wariacje są skończone", "Równość dla funkcji prostych przechodzi"):
            self.assertIn(step,s)



    def test_mt30_012_l1_difference_quotients(self):
        for h in (Q(1,2), Q(1,17), Q(1,1000)):
            self.assertEqual((h/2)*abs(2/h-1/h)+(h/2)*abs(0-1/h),1)
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        self.assertIn(r"\|q_{h/2}-q_h\|_{L^1}",s)
        self.assertIn("co daje równość wariacji",s)

    def test_mt30_013_absolute_continuity_without_finite_variation(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        self.assertIn(r"Jeśli $\nu\ll\mu$, to $|\nu|\ll\mu$.",s)
        self.assertIn(r"\|g\|_{L^\infty}\le\operatorname{Lip}(F)",s)
        for a,b in ((Q(-2),Q(3)),(Q(1,7),Q(2,7)),(Q(-1),Q(0))):
            for slope in (Q(-3),Q(0),Q(5,3)):
                self.assertEqual((b-a)*slope/(b-a),slope)



    def test_mt30_014_birkhoff_source_and_atomic_variation(self):
        s = SOURCE.read_text(encoding="utf-8")
        for label in ("def:birkhoff-30", "thm:birkhoff-basic-30",
                      "thm:birkhoff-measure-30", "thm:bochner-birkhoff-30",
                      "thm:birkhoff-pettis-30", "ex:birkhoff-infinite-variation-30"):
            self.assertIn(r"\label{" + label + "}", s)
        self.assertLess(s.index(r"\label{sec:bochner-30}"),
                        s.index(r"\label{sec:birkhoff-30}"))
        self.assertLess(s.index(r"\label{sec:birkhoff-30}"),
                        s.index(r"\label{sec:rnp-30}"))
        for n in range(2, 20):
            for m in range(n, 30):
                tail = sum((Q(1, k*k) for k in range(n, m+1)), Q(0))
                self.assertLessEqual(tail, Q(1, n-1)-Q(1, m))
        for j in range(1, 10):
            block = sum((Q(1, k) for k in range(2**j, 2**(j+1))), Q(0))
            self.assertGreaterEqual(block, Q(1, 2))
        for n in range(1, 25):
            self.assertEqual(Q(1, 2**n)*Q(2**n, n), Q(1, n))


    def test_mt30_015_birkhoff_orthogonal_tagged_sums(self):
        # A finite analogue of disjoint tagged cells, including null cells.
        for m in range(1, 13):
            weights = [Q(1, 3*m), Q(2, 3*m), Q(0)] * m
            self.assertEqual(sum(weights), 1)
            for k in range(len(weights)+1):
                tail = weights[k:]
                self.assertLessEqual(sum(w*w for w in tail),
                                     Q(1, m)*sum(tail))
            self.assertLessEqual(sum(w*w for w in weights), Q(1, m))
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\label{ex:birkhoff-not-strong-30}", s)
        self.assertIn(r"\lambda_1(J)=0", s)
        self.assertIn(r"F\subseteq I\setminus H", s)


    def test_mt30_016_birkhoff_convex_refinement_and_majorants(self):
        for a,b,c in product(range(-2,3), repeat=3):
            values = [Q(a), Q(b), Q(c)]
            weights = [Q(1,6), Q(1,3), Q(1,2)]
            refined = sum(w*v for w,v in zip(weights,values))
            self.assertLessEqual(min(values), refined)
            self.assertLessEqual(refined, max(values))
            for n in range(1,8):
                majorants = [abs(v)/n for v in values]
                for mask in product((0,1), repeat=3):
                    err = abs(sum(w*v*m/n for w,v,m in zip(weights,values,mask)))
                    self.assertLessEqual(err, sum(w*q for w,q in zip(weights,majorants)))
        s = SOURCE.read_text(encoding="utf-8")
        for label in ("lem:birkhoff-refinement-30", "thm:birkhoff-convex-30",
                      "thm:birkhoff-limit-30", "cor:birkhoff-dct-30"):
            self.assertIn(r"\label{" + label + "}", s)

if __name__ == "__main__":
    unittest.main()
