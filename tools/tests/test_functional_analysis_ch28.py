import itertools
import re
import unittest
from pathlib import Path
from fractions import Fraction as F

DIR = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis"
S = next(DIR.glob("28-*.tex")).read_text(encoding="utf-8")

class Chapter28(unittest.TestCase):
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
                        if p.name[:2].isdigit() and int(p.name[:2]) <= 28)
        for ref in re.findall(r"\\ref\{([^}]+)\}", S):
            self.assertIn(r"\label{" + ref + "}", ctx)

    def test_FA28_uniform_margin_01(self):
        for phrase in (r"\sup_{x\in K}\|Tx-x\|\le2\varepsilon/3<\varepsilon",
                       r"\sup_{x\in K}\|x-P_Ex\|\le\varepsilon/2<\varepsilon",
                       r"\|Tx^{(s)}-x^{(s)}\|_\infty\le\varepsilon/2<\varepsilon"):
            self.assertIn(phrase, S)
        for lam, eps in itertools.product((F(1), F(2), F(7,3)), (F(1,9), F(2), F(5,3))):
            radius = eps/(3*(1+lam))
            self.assertEqual((1+lam)*radius+eps/3, 2*eps/3)
            self.assertLess(2*(eps/4), eps)

    def test_FA28_interpolation_01(self):
        self.assertIn(r"L_nf(t)=(1-\theta)f(t_k)+\theta f(t_{k+1})", S)
        self.assertIn(r"\|L_nf-f\|_\infty\le\omega_f(1/n)", S)
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            for j in range(9):
                t=F(j,8)
                v=(1-t)*a+t*b
                self.assertLessEqual(abs(v), max(abs(a),abs(b)))
                self.assertLessEqual(abs(v-c),max(abs(a-c),abs(b-c)))

    def test_FA28_partition_projection_01(self):
        self.assertIn(r"Ty=\sum_{j=1}^r y_{n_j}\chi_{A_j}", S)
        self.assertIn(r"\|Ty\|_\infty\le\|y\|_\infty", S)
        for x in itertools.product(range(-2,3),repeat=4):
            for partition in ((0,0,1,1),(0,1,0,2),(0,0,0,0),(0,1,2,3)):
                reps={k:partition.index(k) for k in set(partition)}
                def T(v): return tuple(v[reps[k]] for k in partition)
                self.assertEqual(T(T(x)),T(x))
                self.assertLessEqual(max(map(abs,T(x))),max(map(abs,x)))
                self.assertEqual(T((1,)*4),(1,)*4)

    def test_FA28_sequence_density_01(self):
        for phrase in (r"\lambda=\max\{1,\sup_n\|T_n\|\}",
                       r"D=\bigcup_nD_n",r"\|T_nx-x\|<\eta/2",
                       r"\|d-T_nx\|<\eta/2",r"\|d-x\|<\eta"):
            self.assertIn(phrase,S)

    def test_FA28_range_and_compactness_01(self):
        for phrase in (r"\overline{T(B_X)}\times\overline{S(B_X)}",
                       r"\le\sup_{y\in K}\|Sy-y\|<\varepsilon",
                       r"F=S\circ T",r"\|F\|\le\lambda\|T\|"):
            self.assertIn(phrase,S)

    def test_FA28_directed_and_nonseparable_01(self):
        self.assertIn(r"E+F$ jest skończenie wymiarową",S)
        self.assertIn(r"Kule otwarte o promieniu $1/3$",S)
        for a,b in itertools.combinations(itertools.product((0,1),repeat=5),2):
            self.assertEqual(max(abs(u-v) for u,v in zip(a,b)),1)

if __name__ == "__main__":
    unittest.main()
