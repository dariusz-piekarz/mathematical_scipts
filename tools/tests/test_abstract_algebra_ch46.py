#!/usr/bin/env python3
"""AA-46: SymPy verification of matrix PV equations, examples and Riccati reductions.

Finite exact models are regression checks, not a substitute for cited PV theorems.
"""
from pathlib import Path
import re, unittest
import sympy as sp

SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex"
x,t=sp.symbols("x t")
I=sp.I
def d(z,dt):
    return sp.diff(z,x)+dt*sp.diff(z,t)
def dzero(z):
    return sp.simplify(sp.cancel(sp.together(z)))==0
def matrix_zero(M):
    return all(dzero(z) for z in M)

class AA46Mathematical(unittest.TestCase):
    def test_01_fundamental_inverse_derivative(self):
        # For Y' = A Y, check derivative of U^{-1}U is zero
        U=sp.Matrix([[1,t],[0,1/x]])
        A=sp.Matrix([[0,1],[0,-1/x]])
        Du=U.applyfunc(lambda v:d(v,1/x))
        self.assertTrue(matrix_zero(Du-A*U))
        W=U.inv()
        Dw=W.applyfunc(lambda v:d(v,1/x))
        self.assertTrue(matrix_zero(Dw+W*A))
        self.assertTrue(matrix_zero(Dw*U+W*Du))

    def test_02_abel_equation_logarithm(self):
        U=sp.Matrix([[1,t],[0,1/x]])
        A=sp.Matrix([[0,1],[0,-1/x]])
        self.assertTrue(dzero(d(U.det(),1/x)-sp.trace(A)*U.det()))
        self.assertTrue(dzero(U.det()-1/x))

    def test_03_additive_group_matrix_action(self):
        U=sp.Matrix([[1,t],[0,1/x]])
        for c in (sp.Rational(-3,2),sp.Rational(0),sp.Rational(5,3)):
            M=sp.Matrix([[1,c],[0,1]])
            shifted=U.subs(t,t+c)
            self.assertTrue(matrix_zero(shifted-U*M))
            self.assertTrue(matrix_zero(
                shifted.applyfunc(lambda v:d(v,1/x)) -
                shifted*0-sp.Matrix([[0,1],[0,-1/x]])*shifted))

    def test_04_multiplicative_group_action(self):
        for c,e in [(sp.Rational(2),sp.Rational(-1,3)),(sp.Rational(-4,3),sp.Rational(5,2))]:
            self.assertTrue(dzero(d(c*t,t)-c*t))
            self.assertTrue(dzero(d(e*c*t,t)-e*c*t))
            self.assertTrue(dzero(c*e*t-e*c*t))
            self.assertNotEqual(c,0)

    def test_05_harmonic_system_and_wr(self):
        A=sp.Matrix([[0,1],[-1,0]])
        U=sp.Matrix([[t,1/t],[I*t,-I/t]])
        Du=U.applyfunc(lambda z:d(z,I*t))
        self.assertTrue(matrix_zero(Du-A*U))
        self.assertTrue(dzero(U.det()+2*I))
        for c in (sp.Rational(2),sp.Rational(-3,2),I):
            T=sp.diag(c,1/c)
            self.assertTrue(matrix_zero(U*T -
                U.subs(t,c*t,simultaneous=True)))
            self.assertTrue(dzero(T.det()-1))

    def test_06_cyclic_algebraic_extension(self):
        for m in range(2,9):
            dt=t/(m*x)
            self.assertTrue(dzero(d(t**m-x,dt)-(t**m/x-1)))
            # Modulo minimal polynomial t^m-x this vanishes.
            num=sp.together(d(t**m-x,dt)).as_numer_denom()[0]
            self.assertEqual(sp.rem(num,t**m-x,t),0)
            self.assertEqual(sp.factor(sp.diff(t**m,x)),0)
            # Coefficient eigen-character of the generator t^k:
            for k in range(1,m):
                self.assertTrue(dzero(d(t**k,dt)-sp.Rational(k,m)*t**k/x))

    def test_07_general_companion_matrix(self):
        coeff=[x,1/x,x**2]
        A=sp.Matrix([[0,1,0],[0,0,1],[-coeff[0],-coeff[1],-coeff[2]]])
        y0,y1,y2=sp.symbols("y0 y1 y2")
        v=sp.Matrix([y0,y1,y2])
        self.assertEqual(A*v,sp.Matrix([y1,y2,-x*y0-y1/x-x**2*y2]))

    def test_08_airy_riccati_degree_obstruction(self):
        # No POLYNOMIAL r of degree <= 8 can satisfy r'+r^2=x.
        for degree in range(9):
            c=sp.symbols("c0:"+str(degree+1))
            r=sum(c[i]*x**i for i in range(degree+1))
            q=sp.Poly(sp.diff(r,x)+r*r-x,x)
            if degree==0:
                self.assertEqual(q.coeff_monomial(x),-1)
            else:
                self.assertEqual(q.coeff_monomial(x**(2*degree)),c[-1]**2)
        # For rational r regular at infinity, r'+r^2 is regular too.
        r=(x+1)/(x**2+1)
        self.assertEqual(sp.limit(sp.diff(r,x)+r*r,x,sp.oo),0)

    def test_09_airys_traceless_system(self):
        A=sp.Matrix([[0,1],[x,0]])
        self.assertEqual(sp.trace(A),0)
        c=sp.symbols("c",nonzero=True)
        M=sp.diag(c,1/c)
        self.assertEqual(M.det(),1)

    def test_10_source_structure_and_citations(self):
        s=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),28)
        self.assertGreaterEqual(s.count(r"\begin{proof}"),5)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        for lab in ("aa:tw:pv-existence-uniqueness","aa:tw:pv-correspondence",
                    "aa:tw:pv-algebraic-group","aa:tw:pv-liouvillian-criterion",
                    "aa:tw:pv-automorphism-matrices","aa:tw:pv-airy-group",
                    "aa:lem:pv-airy-riccati","aa:prz:pv-cyclic"):
            self.assertIn(r"\label{"+lab+"}",s)
        self.assertIn("cytowane",s.lower())
if __name__=="__main__": unittest.main()
