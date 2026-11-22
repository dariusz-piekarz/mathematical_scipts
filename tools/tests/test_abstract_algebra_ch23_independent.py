"""AA-23 / audit III: independent mathematical checks, no source modifications."""
import itertools
import math
import re
import unittest
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
SRC=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/23-slad-norma-i-wyroznik.tex').read_text(encoding='utf8')
X=s.Symbol('X');t=s.Symbol('t')


def companion(coeffs):
    """Monic X^n + coeffs[n-1]X^(n-1) +...+coeffs[0]."""
    n=len(coeffs)
    C=s.zeros(n)
    for i in range(n-1): C[i+1,i]=1
    for i,c in enumerate(coeffs):C[i,n-1]=-c
    return C


def trace_form(p,f):
    from tools.tests.test_abstract_algebra_ch23 import trace_matrix,field_mul
    n=len(f)-1
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    return s.Matrix(n,n,lambda i,j:trace_matrix(field_mul(basis[i],basis[j],p,f),p,f))


class SourceInvariants(unittest.TestCase):
    def test_01_sources_unchanged(self):
        self.assertEqual(SRC,(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/23-slad-norma-i-wyroznik.tex').read_text(encoding='utf8'))
    def test_02_theorem_environment_balanced(self):
        for typ in ('twierdzenie','lemat','definicja','przyklad','uwaga','proof'):
            self.assertEqual(SRC.count(r'\begin{'+typ+'}'),SRC.count(r'\end{'+typ+'}'))
    def test_03_hypotheses_tower(self):
        self.assertIn(r'[F:K]<\infty$ i $[L:F]<\infty',SRC)
    def test_04_separability_qualified(self):
        self.assertIn('skończonym rozszerzeniem rozdzielczym',SRC)
        self.assertIn('Nie zakładamy rozdzielczości rozszerzenia',SRC)
    def test_05_charpoly_constant_and_trace(self):
        self.assertIn(r'$-\operatorname{tr}A$',SRC)
        self.assertIn(r'$(-1)^n\det A$',SRC)
    def test_06_radical_eisenstein(self):
        self.assertIn(r'\ref{aa:tw:eisenstein}',SRC)
    def test_07_nondegenerate_extension_domain(self):
        self.assertIn('Niech $\\Omega$ będzie domknięciem algebraicznym $K$',SRC)


class CompanionIndependent(unittest.TestCase):
    def test_08_general_n1(self):
        self.assertEqual(companion([s.Integer(7)]).charpoly(X).as_expr(),X+7)
    def test_09_general_n2(self):
        a,b=s.symbols('a b')
        self.assertEqual(s.expand(companion([a,b]).charpoly(X).as_expr()),X**2+b*X+a)
    def test_10_general_n3(self):
        a,b,c=s.symbols('a b c')
        self.assertEqual(s.expand(companion([a,b,c]).charpoly(X).as_expr()),X**3+c*X**2+b*X+a)
    def test_11_general_n4(self):
        a,b,c,d=s.symbols('a b c d')
        self.assertEqual(s.expand(companion([a,b,c,d]).charpoly(X).as_expr()),X**4+d*X**3+c*X**2+b*X+a)
    def test_12_general_n5(self):
        self.assertEqual(companion([3,-2,0,5,-1]).charpoly(X).as_expr(),X**5-X**4+5*X**3-2*X+3)
    def test_13_companion_signs_all_degrees(self):
        for n in range(1,8):
            C=companion([2]+[0]*(n-1))
            self.assertEqual(C.det(),(-1)**n*2)
            self.assertEqual(C.trace(),s.Integer(-2 if n==1 else 0))
    def test_14_scalar_charpoly(self):
        for n in range(1,8):
            self.assertEqual(s.expand(s.eye(n).multiply(3).charpoly(X).as_expr()),s.expand((X-3)**n))


class RelativeNormAndTrace(unittest.TestCase):
    def test_15_biquadratic_element_sum_minpoly(self):
        A=s.Matrix([[0,2],[1,0]]);B=s.Matrix([[0,3],[1,0]])
        M=s.kronecker_product(A,s.eye(2))+s.kronecker_product(s.eye(2),B)
        self.assertEqual(s.factor(M.charpoly(X).as_expr()),X**4-10*X**2+1)
    def test_16_biquadratic_element_sum_norm(self):
        A=s.Matrix([[0,2],[1,0]]);B=s.Matrix([[0,3],[1,0]])
        M=s.kronecker_product(A,s.eye(2))+s.kronecker_product(s.eye(2),B)
        self.assertEqual((M.trace(),M.det()),(0,1))
    def test_17_biquadratic_trace_pairing(self):
        G=s.diag(4,8,12,24)
        self.assertEqual(G.det(),9216)
        self.assertEqual(s.sqrt(G.det()),96)
    def test_18_biquadratic_change_basis(self):
        G=s.diag(4,8,12,24)
        S=s.eye(4);S[1,1]=s.Rational(1,2);S[0,1]=s.Rational(1,2)
        self.assertEqual((S.T*G*S).det(),G.det()/4)
    def test_19_norm_of_rational_scalar(self):
        for n in range(1,6):
            for c in [-3,-1,0,1,2]:
                self.assertEqual((s.eye(n)*c).det(),c**n)
    def test_20_trace_of_rational_scalar(self):
        for n in range(1,6):
            for c in [-3,-1,0,1,2]:
                self.assertEqual((s.eye(n)*c).trace(),n*c)
    def test_21_pure_inseparable_p2(self):
        for u,v in [(1,1),(2,3),(-1,4)]:
            A=u*s.eye(2)+v*companion([-t,0]);
            self.assertEqual(A.trace(),2*u)
            self.assertEqual(s.Poly(s.expand(A.det()-(u*u+v*v*t)),t,modulus=2).is_zero,True)
    def test_22_pure_inseparable_p3(self):
        for u,v in [(1,1),(2,3),(-1,2)]:
            A=u*s.eye(3)+v*companion([-t,0,0]);
            self.assertEqual(s.Poly(s.expand(A.trace()),t,modulus=3).is_zero,True)
            self.assertEqual(s.Poly(s.expand(A.det()-(u**3+v**3*t)),t,modulus=3).is_zero,True)
    def test_23_pure_inseparable_p5(self):
        for u,v in [(1,1),(2,3)]:
            A=u*s.eye(5)+v*companion([-t,0,0,0,0]);
            self.assertEqual(s.Poly(s.expand(A.trace()),t,modulus=5).is_zero,True)
            self.assertEqual(s.Poly(s.expand(A.det()-(u**5+v**5*t)),t,modulus=5).is_zero,True)
    def test_24_tower_norm_quadratic_then_quadratic(self):
        A=s.Matrix([[0,2],[1,0]])
        I=s.eye(2)
        # L=Q(sqrt2,sqrt3), a=sqrt2; over Q(sqrt2), norm a^2=2.
        self.assertEqual(s.kronecker_product(A,I).det(),4)
        self.assertEqual((s.eye(2)*2).det(),4)


class FiniteTracePairing(unittest.TestCase):
    def test_25_trace_pairing_F4(self):
        self.assertEqual(trace_form(2,(1,1,1)).applyfunc(lambda z:z%2),s.Matrix([[0,1],[1,1]]))
    def test_26_trace_pairing_F9(self):
        self.assertEqual(trace_form(3,(1,0,1)).applyfunc(lambda z:z%3),s.Matrix([[2,0],[0,1]]))
    def test_27_non_degeneracy_in_small_fields(self):
        for p,f in [(2,(1,1,1)),(2,(1,1,0,1)),(3,(1,0,1)),(2,(1,1,0,0,1)),(5,(2,0,1)),(3,(1,2,0,1))]:
            self.assertNotEqual(int(trace_form(p,f).det())%p,0)
    def test_28_primitive_field_trace_F4(self):
        from tools.tests.test_abstract_algebra_ch23 import trace_matrix,norm_matrix
        for a,expected in [((0,0),(0,0)),((1,0),(0,1)),((0,1),(1,1)),((1,1),(1,1))]:
            self.assertEqual((trace_matrix(a,2,(1,1,1)),norm_matrix(a,2,(1,1,1))),expected)
    def test_29_trace_linear_in_char2(self):
        from tools.tests.test_abstract_algebra_ch23 import trace_matrix,field_mul
        f=(1,1,0,1);p=2
        elems=list(itertools.product(range(p),repeat=3))
        for a in elems:
            for b in elems:
                c=tuple((x+y)%p for x,y in zip(a,b))
                self.assertEqual(trace_matrix(c,p,f),(trace_matrix(a,p,f)+trace_matrix(b,p,f))%p)
    def test_30_norm_multiplicative_F9(self):
        from tools.tests.test_abstract_algebra_ch23 import norm_matrix,field_mul
        p=3;f=(1,0,1);elems=list(itertools.product(range(p),repeat=2))
        for a in elems:
            for b in elems:
                self.assertEqual(norm_matrix(field_mul(a,b,p,f),p,f),(norm_matrix(a,p,f)*norm_matrix(b,p,f))%p)

if __name__=='__main__':unittest.main(verbosity=2)
