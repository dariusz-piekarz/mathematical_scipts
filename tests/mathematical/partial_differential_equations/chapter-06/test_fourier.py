"""Finite arithmetic regressions for PDE-06; not proofs or TeX parsing."""
import cmath
import math
import unittest


def midpoint(f, a, b, n=4096):
    dx = (b-a)/n
    return dx*sum(f(a+(j+.5)*dx) for j in range(n))


class FourierRegression(unittest.TestCase):
    def test_fejer(self):
        # PDE-06-003,004: both forms and exact discrete period average.
        for n in (0, 1, 5, 20):
            def kernel(t):
                return abs(sum(cmath.exp(1j*j*t) for j in range(n+1)))**2/(n+1)
            for t in (0, .2, 1.3, math.pi):
                series = sum((1-abs(k)/(n+1))*cmath.exp(1j*k*t)
                             for k in range(-n,n+1))
                self.assertAlmostEqual(abs(kernel(t)-series), 0, places=10)
            self.assertAlmostEqual(sum(kernel(2*math.pi*j/64) for j in range(64))/64, 1)

    def test_complex_odd_extension(self):
        # PDE-06-009: complex odd data, not conjugate symmetry.
        for L in (.7, 2., 5.):
            def f(x):
                return (1+2j)*math.sin(math.pi*x/L)-3j*math.sin(3*math.pi*x/L)
            for n in (1, 2, 3, 4):
                cn = midpoint(lambda x: f(x)*cmath.exp(-1j*n*math.pi*x/L), -L,L)/(2*L)
                cm = midpoint(lambda x: f(x)*cmath.exp(1j*n*math.pi*x/L), -L,L)/(2*L)
                bn = 2/L*midpoint(lambda x: f(x)*math.sin(n*math.pi*x/L),0,L)
                self.assertAlmostEqual(abs(cn+cm),0,places=10)
                self.assertAlmostEqual(abs(2j*cn-bn),0,places=10)

    def test_poincare(self):
        # PDE-06-008,010: sharp first mode and derivative coefficients.
        for L in (.8, 2., 4.):
            for n in (1, 2, 5):
                k=n*math.pi/L
                norm=midpoint(lambda x: math.sin(k*x)**2,0,L)
                energy=midpoint(lambda x: (k*math.cos(k*x))**2,0,L)
                self.assertAlmostEqual(norm,L/2)
                self.assertAlmostEqual(energy,k*k*norm)
                self.assertGreaterEqual((L/math.pi)**2*energy+1e-10,norm)
                self.assertAlmostEqual(midpoint(lambda x: k*math.cos(k*x)**2,0,L), k*norm)
                if n==1:
                    self.assertAlmostEqual((L/math.pi)**2*energy,norm)

    def test_periodic_gaussian(self):
        # PDE-06-012,013: unnormalized periodic convolution multiplier.
        for L, kt in ((.7,.15),(2.,.3),(3.,1.2)):
            def G(x):
                return math.exp(-x*x/(4*kt))/math.sqrt(4*math.pi*kt)
            def K(x):
                return sum(G(x+2*j*L) for j in range(-12,13))
            self.assertAlmostEqual(midpoint(K,-L,L,2048),1,places=9)
            for n in (0,1,3):
                cn=midpoint(lambda x: K(x)*cmath.exp(-1j*n*math.pi*x/L),-L,L,2048)/(2*L)
                self.assertAlmostEqual(abs(2*L*cn-math.exp(-kt*(n*math.pi/L)**2)),0,places=9)

    def test_heat_decay(self):
        # PDE-06-015,016: finite modal L2 energies.
        for t in (0.,.01,.3,1.):
            a=[1+2j, -3j, .5]
            k=.4
            energy=sum(abs(z)**2*math.exp(-2*k*n*n*t) for n,z in enumerate(a,1))
            self.assertLessEqual(energy,math.exp(-2*k*t)*sum(abs(z)**2 for z in a)+1e-12)
            self.assertAlmostEqual(abs(a[0]*math.exp(-k*t)),abs(a[0])*math.exp(-k*t))

    def test_wave_energy(self):
        # PDE-06-019,020: complex data and exact modal energy.
        for omega in (.5,2.,7.):
            a,b=1+3j,2-4j
            for t in (0.,.13,1.,5.):
                co,si=math.cos(omega*t),math.sin(omega*t)
                pos=a*co+b/omega*si
                vel=-omega*a*si+b*co
                self.assertAlmostEqual(abs(vel)**2+omega**2*abs(pos)**2,abs(b)**2+omega**2*abs(a)**2,places=10)

    def test_duhamel(self):
        # PDE-06-023,026: f_n(s)=s, exact integrating-factor integral.
        for rate in (.4,2.,5.):
            for t in (0.,.1,1.):
                expected=t/rate+math.expm1(-rate*t)/rate**2
                value=midpoint(lambda s: math.exp(-rate*(t-s))*s,0,t,8192)
                self.assertAlmostEqual(value,expected,places=7)
                self.assertAlmostEqual(-math.expm1(-rate*t)/rate+rate*expected,t)

    def test_green(self):
        # PDE-06-029,031: p=1,q=0, w=2, f=1.
        for L in (.5,2.,4.):
            def G(x,s):
                return min(x,s)*(L-max(x,s))/L
            for x in (0.,L/4,L/2,L):
                self.assertEqual(G(x,0),0)
                self.assertEqual(G(x,L),0)
                self.assertAlmostEqual(midpoint(lambda s: 2*G(x,s),0,L),x*(L-x))
                for s in (L/4,L/2,3*L/4):
                    self.assertEqual(G(x,s),G(s,x))
                    self.assertAlmostEqual(-(-s/L-(L-s)/L),1)

    def test_rectangle(self):
        # PDE-06-037: exact square multiplicity and irrational-ratio pairs.
        pairs=[(m,n) for m in range(1,8) for n in range(1,8) if m*m+n*n==5]
        self.assertEqual(pairs,[(1,2),(2,1)])
        # Coefficients of 1 and sqrt(2) are unique in Q(sqrt(2)).
        values={(m*m,n*n) for m in range(1,9) for n in range(1,9)}
        self.assertEqual(len(values),64)

    def test_backward_heat(self):
        # PDE-06-039–041: finite truncations of the unattainable datum.
        rate=.2
        for n in (1,2,4,8,16):
            h=math.exp(-rate*n*n)
            self.assertAlmostEqual(math.exp(rate*n*n)*h,1)
        self.assertLess(math.exp(-rate*16**2),1e-20)
        for N in (5,20,40):
            self.assertAlmostEqual(sum((math.exp(rate*n*n)*math.exp(-rate*n*n))**2 for n in range(1,N+1)),N)


if __name__ == "__main__":
    unittest.main()
