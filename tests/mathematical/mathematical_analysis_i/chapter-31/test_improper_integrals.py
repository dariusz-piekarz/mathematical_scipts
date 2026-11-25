from fractions import Fraction as F
from math import exp, log, pi, sin, cos
from pathlib import Path
import unittest


class Chapter31(unittest.TestCase):
    def test_power_integrals_at_infinity(self):
        for p in (2,3,4,5):
            for R in map(F,(2,5,10,100)):
                truncated=(1-R**(1-p))/(p-1)
                self.assertGreaterEqual(truncated,0)
                self.assertEqual(F(1,p-1)-truncated,R**(1-p)/(p-1))
        for R in map(F,(2,5,10)):
            self.assertEqual((R**2-1)/2,(R-1)*(R+1)/2)

    def test_power_integrals_at_zero(self):
        for p in (-3,-2,-1,0):
            for e in (F(1,2),F(1,10),F(1,100)):
                truncated=(1-e**(1-p))/(1-p)
                self.assertEqual(F(1,1-p)-truncated,e**(1-p)/(1-p))
        for p in (2,3,4):
            e=F(1,100)
            self.assertGreater((1-e**(1-p))/(1-p),F(10))

    def test_logarithmic_border(self):
        for n in (1,2,5,10):
            R=exp(n)
            e=exp(-n)
            self.assertAlmostEqual(log(R),n)
            self.assertAlmostEqual(-log(e),n)
        for t in (1.,2.,5.):
            R=exp(t)
            self.assertAlmostEqual(1-1/log(R),1-1/t)

    def test_splitting_independent_regular_point(self):
        # Primitive of 1/(1+x)^2 on [0,infinity).
        H=lambda x:-1/(1+x)
        for c,d,R in ((F(1),F(2),F(10)),(F(2),F(7),F(100))):
            self.assertEqual(H(d)-H(0),H(c)-H(0)+H(d)-H(c))
            self.assertEqual(H(R)-H(d),H(R)-H(c)-(H(d)-H(c)))
            self.assertEqual(H(c)-H(0)+H(R)-H(c),H(R)-H(0))

    def test_reflection_preserves_tagged_sums(self):
        p=[F(-3),F(-1),F(0),F(2,3),F(4)]
        tags=[F(-2),F(0),F(1,3),F(4)]
        # Discontinuous at zero, with a distinguished point value.
        def f(x):
            return F(7) if x==0 else x if x<0 else 2*x
        q=[-x for x in reversed(p)]
        reflected_tags=[-t for t in reversed(tags)]
        self.assertEqual(max(b-a for a,b in zip(p,p[1:])),
                         max(b-a for a,b in zip(q,q[1:])))
        self.assertEqual(sum(f(t)*(b-a) for a,b,t in zip(p,p[1:],tags)),
                         sum(f(-t)*(b-a) for a,b,t in zip(q,q[1:],reflected_tags)))
        self.assertEqual([-t for t in reversed(reflected_tags)],tags)

    def test_cauchy_tails_at_both_types_of_endpoint(self):
        for n in (2,5,10,100):
            for u,v in ((F(n),F(2*n)),(F(n),F(n*n))):
                self.assertTrue(0<=1/u-1/v<=F(1,n))
            # Integral of (1-x)^(-1/2) up to x=1-1/n^2.
            u,v=F(1)-F(1,n*n),F(1)-F(1,4*n*n)
            self.assertTrue(u<v<1)
            self.assertEqual(2*F(1,n)-2*F(1,2*n),F(1,n))

    def test_positive_comparison_witnesses(self):
        for u,v in ((F(1),F(2)),(F(2),F(10)),(F(10),F(100))):
            # x^-3 <= x^-2 on [1,infinity)
            a=(1/u**2-1/v**2)/2
            b=1/u-1/v
            self.assertTrue(0<=a<=b)

    def test_absolute_tail_triangle_inequality(self):
        # f=x on [-2,3], split at zero.
        for a,b in ((F(-2),F(3)),(F(-3),F(1))):
            signed=(b*b-a*a)/2
            absolute=(a*a+b*b)/2
            self.assertLessEqual(abs(signed),absolute)

    def test_dirichlet_variation_bound_both_signs(self):
        for sign in (-1,1):
            for u,v in ((F(1),F(2)),(F(3),F(10))):
                gu,gv=sign/u,sign/v
                self.assertEqual(abs(gv-gu),abs(gu)-abs(gv))
                self.assertEqual(2*(abs(gu)+abs(gv))+2*abs(gv-gu),4*abs(gu))

    def test_dirichlet_sine_primitive_bound(self):
        for n in range(1,50):
            self.assertLessEqual(abs(cos(1)-cos(n*pi/7)),2)
        for j in range(1,9):
            self.assertGreaterEqual(sum(F(1,n) for n in range(2**j,2**(j+1))),F(1,2))

    def test_abel_decomposition(self):
        for x in map(F,(1,2,5,20)):
            f=1/x**2
            g=3-1/x
            self.assertEqual(f*g,f*(g-3)+3*f)
            self.assertLessEqual(abs(g-3),1/x)

    def test_principal_value_asymmetric_cut(self):
        for k in (.25,.5,1.,2.,4.):
            for eta in (.01,.001,.0001):
                self.assertAlmostEqual(log(k*eta)-log(eta),log(k))
        for R in (1.,10.,100.):
            self.assertEqual(-log(1+R*R)/2+log(1+R*R)/2,0)

    def test_substitution_finite_to_infinite(self):
        # x=t/(1-t) maps [0,1) to [0,infinity).
        for t in (F(0),F(1,4),F(1,2),F(9,10),F(99,100)):
            x=t/(1-t)
            derivative=1/(1-t)**2
            self.assertEqual(derivative/(1+x)**2,1)
            self.assertEqual(1-1/(1+x),t)

    def test_substitution_with_flat_interval(self):
        # phi(t)=0 on [0,1], (t-1)^2 on [1,infinity): C1, not injective.
        for t in (F(0),F(1,2),F(1),F(2),F(3),F(10)):
            x=max(F(0),t-1)**2
            derivative=2*max(F(0),t-1)
            # Exact derivative of 1-1/(1+phi(t)), including the flat branch.
            expected=F(0) if t<=1 else 2*(t-1)/(t*t-2*t+2)**2
            self.assertEqual(derivative/(1+x)**2,expected)
            if t<=1:
                self.assertEqual(1-1/(1+x),0)
        for r in map(F,(1,4,9,16)):
            from math import isqrt
            T=1+F(isqrt(r.numerator))
            self.assertEqual((T-1)**2,r)
            self.assertEqual(1-1/(1+(T-1)**2),1-1/(1+r))

    def test_parts_exponential_truncation(self):
        for R in (.5,1.,2.,10.,20.):
            value=1-(R+1)*exp(-R)
            self.assertAlmostEqual(value,-R*exp(-R)+(1-exp(-R)))
            self.assertLessEqual(R*exp(-R),2/R)
        self.assertAlmostEqual(1-21*exp(-20),1,places=6)

    def test_figure_source_and_area(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/31-calki-niewlasciwe.tex").read_text(encoding="utf8")
        for token in (r"plot (\x,{1/(\x*\x)})",r"plot (\x,{1/\x})",r"1-1/R"):
            self.assertIn(token,s)
        self.assertEqual(1-F(1,6),F(5,6))


if __name__=="__main__":
    unittest.main()
