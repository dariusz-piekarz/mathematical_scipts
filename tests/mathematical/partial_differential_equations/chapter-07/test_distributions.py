"""Finite numerical regressions for PDE-07, not proofs or TeX parsing."""
import math
import unittest


def midpoint(f, a, b, n=4096):
    dx = (b-a)/n
    return dx*sum(f(a+(j+.5)*dx) for j in range(n))


def bump(x):
    return math.exp(-1/(1-x*x)) if abs(x)<1 else 0.


def bump_prime(x):
    return -2*x/(1-x*x)**2*bump(x) if abs(x)<1 else 0.


class DistributionRegression(unittest.TestCase):
    def test_scaled_test(self):
        # PDE-07-010,019: lower derivatives decay, selected derivative fixed.
        for k in (1, 2, 4, 7):
            psi=lambda z:z**k*bump(z)/(math.factorial(k)*bump(0))
            for eps in (.5, .25, .125):
                f=lambda x:eps**k*psi(x/eps)
                self.assertAlmostEqual(f(eps/2),eps**k*psi(.5))
                # Forward k-th difference of the actual scaled bump.
                h=eps*1e-4
                derivative=sum((-1)**(k-j)*math.comb(k,j)*f(j*h) for j in range(k+1))/h**k
                self.assertAlmostEqual(derivative,1,delta=2e-5)
                self.assertLessEqual(max(abs(f(eps*j/20)) for j in range(-20,21)),eps**k)

    def test_heaviside_and_absolute_value(self):
        # PDE-07-018: integrate H against -phi' and |x| against phi''.
        self.assertAlmostEqual(-midpoint(bump_prime, 0, 1), bump(0), places=7)
        def second(x):
            if abs(x)>=1: return 0.
            a=1-x*x
            return bump(x)*(4*x*x/a**4-2/a**2-8*x*x/a**3)
        self.assertAlmostEqual(midpoint(lambda x: abs(x)*second(x),-1,1),2*bump(0),places=6)

    def test_jump_sign(self):
        # PDE-07-021,023: slopes and jump, normal points right.
        left=lambda x: 2*x+1
        right=lambda x: -3*x+4
        lhs=-midpoint(lambda x:left(x)*bump_prime(x),-1,0)-midpoint(lambda x:right(x)*bump_prime(x),0,1)
        rhs=2*midpoint(bump,-1,0)-3*midpoint(bump,0,1)+(right(0)-left(0))*bump(0)
        self.assertAlmostEqual(lhs,rhs,places=7)

    def test_reflected_kernel(self):
        # PDE-07-035: asymmetric kernel detects wrong reflection.
        mass=midpoint(bump,-1,1)
        rho=lambda z: bump(z)*(1+.7*z)/mass
        for eps in (.1,.4,.8):
            y=.3
            expected=midpoint(lambda z:rho(z)*(y+eps*z)**2,-1,1)
            actual=midpoint(lambda x:rho((x-y)/eps)*x*x/eps,y-eps,y+eps)
            wrong=midpoint(lambda z:rho(z)*(y-eps*z)**2,-1,1)
            self.assertAlmostEqual(actual,expected,places=10)
            self.assertGreater(abs(actual-wrong),.001)

    def test_delta_scaling(self):
        # PDE-07-030,069: unit mass, finite scaled square and divergence.
        mass=midpoint(bump,-1,1)
        rho=lambda z:bump(z)/mass
        c=midpoint(lambda z:rho(z)**2,-1,1)
        values=[]
        for eps in (.5,.25,.125,.0625):
            kernel=lambda x:rho(x/eps)/eps
            self.assertAlmostEqual(midpoint(kernel,-eps,eps),1,places=10)
            values.append(midpoint(lambda x:kernel(x)**2*math.exp(-x*x),-eps,eps))
            self.assertLessEqual(abs(eps*values[-1]-c),c*eps**2)
        self.assertTrue(all(b>a for a,b in zip(values,values[1:])))

    def test_mollifier_heaviside(self):
        # PDE-07-038: symmetric normalized kernel gives H_epsilon(0)=1/2.
        mass=midpoint(bump,-1,1)
        for eps in (.2,.5,1.):
            h0=midpoint(lambda x:bump(x/eps)/(eps*mass),-eps,0)
            self.assertAlmostEqual(h0,.5,places=10)

    def test_radial_laplace(self):
        # PDE-07-050–053: flux normalization and radial integral.
        for d in (2,3,4,7):
            omega=2*math.pi**(d/2)/math.gamma(d/2)
            for r in (.1,.4,.8):
                if d==2:
                    f=lambda s:math.log(1/s)/(2*math.pi)
                    expected=r*r/2*math.log(1/r)+r*r/4
                else:
                    f=lambda s:s**(2-d)/((d-2)*omega)
                    expected=r*r/(2*(d-2))
                self.assertAlmostEqual(midpoint(lambda s:omega*s**(d-1)*f(s),0,r),expected,places=7)
                h=r*1e-5
                derivative=(f(r+h)-f(r-h))/(2*h)
                self.assertAlmostEqual(-derivative*omega*r**(d-1),1,places=7)

    def test_heat_initial_trace(self):
        # PDE-07-055,058: normalized heat kernel against Gaussian test.
        for kappa in (.2,1.,3.):
            for t in (.4,.04,.004):
                value=midpoint(lambda z:math.exp(-z*z)*math.exp(-4*kappa*t*z*z)/math.sqrt(math.pi),-9,9)
                self.assertAlmostEqual(value,1/math.sqrt(1+4*kappa*t),places=10)
            self.assertGreater(1/math.sqrt(1+4*kappa*.004),1/math.sqrt(1+4*kappa*.04))

    def test_heat_operator(self):
        # PDE-07-055: independent central differences of heat kernel in 1D.
        for kappa in (.3,1.,2.):
            for t,x in ((.3,.2),(.7,-1.),(2.,.5)):
                g=lambda s,y:math.exp(-y*y/(4*kappa*s))/math.sqrt(4*math.pi*kappa*s)
                h=1e-4
                dt=(g(t+h,x)-g(t-h,x))/(2*h)
                dxx=(g(t,x+h)-2*g(t,x)+g(t,x-h))/h**2
                self.assertAlmostEqual(dt,kappa*dxx,places=6)

    def test_radial_averaging(self):
        # PDE-07-062: harmonic polynomial x²-y²+2xy, circular means.
        h=lambda x,y:x*x-y*y+2*x*y
        for x,y in ((.3,-.7),(2.,1.)):
            for r in (.1,.4,1.):
                mean=sum(h(x+r*math.cos(2*math.pi*j/128),y+r*math.sin(2*math.pi*j/128)) for j in range(128))/128
                self.assertAlmostEqual(mean,h(x,y),places=12)


if __name__ == '__main__':
    unittest.main()
