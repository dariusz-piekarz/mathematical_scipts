"""AA-30, independent first-audit regression checks (local, not a CI run)."""
import re
import unittest
from pathlib import Path
import sympy as sp

REPO_SOURCE = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/30-konstrukcje-cyrklem-i-linijka-oraz-wielokaty-foremne.tex'
LOCAL_SOURCE = Path('/mnt/data/AA-30-audyt-II-zrodlo.tex')
SRC = REPO_SOURCE if REPO_SOURCE.exists() else LOCAL_SOURCE
TEXT = SRC.read_text(encoding='utf-8')
x,y,a,b,c,d=sp.symbols('x y a b c d')
f=x**4-x-1
R=y**3+4*y-1

class AA30Audit(unittest.TestCase):
    def test_01_labels_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),12)
        self.assertEqual(len(set(labels)),12)
    def test_02_internal_refs(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',TEXT))
        self.assertEqual(refs-labels,{'aa:tw:orbita-stabilizator','aa:tw:cyclotomic-galois'})
    def test_03_no_forward_reference(self):
        self.assertNotIn('aa:tw:vieta-general',TEXT)
    def test_04_environments(self):
        for e in ['twierdzenie','lemat','wniosek','przyklad','uwaga','definicja','proof','tikzpicture']:
            self.assertEqual(TEXT.count('\\begin{'+e+'}'),TEXT.count('\\end{'+e+'}'),e)
    def test_05_no_old_geometry_error(self):
        self.assertIn('Odbicie $(0,ab)$ względem prostej $y=x$',TEXT)
    def test_06_multiplication_geometry(self):
        for A in [-3,-sp.Rational(2,3),0,sp.Rational(1,2),2,7]:
            for B in [-5,-sp.Rational(1,4),0,sp.Rational(3,2),4]:
                self.assertEqual(sp.expand(B*(A-0)),A*B)
                self.assertEqual(B*(A-0),A*B)
    def test_07_division_geometry(self):
        for A in [-3,0,sp.Rational(4,3),5]:
            for B in [-2,sp.Rational(1,3),1,4]:
                A,B=sp.Rational(A),sp.Rational(B)
                # Line through (B,0),(0,A) has equation y=A-(A/B)x.
                self.assertEqual(sp.simplify(A-(A/B)*B),0)
                # Parallel line through (1,0) meets y-axis at A/B.
                m=-A/B
                self.assertEqual(sp.simplify(-m-A/B),0)
    def test_08_sqrt_circle_formula(self):
        t=sp.symbols('t',real=True,positive=True)
        self.assertEqual(sp.expand(((1-(1+t)/2)**2+t)-((1+t)/2)**2),0)
    def test_09_quartic_irreducible_mod2(self):
        self.assertTrue(sp.Poly(f,x,modulus=2).is_irreducible)
    def test_10_quartic_irreducible_Q(self):
        self.assertTrue(sp.Poly(f,x,domain=sp.QQ).is_irreducible)
    def test_11_quartic_factor_mod7(self):
        self.assertEqual(sp.Poly(sp.expand((x-3)*(x**3+3*x**2+2*x-2)-f),x,modulus=7),sp.Poly(0,x,modulus=7))
    def test_12_cubic_mod7_irreducible(self):
        self.assertTrue(sp.Poly(x**3+3*x**2+2*x-2,x,modulus=7).is_irreducible)
    def test_13_cubic_mod7_values(self):
        h=x**3+3*x**2+2*x-2
        self.assertEqual([int(h.subs(x,k)%7) for k in range(7)],[5,4,1,2,6,5,5])
    def test_14_quartic_discriminant(self):
        self.assertEqual(sp.discriminant(f,x),-283)
    def test_15_resolvent_discriminant(self):
        self.assertEqual(sp.discriminant(R,y),-283)
    def test_16_resolvent_irreducible(self):
        self.assertTrue(sp.Poly(R,y,domain=sp.QQ).is_irreducible)
    def test_17_viete_e_constants(self):
        t=sp.symbols('t')
        expr=sp.expand((t-a)*(t-b)*(t-c)*(t-d))
        self.assertEqual(sp.expand(expr-t**4+(a+b+c+d)*t**3),
                         sp.expand((a*b+a*c+a*d+b*c+b*d+c*d)*t**2-(a*b*c+a*b*d+a*c*d+b*c*d)*t+a*b*c*d))
    def test_18_resolvent_symmetric_identities(self):
        u=[a*b+c*d,a*c+b*d,a*d+b*c]
        e1=a+b+c+d
        e2=a*b+a*c+a*d+b*c+b*d+c*d
        e3=a*b*c+a*b*d+a*c*d+b*c*d
        e4=a*b*c*d
        self.assertEqual(sp.expand(sum(u)-e2),0)
        self.assertEqual(sp.expand(sum(u[i]*u[j] for i in range(3) for j in range(i+1,3))-(e1*e3-4*e4)),0)
        self.assertEqual(sp.expand(sp.prod(u)-(e3**2+e1**2*e4-4*e2*e4)),0)
    def test_19_exactly_two_real_roots(self):
        roots=sp.polys.polytools.intervals(sp.Poly(f,x,domain=sp.QQ),eps=sp.Rational(1,1024))
        self.assertEqual(sum(m for _,m in roots),2)
    def test_20_S4_order_not_2_power(self):
        self.assertEqual(sp.factorint(sp.factorial(4)),{2:3,3:1})
    def test_21_double_cube(self):
        self.assertTrue(sp.Poly(x**3-2,x,domain=sp.QQ).is_irreducible)
    def test_22_trisection_polynomial(self):
        self.assertTrue(sp.Poly(x**3-3*x-1,x,domain=sp.QQ).is_irreducible)
    def test_23_triple_angle_identity(self):
        theta=sp.symbols('theta',real=True)
        expr=(2*sp.cos(theta))**3-3*(2*sp.cos(theta))-2*sp.cos(3*theta)
        self.assertEqual(sp.trigsimp(sp.expand_trig(expr)),0)
    def test_24_phi_values(self):
        self.assertEqual([int(sp.totient(n)) for n in [3,5,7,17]],[2,4,6,16])
    def test_25_gauss_wantzel_up_to_400(self):
        # Odd primes p that contribute to n must have p-1 a 2-power,
        # i.e. p a (known) Fermat prime; no odd square divides n.
        for n in range(3,401):
            val=int(sp.totient(n))
            direct=(val & (val-1))==0
            ff=sp.factorint(n)
            structural=all(e==1 and (int(p)-1)&(int(p)-2)==0 for p,e in ff.items() if p!=2)
            self.assertEqual(direct,structural, n)
    def test_26_pentagon_coordinate(self):
        co=(sp.sqrt(5)-1)/4
        si=sp.sqrt(10+2*sp.sqrt(5))/4
        self.assertEqual(sp.simplify(co**2+si**2),1)
        self.assertAlmostEqual(float(co),float(sp.cos(2*sp.pi/5)),places=14)
        self.assertAlmostEqual(float(si),float(sp.sin(2*sp.pi/5)),places=14)
    def test_27_pentagon_minimal(self):
        u=(sp.sqrt(5)-1)/2
        self.assertEqual(sp.simplify(u**2+u-1),0)
    def test_28_cyclotomic_galois_sizes(self):
        for n in range(3,25):
            self.assertEqual(sp.degree(sp.cyclotomic_poly(n,x),x),sp.totient(n))
    def test_29_pentagon_figure_present(self):
        self.assertIn('\\begin{tikzpicture}',TEXT)
        self.assertIn('\\node[anchor=south west] at (P1)',TEXT)
    def test_30_quartic_galois_group_s4(self):
        from sympy.polys.numberfields import galois_group
        group, _ = galois_group(f, x)
        self.assertEqual(group.order(),24)
        self.assertTrue(group.is_symmetric)
    def test_31_lemma_domains(self):
        self.assertIn('Jeżeli ponadto $b\\ne0$, konstruowalna jest liczba $a/b$.',TEXT)

if __name__=='__main__':unittest.main(verbosity=2)
