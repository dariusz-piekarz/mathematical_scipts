"""Finite checks of explicit characteristic formulas, not proofs of PDE theorems."""
import math
import unittest
from fractions import Fraction as F
from itertools import product


def rarefaction(t, x, left, right):
    if x <= left*t:
        return left
    if x >= right*t:
        return right
    return x/t


class Chapter02Regression(unittest.TestCase):
    def test_dilation_jacobian_and_mass_PDE_02_004_005_006(self):
        for a, d, t in product((-2, 0, 3), (1, 2, 3), (0, 0.25, 1)):
            scale = math.exp(a*t)
            jac = scale**d
            self.assertAlmostEqual(jac/math.exp(d*a*t), 1)
            self.assertGreater(jac, 0)
            self.assertGreaterEqual(jac/math.exp(-d*abs(a)*t), 1-1e-12)
            self.assertLessEqual(jac/math.exp(d*abs(a)*t), 1+1e-12)
            for rho0 in (-2, 0, 3):
                self.assertAlmostEqual((rho0/jac)*jac, rho0)
            for p in (1, 2, 4):
                ratio = jac**(1/p)
                self.assertGreaterEqual(ratio/math.exp(-d*abs(a)*t/p), 1-1e-12)
                self.assertLessEqual(ratio/math.exp(d*abs(a)*t/p), 1+1e-12)

    def test_burgers_gradient_PDE_02_009(self):
        for t, xi in product((0, .5, .9, .99), (-2., -.5, 0., .5, 2.)):
            q = -1/math.cosh(xi)**2
            jac = 1+t*q
            self.assertGreater(jac, 0)
            self.assertGreaterEqual(jac+1e-14, 1-t)
            gradient = q/jac
            self.assertAlmostEqual(gradient*jac, q)
            if xi == 0:
                self.assertAlmostEqual(gradient, -1/(1-t))

    def test_rarefaction_initial_trace_PDE_02_010(self):
        for left, right in ((-3, -1), (-2, 4), (1, 5), (0, 2), (-2, 0)):
            for t in (F(1, 2), F(1, 10), F(1, 100)):
                knots = sorted({F(0), left*t, right*t})
                error = F(0)
                for a, b in zip(knots, knots[1:]):
                    initial = left if (a+b)/2 < 0 else right
                    # The error has fixed sign on each linear segment.
                    error += (b-a)*(abs(rarefaction(t, a, left, right)-initial)
                                   + abs(rarefaction(t, b, left, right)-initial))/2
                bound = 2*max(abs(left), abs(right))*t*(max(0, right)-min(0, left))
                self.assertLessEqual(error, bound)
                self.assertEqual(error, t*F(left*left+right*right, 2) if left <= 0 <= right
                                 else t*abs(F(right*right-left*left, 2)))

    def test_rankine_hugoniot_flux_PDE_02_011(self):
        for left, right in product(range(-3, 4), repeat=2):
            if left == right:
                continue
            sigma = F(left+right, 2)
            flux_left = F(left*left, 2)-sigma*left
            flux_right = sigma*right-F(right*right, 2)
            self.assertEqual(flux_left+flux_right, 0)
            self.assertEqual(flux_left+flux_right+(right-left), right-left)

    def test_charpit_contact_PDE_02_012_013(self):
        # F(x,u,p)=p^2+u-x; F_x=-1, F_u=1, F_p=2p.
        for p, dx, dp in product(range(-3, 4), repeat=3):
            xdot, udot, pdot = 2*p, 2*p*p, 1-p
            self.assertEqual(-xdot+udot+2*p*pdot, 0)
            du = dx-2*p*dp  # tangent to F=0
            r = du-p*dx
            rdot = dp*2*p+(-1+p)*dx
            self.assertEqual(rdot, -r)

    def test_kinetic_hamiltonian_PDE_02_017_018(self):
        for t, xi in product((F(0), F(1, 2), F(9, 10)), range(-3, 4)):
            x = (1-t)*xi
            p = -xi
            u = -(1-t)*xi*xi/2
            self.assertEqual(-x*x/(2*(1-t)), u)
            self.assertEqual(-x/(1-t), p)
            self.assertEqual(-x*x/(2*(1-t)**2)+p*p/2, 0)
        for r in (F(1, 2), F(1, 10), F(1, 100)):
            t = 1-r*r
            self.assertEqual(-r*r/(2*(1-t)), -F(1, 2))
            self.assertEqual(-F(0)/(2*(1-t)), 0)


if __name__ == "__main__":
    unittest.main()
