"""Independent AA-22 audit III: Artin fixed fields and normal subgroups.

Pure-Python finite models supplement, rather than replace, general proofs.
"""
import itertools
import re
import unittest
from pathlib import Path

S = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex').read_text(encoding='utf8')

# Represent F_(p^2) as F_p[u], with u^2=q a quadratic non-residue.
def fadd(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def fmul(x,y,p,q):return ((x[0]*y[0]+q*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def fpow(x,n,p,q):
    ans=(1,0)
    while n:
        if n&1:ans=fmul(ans,x,p,q)
        x=fmul(x,x,p,q);n//=2
    return ans

def elems(p):return list(itertools.product(range(p),repeat=2))
def fixed_by_frob(p,q):return [x for x in elems(p) if fpow(x,p,p,q)==x]
def sigma(x,p):return (x[0],(-x[1])%p)

def irreducible_quadratic(a,b,p,q):
    # Minimal polynomial of a+b*u: X^2-2aX+(a^2-qb^2)
    return not any((x*x-2*a*x+a*a-q*b*b)%p==0 for x in range(p))

PERMS=list(itertools.permutations(range(3)))
ID=(0,1,2)
def comp(a,b):return tuple(a[b[i]] for i in range(3))
def subgroup(H):return ID in H and all(comp(a,b) in H for a,b in itertools.product(H,repeat=2))
SUBGROUPS=[frozenset(comb) for k in range(1,7) for comb in itertools.combinations(PERMS,k) if subgroup(comb)]
def inv(a):return next(t for t in PERMS if comp(a,t)==comp(t,a)==ID)
def conjugated(H,g):return frozenset(comp(comp(g,h),inv(g)) for h in H)

class AuditIIIMath(unittest.TestCase):
    def test_01_source_has_explicit_subgroup_types(self):
        self.assertIn(r'H_1,H_2\le\operatorname{Aut}(L)',S)
    def test_02_source_requires_prime(self):
        self.assertIn('Niech $p$ będzie liczbą pierwszą',S)
    def test_03_s3_embedding_is_shown_surjective(self):
        self.assertIn(r'\alpha=(\omega\alpha)/\omega',S)
    def test_04_complex_conjugation_is_well_defined(self):
        self.assertIn(r'\overline{\omega}=\omega^2\in L',S)
    def test_05_labels_and_references(self):
        ls=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual((len(ls),len(set(ls))),(12,12))
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)),21)
    def test_06_cross_reference_embedding_lemma(self):
        self.assertGreaterEqual(S.count(r'\ref{aa:lem:extend-embedding-simple}'),2)
    def test_07_f9_irreducible_modulus(self):
        self.assertNotIn(2, {(a*a)%3 for a in range(3)})
    def test_08_f25_irreducible_modulus(self):
        self.assertNotIn(3, {(a*a)%5 for a in range(5)})
    def test_09_f9_is_field(self):
        for x in elems(3):
            if x!=(0,0):self.assertTrue(any(fmul(x,y,3,2)==(1,0) for y in elems(3)))
    def test_10_f25_is_field(self):
        for x in elems(5):
            if x!=(0,0):self.assertTrue(any(fmul(x,y,5,3)==(1,0) for y in elems(5)))
    def test_11_f9_frobenius_is_conjugation(self):
        self.assertTrue(all(fpow(x,3,3,2)==sigma(x,3) for x in elems(3)))
    def test_12_f25_frobenius_is_conjugation(self):
        self.assertTrue(all(fpow(x,5,5,3)==sigma(x,5) for x in elems(5)))
    def test_13_f9_fixed_field_size(self):
        self.assertEqual(fixed_by_frob(3,2),[(0,0),(1,0),(2,0)])
    def test_14_f25_fixed_field_size(self):
        self.assertEqual(len(fixed_by_frob(5,3)),5)
    def test_15_artin_degree_finite_field(self):
        for p,q in ((3,2),(5,3)):
            self.assertEqual(len(elems(p)),len(fixed_by_frob(p,q))**2)
            self.assertEqual(len(elems(p)),p**2)
            self.assertEqual(len(fixed_by_frob(p,q)),p)
    def test_16_orbit_polynomial_splits_in_field(self):
        for p,q in ((3,2),(5,3)):
            for a,b in elems(p):
                x=(a,b);y=sigma(x,p)
                # (X-x)(X-y) has both coefficients in F_p
                sm=fadd(x,y,p);pr=fmul(x,y,p,q)
                self.assertEqual(sm[1],0)
                self.assertEqual(pr[1],0)
    def test_17_minimal_polynomial_for_nonbase_elements(self):
        for p,q in ((3,2),(5,3)):
            self.assertTrue(all(irreducible_quadratic(a,b,p,q)
                                for a in range(p) for b in range(1,p)))
    def test_18_all_s3_subgroups(self):
        self.assertEqual(len(SUBGROUPS),6)
        self.assertEqual(sorted(len(H) for H in SUBGROUPS),[1,2,2,2,3,6])
    def test_19_normal_s3_subgroups(self):
        normal=[H for H in SUBGROUPS if all(conjugated(H,g)==H for g in PERMS)]
        self.assertEqual(sorted(len(H) for H in normal),[1,3,6])
    def test_20_order_two_subgroups_not_normal(self):
        for H in SUBGROUPS:
            if len(H)==2:self.assertTrue(any(conjugated(H,g)!=H for g in PERMS))
    def test_21_field_degrees_from_subgroups(self):
        self.assertEqual(sorted({6//len(H) for H in SUBGROUPS}),[1,2,3,6])
    def test_22_conjugation_of_subgroups_bijective(self):
        for g in PERMS:
            self.assertEqual({conjugated(H,g) for H in SUBGROUPS},set(SUBGROUPS))

if __name__=='__main__':unittest.main()
