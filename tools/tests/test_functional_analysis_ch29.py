import itertools
import re
import unittest
from pathlib import Path
from fractions import Fraction as F

DIR = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis"
S = next(DIR.glob("29-*.tex")).read_text(encoding="utf-8")

class Chapter29(unittest.TestCase):
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
        ctx = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                        if p.name[:2].isdigit() and int(p.name[:2]) <= 29)
        for ref in re.findall(r"\\ref\{([^}]+)\}", S):
            self.assertIn(r"\label{" + ref + "}", ctx)

    def test_FA29_riesz_and_cover_01(self):
        self.assertIn(r"\operatorname{dist}(x,M)\ge d/\|z-y\|>\theta", S)
        self.assertIn(r"$\varepsilon/3$-siatkę tej rodziny", S)
        self.assertIn(r"$2\varepsilon/3$", S)
        for eps in (F(1,7), F(1), F(5,2)):
            self.assertLess(2*eps/3, eps)

    def test_FA29_adjoint_01(self):
        self.assertIn(r"(T''J_Xx)(y')=(J_Xx)(T'y')", S)
        self.assertIn(r"\sup_{\|x\|\le1}\|Tx\|=\|T\|", S)
        for a,b,c,d in itertools.product(range(-1,2), repeat=4):
            for x,y,u,v in itertools.product(range(-1,2), repeat=4):
                self.assertEqual(u*(a*x+b*y)+v*(c*x+d*y),
                                 (a*u+c*v)*x+(b*u+d*v)*y)

    def test_FA29_weak_classes_01(self):
        for phrase in (r"\|e_n-e_m\|_1=2", r"\|e_n-e_m\|_2=\sqrt2",
                       r"e_n\rightharpoonup0", "Jest także całkowicie ciągłe",
                       "dopełnienie kuli"):
            self.assertIn(phrase,S)

    def test_FA29_diagonal_01(self):
        self.assertIn(r"\|D_ae_n\|=|a_n|", S)
        self.assertIn(r"\|e_n\|\le C\|D_ae_n\|=C/n", S)
        for a in itertools.product(range(-2,3),repeat=4):
            for N in range(4):
                self.assertEqual(max(abs(a[j]) if j>=N else 0 for j in range(4)),
                                 max(map(abs,a[N:])))

    def test_FA29_kernel_01(self):
        for phrase in ("nie zależy od reprezentantów", r"\|\chi_E-\chi_R\|_2^2=\lambda_2(E\triangle R)",
                       r"\|T_k-T_{k_n}\|\le\|k-k_n\|_2"):
            self.assertIn(phrase,S)
        for a,b,c,d in itertools.product(range(-2,3),repeat=4):
            for x,y in itertools.product(range(-2,3),repeat=2):
                self.assertLessEqual((a*x+b*y)**2+(c*x+d*y)**2,
                                     (a*a+b*b+c*c+d*d)*(x*x+y*y))
        sets=[set(i for i in range(4) if m&(1<<i)) for m in range(16)]
        for A,B in itertools.product(sets,repeat=2):
            self.assertEqual(sum((int(i in A)-int(i in B))**2 for i in range(4)),len(A^B))

    def test_FA29_ideals_01(self):
        self.assertIn(r"\mathcal F(X,Y)$", S)
        self.assertIn(r"\|ST_nR-STR\|\le\|S\|\|T_n-T\|\|R\|", S)
        self.assertIn(r"\|I_X-K\|<1", S)

if __name__ == "__main__":
    unittest.main()
