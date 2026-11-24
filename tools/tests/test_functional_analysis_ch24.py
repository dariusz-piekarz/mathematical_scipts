import re
import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = next(DIR.glob("24-*.tex"))

class Chapter24(unittest.TestCase):
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
                            if p.name[:2].isdigit() and int(p.name[:2]) <= 24)
        for a,b in re.findall(r"\\ref\{([^}]+)\}|\\hyperref\[([^\]]+)\]", s):
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_FA24_algebraic_and_projective_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"V/N",
            r"iloraz jest zerowy",
            r"e_i'\otimes I_{F_0}",
            r"P\otimes Q",
            r"\sum_i g_i(y)f_i=0",
            r"h(i,j)=\delta_{ij}",
            r"\pi_{p,q}(x\otimes y)=p(x)q(y)",
            r"p(x-x_0)q(y-y_0)",
            r"s(b(x,y))\le p(x)q(y)",
            r"s(\widetilde b(u))\le\pi_{p,q}(u)",
        ):
            self.assertIn(fragment,s)

    def test_FA24_injective_01(self):
        s = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ell\in E',\ m\in F'",
            r"wartość sumy jest niezależna",
            r"\varepsilon_{p,q}\le\pi_{p,q}",
            r"\varepsilon_{p,q}(u)\ge|(\ell\otimes m)(u)|>0",
            r"\varepsilon_{X,Y}(u)\le",
            r"\|e_i'\|\varepsilon(u)",
            r"\varepsilon(u)\le\pi(u)\le\sum_{i=1}^n\|e_i\|\|y_i\|",
            r"\varepsilon(v_N)=1/N\to0",
            r"\pi(v_N)=1",
        ):
            self.assertIn(fragment,s)

    def test_FA24_finite_l1_models_01(self):
        # On l1^2 x l1^2, epsilon is the maximum over sign vectors.
        # Pi equals the entrywise l1 norm, as certified by a sign matrix.
        signs = list(product((-1,1),repeat=2))
        for a,b,c,d in product(range(-2,3),repeat=4):
            M=((a,b),(c,d))
            eps=max(abs(sum(u[i]*M[i][j]*v[j] for i in range(2) for j in range(2)))
                    for u,v in product(signs,repeat=2))
            pi=sum(abs(x) for row in M for x in row)
            S=tuple(tuple((x>0)-(x<0) for x in row) for row in M)
            self.assertEqual(sum(S[i][j]*M[i][j] for i in range(2) for j in range(2)),pi)
            self.assertLessEqual(eps,pi)
            self.assertGreaterEqual(eps,max(abs(x) for row in M for x in row))
        # Elementary tensors and coordinate projections.
        vectors=list(product(range(-2,3),repeat=2))
        for x,y in product(vectors,repeat=2):
            M=tuple(tuple(a*b for b in y) for a in x)
            eps=max(abs(sum(u[i]*M[i][j]*v[j] for i in range(2) for j in range(2)))
                    for u,v in product(signs,repeat=2))
            self.assertEqual(eps,sum(map(abs,x))*sum(map(abs,y)))
            for i in range(2):
                self.assertLessEqual(sum(map(abs,M[i])),eps)

if __name__ == "__main__":
    unittest.main()
