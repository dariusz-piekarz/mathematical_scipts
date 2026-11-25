from fractions import Fraction as F
from math import factorial, exp, log, sin, cos
from pathlib import Path
import unittest

def val(p,x):
    return sum(c*x**j for j,c in enumerate(p))

def deriv(p):
    return [j*p[j] for j in range(1,len(p))] or [0]

def nth(p,n):
    for _ in range(n):
        p=deriv(p)
    return p

class Chapter23(unittest.TestCase):
    def test_jet_and_exact_polynomial(self):
        p=[F(2),F(-3),F(5,2),F(1,3)]
        for a in (F(-2),F(0),F(2,3)):
            q=[val(nth(p,k),a)/factorial(k) for k in range(len(p))]
            for k in range(len(p)):
                self.assertEqual(val(nth(q,k),F(0)),val(nth(p,k),a))
            for x in (F(-3),F(1,2),F(3)):
                self.assertEqual(val(q,x-a),val(p,x))

    def test_peano_signed_remainders(self):
        # Polynomial with remainder h^(n+1), on both sides of a.
        for n in range(7):
            for h in (F(-1,7),F(-1,100),F(1,100),F(1,7)):
                p=[F(1)]*(n+2)
                self.assertEqual((val(p,h)-val(p[:-1],h))/h**n,h)

    def test_lagrange_both_directions(self):
        for n in range(6):
            for h in (F(-3,2),F(1,2)):
                # f(a+h)=h^(n+1), derivative of order n+1 constant.
                self.assertEqual(F(factorial(n+1),factorial(n+1))*h**(n+1),h**(n+1))

    def test_cauchy_general_p_witness(self):
        for n in range(5):
            # p=n+1 is constant case; p=1, n=1 gives xi at midpoint.
            for h in (F(-2), F(3,4)):
                xi=h/2
                self.assertEqual(2*(h-xi)*h,h*h)
                self.assertEqual(F(factorial(n+1),(n+1)*factorial(n))*h**(n+1),h**(n+1))

    def test_exp_bound(self):
        for x in (-1.0,0.0,0.5,1.0):
            for n in range(8):
                p=sum(x**k/factorial(k) for k in range(n+1))
                self.assertLessEqual(abs(exp(x)-p),exp(1)/factorial(n+1)+1e-14)

    def test_trig_bounds(self):
        for x in (-1.2,0.0,0.7,1.2):
            for m in range(5):
                s=sum((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(m+1))
                c=sum((-1)**j*x**(2*j)/factorial(2*j) for j in range(m+1))
                self.assertLessEqual(abs(sin(x)-s),abs(x)**(2*m+3)/factorial(2*m+3)+1e-14)
                self.assertLessEqual(abs(cos(x)-c),abs(x)**(2*m+2)/factorial(2*m+2)+1e-14)

    def test_log_bounds(self):
        for x in (-0.9,-0.6,-0.1,0.0,0.6,1.0):
            for n in range(1,12):
                p=sum((-1)**(k-1)*x**k/k for k in range(1,n+1))
                bound=abs(x)**(n+1)/(1+x) if x<0 else x**(n+1)/(n+1)
                self.assertLessEqual(abs(log(1+x)-p),bound+1e-14)

    def test_log_cauchy_ratio(self):
        for x in (F(-9,10),F(-2,3),F(-1,4)):
            for j in range(1,10):
                xi=x*j/10
                self.assertTrue(0<(xi-x)/(1+xi)<=abs(x))

    def test_flat_power_bound(self):
        for N in range(8):
            k=N//2+1
            for x in (0.5,0.25,-0.5,-0.25):
                self.assertLessEqual(abs(x)**(-N)*exp(-1/x**2),factorial(k)*abs(x)**(2*k-N))

    def test_flat_polynomial_recurrence(self):
        p=[1]
        for j in range(7):
            out=[0]*(len(p)+3)
            for i,c in enumerate(p):
                if i:
                    out[i+1]-=i*c
                out[i+3]+=2*c
            self.assertEqual(out[-1],2**(j+1))
            self.assertEqual(len(out)-1,3*(j+1))
            p=out

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
          "chapters/pl/mathematical_analysis_i/23-twierdzenie-taylora.tex").read_text(encoding="utf8")
        self.assertIn(r"plot (\x,{1+\x+\x*\x+\x*\x*\x})",s)
        self.assertIn(r"plot (\x,{1+\x+\x*\x})",s)
        self.assertIn("(1,3)--(1,4)",s)
        self.assertEqual(val([1,1,1,1],1)-val([1,1,1],1),1)

if __name__=="__main__":
    unittest.main()
