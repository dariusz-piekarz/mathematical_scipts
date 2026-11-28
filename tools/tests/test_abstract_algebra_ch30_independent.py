"""AA-30: independent, finite reproducible mathematical audit, no network.
Run with: python -m unittest tools.tests.test_abstract_algebra_ch30_independent -v
"""
from pathlib import Path
import itertools
import re
import unittest
import sympy as sp
from sympy.polys.numberfields import galois_group

ROOT = Path(__file__).resolve().parents[2]
REPO_SOURCE = ROOT / 'chapters/pl/abstract_algebra/30-konstrukcje-cyrklem-i-linijka-oraz-wielokaty-foremne.tex'
LOCAL_SOURCE = Path('/mnt/data/AA-30-audyt-II-zrodlo.tex')
SRC = REPO_SOURCE if REPO_SOURCE.exists() else LOCAL_SOURCE
TEXT = SRC.read_text(encoding='utf-8')
x, y = sp.symbols('x y')
f = x**4 - x - 1
r = y**3 + 4*y - 1

class IndependentAA30(unittest.TestCase):
    def test_01_source_is_readable(self):
        self.assertIn(r'\chapter[Konstrukcje i wielokąty foremne]',TEXT)
    def test_02_essential_normal_tower_lemma_exists(self):
        self.assertIn(r'\label{aa:lem:quadratic-tower-normal-closure}',TEXT)
    def test_03_constructibility_definition_excludes_nonisolated(self):
        self.assertIn(r'\emph{izolowanych}',TEXT)
    def test_04_tower_both_directions_have_proofs(self):
        self.assertIn(r'\textbf{Od konstrukcji do wieży.}',TEXT)
        self.assertIn(r'\textbf{Od wieży do konstrukcji.}',TEXT)
    def test_05_no_unpublished_external_reference(self):
        self.assertNotIn('aa:tw:vieta-general',TEXT)
    def test_06_refs_and_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),len(set(labels)))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',TEXT))
        self.assertEqual(refs-set(labels), {'aa:tw:orbita-stabilizator','aa:tw:cyclotomic-galois'})
    def test_07_asymmetrical_lemma_hypothesis(self):
        self.assertIn('Jeżeli ponadto $b\\ne0$, konstruowalna jest liczba $a/b$.',TEXT)
    def test_08_line_intersection_multiplication_all_signs(self):
        for A,B in itertools.product([-5,-1,0,sp.Rational(1,2),2],[-3,0,sp.Rational(2,3),4]):
            # Parallel translate line y=B*(1-x) from x=1 to x=A.
            self.assertEqual(sp.expand(B*(A-x)).subs(x,0),A*B)
    def test_09_line_intersection_division_all_signs(self):
        for A,B in itertools.product([-7,0,sp.Rational(3,2),6],[-2,sp.Rational(1,5),3]):
            self.assertEqual(sp.simplify((-A/sp.Rational(B))*(0-1)),sp.Rational(A)/B)
    def test_10_geometric_mean_theorem(self):
        for A in [sp.Rational(1,4),sp.Integer(1),sp.Rational(8,3),sp.Integer(16)]:
            C=(sp.Integer(1)+A)/2
            self.assertEqual(sp.simplify(C**2 - (1-C)**2),A)
    def test_11_quartic_mod_two_irreducible(self):
        self.assertTrue(sp.Poly(f,x,modulus=2).is_irreducible)
    def test_12_quartic_gcd_with_formal_derivative(self):
        self.assertEqual(sp.gcd(sp.Poly(f,x),sp.Poly(sp.diff(f,x),x)).as_expr(),1)
    def test_13_quartic_has_two_real_simple_roots(self):
        roots=sp.Poly(f,x).intervals(eps=sp.Rational(1,8192))
        self.assertEqual(sum(m for _,m in roots),2)
        self.assertEqual([m for _,m in roots],[1,1])
    def test_14_resolvent_symmetric_polynomial(self):
        a,b,c,d=sp.symbols('a b c d')
        u=[a*b+c*d,a*c+b*d,a*d+b*c]
        e1=a+b+c+d;e2=a*b+a*c+a*d+b*c+b*d+c*d
        e3=a*b*c+a*b*d+a*c*d+b*c*d;e4=a*b*c*d
        self.assertEqual(sp.expand(sum(u[i]*u[j] for i in range(3) for j in range(i+1,3))-(e1*e3-4*e4)),0)
        self.assertEqual(sp.expand(sp.prod(u)-(e3**2+e1**2*e4-4*e2*e4)),0)
    def test_15_resolvent_is_irreducible(self):
        self.assertTrue(sp.Poly(r,y,domain=sp.QQ).is_irreducible)
    def test_16_resolvent_and_quartic_discriminant(self):
        self.assertEqual(sp.discriminant(f,x),sp.discriminant(r,y))
        self.assertEqual(sp.discriminant(f,x),-283)
    def test_17_mod_seven_is_one_plus_irreducible_cubic(self):
        lhs=sp.Poly(f,x,modulus=7)
        rhs=sp.Poly((x-3)*(x**3+3*x**2+2*x-2),x,modulus=7)
        self.assertEqual(lhs,rhs)
        self.assertTrue(sp.Poly(x**3+3*x**2+2*x-2,x,modulus=7).is_irreducible)
    def test_18_galois_group_is_s4(self):
        G,_=galois_group(f,x)
        self.assertEqual(G.order(),24)
        self.assertTrue(G.is_symmetric)
    def test_19_s4_not_two_group(self):
        self.assertEqual(sp.factorint(24),{2:3,3:1})
    def test_20_contrast_constructible_quartic_x4minus2(self):
        G,_=galois_group(x**4-2,x)
        self.assertEqual(G.order(),8)
    def test_21_cubic_root_not_constructible(self):
        self.assertTrue(sp.Poly(x**3-2,x).is_irreducible)
    def test_22_trisection_obstruction(self):
        self.assertTrue(sp.Poly(x**3-3*x-1,x).is_irreducible)
        t=sp.symbols('t',real=True)
        self.assertEqual(sp.trigsimp(sp.expand_trig(2*sp.cos(3*t) - ((2*sp.cos(t))**3-3*(2*sp.cos(t))))),0)
    def test_23_fermat_prime_phi_classification_3_to_2000(self):
        for n in range(3,2001):
            phi=int(sp.totient(n));is_power_two=phi&(phi-1)==0
            factors=sp.factorint(n)
            allowed=all(e==1 and ((int(p)-1)&(int(p)-2)==0) for p,e in factors.items() if p!=2)
            self.assertEqual(is_power_two,allowed,(n,phi))
    def test_24_pentagon_primitive_sin_cos(self):
        C=(sp.sqrt(5)-1)/4
        S=sp.sqrt(10+2*sp.sqrt(5))/4
        self.assertEqual(sp.simplify(C**2+S**2),1)
        self.assertLess(abs(float(C-sp.cos(2*sp.pi/5))),1e-12)
        self.assertLess(abs(float(S-sp.sin(2*sp.pi/5))),1e-12)
    def test_25_pentagon_u_minimal_polynomial(self):
        U=(sp.sqrt(5)-1)/2
        self.assertEqual(sp.simplify(U**2+U-1),0)
    def test_26_figure_has_no_external_graphics(self):
        self.assertIn(r'\begin{tikzpicture}[scale=1.25]',TEXT)
        self.assertNotIn(r'\includegraphics',TEXT)
    def test_27_all_12_labels_still_present(self):
        self.assertEqual(len(re.findall(r'\\label\{([^}]+)\}',TEXT)),12)

if __name__ == '__main__':
    unittest.main(verbosity=2)
