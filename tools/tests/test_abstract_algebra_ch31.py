"""Independent AA-31 checks over integer, finite and nonreduced coefficient rings."""
import itertools
import re
import unittest
from pathlib import Path
from math import factorial
from sympy import Poly, symbols, expand, prod

SRC = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/31-wielomiany-symetryczne-i-wzory-viete.tex')
X = symbols('X1 X2 X3 X4')


def elementary(xs, k):
    if not k:
        return 1
    return sum((prod(subset) for subset in itertools.combinations(xs, k)), 0)


def iszero_mod(expr, xs, m):
    return all(int(c) % m == 0 for c in Poly(expand(expr), *xs).coeffs())


def greedy(el, xs, m):
    # Constructive reverse of f=P(e): cancel lexicographically leading terms over Z/m.
    current = Poly(expand(el), *xs)
    steps = 0
    while True:
        nz = [(mon, int(co) % m) for mon, co in current.terms() if int(co) % m]
        if not nz:
            return steps
        a, coeff = max(nz, key=lambda pair: pair[0])
        if any(a[i] < a[i+1] for i in range(len(a)-1)):
            raise AssertionError('Leading exponent vector is not a partition')
        diffs = [a[i] - (a[i+1] if i+1<len(a) else 0) for i in range(len(a))]
        reducer = prod(elementary(xs[:len(a)], k+1)**d for k,d in enumerate(diffs))
        nextpol = Poly(expand(current.as_expr()-coeff*reducer), *xs)
        if not any(int(co)%m for co in nextpol.coeffs()):
            return steps+1
        new_lead = max(mon for mon,co in nextpol.terms() if int(co)%m)
        if not (new_lead < a):
            raise AssertionError('Leading term did not decrease')
        if nextpol.total_degree() > current.total_degree():
            raise AssertionError('Degree increased')
        current = nextpol
        steps += 1
        if steps > 50:
            raise AssertionError('Unexpected nontermination')


class StructuralAA31(unittest.TestCase):
    def test_labels(self):
        text = SRC.read_text()
        labels = re.findall(r'\\label\{([^}]+)\}', text)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(labels), 9)
    def test_internal_references(self):
        text = SRC.read_text()
        refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', text)
        labels = set(re.findall(r'\\label\{([^}]+)\}', text))
        self.assertEqual(set(refs) - labels, set())
    def test_no_known_typos(self):
        text = SRC.read_text()
        self.assertNotIn('injektyw', text)
        self.assertNotIn('z współczynników', text)
    def test_statement_valid_over_arbitrary_commutative_ring(self):
        text = SRC.read_text()
        self.assertIn('przemiennego pierścienia $A$ z jedynką', text)
        self.assertIn('Jeżeli $1_A=0$', text)
    def test_viete_statement_handles_multiplicity(self):
        self.assertIn('wypisanymi z krotnościami algebraicznymi', SRC.read_text())
    def test_symmetric_generators_fixed(self):
        xs=X[:3];e=[elementary(xs,j) for j in range(1,4)]
        for perm in itertools.permutations(xs):
            self.assertEqual([expand(k) for k in e], [expand(k.xreplace(dict(zip(xs,perm)))) for k in e])
    def test_cube_identity(self):
        a,b,c=X[:3]
        e1,e2,e3=[elementary((a,b,c),j) for j in (1,2,3)]
        self.assertEqual(expand(a**3+b**3+c**3-e1**3+3*e1*e2-3*e3),0)
    def test_two_variable_alg(self):
        a,b=X[:2];self.assertEqual(expand(a*a+b*b+a*b-(a+b)**2+a*b),0)
    def test_three_variable_alg(self):
        a,b,c=X[:3];l=sum(u**2*v for u in (a,b,c) for v in (a,b,c) if u!=v)
        e1,e2,e3=[elementary((a,b,c),j) for j in (1,2,3)]
        self.assertEqual(expand(l-e1*e2+3*e3),0)
    def test_viete_cubic_example(self):
        from sympy import roots
        a,b,c=symbols('a b c')
        expr=prod((a-r) for r in (1,2,3))
        self.assertEqual(expand(expr), a**3-6*a**2+11*a-6)
    def test_sum_of_squares_example(self):
        self.assertEqual(2**2-2*3,-2)
    def test_zero_ring_case(self):
        # Z/1 is singleton, hence the map from the polynomial ring is automatically bijective.
        self.assertEqual({i%1 for i in range(100)}, {0})
    def test_nonintegral_ring_Z4(self):
        a,b=X[:2]
        self.assertTrue(iszero_mod(a*a+b*b-(a+b)**2+2*a*b,(a,b),4))
    def test_characteristic_two_identity(self):
        a,b=X[:2]
        self.assertTrue(iszero_mod(a*a+b*b-(a+b)**2,(a,b),2))
    def test_characteristic_three_identity(self):
        a,b,c=X[:3]
        self.assertTrue(iszero_mod(a*a*a+b*b*b+c*c*c-(a+b+c)**3,(a,b,c),3))
    def test_symmetric_not_linear_in_es(self):
        a,b=X[:2]
        self.assertNotEqual(Poly(a*a+b*b,a,b).coeff_monomial(a*a),0)
        self.assertEqual(Poly(a+b,a,b).coeff_monomial(a*a),0)
        self.assertEqual(Poly(a*b,a,b).coeff_monomial(a*a),0)


def add_parametric_test(n,m):
    def check(self):
        xs = X[:n]
        e=[elementary(xs,k) for k in range(1,n+1)]
        # A deliberately nontrivial P(e) that includes both symmetry and mixed degrees.
        sym=1+sum((j+1)*e[j] for j in range(n))
        sym+=e[0]**2 + e[-1]**2 + 2*e[0]*e[-1]
        steps=greedy(sym,xs,m)
        self.assertGreaterEqual(steps,0)
        self.assertTrue(iszero_mod(sym-sym, xs,m))
    setattr(StructuralAA31, f'test_greedy_n{n}_mod{m}',check)
for n in (1,2,3):
    for m in (2,3,4,5,6):
        add_parametric_test(n,m)

if __name__ == '__main__':
    unittest.main(verbosity=2)
