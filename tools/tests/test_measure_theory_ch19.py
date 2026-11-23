"""Deterministic finite-space regressions for chapter 19 of measure theory.

Tests verify numeric identities and the exact source structures; finite
models do not replace proofs for arbitrary measurable spaces.
Run: python -m unittest discover -s tools/tests -p 'test_measure_theory_ch19.py' -v
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/measure_theory/19-zastosowania-twierdzenia-radona-nikodyma.tex"


def subsets(n):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask & (1 << i))


def kl(q, p):
    return sum(0 if x == 0 else x * math.log(x / y) for x, y in zip(q, p))


class TestMeasureTheoryChapter19(unittest.TestCase):
    def test_change_of_measure_and_image_density(self):
        P = [.1, .2, .3, .4]
        f = [1.5, .5, 1., .75]
        Q = [p * z for p, z in zip(P, f)]
        self.assertAlmostEqual(sum(Q), .85)
        values = [3., -1., 2., 4.]
        self.assertAlmostEqual(sum(v * q for v, q in zip(values, Q)),
                               sum(v * z * p for v, z, p in zip(values, f, P)))
        T = [0, 0, 1, 1]
        for target in (0, 1):
            mask = [i for i, t in enumerate(T) if t == target]
            massP = sum(P[i] for i in mask)
            massQ = sum(Q[i] for i in mask)
            g = massQ / massP
            self.assertAlmostEqual(g, sum(P[i] * f[i] for i in mask) / massP)

    def test_total_variation_and_data_processing(self):
        rng = random.Random(19002)
        for _ in range(160):
            p0 = [rng.randrange(0, 7) for _ in range(4)]
            q0 = [rng.randrange(0, 7) for _ in range(4)]
            if not sum(p0) or not sum(q0):
                continue
            P = [x / sum(p0) for x in p0]
            Q = [x / sum(q0) for x in q0]
            supremum = max(abs(sum(P[i] - Q[i] for i in E)) for E in subsets(4))
            half_l1 = sum(abs(p - q) for p, q in zip(P, Q)) / 2
            overlap = 1 - sum(min(p, q) for p, q in zip(P, Q))
            self.assertAlmostEqual(supremum, half_l1, places=12)
            self.assertAlmostEqual(supremum, overlap, places=12)
            imageP = [P[0] + P[1], P[2] + P[3]]
            imageQ = [Q[0] + Q[1], Q[2] + Q[3]]
            image_tv = abs(imageP[0] - imageQ[0])
            self.assertLessEqual(image_tv, supremum + 1e-12)

    def test_neyman_pearson_threshold_optimality(self):
        P = [.7, .3]
        Q = [.2, .8]
        alpha = .15
        c = 8 / 3
        phi = [0., .5]
        self.assertAlmostEqual(sum(p * z for p, z in zip(P, phi)), alpha)
        self.assertAlmostEqual(sum(q * z for q, z in zip(Q, phi)), .4)
        for a in (0, .05, .1, .2, .4, .6, .8, 1):
            for b in (0, .1, .2, .3, .4, .5, .6, .7, .8, 1):
                if P[0] * a + P[1] * b <= alpha + 1e-12:
                    self.assertLessEqual(Q[0] * a + Q[1] * b, .4 + 1e-12)
        self.assertAlmostEqual(Q[1] / P[1], c)
        self.assertLess(Q[0] / P[0], c)
        self.assertTrue(all(P[0] * a + P[1] * b > alpha for a, b in ((1, 0), (0, 1))))

    def test_neyman_pearson_pointwise_inequality_randomized(self):
        rng = random.Random(19004)
        for _ in range(350):
            rawP = [rng.randint(1, 6) for _ in range(4)]
            rawQ = [rng.randint(0, 6) for _ in range(4)]
            if not any(rawQ):
                continue
            P = [x / sum(rawP) for x in rawP]
            Q = [x / sum(rawQ) for x in rawQ]
            c = rng.randrange(0, 11) / 4
            gamma = rng.randrange(0, 11) / 10
            star = [1 if q > c*p else gamma if q == c*p else 0 for p,q in zip(P,Q)]
            for z in ([0]*4, [.25]*4, [.5]*4, [1]*4):
                lhs = sum((a-b)*(q-c*p) for a,b,q,p in zip(z,star,Q,P))
                self.assertLessEqual(lhs, 1e-12)

    def test_bayesian_discrete_posteriors(self):
        pi = [.2, .5, .3]
        conditional = [[.7, .2, .1], [.1, .7, .2], [.4, .3, .3]]
        observed = [sum(pi[i]*conditional[i][j] for i in range(3)) for j in range(3)]
        self.assertAlmostEqual(sum(observed), 1)
        for j in range(3):
            posterior = [pi[i]*conditional[i][j]/observed[j] for i in range(3)]
            self.assertAlmostEqual(sum(posterior), 1)
            for i in range(3):
                self.assertAlmostEqual(posterior[i]*observed[j],
                                       pi[i]*conditional[i][j])

    def test_conditional_jensen_pullout_and_lp_contraction(self):
        P = [.1, .2, .3, .4]
        Y = [3., -2., 1., 5.]
        blocks = ((0,1), (2,3))
        Z = [0.]*4
        H = [2.,2.,-1.,-1.]
        for B in blocks:
            avg = sum(P[i]*Y[i] for i in B)/sum(P[i] for i in B)
            for i in B: Z[i] = avg
            self.assertLessEqual(avg*avg,
                sum(P[i]*Y[i]*Y[i] for i in B)/sum(P[i] for i in B) + 1e-12)
            self.assertAlmostEqual(
                sum(P[i]*H[i]*Y[i] for i in B),
                sum(P[i]*H[i]*Z[i] for i in B))
        for p in (1, 1.5, 2, 3, 4):
            self.assertLessEqual(sum(w*abs(z)**p for w,z in zip(P,Z)),
                                 sum(w*abs(y)**p for w,y in zip(P,Y))+1e-12)

    def test_gibbs_and_entropy_data_processing(self):
        rng = random.Random(19007)
        for _ in range(200):
            rawP = [rng.randint(1, 10) for _ in range(4)]
            rawQ = [rng.randint(1, 10) for _ in range(4)]
            P = [x / sum(rawP) for x in rawP]
            Q = [x / sum(rawQ) for x in rawQ]
            before = kl(Q, P)
            imageP = [P[0]+P[1], P[2]+P[3]]
            imageQ = [Q[0]+Q[1], Q[2]+Q[3]]
            after = kl(imageQ, imageP)
            self.assertGreaterEqual(before, -1e-12)
            self.assertLessEqual(after, before + 1e-12)

    def test_chapter_structure_and_boundary_randomization_example(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(set(labels)), len(labels))
        self.assertIn("ex:np-randomization-19", labels)
        for label in ("thm:neyman-pearson-19", "thm:bayes-finite-19",
                      "thm:gibbs-19", "thm:kl-data-processing-19"):
            self.assertIn(label, labels)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
            if m[1] == "begin": stack.append(m[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack)
        self.assertIn(r"$\varphi_*=\frac12\chi_{\{b\}}$", s)
        self.assertNotRegex(s, r"\\(?:mathbf|mathbb)\{1\}_")


if __name__ == "__main__":
    unittest.main()
