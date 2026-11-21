"""Regression tests for AA-06. Exhaustive finite models complement the proofs."""
from itertools import permutations, product
from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/abstract_algebra/06-iloczyny-proste-polproste-i-rozszerzenia-grup.tex"

def mul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    return tuple(a.index(i) for i in range(len(a)))

def closure(gens):
    e=tuple(range(len(gens[0])))
    s={e}
    while True:
        new=s|{mul(x,g) for x in s for g in gens}|{mul(x,inv(g)) for x in s for g in gens}
        if new==s:return frozenset(s)
        s=new

def conj(g,x):
    return mul(mul(g,x),inv(g))

def subgroups(G):
    e=tuple(range(len(G[0])))
    for bits in range(1,1<<len(G)):
        h=frozenset(x for i,x in enumerate(G) if bits>>i&1)
        if e in h and all(mul(x,inv(y)) in h for x in h for y in h):yield h

def quaternion(x,y):
    a,i=x;b,j=y;z=a*b
    if i==0:return(z,j)
    if j==0:return(z,i)
    if i==j:return(-z,0)
    rules={(1,2):(1,3),(2,3):(1,1),(3,1):(1,2),
           (2,1):(-1,3),(3,2):(-1,1),(1,3):(-1,2)}
    sign,k=rules[i,j]
    return (z*sign,k)

class AA06Regression(unittest.TestCase):
    def test_structure_and_forward_references(self):
        txt=CHAPTER.read_text("utf-8")
        labels=re.findall(r"\\label\{([^{}]+)\}",txt)
        refs=set(re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^{}]+)\}",txt))
        registered=set()
        for p in (ROOT/"chapters/pl/abstract_algebra").glob("0[1-6]-*.tex"):
            registered.update(re.findall(r"\\label\{([^{}]+)\}",p.read_text("utf-8")))
        forward={"aa:ch:grupy-abelowe","aa:tw:abelian-tensor-cyclic","aa:ch:module-tensor-product"}
        self.assertEqual(len(labels),21)
        self.assertEqual(len(set(labels)),21)
        self.assertEqual(txt.count(r"\begin{proof}"),11)
        self.assertEqual(txt.count(r"\end{proof}"),11)
        self.assertEqual(refs-registered,forward-registered)

    def test_cyclic_chinese_remainder(self):
        for p,q in ((2,3),(3,5),(2,7),(5,7),(3,11)):
            self.assertEqual(len({(k%p,k%q) for k in range(p*q)}),p*q)
        self.assertEqual(len({(k%2,k%2) for k in range(4)}),2)

    def test_dihedral_internal_semidirect(self):
        r=(1,2,3,0);s=(0,3,2,1)
        G=closure((r,s));N=closure((r,));H=closure((s,))
        self.assertEqual((len(G),len(N),len(H)),(8,4,2))
        self.assertEqual(len(N&H),1)
        self.assertTrue(all(conj(g,x) in N for g in G for x in N))
        self.assertEqual({mul(x,y) for x in N for y in H},set(G))
        self.assertEqual(conj(s,r),inv(r))

    def test_split_action_affine_21(self):
        xs=list(product(range(7),range(3)))
        def prod(x,y):return ((x[0]+pow(2,x[1],7)*y[0])%7,(x[1]+y[1])%3)
        self.assertEqual(len(xs),21)
        self.assertEqual({prod(x,y) for x in xs for y in xs},set(xs))
        for x,y,z in product(xs,repeat=3):
            self.assertEqual(prod(prod(x,y),z),prod(x,prod(y,z)))
        self.assertNotEqual(prod((0,1),(1,0)),prod((1,0),(0,1)))

    def test_quaternion_exact_sequence_not_split(self):
        G=list(product((-1,1),range(4)))
        E=(1,0);Z={E,(-1,0)}
        self.assertEqual({quaternion(x,y) for x in G for y in G},set(G))
        self.assertEqual(len({frozenset(quaternion(x,z) for z in Z) for x in G}),4)
        self.assertEqual({x for x in G if quaternion(x,x)==E},Z)
        self.assertEqual(quaternion((1,1),(1,2)),(1,3))
        self.assertEqual(quaternion((1,2),(1,1)),(-1,3))

    def test_c4_nonsplit(self):
        self.assertEqual({x for x in range(4) if x%2==1},{1,3})
        self.assertTrue(all(2*x%4!=0 for x in (1,3)))

    def test_automorphism_subgroups_for_primes(self):
        for q in (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53):
            factors=[p for p in range(2,q) if (q-1)%p==0
                     and all(p%d!=0 for d in range(2,math.isqrt(p)+1))]
            for p in factors:
                hs={frozenset(pow(x,k,q) for k in range(p)) for x in range(2,q) if pow(x,p,q)==1}
                self.assertEqual(len(hs),1,(p,q))
                self.assertEqual(len(next(iter(hs))),p)

    def test_all_d8_normalizers(self):
        G=tuple(closure(((1,2,3,0),(0,3,2,1))))
        hlist=list(subgroups(G))
        self.assertEqual(len(hlist),10)
        for H in hlist:
            if len(H)==len(G):continue
            ng={g for g in G if {conj(g,x) for x in H}==set(H)}
            self.assertGreater(len(ng),len(H))

    def test_s3_not_nilpotent(self):
        G=tuple(permutations(range(3)))
        hs=[H for H in subgroups(G) if len(H)==2]
        self.assertEqual(len(hs),3)
        for H in hs:
            ng={g for g in G if {conj(g,x) for x in H}==set(H)}
            self.assertEqual(ng,set(H))

    def test_nonabelian_kernel_semidirect(self):
        G=tuple(permutations(range(3)))
        t=(1,0,2)
        def product(x,y):
            a,i=x;b,j=y
            return (mul(a,conj(t,b) if i else b),(i+j)%2)
        from itertools import product as cartesian_product
        elems=list(cartesian_product(G,range(2)))
        self.assertEqual(len({product(x,y) for x in elems for y in elems}),12)
        for x,y,z in cartesian_product(elems,repeat=3):
            self.assertEqual(product(product(x,y),z),product(x,product(y,z)))
        def transform(x):
            a,i=x;return (mul(a,t) if i else a,i)
        self.assertEqual(len({transform(x) for x in elems}),12)

    def test_order_pq_cases(self):
        for p,q in ((2,3),(2,5),(3,7),(2,11),(3,13),(5,11)):
            powers={u for u in range(2,q) if pow(u,p,q)==1}
            self.assertEqual(len(powers),p-1)
            a=next(iter(powers))
            self.assertEqual({pow(a,k,q) for k in range(1,p)},powers)

if __name__=="__main__":
    unittest.main()
