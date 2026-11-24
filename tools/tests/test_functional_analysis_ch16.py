"""Structural and exact finite-dimensional regressions for chapter 16."""
from fractions import Fraction as F
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/functional_analysis"
SOURCE = DIR / "16-funkcjonaly-wypukle-i-podstawy-rachunku-wariacyjnego.tex"

class Chapter16(unittest.TestCase):
    def test_environment_balance(self):
        stack = []
        for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", SOURCE.read_text(encoding="utf-8")):
            if kind == "begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), name)
        self.assertFalse(stack)

    def test_unique_labels_and_context_references(self):
        source = SOURCE.read_text(encoding="utf-8")
        source = re.sub(r"(?m)^%.*$", "", source)
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), 19)
        self.assertEqual(len(set(labels)), len(labels))
        context = "\n".join(p.read_text(encoding="utf-8") for p in DIR.glob("*.tex")
                            if int(p.name[:2]) <= 17)
        refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]", source)
        for a,b in refs:
            self.assertIn(r"\label{" + (a or b) + "}", context)

    def test_effective_domain_and_direct_method_contracts(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\operatorname{dom}J=\{x\in C:J(x)<+\infty\}",
            r"x,y\in\operatorname{dom}J",
            r"\sup_\alpha\inf_{\beta\ge\alpha}J(x_\beta)",
            r"m\le J(u_n)<m+1/n",
            r"2M\|v-w\|+|\langle x_{n_k}-x,w\rangle|",
            r"\hyperref[ex:positive-hessian15]",
            r"\ref{cor:weak-convex-closure}",
        ):
            self.assertIn(fragment, source)

    def test_quadratic_tangent_and_strong_convexity(self):
        # J(x)=1/2 (2x_1^2+5x_2^2)+3x_1-x_2.
        # Strong convexity constant 2. All arithmetic exact.
        points = [(F(i,2),F(j,3)) for i in range(-2,3) for j in range(-2,3)]
        def J(x):
            return (2*x[0]**2+5*x[1]**2)/2+3*x[0]-x[1]
        def grad(x):
            return (2*x[0]+3,5*x[1]-1)
        for x in points:
            for y in points:
                h = tuple(b-a for a,b in zip(x,y))
                norm2 = sum(v*v for v in h)
                residual = J(y)-J(x)-sum(a*b for a,b in zip(grad(x),h))
                self.assertGreaterEqual(residual, norm2)
                for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                    z = tuple((1-t)*a+t*b for a,b in zip(x,y))
                    self.assertGreaterEqual((1-t)*J(x)+t*J(y)-J(z),t*(1-t)*norm2)
        xstar = (F(-3,2),F(1,5))
        self.assertEqual(grad(xstar),(0,0))
        for x in points:
            self.assertGreaterEqual(J(x),J(xstar))

    def test_positive_hessian_counterexample(self):
        # Exact values of the counterexample already proved in chapter 15.
        for n in range(1,101):
            t=F(1,n)
            self.assertEqual(t*t/(2*n)-t**3,-F(1,2*n**3))
            self.assertLess(t*t/(2*n)-t**3,0)


    def test_FA16_SUBGRAD_ZERO_01(self):
        # At p=0 the substitution v=p must still be defined.
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"podstawiając $v=p$", source)
        self.assertNotIn(r"v=tp/\|p\|", source)
        for p in (F(0), F(1,2), F(1), F(3,2), F(-2)):
            self.assertEqual(p*p <= abs(p), abs(p) <= 1)

    def test_FA16_DIRICHLET_REMAINDER_01(self):
        # u=a*x*(1-x), h=b*x*(1-x), f=c constant.
        # Integral of (1-2*x)^2 = 1/3; integral of x*(1-x) = 1/6.
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"+\tfrac12\|h\|_H^2", source)
        self.assertIn(r"jej obraz jest zupełny", source)
        for a in map(F, range(-3,4)):
            for b in (F(0), F(1,2), F(-1,3), F(2)):
                for c in map(F, range(-2,3)):
                    def J(t):
                        return t*t/6-c*t/6
                    derivative = a*b/3-c*b/6
                    self.assertEqual(J(a+b)-J(a)-derivative,b*b/6)


    def test_FA16_PROBABILITY_EXTREME_01(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"\ref{thm:krein-milman}", r"\ref{cor:bauer9}",
            r"\ref{cor:alaoglu-norm}", r"\mu(K\setminus S)=0",
            r"\mu_B(B)=1", r"\mu_{K\setminus B}(B)=0",
        ):
            self.assertIn(fragment, source)
        # All probability vectors on three atoms with denominator 8.
        for i in range(9):
            for j in range(9-i):
                p = (F(i,8), F(j,8), F(8-i-j,8))
                if max(p) == 1:
                    self.assertEqual(sum(v != 0 for v in p), 1)
                    continue
                k = next(k for k,v in enumerate(p) if 0 < v < 1)
                t = p[k]
                q = tuple(F(int(l == k)) for l in range(3))
                r = tuple(F(0) if l == k else p[l]/(1-t) for l in range(3))
                self.assertEqual(sum(q), 1)
                self.assertEqual(sum(r), 1)
                self.assertNotEqual(q,r)
                self.assertEqual(tuple(t*a+(1-t)*b for a,b in zip(q,r)),p)
                phi = (F(-2),F(1),F(4))
                self.assertLessEqual(sum(a*b for a,b in zip(phi,p)),max(phi))


    def test_FA16_PROXIMAL_EXTENDED_01(self):
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"Poza dziedziną efektywną $\Phi_y(v)=+\infty$", source)
        self.assertIn(r"\lambda^{-1}\langle u-y,v-u\rangle", source)
        # J(v)=v^2/2 for v>=0, +infinity otherwise.
        for lam in (F(1,2), F(1), F(2)):
            for y in map(F, range(-3,4)):
                u = max(F(0),y/(1+lam))
                def phi(v):
                    return v*v/2+(v-y)**2/(2*lam)
                for v in (F(0), F(1,4), F(1), F(2)):
                    self.assertGreaterEqual(phi(v)-phi(u),(v-u)**2/(2*lam))
                for z in map(F, range(-3,4)):
                    w = max(F(0),z/(1+lam))
                    self.assertLessEqual((u-w)**2,(y-z)*(u-w))


    def test_FA16_DIRICHLET_CONVEXITY_01(self):
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\tfrac12t(1-t)\|u-w\|_H^2", source)
        self.assertIn(r"[u'v]_0^1", source)
        # u=a*x*(1-x), w=b*x*(1-x), f=1.
        def J(a):
            return (a*a-a)/6
        for a in map(F, range(-3,4)):
            for b in map(F, range(-3,4)):
                for t in (F(1,4), F(1,2), F(3,4)):
                    self.assertEqual((1-t)*J(a)+t*J(b)-J((1-t)*a+t*b),
                                     t*(1-t)*(a-b)**2/6)
        for a in map(F, range(-3,4)):
            # Integral u'*v' = a/6 = integral v, for u=x*(1-x)/2.
            self.assertEqual(F(1,2)*a/3,a/6)

if __name__ == "__main__":
    unittest.main()
