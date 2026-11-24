"""Finite numerical and algebraic formula checks, not proofs or TeX parsing."""
import cmath
import math
import unittest
from fractions import Fraction as F


def kernel(t, x, kappa=1.0):
    return math.exp(-x*x/(4*kappa*t))/math.sqrt(4*math.pi*kappa*t)


def midpoint(fn, a, b, count=4096):
    step = (b-a)/count
    return step*math.fsum(fn(a+(j+0.5)*step) for j in range(count))


class HeatTests(unittest.TestCase):
    def test_kernel_equation(self):
        for n in range(1, 9):
            for a in (F(1, 5), F(1), F(3)):
                for t in (F(1, 7), F(1), F(5, 2)):
                    x = [F(j+1, 3) for j in range(n)]
                    dt = -F(n, 2)/t + sum(z*z for z in x)/(4*a*t*t)
                    lap = sum(z*z/(4*a*a*t*t)-1/(2*a*t) for z in x)
                    self.assertEqual(dt, a*lap)

    def test_kernel_normalization_and_l2(self):
        for kappa in (0.3, 1.0, 2.0):
            for t in (0.1, 0.7, 2.0):
                width = 16*math.sqrt(kappa*t)
                self.assertAlmostEqual(midpoint(lambda x: kernel(t,x,kappa), -width,width),1.0,places=11)
                norm2 = midpoint(lambda x: kernel(t,x,kappa)**2,-width,width)
                self.assertAlmostEqual(norm2, (8*math.pi*kappa*t)**(-0.5),places=11)

    def test_semigroup(self):
        for s,t in ((0.1,0.4),(0.5,0.5),(1.,2.)):
            for x in (-2.,0.,0.7):
                width = abs(x)+16*math.sqrt(s+t)
                actual = midpoint(lambda y: kernel(t,x-y)*kernel(s,y),-width,width)
                self.assertAlmostEqual(actual,kernel(t+s,x),places=11)

    def test_halfspace_and_scaling(self):
        for t in (0.01,0.5,2.):
            width=16*math.sqrt(t)
            self.assertAlmostEqual(midpoint(lambda x: kernel(t,x),-width,0.),0.5,places=11)
            for R in (0.3,2.,10.):
                for x in (-1.,0.,2.):
                    self.assertAlmostEqual(kernel(t,x),kernel(t/R**2,x/R)/R,places=12)

    def test_complex_extension_modulus(self):
        for a in (0.1,1.,3.):
            for x in (-2.,0.,1.):
                for eta in (0.,0.3,1.):
                    y=0.7
                    value=cmath.exp(-(complex(x,eta)-y)**2/(4*a))
                    expected=math.exp((eta**2-(x-y)**2)/(4*a))
                    self.assertAlmostEqual(abs(value),expected,places=12)

    def test_duhamel_constant_source_mode(self):
        for rate in (0.5,1.,4.,9.):
            for t in (0.01,0.2,1.):
                integral=midpoint(lambda s: math.exp(-rate*(t-s)),0.,t)
                exact=-math.expm1(-rate*t)/rate
                self.assertAlmostEqual(integral,exact,delta=1e-7)
                self.assertAlmostEqual(math.exp(-rate*t)+rate*exact,1.,places=13)

    def test_energy_and_backward_modes(self):
        for m in range(1,9):
            norm2=midpoint(lambda x: math.sin(m*x)**2,0.,math.pi)
            grad2=midpoint(lambda x: (m*math.cos(m*x))**2,0.,math.pi)
            self.assertAlmostEqual(norm2,math.pi/2,places=11)
            self.assertAlmostEqual(grad2,m*m*norm2,places=10)
        for T in (0.1,0.5,1.):
            values=[math.exp(-m*m*T) for m in range(1,11)]
            self.assertTrue(all(a>b for a,b in zip(values,values[1:])))
            self.assertAlmostEqual(values[-1]*math.exp(100*T),1.,places=12)

    def test_tychonoff_cauchy_and_factorials(self):
        c=F(128,625)
        for i in range(-8,9):
            for j in range(-8,9):
                a,b=1+F(i,32),F(j,32)
                if (a-1)**2+b*b<=F(1,16):
                    self.assertGreaterEqual((a*a-b*b)/(a*a+b*b)**2,c)
        for p in range(6):
            for q in range(6):
                for k in range(1,31):
                    if 2*k>=q:
                        ratio=F(math.factorial(k+p),math.factorial(2*k-q))
                        bound=F((k+p)**p*(2*k)**q,math.factorial(k))
                        self.assertLessEqual(ratio,bound)

    def test_tychonoff_flat_majorant(self):
        c=F(128,625)
        for B in (1,2,5):
            for j in range(1,11):
                t=c/(8*B*B*j)
                self.assertLessEqual(-c/t**2+4*B*B/t,-c/(2*t**2))


if __name__ == "__main__":
    unittest.main()
