"""Finite regression checks for PDE-05, not formal proofs or TeX parsing."""
import cmath
import math
import unittest
from fractions import Fraction as F


def step(a, b, q):
    return 2 * (1 - 2*q)*b - a


class WaveRegression(unittest.TestCase):
    def test_dalembert_polynomial(self):
        # PDE-05-003: g=x^3, h=x^2; u=x^3+3xc²t²+x²t+c²t³/3.
        for c in (F(1, 2), F(1), F(3)):
            for t in (F(0), F(1, 3), F(2)):
                for x in (F(-2), F(0), F(3, 2)):
                    a, b = x-c*t, x+c*t
                    u = (a**3+b**3)/2+(b**3-a**3)/(6*c)
                    self.assertEqual(u, x**3+3*x*c*c*t*t+x*x*t+c*c*t**3/3)
                    self.assertEqual(6*x*c*c+2*c*c*t, c*c*(6*x+2*t))

    def test_cone_flux_square(self):
        # PDE-05-006,008: normal and tangential parts of gradient.
        for c in (F(1, 3), F(1), F(2)):
            for a in range(-3, 4):
                for b in range(-3, 4):
                    for tang2 in (0, 1, 5):
                        flux = c*c*a*b-c*F(a*a+c*c*(b*b+tang2), 2)
                        self.assertEqual(flux, -c*F((a-c*b)**2+c*c*tang2, 2))
                        self.assertLessEqual(flux, 0)

    def test_darboux_and_kirchhoff(self):
        # PDE-05-010–013: v=|x|²; M_r v=|x|²+r².
        for r in (F(-2), F(0), F(1, 4), F(3)):
            d = F(1, 7)
            w = lambda s: s*(5+s*s)
            self.assertEqual((w(r+d)-2*w(r)+w(r-d))/d**2, 6*r)
        # g=|x|², h=|x|²: u=|x|²+3c²t²+t|x|²+c²t³.
        for c in (F(1, 2), F(2)):
            for t in (F(0), F(1, 3), F(2)):
                self.assertEqual(6*c*c+6*c*c*t, c*c*(6+6*t))
        # Discrete exact spherical second moments using six axis points.
        points = [tuple(s if j == k else 0 for j in range(3))
                  for k in range(3) for s in (-1, 1)]
        for j in range(3):
            self.assertEqual(sum(p[j] for p in points), 0)
            for k in range(3):
                self.assertEqual(F(sum(p[j]*p[k] for p in points), 6),
                                 F(int(j == k), 3))

    def test_poisson_disk_moments(self):
        # PDE-05-016,017: substitute rho=sin(phi), integrate cos-weight-free.
        n = 4096
        d = math.pi/(2*n)
        radial_mass = sum(math.sin((i+.5)*d)*d for i in range(n))
        radial_second = sum(math.sin((i+.5)*d)**3*d for i in range(n))
        self.assertAlmostEqual(radial_mass, 1, places=7)
        self.assertAlmostEqual(radial_second, 2/3, places=7)
        # normalized disk mean of each coordinate squared is 1/3.
        self.assertAlmostEqual(radial_second/2, 1/3, places=7)

    def test_duhamel_polynomial(self):
        # PDE-05-019–022: f(s,y)=y²+s, zero initial data.
        # integral over the cone gives v=x²t²/2+c²t⁴/12+t³/6.
        for c in (F(1, 2), F(2)):
            for t in (F(0), F(1, 3), F(2)):
                for x in (F(-2), F(0), F(3)):
                    # Integrate y²+s in y, then integrate the resulting
                    # polynomial in s exactly via Simpson's 3/8 rule.
                    def integrand(s):
                        a,b=x-c*(t-s),x+c*(t-s)
                        return ((b**3-a**3)/3+s*(b-a))/(2*c)
                    v=t/8*(integrand(0)+3*integrand(t/3)
                           +3*integrand(2*t/3)+integrand(t))
                    self.assertEqual(v,x*x*t*t/2+c*c*t**4/12+t**3/6)
                    self.assertEqual(x*x+c*c*t*t+t-c*c*t*t,x*x+t)

    def test_string_energy(self):
        # PDE-05-025: exact normalized oscillator energy.
        for a, b in ((1, 2), (-3, 4), (0, 1)):
            for omega in (0.5, 2., 7.):
                for t in (0., .13, 1., 5.):
                    co, si = math.cos(omega*t), math.sin(omega*t)
                    pos, vel = a*co+b*si, omega*(-a*si+b*co)
                    self.assertAlmostEqual(vel**2+omega**2*pos**2,
                                           omega**2*(a*a+b*b), places=10)

    def test_cfl_root_classification(self):
        # PDE-05-027,028.
        for q in (0., .001, .25, .5, .99, 1., 1.01, 2.):
            d = 4*q*(q-1)
            roots = [1-2*q+s*cmath.sqrt(d) for s in (-1, 1)]
            for z in roots:
                self.assertAlmostEqual(abs(z*z-2*(1-2*q)*z+1), 0, places=10)
            self.assertAlmostEqual(abs(roots[0]*roots[1]-1), 0)
            if q <= 1:
                self.assertAlmostEqual(max(map(abs, roots)), 1)
            else:
                self.assertGreater(max(map(abs, roots)), 1)

    def test_cfl_initialized_modes(self):
        # PDE-05-029,030: exact arithmetic also at repeated roots.
        for q in (F(0), F(1, 100), F(1, 2), F(99, 100), F(1)):
            for g, h in ((F(2), F(-3)), (F(0), F(1)), (F(1), F(0))):
                dt = F(1, 20)
                a, b = g, (1-2*q)*g+dt*h
                for m in range(1, 81):
                    self.assertLessEqual(abs(b), abs(g)+m*dt*abs(h))
                    if q == 0:
                        self.assertEqual(b, g+m*dt*h)
                    if q == 1:
                        self.assertEqual(b, (-1)**m*(g-m*dt*h))
                    a, b = b, step(a, b, q)

    def test_periodic_cfl_and_stencil(self):
        # PDE-05-030,031: physical-space periodic recurrence.
        n, dt = 64, .05
        g = [math.sin(j*.3)+.2*(-1)**j for j in range(n)]
        h = [math.cos(j*.7)+.3*(-1)**j for j in range(n)]
        norm = lambda v: math.sqrt(sum(x*x for x in v))
        for lam in (.25, .9, 1.):
            a = g[:]
            b = [g[j]+dt*h[j]+lam**2/2*(g[(j+1)%n]-2*g[j]+g[j-1])
                 for j in range(n)]
            for m in range(1, 50):
                self.assertLessEqual(norm(b), norm(g)+m*dt*norm(h)+1e-10)
                a, b = b, [lam**2*(b[j-1]+b[(j+1)%n])
                            +2*(1-lam**2)*b[j]-a[j] for j in range(n)]
            # Compact impulse, no wrap within tested time horizon.
            a = [F(int(j == n//2)) for j in range(n)]
            l2 = F(str(lam))**2
            b = [a[j]+l2/2*(a[j-1]-2*a[j]+a[(j+1)%n]) for j in range(n)]
            for m in range(1, 12):
                self.assertTrue(all(v == 0 for j,v in enumerate(b)
                                    if abs(j-n//2)>m))
                a,b = b,[l2*(b[j-1]+b[(j+1)%n])+2*(1-l2)*b[j]-a[j]
                         for j in range(n)]


if __name__ == "__main__":
    unittest.main()
