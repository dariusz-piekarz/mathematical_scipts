import re
import unittest
from pathlib import Path
from math import prod
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("21-*.tex"))

def falling(n, k):
    return prod(range(n-k+1, n+1)) if k <= n else 0

class Chapter21(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 21)
        for a, b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA21_compact_extension_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\langle T,(\chi_1-\chi_2)f\rangle=0",
            r"$(1-\chi)f$",
            r"\partial^\alpha(\chi f)",
            r"T=F|_{\mathcal D}",
            r"\supp T\subseteq L",
            r"F(f-\chi f)=0",
        ):
            self.assertIn(fragment, s)

    def test_FA21_iterated_actions_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\langle S_y,\partial_x^\alpha\Phi(x,y)\rangle",
            r"C_TC_S p_{m_T+m_S}(\Phi)",
            r"\langle T,u\rangle\langle S,v\rangle",
            r"\rho_\varepsilon(x-u)\sigma_\varepsilon(y-v)",
            r"p_n(F_n-\Phi_{1/n})<1/n",
            r"p_m(F_n-\Phi)\le 1/n+p_m(\Phi_{1/n}-\Phi)",
        ):
            self.assertIn(fragment, s)
        # Exact point-jet models of the two iterated actions, using
        # monomials x**i y**j and derivatives of Dirac distributions.
        for i,j,p,q,a,b in product(range(4), range(4), range(3), range(3), [-2,0,1], [-1,0,2]):
            vx = 0 if p > i else (-1)**p * falling(i,p) * a**(i-p)
            vy = 0 if q > j else (-1)**q * falling(j,q) * b**(j-q)
            # Apply the y action to the coefficient of x**i, and vice versa.
            left = 0 if p > i else (-1)**p * falling(i,p) * (vy * a**(i-p))
            right = 0 if q > j else (-1)**q * falling(j,q) * (vx * b**(j-q))
            self.assertEqual(left, right)

    def test_FA21_support_and_transpose_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\supp(A_T\varphi)\subseteq L-K",
            r"p_{m+r}(\varphi)",
            r"A_T(B)\subseteq tU",
            r"$(\supp\varphi-K)\cap F=\varnothing$",
            r"\supp(A_T\varphi)\cap F=\varnothing",
            r"\supp(T*S)\subseteq K+F",
        ):
            self.assertIn(fragment, s)
        # Finite support models, including empty supports.
        universe = [-2,-1,0,1,2]
        subsets = [{v for i,v in enumerate(universe) if mask & (1 << i)}
                   for mask in range(1 << len(universe))]
        for K,F,L in product(subsets, repeat=3):
            minkowski = {k+f for k in K for f in F}
            difference = {u-k for u in L for k in K}
            self.assertEqual(bool(L & minkowski), bool(difference & F))

if __name__ == "__main__":
    unittest.main()
