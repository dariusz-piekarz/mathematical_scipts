"""AA-54: exact polynomial substitution, covariance and relations."""
import unittest
from math import comb
import sympy as s
x,y=s.symbols("x y")
I=s.I; p=(1+s.sqrt(5))/2
f=x*y*(x**4-y**4)
g=x**8+14*x**4*y**4+y**8
t=x**12-33*x**8*y**4-33*x**4*y**8+y**12
F=s.sqrt(5)*t-22*f**2

def invariant(P,q,K):
    a,b,c,d=[K.from_sympy(s.sympify(v)) for v in q]
    ii=K.from_sympy(I)
    A,B,C,D=a+b*ii,c+d*ii,-c+d*ii,a-b*ii
    poly=s.Poly(P,x,y,domain=K); n=poly.total_degree()
    src=[K.from_sympy(poly.coeff_monomial(x**(n-k)*y**k)) for k in range(n+1)]
    out=[K.zero]*(n+1)
    for k,v in enumerate(src):
        if not v: continue
        for j in range(n-k+1):
            for l in range(k+1):
                out[j+l]+=v*comb(n-k,j)*comb(k,l)*A**(n-k-j)*B**j*C**(k-l)*D**l
    return out==src

class AA54Tests(unittest.TestCase):
    def test_tetrahedral(self):
        K=s.QQ.algebraic_field(I)
        h=[s.Rational(1,2)]*4
        for P in (f,g,t):
            for q in (h,[0,1,0,0],[0,0,1,0]):
                self.assertTrue(invariant(P,q,K))
        self.assertEqual(s.expand(t*t-g**3+108*f**4),0)
    def test_octahedral(self):
        K=s.QQ.algebraic_field(I,s.sqrt(2))
        h=[s.Rational(1,2)]*4
        r=[s.sqrt(2)/2,s.sqrt(2)/2,0,0]
        for P in (f*f,g,f*t):
            for q in (h,r):
                self.assertTrue(invariant(P,q,K))
    def test_icosahedral(self):
        K=s.QQ.algebraic_field(I,s.sqrt(5))
        for q in ([s.Rational(1,2)]*4,[0,1,0,0],[p/2,0,(p-1)/2,s.Rational(1,2)]):
            self.assertTrue(invariant(F,q,K))
    def test_icosahedral_relation(self):
        K=s.QQ.algebraic_field(s.sqrt(5))
        P=s.Poly(F,x,y,domain=K)
        H=P.diff(x).diff(x)*P.diff(y).diff(y)-P.diff(x).diff(y)**2
        J=P.diff(x)*H.diff(y)-P.diff(y)*H.diff(x)
        self.assertEqual((P.total_degree(),H.total_degree(),J.total_degree()),(12,20,30))
        self.assertTrue((J**2+129534197760*P**5+s.Rational(400,121)*H**3).is_zero)
if __name__=="__main__": unittest.main()
