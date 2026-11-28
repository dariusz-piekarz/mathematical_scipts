"""Independent AA-22 audit II: finite-field and biquadratic arithmetic.

Checks illustrate particular instances of Galois theory, not its general proof.
"""
import itertools
import re
import unittest
from pathlib import Path

SRC = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex')
S = SRC.read_text(encoding='utf-8')

# F_16 = F_2[x] / (x^4+x+1), with x represented by binary 0010.
def mul16(a,b):
    out=0
    for i in range(4):
        if (b >> i) & 1:out ^= a
        a <<= 1
        if a & 16:a ^= 0b10011
    return out & 15

def pow16(a,n):
    out=1
    while n:
        if n&1:out=mul16(out,a)
        a=mul16(a,a)
        n//=2
    return out

def fr(a,k):return pow16(a,2**k)

# Q(sqrt 2,sqrt 3) with basis (1,a,b,ab).
def mult_biq(x,y):
    z=[0]*4
    for i,u in enumerate(x):
        for j,v in enumerate(y):
            factor=(2 if (i&1 and j&1) else 1) * (3 if (i&2 and j&2) else 1)
            z[i^j] += u*v*factor
    return tuple(z)

def auto_biq(x,s,t):
    return tuple(x[i]*(-1 if bool(s and (i&1)) != bool(t and (i&2)) else 1) for i in range(4))

class IndependentAuditII(unittest.TestCase):
    def test_01_fixed_field_defines_zero_and_one(self):
        self.assertIn(r'$0,1\in L^H$',S)

    def test_02_algebraic_closure_omega_explicit(self):
        self.assertIn('ciało algebraicznie domknięte $\\Omega$ zawierające $L$', S)
        self.assertLess(S.index('domknięte $\\Omega$'),S.index(r'\iota:E\hookrightarrow\Omega'))

    def test_03_tower_used_for_intermediate_finiteness(self):
        self.assertIn(r'[L:K]=[L:E][E:K]<\infty', S)
        self.assertIn(r'\ref{aa:tw:field-tower}', S)

    def test_04_reverse_subgroups_inclusions_shown(self):
        self.assertIn(r'H_1\subseteq H_2', S)
        self.assertIn(r'L^{H_2}\subseteq L^{H_1}', S)

    def test_05_source_counts(self):
        self.assertEqual((len(re.findall(r'\\label\{[^}]+\}',S)),len(re.findall(r'\\(?:ref|eqref)\{[^}]+\}',S))),(12,21))

    def test_06_f16_relations(self):
        self.assertEqual(pow16(2,4),3) # x^4=x+1
        self.assertEqual(pow16(2,15),1)

    def test_07_f16_all_nonzero_have_inverse(self):
        for a in range(1,16):
            self.assertTrue(any(mul16(a,b)==1 for b in range(1,16)))

    def test_08_frobenius_is_additive(self):
        for a,b in itertools.product(range(16),repeat=2):
            self.assertEqual(fr(a^b,1),fr(a,1)^fr(b,1))

    def test_09_frobenius_is_multiplicative(self):
        for a,b in itertools.product(range(16),repeat=2):
            self.assertEqual(fr(mul16(a,b),1),mul16(fr(a,1),fr(b,1)))

    def test_10_frobenius_order_four(self):
        self.assertTrue(all(fr(a,4)==a for a in range(16)))
        for j in (1,2,3):self.assertNotEqual(fr(2,j),2)

    def test_11_F16_fixed_by_total_group_is_F2(self):
        self.assertEqual([a for a in range(16) if all(fr(a,j)==a for j in range(4))],[0,1])

    def test_12_F16_fixed_by_Frob_squared_is_F4(self):
        fixed={a for a in range(16) if fr(a,2)==a}
        self.assertEqual(len(fixed),4)
        self.assertTrue(all((a^b) in fixed and mul16(a,b) in fixed for a,b in itertools.product(fixed,repeat=2)))

    def test_13_F16_fixed_by_identity_is_F16(self):
        self.assertEqual(sum(fr(a,4)==a for a in range(16)),16)

    def test_14_F16_Artin_degree_count(self):
        for step in (1,2,4):
            H={j%4 for j in range(0,4,step)}
            F={a for a in range(16) if all(fr(a,j)==a for j in H)}
            self.assertEqual(len(F)**len(H),16)

    def test_15_biquadratic_basic_products(self):
        a=(0,1,0,0);b=(0,0,1,0);ab=(0,0,0,1)
        self.assertEqual(mult_biq(a,a),(2,0,0,0))
        self.assertEqual(mult_biq(b,b),(3,0,0,0))
        self.assertEqual(mult_biq(a,b),ab)
        self.assertEqual(mult_biq(ab,ab),(6,0,0,0))

    def test_16_biquadratic_multiplication_associative_models(self):
        basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        for x,y,z in itertools.product(basis,repeat=3):
            self.assertEqual(mult_biq(mult_biq(x,y),z),mult_biq(x,mult_biq(y,z)))

    def test_17_biquadratic_s_is_automorphism(self):
        basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        for x,y in itertools.product(basis,repeat=2):
            self.assertEqual(auto_biq(mult_biq(x,y),1,0),mult_biq(auto_biq(x,1,0),auto_biq(y,1,0)))

    def test_18_biquadratic_st_is_involution(self):
        for x in itertools.product(range(-2,3),repeat=4):
            self.assertEqual(auto_biq(auto_biq(x,1,1),1,1),x)

    def test_19_biquadratic_s_fixed_basis_is_Q_sqrt3(self):
        basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        self.assertEqual([i for i,x in enumerate(basis) if auto_biq(x,1,0)==x],[0,2])

    def test_20_biquadratic_st_fixed_basis_is_Q_sqrt6(self):
        basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        self.assertEqual([i for i,x in enumerate(basis) if auto_biq(x,1,1)==x],[0,3])

    def test_21_biquadratic_all_fixed_is_Q(self):
        basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        self.assertEqual([i for i,x in enumerate(basis) if all(auto_biq(x,s,t)==x for s,t in itertools.product((0,1),repeat=2))],[0])

    def test_22_example_cubic_s3_group_nonabelian(self):
        sigma=(1,2,0);tau=(0,2,1)
        def mul(a,b):return tuple(a[b[i]] for i in range(3))
        self.assertNotEqual(mul(sigma,tau),mul(tau,sigma))
        self.assertEqual(mul(tau,mul(sigma,tau)),mul(sigma,sigma))

    def test_23_s3_normals_exact(self):
        p=list(itertools.permutations(range(3)));identity=(0,1,2)
        def mul(a,b):return tuple(a[b[i]] for i in range(3))
        def inv(a):return next(b for b in p if mul(a,b)==identity)
        sg=[]
        for n in range(1,7):
            for tup in itertools.combinations(p,n):
                H=set(tup)
                if identity in H and all(mul(x,y) in H for x,y in itertools.product(H,repeat=2)):
                    sg.append(H)
        normal=[H for H in sg if all(mul(mul(a,x),inv(a)) in H for a,x in itertools.product(p,H))]
        self.assertEqual(sorted(map(len,normal)),[1,3,6])

    def test_24_non_normal_cubic_aut_group(self):
        # Q(real cube root 2) admits no nontrivial Q-automorphism.
        # Its minimal polynomial has one real root by strict monotonicity.
        for k in range(-8,9):
            for m in range(-8,9):
                if k!=m:self.assertNotEqual(k**3,m**3)

if __name__=='__main__':unittest.main()
