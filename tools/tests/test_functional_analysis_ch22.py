import re
import unittest
from pathlib import Path
from math import comb
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("22-*.tex"))

class Chapter22(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 22)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA22_tempered_embeddings_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"(1+\max_{x\in K}|x|)^N p_m(\varphi)",
            r"T|_{\mathcal D}=T\circ j",
            r"2^{k(d+M-N)}",
            r"\mathrm d|\mu|(x)",
            r"Q_{N,m}(g-\chi(\cdot/R)g)",
            r"R^d\lambda_d(B(0,1))",
            r"P_B(T_f)\le C_d\|f\|_2",
            r"\overline f$ w $L^2$",
            r"P_B(T|_{\mathcal D})=P_{j(B)}(T)",
            r"\ref{lem:compact-action21}",
        ):
            self.assertIn(fragment, s)
        # Exact dyadic tail ratios for all integer exponent models.
        for d,M,extra in product(range(1,7),range(6),range(1,5)):
            N = d+M+extra
            ratio = F(2)**(d+M-N)
            self.assertTrue(0 < ratio < 1)
            self.assertEqual(sum(ratio**k for k in range(8)),
                             (1-ratio**8)/(1-ratio))

    def test_FA22_multiplier_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"M_m=\max_{|\gamma|\le m}M_\gamma",
            r"\binom\beta\gamma C_\gamma",
            r"Q_{N,m}(a\varphi)\le C_m Q_{N+M_m,m}(\varphi)",
            r"P_B(A^{\mathrm t}T)=P_{A(B)}(T)",
            r"A\varphi=(-1)^{|\alpha|}",
        ):
            self.assertIn(fragment,s)
        # Polynomial jets at a point: derivative of a product.
        def jet(p,k,x):
            return sum(v*comb(i,k)*x**(i-k) for i,v in enumerate(p) if i>=k)
        polys = [[1], [1,-2,3], [0,1,0,-3,1]]
        for a,b,x,k in product(polys,polys,[-2,0,3],range(7)):
            ab = [0]*(len(a)+len(b)-1)
            for i,u in enumerate(a):
                for j,v in enumerate(b):
                    ab[i+j] += u*v
            self.assertEqual(jet(ab,k,x),
                             sum(jet(a,j,x)*jet(b,k-j,x) for j in range(k+1)))

    def test_FA22_montel_and_topologies_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\|x-y\|_1\sup_{\psi\in B}Q_{0,m+1}(\psi)",
            r"Q_{N+1,m}(\varphi_{n_k})",
            r"w domknięciu $B$ wybieramy $f_n\in B$",
            r"\sup_n|\langle T_n-T,v\rangle|",
            r"e^{-n^2}(2+3n)^N Q_{0,m}(\psi)",
            r"\mathcal S/M",
            r"T(\psi_n)=1",
        ):
            self.assertIn(fragment,s)
        self.assertNotIn("równoodległościowość",s)
        self.assertNotIn("sekwencyjna",s)

if __name__ == "__main__":
    unittest.main()
