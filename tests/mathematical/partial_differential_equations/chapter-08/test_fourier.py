"""Finite numerical regressions for PDE-08; not proofs or TeX parsing."""
import cmath
import math
import unittest


def integrate(f, a=-12., b=12., n=4096):
    dx = (b-a)/n
    return dx*sum(f(a+(j+.5)*dx) for j in range(n))


def ft(f, xi):
    return integrate(lambda x: f(x)*cmath.exp(-1j*x*xi))


def gaussian(a, xi):
    return math.sqrt(math.pi/a)*math.exp(-xi*xi/(4*a))


class FourierRegression(unittest.TestCase):
    def test_gaussian(self):
        # PDE-08-017,018
        for a in (.4, 1., 2.5):
            for xi in (-2., .3, 1.7):
                self.assertAlmostEqual(ft(lambda x: math.exp(-a*x*x), xi), gaussian(a, xi), delta=1e-10)

    def test_differentiation_and_multiplication(self):
        # PDE-08-011,012: use a shifted Gaussian to detect signs.
        f = lambda x: math.exp(-(x-.6)**2)
        for xi in (-1.3, .7):
            F = ft(f, xi)
            self.assertAlmostEqual(ft(lambda x: -2*(x-.6)*f(x), xi), 1j*xi*F, delta=1e-10)
            h = 1e-5
            derivative = (ft(f, xi+h)-ft(f, xi-h))/(2*h)
            self.assertAlmostEqual(ft(lambda x: x*f(x), xi), 1j*derivative, delta=1e-8)

    def test_inversion(self):
        # PDE-08-019,022: asymmetric Gaussian, actual inverse quadrature.
        for x in (-1., .4, 2.):
            F = lambda xi: gaussian(1., xi)*cmath.exp(-.4j*xi)
            inv = integrate(lambda xi: cmath.exp(1j*x*xi)*F(xi), -20, 20)/(2*math.pi)
            self.assertAlmostEqual(inv, math.exp(-(x-.4)**2), delta=1e-10)
            twice = integrate(lambda xi: cmath.exp(-1j*x*xi)*F(xi), -20, 20)
            self.assertAlmostEqual(twice, 2*math.pi*math.exp(-(-x-.4)**2), delta=1e-9)

    def test_gaussian_approximation(self):
        # PDE-08-020: evaluate convolution and the quantitative bound.
        for eps in (.5, .1, .02):
            G = lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
            for x in (0., .5, 2.):
                actual = integrate(lambda z: G(z)*math.exp(-(x-math.sqrt(eps)*z)**2))
                self.assertLessEqual(abs(actual-math.exp(-x*x)), math.sqrt(2/math.e)*math.sqrt(eps)*math.sqrt(2/math.pi)+1e-10)

    def test_convolution_and_product(self):
        # PDE-08-024,025: two distinct Gaussian widths.
        a, b = .8, 1.3
        for xi in (-1., .4, 2.):
            conv = lambda x: math.sqrt(math.pi/(a+b))*math.exp(-a*b*x*x/(a+b))
            self.assertAlmostEqual(ft(conv, xi), gaussian(a, xi)*gaussian(b, xi), delta=1e-9)
            product = integrate(lambda eta: gaussian(a, xi-eta)*gaussian(b, eta), -24, 24)/(2*math.pi)
            self.assertAlmostEqual(product, ft(lambda x: math.exp(-(a+b)*x*x), xi), delta=1e-10)

    def test_parseval(self):
        # PDE-08-026: cross inner product, complex phase.
        f = lambda x: cmath.exp(-x*x+.6j*x)
        g = lambda x: cmath.exp(-.7*x*x-.3j*x)
        left = integrate(lambda x: f(x)*g(x).conjugate())
        right = integrate(lambda xi: gaussian(1., xi-.6)*gaussian(.7, xi+.3), -24, 24)/(2*math.pi)
        self.assertAlmostEqual(left, right, delta=1e-10)

    def test_delta_and_plane_wave(self):
        # PDE-08-048: delta_a phase and plane-wave action on Gaussian test.
        for a in (-1.2, .7):
            lhs = integrate(lambda x: cmath.exp(1j*a*x)*gaussian(1., x), -20, 20)
            self.assertAlmostEqual(lhs, 2*math.pi*math.exp(-a*a), delta=1e-10)
            self.assertAlmostEqual(ft(lambda x: math.exp(-x*x), a), gaussian(1., a), delta=1e-10)

    def test_riesz(self):
        # PDE-08-058: finite nonzero frequency samples.
        for xi in ((1.,), (1., -2.), (.1, 3., -4.)):
            r = math.sqrt(sum(x*x for x in xi))
            m = [-1j*x/r for x in xi]
            self.assertAlmostEqual(sum(abs(z)**2 for z in m), 1.)
            self.assertAlmostEqual(sum(z*z for z in m), -1.)
            self.assertTrue(all(z.conjugate() == -z for z in m))

    def test_evolution(self):
        # PDE-08-065: check time derivatives by finite differences.
        dt, t, c, k = 1e-4, .6, 1.3, .8
        for r in (0., .001, .8, 2.):
            H = lambda t: math.exp(-k*t*r*r)
            C = lambda t: math.cos(c*t*r)
            S = lambda t: math.sin(c*t*r)/(c*r) if r else t
            self.assertAlmostEqual((H(t+dt)-H(t-dt))/(2*dt), -k*r*r*H(t), delta=1e-7)
            for a in (C, S):
                self.assertAlmostEqual((a(t+dt)-2*a(t)+a(t-dt))/dt**2, -c*c*r*r*a(t), delta=1e-7)
            self.assertEqual(S(0), 0.)
            self.assertAlmostEqual((S(dt)-S(-dt))/(2*dt), 1., delta=1e-7)

    def test_bessel_and_elliptic(self):
        # PDE-08-070,080,081
        for r in (0., .1, 2., 1e5):
            for s in (-2.5, 0., 3.):
                b = lambda t: (1+r*r)**(t/2)
                self.assertAlmostEqual(b(s)*b(-s), 1.)
                self.assertAlmostEqual(b(s)*b(.7)/b(s+.7), 1.)
            for a in (.3, 1., 2.):
                ratio = (1+r*r)/(r*r+a*a)
                self.assertLessEqual(ratio, max(1., a**-2)+1e-12)

    def test_poisson_threshold(self):
        # PDE-08-083,084: cutoff radial integrals, not infinite-integral proofs.
        for d in (1, 2, 3, 4, 5, 6):
            def radial(eps):
                return -math.log(eps) if d == 4 else (1-eps**(d-4))/(d-4)
            self.assertGreater(radial(.01), radial(.1))
            if d > 4:
                self.assertLess(radial(.001), 1/(d-4))
        self.assertGreater((1/.01**2-1)/2, (1/.1**2-1)/2)

    def test_heisenberg_gaussian(self):
        # PDE-08-087,089: saturation with nonunitary normalization.
        for a in (.5, 1., 2.):
            f2 = integrate(lambda x: math.exp(-2*a*x*x))
            xf2 = integrate(lambda x: x*x*math.exp(-2*a*x*x))
            F2 = integrate(lambda xi: gaussian(a, xi)**2, -24, 24)
            xiF2 = integrate(lambda xi: xi*xi*gaussian(a, xi)**2, -24, 24)
            self.assertAlmostEqual(math.sqrt(xf2*xiF2), .5*math.sqrt(f2*F2), delta=1e-10)


if __name__ == '__main__':
    unittest.main()
