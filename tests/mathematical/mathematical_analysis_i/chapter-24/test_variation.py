from fractions import Fraction as F
from math import exp
from pathlib import Path
import unittest

class Chapter24(unittest.TestCase):
    def test_first_derivative_signs(self):
        for h in (F(1,10),F(1,2),F(2)):
            self.assertGreater(abs(h),0)
            self.assertGreater(abs(-h),0)
            self.assertLess((-h)**3,0)
            self.assertGreater(h**3,0)

    def test_continuity_assumption(self):
        for h in (F(1,10),F(1,2)):
            self.assertLess(abs(h),1)
            self.assertLess(abs(-h),1)

    def test_higher_derivative_parity(self):
        for m in range(1,9):
            for c in (-2,3):
                h=F(1,7)
                self.assertEqual(c*(-h)**m,(-1)**m*c*h**m)
                self.assertEqual((c*h**m>0),(c>0))

    def test_flat_extrema_signs(self):
        for x in (-1.,-.5,.5,1.):
            h=exp(-1/x**2)
            self.assertGreater(h,0)
            self.assertLess(-h,0)
            self.assertEqual(x*h>0,x>0)

    def test_slope_not_sufficient(self):
        for k in (2,10,100):
            x=F(k*k)
            f=x+k
            self.assertEqual(f/x,1+F(1,k))
            self.assertEqual(f-x,k)

    def test_rational_derivative_signs(self):
        for x,sign in ((F(-2),1),(F(-1),0),(F(-1,2),-1),
                       (F(1,2),-1),(F(1),0),(F(2),1)):
            d=1-1/x**2
            self.assertEqual(d,(x-1)*(x+1)/x**2)
            self.assertEqual((d>0)-(d<0),sign)

    def test_rational_range_and_asymptote(self):
        for x in (F(1,10),F(1),F(5),F(100)):
            f=x+1/x
            self.assertEqual(f-2,(x-1)**2/x)
            self.assertGreaterEqual(f,2)
            self.assertEqual(-x+1/(-x),-f)
            self.assertEqual(f-x,1/x)
        self.assertEqual(F(1)+1/F(1),2)

    def test_exp_derivative_signs(self):
        for x,s in ((-2,-1),(0,0),(1,1),(2,0),(3,-1)):
            d=x*(2-x)*exp(-x)
            self.assertEqual((d>0)-(d<0),s)
        self.assertAlmostEqual(2**2*exp(-2),4*exp(-2))

    def test_exp_tail_bounds(self):
        for x in (.1,1.,2.,10.,20.):
            self.assertLessEqual(x*x*exp(-x),6/x)
        for x in (-.1,-1.,-10.):
            self.assertGreaterEqual(x*x*exp(-x),x*x)
            self.assertLessEqual(x*exp(-x),x)

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/24-przebieg-zmiennosci-funkcji.tex").read_text(encoding="utf8")
        self.assertEqual(s.count(r"plot (\x,{\x+1/\x})"),2)
        self.assertIn("domain=.22:4",s)
        self.assertIn("domain=-4:-.22",s)
        self.assertIn("(-4.2,-4.2)--(4.2,4.2)",s)
        self.assertIn("(1,2) circle",s)
        self.assertIn("(-1,-2) circle",s)
        self.assertIn(r"plot (\x,{\x*\x*exp(-\x)})",s)
        self.assertIn("(2,{4*exp(-2)}) circle",s)

if __name__=="__main__":
    unittest.main()
