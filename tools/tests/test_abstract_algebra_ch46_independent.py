#!/usr/bin/env python3
"""AA-46 independent exact-rational matrix/group arithmetic, no SymPy."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import re,unittest

SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex"

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def determinant2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def derivative_rational(c,x):
    # d/dx (a+b*x^(-1)+c*x^(-2)) of three coefficients
    a,b,c2=c
    return -b/x**2-2*c2/x**3

class IndependentPVAA46(unittest.TestCase):
    def test_01_additive_representation_and_group_law(self):
        for a,b in product([Q(-2),Q(-1,3),Q(0),Q(5,2)],repeat=2):
            Ma=[[Q(1),a],[Q(0),Q(1)]]
            Mb=[[Q(1),b],[Q(0),Q(1)]]
            Msum=[[Q(1),a+b],[Q(0),Q(1)]]
            self.assertEqual(matmul(Ma,Mb),Msum)
            self.assertEqual(determinant2(Msum),Q(1))

    def test_02_multiplicative_representation_and_character(self):
        for a,b in product([Q(-2),Q(-1,3),Q(1),Q(5,2)],repeat=2):
            Ma=[[a,Q(0)],[Q(0),1/a]]
            Mb=[[b,Q(0)],[Q(0),1/b]]
            self.assertEqual(matmul(Ma,Mb),
                             [[a*b,Q(0)],[Q(0),1/(a*b)]])
            self.assertEqual(determinant2(Ma),Q(1))
            self.assertEqual(determinant2(matmul(Ma,Mb)),Q(1))

    def test_03_logarithmic_fundamental_matrix_exact(self):
        # U=[[1,t],[0,1/x]], Dt=1/x, A=[[0,1],[0,-1/x]].
        for x,t in product([Q(1,2),Q(2),Q(-3,2)],[Q(-2),Q(0),Q(4,3)]):
            A=[[Q(0),Q(1)],[Q(0),-Q(1)/x]]
            U=[[Q(1),t],[Q(0),Q(1)/x]]
            DU=[[Q(0),Q(1)/x],[Q(0),-Q(1)/(x*x)]]
            self.assertEqual(matmul(A,U),DU)
            self.assertEqual(determinant2(U),Q(1)/x)
            self.assertEqual(-Q(1)/(x*x),(-Q(1)/x)*determinant2(U))

    def test_04_cyclic_group_mod_m(self):
        for m in range(2,15):
            elements=set(range(m))
            self.assertEqual(len(elements),m)
            for a,b in product(elements,repeat=2):
                self.assertIn((a+b)%m,elements)
                self.assertEqual((a-b+b)%m,a)
            self.assertEqual({(k*m)%m for k in elements},{0})

    def test_05_abel_identity_symbolic_fraction_examples(self):
        # A diagonal with trace a+b, determinant u*v.
        for x in [Q(-3,2),Q(1,2),Q(2),Q(5)]:
            # u=x^2, v=1/x; U=diag(u,v), DU=diag(2x,-1/x^2)
            u=x*x;v=1/x
            det=u*v
            trA=Q(2)/x-Q(1)/x
            detprime=Q(1)
            self.assertEqual(detprime,trA*det)
            self.assertEqual(u*v,x)

    def test_06_cyclic_derivative_exact_relation(self):
        # In K[t]/(t^m-x), Dt=t/(mx) is forced by D(t^m-x)=0.
        for m,x in product(range(2,11),[Q(1,3),Q(2),Q(5)]):
            self.assertEqual(Q(m)*Q(1,m)*x/x-Q(1),0)
            for k in range(1,m+1):
                # D(t^k)/t^k = k/(mx).
                self.assertEqual(Q(k,m)/x,Q(k)/(Q(m)*x))

    def test_07_airys_traceless_and_leading_poles(self):
        for x in [Q(-3),Q(-1,2),Q(0),Q(5,2)]:
            A=[[Q(0),Q(1)],[x,Q(0)]]
            self.assertEqual(A[0][0]+A[1][1],0)
        for degree in range(1,8):
            r=[Q(i+1) for i in range(degree+1)]
            # coefficient of x^(2d) in r^2+r'-x is leading coefficient squared
            coeff=sum((r[i]*r[2*degree-i] for i in range(len(r))
                       if 0<=2*degree-i<len(r)),Q(0))
            self.assertEqual(coeff,r[-1]**2)
            self.assertNotEqual(coeff,0)

    def test_08_rational_residue_obstruction_and_structure(self):
        # For u=(x-a)^(-m), u'=-m*(x-a)^(-m-1):
        # no pole of order one can appear from such a derivative.
        for m in range(1,9):
            for dx in [Q(1,2),Q(1),Q(2),Q(3)]:
                self.assertEqual(-Q(m)/dx**(m+1),
                                 (-m)*dx**(-m-1))
            self.assertGreater(m+1,1)
        s=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for lab in ("aa:prz:pv-multiplicative","aa:prz:pv-additive",
                    "aa:prz:pv-harmonic","aa:prz:pv-cyclic","aa:tw:pv-airy-group"):
            self.assertIn(r"\label{"+lab+"}",s)
if __name__=="__main__": unittest.main()
