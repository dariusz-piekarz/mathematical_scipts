"""AA-33 -- independently verified Sylvester matrices, resultant and discriminant.
Run: python -m unittest -v /mnt/data/AA-33-audyt-I-testy.py
Uses SymPy only for cross-checks, the test constructs Sylvester matrices separately.
"""
from __future__ import annotations
import unittest
import sympy as sp
from pathlib import Path

x,s,t=sp.symbols('x s t')


def sylvester_r(f,g,m=None,n=None):
    """Construct columns from coefficients in the *ascending* power basis.
    If m,n are passed, they are formal upper degrees including padding.
    """
    P=sp.Poly(f,x);Q=sp.Poly(g,x)
    if m is None:m=P.degree()
    if n is None:n=Q.degree()
    assert m>=1 and n>=1 and P.degree()<=m and Q.degree()<=n
    col=[]
    for shift in range(n):col.append([P.nth(k-shift) if 0<=k-shift<=m else 0 for k in range(m+n)])
    for shift in range(m):col.append([Q.nth(k-shift) if 0<=k-shift<=n else 0 for k in range(m+n)])
    M=sp.Matrix(m+n,m+n,lambda row,column:col[column][row])
    return sp.expand((-1)**(m*n)*M.det(method='berkowitz'))


def disc_from_sylvester(f, p=None):
    P=sp.Poly(f,x);n=P.degree()
    assert n>=2 and P.LC()==1
    val=sp.expand((-1)**(n*(n-1)//2)*sylvester_r(f,sp.diff(f,x),n,n-1))
    if p is not None:val=int(val)%p
    return val


def check(eq,expected):
    if sp.expand(eq-expected)!=0:raise AssertionError((eq,expected))


class AA33Tests(unittest.TestCase):
    def test_linear_sign_and_formal_padding(self):
        f=2*x+1;g=x+3
        self.assertEqual(sylvester_r(f,g),5)
        self.assertEqual(sylvester_r(f,g,1,2),10)
        self.assertEqual(sylvester_r(g,f),-5)
        self.assertEqual(sylvester_r(f,g,2,1),-5)  # padding f changes sign/factor

    def test_elimination_and_specialization(self):
        check(sylvester_r(x*x-s,x-t),t*t-s)
        for a in [-2,-1,0,1,4,9]:
            for b in [-2,-1,0,1,2,3]:
                check((t*t-s).subs({s:a,t:b}),b*b-a)

    def test_repeated_roots(self):
        self.assertEqual(sylvester_r((x-1)**2,x+2),9)
        self.assertEqual(sylvester_r((x-1)**2,2*(x-1)),0)
        self.assertEqual(sylvester_r((x-1)**3,(x+2)**2),729)

    def test_nilpotent_counterexample(self):
        self.assertTrue(all((2*k+1)%4 != 0 for k in range(4)))
        self.assertEqual(sylvester_r(2*x+1,2*x+1),0)
        check(sp.expand((1+2*x)*(1-2*x)).subs(x,1)-1,-4)
        self.assertEqual(sp.expand((1+2*x)*(1-2*x)-1).coeff(x,2) % 4,0)

    def test_symmetry_convention(self):
        for f,g in [(x-1,x+3),(2*x+1,x+3),(x**2-2,x-3),(x**2+x+1,x**3+1),(x**3+x+1,x**2+2*x+1)]:
            a,b=sp.degree(f,x),sp.degree(g,x)
            check(sylvester_r(g,f),(-1)**(a*b)*sylvester_r(f,g))

    def test_biquadratic_symbolic(self):
        check(sylvester_r(x*x-s,x*x-t),(s-t)**2)
        check(sylvester_r(x**2+s,x**2+t),(s-t)**2)

    def test_formal_derivative_inseparable(self):
        self.assertEqual(disc_from_sylvester(x*x+s),-4*s)
        self.assertEqual(disc_from_sylvester(x**3+s),-27*s*s)
        self.assertEqual(disc_from_sylvester(x**2+1,p=2),0)
        self.assertEqual(disc_from_sylvester(x**3+1,p=3),0)
        self.assertEqual(disc_from_sylvester(x**4+1,p=2),0)

    def test_discriminant_cubic(self):
        f=x**3+s*x+t
        check(disc_from_sylvester(f),-4*s**3-27*t*t)
        check(disc_from_sylvester(x**3+x+t).subs(t,sp.Integer(1))%2,1)
        self.assertEqual(int(sp.expand(-4-27*t*t).subs(t,2))%2,0)

    def test_discriminant_quadratic(self):
        for b in [-3,-1,0,2,7]:
            for c in [-2,0,1,3]:
                f=x*x+b*x+c
                self.assertEqual(disc_from_sylvester(f),b*b-4*c)

    def test_base_change(self):
        for f,g in [(2*x+1,3*x+2),(2*x*x+3*x+1,4*x+3),(x*x+x+1,x*x+2*x+3)]:
            val=sylvester_r(f,g)
            for p in (2,3,4,5,6,7):
                # reduction to Z/pZ preserves the universal determinant polynomial
                coeff_f=[int(c)%p for c in sp.Poly(f,x).all_coeffs()]
                coeff_g=[int(c)%p for c in sp.Poly(g,x).all_coeffs()]
                fbar=sp.Poly.from_list(coeff_f,gens=x).as_expr()
                gbar=sp.Poly.from_list(coeff_g,gens=x).as_expr()
                self.assertEqual(int(sylvester_r(fbar,gbar,sp.degree(f,x),sp.degree(g,x)))%p,int(val)%p)


# Named, independent polynomials: each adds an individually reported test.
EXAMPLES=[
(x+1,x+2),(2*x+1,x+2),(x-2,x-3),(2*x+1,3*x-1),
(x*x-2,x-3),(x*x+1,x-1),(x*x+1,x*x-1),
(x*x+x+1,x*x-x+1),(2*x*x+3*x+1,x+2),
(x**3-2,x-1),(x**3-2,x-2),(x**3+x+1,x*x+x+1),
((x+1)**3,(x+1)**2),(x**3+3*x+1, x*x+x+2),
(x**4+1,x*x+1),(x**3+x+1,x**3+x+1),(x**4+x+1,x*x+1),
(x**3+2*x+2,2*x*x+x+1)
]
for index,(f,g) in enumerate(EXAMPLES,1):
    def test_case(self,f=f,g=g):
        check(sylvester_r(f,g),sp.resultant(f,g,x))
        if sp.degree(f,x)>=1 and sp.degree(g,x)>=1:
            self.assertEqual(sylvester_r(f,g)==0,sp.degree(sp.gcd(f,g),x)>0)
    setattr(AA33Tests,f'test_symbolic_resultant_{index:02d}',test_case)

for p in [2,3,5,7]:
  for num, (f,g) in enumerate([(x*x+x+1,x*x+1),(x*x-1,x-1),(x**3+x+1,x*x+x+1),((x+1)**3,x*x+1)],1):
    def test_finite(self,p=p,f=f,g=g):
        lhs=int(sylvester_r(f,g))%p
        A=sp.Poly(f,x,modulus=p);B=sp.Poly(g,x,modulus=p)
        self.assertEqual(lhs==0, A.gcd(B).degree()>0)
    setattr(AA33Tests,f'test_finite_field_p{p}_case{num}',test_finite)

for n in [2,3,4]:
  for i, f in enumerate([x**n+x+1,x**n+2*x+1,x**n-2,x**n+3*x+2],1):
    def test_disc(self,f=f):
        check(disc_from_sylvester(f),sp.discriminant(f,x))
    setattr(AA33Tests,f'test_discriminant_deg{n}_case{i}',test_disc)

if __name__=='__main__':unittest.main(verbosity=2)
