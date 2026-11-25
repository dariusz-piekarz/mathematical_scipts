from fractions import Fraction as F
from math import cos, sin, pi, exp, log, sqrt
from pathlib import Path
import unittest

class Chapter27(unittest.TestCase):
    def test_darboux_auxiliary_minimum(self):
        for lam in (F(-2),F(0),F(3,2)):
            a,b=F(-2),F(2)
            c=lam/2
            h=lambda x:x*x-lam*x
            self.assertLess(2*a-lam,0)
            self.assertGreater(2*b-lam,0)
            self.assertTrue(a<c<b)
            for x in (a,b,c,F(0),F(1)):
                self.assertEqual(h(x)-h(c),(x-c)**2)

    def test_darboux_reverse_sign(self):
        for lam in (F(-2),F(0),F(2)):
            c=-lam/2
            self.assertTrue(-2<c<2)
            self.assertEqual(-2*c,lam)
            self.assertGreater(F(4),lam)
            self.assertLess(F(-4),lam)

    def test_zero_form_increment_ratio(self):
        for x in (F(-1,5),F(1,5),F(1,100)):
            for y in (x/2,x/3,x/10):
                for sign in (-1,1):
                    g=lambda t:sign*t
                    f=lambda t:3*g(t)+t*t
                    q=(f(x)-f(y))/(g(x)-g(y))
                    self.assertEqual(q,3+sign*(x+y))
                    self.assertEqual(q,3+2*sign*((x+y)/2))

    def test_infinite_denominator_identity(self):
        for sign in (-1,1):
            for x in (F(10),F(100),F(1000)):
                b=F(2)
                g=lambda t:sign*t*t
                f=lambda t:3*g(t)+t+7
                q=(f(x)-f(b))/(g(x)-g(b))
                self.assertEqual(f(x)/g(x)-3,(q-3)*(1-g(b)/g(x))+(f(b)-3*g(b))/g(x))

    def test_infinite_denominator_positive_factor(self):
        for sign in (-1,1):
            for x in (F(10),F(100)):
                g=lambda t:sign*t
                f=lambda t:sign*t*t
                b=F(1)
                q=(f(x)-f(b))/(g(x)-g(b))
                self.assertEqual(f(x)/g(x),q*(1-g(b)/g(x))+f(b)/g(x))
                self.assertGreater(1-g(b)/g(x),F(1,2))

    def test_unbounded_quotient_zero_form(self):
        for x in (F(1,10),F(1,100),F(1,1000)):
            for sign in (-1,1):
                self.assertEqual(sign*x/(x*x),sign/x)
                self.assertEqual(F(sign,1)/(2*x),sign/(2*x))

    def test_nondeterminate_counterexample(self):
        for x in (F(-1,10),F(1,10)):
            self.assertEqual((1+x)/(2+x)-F(1,2),x/(2*(2+x)))
        self.assertNotEqual(F(1,2),1)

    def test_oscillating_derivative_ratio(self):
        for n in (1,5,20,100):
            a,b=1/(2*n*pi),1/((2*n+1)*pi)
            derivative=lambda x:1+2*x*sin(1/x)-cos(1/x)
            self.assertAlmostEqual(derivative(a),0,places=12)
            self.assertAlmostEqual(derivative(b),2,places=12)
            for x in (a,b):
                self.assertLessEqual(abs((1+x*sin(1/x))-1),x+1e-15)

    def test_sqrt_rationalization(self):
        for x in (1.,10.,100.):
            self.assertAlmostEqual(sqrt(x*x+x)-x,1/(sqrt(1+1/x)+1),places=12)

    def test_repeated_rule_example(self):
        # Exact Taylor coefficients at zero, not a numerical limit proof.
        self.assertEqual(F(1,2),F(1,2)/1)
        self.assertEqual(F(1,2),F(1,2)*F(2,2))
        for x in (0.01,-0.01):
            self.assertLess(abs((exp(x)-1-x)/(x*x)-0.5),0.002)

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/27-wlasnosci-pochodnych.tex").read_text(encoding="utf8")
        for token in (r"plot (\x,{(\x-1.5)*(\x-1.5)+.5})",
                      "(.5,1.5)","(1.5,.5)","(2.5,1.5)",
                      r"H'(c)=0"):
            self.assertIn(token,s)

if __name__=="__main__":
    unittest.main()
