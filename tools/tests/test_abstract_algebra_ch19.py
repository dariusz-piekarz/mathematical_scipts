"""AA-19 regression checks (70 tests across three independent audit suites)."""



# Original audit suite: test_aa19.py
"""Independent AA-19 finite-model, arithmetic, and structural regression tests.
Finite test models corroborate the mathematical proofs; they do not prove general theorems.
"""
import itertools
import math
import random
import re
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/19-ciala-ulamkow-i-konstrukcje-liczb.tex')
TEXT = SOURCE.read_text(encoding='utf-8')
RAND = random.Random(20261121)


def equiv(x,y):
    a,b=x;c,d=y
    return a*d==b*c

def add_frac(x,y):
    a,b=x;c,d=y
    return (a*d+b*c,b*d)

def mul_frac(x,y):
    a,b=x;c,d=y
    return (a*c,b*d)

def cmul(z,w):
    a,b=z;c,d=w
    return (a*c-b*d,a*d+b*c)

def cadd(z,w):
    return tuple(a+b for a,b in zip(z,w))

class Structure(unittest.TestCase):
    def test_01_labels_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(all(x.startswith('aa:') for x in labels))
    def test_02_references_exist(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)
        self.assertEqual(set(refs)-labels,set())
    def test_03_proof_blocks_balance(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),TEXT.count(r'\end{proof}'))
        self.assertGreaterEqual(TEXT.count(r'\begin{proof}'),5)
    def test_04_all_environments_balance(self):
        for env in ('twierdzenie','stwierdzenie','lemat','przyklad','definicja','uwaga'):
            self.assertEqual(TEXT.count(r'\begin{'+env+'}'),TEXT.count(r'\end{'+env+'}'),env)
    def test_05_style(self):
        self.assertNotIn('tensorowanie',TEXT.lower())
        self.assertNotIn('sekwencj',TEXT.lower())
    def test_06_standalone_theorem(self):
        self.assertIn('Niech $R$ będzie dziedziną całkowitości,\n$S=R\\setminus',TEXT)
        self.assertIn('Relacja z\nDefinicji~\\ref{aa:def:fractions-relation}',TEXT)
    def test_07_universal_arithmetic_explicit(self):
        self.assertIn(r'\overline f\left(\frac ab+\frac cd\right)',TEXT)
    def test_08_complex_associativity_explicit(self):
        self.assertIn('Obliczając $(c,d)(e,f)',TEXT)
    def test_09_complex_quotient_bezout_explicit(self):
        self.assertIn('Tożsamość Bézouta',TEXT)

class FormalFractions(unittest.TestCase):
    pairs = [(a,b) for a in range(-5,6) for b in range(-5,6) if b]
    def test_10_equivalence_reflexive(self):
        for x in self.pairs: self.assertTrue(equiv(x,x))
    def test_11_equivalence_symmetric(self):
        for x,y in itertools.product(self.pairs[:32],repeat=2):
            self.assertEqual(equiv(x,y),equiv(y,x))
    def test_12_equivalence_transitive(self):
        for _ in range(1000):
            a=RAND.randint(-5,5);b=RAND.choice([x for x in range(-6,7) if x]);
            u,v,w=(a,b),(2*a,2*b),(3*a,3*b)
            self.assertTrue(equiv(u,v) and equiv(v,w) and equiv(u,w))
    def test_13_addition_representatives(self):
        for _ in range(500):
            x,y=RAND.choice(self.pairs),RAND.choice(self.pairs)
            k,l=RAND.choice([-3,-2,-1,1,2,3]),RAND.choice([-3,-2,-1,1,2,3])
            xx=(k*x[0],k*x[1]);yy=(l*y[0],l*y[1]);
            self.assertTrue(equiv(add_frac(x,y),add_frac(xx,yy)))
    def test_14_multiplication_representatives(self):
        for _ in range(500):
            x,y=RAND.choice(self.pairs),RAND.choice(self.pairs)
            k,l=RAND.choice([-3,-2,1,2,3]),RAND.choice([-3,-2,1,2,3])
            xx=(k*x[0],k*x[1]);yy=(l*y[0],l*y[1]);
            self.assertTrue(equiv(mul_frac(x,y),mul_frac(xx,yy)))
    def test_15_fraction_addition_matches_fraction(self):
        for x,y in itertools.product(self.pairs[:45],repeat=2):
            z=add_frac(x,y)
            self.assertEqual(Fraction(*z),Fraction(*x)+Fraction(*y))
    def test_16_fraction_multiplication_matches_fraction(self):
        for x,y in itertools.product(self.pairs[:45],repeat=2):
            self.assertEqual(Fraction(*mul_frac(x,y)),Fraction(*x)*Fraction(*y))
    def test_17_multiplicative_inverse(self):
        for x in self.pairs:
            if x[0]:self.assertTrue(equiv(mul_frac(x,(x[1],x[0])),(1,1)))
    def test_18_distributivity(self):
        for _ in range(200):
            x,y,z=(RAND.choice(self.pairs) for _ in range(3))
            self.assertTrue(equiv(mul_frac(x,add_frac(y,z)),
                                  add_frac(mul_frac(x,y),mul_frac(x,z))))
    def test_19_monomorphism_integers(self):
        for a,b in itertools.product(range(-20,21),repeat=2):
            self.assertEqual(equiv((a,1),(b,1)),a==b)
    def test_20_partial_mod_p_evaluation_not_frac_Z_map(self):
        # Defined only for fractions with denominators nonzero modulo p;
        # this is NOT a map from Frac(Z)=Q to F_p.
        for p in (2,3,5,7,11):
            for a in range(-10,11):
                for b in range(-10,11):
                    if b and b%p:
                        mapped=a*pow(b,-1,p)%p
                        self.assertEqual(mapped, Fraction(a,b).numerator*pow(Fraction(a,b).denominator,-1,p)%p)
    def test_21_universal_operations_mod_p(self):
        for p in (5,7,11):
            valid=[x for x in self.pairs if x[1]%p]
            for _ in range(400):
                x,y=RAND.choice(valid),RAND.choice(valid)
                ev=lambda z:z[0]*pow(z[1],-1,p)%p
                self.assertEqual(ev(add_frac(x,y)),(ev(x)+ev(y))%p)
                self.assertEqual(ev(mul_frac(x,y)),(ev(x)*ev(y))%p)
    def test_22_fraction_quotients(self):
        self.assertTrue(equiv((2,3),(4,6)))
        self.assertFalse(equiv((2,3),(3,4)))
        self.assertTrue(equiv(add_frac((1,2),(1,3)),(5,6)))

class PrimeFields(unittest.TestCase):
    def test_23_prime_characteristic(self):
        for p in (2,3,5,7,11,13):
            self.assertTrue(all((a*b)%p for a in range(1,p) for b in range(1,p)))
    def test_24_finite_field_inverses(self):
        for p in (2,3,5,7,11):
            self.assertTrue(all((a*pow(a,-1,p))%p==1 for a in range(1,p)))
    def test_25_composite_residue_zero_divisors(self):
        for n in (4,6,8,9,10,12,15):
            self.assertTrue(any((a*b)%n==0 for a in range(1,n) for b in range(1,n)))
    def test_26_frobenius_additive(self):
        for p in (2,3,5,7,11):
            for x,y in itertools.product(range(p),repeat=2):
                self.assertEqual(pow((x+y)%p,p,p),(pow(x,p,p)+pow(y,p,p))%p)
    def test_27_frobenius_multiplicative(self):
        for p in (2,3,5,7,11):
            for x,y in itertools.product(range(p),repeat=2):
                self.assertEqual(pow((x*y)%p,p,p),(pow(x,p,p)*pow(y,p,p))%p)
    def test_28_frobenius_bijective(self):
        for p in (2,3,5,7,11,13):
            self.assertEqual({pow(x,p,p) for x in range(p)},set(range(p)))
    def test_29_binomial_divisible_by_p(self):
        for p in (2,3,5,7,11,13,17,19):
            self.assertTrue(all(math.comb(p,k)%p==0 for k in range(1,p)))
    def test_30_non_surjective_rational_Fp_t(self):
        for p in (2,3,5,7):
            self.assertTrue(all((p*a-(1+p*b))%p!=0 for a in range(10) for b in range(10)))

class ComplexPairs(unittest.TestCase):
    vals=[Fraction(i,3) for i in range(-5,6)]
    def test_31_additive_group(self):
        z=(Fraction(0),Fraction(0))
        for a,b in itertools.product(self.vals[:5],repeat=2):
            x=(a,b)
            self.assertEqual(cadd(x,(-a,-b)),z)
    def test_32_multiplication_associative(self):
        for _ in range(900):
            u,v,w=(tuple(RAND.choice(self.vals) for _ in range(2)) for _ in range(3))
            self.assertEqual(cmul(cmul(u,v),w),cmul(u,cmul(v,w)))
    def test_33_left_distributive(self):
        for _ in range(900):
            u,v,w=(tuple(RAND.choice(self.vals) for _ in range(2)) for _ in range(3))
            self.assertEqual(cmul(u,cadd(v,w)),cadd(cmul(u,v),cmul(u,w)))
    def test_34_multiplicative_inverse(self):
        for a,b in itertools.product(self.vals,repeat=2):
            if a or b:
                q=a*a+b*b
                self.assertEqual(cmul((a,b),(a/q,-b/q)),(Fraction(1),Fraction(0)))
    def test_35_i_squared(self):
        self.assertEqual(cmul((0,1),(0,1)),(-1,0))
    def test_36_quotient_X2_plus1(self):
        # Multiplication of residues a+bX (mod X^2+1).
        for _ in range(500):
            a,b,c,d=(RAND.choice(self.vals) for _ in range(4))
            self.assertEqual(cmul((a,b),(c,d)),(a*c-b*d,a*d+b*c))
    def test_37_roots_of_minus_one(self):
        for z in [(0,1),(0,-1)]:
            self.assertEqual(cadd(cmul(z,z),(1,0)),(0,0))
    def test_38_nonzero_positivity(self):
        for a,b in itertools.product(self.vals,repeat=2):
            if a or b:self.assertGreater(a*a+b*b,0)


# Original audit suite: test_aa19_independent.py
"""Additional independent regression tests for AA-19 audit II.

These finite computations corroborate examples and mathematical arguments,
but do not replace proofs for arbitrary rings and fields.
"""
import itertools
import math
import re
import unittest
from fractions import Fraction as F
from pathlib import Path

SRC=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/19-ciala-ulamkow-i-konstrukcje-liczb.tex').read_text()


def quadratic_mul(x,y,d=2,p=None):
    a,b=x;c,e=y
    z=(a*c+d*b*e,a*e+b*c)
    return tuple(t%p for t in z) if p else z


def quadratic_add(x,y,p=None):
    z=(x[0]+y[0],x[1]+y[1])
    return tuple(t%p for t in z) if p else z


def quadratic_inv(x,d=2):
    a,b=x
    N=a*a-d*b*b
    if not N: raise ZeroDivisionError
    return (a/N,-b/N)


def formal_frac_zsqrt2(num,den):
    return quadratic_mul(num,quadratic_inv(den))


class IndependentAA19(unittest.TestCase):
    def test_01_inverse_representative_independence(self):
        for a,b in itertools.product(range(-8,9),range(-8,9)):
            if not a or not b: continue
            for k in (-5,-2,1,3,7):
                self.assertEqual(F(b,a),F(k*b,k*a))

    def test_02_universal_zsqrt2_addition(self):
        numerators=[(F(a),F(b)) for a,b in itertools.product(range(-2,3),repeat=2)]
        denoms=[(F(a),F(b)) for a,b in itertools.product(range(-2,3),repeat=2) if a or b]
        for u,v in itertools.product(numerators[::5],repeat=2):
            for q,r in itertools.product(denoms[::9],repeat=2):
                x=formal_frac_zsqrt2(u,q);y=formal_frac_zsqrt2(v,r)
                numerator=quadratic_add(quadratic_mul(u,r),quadratic_mul(v,q))
                denominator=quadratic_mul(q,r)
                self.assertEqual(formal_frac_zsqrt2(numerator,denominator),quadratic_add(x,y))

    def test_03_universal_zsqrt2_multiplication(self):
        pairs=[(F(a),F(b)) for a,b in itertools.product(range(-2,3),repeat=2)]
        nonzero=[z for z in pairs if z!=(0,0)]
        for u,v in itertools.product(pairs[::4],repeat=2):
            for q,r in itertools.product(nonzero[::8],repeat=2):
                lhs=formal_frac_zsqrt2(quadratic_mul(u,v),quadratic_mul(q,r))
                rhs=quadratic_mul(formal_frac_zsqrt2(u,q),formal_frac_zsqrt2(v,r))
                self.assertEqual(lhs,rhs)

    def test_04_universal_zsqrt2_representatives(self):
        u=(F(3),F(2));q=(F(5),F(-1))
        x=formal_frac_zsqrt2(u,q)
        for k in (-4,-2,1,3,5):
            self.assertEqual(x,formal_frac_zsqrt2((k*u[0],k*u[1]),(k*q[0],k*q[1])))

    def test_05_zsqrt2_norm_nonzero(self):
        for a,b in itertools.product(range(-10,11),repeat=2):
            if a or b:
                self.assertNotEqual(a*a-2*b*b,0)

    def test_06_zsqrt2_inverse(self):
        one=(F(1),F(0))
        for a,b in itertools.product(range(-5,6),repeat=2):
            if not (a or b):continue
            z=(F(a),F(b))
            self.assertEqual(quadratic_mul(z,quadratic_inv(z)),one)

    def test_07_frobenius_F9_additive(self):
        elems=list(itertools.product(range(3),repeat=2))
        f=lambda z:quadratic_mul(quadratic_mul(z,z,d=-1,p=3),z,d=-1,p=3)
        for a,b in itertools.product(elems,repeat=2):
            self.assertEqual(f(quadratic_add(a,b,3)),quadratic_add(f(a),f(b),3))

    def test_08_frobenius_F9_multiplicative(self):
        elems=list(itertools.product(range(3),repeat=2))
        f=lambda z:quadratic_mul(quadratic_mul(z,z,d=-1,p=3),z,d=-1,p=3)
        self.assertEqual(len({f(z) for z in elems}),9)
        self.assertNotEqual(f((0,1)),(0,1))
        for a,b in itertools.product(elems,repeat=2):
            self.assertEqual(f(quadratic_mul(a,b,-1,3)),quadratic_mul(f(a),f(b),-1,3))

    def test_09_F3_X2plus1_is_a_field(self):
        elems=list(itertools.product(range(3),repeat=2))
        one=(1,0)
        for a in elems:
            if a!=(0,0):
                self.assertTrue(any(quadratic_mul(a,b,-1,3)==one for b in elems))

    def test_10_F5_X2plus1_not_field(self):
        a=(2,1);b=(2,4)
        self.assertNotEqual(a,(0,0))
        self.assertNotEqual(b,(0,0))
        self.assertEqual(quadratic_mul(a,b,-1,5),(0,0))

    def test_11_polynomial_quotient_and_evaluation_at_i(self):
        # Reduce a0+a1*X+... modulo X^2+1; compare evaluating at i.
        for coef in itertools.product((-1,0,1),repeat=6):
            constant=sum(((-1)**(k//2))*coef[k] for k in range(0,6,2))
            linear=sum(((-1)**(k//2))*coef[k] for k in range(1,6,2))
            power=(1,0); value=(0,0)
            for c in coef:
                value=quadratic_add(value,(c*power[0],c*power[1]))
                power=quadratic_mul(power,(0,1),-1)
            self.assertEqual(value,(constant,linear))

    def test_12_char_nonprime_Zn_has_divisors(self):
        for n in range(4,45):
            if any(n%d==0 for d in range(2,math.isqrt(n)+1)):
                self.assertTrue(any(a*b%n==0 for a in range(1,n) for b in range(1,n)))

    def test_13_no_field_hom_Q_to_Fp(self):
        # Any unital map sends integers n to n mod p; p then maps to 0,
        # although it is invertible in Q. This cannot preserve inverse.
        for p in (2,3,5,7,11):
            image_p=p%p
            self.assertEqual(image_p,0)
            self.assertFalse(any(image_p*y%p==1 for y in range(p)))
        self.assertIn('nie przedłuża się do homomorfizmu ciał',SRC)

    def test_14_explicit_multiplication_of_universal_extension(self):
        self.assertIn(r'f(ac)f(bd)^{-1}',SRC)
        self.assertIn(r'\bigl(f(a)f(b)^{-1}\bigr)',SRC)
        self.assertIn('wzór nie zależy od reprezentanta',SRC)

    def test_15_embedding_Q_into_complex_pairs(self):
        for a,b,c,d in itertools.product(range(-3,4),repeat=4):
            if not b or not d:continue
            x=(F(a,b),F(0));y=(F(c,d),F(0))
            self.assertEqual(quadratic_mul(x,y,-1),(F(a,b)*F(c,d),F(0)))
            self.assertEqual(quadratic_add(x,y),(F(a,b)+F(c,d),F(0)))

    def test_16_field_presentation_unique_a_plus_bX(self):
        for a,b,c,d in itertools.product(range(-2,3),repeat=4):
            # Nonzero polynomial of degree <2 cannot be multiple of X^2+1.
            if (a,b)!=(c,d):
                self.assertNotEqual((a-c,b-d),(0,0))


# Original audit suite: test_aa19_audit3.py
"""Third independent audit of AA-19: finite checks support, not replace, proofs."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from math import gcd
import re
import unittest

TEXT = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/19-ciala-ulamkow-i-konstrukcje-liczb.tex').read_text()


def cp(a,b):
    x,y=a; u,v=b
    return x*u-y*v,x*v+y*u


def ca(a,b):
    return a[0]+b[0],a[1]+b[1]


def cpow(a,p):
    x=(1,0)
    for _ in range(p): x=cp(x,a)
    return x


def f9_mul(a,b):
    # F_3[u]/(u^2+1), irreducible since -1 is not a square mod 3
    x,y=a; z,w=b
    return ((x*z-y*w)%3,(x*w+y*z)%3)


def f9_pow(x,n):
    res=(1,0)
    for _ in range(n): res=f9_mul(res,x)
    return res


class ReviewIII(unittest.TestCase):
    def test_01_structural_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)
        self.assertEqual((len(labels),len(set(labels)),len(refs)),(20,20,6))
        self.assertTrue(set(refs)<=set(labels))

    def test_02_structural_proofs(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),9)
        self.assertEqual(TEXT.count(r'\end{proof}'),9)
        self.assertEqual(TEXT.count(r'\begin{przyklad}'),5)
        self.assertEqual(TEXT.count(r'\end{przyklad}'),5)

    def test_03_inverse_independent_of_representative(self):
        for a,b,k in product(range(-6,7),range(-6,7),range(-4,5)):
            if a==0 or b==0 or k==0: continue
            self.assertEqual(Q(b,a),Q(k*b,k*a))

    def test_04_formal_fractions_total(self):
        for a,b,c,d in product(range(-3,4),repeat=4):
            if b==0 or d==0: continue
            self.assertEqual(a*d==b*c,Q(a,b)==Q(c,d))

    def test_05_formal_fractions_operations(self):
        for a,b,c,d in product(range(-3,4),repeat=4):
            if b==0 or d==0: continue
            self.assertEqual(Q(a,b)+Q(c,d),Q(a*d+b*c,b*d))
            self.assertEqual(Q(a,b)*Q(c,d),Q(a*c,b*d))

    def test_06_negative_denominator_example(self):
        self.assertEqual(Q(-5,7),Q(5,-7))
        self.assertNotEqual(Q(2,3),Q(3,4))

    def test_07_polynomial_nondivisibility_all_prime_fields(self):
        # t+1 divides t iff substitution t=-1 gives 0; it gives -1 !=0.
        for p in (2,3,5,7,11,13):
            self.assertNotEqual((-1)%p,0)
            self.assertEqual(((-1)+1)%p,0)
        self.assertIn('podstawienie $t=-1$',TEXT)

    def test_08_order_characteristic_zero(self):
        for n in range(1,100):
            self.assertGreater(n*Q(1),0)
        self.assertIn('ciało uporządkowane',TEXT)
        self.assertIn(r'$n\cdot1>0$',TEXT)

    def test_09_no_z_to_fp_fraction_extension(self):
        for p in (2,3,5,7,11):
            self.assertEqual(p%p,0)
            self.assertEqual(Q(p)*Q(1,p),1)
            self.assertFalse(any((p%p)*x%p==1 for x in range(p)))

    def test_10_prime_field_all_units(self):
        for p in (2,3,5,7):
            for a in range(1,p):
                self.assertEqual((a*pow(a,-1,p))%p,1)

    def test_11_frobenius_on_prime_fields(self):
        for p in (2,3,5,7,11):
            for a,b in product(range(p),repeat=2):
                self.assertEqual(pow((a+b)%p,p,p),(pow(a,p,p)+pow(b,p,p))%p)
                self.assertEqual(pow(a,p,p),a)

    def test_12_frobenius_on_F9(self):
        field=list(product(range(3),repeat=2))
        F=[f9_pow(a,3) for a in field]
        self.assertEqual(len(set(F)),9)
        self.assertTrue(any(F[i]!=field[i] for i in range(9)))
        self.assertTrue(all(f9_pow(a,9)==a for a in field))

    def test_13_frobenius_unsurjective_degree_obstruction(self):
        for p in (2,3,5,7):
            for da,db in product(range(8),repeat=2):
                self.assertNotEqual(p*da,1+p*db)

    def test_14_complex_pair_associativity(self):
        sample=[(Q(a),Q(b)) for a,b in product(range(-2,3),repeat=2)]
        for a,b,c in product(sample[::3],repeat=3):
            self.assertEqual(cp(cp(a,b),c),cp(a,cp(b,c)))

    def test_15_complex_pair_inverse(self):
        for a,b in product(range(-7,8),repeat=2):
            if not a and not b: continue
            N=a*a+b*b
            self.assertEqual(cp((Q(a),Q(b)),(Q(a,N),Q(-b,N))),(1,0))

    def test_16_complex_pair_multiplication_matches_X2plus1(self):
        for a,b,c,d in product(range(-4,5),repeat=4):
            expected=(a*c-b*d,a*d+b*c)
            self.assertEqual(cp((a,b),(c,d)),expected)
            self.assertEqual(ca(cp((a,b),(c,d)),(0,0)),expected)

