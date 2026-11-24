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

    def test_FA21_associativity_and_derivative_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\langle S_y,\langle T_x,\Phi(x,y)\rangle\rangle",
            r"A_{T*S}=A_S A_T",
            r"\langle U,A_S A_T\varphi\rangle",
            r"(U*T)*S",
            r"(U*S)*T",
            r"\mathcal D_{K-a}",
            r"A_{\delta_a}\varphi(y)=\varphi(a+y)",
            r"\langle\partial_jT,f\rangle",
            r"(\partial_j\chi)f",
            r"\partial^{\alpha+\beta}\varphi(0)",
        ):
            self.assertIn(fragment, s)

        # Each entry (point, derivative order, coefficient) represents
        # a signed derivative of a Dirac distribution.
        def conv(P, Q):
            result = {}
            for (a,n),c in P.items():
                for (b,m),d in Q.items():
                    key = (a+b,n+m)
                    result[key] = result.get(key,0)+c*d
            return {key:c for key,c in result.items() if c}
        def deriv(P):
            return {(a,n+1):c for (a,n),c in P.items()}
        def act(P, f, z=0):
            return sum(c*(-1)**n*sum(v*falling(i,n)*(a+z)**(i-n)
                       for i,v in enumerate(f) if i >= n)
                       for (a,n),c in P.items())
        from math import comb
        def test_operator(P, f):
            return [sum(c*(-1)**n*sum(v*falling(i,n)*comb(i-n,j)*a**(i-n-j)
                       for i,v in enumerate(f) if i >= n+j)
                       for (a,n),c in P.items()) for j in range(len(f))]
        models = [{}, {(0,0):1}, {(-1,0):2,(2,1):-3},
                  {(0,0):1,(1,0):-1}, {(-2,2):1,(1,1):2}]
        for P,Q,U in product(models, repeat=3):
            self.assertEqual(conv(conv(P,Q),U), conv(P,conv(Q,U)))
        for P,Q in product(models, repeat=2):
            self.assertEqual(conv(P,Q),conv(Q,P))
            self.assertEqual(deriv(conv(P,Q)),conv(deriv(P),Q))
            self.assertEqual(deriv(conv(P,Q)),conv(P,deriv(Q)))
            for f,z in product(([1],[0,1],[1,-2,3,0,2]),[-2,0,3]):
                self.assertEqual(act(conv(P,Q),f,z),
                                 act(Q,test_operator(P,f),z))

if __name__ == "__main__":
    unittest.main()
