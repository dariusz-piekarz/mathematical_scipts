"""Independent AA-34 audit II: group enumeration, coefficient specializations,
resultant/discriminant identities and Galois examples.
Run: python AA-34-audyt-II-testy-niezalezne.py -v
No dependency on first-audit test code or its computed results.
"""
from __future__ import annotations
import itertools
import math
import random
import re
import unittest
from pathlib import Path
import sympy as sp

BASE = Path(__file__).resolve().parent
SOURCE = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/34-rezolwenta-szescienna-i-grupy-galois-stopnia-czwartego.tex'
x,y = sp.symbols('x y')
R1,R2,R3,R4 = sp.symbols('R1 R2 R3 R4')
ID = (0,1,2,3)
S4 = tuple(itertools.permutations(range(4)))
PARTITIONS = (
 ((0,1),(2,3)),
 ((0,2),(1,3)),
 ((0,3),(1,2)),
)

def pcompose(p,q):
    return tuple(p[q[i]] for i in range(4))

def on_partitions(p):
    def canonical(a):
        return tuple(sorted(tuple(sorted(pair)) for pair in a))
    return tuple([canonical(z) for z in PARTITIONS].index(canonical(tuple(tuple(p[i] for i in pair) for pair in ptn))) for ptn in PARTITIONS)

def group_generated(gens):
    out={ID}; pending=[ID]
    while pending:
        p=pending.pop()
        for q in gens:
            a=pcompose(p,q)
            if a not in out:
                out.add(a);pending.append(a)
    return frozenset(out)

def all_subgroups():
    subs={frozenset([ID])}; queue=[frozenset([ID])]
    while queue:
        h=queue.pop()
        for p in S4:
            if p in h:continue
            new=group_generated(tuple(h)+(p,))
            if new not in subs:subs.add(new);queue.append(new)
    return subs

def orbit_sizes(group, action=None, degree=4):
    to_perm = action or (lambda v:v)
    seen=set();orbits=[]
    for i in range(degree):
        if i in seen:continue
        orb={to_perm(g)[i] for g in group}
        seen.update(orb);orbits.append(len(orb))
    return tuple(sorted(orbits))

def resolvent(aa,bb,cc,dd):
    return y**3-bb*y**2+(aa*cc-4*dd)*y-(aa**2*dd+cc**2-4*bb*dd)

class GroupChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subgroups=all_subgroups()
        cls.transitive=[g for g in cls.subgroups if orbit_sizes(g)==(4,)]

    def test_all_subgroups_count(self):
        self.assertEqual(len(self.subgroups),30)

    def test_transitive_subgroup_count(self):
        self.assertEqual(len(self.transitive),9)

    def test_transitive_isomorphism_order_image_pairs(self):
        expected={(4,1),(4,2),(8,2),(12,3),(24,6)}
        found=set()
        for h in self.transitive:
            n=len(h); m=len({on_partitions(g) for g in h})
            self.assertIn((n,m),expected)
            found.add((n,m))
        self.assertEqual(found,expected)

    def test_orbits_match_resolvent_factorization(self):
        for h in self.transitive:
            size=orbit_sizes(h,on_partitions,3)
            kind=len({on_partitions(v) for v in h})
            expect={1:(1,1,1),2:(1,2),3:(3,),6:(3,)}[kind]
            self.assertEqual(size,expect)

    def test_image_kernels_are_normal(self):
        for h in self.subgroups:
            kernel={v for v in h if on_partitions(v)==(0,1,2)}
            self.assertEqual(len(h)%len(kernel),0)
            for g in h:
                inverse=tuple(g.index(i) for i in range(4))
                for k in kernel:
                    self.assertIn(pcompose(g,pcompose(k,inverse)),kernel)

    def test_action_quotient_sizes(self):
        for h in self.subgroups:
            image={on_partitions(v) for v in h}
            kernel={v for v in h if on_partitions(v)==(0,1,2)}
            self.assertEqual(len(image)*len(kernel),len(h))

    def test_every_transitive_group_orders(self):
        self.assertEqual({len(g) for g in self.transitive},{4,8,12,24})

    def test_even_and_odd_images(self):
        # The only transitive index-two subgroup of S4 is A4.
        h12=[g for g in self.transitive if len(g)==12]
        self.assertEqual(len(h12),1)
        def sign(p):
            inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
            return (-1)**inversions
        self.assertTrue(all(sign(p)==1 for p in h12[0]))

class PolynomialChecks(unittest.TestCase):
    def test_difference_factorization(self):
        a,b,c,d=R1,R2,R3,R4
        betas=[a*b+c*d,a*c+b*d,a*d+b*c]
        expected=[(a-d)*(b-c),(a-c)*(b-d),(a-b)*(c-d)]
        for (i,j),rhs in zip(((0,1),(0,2),(1,2)),expected):
            self.assertEqual(sp.expand(betas[i]-betas[j]-rhs),0)

    def test_resultant_discriminant_generic(self):
        a,b,c,d=sp.symbols('a b c d')
        f=x**4+a*x**3+b*x**2+c*x+d
        q=resolvent(a,b,c,d)
        self.assertEqual(sp.expand(sp.discriminant(f,x)-sp.discriminant(q,y)),0)

    def test_generic_coefficient_symbolic_vieta(self):
        p=(x-R1)*(x-R2)*(x-R3)*(x-R4)
        aa,bb,cc,dd=sp.Poly(sp.expand(p),x).all_coeffs()[1:]
        q=sp.expand(resolvent(aa,bb,cc,dd))
        ts=[R1*R2+R3*R4,R1*R3+R2*R4,R1*R4+R2*R3]
        self.assertEqual(sp.expand(q-sp.prod(y-t for t in ts)),0)

    def test_discriminant_specialization_char2(self):
        for aa,bb,cc,dd in itertools.product((0,1),repeat=4):
            f=x**4+aa*x**3+bb*x**2+cc*x+dd
            q=resolvent(aa,bb,cc,dd)
            self.assertEqual(int(sp.discriminant(f,x)-sp.discriminant(q,y))%2,0)

    def test_discriminant_specialization_char3(self):
        for aa,bb,cc,dd in itertools.product((0,1,2),repeat=4):
            f=x**4+aa*x**3+bb*x**2+cc*x+dd
            q=resolvent(aa,bb,cc,dd)
            self.assertEqual(int(sp.discriminant(f,x)-sp.discriminant(q,y))%3,0)

    def test_82_or_125_cycles_not_generic_assumption(self):
        f=x**4-3*x**3+3*x**2+2*x+1
        q=resolvent(-3,3,2,1)
        self.assertEqual(sp.expand(q),y**3-3*y**2-10*y-1)
        self.assertEqual(sp.discriminant(f,x),4225)
        self.assertTrue(sp.Poly(f,x,domain='QQ').is_irreducible)
        self.assertTrue(sp.Poly(q,y,domain='QQ').is_irreducible)
        G,_=sp.polys.numberfields.galois_group(f,x)
        self.assertEqual(G.order(),12)
        self.assertTrue(G.is_subgroup(sp.combinatorics.named_groups.AlternatingGroup(4)))

    def test_reducible_case_discriminant_identity(self):
        for poly in ((x-1)**4, x*(x-1)**3, (x**2+1)**2, x**4):
            aa,bb,cc,dd=sp.Poly(poly,x).all_coeffs()[1:]
            self.assertEqual(sp.discriminant(poly,x),sp.discriminant(resolvent(aa,bb,cc,dd),y))

    def test_cyclic_case(self):
        poly=x**4+x**3+x**2+x+1
        self.assertEqual(sp.factor(resolvent(1,1,1,1)),(y-2)*(y**2+y-1))
        G,_=sp.polys.numberfields.galois_group(poly,x)
        self.assertEqual(G.order(),4)
        self.assertTrue(G.is_cyclic)

    def test_dihedral_case(self):
        poly=x**4-2
        G,_=sp.polys.numberfields.galois_group(poly,x)
        self.assertEqual(G.order(),8)
        self.assertEqual(sp.factor(resolvent(0,0,0,-2)),y*(y**2+8))

    def test_klein_case(self):
        poly=x**4-10*x**2+1
        G,_=sp.polys.numberfields.galois_group(poly,x)
        self.assertEqual(G.order(),4)
        self.assertFalse(G.is_cyclic)
        self.assertEqual(sp.factor(resolvent(0,-10,0,1)),(y+10)*(y-2)*(y+2))

    def test_s4_case(self):
        poly=x**4-x-1
        G,_=sp.polys.numberfields.galois_group(poly,x)
        self.assertEqual(G.order(),24)
        self.assertTrue(sp.Poly(resolvent(0,0,-1,-1),y).is_irreducible)
        self.assertEqual(sp.discriminant(poly,x),-283)

class SourceChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src=SOURCE.read_text(encoding='utf8')
    def test_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',self.src)
        self.assertEqual(len(labels),14)
        self.assertEqual(len(set(labels)),len(labels))
    def test_no_new_proof_gap(self):
        self.assertIn('G=V_4',self.src)
        self.assertIn(r'\operatorname{disc}(r_f)=\operatorname{disc}(f)',self.src)
    def test_four_named_examples(self):
        for n in ('c4','s4','v4','klein'):
            self.assertIn('aa:prz:quartic-'+n,self.src)
    def test_no_accidental_latex_escape(self):
        self.assertNotIn('\\\n e',self.src)
    def test_no_duplicate_new_refs(self):
        for tag in ('aa:wn:quartic-resolvent-disc','aa:wn:quartic-resolvent-factorization'):
            self.assertEqual(self.src.count(r'\label{'+tag+'}'),1)

if __name__=='__main__':
    unittest.main(verbosity=2)
