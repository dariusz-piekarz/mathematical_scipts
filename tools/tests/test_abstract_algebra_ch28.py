"""AA-28 audit I: independent cyclotomic algebra and source integrity tests.
Run: python -m unittest tools.tests.test_abstract_algebra_ch28 -v
"""
import math
import re
import unittest
from pathlib import Path
from sympy import (Symbol, Poly, QQ, ZZ, I, sqrt, cyclotomic_poly,
                   totient, divisors, factor_list, gcd, expand, primitive_root)
from sympy.polys.domains import GF

ROOT=Path(__file__).resolve().parents[2]
CHAPTER=ROOT / 'chapters/pl/abstract_algebra/28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex'
if not CHAPTER.exists(): CHAPTER=Path('/mnt/data/AA-28-audyt-I-zrodlo.tex')
SOURCE=CHAPTER.read_text(encoding='utf8')
x=Symbol('x')

class TestCyclotomicMath(unittest.TestCase):
    def test_01_degrees_equal_totient(self):
        for n in range(1,101):
            self.assertEqual(Poly(cyclotomic_poly(n,x),x).degree(),int(totient(n)),n)
    def test_02_integral_monic(self):
        for n in range(1,101):
            p=Poly(cyclotomic_poly(n,x),x,domain=ZZ)
            self.assertEqual(p.LC(),1,n)
    def test_03_product_identity(self):
        for n in range(1,81):
            q=Poly(1,x,domain=ZZ)
            for d in divisors(n): q*=Poly(cyclotomic_poly(d,x),x,domain=ZZ)
            self.assertEqual(q,Poly(x**n-1,x,domain=ZZ),n)
    def test_04_irreducibility_over_Q(self):
        for n in range(1,81):
            self.assertTrue(Poly(cyclotomic_poly(n,x),x,domain=QQ).is_irreducible,n)
    def test_05_phi_1(self):
        self.assertEqual(cyclotomic_poly(1,x),x-1)
    def test_06_phi_5(self):
        self.assertEqual(cyclotomic_poly(5,x),x**4+x**3+x**2+x+1)
    def test_07_phi_8(self):
        self.assertEqual(cyclotomic_poly(8,x),x**4+1)
    def test_08_unit_group_5(self):
        self.assertEqual([(2**k)%5 for k in range(1,5)],[2,4,3,1])
    def test_09_unit_group_8_klein(self):
        self.assertEqual([k for k in range(8) if math.gcd(k,8)==1],[1,3,5,7])
        for k in (3,5,7):self.assertEqual(k*k%8,1)
    def test_10_zeta5_real_subfield_polynomial(self):
        q=Poly(cyclotomic_poly(5,x),x,domain=ZZ)
        # x^2 * ((x + 1/x)^2 +(x + 1/x) - 1) modulo Phi_5
        z=x
        relation=(z*z+1)**2+z*(z*z+1)-z*z
        self.assertEqual(Poly(relation,x,domain=ZZ).rem(q),Poly(0,x,domain=ZZ))
        self.assertTrue(Poly(x*x+x-1,x,domain=QQ).is_irreducible)
    def test_11_mod3_phi3_repeated_root(self):
        p=Poly(cyclotomic_poly(3,x),x,modulus=3)
        h=Poly((x-1)**2,x,modulus=3)
        self.assertEqual(p,h)
        self.assertEqual(gcd(p,p.diff()).degree(),1)
    def test_12_mod2_phi5_irreducible(self):
        self.assertTrue(Poly(cyclotomic_poly(5,x),x,modulus=2).is_irreducible)
    def test_13_mod11_phi5_splits(self):
        p=Poly(cyclotomic_poly(5,x),x,modulus=11)
        self.assertEqual(len([a for a in range(11) if p.eval(a)==0]),4)
    def test_14_prime_to_n_squarefree(self):
        for n in range(1,31):
            for ell in [2,3,5,7,11,13]:
                if n%ell==0:continue
                p=Poly(x**n-1,x,modulus=ell)
                self.assertEqual(gcd(p,p.diff()).degree(),0,(n,ell))
    def test_15_prime_dividing_n_nonsquarefree(self):
        for ell in [2,3,5,7]:
            for n in [ell,ell*2,ell*3]:
                p=Poly(x**n-1,x,modulus=ell)
                self.assertGreater(gcd(p,p.diff()).degree(),0,(n,ell))
    def test_16_order_partition_of_roots(self):
        for n in range(1,101):
            self.assertEqual(sum(int(totient(d)) for d in divisors(n)),n)
    def test_17_primitive_residues_acted_by_units(self):
        for n in range(2,81):
            U={k for k in range(1,n) if math.gcd(k,n)==1}
            for a in U:
                self.assertEqual({(a*k)%n for k in U},U,(n,a))
    def test_18_primitive_nth_powers(self):
        for n in range(2,81):
            for k in range(1,n):
                order=min(d for d in range(1,n+1) if (k*d)%n==0)
                self.assertEqual(order,n//math.gcd(n,k),(n,k))
    def test_19_source_labels_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SOURCE)
        self.assertEqual(len(labels),len(set(labels)))
    def test_20_source_refs_internal_or_verified_external(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',SOURCE))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',SOURCE))
        ext=refs-labels
        self.assertEqual(ext,{'aa:ch:fields-fractions','aa:ch:kummer'})
    def test_21_no_old_terminology(self):
        self.assertNotIn('injektywne',SOURCE)
        self.assertNotIn('pole elementów stałych',SOURCE)
    def test_22_figure_and_proof_present(self):
        self.assertIn('\\label{aa:fig:cyclotomic-five}',SOURCE)
        self.assertIn('\\label{aa:lem:cyclotomic-prime}',SOURCE)
        self.assertIn('\\label{aa:tw:cyclotomic-irreducible}',SOURCE)

if __name__=='__main__':unittest.main(verbosity=2)
