import re
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("26-*.tex"))


class Chapter26(unittest.TestCase):
    def test_structure_and_references(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 26)
        for a, b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA26_canonical_goldstine_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"|f(x)|\le\|f\|\|x\|",
            r"\ref{cor:norming}",
            r"|(J_Xx)(f)|=|f(x)|",
            r"J_X(B_X)\subseteq B_{X''}",
            r"\Phi\in B_{X''}\setminus\overline{J_X(B_X)}^{\,w^\ast}",
            r"|f_j(x)-\Phi(f_j)|<\eta",
            r"\ref{cor:point-closed-convex}",
            r"\ref{lem:realification}",
            r"\sup_{x\in B_X}\operatorname{Re}f(x)=\|f\|",
            r"\operatorname{Re}\Phi(f)\le|\Phi(f)|",
            r"\ref{cor:weak-convex-closure}",
            r"J_X(B_X)=B_{X''}",
            r"J_X(\|\Phi\|x)=\Phi",
            r"|f(x)|\le\|G\|\|x\|",
            r"\ref{thm:point-closed-subspace}",
        ):
            self.assertIn(fragment, s)

    def test_FA26_complex_norming_model_01(self):
        # Exact finite-dimensional models on C^3 with the l1 norm.
        # Complex numbers are pairs of rationals, avoiding floating point.
        def mul(z, w):
            a, b = z
            c, d = w
            return (a*c-b*d, a*d+b*c)

        def pairing(a, x):
            terms = [mul(z, w) for z, w in zip(a, x)]
            return tuple(sum(t[k] for t in terms) for k in range(2))

        coeffs = [((0, 0), 0), ((1, 0), 1), ((0, -2), 2),
                  ((3, 4), 5), ((-4, 3), 5)]
        for entries in product(coeffs, repeat=3):
            a = [z for z, m in entries]
            M = max(m for z, m in entries)
            j = next(i for i, (z, m) in enumerate(entries) if m == M)
            x = [(F(0), F(0)) for _ in range(3)]
            if M:
                x[j] = (F(a[j][0], M), F(-a[j][1], M))
            self.assertEqual(pairing(a, x), (M, 0))
            # Check the dual-norm bound on independent l1-unit vectors.
            for i, (u, v) in product(range(3), ((1, 0), (0, 1),
                                                (F(3, 5), F(-4, 5)))):
                y = [(F(0), F(0)) for _ in range(3)]
                y[i] = (u, v)
                re, im = pairing(a, y)
                self.assertLessEqual(re*re+im*im, M*M)
        # Reconstruction of the complex-linear functional from its
        # real part L: f(z)=L(z)-i L(iz).
        for a, z in product(product(((-1, 0), (0, 1), (1, -1)), repeat=3),
                            product(((-1, 0), (0, 1), (1, -1)), repeat=3)):
            iz = [(-v, u) for u, v in z]
            self.assertEqual(pairing(a, z),
                             (pairing(a, z)[0], -pairing(a, iz)[0]))


    def test_FA26_eberlein_smulian_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"F=\{0\}",
            r"\|\Theta-\Psi_j\|\|f_{\Psi_j}\|",
            r"F=\{f_{\Psi_1},\ldots,f_{\Psi_r}\}",
            r"\|y\|-2\|y-y_j\|>\|y\|/3",
            r"0\le d(u,v)-d_N(u,v)\le2^{-N}",
            r"\ref{cor:uniform-boundedness}",
            r"n>|f(x)|+1",
            r"|f(x_n)-\Phi(f)|<1/n",
            r"\|G-\Psi\|<\eta",
            r"\|\Psi\|\le3\|\Psi-G\|<3\eta",
            r"C=\overline{J_X(A)}^{\,w^\ast}",
            r"J_X(\overline A^{\,w})=C",
        ):
            self.assertIn(fragment, s)
        # Exact finite models of the metric and finite norming cover.
        V = list(product((-1, 0, 1), repeat=2))

        def term(u, v, j):
            return F(1, 2**j)*min(1, abs(u[j-1]-v[j-1]))

        def metric(u, v):
            return sum(term(u, v, j) for j in (1, 2))

        for u, v, w in product(V, repeat=3):
            self.assertLessEqual(metric(u, w), metric(u, v)+metric(v, w))
        for u, v in product(V, repeat=2):
            self.assertEqual(metric(u, v)==0, u==v)
            for N in range(3):
                tail = metric(u, v)-sum(term(u, v, j) for j in range(1, N+1))
                self.assertTrue(0 <= tail <= F(1, 2**N))

        S = [(F(a, 16), F(b, 16)) for a, b in
             product(range(-16, 17), repeat=2) if max(abs(a), abs(b))==16]
        for p, q in product(S, repeat=2):
            d = max(abs(a-b) for a, b in zip(p, q))
            if d >= F(1, 4):
                continue
            j = next(i for i in range(2) if abs(p[i])==1)
            self.assertTrue(abs(q[j]) >= abs(p[j])-d > F(1, 2))

if __name__ == "__main__":
    unittest.main()
