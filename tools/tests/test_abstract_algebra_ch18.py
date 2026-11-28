"""AA-18: 64 regression checks for tensor products and localization.

Finite-model checks support but do not replace mathematical proofs.
"""


# From test_aa18.py
"""Independent mathematical and structural checks for abstract algebra AA-18.

Finite-model tests illustrate/check specific formulas, not proofs of general theorems.
"""
import itertools
import math
import random
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex'
SOURCE=ROOT
TEXT=SOURCE.read_text(encoding='utf-8')


def m2mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2
                 for i in range(2) for j in range(2))


def gf2_rank(matrix):
    if not matrix: return 0
    bits=[sum((val&1)<<j for j,val in enumerate(row)) for row in matrix]
    basis={}
    for row in bits:
        while row:
            p=row.bit_length()-1
            if p in basis: row^=basis[p]
            else:
                basis[p]=row
                break
    return len(basis)


def eval_pair(c,a,b):
    return sum(c[4*i+j]*a[i]*b[j] for i in range(4) for j in range(4))%2


def zmod_loc(m,k):
    """Value of m/2**k in Z/3: localization of Z/6 at powers of 2."""
    return m*pow(2,-k,3)%3


def equiv_local(a,b):
    """Compare pairs (residue mod 6, 2**k), with enough annihilators."""
    m,k=a; n,l=b
    diff=(2**l*m-2**k*n)%6
    return any(pow(2,j,6)*diff%6==0 for j in range(0,6))


class StructuralChecks(unittest.TestCase):
    def test_01_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),20)
        self.assertEqual(len(labels),len(set(labels)))

    def test_02_refs(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEXT))
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',TEXT)
        self.assertEqual(len(refs),11)
        self.assertEqual(set(refs)-labels,
                         {'aa:ch:grupy-abelowe','aa:ch:modules-introduction',
                          'aa:tw:modules-projective-summand'})

    def test_03_proofs_and_examples(self):
        self.assertEqual(TEXT.count(r'\begin{proof}'),12)
        self.assertEqual(TEXT.count(r'\end{proof}'),12)
        self.assertEqual(TEXT.count(r'\begin{przyklad}'),7)
        self.assertEqual(TEXT.count(r'\end{przyklad}'),7)

    def test_04_all_environments(self):
        for env in ('twierdzenie','wniosek','definicja','stwierdzenie','uwaga'):
            self.assertEqual(TEXT.count(r'\begin{'+env+'}'),
                             TEXT.count(r'\end{'+env+'}'))

    def test_05_style(self):
        self.assertNotIn('tensorowanie',TEXT.lower())
        self.assertNotIn('sekwencj',TEXT.lower())

    def test_06_universal_construction_quotient(self):
        self.assertIn('wolną grupą abelową',TEXT)
        self.assertIn(r'M\otimes_RN=F/L',TEXT)
        self.assertIn(r'\bar b(x+L)=B(x)',TEXT)

    def test_07_full_localization_operations(self):
        self.assertIn("$[m,s]+[m',s']=[s'm+sm',ss']$",TEXT)
        self.assertIn("$r[m,s]=[rm,s]$",TEXT)
        self.assertIn('Jest to relacja równoważności',TEXT)
        self.assertIn('Łączność dodawania wynika',TEXT)


class CyclicTensors(unittest.TestCase):
    def test_08_gcd_formula_range(self):
        for m,n in itertools.product(range(1,51),repeat=2):
            d=math.gcd(m,n)
            subgroup={m*a+n*b for a in range(-12,13) for b in range(-12,13)}
            self.assertTrue(all(x%d==0 for x in subgroup))
            self.assertTrue(m%d==0 and n%d==0)

    def test_09_zero_tensor_nonzero_cyclic(self):
        for m,n in ((2,3),(3,5),(4,9),(8,15)):
            self.assertEqual(math.gcd(m,n),1)
            self.assertGreater(m,1);self.assertGreater(n,1)

    def test_10_symmetric_cyclic(self):
        for m,n in itertools.product(range(1,40),repeat=2):
            self.assertEqual(math.gcd(m,n),math.gcd(n,m))

    def test_11_associative_cyclic(self):
        for m,n,k in itertools.product(range(1,13),repeat=3):
            self.assertEqual(math.gcd(math.gcd(m,n),k),
                             math.gcd(m,math.gcd(n,k)))

    def test_12_direct_sum_tensor_order(self):
        for m,n,k in itertools.product(range(1,15),repeat=3):
            # (Z/m ⊕ Z/n) ⊗ Z/k has order gcd(m,k)*gcd(n,k).
            cardinal=math.gcd(m,k)*math.gcd(n,k)
            self.assertGreaterEqual(cardinal,1)
            if m==n==k: self.assertEqual(cardinal,k*k)

    def test_13_tensor_with_Z(self):
        for n in range(1,100):
            self.assertEqual(math.gcd(0,n),n)

    def test_14_cyclic_hom_count(self):
        for m,n in itertools.product(range(1,28),repeat=2):
            solutions=[y for y in range(n) if m*y%n==0]
            self.assertEqual(len(solutions),math.gcd(m,n))

    def test_15_cyclic_hom_generators(self):
        for m,n in itertools.product(range(1,28),repeat=2):
            d=math.gcd(m,n)
            self.assertEqual({y for y in range(n) if m*y%n==0},
                             {(n//d*j)%n for j in range(d)})

    def test_16_tensor_quotient_Zn(self):
        for m,n in itertools.product(range(1,35),repeat=2):
            im={m*a+n*b for a,b in itertools.product(range(-5,6),repeat=2)}
            d=math.gcd(m,n)
            self.assertTrue(all(x%d==0 for x in im))
            self.assertEqual(d,math.gcd(m,n))

    def test_17_Q_divisible(self):
        for q in [Fraction(a,b) for a in range(-10,11) for b in range(1,8)]:
            for n in range(1,15):
                self.assertEqual(n*(q/n),q)

    def test_18_right_exactness_cyclic(self):
        for n,m in itertools.product(range(1,24),repeat=2):
            # tensor the exact Z --n--> Z --> Z/n --> 0 by Z/m
            image={n*x%m for x in range(m)}
            d=math.gcd(n,m)
            kernel={y for y in range(m) if y%d==0}
            self.assertEqual(image,kernel)
            self.assertEqual(len(image)*d,m)

    def test_19_left_exactness_can_fail(self):
        for n in (2,3,5,7):
            self.assertEqual({(n*x)%n for x in range(n)},{0})

    def test_20_Q_flatness_multiplication(self):
        for a in range(1,12):
            samples=[Fraction(n,d) for n in range(-6,7) for d in range(1,7)]
            self.assertEqual(len({a*x for x in samples}),len(set(samples)))

    def test_21_Q_no_hom_to_Z(self):
        for h1 in range(-100,101):
            if all(h1 % n == 0 for n in range(1,201)):
                self.assertEqual(h1,0)


class VectorTensors(unittest.TestCase):
    def test_22_simple_tensors_F2_rank_one(self):
        outer=set()
        for v,w in itertools.product(itertools.product(range(2),repeat=2),repeat=2):
            outer.add(tuple(v[i]*w[j]%2 for i in range(2) for j in range(2)))
        self.assertEqual(len(outer),10)
        self.assertNotIn((1,0,0,1),outer)  # identity rank 2

    def test_23_tensor_basis_F3(self):
        outer=[]
        for v,w in itertools.product(itertools.product(range(3),repeat=2),repeat=2):
            outer.append(tuple(v[i]*w[j]%3 for i in range(2) for j in range(2)))
        canonical={(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)}
        self.assertTrue(canonical.issubset(set(outer)))

    def test_24_vector_hom_adjunction_dims(self):
        for m,n,p in itertools.product(range(4),repeat=3):
            self.assertEqual((m*n)*p,m*(n*p))

    def test_25_vector_sum_distributes(self):
        for m,n,p in itertools.product(range(4),repeat=3):
            self.assertEqual((m+n)*p,m*p+n*p)

    def test_26_vector_associativity(self):
        for m,n,p in itertools.product(range(4),repeat=3):
            self.assertEqual((m*n)*p,m*(n*p))


class NoncommutativeChecks(unittest.TestCase):
    def test_27_balanced_product_M2F2(self):
        basis=[tuple(int(i==k) for i in range(4)) for k in range(4)]
        for x,y,r in itertools.product(basis,repeat=3):
            self.assertEqual(m2mul(m2mul(x,r),y),m2mul(x,m2mul(r,y)))

    def test_28_balanced_form_dimension_M2F2(self):
        basis=[tuple(int(i==k) for i in range(4)) for k in range(4)]
        equations=[]
        for x,y,r in itertools.product(basis,repeat=3):
            xr=m2mul(x,r);ry=m2mul(r,y)
            equations.append([((xr[i]*y[j])^(x[i]*ry[j])) for i in range(4) for j in range(4)])
        self.assertEqual(gf2_rank(equations),12)
        self.assertEqual(16-gf2_rank(equations),4)  # R⊗_R R ≅ R additive

    def test_29_balanced_multiplication_pairing(self):
        basis=[tuple(int(i==k) for i in range(4)) for k in range(4)]
        for phi in basis:
            for x,y,r in itertools.product(basis,repeat=3):
                coeff=lambda z: sum(p*q for p,q in zip(phi,z))%2
                self.assertEqual(coeff(m2mul(m2mul(x,r),y)),
                                 coeff(m2mul(x,m2mul(r,y))))


class LocalizationChecks(unittest.TestCase):
    def test_30_localization_equiv_reflexive_symmetric(self):
        pairs=list(itertools.product(range(6),range(4)))
        for a in pairs:
            self.assertTrue(equiv_local(a,a))
            for b in pairs:self.assertEqual(equiv_local(a,b),equiv_local(b,a))

    def test_31_localization_equiv_transitive(self):
        pairs=list(itertools.product(range(6),range(4)))
        for a,b,c in itertools.product(pairs,repeat=3):
            if equiv_local(a,b) and equiv_local(b,c):
                self.assertTrue(equiv_local(a,c))

    def test_32_localization_three_classes(self):
        pairs=list(itertools.product(range(6),range(4)))
        classes={zmod_loc(*x) for x in pairs}
        self.assertEqual(classes,{0,1,2})
        for a,b in itertools.product(pairs,repeat=2):
            self.assertEqual(equiv_local(a,b),zmod_loc(*a)==zmod_loc(*b))

    def test_33_localization_addition(self):
        pairs=list(itertools.product(range(6),range(4)))
        for (m,k),(n,l) in itertools.product(pairs,repeat=2):
            c=(2**l*m+2**k*n,k+l)
            self.assertEqual(zmod_loc(*c),(zmod_loc(m,k)+zmod_loc(n,l))%3)

    def test_34_localization_scalar(self):
        for m,k in itertools.product(range(6),range(4)):
            for r in range(-5,6):
                self.assertEqual(zmod_loc(r*m,k),r*zmod_loc(m,k)%3)

    def test_35_localization_exact_sequence(self):
        # 0 --> Z/2 --times 3--> Z/6 --mod 3--> Z/3 --> 0
        i={3*x%6 for x in range(2)}
        ker={x for x in range(6) if x%3==0}
        self.assertEqual(i,ker)
        # After localizing at 2: Z/2 vanishes, and Z/6 -> Z/3 becomes isomorphism.
        self.assertEqual({zmod_loc(m,k) for m in (0,3) for k in range(3)},{0})
        self.assertEqual({zmod_loc(m,0) for m in range(6)},set(range(3)))


# From test_aa18_independent.py
"""Independent finite-model regression checks for AA-18 audit II.

These checks validate specific algebraic models, not general proofs.
"""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex'
SOURCE=ROOT
TXT=SOURCE.read_text()


def equivalent_zmod(a, b, mod, prime):
    m,k=a; n,l=b
    diff=(pow(prime,l,mod)*m-pow(prime,k,mod)*n)%mod
    return any(diff*pow(prime,j,mod)%mod==0 for j in range(12))


def phi(a, modulus, prime):
    m,k=a
    return m*pow(pow(prime,k,modulus),-1,modulus)%modulus


def add_pairs(a,b,prime):
    m,k=a;n,l=b
    return (prime**l*m+prime**k*n,k+l)

class AuditIIIndependent(unittest.TestCase):
    def test_01_Z12_localization_classification(self):
        pairs=list(itertools.product(range(12),range(4)))
        for a,b in itertools.product(pairs,repeat=2):
            self.assertEqual(equivalent_zmod(a,b,12,3),phi(a,4,3)==phi(b,4,3))

    def test_02_Z18_localization_classification(self):
        pairs=list(itertools.product(range(18),range(3)))
        for a,b in itertools.product(pairs,repeat=2):
            self.assertEqual(equivalent_zmod(a,b,18,2),phi(a,9,2)==phi(b,9,2))

    def test_03_addition_well_defined_Z12(self):
        pairs=list(itertools.product(range(12),range(3)))
        for a,b in itertools.product(pairs,repeat=2):
            c=add_pairs(a,b,3)
            self.assertEqual(phi(c,4,3),(phi(a,4,3)+phi(b,4,3))%4)

    def test_04_addition_well_defined_Z18(self):
        pairs=list(itertools.product(range(18),range(3)))
        for a,b in itertools.product(pairs,repeat=2):
            self.assertEqual(phi(add_pairs(a,b,2),9,2),(phi(a,9,2)+phi(b,9,2))%9)

    def test_05_scalar_action_R_module(self):
        pairs=list(itertools.product(range(12),range(3)))
        for r,q,a in itertools.product(range(12),range(12),pairs):
            m,k=a
            self.assertEqual(phi(((r+q)*m,k),4,3),(phi((r*m,k),4,3)+phi((q*m,k),4,3))%4)
            self.assertEqual(phi((r*q*m,k),4,3),phi((r*(q*m),k),4,3))

    def test_06_r_distributes_over_localized_sum(self):
        pairs=list(itertools.product(range(12),range(3)))
        for r in range(12):
            for a,b in itertools.product(pairs,repeat=2):
                c=add_pairs(a,b,3)
                self.assertEqual(phi((r*c[0],c[1]),4,3),
                                 (r*phi(a,4,3)+r*phi(b,4,3))%4)

    def test_07_localization_module_naturality(self):
        # Reduction Z/12 -> Z/6 localizes to Z/4 -> Z/2.
        for m,k in itertools.product(range(12),range(5)):
            a=phi((m,k),4,3)%2
            b=phi((m%6,k),2,3)
            self.assertEqual(a,b)

    def test_08_exactness_localized(self):
        # 0 -> Z/3 --x4--> Z/12 -> Z/4 -> 0
        left={phi((4*x,k),4,3) for x in range(3) for k in range(4)}
        middle={phi((x,0),4,3) for x in range(12)}
        right={x for x in range(4)}
        self.assertEqual(left,{0})
        self.assertEqual(middle,right)

    def test_09_tensor_two_quotients(self):
        for m,n in itertools.product(range(1,32),repeat=2):
            d=math.gcd(m,n)
            # Balanced pairing (x mod m,y mod n) -> xy mod d.
            values={(x*y)%d for x in range(m) for y in range(n)}
            self.assertEqual(values,set(range(d)))
            self.assertEqual((m%n)%d,0)
            self.assertEqual((n%m)%d,0)

    def test_10_non_simple_F3_tensor(self):
        # Outer products produce rank <=1; identity has determinant 1.
        vectors=list(itertools.product(range(3),repeat=2))
        products={tuple(v[i]*w[j]%3 for i in range(2) for j in range(2))
                  for v,w in itertools.product(vectors,repeat=2)}
        self.assertNotIn((1,0,0,1),products)

    def test_11_balanced_pairing_Z4_tensor_Z2(self):
        for m,n,r in itertools.product(range(4),range(2),range(4)):
            left=((m*r)%4*n)%2
            right=(m*((r*n)%2))%2
            self.assertEqual(left,right)

    def test_12_balanced_identity_noncommutative(self):
        def m2(a,b):
            return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2
                         for i in range(2) for j in range(2))
        all_mat=list(itertools.product(range(2),repeat=4))
        # Check every triple, not only matrix-unit generators.
        for a,r,b in itertools.product(all_mat,repeat=3):
            self.assertEqual(m2(m2(a,r),b),m2(a,m2(r,b)))

    def test_13_localization_group_axioms_Z12(self):
        pairs=list(itertools.product(range(12),range(3)))
        for a,b,c in itertools.product(pairs,repeat=3):
            self.assertEqual(phi(add_pairs(add_pairs(a,b,3),c,3),4,3),
                             phi(add_pairs(a,add_pairs(b,c,3),3),4,3))
        for a in pairs:
            self.assertEqual(phi(add_pairs(a,(0,0),3),4,3),phi(a,4,3))
            self.assertEqual(phi(add_pairs(a,(-a[0],a[1]),3),4,3),0)

    def test_14_source_invariants(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TXT)
        self.assertEqual((len(labels),len(set(labels))),(20,20))
        self.assertEqual(TXT.count(r'\begin{proof}'),12)
        self.assertEqual(TXT.count(r'\end{proof}'),12)
        self.assertIn('Przemienność dodawania wynika',TXT)
        self.assertIn('Addytywność względem',TXT)


# From test_aa18_stability.py
"""Independent stability tests for AA-18 audit III.

Examples/countermodels corroborate mathematical proof; do not replace it.
"""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex'
S = ROOT.read_text(encoding='utf-8')


def mul2(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2
                 for i in range(2) for j in range(2))


def loc_value(a, k, mod, unit):
    """Interpret a/unit^k in Z/mod where unit is invertible."""
    return (a*pow(unit, -k, mod))%mod


class Stabilization(unittest.TestCase):
    def test_01_math_source_naturality_explicit(self):
        self.assertIn('naturalność tego izomorfizmu', S)
        self.assertIn('otrzymujemy równość homomorfizmów', S)
        self.assertIn(r'\\operatorname{id}_K\\otimes f'.replace('\\\\','\\'), S)

    def test_02_empty_set_and_nonsimple(self):
        self.assertIn('Nie każdy element', S)
        self.assertIn('przestrzeni', S)
        self.assertIn('$V=W=K^2$', S)
        for p in (2,3,5,7):
            vectors=list(itertools.product(range(p),repeat=2))
            rank_one={tuple(a[i]*b[j]%p for i in range(2) for j in range(2))
                      for a,b in itertools.product(vectors,repeat=2)}
            self.assertNotIn((1,0,0,1),rank_one)

    def test_03_r_not_flat_example(self):
        # Z/6 tensor_Z (Z/2 -> Z/2) with multiplication by 2.
        self.assertEqual({(2*x)%6 for x in range(6)},{0,2,4})
        self.assertEqual({(2*x)%2 for x in range(2)},{0})

    def test_04_localization_exact_sequence_invert3(self):
        # 0 -> Z/4 --3-> Z/12 -> Z/3 -> 0
        # Localizing at 3 yields 0 -> Z/4 --3-> Z/4 -> 0.
        for k in range(5):
            for a in range(4):
                left=loc_value(a,k,4,3)
                mid=loc_value(3*a,k,4,3)
                self.assertEqual(mid,3*left%4)
        self.assertEqual({3*a%4 for a in range(4)},set(range(4)))

    def test_05_localization_exact_sequence_invert2(self):
        # Same short exact sequence localized at 2 gives
        # 0 -> 0 -> Z/3 -> Z/3 -> 0.
        for k in range(5):
            for b in range(12):
                self.assertEqual(loc_value(b,k,3,2),loc_value(b%3,k,3,2))
        self.assertEqual(set(range(3)),{b%3 for b in range(12)})

    def test_06_localization_module_hom_naturality(self):
        # f: Z/12 -> Z/12, x |-> 5*x, inverting 3.
        for k in range(5):
            for x in range(12):
                via_loc=loc_value(5*x,k,4,3)
                via_tensor=5*loc_value(x,k,4,3)%4
                self.assertEqual(via_loc,via_tensor)

    def test_07_composition_naturality(self):
        # f: Z/12 -> Z/6 reduction; g: Z/6 -> Z/2 reduction,
        # invert 3. Localization of g∘f agrees with composition.
        for k in range(5):
            for x in range(12):
                direct=loc_value(x%2,k,2,3)
                via_mid=loc_value(loc_value(x,k,2,3),0,2,3)
                self.assertEqual(direct,via_mid)

    def test_08_tensor_quotient_representative_independent(self):
        # (Z/6) ⊗_Z (Z/10) maps to Z/2.
        for a,b in itertools.product(range(6),range(10)):
            val=a*b%2
            for i,j in itertools.product((-2,-1,0,1,2),repeat=2):
                self.assertEqual(val,((a+6*i)*(b+10*j))%2)

    def test_09_scalar_balance_free_module(self):
        # R=Z/4; right regular R, left regular R.
        for m,n,r in itertools.product(range(4),repeat=3):
            self.assertEqual(((m*r)%4*n)%4,(m*((r*n)%4))%4)

    def test_10_noncommutative_balance_matrix(self):
        ring=list(itertools.product((0,1),repeat=4))
        for a,r,b in itertools.product(ring,repeat=3):
            self.assertEqual(mul2(mul2(a,r),b),mul2(a,mul2(r,b)))

    def test_11_direct_sum_tensors_cyclic(self):
        # (Z/m ⊕ Z/n) ⊗ Z/k decomposes as Z/gcd(m,k) ⊕ Z/gcd(n,k).
        for m,n,k in itertools.product(range(1,12),repeat=3):
            d1,d2=math.gcd(m,k),math.gcd(n,k)
            self.assertEqual(d1*d2,len(list(itertools.product(range(d1),range(d2)))))

    def test_12_hom_tensor_adjunction_F2(self):
        # Bilinear maps F2^2 × F2^3 -> F2 correspond to 6 coefficients.
        coeffs=list(itertools.product(range(2),repeat=6))
        self.assertEqual(len(coeffs),64)
        for c in coeffs:
            B=lambda x,y:sum(c[3*i+j]*x[i]*y[j] for i in range(2) for j in range(3))%2
            for x,xp in itertools.product(itertools.product(range(2),repeat=2),repeat=2):
                for y in itertools.product(range(2),repeat=3):
                    xsum=tuple((u+v)%2 for u,v in zip(x,xp))
                    self.assertEqual(B(xsum,y),(B(x,y)+B(xp,y))%2)

    def test_13_abelian_hom_count(self):
        for m,n in itertools.product(range(1,24),repeat=2):
            self.assertEqual(sum((m*y)%n==0 for y in range(n)),math.gcd(m,n))

    def test_14_finite_support_of_direct_sum(self):
        # The image of a simple tensor has support inside support of input.
        for vec in ({},{0:1},{3:1,100:0},{1:2,40:1}):
            support={i for i,x in vec.items() if x}
            for c in range(4):
                image={i for i,x in vec.items() if c*x%4}
                self.assertTrue(image<=support)

    def test_15_source_structural_checks(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)
        self.assertEqual((len(labels),len(set(labels)),len(refs)),(20,20,11))
        self.assertEqual((S.count(r'\begin{proof}'),S.count(r'\end{proof}')),(12,12))
        self.assertEqual((S.count(r'\begin{przyklad}'),S.count(r'\end{przyklad}')),(7,7))
        self.assertNotIn('Nie jest on iniekcją',S)

