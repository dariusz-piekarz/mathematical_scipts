from fractions import Fraction as F
from math import comb, factorial, sin, cos, pi
from pathlib import Path
import unittest

def derivative(p):
    return [i * p[i] for i in range(1, len(p))] or [0]

def nth(p, n):
    for _ in range(n):
        p = derivative(p)
    return p

def val(p, x):
    return sum(c * x**i for i, c in enumerate(p))

def product(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

class Chapter22(unittest.TestCase):
    def test_linearity(self):
        p, q = [1, 2, 3, 4], [-2, 1, 0, 5]
        for n in range(7):
            self.assertEqual(nth([2*a-3*b for a,b in zip(p,q)], n),
                             [2*a-3*b for a,b in zip(nth(p,n),nth(q,n))])

    def test_leibniz(self):
        p, q = [2,-3,1], [1,0,4,-2]
        for n in range(9):
            for x in (F(-2), F(1,3), F(0), F(2)):
                self.assertEqual(val(nth(product(p,q),n),x),
                    sum(comb(n,k)*val(nth(p,k),x)*val(nth(q,n-k),x) for k in range(n+1)))

    def test_polynomial_exp_coefficients(self):
        p = [0,0,1]
        for n in range(10):
            self.assertEqual(p,[n*(n-1),2*n,1])
            d = derivative(p)
            p = [c+(d[i] if i<len(d) else 0) for i,c in enumerate(p)]

    def test_monomial(self):
        for p in range(8):
            for n in range(10):
                expected = [0]*(p-n)+[factorial(p)//factorial(p-n)] if n<=p else [0]
                self.assertEqual(nth([0]*p+[1],n),expected)

    def test_log_coefficients(self):
        c = 1
        for n in range(1,10):
            self.assertEqual(c,(-1)**(n-1)*factorial(n-1))
            c *= -n

    def test_trigonometric_phase(self):
        for n in range(8):
            for t in (-1.2, 0.0, 2.1):
                self.assertAlmostEqual(sin(t+n*pi/2), [sin(t),cos(t),-sin(t),-cos(t)][n%4])
                self.assertAlmostEqual(cos(t+n*pi/2), [cos(t),-sin(t),-cos(t),sin(t)][n%4])

    def test_composition_second_third(self):
        # f(t)=t^3, g(x)=x^2+1, exact polynomial composition
        g = [1,0,1]
        p = product(product(g,g),g)
        for x in (F(-2),F(0),F(2,3)):
            t, gp, gpp = x*x+1, 2*x, 2
            self.assertEqual(val(nth(p,2),x),6*t*gp**2+3*t*t*gpp)
            self.assertEqual(val(nth(p,3),x),6*gp**3+18*t*gp*gpp)

    def test_inverse_second(self):
        # f(x)=1/x for x>0, h=f, check formula without division by zero
        for y in (F(1,3),F(1),F(5)):
            h=1/y
            self.assertEqual(- (2/h**3) / (-1/h**2)**3, 2/y**3)

    def test_strict_hierarchy(self):
        for m in range(8):
            p=[0]*(m+1)+[1]
            for h in (F(1,7), F(1,31)):
                self.assertEqual(val(nth(p,m),h)/h,factorial(m+1))
                self.assertEqual(-val(nth(p,m),-h)/(-h),-factorial(m+1))

    def test_discontinuous_second(self):
        # At the two specified phases the cosine term vanishes exactly.
        for k in (10,100,1000):
            x=1/(pi/2+2*k*pi)
            y=1/(3*pi/2+2*k*pi)
            self.assertLess(abs((12*x*x-1)+1), 1/k)
            self.assertLess(abs((-12*y*y+1)-1), 1/k)

    def test_mechanics(self):
        for x in (F(0),F(1,2),F(2)):
            self.assertEqual(val(nth([0,0,1],1),x),2*x)
            self.assertEqual(val(nth([0,0,1],2),x),2)

    def test_endpoint_extensions(self):
        # Left and right signed difference quotients of extended derivatives.
        p = [3, -2, 1, 4]
        a, b = F(-1), F(2)
        for j in range(1, 4):
            q = nth(p, j-1)
            dq = nth(p, j)
            for x, sign in ((a, 1), (b, -1)):
                for k in (10, 100, 1000):
                    h = F(sign, k)
                    quotient = (val(q, x+h)-val(q, x))/h
                    self.assertLessEqual(abs(quotient-val(dq,x)), 100*abs(h))

    def test_reciprocal_both_half_axes(self):
        for x in (F(-3), F(-1,2), F(1,2), F(3)):
            for j in range(8):
                c = (-1)**j * factorial(j)
                self.assertEqual(c*(-j-1)*x**(-j-2),
                                 (-1)**(j+1)*factorial(j+1)*x**(-j-2))

    def test_figure_source(self):
        source=(Path(__file__).resolve().parents[4] /
                "chapters/pl/mathematical_analysis_i/22-pochodne-wyzsze.tex").read_text(encoding="utf8")
        self.assertIn(r"plot (\x,{\x*\x})",source)
        self.assertIn("(0,0)--(2,4)",source)
        self.assertIn("(0,2)--(2,2)",source)

if __name__ == "__main__":
    unittest.main()
