import itertools
import re
import unittest
from pathlib import Path
from fractions import Fraction as F

DIR = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis"
S = next(DIR.glob("27-*.tex")).read_text(encoding="utf-8")

class Chapter27(unittest.TestCase):
    def test_structure(self):
        labels = re.findall(r"\\label\{([^}]+)\}", S)
        self.assertEqual(len(labels), len(set(labels)))
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", S):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 27)
        for ref in re.findall(r"\\ref\{([^}]+)\}", S):
            self.assertIn(r"\label{" + ref + "}", context)

    def test_FA27_coefficient_completeness_01(self):
        for phrase in (r"E_e$ jest", r"\le2\|a^{(k)}-a^{(\ell)}\|_{E_e}",
                       r"\le2\eta+", r"z zupełności $X$", r"\|a^{(k)}-a\|_{E_e}\to0"):
            self.assertIn(phrase, S)
        for a in itertools.product(range(-2, 3), repeat=4):
            sums = [sum(a[:i]) for i in range(5)]
            bound = max(map(abs, sums))
            for n in range(4):
                self.assertLessEqual(abs(a[n]), 2 * bound)
            for i in range(5):
                for j in range(i, 5):
                    self.assertLessEqual(abs(sum(a[i:j])), 2 * bound)

    def test_FA27_block_permutation_01(self):
        self.assertIn(r"\max(D_k\cup\{k\})", S)
        self.assertIn("w tym indeksów wstawionych między blokami", S)
        self.assertIn("tuż przed blokiem", S)
        for lengths in itertools.product((1, 2, 3), repeat=5):
            order = []
            for k, length in enumerate(lengths, 1):
                start = max([k] + order) + 1
                block = list(range(start, start + length))
                order.extend(block)
                least = next(j for j in itertools.count(1) if j not in order)
                order.append(least)
                self.assertEqual(len(order), len(set(order)))
                self.assertTrue(set(range(1, k+1)) <= set(order))

    def test_FA27_finite_sum_bound_01(self):
        self.assertIn(r"P_Fx=P_{F\cup F_0}x-P_{F_0\setminus F}x", S)
        self.assertIn(r"\max_{E\subseteq F_0}\|P_Ex\|", S)
        sets = [set(i for i in range(4) if mask & (1 << i)) for mask in range(16)]
        for values in itertools.product((-2, 0, 3), repeat=4):
            def p(A): return sum(values[i] for i in A)
            for A, B in itertools.product(sets, repeat=2):
                self.assertEqual(p(A), p(A | B) - p(B - A))
                self.assertLessEqual(abs(p(A)), abs(p(A | B)) + max(abs(p(E)) for E in sets if E <= B))

    def test_FA27_empty_projection_01(self):
        self.assertIn(r"F=\varnothing$ jest zerowy", S)
        for mask in range(8):
            A = [i for i in range(3) if mask & (1 << i)]
            for x in itertools.product(range(-2, 3), repeat=3):
                self.assertLessEqual(sum(x[i]**2 for i in A), sum(t*t for t in x))
            self.assertEqual(max(sum(int(i==j)**2 for i in A) for j in range(3)), int(bool(A)))

    def test_FA27_summing_basis_01(self):
        self.assertIn(r"a_j=x_j-x_{j+1}", S)
        for x in itertools.product((F(-1), F(0), F(1)), repeat=4):
            x = x + (F(0),)
            a = [x[i]-x[i+1] for i in range(4)]
            for N in range(1, 5):
                y = [sum(a[j:N]) if j < N else 0 for j in range(4)]
                self.assertEqual(y[:N], [x[j]-x[N] for j in range(N)])
                self.assertLessEqual(max(abs(x[j]-y[j]) for j in range(4)),
                                     2*max(map(abs, x[N:])))

    def test_FA27_reflexivity_norming_01(self):
        self.assertIn(r"\|s_N\|=\sup_{\|f\|\le1}|f(s_N)|\le K_e\|\Phi\|", S)
        self.assertIn(r"\|f-P_N'f\|\le(1+K_e)\|f|_{Y_N}\|", S)

    def test_FA27_basic_sequence_extension_01(self):
        for phrase in (r"\|P_N(y_k-z_k)\|\le K\|y_k-z_k\|\to0",
                       r"(P_n-P_{n-1})x=f_n(x)e_n",
                       r"|f_n(x)|\le2K\|x\|/\|e_n\|",
                       r"f_n(e_m)=\delta_{nm}",
                       r"P_Nx=\sum_{n=1}^Nf_n(x)e_n"):
            self.assertIn(phrase, S)
        weights = (2, 3, 5)
        for a in itertools.product(range(-2, 3), repeat=3):
            x = tuple(w*t for w,t in zip(weights,a))
            for n in range(1, 4):
                p = tuple(x[j] if j < n else 0 for j in range(3))
                q = tuple(x[j] if j < n-1 else 0 for j in range(3))
                self.assertEqual(tuple(u-v for u,v in zip(p,q)),
                                 tuple(weights[j]*a[j] if j==n-1 else 0 for j in range(3)))
                self.assertLessEqual(abs(a[n-1])*weights[n-1], 2*max(map(abs,x)))

    def test_FA27_conditional_even_tail_01(self):
        self.assertIn(r"a_{2k}\ge1/\sqrt{2k}\ge1/(2k)", S)
        self.assertIn(r"\|\sum_{n\in F}a_ns_n\|_\infty\ge|\sum_{n\in F}a_n|\ge1", S)
        self.assertIn(r"\varepsilon=1", S)
        for m in (1, 3, 7, 16, 31):
            tail = sum((F(1,2*k) for k in range(m+1,16*m+1)), F(0))
            self.assertGreaterEqual(tail, 1)

if __name__ == "__main__":
    unittest.main()
