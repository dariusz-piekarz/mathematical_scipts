"""Independent regressions for abstract algebra AA-02; models are not proofs."""
from itertools import permutations, combinations, product
from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AA01 = (ROOT / "chapters/pl/abstract_algebra/01-grupy-podgrupy-i-grupy-cykliczne.tex").read_text("utf-8")
AA02 = (ROOT / "chapters/pl/abstract_algebra/02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex").read_text("utf-8")

def perms(n):
    return tuple(permutations(range(n)))

def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    return tuple(p.index(i) for i in range(len(p)))

def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 == 0

def subgroups(g):
    ident=tuple(range(len(g[0])))
    result=[]
    for bits in range(1, 1<<len(g)):
        h=frozenset(x for i,x in enumerate(g) if bits>>i&1)
        if ident in h and all(mul(x, inv(y)) in h for x in h for y in h):
            result.append(h)
    return result

def left(g,h):
    return frozenset(mul(g,x) for x in h)

def right(g,h):
    return frozenset(mul(x,g) for x in h)

class AA02Regression(unittest.TestCase):
    def test_structure_and_references(self):
        labels=re.findall(r"\\label\{([^{}]+)\}", AA02)
        all_labels=set(labels)|set(re.findall(r"\\label\{([^{}]+)\}",AA01))
        refs=re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^{}]+)\}", AA02)
        self.assertEqual(len(labels),33)
        self.assertEqual(len(set(labels)),33)
        self.assertTrue(all(l.startswith("aa:") for l in labels))
        self.assertTrue(set(refs).issubset(all_labels))
        self.assertEqual(AA02.count(r"\begin{proof}"),23)
        self.assertEqual(AA02.count(r"\end{proof}"),23)

    def test_s3_cosets_normality_and_quotient(self):
        g=perms(3)
        hs=subgroups(g)
        self.assertEqual(sorted(map(len,hs)),[1,2,2,2,3,6])
        for h in hs:
            lc={left(x,h) for x in g}; rc={right(x,h) for x in g}
            self.assertEqual(sum(map(len,lc)),6)
            self.assertEqual({frozenset(inv(x) for x in c) for c in lc},rc)
            normal=all(left(x,h)==right(x,h) for x in g)
            well_defined=all(len({left(mul(a,b),h) for a in c for b in d})==1
                             for c in lc for d in lc)
            self.assertEqual(normal,well_defined)

    def test_second_and_third_isomorphism_in_s3(self):
        g=perms(3)
        hs=subgroups(g)
        ns=[h for h in hs if all(left(x,h)==right(x,h) for x in g)]
        for h,n in product(hs,ns):
            hn=frozenset(mul(x,y) for x in h for y in n)
            self.assertIn(hn,hs)
            self.assertEqual(len(h)*len(n),len(hn)*len(h & n))
        for n,m in product(ns,repeat=2):
            if n<=m:
                self.assertEqual((len(g)//len(n))//(len(m)//len(n)),len(g)//len(m))

    def test_euler_fermat_and_pseudoprimality(self):
        from fractions import Fraction
        for n in range(2,101):
            primes=[p for p in range(2,n+1) if n%p==0 and
                    all(p%d for d in range(2,math.isqrt(p)+1))]
            phi=sum(math.gcd(a,n)==1 for a in range(1,n+1))
            predicted=Fraction(n)
            for p in primes:
                predicted*=Fraction(p-1,p)
            self.assertEqual(phi,predicted)
            for a in range(n):
                if math.gcd(a,n)==1:
                    self.assertEqual(pow(a,phi,n),1)
        self.assertEqual(pow(2,340,341),1)
        self.assertEqual(pow(3,8,15),6)

    def test_a4_no_subgroup_of_order_six(self):
        a4=tuple(x for x in perms(4) if even(x))
        self.assertEqual(len(a4),12)
        e=(0,1,2,3)
        for trial in combinations(a4,6):
            h=set(trial)
            if e in h:
                self.assertFalse(all(mul(x,inv(y)) in h for x in h for y in h))

    def test_cayley_and_s3_abelianization(self):
        g=perms(3); e=(0,1,2)
        self.assertEqual(len({tuple(mul(x,y) for y in g) for x in g}),6)
        comm={mul(mul(mul(x,y),inv(x)),inv(y)) for x in g for y in g}
        a3={x for x in g if even(x)}
        self.assertEqual(comm,a3)
        self.assertEqual(len({left(x,a3) for x in g}),2)

    def test_klein_four_kernel_of_s4_partition_action(self):
        g=perms(4)
        partitions=[frozenset((frozenset((0,1)),frozenset((2,3)))),
                    frozenset((frozenset((0,2)),frozenset((1,3)))),
                    frozenset((frozenset((0,3)),frozenset((1,2))))]
        def action(x):
            return tuple(partitions.index(frozenset(
                frozenset(x[a] for a in part) for part in split)) for split in partitions)
        image={action(x) for x in g}
        kernel={x for x in g if action(x)==(0,1,2)}
        self.assertEqual((len(image),len(kernel)),(6,4))
        for x,y in product(g,repeat=2):
            self.assertEqual(action(mul(x,y)),mul(action(x),action(y)))

if __name__=="__main__":
    unittest.main()
