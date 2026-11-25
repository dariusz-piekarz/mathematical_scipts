"""Finite exact checks of PDE chapter 11 examples and formulas, not analytic proofs."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "chapters/pl/partial_differential_equations/11-metody-wariacyjne-i-twierdzenie-laxa-milgrama.tex"


class VariationalChecks(unittest.TestCase):
    def test_PDE_11_013_016_contraction(self):
        # For T = [[1,-1],[1,1]], alpha=1 and M^2=2.
        for t in (F(1,4), F(1,2), F(3,4)):
            q2 = 1-2*t+2*t*t
            self.assertTrue(0 <= q2 < 1)
            for x,y in product(range(-3,4), repeat=2):
                a,b = x-t*(x-y), y-t*(x+y)
                self.assertEqual(a*a+b*b,q2*(x*x+y*y))
        self.assertEqual(1-2*F(1,2)+2*F(1,2)**2,F(1,2))
        # q=0 for T=I and t=1: one step.
        self.assertEqual(F(7)-1*(F(7)-F(3)),F(3))

    def test_PDE_11_033_036_neumann_sign(self):
        # u=x^2-1/3, -u''=-2, outward flux (0,2).
        f,h0,h1 = -2,0,2
        self.assertEqual(f+h0+h1,0)
        self.assertEqual(F(1,3)-F(1,3),0)
        for k in range(1,9):
            # Test v=x^k on (0,1).
            self.assertEqual(F(2*k,k+1),F(f,k+1)+h1)

    def test_PDE_11_049_052_energy(self):
        # Symmetric diagonal form diag(2,3), F(v)=2v_1+6v_2.
        def energy(x,y):
            return x*x+F(3,2)*y*y-2*x-6*y
        for x,y in product(range(-3,4),repeat=2):
            error = (x-1)**2+(y-2)**2
            gap = energy(x,y)-energy(1,2)
            self.assertEqual(gap,F(2*(x-1)**2+3*(y-2)**2,2))
            self.assertLessEqual(error,gap)
            self.assertLessEqual(gap,F(3,2)*error)
        x,y=F(1,2),F(-1,2)
        self.assertEqual((x-y,x+y),(1,0))
        self.assertNotEqual((x,y),(1,0))

    def test_PDE_11_054_scalar_minimum(self):
        for p in range(2,8):
            pp=F(p,p-1)
            for s0 in (F(0),F(1,2),F(2),F(3)):
                B=s0**(p-1)
                minimum=s0**p/p-B*s0
                self.assertEqual(minimum,-s0**p/pp)
                for s in (F(0),s0/2,s0,2*s0,F(4)):
                    self.assertGreaterEqual(s**p/p-B*s,minimum)

    def test_PDE_11_059_strict_monotonicity(self):
        # Scalar rational samples for integer exponents, including zero.
        for p in range(2,8):
            for x,y in product(map(F,range(-3,4)),repeat=2):
                def flux(z):
                    return abs(z)**(p-2)*z if z else F(0)
                result=(flux(x)-flux(y))*(x-y)
                if x == y:
                    self.assertEqual(result,0)
                else:
                    self.assertGreater(result,0)

    def test_PDE_11_068_070_fem_matrix(self):
        for n in range(2,17):
            h=F(1,n)
            u=[F(i,n)*(1-F(i,n))/2 for i in range(n+1)]
            for i in range(1,n):
                self.assertEqual((-u[i-1]+2*u[i]-u[i+1])/h,h)
            z=[F(0)]+[F((-1)**i*i,3) for i in range(1,n)]+[F(0)]
            quadratic=sum(z[i]*(2*z[i]-z[i-1]-z[i+1])/h for i in range(1,n))
            self.assertEqual(quadratic,sum((z[i+1]-z[i])**2/h for i in range(n)))
            self.assertGreater(quadratic,0)

    def test_PDE_11_071_072_fem_errors(self):
        for n in range(2,17):
            h=F(1,n)
            local_gradient=2*(h/2)**3/3
            local_value=(h*h*h**3/3-2*h*h**4/4+h**5/5)/4
            self.assertEqual(n*local_gradient,h*h/12)
            self.assertEqual(n*local_value,h**4/120)

    def test_PDE_11_073_diagram_nodes(self):
        source=SOURCE.read_text(encoding="utf-8")
        diagram=source.split(r"\begin{tikzpicture}",1)[1].split(r"\end{tikzpicture}",1)[0]
        line=next(line for line in diagram.splitlines() if r"\draw[orange!85!black,thick] (0,0)" in line)
        points=[(F(x),F(y)) for x,y in re.findall(r"\(([.\d]+),([.\d]+)\)",line)]
        self.assertEqual([x for x,_ in points],[F(i,4) for i in range(5)])
        self.assertTrue(all(y==x*(1-x)/2 for x,y in points))

    def test_PDE_11_075_discontinuous_coefficient(self):
        c=F(5,12)
        integral_inverse=F(1,2)+F(1,4)
        integral_s=F(1,8)+F(3,16)
        self.assertEqual(c*integral_inverse-integral_s,0)
        left=c-F(1,2)
        right=left/2
        self.assertEqual((left,right),(F(-1,12),F(-1,24)))
        self.assertNotEqual(left,right)
        self.assertEqual(left,2*right)


if __name__ == "__main__":
    unittest.main()
