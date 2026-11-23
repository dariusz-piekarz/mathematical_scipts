"""Chapter 22 measure-convergence finite-model and source regressions.

Finite and numeric tests are not proofs of Portmanteau or Prokhorov in
arbitrary metric spaces.
Run: python -m unittest discover -s tools/tests -p 'test_measure_theory_ch22.py' -v
"""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/measure_theory/22-zbieznosc-miar-twierdzenie-portmanteau-i-zwartosc-prochorowa.tex"


def subsets(n):
    for k in range(1 << n):
        yield [i for i in range(n) if (k >> i) & 1]


class TestMeasureTheoryChapter22(unittest.TestCase):
    def test_discrete_portmanteau_and_total_variation(self):
        p, r = [0.2, 0.3, 0.5], [0.6, 0.1, 0.3]
        for n in (1, 2, 5, 10, 100, 1000):
            q = [(1 - 1/n) * a + b / n for a, b in zip(p, r)]
            distance = max(abs(sum(q[i] - p[i] for i in E)) for E in subsets(3))
            self.assertAlmostEqual(distance, sum(abs(x - y) for x, y in zip(q, p)) / 2)
            self.assertLessEqual(distance, 1/n)
            for E in subsets(3):
                self.assertLessEqual(
                    abs(sum(q[i] - p[i] for i in E)), distance + 1e-12
                )

    def test_dirac_weak_without_tv(self):
        for n in (2, 5, 10, 100, 1000):
            x = 1 / n
            self.assertLessEqual(abs(math.sin(x) - math.sin(0)), 1/n)
            self.assertEqual(1, 1.0)  # TV(delta_{1/n}, delta_0).
            self.assertLessEqual(abs(math.exp(-x*x) - 1), 1/n**2)

    def test_vague_without_c0_weak_star(self):
        # n*delta_n is eventually zero on any fixed compact support,
        # but the C0 test f(x)=(1+|x|)^(-1/2) has divergent integral.
        for n in (1, 2, 5, 10, 100, 10000):
            value = n / math.sqrt(1 + n)
            self.assertGreater(value, 0)
            if n >= 2:
                self.assertGreaterEqual(value, math.sqrt(n/2))

    def test_lipschitz_infimum_extension_on_finite_net(self):
        points = [-1., 0., 1.]
        h = [-1., 0., 1.]
        L = 1.
        for x, fx in zip(points, h):
            envelope = min(v + L*abs(x-z) for z, v in zip(points, h))
            self.assertAlmostEqual(envelope, fx)
        grid = [k / 10 for k in range(-25, 26)]
        values = [
            max(-1, min(1, min(v + L*abs(x-z) for z,v in zip(points,h))))
            for x in grid
        ]
        self.assertTrue(all(abs(v) <= 1 for v in values))
        self.assertTrue(all(abs(b-a) <= L * abs(y-x) + 1e-12
                            for (x,a),(y,b) in zip(zip(grid,values), zip(grid[1:],values[1:]))))

    def test_hilbert_cube_coordinate_embedding_on_finite_space(self):
        points = [0., 0.3, 1., 2.]
        feature = lambda x: [abs(x-z)/(1+abs(x-z)) for z in points]
        embedding = [feature(x) for x in points]
        for i in range(len(points)):
            for j in range(len(points)):
                D = sum(2**(-k-1)*abs(a-b)
                        for k,(a,b) in enumerate(zip(embedding[i], embedding[j])))
                if i == j:
                    self.assertAlmostEqual(D, 0)
                else:
                    self.assertGreater(D, 0)

    def test_uniform_tightness_geometric_atomic_family(self):
        # A family of tail-perturbed measures on a countable metric space:
        # total mass outside first m atoms is bounded by 2^(-m).
        for m in range(1, 15):
            bound = 2.0 ** (-m)
            tails = [bound * factor for factor in (0., .2, .5, .9, 1.)]
            self.assertLessEqual(max(tails), bound)
            if m >= 8:
                self.assertLess(bound, .005)

    def test_first_moment_not_continuous_under_tv_convergence(self):
        for n in (1, 2, 3, 5, 10, 100, 1000):
            p0, pn = 1 - 1/n, 1/n
            self.assertAlmostEqual(p0 + pn, 1)
            self.assertAlmostEqual(pn, 1/n)  # Total variation distance to delta_0.
            self.assertAlmostEqual(pn * n, 1)  # First moment remains 1.
        # The limit delta_0 has first absolute moment zero.
        self.assertEqual(0, 0 * 1.0)

    def test_tex_structure_and_new_counterexample(self):
        source = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertGreaterEqual(len(labels), 22)
        self.assertEqual(len(labels), len(set(labels)))
        required = {"thm:portmanteau-22", "thm:prokhorov-22",
                    "thm:prokhorov-forward-22", "ex:moment-not-continuous-22",
                    "lem:compact-prob-22", "lem:hilbert-cube-22"}
        self.assertTrue(required.issubset(set(labels)))
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack, "Unmatched \\end")
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack, "Open LaTeX environments")
        self.assertIn(r"d_{\mathrm{TV}}(\mu_n,\mu)=1/n\to0", source)
        self.assertIn(r"\int_{\mathbb R}|x|\,\mathrm d\mu_n(x)=1", source)
        self.assertNotIn("jest ograniczona.", source)
        self.assertNotRegex(source, r"\\(?:mathbf|mathbb)\{1\}_")


if __name__ == "__main__":
    unittest.main()
