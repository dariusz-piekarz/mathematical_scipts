"""Independent mathematical and structural regression tests for AA-29.
Run: python -m unittest tools.tests.test_abstract_algebra_ch29 -v
Small finite fields are implemented without a computer-algebra-system black box.
"""
import itertools
import math
import re
import unittest
from pathlib import Path
from sympy import mobius, divisors

SRC = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/29-struktura-cial-skonczonych-i-wielomiany-nierozkladalne.tex'
TEXT = SRC.read_text(encoding='utf-8')

class Field:
    def __init__(self, p, modulus=None):
        self.p=p
        self.modulus=modulus
        self.deg=1 if modulus is None else 2
        self.q=p**self.deg
        if modulus is not None: assert len(modulus)==3 and modulus[-1]==1
        self.invs={a:next(b for b in range(1,self.q) if self.mul(a,b)==1) for a in range(1,self.q)}

    def add(self,a,b):
        if self.deg==1:return (a+b)%self.p
        return ((a%self.p+b%self.p)%self.p) + self.p*((a//self.p+b//self.p)%self.p)

    def neg(self,a):
        if self.deg==1:return (-a)%self.p
        return (-a%self.p)+self.p*((-(a//self.p))%self.p)

    def sub(self,a,b):return self.add(a,self.neg(b))

    def mul(self,a,b):
        p=self.p
        if self.deg==1:return a*b%p
        a0,a1=a%p,a//p
        b0,b1=b%p,b//p
        t=a1*b1
        c0=(a0*b0-t*self.modulus[0])%p
        c1=(a0*b1+a1*b0-t*self.modulus[1])%p
        return c0+p*c1

    def poly_trim(self,a):
        a=list(a)
        while len(a)>1 and a[-1]==0:a.pop()
        return tuple(a)

    def poly_divrem(self,a,b):
        a=list(self.poly_trim(a));b=self.poly_trim(b)
        assert b[-1]
        inv=self.invs[b[-1]]
        while len(a)>=len(b) and a!=[0]:
            coef=self.mul(a[-1],inv)
            shift=len(a)-len(b)
            for j in range(len(b)):
                a[shift+j]=self.sub(a[shift+j],self.mul(coef,b[j]))
            a=list(self.poly_trim(a))
        return tuple(a)

    def poly_mul(self,a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]=self.add(out[i+j],self.mul(x,y))
        return self.poly_trim(out)

    def poly_pow_x_mod(self,exp,f):
        v=(1,);base=self.poly_divrem((0,1),f)
        while exp:
            if exp&1:v=self.poly_divrem(self.poly_mul(v,base),f)
            base=self.poly_divrem(self.poly_mul(base,base),f)
            exp//=2
        return v

    def irreducible(self,f):
        n=len(f)-1
        if n<1 or f[-1]!=1:return False
        for d in range(1,n//2+1):
            for xs in itertools.product(range(self.q),repeat=d):
                g=xs+(1,)
                if self.poly_divrem(f,g)==(0,):return False
        return True

    def irreducibles(self,n):
        for xs in itertools.product(range(self.q),repeat=n):
            f=xs+(1,)
            if self.irreducible(f):yield f

    def count(self,n):return sum(1 for _ in self.irreducibles(n))

F2=Field(2)
F3=Field(3)
F5=Field(5)
F4=Field(2,(1,1,1)) # theta^2+theta+1
F9=Field(3,(1,0,1)) # theta^2+1


def N(q,n):
    return sum(int(mobius(d))*q**(n//d) for d in divisors(n))//n

class StructureTests(unittest.TestCase):
    def test_01_no_duplicate_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),9)

    def test_02_internal_references(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        targets=set(re.findall(r'\\ref\{([^}]+)\}',TEXT))
        self.assertEqual(targets-labels,{'aa:ch:embeddings-normal-separable'})

    def test_03_balanced_environments(self):
        for env in ('twierdzenie','wniosek','definicja','lemat','przyklad','uwaga','proof','section'):
            self.assertEqual(TEXT.count('\\begin{'+env+'}'),TEXT.count('\\end{'+env+'}'))

    def test_04_math_environment_balance(self):
        self.assertEqual(TEXT.count('\\['),TEXT.count('\\]'))
        self.assertEqual(TEXT.count('\\('),TEXT.count('\\)'))

    def test_05_forbidden_spelling(self):
        self.assertNotIn('injektywn',TEXT)

    def test_06_kinds_of_results(self):
        for lbl in ('aa:tw:finite-frobenius-roots','aa:cor:finite-degree-count',
                    'aa:tw:finite-irreducible-count','aa:lem:mobius-sum'):
            self.assertIn('\\label{'+lbl+'}',TEXT)

    def test_07_earlier_edge_cases_explicit(self):
        self.assertIn('Dla $n=1$',TEXT)
        self.assertIn('Dla $n=1$ wystarczy',TEXT)

    def test_08_qth_power_preserves_field(self):
        self.assertIn('$(x^q)^{q^s}=x^q$',TEXT)

class CountingTests(unittest.TestCase):
    def test_09_mobius_sum_to_24(self):
        for n in range(1,25):
            self.assertEqual(sum(int(mobius(d)) for d in divisors(n)),1 if n==1 else 0)

    def test_10_formula_integrality_and_positivity(self):
        for q in (2,3,4,5,7,8,9,16):
            for n in range(1,13):
                v=sum(int(mobius(d))*q**(n//d) for d in divisors(n))
                self.assertEqual(v%n,0)
                self.assertGreater(v,0)

    def test_11_mobius_degree_sum(self):
        for q in (2,3,4,5,7,8,9,16):
            for n in range(1,13):
                self.assertEqual(sum(d*N(q,d) for d in divisors(n)),q**n)

    def test_12_prime_field_2_counts(self):
        for n in range(1,7):self.assertEqual(F2.count(n),N(2,n))

    def test_13_prime_field_3_counts(self):
        for n in range(1,6):self.assertEqual(F3.count(n),N(3,n))

    def test_14_prime_field_5_counts(self):
        for n in range(1,5):self.assertEqual(F5.count(n),N(5,n))

    def test_15_nonprime_field_4_counts(self):
        for n in range(1,5):self.assertEqual(F4.count(n),N(4,n))

    def test_16_nonprime_field_9_counts(self):
        for n in range(1,4):self.assertEqual(F9.count(n),N(9,n))

    def test_17_F2_quadratic(self):
        self.assertEqual(list(F2.irreducibles(2)),[(1,1,1)])

    def test_18_F2_cubics(self):
        self.assertEqual(set(F2.irreducibles(3)),{(1,1,0,1),(1,0,1,1)})

    def test_19_F3_quadratics(self):
        self.assertEqual(set(F3.irreducibles(2)),{(1,0,1),(2,1,1),(2,2,1)})

    def test_20_F4_arithmetic(self):
        self.assertEqual(F4.mul(2,2),3)
        self.assertEqual(F4.mul(2,3),1)
        self.assertEqual(F4.mul(3,3),2)

    def test_21_F9_arithmetic(self):
        self.assertEqual(F9.mul(3,3),2)
        self.assertEqual(F9.mul(3,6),1)

class FactorizationTests(unittest.TestCase):
    def _factorization(self,field,n):
        prod=(1,)
        for d in divisors(n):
            for f in field.irreducibles(d):
                prod=field.poly_mul(prod,f)
        degree=field.q**n
        goal=[0]*(degree+1)
        goal[degree]=1
        goal[1]=field.neg(1)
        self.assertEqual(prod,field.poly_trim(goal))

    def test_22_factor_F2(self):
        for n in (1,2,3,4,5):
            with self.subTest(n=n):self._factorization(F2,n)

    def test_23_factor_F3(self):
        for n in (1,2,3):
            with self.subTest(n=n):self._factorization(F3,n)

    def test_24_factor_F4(self):
        for n in (1,2,3):
            with self.subTest(n=n):self._factorization(F4,n)

    def test_25_factor_F9(self):
        for n in (1,2):
            with self.subTest(n=n):self._factorization(F9,n)

    def test_26_frobenius_period_in_F2(self):
        for degree in range(1,6):
            for f in F2.irreducibles(degree):
                for n in range(1,10):
                    fixed=F2.poly_pow_x_mod(2**n,f)==F2.poly_divrem((0,1),f)
                    self.assertEqual(fixed,n%degree==0,(f,n))

    def test_27_frobenius_period_in_F3(self):
        for degree in range(1,5):
            for f in F3.irreducibles(degree):
                for n in range(1,9):
                    fixed=F3.poly_pow_x_mod(3**n,f)==F3.poly_divrem((0,1),f)
                    self.assertEqual(fixed,n%degree==0,(f,n))

    def test_28_frobenius_period_in_F4(self):
        for degree in range(1,4):
            for f in F4.irreducibles(degree):
                for n in range(1,8):
                    fixed=F4.poly_pow_x_mod(4**n,f)==F4.poly_divrem((0,1),f)
                    self.assertEqual(fixed,n%degree==0,(f,n))

    def test_29_frobenius_period_in_F9(self):
        for degree in range(1,4):
            for f in F9.irreducibles(degree):
                for n in range(1,7):
                    fixed=F9.poly_pow_x_mod(9**n,f)==F9.poly_divrem((0,1),f)
                    self.assertEqual(fixed,n%degree==0,(f,n))

    def test_30_reducible_nonreduced_example(self):
        g=(1,1,1)
        self.assertEqual(F2.poly_mul(g,g),(1,0,1,0,1))
        self.assertFalse(F2.irreducible((1,0,1,0,1)))

if __name__=='__main__':unittest.main(verbosity=2)
