"""Independent AA-23 audit-I regressions: trace, norm and discriminant."""
from __future__ import annotations
import itertools
import re
import unittest
from pathlib import Path
import sympy as sp

SOURCE=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/23-slad-norma-i-wyroznik.tex')
S=SOURCE.read_text(encoding='utf-8')


def field_mul(a,b,p,f):
    d=len(f)-1; c=[0]*(2*d-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    for k in range(2*d-2,d-1,-1):
        q=c[k]
        for j in range(d): c[k-d+j]=(c[k-d+j]-q*f[j])%p
    return tuple(c[:d])


def field_pow(a,k,p,f):
    z=(1,)+(0,)*(len(f)-2)
    while k:
        if k&1:z=field_mul(z,a,p,f)
        a=field_mul(a,a,p,f);k//=2
    return z


def multiplication_matrix(a,p,f):
    d=len(f)-1
    basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    cols=[field_mul(a,e,p,f) for e in basis]
    return sp.Matrix(d,d,lambda i,j:cols[j][i])


def trace_matrix(a,p,f):return int(multiplication_matrix(a,p,f).trace())%p

def norm_matrix(a,p,f):return int(multiplication_matrix(a,p,f).det())%p

def trace_frobenius(a,p,f):
    d=len(f)-1; z=(0,)*d
    for i in range(d):
        u=field_pow(a,p**i,p,f)
        z=tuple((x+y)%p for x,y in zip(z,u))
    return z


def norm_frobenius(a,p,f):return field_pow(a,sum(p**i for i in range(len(f)-1)),p,f)


class SourceTests(unittest.TestCase):
    def test_01_source_available(self):self.assertGreater(len(S),26000)
    def test_02_balanced_proofs(self):self.assertEqual(S.count(r'\begin{proof}'),S.count(r'\end{proof}'))
    def test_03_proof_count(self):self.assertEqual(S.count(r'\begin{proof}'),11)
    def test_04_examples(self):self.assertEqual(S.count(r'\begin{przyklad}'),7)
    def test_05_theorems(self):self.assertEqual(S.count(r'\begin{twierdzenie}'),8)
    def test_06_lemmas(self):self.assertEqual(S.count(r'\begin{lemat}'),3)
    def test_07_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual((len(labels),len(set(labels))),(30,30))
    def test_08_internal_refs(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',S))
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)
        self.assertGreaterEqual(len(refs),15)
        self.assertTrue(all(x.startswith('aa:') for x in refs))
        self.assertIn('aa:tw:trace-norm-embeddings',labels)
    def test_09_no_unsupported_numerics(self):
        self.assertNotIn('tensorowanie',S.lower())
        self.assertNotIn('sekwencyjn',S.lower())
    def test_10_algebraic_closure_defined(self):
        self.assertIn('Niech $\\Omega$ będzie domknięciem algebraicznym $K$',S)
    def test_11_primitive_finite_case(self):
        self.assertIn(r'\ref{aa:tw:finite-field-multiplicative-cyclic}',S)
    def test_12_eisenstein_cubic(self):
        self.assertIn(r'\ref{aa:tw:eisenstein}',S)
    def test_13_nonseparable_caveat(self):
        self.assertIn('Nie zakładamy rozdzielczości rozszerzenia',S)
    def test_14_degree_one_case(self):
        self.assertIn('Dla $n=1$ mamy $L=K$',S)
        self.assertIn(r'0_{1\times(n-1)}',S)
    def test_15_change_basis(self):
        self.assertIn(r'G_c=S^{\mathsf T}G_bS',S)
    def test_16_charpoly_basis_independence(self):
        self.assertIn(r'\det(TI-B)=\det(TI-A)',S)
    def test_17_finite_trace_surjective_proof(self):
        self.assertIn(r'p^{n-1}<q',S)
    def test_18_restriction_det_cases(self):
        self.assertIn(r'(-1)^{d^2}=(-1)^d',S)


class RationalAndMatrixTests(unittest.TestCase):
    def test_quadratic_trace(self):
        a,b,d=sp.symbols('a b d');M=sp.Matrix([[a,b*d],[b,a]])
        self.assertEqual(M.trace(),2*a)
    def test_quadratic_norm(self):
        a,b,d=sp.symbols('a b d');M=sp.Matrix([[a,b*d],[b,a]])
        self.assertEqual(M.det(),a*a-d*b*b)
    def test_degree_one(self):
        x=sp.symbols('x');M=sp.Matrix([[x]])
        self.assertEqual((M.det(),M.trace()),(x,x))
    def test_cubic_companion(self):
        t=sp.symbols('t');M=sp.Matrix([[0,0,t],[1,0,0],[0,1,0]])
        self.assertEqual((M.trace(),M.det()),(0,t))
        self.assertEqual(M.charpoly().as_expr(),sp.Symbol('lambda')**3-t)
    def test_cubic_2(self):
        M=sp.Matrix([[0,0,2],[1,0,0],[0,1,0]])
        self.assertEqual(M.det(),2)
    def test_cubic_norm_multiplicative(self):
        M=sp.Matrix([[0,0,2],[1,0,0],[0,1,0]])
        self.assertEqual(M.det()**3,(M**3).det())
    def test_quadratic_discriminant_5(self):
        G=sp.diag(2,10);self.assertEqual(G.det(),20)
    def test_new_basis_discriminant_5(self):
        S=sp.Matrix([[1,sp.Rational(1,2)],[0,sp.Rational(1,2)]])
        G=sp.diag(2,10)
        self.assertEqual(S.T*G*S,sp.Matrix([[2,1],[1,3]]))
        self.assertEqual((S.T*G*S).det(),5)
    def test_new_basis_disc_ratio(self):
        S=sp.Matrix([[1,sp.Rational(1,2)],[0,sp.Rational(1,2)]])
        G=sp.diag(2,10)
        self.assertEqual((S.T*G*S).det(),S.det()**2*G.det())
    def test_biquadratic_trace(self):
        M=sp.diag(sp.Matrix([[0,2],[1,0]]),sp.Matrix([[0,2],[1,0]]))
        self.assertEqual(M.trace(),0)
    def test_biquadratic_norm(self):
        M=sp.diag(sp.Matrix([[0,2],[1,0]]),sp.Matrix([[0,2],[1,0]]))
        self.assertEqual(M.det(),4)
    def test_minpoly_power_2(self):
        X=sp.Symbol('X')
        M=sp.diag(sp.Matrix([[0,2],[1,0]]),sp.Matrix([[0,2],[1,0]]))
        self.assertEqual(sp.expand(M.charpoly(X).as_expr()),sp.expand((X*X-2)**2))
    def test_norm_1_plus_sqrt2_over_Q(self):
        A=sp.Matrix([[1,2],[1,1]])
        self.assertEqual(A.det(),-1)
    def test_norm_1_plus_sqrt2_over_biquadratic(self):
        A=sp.Matrix([[1,2],[1,1]]);M=sp.diag(A,A)
        self.assertEqual(M.det(),1)
    def test_trace_1_plus_sqrt2_over_biquadratic(self):
        A=sp.Matrix([[1,2],[1,1]]);M=sp.diag(A,A)
        self.assertEqual(M.trace(),4)
    def test_primitive_sqrt2_plus_sqrt3(self):
        X=sp.Symbol('X')
        expr=X**4-10*X**2+1
        self.assertEqual(sp.factor(expr,extension=sp.sqrt(2)+sp.sqrt(3)).subs(X,sp.sqrt(2)+sp.sqrt(3)).simplify(),0)
    def test_primitive_degree_four(self):
        X=sp.Symbol('X')
        self.assertTrue(sp.Poly(X**4-10*X**2+1,X,domain='QQ').is_irreducible)
    def test_trace_powerbasis_nondegenerate(self):
        V=sp.Matrix([[1,sp.sqrt(2)],[1,-sp.sqrt(2)]])
        self.assertEqual((V.T*V).det(),8)
    def test_trace_discriminant_sqrt2(self):
        G=sp.diag(2,4);self.assertEqual(G.det(),8)
    def test_swap_block_det(self):
        for d in range(1,5):
            Z=sp.zeros(d);I=sp.eye(d)
            A=sp.BlockMatrix([[Z,I],[I,Z]]).as_explicit()
            self.assertEqual(A.det(),(-1)**d)
    def test_inseparable_trace_two(self):
        t=sp.Symbol('t');M=sp.Matrix([[0,t],[1,0]])
        self.assertEqual(M.trace(),0)
        self.assertEqual(M.det(),-t)
        self.assertEqual(sp.expand(M.charpoly().as_expr()- (sp.Symbol('lambda')**2-t)),0)
    def test_inseparable_trace_three(self):
        t=sp.Symbol('t');M=sp.Matrix([[0,0,t],[1,0,0],[0,1,0]])
        self.assertEqual(M.trace(),0)
        self.assertEqual(M.det(),t)
    def test_inseparable_five(self):
        t=sp.Symbol('t');M=sp.zeros(5)
        for i in range(4):M[i+1,i]=1
        M[0,4]=t
        self.assertEqual(M.trace(),0)
        self.assertEqual(M.det(),t)


FIELD_CASES={
    'F4':(2,(1,1,1)),
    'F8':(2,(1,1,0,1)),
    'F9':(3,(1,0,1)),
    'F16':(2,(1,1,0,0,1)),
    'F25':(5,(2,0,1)),
    'F27':(3,(1,2,0,1)),
}

class FiniteFieldTests(unittest.TestCase):
    def check_field(self,p,f,kind):
        d=len(f)-1; elements=list(itertools.product(range(p),repeat=d))
        zero=(0,)*d;one=(1,)+(0,)*(d-1)
        for a in elements:
            if kind=='trace':
                self.assertEqual(trace_frobenius(a,p,f)[1:],(0,)*(d-1))
                self.assertEqual(trace_matrix(a,p,f),trace_frobenius(a,p,f)[0])
            elif kind=='norm':
                self.assertEqual(norm_frobenius(a,p,f)[1:],(0,)*(d-1))
                self.assertEqual(norm_matrix(a,p,f),norm_frobenius(a,p,f)[0])
            elif kind=='frobenius':
                self.assertEqual(field_pow(a,p**d,p,f),a)
            elif kind=='norm_nonzero':
                self.assertEqual(norm_matrix(a,p,f)!=0,a!=zero)
            elif kind=='surjective_trace':
                pass
        if kind=='surjective_trace':
            self.assertEqual({trace_matrix(a,p,f) for a in elements},set(range(p)))
        if kind=='surjective_norm':
            self.assertEqual({norm_matrix(a,p,f) for a in elements if a!=zero},set(range(1,p)))

for label,(p,f) in FIELD_CASES.items():
    for kind in ('trace','norm','frobenius','norm_nonzero','surjective_trace','surjective_norm'):
        def test(self,p=p,f=f,kind=kind):
            self.check_field(p,f,kind)
        setattr(FiniteFieldTests,'test_'+label+'_'+kind,test)

if __name__=='__main__':unittest.main(verbosity=2)
