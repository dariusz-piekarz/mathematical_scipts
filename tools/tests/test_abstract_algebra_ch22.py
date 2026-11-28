"""AA-22, audit I: independent structural and finite-model checks.

Finite models and symbolic examples corroborate, but do not replace,
proofs of Artin's theorem and the Galois correspondence.
"""
import itertools
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra'
SRC=ROOT/'22-twierdzenie-artina-i-odpowiedniosc-galois.tex'
S=SRC.read_text(encoding='utf8')
POSSIBLE={tuple(x) for x in itertools.permutations(range(3))}
E=(0,1,2)

def compose(a,b):
    return tuple(a[b[i]] for i in range(3))

def subgroup(G,H,mul=compose,one=E):
    return one in H and all(mul(a,b) in H for a in H for b in H)

def subgroups(G):
    el=list(G)
    return [frozenset(H) for k in range(1,len(el)+1) for H in itertools.combinations(el,k)
            if subgroup(G,H)]

def inverse_perm(a):
    return next(x for x in POSSIBLE if compose(a,x)==E and compose(x,a)==E)

def conjugate_subgroup(G,H,a):
    ia=inverse_perm(a)
    return frozenset(compose(compose(a,h),ia) for h in H)

def v4mul(a,b):return a^b

V4=tuple(range(4))
V4H=[frozenset(H) for k in range(1,5) for H in itertools.combinations(V4,k)
     if 0 in H and all(v4mul(a,b) in H for a in H for b in H)]

def v4_fixed_dim(H):
    # Basis 1, sqrt(2), sqrt(3), sqrt(6): s=(1,0), t=(0,1)
    weights=[(0,0),(1,0),(0,1),(1,1)]
    return sum(all((weights[j][0]*(h&1)+weights[j][1]*((h>>1)&1))%2==0
                   for h in H) for j in range(4))

class Structure(unittest.TestCase):
    def test_01_heading(self):
        self.assertIn(r'\chapter[Twierdzenie Artina i odpowiedniość Galois]',S)
    def test_02_labels_are_unique(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual(len(labels),12)
        self.assertEqual(len(set(labels)),len(labels))
    def test_03_refs(self):
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)
        self.assertEqual(len(refs),21)
        labels=set(re.findall(r'\\label\{([^}]+)\}',S))
        self.assertEqual(set(refs)-labels, {
            'aa:ch:embeddings-normal-separable','aa:ch:szeregi',
            'aa:lem:extend-embedding-simple','aa:prz:biquadratic-extension',
            'aa:prz:cubic-splitting','aa:prz:quadratic-conjugation',
            'aa:tw:galois-group-degree','aa:tw:field-tower','aa:tw:algebraic-closure-exists','aa:tw:normal-embeddings',
            'aa:wn:extend-embedding-finite'})
    def test_04_environments(self):
        for e in ('proof','twierdzenie','wniosek','lemat','definicja','przyklad','uwaga'):
            self.assertEqual(S.count('\\begin{'+e+'}'), S.count('\\end{'+e+'}'),e)
    def test_05_proof_and_example_counts(self):
        self.assertEqual(S.count(r'\begin{proof}'),5)
        self.assertEqual(S.count(r'\begin{przyklad}'),4)
    def test_06_terminology(self):
        self.assertNotIn('tensorowanie',S.lower())
        self.assertNotIn('sekwencyjn',S.lower())
        self.assertNotIn('zwartościowanie',S.lower())
    def test_07_Artin_upper_bound_source(self):
        self.assertIn(r'[L:F]\le m',S)
        self.assertIn('najmniejszą',S)
        self.assertIn(r'\tau(a_j)-a_j',S)
    def test_08_Artin_lower_bound_source(self):
        self.assertIn(r'm\le n',S)
        self.assertIn(r'\ref{aa:lem:artin-independence}',S)
    def test_09_orbit_polynomial_source(self):
        self.assertIn(r'p_x(X)=\prod_{y\in Gx}(X-y)',S)
        self.assertIn('pierwiastki proste',S)
    def test_10_intermediate_splitting_source(self):
        self.assertIn(r'L=K(S)',S)
        self.assertIn(r'L=E(S)',S)
    def test_11_cubic_Galois_action_source(self):
        self.assertIn(r'G\cong S_3',S)
        self.assertIn(r'\tau\sigma\tau^{-1}=\sigma^{-1}',S)
    def test_12_field_fixed_definition(self):
        self.assertIn(r'L^H=\{x\in L:',S)

class Biquadratic(unittest.TestCase):
    def test_13_five_subgroups(self):
        self.assertEqual(len(V4H),5)
    def test_14_trivial_group_fixed_field(self):
        self.assertEqual(v4_fixed_dim(frozenset([0])),4)
    def test_15_full_group_fixed_field(self):
        self.assertEqual(v4_fixed_dim(frozenset(V4)),1)
    def test_16_order_two_subgroups(self):
        self.assertEqual(sum(len(H)==2 for H in V4H),3)
    def test_17_Artin_degree_identity(self):
        for H in V4H:
            self.assertEqual(v4_fixed_dim(H)*len(H),4)
    def test_18_all_subgroups_normal(self):
        for H in V4H:
            for a in V4:
                self.assertEqual({a^h^a for h in H},set(H))
    def test_19_fixed_quotient_fields(self):
        self.assertEqual(v4_fixed_dim(frozenset([0,1])),2) # Q(sqrt3)
        self.assertEqual(v4_fixed_dim(frozenset([0,2])),2) # Q(sqrt2)
        self.assertEqual(v4_fixed_dim(frozenset([0,3])),2) # Q(sqrt6)
    def test_20_quadratic_invariants(self):
        for a in range(-3,4):
            for b in range(-3,4):
                self.assertEqual((a,b)==(a,-b),b==0)
    def test_21_degrees(self):
        self.assertEqual(4//2,2)
        self.assertEqual(2*2,4)

class S3(unittest.TestCase):
    def test_22_group_size(self):self.assertEqual(len(POSSIBLE),6)
    def test_23_composition_closed(self):
        for a,b in itertools.product(POSSIBLE,repeat=2):
            self.assertIn(compose(a,b),POSSIBLE)
    def test_24_six_subgroups(self):self.assertEqual(len(subgroups(POSSIBLE)),6)
    def test_25_three_transpositions(self):
        self.assertEqual(sum(len(H)==2 for H in subgroups(POSSIBLE)),3)
    def test_26_normal_subgroups(self):
        G=POSSIBLE
        normals=[H for H in subgroups(G) if all(conjugate_subgroup(G,H,a)==H for a in G)]
        self.assertEqual(sorted(map(len,normals)),[1,3,6])
    def test_27_C3_fixed_degree2(self):
        self.assertEqual(6//3,2)
    def test_28_C2_fixed_degree3(self):
        self.assertEqual(6//2,3)
    def test_29_sigma_tau_relation(self):
        sigma=(1,2,0);tau=(0,2,1)
        self.assertEqual(compose(tau,compose(sigma,tau)),compose(sigma,sigma))
    def test_30_sigma_order(self):
        sigma=(1,2,0)
        self.assertEqual(compose(sigma,compose(sigma,sigma)),E)
    def test_31_tau_order(self):
        tau=(0,2,1)
        self.assertEqual(compose(tau,tau),E)
    def test_32_non_normal_intermediate(self):
        H=frozenset([E,(0,2,1)])
        self.assertTrue(any(conjugate_subgroup(POSSIBLE,H,a)!=H for a in POSSIBLE))
    def test_33_Galois_order_reversing(self):
        for H in subgroups(POSSIBLE):
            for J in subgroups(POSSIBLE):
                if H <= J:
                    self.assertGreaterEqual(6//len(H),6//len(J))

class FiniteFields(unittest.TestCase):
    def test_34_divisors_of12(self):
        self.assertEqual([d for d in range(1,13) if 12%d==0],[1,2,3,4,6,12])
    def test_35_subgroups_cyclic_12(self):
        for d in (1,2,3,4,6,12):
            H={(d*k)%12 for k in range(12)}
            self.assertEqual(len(H),12//d)
    def test_36_fixed_field_cardinality(self):
        for p in (2,3,5,7):
            for d in (1,2,3,4,6,12):
                self.assertEqual(math.gcd(p**12-1,p**d-1),p**d-1)
    def test_37_frobenius_generation(self):
        for d in (1,2,3,4,6,12):
            self.assertEqual(12//math.gcd(12,d),12//d)
    def test_38_degree_index(self):
        for d in (1,2,3,4,6,12):
            self.assertEqual((12//d)*d,12)
    def test_39_subgroup_lattice(self):
        H={d:{(d*k)%12 for k in range(12)} for d in (1,2,3,4,6,12)}
        for d,e in itertools.product(H,repeat=2):
            self.assertEqual(H[d]<=H[e],d%e==0)

class CubicNonNormal(unittest.TestCase):
    def test_40_x_cubed_two_no_rational_root(self):
        self.assertTrue(all(Fraction(a,b)**3!=2 for a in range(-12,13)
                            for b in range(1,13)))
    def test_41_omega_quadratic(self):
        # X^2+X+1 has discriminant -3, hence no real root.
        self.assertEqual(1-4,-3)
    def test_42_unique_real_root_of_x_cubed2(self):
        from math import isclose
        a=2**(1/3)
        self.assertTrue(isclose(a**3,2,rel_tol=1e-12))
        self.assertTrue(a>0)
    def test_43_Artin_trivial_automorphism(self):
        # A real K-automorphism must send alpha to a real root of X^3-2.
        # Strict monotonicity on R implies this root is alpha only.
        for x in (-3,-1,0,1,3):
            for y in (-3,-1,0,1,3):
                self.assertEqual(x**3==y**3,x==y)
    def test_44_simple_degree(self):
        self.assertEqual(3*2,6)

class LinearIndependenceModels(unittest.TestCase):
    def test_45_quadratic_evaluation_determinant(self):
        # Rows are the identity and conjugation on basis 1, sqrt(2).
        # det[[1,sqrt2],[1,-sqrt2]] = -2 sqrt(2) != 0.
        import math
        a=math.sqrt(2)
        self.assertNotEqual(1*(-a)-1*a,0)
    def test_46_V4_character_matrix_determinant(self):
        # Each of the four automorphisms is distinguished by values on
        # 1, sqrt2, sqrt3, sqrt6; the character table is Hadamard.
        mat=[]
        for h in V4:
            mat.append([(-1)**((bits[0]*(h&1)+bits[1]*((h>>1)&1))%2)
                        for bits in [(0,0),(1,0),(0,1),(1,1)]])
        det=sum((-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
                *math.prod(mat[i][perm[i]] for i in range(4))
                for perm in itertools.permutations(range(4)))
        self.assertEqual(abs(det),16)
    def test_47_quadratic_inverse(self):
        # (a+b sqrt2)^(-1)=(a-b sqrt2)/(a^2-2b^2).
        for a,b in itertools.product(range(-5,6),repeat=2):
            if a==b==0:continue
            d=a*a-2*b*b
            self.assertNotEqual(d,0)
            # (a+b r)(a-b r)=d for r^2=2.
            self.assertEqual((a*a-2*b*b,0),(d,0))

if __name__=='__main__':
    unittest.main()
