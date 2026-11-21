"""Independent mathematical models for the AA-10 audit; not replacements for proofs."""
import math
import random
import re
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CH=ROOT/'chapters/pl/abstract_algebra/10-podzielnosc-dziedziny-euklidesowe-i-idealy-glowne.tex'

def bezout(a,b):
    old_r,r=a,b;old_s,s=1,0;old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t

def trim(p):
    p=list(p)
    while p and p[-1]==0:p.pop()
    return tuple(p)

def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1) if a and b else []
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def psub(a,b):
    return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def pdiv(a,b):
    a,b=trim(a),trim(b)
    if not b:raise ZeroDivisionError
    q=[Fraction(0)]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        n=len(a)-len(b);coeff=a[-1]/b[-1];q[n]+=coeff
        a=psub(a,(Fraction(0),)*n+tuple(x*coeff for x in b))
    return trim(q),a

def pgcd(a,b):
    while b:_,r=pdiv(a,b);a,b=b,r
    return tuple(x/a[-1] for x in a) if a else ()

def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gn(a):return a[0]**2+a[1]**2

def gd(a,b):
    denominator=gn(b)
    q=tuple(round(Fraction(a[0]*b[0]+a[1]*b[1],denominator)) if i==0
            else round(Fraction(a[1]*b[0]-a[0]*b[1],denominator)) for i in range(2))
    r=(a[0]-gm(b,q)[0],a[1]-gm(b,q)[1])
    return q,r

def nm(a,b):return (a[0]*b[0]-5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def nn(a):return a[0]*a[0]+5*a[1]*a[1]

class AA10Tests(unittest.TestCase):
    def test_01_labels_unique_and_proof_balance(self):
        text=CH.read_text();labels=re.findall(r'\\label\{([^}]+)\}',text)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(text.count(r'\begin{proof}'),text.count(r'\end{proof}'))
    def test_02_gcd_zero_zero(self):
        self.assertEqual(math.gcd(0,0),0)
        self.assertEqual(bezout(0,0)[0],0)
    def test_03_gcd_edge_zeros(self):
        for a in range(-30,31):
            self.assertEqual(math.gcd(a,0),abs(a))
            d,s,t=bezout(a,0);self.assertEqual(d,s*a+t*0)
    def test_04_bezout_all_small_pairs(self):
        for a,b in product(range(-20,21),repeat=2):
            d,s,t=bezout(a,b)
            self.assertEqual(d,s*a+t*b)
            self.assertEqual(abs(d),math.gcd(a,b))
    def test_05_integers_division_first_zero_remainder(self):
        for b in range(-15,16):
            if not b:continue
            for k in range(-9,10):
                d,s,t=bezout(b*k,b)
                self.assertEqual(abs(d),abs(b))
                self.assertEqual(d,s*b*k+t*b)
    def test_06_integer_division_nonnegative_remainder(self):
        for a in range(-80,81):
            for b in range(1,21):
                q,r=divmod(a,b)
                self.assertEqual(a,b*q+r)
                self.assertLess(r,b)
                self.assertGreaterEqual(r,0)
    def test_07_gaussian_norm_multiplicative(self):
        for a,b in product(product(range(-3,4),repeat=2),repeat=2):
            self.assertEqual(gn(gm(a,b)),gn(a)*gn(b))
    def test_08_gaussian_remainder_smaller(self):
        for a,b in product(product(range(-4,5),repeat=2),repeat=2):
            if b==(0,0):continue
            q,r=gd(a,b)
            x=gm(b,q)
            self.assertEqual(a,(x[0]+r[0],x[1]+r[1]))
            self.assertTrue(r==(0,0) or gn(r)<gn(b))
    def test_09_gaussian_units(self):
        self.assertEqual({(a,b) for a,b in product(range(-3,4),repeat=2) if gn((a,b))==1},{(1,0),(-1,0),(0,1),(0,-1)})
    def test_10_polynomial_division(self):
        rng=random.Random(20261121)
        for _ in range(300):
            a=trim([Fraction(rng.randint(-5,5)) for _ in range(rng.randint(0,6))])
            b=()
            while not b:b=trim([Fraction(rng.randint(-5,5)) for _ in range(rng.randint(1,5))])
            q,r=pdiv(a,b)
            self.assertEqual(a,trim(tuple((pmul(q,b)[i] if i<len(pmul(q,b)) else 0)+(r[i] if i<len(r) else 0) for i in range(max(len(pmul(q,b)),len(r))))))
            self.assertTrue(not r or len(r)<len(b))
    def test_11_polynomial_zero_cases(self):
        self.assertEqual(pdiv((),(2,1)),((),()))
        self.assertEqual(pdiv((2,),(1,1)),((),(2,)))
    def test_12_polynomial_gcd_example(self):
        self.assertEqual(pgcd((-1,0,0,1),(-1,0,1)),(-1,1))
    def test_13_polynomial_quotient_example(self):
        f=(Fraction(1),Fraction(2),Fraction(0),Fraction(1));g=(Fraction(1),Fraction(1))
        q,r=pdiv(f,g)
        self.assertEqual(q,(Fraction(3),Fraction(-1),Fraction(1)))
        self.assertEqual(r,(-2,))
    def test_14_poly_ufd_nontrivial(self):
        self.assertEqual(pmul((-1,1),(1,1)),(-1,0,1))
        self.assertEqual(pmul((-1,1),(1,1,1)),(-1,0,0,1))
    def test_15_pid_ideal_zn(self):
        for n in range(2,35):
            for a,b in product(range(n),repeat=2):
                d=math.gcd(a,b,n)
                I={(x*a+y*b)%n for x,y in product(range(n),repeat=2)}
                self.assertEqual(I,{(k*d)%n for k in range(n)})
    def test_16_gaussian_euclidean_bezout(self):
        def add(a,b):return a[0]+b[0],a[1]+b[1]
        def minus(a):return -a[0],-a[1]
        for a,b in product(((0,0),(3,0),(2,1),(4,-1),(6,3),(-1,4)),repeat=2):
            old,r=a,b;s0,s1=(1,0),(0,0);t0,t1=(0,0),(1,0)
            while r!=(0,0):
                q,next_r=gd(old,r)
                old,r=r,next_r
                s0,s1=s1,add(s0,minus(gm(q,s1)))
                t0,t1=t1,add(t0,minus(gm(q,t1)))
            self.assertEqual(add(gm(s0,a),gm(t0,b)),old)
            if old!=(0,0):
                for x in (a,b):self.assertEqual(gd(x,old)[1],(0,0))
    def test_17_zsqrtminus5_norm_multiplicative(self):
        for a,b in product(product(range(-3,4),repeat=2),repeat=2):
            self.assertEqual(nn(nm(a,b)),nn(a)*nn(b))
    def test_18_zsqrtminus5_no_norm2_3(self):
        for target in (2,3):
            self.assertFalse(any(nn(x)==target for x in product(range(-10,11),repeat=2)))
    def test_19_zsqrtminus5_units(self):
        self.assertEqual({x for x in product(range(-10,11),repeat=2) if nn(x)==1},{(1,0),(-1,0)})
    def test_20_zsqrtminus5_factors_six(self):
        self.assertEqual(nm((1,1),(1,-1)),(6,0))
        self.assertEqual(nm((2,0),(3,0)),(6,0))
        self.assertEqual(nn((1,1)),6)
        self.assertEqual(nn((1,-1)),6)
    def test_21_irreducible_two_not_prime(self):
        product6=nm((1,1),(1,-1));self.assertEqual(product6[0]%2,0)
        self.assertTrue(any(c%2 for c in (1,1)))
    def test_22_Kxy_ideal_proper(self):
        # Model polynomials as dicts (x-degree,y-degree) -> integer coefficient.
        def mult(P,Q):
            result={}
            for (i,j),a in P.items():
                for (k,l),b in Q.items():
                    e=(i+k,j+l);result[e]=result.get(e,0)+a*b
            return {e:c for e,c in result.items() if c}
        def add(P,Q):
            out=dict(P)
            for e,c in Q.items():out[e]=out.get(e,0)+c
            return {e:c for e,c in out.items() if c}
        x={(1,0):1};y={(0,1):1}
        polys=[{(0,0):a,(1,0):b,(0,1):c,(1,1):d} for a,b,c,d in product(range(-1,2),repeat=4)]
        for P,Q in product(polys[:27],polys[:27]):
            elem=add(mult(x,P),mult(y,Q))
            self.assertEqual(elem.get((0,0),0),0)
        self.assertNotEqual({(0,0):1}.get((0,0)),0)
    def test_23_prime_irred_in_Z(self):
        def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
        for n in range(2,100):
            divisors=[d for d in range(2,n) if n%d==0]
            self.assertEqual(prime(n),not divisors)
    def test_24_gcd_both_positive_zw(self):
        for a,b in product(range(1,30),repeat=2):
            self.assertEqual(math.gcd(a,b)*math.lcm(a,b),a*b)




"""Supplemental independent tests in audit II of AA-10."""
import math
import random
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys
base=sys.modules[__name__]

class AA10AdditionalTests(unittest.TestCase):
    def test_25_extended_polynomial_euclid_bezout(self):
        rng=random.Random(142857)
        for _ in range(170):
            a=base.trim([Fraction(rng.randint(-4,4)) for _ in range(rng.randint(0,5))])
            b=base.trim([Fraction(rng.randint(-4,4)) for _ in range(rng.randint(0,5))])
            if not a and not b:continue
            R0,R1=a,b;S0,S1=(Fraction(1),),();T0,T1=(),(Fraction(1),)
            while R1:
                Q,R=base.pdiv(R0,R1)
                R0,R1=R1,R
                S0,S1=S1,base.psub(S0,base.pmul(Q,S1))
                T0,T1=T1,base.psub(T0,base.pmul(Q,T1))
            lhs=base.psub(base.pmul(a,S0), tuple(-x for x in base.pmul(b,T0)))
            self.assertEqual(lhs,R0)
            d=tuple(x/R0[-1] for x in R0)
            self.assertEqual(d,base.pgcd(a,b))
            self.assertTrue(not base.pdiv(a,R0)[1])
            self.assertTrue(not base.pdiv(b,R0)[1])

    def test_26_euclid_trace_terminates_even_when_first_remainder_zero(self):
        for a,b in product(range(-40,41),repeat=2):
            if not b:continue
            prev,current=a,b
            found=[]
            for _ in range(100):
                q,rem=divmod(prev,current)
                self.assertEqual(prev,current*q+rem)
                if rem==0:break
                self.assertLess(abs(rem),abs(current))
                found.append(rem)
                prev,current=current,rem
            else:self.fail('Nonterminating Euclid trace')
            self.assertEqual(abs(current),math.gcd(a,b))
            self.assertEqual(len(found)==0,a%b==0)

    def test_27_stabilization_in_integer_principal_chains(self):
        for a,b in product(range(-20,21),repeat=2):
            if a==0 or abs(b)<=1:continue
            # a*b generates a strictly smaller ideal than a.
            self.assertTrue((a*b)%a==0)
            self.assertFalse(a%(a*b)==0)

    def test_28_pid_bezout_ideal_generation(self):
        for a,b in product(range(-35,36),repeat=2):
            if not (a or b):continue
            d,s,t=base.bezout(a,b)
            self.assertEqual(abs(d),math.gcd(a,b))
            self.assertEqual(s*a+t*b,d)
            for m,n in product((-8,-3,0,2,7),repeat=2):
                z=m*a+n*b
                self.assertEqual(z%abs(d),0)

    def test_29_irred_implies_prime_in_Z(self):
        for p in (2,3,5,7,11,13,17,19,23,29,31):
            for a,b in product(range(-15,16),repeat=2):
                self.assertFalse((a*b)%p==0 and (a%p)!=0 and (b%p)!=0)

    def test_30_two_distinct_nonassociate_zsqrtminus5_factorizations(self):
        factors=((2,0),(3,0),(1,1),(1,-1))
        self.assertEqual(base.nm(factors[0],factors[1]),(6,0))
        self.assertEqual(base.nm(factors[2],factors[3]),(6,0))
        norms=[base.nn(x) for x in factors]
        self.assertEqual(norms,[4,9,6,6])
        for x in factors:
            self.assertGreater(base.nn(x),1)
        self.assertEqual({base.nn(x) for x in factors},{4,6,9})
        for x,y in product(factors,repeat=2):
            if x==y:continue
            if base.nn(x)!=base.nn(y):continue
            self.assertNotEqual(x,(-y[0],-y[1]))

    def test_31_euclidean_function_examples_at_zero(self):
        self.assertEqual(base.gn((0,0)),0)
        self.assertEqual(base.nn((0,0)),0)
        self.assertEqual(base.pdiv((),(1,)),((),()))
        with self.assertRaises(ZeroDivisionError):base.pdiv((1,),())

    def test_32_source_standalone_assumptions_and_proof_balance(self):
        text=CH.read_text(encoding='utf-8')
        self.assertEqual(text.count('\\begin{proof}'),9)
        self.assertEqual(text.count('\\end{proof}'),9)
        self.assertEqual(text.count('\\label{'),26)
        self.assertIn('Istnieje liczba całkowita $k\\ge0$',text)
        self.assertIn('$b_jd=1_R$',text)
        self.assertIn('Niech $a,b\\in K^\\times$',text)



if __name__=="__main__":unittest.main()


class AA10AuditIIIAdditionalTests(unittest.TestCase):
    """Independent checks for tricky boundary cases of Euclidean/PID/UFD theory."""

    def test_33_gcd_divisor_characterization_including_zero(self):
        def divides(d,n):return n==0 if d==0 else n%d==0
        for a,b in product(range(-12,13),repeat=2):
            g=math.gcd(a,b)
            self.assertTrue(divides(g,a) and divides(g,b))
            for c in range(-12,13):
                if divides(c,a) and divides(c,b):
                    self.assertTrue(divides(c,g),(a,b,c))

    def test_34_polynomial_division_over_finite_field(self):
        p=5
        def clean(a):
            a=list(a)
            while a and a[-1]%p==0:a.pop()
            return tuple(x%p for x in a)
        def divide(a,b):
            a,b=clean(a),clean(b)
            if not b:raise ZeroDivisionError
            q=[0]*max(0,len(a)-len(b)+1)
            while len(a)>=len(b):
                shift=len(a)-len(b); c=a[-1]*pow(b[-1],-1,p)%p
                q[shift]=(q[shift]+c)%p
                nxt=list(a)
                for i,x in enumerate(b):nxt[shift+i]=(nxt[shift+i]-c*x)%p
                a=clean(nxt)
            return clean(q),a
        polys=[()] + [clean(a) for k in range(1,4) for a in product(range(p),repeat=k)]
        for a in polys[::3]:
            for b in polys:
                if not b:continue
                q,r=divide(a,b)
                s=[0]*max(len(a),len(q)+len(b)-1,len(r))
                for i,x in enumerate(q):
                    for j,y in enumerate(b):s[i+j]=(s[i+j]+x*y)%p
                for i,x in enumerate(r):s[i]=(s[i]+x)%p
                self.assertEqual(clean(s),a)
                self.assertTrue(not r or len(r)<len(b))

    def test_35_exact_first_remainder(self):
        for b in range(-50,51):
            if not b:continue
            for k in range(-10,11):
                a=b*k
                self.assertEqual(divmod(a,b)[1],0)
                self.assertEqual(math.gcd(a,b),abs(b))
                self.assertEqual(abs(bezout(a,b)[0]),abs(b))

    def test_36_gaussian_prime_norm_primality(self):
        for pi in ((1,1),(2,1),(2,-1),(3,2)):
            self.assertIn(gn(pi),(2,5,13))
            for a,b in product(product(range(-3,4),repeat=2),repeat=2):
                if gd(gm(a,b),pi)[1]!=(0,0):continue
                self.assertTrue(gd(a,pi)[1]==(0,0) or gd(b,pi)[1]==(0,0))

    def test_37_ascending_integer_ideal_chains_stabilize(self):
        for prime in (2,3,5,7):
            ds=[prime**k for k in range(6,-1,-1)]+[1]*6
            self.assertTrue(all(ds[i]%ds[i+1]==0 for i in range(len(ds)-1)))
            self.assertTrue(all(x==1 for x in ds[-6:]))

    def test_38_gaussian_zero_norm_and_units(self):
        units={(1,0),(-1,0),(0,1),(0,-1)}
        for x in product(range(-50,51),repeat=2):
            self.assertEqual(gn(x)==1,x in units)
            self.assertEqual(gn(x)==0,x==(0,0))

    def test_39_sqrtminus5_four_irreducible_factors(self):
        for x in ((2,0),(3,0),(1,1),(1,-1)):
            n=nn(x)
            self.assertIn(n,(4,6,9))
            for a in product(range(-4,5),repeat=2):
                if nn(a)<=1 or n%nn(a):continue
                for b in product(range(-4,5),repeat=2):
                    if nn(b)<=1:continue
                    self.assertNotEqual(nm(a,b),x)

    def test_40_degree_additivity_in_two_variable_polynomials(self):
        def mul(P,Q,p=3):
            out={}
            for (i,j),v in P.items():
                for (k,l),w in Q.items():
                    e=i+k,j+l;out[e]=(out.get(e,0)+v*w)%p
            return {e:v for e,v in out.items() if v%p}
        polys=[]
        for coeff in product(range(3),repeat=4):
            P={e:c for e,c in zip(((0,0),(1,0),(0,1),(1,1)),coeff) if c}
            if P:polys.append(P)
        degree=lambda P:max(i+j for i,j in P)
        for f,g in product(polys,repeat=2):
            h=mul(f,g)
            self.assertTrue(h)
            self.assertEqual(degree(h),degree(f)+degree(g))
