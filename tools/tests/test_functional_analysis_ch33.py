import itertools
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis"
S = next(DIR.glob("33-*.tex")).read_text(encoding="utf-8")

class Chapter33(unittest.TestCase):
    def test_FA33_structure_01(self):
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
        ctx = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex"))
        for label in re.findall(r"\\ref\{([^}]+)\}", S) + re.findall(r"\\hyperref\[([^\]]+)\]", S):
            self.assertIn(r"\label{" + label + "}", ctx)

    def test_FA33_product_domain_01(self):
        self.assertIn(r"\mu_{g(E)x}(C)", S)
        self.assertIn(r"D(f(E)g(E))=D((fg)(E))", S)
        # Multiplication by n is unbounded on l2; x_n=1/n belongs to l2
        # but not to D(M_n), whereas M_(1/n)x lies in D(M_n).
        for n in range(1, 101):
            x, f, g = F(1,n), n, F(1,n)
            self.assertEqual(f * (g * x), x)
            self.assertEqual((f*x)**2, 1)
            self.assertEqual((f*g*x)**2, F(1,n*n))

    def test_FA33_cayley_01(self):
        for token in (r"P(C\cap\sigma(U))",r"Q(\sigma(U))=I_H",r"g_z(E)H\subseteq D(A)"):
            self.assertIn(token,S)
        # Exact rational real and imaginary parts of (t-i)/(t+i).
        for t in map(F, range(-30,31)):
            a, b = (t*t-1)/(t*t+1), -2*t/(t*t+1)
            self.assertEqual(a*a+b*b,1)
            self.assertNotEqual((a,b),(1,0))
            self.assertEqual(-2*b/((1-a)**2+b*b),t)

    def test_FA33_resolvent_support_01(self):
        for token in (r"\lambda-\varepsilon/2",r"|t-\lambda|\ge\delta",
                      r"\operatorname{Ran}(A-zI)^\perp=\ker(A^*-\overline z I)"):
            self.assertIn(token,S)
        for t,z in itertools.product(range(-10,11),repeat=2):
            if t != z:
                g=F(1,t-z)
                self.assertEqual((t-z)*g,1)
                self.assertEqual(t*g,1+z*g)

    def test_FA33_boundary_01(self):
        for token in (r"|f(0)|,|f(1)|",r"q=Vv",r"|f(t)|^2",
                      r"\gamma(f)=(f(0),f(1))"):
            self.assertIn(token,S)
        for phase in (1,-1,1j,-1j):
            for a,c in itertools.product((0,1,-1,1j,-1j,1+1j),repeat=2):
                b,d=phase*a,phase*c
                self.assertEqual(b*d.conjugate()-a*c.conjugate(),0)
            for a,b in itertools.product((0,1,-1,1j,-1j),repeat=2):
                self.assertEqual(phase*b.conjugate()-a.conjugate()==0,b==phase*a)

    def test_FA33_stone_01(self):
        for token in (r"4\lambda^2",r"A+iI=i(I_H-G)",r"A-iI=-i(I_H+G)",
                      r"\phi(t-s)-\phi(t)"):
            self.assertIn(token,S)
        for a in range(-20,21):
            G=1j*a
            self.assertEqual(a+1j,1j*(1-G))
            self.assertEqual(a-1j,-1j*(1+G))

    def test_FA33_fourier_and_graph_01(self):
        for token in (r"thm:plancherel22",r"D(M_\xi)",r"G(A^{**})=\overline{G(A)}",
                      r"n^{-1}\eta'"):
            self.assertIn(token,S)

if __name__ == "__main__":
    unittest.main()
