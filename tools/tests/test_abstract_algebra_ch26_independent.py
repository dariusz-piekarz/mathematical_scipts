"""Independent AA-26 re-audit: Kummer theory structural + arithmetic tests."""
import unittest, re, itertools
from pathlib import Path
from sympy import symbols, Poly, factor, I, sqrt, minpoly, QQ, primitive_root

ROOT=Path(__file__).resolve().parents[2]
SRC=(ROOT/'chapters/pl/abstract_algebra/26-rozszerzenia-cykliczne-i-teoria-kummera.tex').read_text(encoding='utf-8')
x=symbols('x')
P=7

def mul(a,b):
    v=[0]*5
    for i in range(3):
        for j in range(3): v[i+j]+=a[i]*b[j]
    v[0]+=2*v[3];v[1]+=2*v[4]
    return tuple(v[i]%P for i in range(3))

def exp(a,n):
    out=(1,0,0)
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out

def aut(a):return (a[0],a[1]*2%7,a[2]*4%7)

def alpha_projection(a):
    # P(x)=sum_{j=0}^{2} 2^{-j} sigma^j(x), ζ=2 mod 7
    s=[0,0,0];z=1;y=a
    for _ in range(3):
        for i in range(3):s[i]=(s[i]+z*y[i])%7
        z=z*4%7;y=aut(y)
    return tuple(s)

V=list(itertools.product(range(P),repeat=3))

class KummerAudit2(unittest.TestCase):
    def test_core_theorem_labels(self):
        for label in ('aa:tw:kummer-radical-cyclic','aa:tw:kummer-converse','aa:tw:kummer-prime-classification'):
            self.assertIn(r'\label{' + label + '}', SRC)
    def test_labels(self):
        labs=re.findall(r'\\label\{([^}]+)\}',SRC)
        self.assertEqual(len(labs),12)
        self.assertEqual(len(labs),len(set(labs)))
    def test_crossrefs(self):
        labs=set(re.findall(r'\\label\{([^}]+)\}',SRC));refs=set(re.findall(r'\\(?:eq)?ref\{([^}]+)\}',SRC))
        self.assertEqual(refs-labs,{'aa:lem:dedekind-independent'})
    def test_no_old_mistakes(self):
        for m in ('injektywne','injektywnym','pole stałe','Liczba złożona w wykładniku'):
            self.assertNotIn(m,SRC)
    def test_explicit_Kummer_hypotheses(self):
        self.assertIn(r'\operatorname{char}F\neq p',SRC)
        self.assertIn(r'|\mu_p(F)|=p',SRC)
    def test_environments_balanced(self):
        for env in ('proof','twierdzenie','lemat','wniosek','definicja','przyklad','uwaga','figure','tikzpicture','enumerate'):
            self.assertEqual(SRC.count('\\begin{'+env+'}'),SRC.count('\\end{'+env+'}'),env)
    def test_mu_n_F7(self):
        for n in (1,2,3,6):
            roots={t for t in range(1,7) if pow(t,n,7)==1}
            self.assertEqual(len(roots),n)
    def test_f7_cubes(self):
        self.assertEqual({pow(a,3,7) for a in range(1,7)},{1,6})
    def test_polynomial_irreducibility(self):
        self.assertTrue(Poly(x**3-2,x, modulus=7).is_irreducible)
        self.assertTrue(Poly(x**3-4,x, modulus=7).is_irreducible)
    def test_field_identity(self):
        e=(1,0,0)
        self.assertTrue(all(mul(e,v)==v and mul(v,e)==v for v in V))
    def test_field_inverses(self):
        for v in V[1:]:self.assertEqual(exp(v,342),(1,0,0))
    def test_sigma_order_three(self):
        for v in V:self.assertEqual(aut(aut(aut(v))),v)
    def test_sigma_homomorphism_full(self):
        # exhaustive 343^2 checks
        for v in V:
            for w in V:
                self.assertEqual(aut(mul(v,w)),mul(aut(v),aut(w)))
    def test_sigma_fixed_field(self):
        self.assertEqual({v for v in V if aut(v)==v},{(i,0,0) for i in range(7)})
    def test_projection_eigenvector(self):
        for v in V:self.assertEqual(aut(alpha_projection(v)),tuple(2*k%7 for k in alpha_projection(v)))
    def test_projection_nonzero(self):
        self.assertNotEqual(alpha_projection((0,1,0)),(0,0,0))
    def test_cube_radical_classification(self):
        a=(0,1,0);b=exp(a,2)
        self.assertEqual(exp(a,3),(2,0,0))
        self.assertEqual(exp(b,3),(4,0,0))
        self.assertEqual(mul(exp(b,2),(4,0,0)),a)
    def test_cyclic_group_degree(self):
        self.assertEqual(len({a for a in range(7) if pow(a,3,7)==2}),0)
    def test_quartic_counterexample_factor(self):
        self.assertEqual(factor(x**4-4,extension=I),(x**2-2)*(x**2+2))
    def test_quartic_counterexample_minpoly(self):
        self.assertEqual(minpoly(sqrt(2),x,domain=QQ.algebraic_field(I)),x**2-2)
    def test_quartic_no_root_over_Qi(self):
        # Four solutions b^4=4 in C are +/-sqrt(2), +/-i sqrt(2).
        # None belongs to Q(i), because its nonzero rational coordinates
        # would have to equal +/-sqrt(2).
        self.assertFalse(bool(sqrt(2).is_rational))
        self.assertTrue(bool(minpoly(sqrt(2),x,domain=QQ.algebraic_field(I)) == x**2-2))
    def test_qomega_cubic_irreducible(self):
        self.assertEqual(factor(x**3-2,extension=(-1+sqrt(-3))/2),x**3-2)
    def test_inseparable_derivative(self):
        for p in (2,3,5,7):self.assertTrue(Poly(p*x**(p-1),x,modulus=p).is_zero)
    def test_char_p_mu_p(self):
        for p in (2,3,5,7):self.assertTrue(Poly(x**p-1-(x-1)**p,x,modulus=p).is_zero)
    def test_rat_squareclasses(self):
        for t in (2,3,6):self.assertFalse(bool(sqrt(t).is_rational))
    def test_f4_cube_nontrivial(self):
        # GF(4)=F_2[w]/(w^2+w+1), GF(4)^*=C_3.
        def f4mul(a,b):
            z=a[1]*b[1]
            return ((a[0]*b[0]+z)%2,(a[0]*b[1]+a[1]*b[0]+z)%2)
        for t in [(1,0),(0,1),(1,1)]:
            self.assertEqual(f4mul(f4mul(t,t),t),(1,0))

if __name__=='__main__': unittest.main(verbosity=2)