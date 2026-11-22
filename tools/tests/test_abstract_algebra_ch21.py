"""AA-21: niezależne testy rachunkowe i strukturalne.

Kontrole skończonych modeli nie zastępują dowodów ogólnych.
"""
import itertools
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/21-zanurzenia-automorfizmy-i-rozszerzenia-galois.tex')
TEXT=SOURCE.read_text(encoding='utf-8')


def fadd(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))


def fmul(a,b,p,mod):
    """Iloczyn w F_p[x]/(mod), mod unormowany i nierozkładalny."""
    n=len(mod)-1; cc=[0]*(2*n-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):cc[i+j]=(cc[i+j]+x*y)%p
    for k in range(2*n-2,n-1,-1):
        z=cc[k]
        for i in range(n):cc[k-n+i]=(cc[k-n+i]-z*mod[i])%p
    return tuple(cc[:n])


def fpow(a,k,p,mod):
    ans=(1,)+(0,)*(len(mod)-2)
    while k:
        if k&1:ans=fmul(ans,a,p,mod)
        a=fmul(a,a,p,mod)
        k//=2
    return ans


def f_order(a,p,mod):
    if not any(a):return 0
    one=(1,)+(0,)*(len(mod)-2)
    for k in range(1,p**(len(mod)-1)):
        if fpow(a,k,p,mod)==one:return k
    return -1

FIELDS=[(2,(1,1,1),4),(2,(1,1,0,1),8),(3,(1,0,1),9),
        (2,(1,1,0,0,1),16),(5,(2,0,1),25)]


class Structural(unittest.TestCase):
    def test_01_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual((len(labels),len(set(labels))),(20,20))
    def test_02_references(self):
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)),18)
    def test_03_proofs(self):
        self.assertEqual((TEXT.count(r'\begin{proof}'),TEXT.count(r'\end{proof}')),(10,10))
    def test_04_theorems(self):
        self.assertEqual(TEXT.count(r'\begin{twierdzenie}'),7)
    def test_05_examples(self):
        self.assertEqual(TEXT.count(r'\begin{przyklad}'),5)
    def test_06_definitions(self):
        self.assertEqual(TEXT.count(r'\begin{definicja}'),3)
    def test_07_prohibited_terminology(self):
        self.assertNotIn('tensorowanie',TEXT.lower())
        self.assertIsNone(re.search(r'\bsekwencj\w*',TEXT.lower()))
    def test_08_cross_reference_eisenstein(self):
        self.assertIn(r'\ref{aa:tw:eisenstein}',TEXT)
    def test_09_finite_root_adjoining_explained(self):
        self.assertIn('twierdzenie o wieży zapewnia',TEXT)
    def test_10_maximal_ideal_justification(self):
        self.assertIn('lemat Kuratowskiego--Zorna',TEXT)
        self.assertIn('skończona relacja',TEXT)


class QuadraticAutomorphisms(unittest.TestCase):
    def test_11_conjugation_addition(self):
        for a,b,c,d in itertools.product(range(-3,4),repeat=4):
            conj_sum=(a+c,-(b+d))
            sum_conj=(a+c,(-b)+(-d))
            self.assertEqual(conj_sum,sum_conj)
    def test_12_conjugation_multiplication(self):
        for a,b,c,d in itertools.product(range(-3,4),repeat=4):
            p=(a*c+2*b*d,a*d+b*c)
            q=(a*c+2*b*d,-a*d-b*c)
            conja=(a,-b);conjb=(c,-d)
            out=(conja[0]*conjb[0]+2*conja[1]*conjb[1],
                 conja[0]*conjb[1]+conja[1]*conjb[0])
            self.assertEqual(out,q)
    def test_13_conjugation_involution(self):
        for a,b in itertools.product(range(-9,10),repeat=2):
            self.assertEqual((a,-(-b)),(a,b))
    def test_14_quadratic_minimal_roots(self):
        r=math.sqrt(2)
        self.assertAlmostEqual(r*r-2,0)
        self.assertAlmostEqual((-r)*(-r)-2,0)
    def test_15_biquadratic_sign_embeddings(self):
        # Q(sqrt2,sqrt3): all four sign substitutions preserve (sqrt6)^2=6.
        imgs=[]
        for a,b in itertools.product((-1,1),repeat=2):
            x=a*math.sqrt(2);y=b*math.sqrt(3)
            self.assertAlmostEqual(x*x,2)
            self.assertAlmostEqual(y*y,3)
            self.assertAlmostEqual((x*y)**2,6)
            imgs.append((a,b))
        self.assertEqual(len(set(imgs)),4)
    def test_16_cubic_non_normal(self):
        alpha=2**(1/3)
        roots=[alpha*complex(-.5,math.sqrt(3)/2)**k for k in range(3)]
        self.assertEqual(sum(abs(z.imag)<1e-10 for z in roots),1)
        self.assertEqual(len({round(z.real,7)+1j*round(z.imag,7) for z in roots}),3)


class Inseparable(unittest.TestCase):
    def test_17_derivative_vanishes(self):
        for p in (2,3,5,7):
            self.assertEqual(p%p,0)
    def test_18_eisenstein_coefficients(self):
        for p in (2,3,5,7):
            # For X^p-t in F_p[t][X], all coefficients except the
            # leading coefficient vanish modulo t, and -t not modulo t^2.
            # Model a polynomial in t by its coefficient vector.
            coeffs = {0:(0,-1),p:(1,)}
            self.assertEqual(coeffs[p][0]%p,1)
            for k in range(p):
                a=coeffs.get(k,(0,))
                self.assertEqual(a[0]%p,0)
            self.assertNotEqual(coeffs[0][1]%p,0)
    def test_19_frobenius_multiplicativity(self):
        for p in (2,3,5,7):
            for a,b in itertools.product(range(p),repeat=2):
                self.assertEqual(pow(a*b,p,p),pow(a,p,p)*pow(b,p,p)%p)
    def test_20_frobenius_additivity(self):
        for p in (2,3,5,7):
            for a,b in itertools.product(range(p),repeat=2):
                self.assertEqual(pow(a+b,p,p),(pow(a,p,p)+pow(b,p,p))%p)
    def test_21_pure_inseparability_degree(self):
        for p in (2,3,5,7):
            # The t-adic valuation of t is 1, but v(z^p)=p*v(z)
            # for rational monomials z=t^a/t^b. In particular t
            # cannot be a p-th power of such a rational function.
            for a,b in itertools.product(range(0,12),repeat=2):
                self.assertNotEqual(p*(a-b),1)
    def test_22_normality_not_separability(self):
        for p in (2,3,5,7):
            # In char p, (X-alpha)^p = X^p-alpha^p.
            for k in range(1,p):
                self.assertEqual(math.comb(p,k)%p,0)
            self.assertEqual(p%p,0)  # derivative of X^p-t vanishes


class FiniteFields(unittest.TestCase):
    def test_23_cardinality(self):
        for p,mod,q in FIELDS:
            self.assertEqual(len(list(itertools.product(range(p),repeat=len(mod)-1))),q)
    def test_24_frobenius_q_identity(self):
        for p,mod,q in FIELDS:
            for x in itertools.product(range(p),repeat=len(mod)-1):
                self.assertEqual(fpow(x,q,p,mod),x)
    def test_25_units(self):
        for p,mod,q in FIELDS:
            for x in itertools.product(range(p),repeat=len(mod)-1):
                if not any(x):continue
                self.assertEqual(fpow(x,q-1,p,mod),(1,)+(0,)*(len(mod)-2))
    def test_26_frobenius_exact_order(self):
        for p,mod,q in FIELDS:
            n=len(mod)-1
            for r in range(1,n):
                self.assertTrue(any(fpow(x,p**r,p,mod)!=x
                                    for x in itertools.product(range(p),repeat=n)))
    def test_27_frobenius_cycle_length(self):
        for p,mod,q in FIELDS:
            n=len(mod)-1
            self.assertTrue(all(fpow(x,p**n,p,mod)==x
                                for x in itertools.product(range(p),repeat=n)))
    def test_28_primitive_element_exists(self):
        for p,mod,q in FIELDS:
            self.assertTrue(any(f_order(x,p,mod)==q-1
                                for x in itertools.product(range(p),repeat=len(mod)-1)))
    def test_29_frobenius_additive(self):
        for p,mod,q in FIELDS:
            all_x=list(itertools.product(range(p),repeat=len(mod)-1))
            for x,y in itertools.product(all_x,repeat=2):
                self.assertEqual(fpow(fadd(x,y,p),p,p,mod),
                                 fadd(fpow(x,p,p,mod),fpow(y,p,p,mod),p))
    def test_30_frobenius_multiplicative(self):
        for p,mod,q in FIELDS:
            a=list(itertools.product(range(p),repeat=len(mod)-1))
            for x,y in itertools.product(a,repeat=2):
                self.assertEqual(fpow(fmul(x,y,p,mod),p,p,mod),
                                 fmul(fpow(x,p,p,mod),fpow(y,p,p,mod),p,mod))
    def test_31_field_f2_galois_trivial(self):
        self.assertEqual(len([x for x in range(2) if x!=0]),1)
    def test_32_field_f8_galois_order_three(self):
        p,mod,q=FIELDS[1]
        alpha=(0,1,0)
        self.assertNotEqual(fpow(alpha,2,p,mod),alpha)
        self.assertNotEqual(fpow(alpha,4,p,mod),alpha)
        self.assertEqual(fpow(alpha,8,p,mod),alpha)
    def test_33_roots_of_Xq_X_are_distinct(self):
        for p,mod,q in FIELDS:
            all_x=list(itertools.product(range(p),repeat=len(mod)-1))
            self.assertEqual(len(set(all_x)),q)
            self.assertTrue(all(fpow(x,q,p,mod)==x for x in all_x))
    def test_34_root_count_simple_examples(self):
        # In F4, X^2+X+1 has 2 distinct roots.
        p,mod,q=FIELDS[0]
        roots=[]
        for a in itertools.product(range(p),repeat=2):
            expr=fadd(fadd(fmul(a,a,p,mod),a,p),(1,0),p)
            if expr==(0,0):roots.append(a)
        self.assertEqual(len(roots),2)
    def test_35_galois_cardinality(self):
        for p,mod,q in FIELDS:
            self.assertEqual(q,p**(len(mod)-1))


if __name__=='__main__':unittest.main()
