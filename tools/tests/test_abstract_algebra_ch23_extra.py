"""AA-23 audit II: independent algebraic and finite-characteristic checks."""
import itertools
import re
import unittest
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parent
TEX=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/23-slad-norma-i-wyroznik.tex').read_text(encoding='utf-8')
X=s.Symbol('X')

def companion(coeffs):
    """Companion of monic x^n + coeffs[n-1]x^(n-1)+...+coeffs[0]."""
    n=len(coeffs)
    A=s.zeros(n)
    for j in range(n-1):A[j+1,j]=1
    for i,x in enumerate(coeffs):A[i,n-1]=-x
    return A

def block(mats):
    r=sum(x.rows for x in mats)
    C=s.zeros(r)
    j=0
    for m in mats:
        C[j:j+m.rows,j:j+m.cols]=m
        j+=m.rows
    return C

class StructuralTests(unittest.TestCase):
    def test_01_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEX)
        self.assertEqual((len(labels),len(set(labels))),(30,30))
    def test_02_all_old_labels_preserved(self):
        baseline={'aa:tw:trace-norm-basic', 'aa:tw:trace-norm-embeddings', 'aa:tw:primitive-element', 'aa:tw:trace-norm-tower', 'aa:uw:trace-relative-extension', 'aa:thm:trace-norm-tower', 'aa:uw:trace-norm-inseparable', 'aa:ch:trace-norm', 'aa:def:field-trace-norm', 'aa:ex:inseparable-trace', 'aa:prz:finite-field-trace-four', 'aa:tw:trace-norm-companion', 'aa:ex:quadratic-norm', 'aa:uw:pure-inseparable-norm', 'aa:prz:trace-norm-quadratic', 'aa:prz:trace-discriminant-other-basis', 'aa:prz:trace-norm-cubic', 'aa:lem:trace-discriminant-base-change', 'aa:ch:trace-norm-discriminant', 'aa:thm:trace-norm-minpoly', 'aa:tw:trace-nondegenerate', 'aa:prz:quadratic-discriminant', 'aa:lem:trace-norm-basis', 'aa:lem:restriction-determinant', 'aa:prz:trace-norm-relative-biquadratic', 'aa:uw:trace-not-ring', 'aa:uw:trace-norm-next', 'aa:def:trace-discriminant', 'aa:thm:trace-norm-properties', 'aa:tw:finite-field-trace-norm'}
        self.assertEqual(baseline,set(re.findall(r'\\label\{([^}]+)\}',TEX)))
    def test_03_no_undeclared_scalar_extension(self):
        self.assertIn('Niech $\\Omega$ będzie domknięciem algebraicznym $K$\nzawierającym $L$. Wybierzmy element pierwotny',TEX)
    def test_04_n2_companion_display_is_valid(self):
        self.assertIn(r'0_{1\times(n-1)}',TEX)
        self.assertIn(r'I_{n-1}',TEX)
        self.assertNotIn(r'-a_2\\' ,TEX)
    def test_05_stated_integral_rank(self):
        self.assertIn('niech $r\\ge1$ będzie liczbą całkowitą',TEX)
    def test_06_basis_independence_selfcontained(self):
        self.assertIn('Niech $L/K$ będzie skończonym rozszerzeniem ciał, a $a\\in L$',TEX)
    def test_07_companion_determinant_justified(self):
        self.assertIn('składnik pochodzący od $c_{i-1}$',TEX)
        self.assertIn(r'\det(TI-C)=T^d+c_{d-1}T^{d-1}+\cdots+c_0',TEX)
    def test_08_refs(self):
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEX)
        self.assertEqual(len(refs),16)
    def test_09_proof_count(self):
        self.assertEqual(TEX.count(r'\begin{proof}'),11)
        self.assertEqual(TEX.count(r'\end{proof}'),11)

class CompanionTests(unittest.TestCase):
    def test_10_degree_one(self):
        a=s.Symbol('a'); A=companion([a])
        self.assertEqual((A.shape,A.trace(),A.det(),A.charpoly(X).as_expr()),((1,1),-a,-a,X+a))
    def test_11_degree_two_symbolic(self):
        a0,a1=s.symbols('a0 a1');A=companion([a0,a1])
        self.assertEqual(A,s.Matrix([[0,-a0],[1,-a1]]))
        self.assertEqual(A.det(),a0)
        self.assertEqual(s.expand(A.charpoly(X).as_expr()),X**2+a1*X+a0)
    def test_12_degree_three_symbolic(self):
        a=s.symbols('a0:3');A=companion(a)
        self.assertEqual(A.det(),-a[0])
        self.assertEqual(s.expand(A.charpoly(X).as_expr()),X**3+a[2]*X**2+a[1]*X+a[0])
    def test_13_degree_four_symbolic(self):
        a=s.symbols('a0:4');A=companion(a)
        self.assertEqual(A.det(),a[0])
        self.assertEqual(s.expand(A.charpoly(X).as_expr()),X**4+a[3]*X**3+a[2]*X**2+a[1]*X+a[0])
    def test_14_charpoly_power(self):
        C=companion([-2,0]);B=block([C,C,C]);self.assertEqual(s.expand(B.charpoly(X).as_expr()),s.expand((X**2-2)**3))
    def test_15_trace_norm_in_repeated_extension(self):
        C=companion([-2,0]);B=block([C,C,C]);self.assertEqual((B.trace(),B.det()),(0,-8))
    def test_16_scalar_element(self):
        C=s.eye(5)*s.Rational(7,3)
        self.assertEqual((C.trace(),C.det()),(s.Rational(35,3),s.Rational(7,3)**5))
    def test_17_trace_change_of_basis(self):
        A=companion([-3,2,1]);S=s.Matrix([[1,1,0],[0,1,2],[0,0,1]])
        B=S.inv()*A*S
        self.assertEqual((A.trace(),A.det(),A.charpoly(X).as_expr()),(B.trace(),B.det(),B.charpoly(X).as_expr()))

class DiscriminantAndTowerTests(unittest.TestCase):
    def test_18_cubic_trace_matrix(self):
        G=s.Matrix([[3,0,0],[0,0,6],[0,6,0]])
        self.assertEqual(G.det(),-108)
        self.assertEqual(s.discriminant(X**3-2,X),-108)
    def test_19_quadratic_trace_gram_f4(self):
        G=s.Matrix([[0,1],[1,1]])
        self.assertEqual(int(G.det())%2,1)
    def test_20_quadratic_trace_gram_f9(self):
        G=s.diag(2,1)
        self.assertEqual(int(G.det())%3,2)
    def test_21_tower_norm_sqrt3(self):
        # L=Q(sqrt2,sqrt3), F=Q(sqrt2).
        # minimal polynomial of sqrt3 over F: t^2-3
        A=companion([-3,0]);B=block([A,A])
        self.assertEqual((A.det(),B.det()),(-3,9))
    def test_22_tower_restriction_determinant(self):
        z=s.sqrt(2)
        A=s.Matrix([[1+z,z],[3,2-z]])
        detA=s.simplify(A.det())
        self.assertEqual(detA,-2*z)
        def mulF(u):
            return s.Matrix([[s.simplify((u+s.conjugate(u))/2),s.simplify((u-s.conjugate(u))*z/2)],
                              [s.simplify((u-s.conjugate(u))/(2*z)),s.simplify((u+s.conjugate(u))/2)]])
        # sqrt(2) real: use conjugation z -> -z, not complex conjugation.
        def m(u):
            bar=s.expand(u).subs(z,-z)
            aa=s.simplify((u+bar)/2);bb=s.simplify((u-bar)/(2*z))
            return s.Matrix([[aa,2*bb],[bb,aa]])
        K=s.BlockMatrix([[m(A[0,0]),m(A[0,1])],[m(A[1,0]),m(A[1,1])]]).as_explicit()
        self.assertEqual(s.simplify(K.det()),-8)
        self.assertEqual(s.simplify(detA*detA.subs(z,-z)),-8)
    def test_23_change_basis_general(self):
        G=s.Matrix([[3,0,0],[0,0,6],[0,6,0]])
        S=s.Matrix([[1,1,2],[0,1,3],[0,0,2]])
        self.assertEqual((S.T*G*S).det(),S.det()**2*G.det())
    def test_24_pure_inseparable_char2(self):
        t=s.Symbol('t')
        # multiplication by 1+s in K(s), s^2=t, in characteristic two
        A=s.eye(2)+companion([-t,0])
        self.assertEqual(A.trace()%2,0)
        self.assertEqual(s.Poly(A.det(),t,modulus=2).as_expr(),t+1)
    def test_25_pure_inseparable_char3(self):
        t=s.Symbol('t')
        A=s.eye(3)+companion([-t,0,0])
        self.assertEqual(A.trace()%3,0)
        self.assertEqual(s.Poly(A.det(),t,modulus=3).as_expr(),t+1)
    def test_26_quartic_primitive_minimal(self):
        m=s.minpoly(s.sqrt(2)+s.sqrt(3),X)
        self.assertEqual(m,X**4-10*X**2+1)
    def test_27_inseparable_characteristic_p_norm(self):
        for p in (2,3,5):
            t=s.Symbol('t');M=companion([-t]+[0]*(p-1))
            self.assertEqual(M.det(),(-1)**(p+1)*t)
            self.assertEqual(s.expand(M.charpoly(X).as_expr()),X**p-t)

if __name__=='__main__':unittest.main(verbosity=2)
