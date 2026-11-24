import re
import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("23-*.tex"))

class Chapter23(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 23)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA23_montel_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ref{lem:montel-schwartz22}",
            r"\ref{lem:exhaustion17}",
            r"|x-y|<\delta_j",
            r"M_{j+1,m+1}\sum_{i=1}^d|x_i-y_i|",
            r"\ref{thm:D-Montel18}",
            r"Funkcjonał Minkowskiego $p_U$",
            r"\{f:p_U(f)<1\}\subseteq U",
            r"\{u_n-u:n\ge1\}",
            r"\sup_{x\in B}|(u_n-u)(x)|\le2\varepsilon/3",
        ):
            self.assertIn(fragment,s)

    def test_FA23_nuclear_banach_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\sum_j\|\ell_j(x)y_j\|\le\|x\|\sum_j\|\ell_j\|\|y_j\|",
            r"\|T-T_N\|\le\sum_{j>N}\|\ell_j\|\|y_j\|",
            r"\|T-T_N\|<\varepsilon/2",
            r"\|T\|\le\|T\|_{\mathcal N}",
            r"\|BTA\|_{\mathcal N}\le\|B\|\|T\|_{\mathcal N}\|A\|",
            r"(\ell_j\circ A)(x)By_j",
            r"\|D-D_N\|=1/(N+1)",
            r"\sum_{n=1}^N|\ell_j(e_n)|^2\le\|\ell_j\|^2",
        ):
            self.assertIn(fragment,s)
        # Exact finite diagonal truncation models (not a proof of compactness).
        for N in range(1,33):
            for extra in range(1,9):
                tail = [F(1,n) for n in range(N+1,N+extra+1)]
                self.assertEqual(max(tail),F(1,N+1))
                self.assertGreaterEqual(sum(tail),F(1,N+1))
        # Harmonic sum dyadic blocks have a uniform lower bound.
        for k in range(10):
            self.assertGreaterEqual(sum(F(1,n) for n in range(2**k+1,2**(k+1)+1)),F(1,2))

    def test_FA23_ideal_composition_01(self):
        # Exact finite rank-one composition models on Q^2:
        # (B(y ell)A) x == By (ell A)x.
        def mv(A,x):
            return tuple(sum(a*b for a,b in zip(row,x)) for row in A)
        matrices = [((1,0),(0,1)),((1,2),(-1,3)),((0,-2),(1,0))]
        vectors = [(1,0),(0,1),(2,-3)]
        for A,B,y,ell,x in product(matrices,matrices,vectors,vectors,vectors):
            T = tuple(tuple(v*c for c in ell) for v in y)
            lhs = mv(B,mv(T,mv(A,x)))
            eA = tuple(sum(ell[i]*A[i][j] for i in range(2)) for j in range(2))
            By = mv(B,y)
            rhs = tuple(v*sum(c*t for c,t in zip(eA,x)) for v in By)
            self.assertEqual(lhs,rhs)

if __name__ == "__main__":
    unittest.main()
