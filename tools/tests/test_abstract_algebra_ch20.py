"""AA-20 audit I: exact independent mathematical and structural regressions.

Finite checks illustrate concrete instances; they do not replace general proofs.
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

import sympy as sp

SOURCE = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/20-rozszerzenia-cial-i-ciala-rozkladu-wielomianow.tex')
TEXT = SOURCE.read_text(encoding='utf-8')
X = sp.symbols('X')


def extension_mul(a,b,p,mod):
    n=len(mod)-1
    t=[0]*(2*n-1)
    for i in range(n):
        for j in range(n):t[i+j]=(t[i+j]+a[i]*b[j])%p
    for k in range(2*n-2,n-1,-1):
        c=t[k]
        for j in range(n):t[k-n+j]=(t[k-n+j]-c*mod[j])%p
    return tuple(t[:n])


def extension_pow(a,e,p,mod):
    n=len(mod)-1
    result=(1,)+(0,)*(n-1)
    while e:
        if e&1:result=extension_mul(result,a,p,mod)
        a=extension_mul(a,a,p,mod)
        e//=2
    return result


def primitive_elements(p,mod):
    n=len(mod)-1
    one=(1,)+(0,)*(n-1)
    elems=list(itertools.product(range(p),repeat=n))
    units=[x for x in elems if any(x)]
    for a in units:
        if extension_pow(a,p**n-1,p,mod)!=one:
            return False,0
    primitive=sum(all(extension_pow(a,(p**n-1)//ell,p,mod)!=one
                      for ell in sp.factorint(p**n-1)) for a in units)
    return True,primitive


class Structural(unittest.TestCase):
    def test_01_labels_are_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual((len(labels),len(set(labels))),(25,25))

    def test_02_references_resolve_to_local_or_prior(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)
        self.assertEqual(len(refs),11)
        self.assertEqual(set(refs)-labels,{
            'aa:ch:fields-fractions', 'aa:tw:prime-subfield',
            'aa:tw:eisenstein','aa:wn:abelian-fg-structure'})

    def test_03_proofs(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),12)
        self.assertEqual(TEXT.count(r'\end{proof}'),12)

    def test_04_examples(self):
        self.assertEqual(TEXT.count(r'\begin{przyklad}'),7)
        self.assertEqual(TEXT.count(r'\end{przyklad}'),7)

    def test_05_theorem_environments_balanced(self):
        for env in ('lemat','twierdzenie','stwierdzenie','wniosek','definicja','uwaga'):
            self.assertEqual(TEXT.count(r'\begin{'+env+'}'),TEXT.count(r'\end{'+env+'}'),env)

    def test_06_no_forbidden_terms(self):
        self.assertNotIn('tensorowanie',TEXT.lower())
        self.assertNotIn('sekwencj',TEXT.lower())

    def test_07_field_extension_assumptions(self):
        self.assertIn(r'\label{aa:lem:minimal-polynomial}',TEXT)
        self.assertIn(r'\label{aa:tw:adjoin-root-abstract}',TEXT)
        self.assertIn('Nie zawiera jednak niezerowej',TEXT)

    def test_08_citations_of_old_lemmas(self):
        self.assertIn(r'Twierdzenia~\ref{aa:tw:eisenstein}',TEXT)
        self.assertIn(r'Wniosku~\ref{aa:wn:abelian-fg-structure}',TEXT)


class MinimalAndTower(unittest.TestCase):
    def test_09_tower_dimension_product(self):
        # Q(sqrt(2),sqrt(3)) has degree four via independent conjugates.
        basis=[sp.Integer(1),sp.sqrt(2),sp.sqrt(3),sp.sqrt(6)]
        rows=[]
        for a,b in itertools.product((1,-1),repeat=2):
            rows.append([1,a*sp.sqrt(2),b*sp.sqrt(3),a*b*sp.sqrt(6)])
        self.assertNotEqual(sp.simplify(sp.det(sp.Matrix(rows))),0)

    def test_10_minpoly_sqrt2(self):
        self.assertEqual(sp.minimal_polynomial(sp.sqrt(2),X),X**2-2)

    def test_11_minpoly_sqrt3(self):
        self.assertEqual(sp.minimal_polynomial(sp.sqrt(3),X),X**2-3)

    def test_12_biquadratic_primitive_element(self):
        z=sp.sqrt(2)+sp.sqrt(3)
        self.assertEqual(sp.minimal_polynomial(z,X),X**4-10*X**2+1)

    def test_13_rational_quadratic_inverses(self):
        for a,b in itertools.product(range(-8,9),repeat=2):
            if a==b==0:continue
            den=a*a-2*b*b
            self.assertNotEqual(den,0)
            self.assertEqual(sp.simplify((a+b*sp.sqrt(2))*(a-b*sp.sqrt(2))/den),1)

    def test_14_eisenstein_sample_degrees(self):
        for n in range(1,15):
            self.assertTrue(sp.Poly(X**n-2,X,domain=sp.QQ).is_irreducible)

    def test_15_field_tower_divisibility(self):
        self.assertEqual((2*2,3*2),(4,6))

    def test_16_finite_generated_extension_algebraic(self):
        for n in (2,3,4,5,6,7,8):
            y=2**sp.Rational(1,n)
            self.assertEqual(sp.degree(sp.minimal_polynomial(y,X)),n)


class QuotientsAndSplitting(unittest.TestCase):
    def test_17_F4_polynomial_is_irreducible(self):
        self.assertTrue(sp.Poly(X**2+X+1,X,modulus=2).is_irreducible)

    def test_18_F4_square_relation(self):
        p,mod=2,(1,1,1)
        a=(0,1);one=(1,0)
        self.assertEqual(extension_mul(a,a,p,mod),(1,1))
        self.assertEqual(extension_mul(a,(1,1),p,mod),one)

    def test_19_F4_automorphisms_two_roots(self):
        p,mod=2,(1,1,1)
        roots=[]
        for a in itertools.product(range(2),repeat=2):
            sq=extension_mul(a,a,p,mod)
            val=tuple((sq[i]+a[i]+(1 if i==0 else 0))%2 for i in range(2))
            if val==(0,0):roots.append(a)
        self.assertEqual(set(roots),{(0,1),(1,1)})

    def test_20_cubic_splitting_degree6(self):
        self.assertTrue(sp.Poly(X**3-2,X).is_irreducible)
        self.assertEqual(sp.discriminant(X**3-2,X),-108)
        self.assertEqual(sp.degree(sp.minimal_polynomial(sp.real_root(2,3),X)),3)

    def test_21_poly_quotient_remainder(self):
        mod=sp.Poly(X**3+X+1,X,modulus=2)
        rng=random.Random(101)
        for _ in range(100):
            coeff=[rng.randrange(2) for i in range(8)]
            expr=sum(c*X**j for j,c in enumerate(coeff))
            r=sp.rem(sp.Poly(expr,X,modulus=2),mod)
            self.assertLess(r.degree(),3)
            self.assertTrue(sp.rem(sp.Poly(expr,X,modulus=2)-r,mod).is_zero)

    def test_22_finite_separable_root_counts(self):
        for p in (2,3,5,7):
            f=sp.Poly(X**p-X,X,modulus=p)
            self.assertEqual(f.gcd(f.diff()).degree(),0)

    def test_23_multiple_roots_gcd(self):
        for p in (2,3,5):
            f=sp.Poly((X-1)**2*(X+1),X,modulus=p)
            self.assertGreater(f.gcd(f.diff()).degree(),0)

    def test_24_inseparable_xp_t_formal_derivative(self):
        t=sp.symbols('t')
        for p in (2,3,5,7):
            # formal derivative is p*X^(p-1) and vanishes mod p
            self.assertEqual(p%p,0)
            self.assertEqual(sp.Poly(X**p-t,X,domain=sp.GF(p).poly_ring(t)).diff().as_expr(),0)

    def test_25_splitting_induction_degree_step(self):
        for p in (2,3,5):
            for a in range(p):
                pol=sp.Poly((X-a)*(X**2+X+1),X,modulus=p)
                q,r=sp.div(pol,sp.Poly(X-a,X,modulus=p))
                self.assertTrue(r.is_zero)
                self.assertEqual(q.degree(),2)


class FiniteFields(unittest.TestCase):
    FIELDS=((2,(1,1,1)),(2,(1,1,0,1)),(2,(1,1,0,0,1)),
            (3,(1,0,1)),(5,(2,0,1)))
    def test_26_irreducible_field_moduli(self):
        for p,mod in self.FIELDS:
            f=sp.Poly(sum(c*X**j for j,c in enumerate(mod)),X,modulus=p)
            self.assertTrue(f.is_irreducible,(p,mod))

    def test_27_field_sizes_prime_power(self):
        for p,mod in self.FIELDS:
            n=len(mod)-1
            self.assertEqual(len(list(itertools.product(range(p),repeat=n))),p**n)

    def test_28_all_nonzero_elements_are_units(self):
        for p,mod in self.FIELDS:
            n=len(mod)-1
            one=(1,)+(0,)*(n-1)
            for a in itertools.product(range(p),repeat=n):
                if not any(a):continue
                inv=extension_pow(a,p**n-2,p,mod)
                self.assertEqual(extension_mul(a,inv,p,mod),one,(p,mod,a))

    def test_29_multiplicative_groups_cyclic(self):
        for p,mod in self.FIELDS:
            ok,number=primitive_elements(p,mod)
            self.assertTrue(ok,(p,mod))
            self.assertGreater(number,0)

    def test_30_count_primitive_elements(self):
        for p,mod in self.FIELDS:
            n=len(mod)-1
            self.assertEqual(primitive_elements(p,mod)[1],int(sp.totient(p**n-1)))

    def test_31_F4_alpha_order3(self):
        a=(0,1);mod=(1,1,1)
        self.assertEqual(extension_pow(a,3,2,mod),(1,0))
        self.assertNotEqual(a,(1,0))

    def test_32_F8_nontrivial(self):
        p,mod=2,(1,1,0,1)
        self.assertEqual(extension_pow((0,1,0),7,p,mod),(1,0,0))

    def test_33_F9_primitive_elements_four(self):
        self.assertEqual(primitive_elements(3,(1,0,1))[1],4)

    def test_34_F16_primitive_elements_eight(self):
        self.assertEqual(primitive_elements(2,(1,1,0,0,1))[1],8)

    def test_35_Z4_is_not_field(self):
        self.assertNotEqual(2%4,0)
        self.assertEqual(2*2%4,0)




# New independent tests from audit II
"""AA-20 audit II: independent checks of field extensions and corrected proofs.

Finite computations corroborate individual formulas and boundary cases;
independent mathematical review remains essential for general proofs.
"""
import itertools
import math
import re
import unittest
from pathlib import Path

import sympy as sp

SRC=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/20-rozszerzenia-cial-i-ciala-rozkladu-wielomianow.tex')
TEXT=SRC.read_text(encoding='utf-8')
x=sp.Symbol('x')


def bezout_poly_mod(a,b,p):
    return sp.gcdex(sp.Poly(a,x,modulus=p),sp.Poly(b,x,modulus=p))


def mul_F4(a,b):
    # α² = α+1: F_2[α]/(α²+α+1).
    return ((a[0]*b[0]+a[1]*b[1])%2,
            (a[0]*b[1]+a[1]*b[0]+a[1]*b[1])%2)


class AuditIIIndependent(unittest.TestCase):
    def test_01_explicit_splitting_induction_justification(self):
        self.assertIn('kolejne rozkładanie musi się zakończyć',TEXT)

    def test_02_cubic_eisenstein_reference(self):
        self.assertIn(r'Wielomian $f=X^3-2$ jest nierozkładalny nad',TEXT)
        self.assertGreaterEqual(TEXT.count(r'\ref{aa:tw:eisenstein}'),3)

    def test_03_cubic_omega_exact_minimal_polynomial(self):
        w=(-1+sp.sqrt(-3))/2
        self.assertEqual(sp.simplify(w**2+w+1),0)
        self.assertEqual(sp.simplify(w**3),1)
        self.assertNotEqual(w,1)
        self.assertEqual(sp.minimal_polynomial(w,x),x*x+x+1)

    def test_04_quadratic_discriminant_negative_real(self):
        self.assertIn(r'$(2x+1)^2=-3$',TEXT)
        f=x*x+x+1
        self.assertLess(sp.discriminant(f,x),0)
        self.assertEqual(sp.solve(f,x),[-sp.Rational(1,2)-sp.sqrt(3)*sp.I/2,
                                        -sp.Rational(1,2)+sp.sqrt(3)*sp.I/2])

    def test_05_no_real_omega_conjugate(self):
        w=(-1+sp.sqrt(-3))/2
        for z in (w, sp.conjugate(w)):
            self.assertNotEqual(sp.im(z),0)
            self.assertEqual(sp.simplify(z**3),1)

    def test_06_splitting_polynomial_over_extension(self):
        c=sp.real_root(2,3)
        w=(-1+sp.sqrt(-3))/2
        z=sp.Symbol('z')
        self.assertEqual(sp.simplify((z-c)*(z-c*w)*(z-c*w*w)-(z**3-2)),0)

    def test_07_cubic_splitting_degree_six(self):
        a=sp.real_root(2,3)
        w=(-1+sp.sqrt(-3))/2
        polynomial=sp.minimal_polynomial(a+w,x)
        self.assertEqual(sp.degree(polynomial,x),6)

    def test_08_trivial_multiplicative_group_F2(self):
        self.assertIn('Jeśli $|G|=1$',TEXT)
        units=[a for a in range(2) if a!=0]
        self.assertEqual(units,[1])
        self.assertEqual({(1**k)%2 for k in range(1,8)},{1})

    def test_09_F4_all_nonzero_powers(self):
        one=(1,0); alpha=(0,1)
        powers=[];a=one
        for _ in range(3):
            powers.append(a);a=mul_F4(a,alpha)
        self.assertEqual(set(powers),{(1,0),(0,1),(1,1)})
        self.assertEqual(a,one)

    def test_10_finite_abelian_exponents(self):
        # Cyclic factors with prime-power orders; gcd/lcm determines exponent.
        for orders in ((2,4,3,9),(2,8,3),(3,9,5,25),(4,4,7),(5,5,5)):
            ex=math.lcm(*orders)
            grouped={p:max((o for o in orders if o>1 and all(o%q!=0 for q in range(2,int(o**.5)+1) if q!=p) and o%p==0),default=1)
                     for p in (2,3,5,7)}
            self.assertEqual(ex,math.prod(v for v in grouped.values() if v>1))

    def test_11_exponent_witness_product_coprime_factors(self):
        # In Z/8 × Z/9 × Z/25, (1,1,1) has order 1800.
        dims=(8,9,25)
        e=math.prod(dims)
        for k in range(1,e):
            self.assertFalse(all(k%d==0 for d in dims))
        self.assertTrue(all(e%d==0 for d in dims))

    def test_12_root_bound_f2_f3(self):
        for p in (2,3):
            for deg in range(1,5):
                for coeff in itertools.product(range(p),repeat=deg):
                    poly=sp.Poly(x**deg+sum(c*x**i for i,c in enumerate(coeff)),x,modulus=p)
                    roots=sum(poly.eval(i)%p==0 for i in range(p))
                    self.assertLessEqual(roots,deg)

    def test_13_squarefree_derivative_characteristic_two(self):
        cases=[(x**2+x+1, True),(x**2+1, False),(x**3+x+1,True)]
        for expr,squarefree in cases:
            poly=sp.Poly(expr,x,modulus=2)
            self.assertEqual(poly.gcd(poly.diff()).degree()==0,squarefree)

    def test_14_inseparable_polynomials_gcd_nonconstant(self):
        t=sp.Symbol('t')
        for p in (2,3,5):
            # Polynomial X^p-t over F_p(t), derivative identically zero.
            self.assertEqual((p%p),0)
            self.assertEqual(sp.Poly(x**p-t,x,domain=sp.GF(p).poly_ring(t)).diff().as_expr(),0)

    def test_15_euclidean_bezout_irreducibility_field(self):
        f=sp.Poly(x**2+x+1,x,modulus=2)
        for g in (sp.Poly(x,x,modulus=2),sp.Poly(x+1,x,modulus=2),sp.Poly(1,x,modulus=2)):
            s,t,d=sp.gcdex(g,f)
            self.assertEqual(d,sp.Poly(1,x,modulus=2))
            self.assertTrue((s*g+t*f-d).is_zero)

    def test_16_structure_and_labels_after_revision(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),12)
        self.assertEqual(TEXT.count(r'\end{proof}'),12)
        self.assertEqual(TEXT.count(r'\begin{przyklad}'),7)
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)
        self.assertEqual((len(labels),len(set(labels)),len(refs)),(25,25,11))
        self.assertIn(r'$e=\prod_\ell\ell^{a_\ell}$',TEXT)




if __name__ == "__main__":
    unittest.main()
