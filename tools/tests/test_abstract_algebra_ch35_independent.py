"""Independent AA-35 tests: elementary F_p polynomial arithmetic, Frobenius and citations.
Usage in repository: python -m unittest tools.tests.test_abstract_algebra_ch35_independent -v
"""
import re
import math
import unittest
from pathlib import Path
from itertools import product
import sympy as sp

X=sp.Symbol('X')
ROOT=Path(__file__).resolve().parents[2]
CHAPTER=ROOT/'chapters/pl/abstract_algebra/35-redukcja-modulo-p-i-cykle-frobeniusa.tex'
if not CHAPTER.is_file():
    CHAPTER=Path(__file__).resolve().parent/'AA-35-audyt-II-zrodlo.tex'
F={
 's3':X**3-X-1,
 'c3':X**3-3*X+1,
 's4':X**4-X-1,
 'd4':X**4-2,
 'v4':X**4-10*X**2+1,
 'red':(X**2-2)*(X-3),
 'quad':X**2-5,
 'sep':X**3+2*X+1,
}
PRIMES=[2,3,5,7,11,13,17,23]

def normalize(a,p):
    c=[x%p for x in a]
    while c and c[-1]==0:c.pop()
    return c

def divide(a,b,p):
    a=normalize(a,p);b=normalize(b,p)
    if not b:raise ZeroDivisionError
    out=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b);q=a[-1]*pow(b[-1],-1,p)%p;out[k]=q
        for j,z in enumerate(b):a[k+j]=(a[k+j]-q*z)%p
        a=normalize(a,p)
    return normalize(out,p),a

def monic_gcd(a,b,p):
    a=normalize(a,p);b=normalize(b,p)
    while b:_,r=divide(a,b,p);a,b=b,r
    return [(x*pow(a[-1],-1,p))%p for x in a] if a else []

def derivative(a,p):return normalize([(i*a[i])%p for i in range(1,len(a))],p)

def irreducible_factor_degrees(f,p):
    a=normalize([int(c) for c in reversed(sp.Poly(f,X,domain=sp.ZZ).all_coeffs())],p)
    ans=[]
    while len(a)>1:
        d=len(a)-1;factor=None
        for k in range(1,d//2+1):
            for c in product(range(p),repeat=k):
                b=list(c)+[1];q,r=divide(a,b,p)
                if not r:factor=(b,q);break
            if factor:break
        if factor:
            a=factor[1]
            # recursively subdivide selected factor so only irreducibles are recorded
            part=irreducible_factor_degrees_from_list(factor[0],p)
            ans.extend(part)
        else:ans.append(d);break
    return tuple(sorted(ans))

def irreducible_factor_degrees_from_list(a,p):
    a=normalize(a,p)
    if len(a)<=1:return ()
    for d in range(1,(len(a)-1)//2+1):
        for c in product(range(p),repeat=d):
            b=list(c)+[1];q,r=divide(a,b,p)
            if not r:return irreducible_factor_degrees_from_list(b,p)+irreducible_factor_degrees_from_list(q,p)
    return (len(a)-1,)

def power_mod(a,n,mod,p):
    def mul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
        return divide(out,mod,p)[1]
    v=[1]
    while n:
        if n&1:v=mul(v,a)
        a=mul(a,a);n//=2
    return normalize(v,p)

class CitationAndStructure(unittest.TestCase):
    def test_readable_source(self):self.assertTrue(CHAPTER.is_file())
    def test_unique_labels(self):
        s=CHAPTER.read_text(encoding='utf-8');ls=re.findall(r'\\label\{([^}]+)\}',s)
        self.assertEqual(len(ls),len(set(ls)))
        self.assertEqual(len(ls),12)
    def test_every_local_ref_exists(self):
        s=CHAPTER.read_text(encoding='utf-8');ls=set(re.findall(r'\\label\{([^}]+)\}',s))
        ext={'aa:tw:fundamental-symmetric','aa:tw:disc-separable','aa:tw:finite-frobenius-roots','aa:tw:disc-alternating','aa:tw:cubic-disc'}
        self.assertFalse(set(re.findall(r'\\ref\{([^}]+)\}',s))-ls-ext)
    def test_nondegenerate_lemma(self):
        s=CHAPTER.read_text(encoding='utf-8')
        self.assertIn('B^G=\\mathbb Z',s)
        self.assertIn('\\prod_{\\sigma\\in G}',s)
        self.assertIn('\\sigma(\\mathfrak p)=\\mathfrak p',s)
    def test_no_division_or_polynomial_degree_blindness(self):
        s=CHAPTER.read_text(encoding='utf-8')
        self.assertIn('stopień pochodnej może bowiem się zmniejszyć',s)
        self.assertIn('\\operatorname{disc}(\\bar f)',s)

class PolynomialArithmetic(unittest.TestCase):
    pass

def arithmetic_test(label,p):
    f=F[label]
    def run(self):
        z=sp.Poly(f,X,domain=sp.ZZ)
        c=[int(i) for i in reversed(z.all_coeffs())]
        lhs=(int(sp.discriminant(f,X))%p!=0)
        rhs=len(monic_gcd(c,derivative(c,p),p))==1
        self.assertEqual(lhs,rhs,(label,p,'squarefreeness'))
        factor=irreducible_factor_degrees(f,p)
        self.assertEqual(sum(factor),z.degree())
        _,spfac=sp.factor_list(sp.Poly(f,X,modulus=p))
        expected=sorted([h.degree() for h,m in spfac for _ in range(m)])
        self.assertEqual(list(factor),expected,(label,p,'independent factorization'))
        if lhs:
            self.assertEqual(sum(d-1 for d in factor)%2,(z.degree()-len(factor))%2)
            disc=int(sp.discriminant(f,X))
            if disc>0 and math.isqrt(disc)**2==disc:
                self.assertEqual((z.degree()-len(factor))%2,0,(label,p,'alternating group'))
    return run

for label in F:
    for p in PRIMES:
        setattr(PolynomialArithmetic,f'test_independent_{label}_{p:02d}',arithmetic_test(label,p))

class DelicateCases(unittest.TestCase):
    def test_characteristic2_zero_derivative(self):
        f=[1,0,1,0,1]
        self.assertEqual(derivative(f,2),[])
        self.assertGreater(len(monic_gcd(f,derivative(f,2),2)),1)
    def test_characteristic3_derivative_degree_loss(self):
        f=[1,2,0,1]
        self.assertEqual(derivative(f,3),[2])
        self.assertEqual(monic_gcd(f,derivative(f,3),3),[1])
    def test_explicit_prime_23_bad_factorization(self):
        self.assertEqual(irreducible_factor_degrees(F['s3'],23),(1,1,1))
        self.assertEqual(len(monic_gcd([22,22,0,1],derivative([22,22,0,1],23),23)),2)
    def test_prime_59_full_split(self):
        self.assertEqual(irreducible_factor_degrees(F['s3'],59),(1,1,1))
        self.assertEqual([i for i in range(59) if (i*i*i-i-1)%59==0],[4,13,42])
    def test_cubic_sign_and_galois(self):
        self.assertEqual(irreducible_factor_degrees(F['s3'],2),(3,))
        self.assertEqual(irreducible_factor_degrees(F['s3'],5),(1,2))
    def test_reducible_frobenius(self):
        self.assertEqual(int(sp.discriminant(F['red'],X)),392)
        self.assertEqual(irreducible_factor_degrees(F['red'],5),(1,2))
    def test_galois_no_transitivity_needed(self):
        self.assertFalse(sp.Poly(F['red'],X).is_irreducible)
        self.assertEqual(sp.Poly(F['red'],X).degree(),3)
    def test_finite_module_dedekind_2(self):
        self.assertEqual(sorted([i for i in range(2) if (i**3-i-1)%2==0]),[])
    def test_powers_of_frobenius_degree_three(self):
        p=2;mod=[1,1,0,1];x=[0,1]
        self.assertNotEqual(power_mod(x,2,mod,p),x)
        self.assertNotEqual(power_mod(x,4,mod,p),x)
        self.assertEqual(power_mod(x,8,mod,p),x)
    def test_powers_of_frobenius_degree_two(self):
        p=5;mod=[3,2,1];x=[0,1]
        self.assertNotEqual(power_mod(x,5,mod,p),x)
        self.assertEqual(power_mod(x,25,mod,p),x)
    def test_nontrivial_frobenius_even_with_splitting_elsewhere(self):
        self.assertEqual(irreducible_factor_degrees(F['s3'],59),(1,1,1))
        self.assertEqual(irreducible_factor_degrees(F['s3'],5),(1,2))
    def test_good_prime_discriminant(self):
        self.assertEqual(int(sp.discriminant(F['s3'],X)),-23)
        self.assertEqual(int(sp.discriminant(F['s4'],X)),-283)
    def test_quadratic_bad_prime_two(self):
        self.assertEqual(irreducible_factor_degrees(F['quad'],2),(1,1))
        self.assertEqual(int(sp.discriminant(F['quad'],X))%2,0)

if __name__=='__main__':unittest.main()
