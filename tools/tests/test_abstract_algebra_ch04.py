"""Independent finite-group regression models for the first audit of AA-04.

Finite checks test examples and invariants; they are NOT substitutions for proofs.
"""
from collections import defaultdict
from itertools import permutations, product
from math import comb, gcd
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[2]
WD=ROOT/'chapters/pl/abstract_algebra'
CH4=WD/'04-twierdzenia-cauchyego-i-sylowa.tex'

def perm_mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def perm_inv(a):return tuple(a.index(i) for i in range(len(a)))
def even(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

class FiniteGroup:
    def __init__(self, elements, multiply, unit):
        self.elements=tuple(elements);self.mul=multiply;self.e=unit
        self.order=len(self.elements)
        self.inverses={x:next(y for y in self.elements if multiply(x,y)==unit and multiply(y,x)==unit) for x in self.elements}
    def inv(self,x):return self.inverses[x]
    def subgroup(self,gens):
        s={self.e}|set(gens)
        while True:
            t=s|{self.mul(a,b) for a in s for b in s}|{self.inv(a) for a in s}
            if s==t:return frozenset(s)
            s=t
    def all_subgroups(self):
        seen={frozenset((self.e,))};frontier=list(seen)
        while frontier:
            h=frontier.pop()
            for g in self.elements:
                if g in h:continue
                k=self.subgroup((*h,g))
                if k not in seen:seen.add(k);frontier.append(k)
        return sorted(seen,key=lambda h:(len(h),repr(h)))
    def conjugate(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def normal(self,h):return all(self.conjugate(g,x) in h for g in self.elements for x in h)
    def sylows(self,p):
        a=1
        while self.order%(a*p)==0:a*=p
        return [h for h in self.all_subgroups() if len(h)==a]

def symmetric(n):
    e=tuple(range(n))
    return FiniteGroup(permutations(range(n)),perm_mul,e)

def alternating(n):
    e=tuple(range(n))
    return FiniteGroup((p for p in permutations(range(n)) if even(p)),perm_mul,e)

def affine(p,scalings):
    els=[(a,b) for a in scalings for b in range(p)]
    return FiniteGroup(els,lambda x,y:(x[0]*y[0]%p,(x[0]*y[1]+x[1])%p),(1,0))

class SylowAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s3=symmetric(3);cls.s4=symmetric(4);cls.a4=alternating(4)
        cls.aff21=affine(7,(1,2,4))
        cls.groups=(cls.s3,cls.s4,cls.a4,cls.aff21)

    def test_all_sylow_counts(self):
        expected={(6,2):3,(6,3):1,(24,2):3,(24,3):4,(12,2):1,(12,3):4,(21,3):7,(21,7):1}
        for group in self.groups:
            for p in (2,3,7):
                if group.order%p:continue
                count=len(group.sylows(p))
                self.assertEqual(count,expected[(group.order,p)])
                self.assertEqual(count%p,1)
                a=1
                while group.order%(a*p)==0:a*=p
                self.assertEqual((group.order//a)%count,0)

    def test_sylow_conjugacy(self):
        for group in self.groups:
            for p in (2,3,7):
                if group.order%p:continue
                sylows=group.sylows(p)
                for p1 in sylows:
                    self.assertEqual({frozenset(group.conjugate(g,x) for x in p1) for g in group.elements},set(sylows))

    def test_sylow3_single_fixed_point(self):
        for group in self.groups:
            for p in (2,3,7):
                if group.order%p:continue
                for psub in group.sylows(p):
                    fixed=[qsub for qsub in group.sylows(p) if all(frozenset(group.conjugate(g,x) for x in qsub)==qsub for g in psub)]
                    self.assertEqual(fixed,[psub])

    def test_S4_three_pair_stabilizers_distinct(self):
        g=self.s4
        parts=[frozenset((frozenset((0,1)),frozenset((2,3)))),
               frozenset((frozenset((0,2)),frozenset((1,3)))),
               frozenset((frozenset((0,3)),frozenset((1,2))))]
        def action(a,part):return frozenset(frozenset(a[x] for x in pair) for pair in part)
        hs=[frozenset(a for a in g.elements if action(a,part)==part) for part in parts]
        self.assertEqual([len(x) for x in hs],[8,8,8]);self.assertEqual(len(set(hs)),3)
        for i,(a,b) in enumerate(((0,1),(0,2),(0,3))):
            t=list(range(4));t[a],t[b]=t[b],t[a];t=tuple(t)
            self.assertEqual([t in h for h in hs],[j==i for j in range(3)])

    def test_S4_A4_element_counts(self):
        self.assertEqual(len(self.s4.sylows(3)),4)
        self.assertEqual(len(self.a4.sylows(3)),4)
        self.assertEqual(len(self.a4.sylows(2)),1)
        v=self.a4.sylows(2)[0]
        self.assertTrue(all(self.a4.mul(x,x)==self.a4.e for x in v))
        self.assertTrue(self.a4.normal(v))
        self.assertFalse(any(len(h)==6 for h in self.a4.all_subgroups()))

    def test_cauchy_noncommutative_fixed_tuple_counts(self):
        for group in (self.s3,self.s4,self.a4):
            for p in (2,3):
                if group.order%p:continue
                fixed=[g for g in group.elements if self_power(group,g,p)==group.e]
                self.assertEqual(len(fixed)%p,0)
                self.assertGreaterEqual(len(fixed),p)

    def test_binomial_congruence(self):
        for p in (2,3,5,7):
            for a in range(4):
                q=p**a
                for m in range(1,35):
                    if m%p:
                        self.assertEqual(comb(q*m,q)%p,m%p)

    def test_affine_21_structure(self):
        g=self.aff21
        self.assertEqual(g.order,21)
        self.assertNotEqual(g.mul((2,0),(1,1)),g.mul((1,1),(2,0)))
        t=frozenset((1,b) for b in range(7))
        self.assertTrue(g.normal(t));self.assertEqual(len(t),7)
        h=g.subgroup(((2,0),))
        self.assertEqual(len(h),3);self.assertFalse(g.normal(h))
        self.assertEqual(len(g.sylows(3)),7)

    def test_Cauchy_action_orbit_count_nonabelian(self):
        for group in (self.s3,self.s4,self.a4):
            for p in (2,3):
                if group.order%p:continue
                xset=set()
                for head in product(group.elements,repeat=p-1):
                    total=group.e
                    for el in head:total=group.mul(total,el)
                    xset.add(head+(group.inv(total),))
                self.assertEqual(len(xset),group.order**(p-1))
                fixed={x for x in xset if x[1:]+x[:1]==x}
                self.assertEqual(len(fixed)%p,0)
                unseen=set(xset)
                while unseen:
                    t=next(iter(unseen)); orbit=set(); curr=t
                    while curr not in orbit:
                        self.assertIn(curr,xset)
                        orbit.add(curr)
                        curr=curr[1:]+curr[:1]
                    self.assertIn(len(orbit),(1,p))
                    unseen-=orbit
                self.assertEqual(len(fixed),sum(self_power(group,g,p)==group.e for g in group.elements))

    def test_Sylow_first_action_on_subsets(self):
        from itertools import combinations
        for group,p in ((self.s3,2),(self.s3,3),(self.a4,2),(self.a4,3)):
            r=1
            while group.order%(r*p)==0:r*=p
            subsets=[frozenset(x) for x in combinations(group.elements,r)]
            self.assertNotEqual(len(subsets)%p,0)
            orbit_sizes=set()
            stabilizers=[]
            for a in subsets:
                stabilizer=frozenset(g for g in group.elements
                   if frozenset(group.mul(g,x) for x in a)==a)
                orbit_size=group.order//len(stabilizer)
                orbit_sizes.add(orbit_size)
                if orbit_size%p:stabilizers.append(stabilizer)
            self.assertTrue(stabilizers)
            self.assertTrue(all(len(h)==r for h in stabilizers))

    def test_Sylow_second_contains_every_p_subgroup(self):
        for group in self.groups:
            subgroups=group.all_subgroups()
            for p in (2,3,7):
                if group.order%p:continue
                sylows=group.sylows(p)
                for h in subgroups:
                    if len(h)>1 and is_prime_power(len(h),p):
                        self.assertTrue(any(h <= psub for psub in sylows))

    def test_normalizer_index_counts(self):
        for group in self.groups:
            for p in (2,3,7):
                if group.order%p:continue
                sylows=group.sylows(p)
                for psub in sylows:
                    norm=frozenset(g for g in group.elements
                      if frozenset(group.conjugate(g,x) for x in psub)==psub)
                    self.assertEqual(len(sylows),group.order//len(norm))
                    self.assertEqual(group.order//len(psub),len(sylows)*(len(norm)//len(psub)))

    def test_index_smallest_prime(self):
        for group in self.groups:
            smallest=next(p for p in range(2,group.order+1) if group.order%p==0)
            for h in group.all_subgroups():
                if group.order//len(h)==smallest:
                    self.assertTrue(group.normal(h))

    def test_labels_references_and_proofs(self):
        s=CH4.read_text()
        labels=re.findall(r'\\label\{([^}]+)\}',s)
        self.assertEqual(len(labels),18)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertTrue(all(x.startswith('aa:') for x in labels))
        self.assertEqual(s.count('\\begin{proof}'),12)
        self.assertEqual(s.count('\\begin{proof}'),s.count('\\end{proof}'))
        assert_files=[WD/'01-grupy-podgrupy-i-grupy-cykliczne.tex',WD/'02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex',WD/'03-dzialania-grup-orbity-i-rownanie-klas.tex',CH4]
        all_labels=set().union(*(set(re.findall(r'\\label\{([^}]+)\}',f.read_text())) for f in assert_files))
        refs=set(re.findall(r'\\(?:ref|eqref|pageref|autoref|nameref)\{([^}]+)\}',s))
        self.assertTrue(refs<=all_labels,repr(refs-all_labels))

def is_prime_power(n,p):
    if n<1:return False
    while n%p==0 and n>1:n//=p
    return n==1

def self_power(G,x,n):
    y=G.e
    for _ in range(n):y=G.mul(y,x)
    return y

if __name__=='__main__':unittest.main(verbosity=2)


"""Additional independent edge-case checks for AA-04 audit II."""
import unittest

from math import comb
from itertools import product


def cyclic(n):
    return FiniteGroup(range(n),lambda a,b:(a+b)%n,0)


def dihedral(n):
    # element (a,b) represents r^a s^b, srs = r^-1
    return FiniteGroup([(a,b) for a in range(n) for b in range(2)],
                       lambda x,y: ((x[0]+(-1 if x[1] else 1)*y[0])%n,(x[1]+y[1])%2), (0,0))

class EdgeCases(unittest.TestCase):
    def test_p_does_not_divide_group_order(self):
        for grp in (cyclic(1),cyclic(3),symmetric(3),dihedral(4)):
            for p in (5,7,11):
                if grp.order%p:continue
                self.assertEqual(grp.sylows(p),[frozenset((grp.e,))])

    def test_p_groups_unique_sylow_including_nonabelian(self):
        for grp,p in ((cyclic(8),2),(dihedral(4),2),(cyclic(9),3),(cyclic(1),2)):
            self.assertEqual(grp.sylows(p),[frozenset(grp.elements)])

    def test_fixed_point_count_mod_p(self):
        # A p-group acting by conjugation on a p-subgroup's Sylow orbit.
        for grp in (dihedral(4),dihedral(5),symmetric(3)):
            for p in (2,3,5):
                if grp.order%p:continue
                ps=grp.sylows(p)
                for P in ps:
                    fixed=[Q for Q in ps if all(frozenset(grp.conjugate(u,x) for x in Q)==Q for u in P)]
                    self.assertEqual(fixed,[P])
                    self.assertEqual(len(ps)%p,1)

    def test_distinct_order21_sylow3(self):
        grp=affine(7,(1,2,4))
        ps=grp.sylows(3)
        self.assertEqual(len(ps),7)
        self.assertEqual(len(set(ps)),7)
        self.assertEqual([len(ps),len(grp.sylows(7))],[7,1])

    def test_binomial_a_zero_and_high_prime(self):
        for p in (2,3,5,7,11,13):
            for a in range(3):
                for m in range(1,20):
                    if m%p: self.assertEqual(comb(p**a*m,p**a)%p,m%p)

    def test_smallest_prime_index_group_action(self):
        for grp in (dihedral(4),dihedral(5),cyclic(12),symmetric(3),alternating(4)):
            smallest=next(p for p in range(2,grp.order+1) if grp.order%p==0)
            for h in grp.all_subgroups():
                if grp.order//len(h)==smallest:
                    self.assertTrue(grp.normal(h))


