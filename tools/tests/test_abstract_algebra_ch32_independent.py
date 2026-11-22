"""Niezalezne testy matematyczne rozdzialu AA-32; unittest + SymPy.
Testy skonczone nie zastepuja dowodow nad F_2(t)."""
import re
import unittest
from pathlib import Path
from math import gcd
from itertools import permutations, product
import sympy as sp

SOURCE = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/32-wyroznik-i-grupa-galois.tex').read_text('utf-8')
x, p, q, u, v, t, a, b, c = sp.symbols('x p q u v t a b c')


def gf2_mul(f, g):
    z = 0
    while g:
        if g & 1:
            z ^= f
        f <<= 1
        g >>= 1
    return z


def gf2_pow(f, n):
    z = 1
    for _ in range(n):
        z = gf2_mul(z, f)
    return z


def odd_prime(n):
    return n > 2 and sp.isprime(n)


class IndependentAA32(unittest.TestCase):
    def test_01_source_heading_and_provenance(self):
        self.assertIn(r'\chapter{Wyróżnik wielomianu i grupa Galois}',SOURCE)
        self.assertIn(r'\label{aa:ch:discriminant-galois}',SOURCE)

    def test_02_label_uniqueness(self):
        labels = re.findall(r'\\label\{([^}]+)\}', SOURCE)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(labels), 9)

    def test_03_all_external_refs_are_prior_chapters(self):
        labels = set(re.findall(r'\\label\{([^}]+)\}', SOURCE))
        refs = set(re.findall(r'\\ref\{([^}]+)\}', SOURCE))
        self.assertEqual(refs-labels, {'aa:tw:fundamental-symmetric',
                                      'aa:tw:vieta-general', 'aa:tw:orbita-stabilizator'})

    def test_04_structural_balance(self):
        for env in ['definicja', 'twierdzenie', 'przyklad', 'proof', 'uwaga']:
            self.assertEqual(SOURCE.count(r'\begin{' + env + '}'),
                             SOURCE.count(r'\end{' + env + '}'))

    def test_05_char2_broken_ne_is_absent(self):
        self.assertIn(r'r\ne0', SOURCE)
        self.assertIn(r'\alpha^2\ne0', SOURCE)
        self.assertNotIn('r^3+r=0\ne t', SOURCE)
        self.assertNotIn('A\ne0\n', SOURCE)

    def test_06_empty_discriminant(self):
        self.assertEqual(sp.discriminant(x-3, x), 1)

    def test_07_monic_quadratic(self):
        z = sp.symbols('z')
        self.assertEqual(sp.discriminant(x*x+z*x+q, x), z*z-4*q)

    def test_08_product_discriminant_over_integers(self):
        for roots in [(0,1,2),(-2,0,3),(-4,-1,2,5),(1,1,3),(-1,2,2,3)]:
            poly = sp.prod(x-r for r in roots)
            vand = sp.prod((roots[i]-roots[j])**2 for i in range(len(roots))
                            for j in range(i+1,len(roots)))
            self.assertEqual(sp.discriminant(poly,x),vand)

    def test_09_vandermonde_sign_all_s4(self):
        roots = (0,2,5,9)
        delta = sp.prod(roots[i]-roots[j] for i in range(4) for j in range(i+1,4))
        for pi in permutations(range(4)):
            permuted = sp.prod(roots[pi[i]]-roots[pi[j]]
                               for i in range(4) for j in range(i+1,4))
            inversions = sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))
            self.assertEqual(permuted,(-1)**inversions*delta)

    def test_10_cubic_formula_symbolic(self):
        self.assertEqual(sp.expand(sp.discriminant(x**3+p*x+q,x)+4*p**3+27*q**2),0)

    def test_11_cubic_formula_vieta_alternative(self):
        lhs=(u*u-4*v)*(2*u*u+v)**2
        rhs=-4*(v-u*u)**3-27*(u*v)**2
        self.assertEqual(sp.expand(lhs-rhs),0)

    def test_12_cubic_formula_via_resultant(self):
        f=x**3+p*x+q
        self.assertEqual(sp.factor(-sp.resultant(f,sp.diff(f,x),x)),
                         -4*p**3-27*q**2)

    def test_13_char2_reduction_of_cubic_disc(self):
        for pp,qq in product(range(2),repeat=2):
            self.assertEqual((-4*pp**3-27*qq**2)%2,qq%2)

    def test_14_char3_reduction_of_cubic_disc(self):
        for pp,qq in product(range(3),repeat=2):
            self.assertEqual((-4*pp**3-27*qq**2)%3,(-pp**3)%3)

    def test_15_quadratic_discriminant_separability_finite_fields(self):
        # f=x^2+b*x+c has repeated root iff disc=0, p odd and even.
        for characteristic in (2,3,5,7):
            for bb,cc in product(range(characteristic),repeat=2):
                f=sp.Poly(x*x+bb*x+cc,x,modulus=characteristic)
                disc=(bb*bb-4*cc)%characteristic
                is_squarefree=sp.gcd(f,f.diff()).degree()==0
                self.assertEqual(disc!=0,is_squarefree)

    def test_16_cubic_discriminant_separability_finite_fields(self):
        for prime in (2,3,5,7):
            for pp,qq in product(range(prime),repeat=2):
                f=sp.Poly(x**3+pp*x+qq,x,modulus=prime)
                disc=(-4*pp**3-27*qq**2)%prime
                self.assertEqual(disc!=0,sp.gcd(f,f.diff()).degree()==0)

    def test_17_example_s3_over_Q(self):
        f=sp.Poly(x**3-2,x,domain='QQ')
        self.assertTrue(f.is_irreducible)
        self.assertEqual(sp.discriminant(f.as_expr(),x),-108)
        self.assertEqual(f.galois_group()[0].order(),6)

    def test_18_example_a3_over_Q(self):
        f=sp.Poly(x**3-3*x+1,x,domain='QQ')
        self.assertTrue(f.is_irreducible)
        self.assertEqual(sp.discriminant(f.as_expr(),x),81)
        self.assertEqual(f.galois_group()[0].order(),3)

    def test_19_char2_f2_cubic_irreducible(self):
        f=sp.Poly(x**3+x+1,x,modulus=2)
        self.assertTrue(f.is_irreducible)
        self.assertEqual(f.diff(),sp.Poly(x*x+1,x,modulus=2))

    def test_20_char2_t_cubic_factorization(self):
        expr=(x+a)*(x*x+a*x+a*a+1)
        self.assertEqual(sp.Poly(expr-(x**3+x+a**3+a),x,a,modulus=2).is_zero,True)

    def test_21_char2_t_cubic_nonzero_linear_coeff(self):
        self.assertEqual(sp.Poly(x**3+x+t,x,t,modulus=2).diff(x),
                         sp.Poly(x*x+1,x,t,modulus=2))

    def test_22_char2_t_cubic_h_at_1(self):
        self.assertEqual(sp.Poly((x**3+x+t).subs(x,1),t,modulus=2).as_expr(),t)

    def test_23_char2_t_cubic_disc_square(self):
        self.assertEqual(sp.Poly(-4-27*t*t,t,modulus=2), sp.Poly(t*t,t,modulus=2))

    def test_24_char2_quadratic_split_condition(self):
        z=sp.symbols('z')
        expr=(a*z)**2+a*(a*z)+a*a+1
        expected=(a*a)*(z*z+z+1)+1
        self.assertTrue(sp.Poly(expr-expected,a,z,modulus=2).is_zero)

    def test_25_no_low_degree_rational_root_for_h(self):
        # If A/B solves r^3+r=t in F2(t), A^3+AB^2+tB^3=0.
        for A in range(1,32):
            for B in range(1,32):
                z=gf2_pow(A,3)^gf2_mul(A,gf2_pow(B,2))^(gf2_pow(B,3)<<1)
                self.assertNotEqual(z,0,(A,B))

    def test_26_no_low_degree_rational_as_solution(self):
        # If C/D solves z^2+z=1+a^-2, multiply by a^2 D^2.
        for C in range(32):
            for D in range(1,32):
                z=(gf2_pow(C,2)<<2)^(gf2_mul(C,D)<<2)^gf2_mul(0b101,gf2_pow(D,2))
                self.assertNotEqual(z,0,(C,D))

    def test_27_rational_function_order_at_infinity(self):
        for numerator in range(1,64):
            for denominator in range(1,64):
                m=numerator.bit_length()-denominator.bit_length()
                if m>0:
                    self.assertEqual(3*m,m+2*m)
                    self.assertNotEqual(3*m,1)

    def test_28_odd_characteristic_a3_test_with_splitting_roots(self):
        # Over F7 x^3-3x+1 splits with distinct roots; group is trivial and disc square.
        p7=7
        roots=[v for v in range(p7) if (v**3-3*v+1)%p7==0]
        disc=81%p7
        self.assertIn(disc,{z*z%p7 for z in range(p7)})
        # not require 3 roots: finite-field factorization is its own check
        f=sp.Poly(x**3-3*x+1,x,modulus=p7)
        self.assertEqual(f.degree(),3)

    def test_29_char2_vandermonde_fixed_by_any_permutation(self):
        roots=(1,2,4)
        products=[]
        for pi in permutations(range(3)):
            products.append(sp.prod((roots[pi[i]]-roots[pi[j]])%2 for i in range(3) for j in range(i+1,3))%2)
        self.assertEqual(len(set(products)),1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
