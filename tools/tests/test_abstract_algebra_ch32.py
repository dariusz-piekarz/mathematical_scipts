"""Niezależne testy AA-32 (audyt I). Python >= 3.10, SymPy.
Ważne: testy dla funkcji wymiernych mają skończony zakres; ogólne
uzasadnienie algebraiczne znajduje się w rozdziale.
"""
from __future__ import annotations
import unittest, re
from pathlib import Path
from itertools import product
from sympy import Symbol, Poly, discriminant, resultant, factor, gcd, symbols
from sympy.polys.domains import GF

SRC = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/32-wyroznik-i-grupa-galois.tex').read_text(encoding='utf8')
x,t=symbols('x t')

# Wielomiany nad F_2 reprezentowane jako maski bitowe współczynników.
def gf2_mul(a,b):
    v=0
    while b:
        if b&1:v^=a
        a<<=1
        b>>=1
    return v

def gf2_pow(a,n):
    r=1
    while n:
        if n&1:r=gf2_mul(r,a)
        a=gf2_mul(a,a);n>>=1
    return r

def deg(a):return a.bit_length()-1

class DiscriminantGaloisTests(unittest.TestCase):
    def test_source_label_uniqueness(self):
        v=re.findall(r'\\label\{([^}]*)\}', SRC)
        self.assertEqual(len(v),9)
        self.assertEqual(len(v),len(set(v)))
    def test_source_references(self):
        defined=set(re.findall(r'\\label\{([^}]*)\}',SRC))
        external={'aa:tw:fundamental-symmetric','aa:tw:vieta-general','aa:tw:orbita-stabilizator'}
        self.assertEqual(set(re.findall(r'\\ref\{([^}]*)\}',SRC))-defined,external)
    def test_latex_environment_balance(self):
        for env in ['twierdzenie','proof','definicja','przyklad','uwaga']:
            self.assertEqual(SRC.count(r'\begin{'+env+'}'),SRC.count(r'\end{'+env+'}'))
    def test_broken_math_delimiters_removed(self):
        self.assertNotIn('r^3+r=0\ne t',SRC)  # newline caused by broken backslash
        self.assertIn(r'r\ne0',SRC)
        self.assertIn(r'\alpha^2\ne0',SRC)
        self.assertNotIn('\ne0',SRC) # newline before e0
    def test_main_theorem_labels_present(self):
        for label in ['aa:tw:disc-separable','aa:tw:disc-alternating','aa:tw:cubic-disc','aa:tw:cubic-galois']:
            self.assertIn('\\label{'+label+'}',SRC)
    def test_disc_quadratic_formula_integers(self):
        a,b=symbols('a b')
        self.assertEqual(discriminant(x*x+a*x+b,x).expand(),a*a-4*b)
    def test_disc_repeated_root(self):
        self.assertEqual(discriminant((x-1)**2*(x+2),x),0)
    def test_disc_distinct_rational_roots(self):
        self.assertEqual(discriminant((x-1)*(x-2)*(x-3),x),4)
    def test_cubic_disc_over_Z(self):
        p,q=symbols('p q')
        self.assertEqual(discriminant(x**3+p*x+q,x).expand(),-4*p**3-27*q**2)
    def test_cubic_disc_resultant_identity(self):
        p,q=symbols('p q')
        f=x**3+p*x+q
        self.assertEqual(resultant(f,3*x*x+p,x).expand(),-(-4*p**3-27*q*q))
    def test_cubic_disc_characteristic_2(self):
        p,q=symbols('p q')
        d=Poly(-4*p**3-27*q**2,p,q,modulus=2)
        self.assertEqual(d,Poly(q*q,p,q,modulus=2))
    def test_cubic_disc_characteristic_3(self):
        p,q=symbols('p q')
        d=Poly(-4*p**3-27*q**2,p,q,modulus=3)
        self.assertEqual(d,Poly(-p**3,p,q,modulus=3))
    def test_cubic_example_S3_Q(self):
        f=x**3-2
        self.assertTrue(Poly(f,x,domain='QQ').is_irreducible)
        self.assertEqual(discriminant(f,x),-108)
        self.assertEqual(Poly(f,x).galois_group()[0].order(),6)
    def test_cubic_example_A3_Q(self):
        f=x**3-3*x+1
        self.assertTrue(Poly(f,x,domain='QQ').is_irreducible)
        self.assertEqual(discriminant(f,x),81)
        self.assertEqual(Poly(f,x).galois_group()[0].order(),3)
    def test_X3_plus_X_plus_1_F2(self):
        f=Poly(x**3+x+1,x,modulus=2)
        self.assertTrue(f.is_irreducible)
        self.assertEqual(f.diff(),Poly(x*x+1,x,modulus=2))
        self.assertEqual(Poly(-4-27,x,modulus=2),Poly(1,x,modulus=2))
    def test_h_derivative_F2(self):
        h=Poly(x**3+x+t,x,t,modulus=2)
        self.assertEqual(h.diff(x), Poly(x*x+1,x,t,modulus=2))
    def test_h_factorization_F2(self):
        a=symbols('a')
        lhs=Poly((x+a)*(x*x+a*x+a*a+1),x,a,modulus=2)
        rhs=Poly(x**3+x+a**3+a,x,a,modulus=2)
        self.assertEqual(lhs,rhs)
    def test_h_quadratic_substitution_F2(self):
        a,z=symbols('a z')
        f=Poly((a*z)**2+a*(a*z)+a*a+1,a,z,modulus=2)
        g=Poly(a*a*(z*z+z+1)+1,a,z,modulus=2)
        self.assertEqual(f,g)
    def test_h_rational_roots_low_degrees(self):
        # A^3+A B^2+t B^3=0: t represented by binary mask 0b10.
        for A in range(1,32):
            for B in range(1,32):
                v=gf2_pow(A,3)^gf2_mul(A,gf2_pow(B,2))^(gf2_pow(B,3)<<1)
                self.assertNotEqual(v,0,(A,B))
    def test_h_quadratic_AS_obstruction_low_degrees(self):
        # z^2+z=1+a^-2 => a^2 A^2+a^2 AB+(a^2+1)B^2=0.
        for A in range(32):
            for B in range(1,32):
                v=(gf2_pow(A,2)<<2)^(gf2_mul(A,B)<<2)^gf2_mul(0b101,gf2_pow(B,2))
                self.assertNotEqual(v,0,(A,B))
    def test_odd_cubic_discriminant_alternating(self):
        for p,q in [(0,-2),(-3,1),(1,1),(1,-1),(-2,3)]:
            d=discriminant(x**3+p*x+q,x)
            self.assertEqual(d,-4*p**3-27*q*q)
    def test_quadratic_example_F2t_inseparable(self):
        f=Poly(x*x+t,x,t,modulus=2)
        self.assertEqual(f.diff(x),Poly(0,x,t,modulus=2))
    def test_finite_quadratic_example_F2t_not_square_bounded(self):
        for A in range(1,32):
            for B in range(1,32):
                self.assertNotEqual(gf2_pow(A,2),gf2_pow(B,2)<<1)
    def test_full_discriminant_product_roots(self):
        roots=[0,1,2,4]
        d=1
        for i in range(len(roots)):
            for j in range(i+1,len(roots)):
                d*=(roots[i]-roots[j])**2
        f=1
        for z in roots:f*=x-z
        self.assertEqual(d,discriminant(f,x))
    def test_separability_independent(self):
        # gcd(f,f') over F2 when h=x^3+x+t (t transcendental):
        # only possible repeated root x=1, but h(1)=t.
        self.assertEqual(Poly(1+1+t,t,modulus=2),Poly(t,t,modulus=2))
    def test_w_algebra_identity(self):
        a,w=symbols('a w')
        # (a^-1+w)^2+(a^-1+w) : clearing a^2
        result=Poly((1+a*w)**2+a*(1+a*w),a,w,modulus=2)
        expected=Poly(1+a+a*a*(w*w+w),a,w,modulus=2)
        self.assertEqual(result,expected)

if __name__=='__main__':unittest.main(verbosity=2)
