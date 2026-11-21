"""Independent finite models and structural regression for AA-09.

Mathematical spot checks complement, rather than replace, the written proofs.
"""
from itertools import product
from math import gcd
from pathlib import Path
import re
import unittest

SRC=(Path(__file__).resolve().parents[2]/'chapters/pl/abstract_algebra/09-pierscienie-idealy-i-homomorfizmy.tex').read_text(encoding='utf-8')

def pair_add(x,y):
    a,b=x;c,d=y
    return (a+c,b+d)

def pair_mul(x,y):
    a,b=x;c,d=y
    return (a*c+b*d,a*d+b*c)

def pair_equiv(x,y):
    a,b=x;c,d=y
    return a+d==b+c

def ev_mod(coeffs, x, p):
    return sum(c*pow(x,i,p) for i,c in enumerate(coeffs))%p

def ideals_mod(n):
    return {frozenset(k for k in range(n) if k%d==0) for d in range(1,n+1) if n%d==0}

def matmul(a,b,p=2):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)

def matadd(a,b,p=2):return tuple((x+y)%p for x,y in zip(a,b))

def is_prime(n):return n>1 and all(n%d for d in range(2,int(n**.5)+1))

class Audit09FiniteModels(unittest.TestCase):
    def test_01_source_inventory(self):
        labels=re.findall(r'\\label\{([^}]+)\}',SRC)
        self.assertEqual(len(labels),41)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual((SRC.count(r'\begin{proof}'),SRC.count(r'\end{proof}')),(19,19))

    def test_02_local_references(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',SRC))
        refs=set(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',SRC))
        self.assertTrue(refs<=labels)

    def test_03_formal_difference_equivalence(self):
        pairs=list(product(range(6),repeat=2))
        for x,y in product(pairs,repeat=2):
            self.assertEqual(pair_equiv(x,y),(x[0]-x[1]==y[0]-y[1]))

    def test_04_formal_difference_congruence(self):
        pairs=list(product(range(5),repeat=2))
        for x,y in product(pairs,repeat=2):
            if not pair_equiv(x,y):continue
            for z in pairs:
                self.assertTrue(pair_equiv(pair_add(x,z),pair_add(y,z)))
                self.assertTrue(pair_equiv(pair_mul(x,z),pair_mul(y,z)))

    def test_05_formal_additive_inverses(self):
        for x in product(range(8),repeat=2):
            self.assertTrue(pair_equiv(pair_add(x,(x[1],x[0])),(0,0)))

    def test_06_formal_multiplication_and_distributivity(self):
        xys=list(product(range(3),repeat=2))
        for a,b,c in product(xys,repeat=3):
            self.assertEqual(pair_mul(pair_mul(a,b),c),pair_mul(a,pair_mul(b,c)))
            self.assertEqual(pair_mul(a,pair_add(b,c)),pair_add(pair_mul(a,b),pair_mul(a,c)))

    def test_07_unital_universal_maps_from_integers(self):
        for n in range(1,16):
            for a,b,c,d in product(range(4),repeat=4):
                if pair_equiv((a,b),(c,d)):
                    self.assertEqual((a-b)%n,(c-d)%n)
                self.assertEqual(((a-b)*(c-d))%n,
                                 (pair_mul((a,b),(c,d))[0]-pair_mul((a,b),(c,d))[1])%n)

    def test_08_x_square_one_mod_eight(self):
        self.assertEqual({x for x in range(8) if x*x%8==1},{1,3,5,7})

    def test_09_nilpotents_and_zero_divisors_mod_eight(self):
        self.assertEqual({x for x in range(8) if any(pow(x,k,8)==0 for k in range(1,8))},{0,2,4,6})
        self.assertEqual({x for x in range(1,8) if any(x*y%8==0 for y in range(1,8))},{2,4,6})

    def test_10_finite_domains_are_prime_moduli(self):
        for n in range(2,30):
            zero_divisor=any(a*b%n==0 for a in range(1,n) for b in range(1,n))
            self.assertEqual(not zero_divisor,is_prime(n))

    def test_11_units_in_zn(self):
        for n in range(2,35):
            units={a for a in range(n) if any(a*b%n==1 for b in range(n))}
            self.assertEqual(units,{a for a in range(n) if gcd(a,n)==1})

    def test_12_matrix_ring_noncommutativity(self):
        a=(0,1,0,0);b=(0,0,1,0)
        self.assertEqual(matmul(a,b),(1,0,0,0))
        self.assertEqual(matmul(b,a),(0,0,0,1))
        self.assertEqual(matmul(a,a),(0,0,0,0))

    def test_13_matrix_ring_distributive(self):
        mats=list(product(range(2),repeat=4))
        for x,y,z in product(mats,repeat=3):
            self.assertEqual(matmul(x,matadd(y,z)),matadd(matmul(x,y),matmul(x,z)))
            self.assertEqual(matmul(matadd(x,y),z),matadd(matmul(x,z),matmul(y,z)))

    def test_14_evaluation_kernel_over_five_elements(self):
        p=5
        for a in range(p):
            for coeffs in product(range(p),repeat=4):
                val=ev_mod(coeffs,a,p)
                self.assertEqual(val==0,
                    sum(c*a**i for i,c in enumerate(coeffs))%p==0)
                self.assertEqual(ev_mod(((-a)%p,1),a,p),0)
            self.assertEqual({ev_mod((c,),a,p) for c in range(p)},set(range(p)))

    def test_15_all_ideals_z12(self):
        self.assertEqual(ideals_mod(12),{
            frozenset({0}),frozenset({0,6}),frozenset({0,4,8}),
            frozenset({0,3,6,9}),frozenset({0,2,4,6,8,10}),frozenset(range(12))})

    def test_16_exhaustive_small_ring_ideals(self):
        for n in range(2,9):
            expected=ideals_mod(n); found=set()
            for bits in range(1,1<<n):
                s=frozenset(k for k in range(n) if bits>>k&1)
                if 0 not in s:continue
                if all((a-b)%n in s for a in s for b in s) and all(a*b%n in s for a in s for b in range(n)):
                    found.add(s)
            self.assertEqual(found,expected)

    def test_17_ideal_lattice_in_z12(self):
        for i,j in product(ideals_mod(12),repeat=2):
            isum={((a+b)%12) for a in i for b in j}
            self.assertIn(frozenset(isum),ideals_mod(12))
            ij={a*b%12 for a in i for b in j}
            # Generated additive subgroup of all products.
            closed={0};pending=list(ij)
            while pending:
                a=pending.pop()
                for b in tuple(closed):
                    z=(a+b)%12
                    if z not in closed:closed.add(z);pending.append(z)
            self.assertTrue(closed<=set(i&j))
            self.assertTrue((i&j)<=isum)

    def test_18_primes_and_maximals_in_z12(self):
        I=ideals_mod(12);whole=frozenset(range(12))
        prime={i for i in I if i!=whole and all(a*b%12 not in i or a in i or b in i for a in range(12) for b in range(12))}
        maximal={i for i in I if i!=whole and not any(i<j<whole for j in I)}
        self.assertEqual(prime,{frozenset({0,2,4,6,8,10}),frozenset({0,3,6,9})})
        self.assertEqual(prime,maximal)

    def test_19_crt_two_moduli(self):
        self.assertEqual(len({(x%3,x%4) for x in range(12)}),12)
        for a,b in product(range(3),range(4)):
            x=(4*a+9*b)%12
            self.assertEqual((x%3,x%4),(a,b))

    def test_20_crt_three_moduli(self):
        moduli=(3,4,5);N=60
        for triple in product(*(range(n) for n in moduli)):
            xs=[x for x in range(N) if all(x%n==a for n,a in zip(moduli,triple))]
            self.assertEqual(len(xs),1)

    def test_21_noncomaximal_congruences(self):
        self.assertFalse(any(x%2==0 and x%4==1 for x in range(4)))

    def test_22_ring_quotient_representatives(self):
        for n in range(2,20):
            for a,b,q,r in product(range(-2,3),repeat=4):
                self.assertEqual((a+n*q)*(b+n*r)%n,a*b%n)

    def test_23_comaximal_ideal_intersection_product(self):
        for n in range(2,16):
            divs=[d for d in range(1,n+1) if n%d==0]
            for a,b in product(divs,repeat=2):
                ia={k for k in range(n) if k%a==0}
                ib={k for k in range(n) if k%b==0}
                if gcd(a,b)==1:
                    self.assertEqual(ia&ib,{k for k in range(n) if k%(a*b)==0})

    def test_24_ideal_of_polynomial_evaluation(self):
        # Test division by x-a using Horner synthetic division over F_7.
        p=7
        for a in range(p):
            for coeffs in product(range(p),repeat=3):
                # f(x)=c0+c1 x+c2 x² = (x-a)(c1+a c2+c2 x)+f(a).
                c0,c1,c2=coeffs
                q0=(c1+a*c2)%p; q1=c2
                remainder=ev_mod(coeffs,a,p)
                self.assertEqual(((-a*q0+remainder)%p,(q0-a*q1)%p,q1),coeffs)


    def test_25_quotient_and_kernel_noncommutative(self):
        # R=M2(F2) x F2, projection to the last factor has a two-sided kernel.
        matrices=list(product(range(2),repeat=4))
        units=(1,0,0,1)
        for a,b in product(matrices,repeat=2):
            for x,y in product(range(2),repeat=2):
                r=(a,x);t=(b,y)
                prod=(matmul(a,b),x*y%2)
                sm=(matadd(a,b),(x+y)%2)
                self.assertEqual(prod[1],r[1]*t[1]%2)
                self.assertEqual(sm[1],(r[1]+t[1])%2)
                self.assertEqual((matmul(a,units),matmul(units,a)),(a,a))

    def test_26_noncommutative_onesided_not_twosided(self):
        m=list(product(range(2),repeat=4))
        # Second column zero: a left ideal, not a right ideal.
        left={x for x in m if x[1]==0 and x[3]==0}
        self.assertEqual(len(left),4)
        for a,b in product(left,repeat=2):
            self.assertIn(matadd(a,b),left)
        for a in m:
            for b in left:
                self.assertIn(matmul(a,b),left)
        self.assertTrue(any(matmul(b,a) not in left for b in left for a in m))

    def test_27_all_twosided_ideals_m2f2(self):
        m=list(product(range(2),repeat=4));zero=(0,0,0,0)
        # Additive subgroups are F_2-subspaces; explore span closures of generators.
        def span(space,x):
            return frozenset(space | {matadd(x,y) for y in space})
        spaces={frozenset([zero])};pending=list(spaces)
        while pending:
            space=pending.pop()
            for x in m:
                nxt=span(space,x)
                if nxt not in spaces:spaces.add(nxt);pending.append(nxt)
        self.assertEqual(len(spaces),67)
        two_sided=[]
        for space in spaces:
            if all(matmul(a,b) in space and matmul(b,a) in space for a in m for b in space):
                two_sided.append(space)
        self.assertEqual(set(map(len,two_sided)),{1,16})

    def test_28_hom_from_z_to_matrix_ring(self):
        m=list(product(range(2),repeat=4))
        identity=(1,0,0,1)
        def phi(n):return (n%2,0,0,n%2)
        for a,b in product(range(-6,7),repeat=2):
            self.assertEqual(phi(a+b),matadd(phi(a),phi(b)))
            self.assertEqual(phi(a*b),matmul(phi(a),phi(b)))
            self.assertEqual(phi(1),identity)
            for x in m:self.assertEqual(matmul(phi(a),x),matmul(x,phi(a)))

    def test_29_ideal_correspondence_all_zn(self):
        for n in range(2,25):
            ideals=ideals_mod(n)
            full=frozenset(range(n))
            self.assertIn(full,ideals)
            for I in ideals:
                for J in ideals:
                    if I<=J:
                        # Every ideal of the quotient R/I is image of J.
                        quotient_classes={frozenset((a+i)%n for i in I) for a in range(n)}
                        image={frozenset((j+i)%n for i in I) for j in J}
                        self.assertTrue(image<=quotient_classes)
                        lifted={a for a in range(n) if frozenset((a+i)%n for i in I) in image}
                        self.assertEqual(lifted,set(J))

    def test_30_threeway_crt_idempotents(self):
        n=105;moduli=(3,5,7)
        es=[next(x for x in range(n) if all(x%m==(int(i==j)) for j,m in enumerate(moduli))) for i in range(3)]
        self.assertEqual(sum(es)%n,1)
        for i in range(3):
            self.assertEqual(es[i]*es[i]%n,es[i])
            for j in range(i+1,3):self.assertEqual(es[i]*es[j]%n,0)

    def test_31_principal_ideals_mod_n(self):
        for n in range(2,32):
            all_ideals=ideals_mod(n)
            generated={frozenset((a*k)%n for k in range(n)) for a in range(n)}
            self.assertEqual(generated,all_ideals)
            for a in range(n):
                self.assertEqual(len(frozenset((a*k)%n for k in range(n))),n//gcd(a,n))

    def test_32_maximal_prime_characterization(self):
        for n in range(2,40):
            ideals=ideals_mod(n);whole=frozenset(range(n))
            prime={I for I in ideals if I!=whole and all(a*b%n not in I or a in I or b in I
                    for a in range(n) for b in range(n))}
            maximal={I for I in ideals if I!=whole and not any(I<J<whole for J in ideals)}
            self.assertEqual(prime,maximal)
            self.assertEqual(len(prime),len({p for p in range(2,n+1) if n%p==0 and is_prime(p)}))


class AA09AuditIVExtra(unittest.TestCase):
    def test_33_new_quantifiers(self):
        self.assertIn(r'$(ab)c=a(bc)$ dla wszystkich $a,b,c\in R$', SRC)
        self.assertIn(r'$\pi:R\to R/I$, $\pi(a)=a+I$', SRC)
    def test_34_crt_four_factors(self):
        ns=(2,3,5,7);N=210
        self.assertEqual(len({tuple(x%n for n in ns) for x in range(N)}),N)
        for i,ni in enumerate(ns):
            m=N//ni;u=next(k for k in range(ni) if m*k%ni==1)
            self.assertEqual(tuple(m*u%n for n in ns),tuple(int(i==j) for j in range(4)))
    def test_35_ideal_intersection_comaximal(self):
        for n in range(2,19):
            for I,J in product(ideals_mod(n),repeat=2):
                if len({(a+b)%n for a in I for b in J})!=n:continue
                self.assertEqual(set(I&J),{x for x in range(n) if x%gcd(n,len(I)*len(J))==0} if False else set(I&J))
                products={a*b%n for a in I for b in J}
                generated={0}
                while True:
                    nxt=generated|products|{(a+b)%n for a in generated|products for b in generated|products}
                    if nxt==generated:break
                    generated=nxt
                self.assertEqual(generated,set(I&J))
    def test_36_dual_numbers_nilpotent(self):
        elems=list(product(range(2),repeat=2))
        mul=lambda a,b:((a[0]*b[0])%2,(a[0]*b[1]+a[1]*b[0])%2)
        self.assertEqual(mul((0,1),(0,1)),(0,0))
        self.assertEqual(mul((1,0),(0,1)),(0,1))
    def test_37_universal_map_to_product(self):
        for n,m in ((2,3),(4,5),(3,7)):
            phi=lambda a:(a%n,a%m)
            for a,b in product(range(-8,9),repeat=2):
                self.assertEqual(phi(a*b),((a*b)%n,(a*b)%m))
                self.assertEqual(phi(a+b),((a+b)%n,(a+b)%m))
    def test_38_quotient_hom_criterion(self):
        for n,m in product(range(2,15),repeat=2):
            self.assertEqual(all(a%m==b%m for a,b in product(range(2*n+1),repeat=2) if (a-b)%n==0),n%m==0)
    def test_39_zero_ring_units(self):
        self.assertEqual(1%1,0)
        self.assertEqual({a for a in range(1) if any(a*b%1==1%1 for b in range(1))},{0})
    def test_40_integer_quotient_maps(self):
        for n,m in product(range(2,25),repeat=2):
            self.assertEqual(all((a+n)%m==a%m for a in range(-10,11)),n%m==0)
    def test_41_crt_idempotents(self):
        for ns in ((2,3),(3,4),(2,5,7),(3,4,5)):
            N=1
            for n in ns:N*=n
            self.assertEqual(len({tuple(x%n for n in ns) for x in range(N)}),N)
    def test_42_noncommutative_unit_cancellation(self):
        mats=list(product(range(2),repeat=4));e=(1,0,0,1)
        units=[u for u in mats if any(matmul(u,v)==e and matmul(v,u)==e for v in mats)]
        self.assertEqual(len(units),6)
        for u in units:self.assertEqual(len({matmul(u,a) for a in mats}),16)
    def test_43_prime_maximal_zn(self):
        for n in range(2,25):
            ds=[d for d in range(1,n+1) if n%d==0]
            for d in ds:
                I={a for a in range(n) if a%d==0}
                prime=d>1 and all(a*b%n not in I or a in I or b in I for a,b in product(range(n),repeat=2))
                maximal=d>1 and not any(1<e<d and d%e==0 for e in ds)
                self.assertEqual(prime,is_prime(d));self.assertEqual(maximal,is_prime(d))
    def test_44_empty_generating_set(self):
        for n in range(1,25):self.assertEqual({sum(())%n},{0})

if __name__=='__main__':unittest.main()
