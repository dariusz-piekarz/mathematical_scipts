"""AA-17 regressions: Smith form, determinantal ideals and module classification.

Finite examples corroborate proofs, not replace general theorems.
Standard-library only: compatible with the existing CI workflow.
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

SOURCE=(Path(__file__).resolve().parents[2]/
        "chapters/pl/abstract_algebra/17-moduly-nad-dziedzinami-idealow-glownych-i-postac-smitha.tex")
TEXT=SOURCE.read_text(encoding="utf-8")
RNG=random.Random(171126)

def det(a):
    n=len(a)
    if n==0:return 1
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))*
               math.prod(a[i][p[i]] for i in range(n))
               for p in itertools.permutations(range(n)))

def minors_gcd(a,k):
    if k==0:return 1
    nr,nc=len(a),len(a[0])
    if k>min(nr,nc):return 0
    g=0
    for rows in itertools.combinations(range(nr),k):
        for cols in itertools.combinations(range(nc),k):
            g=math.gcd(g,det([[a[i][j] for j in cols] for i in rows]))
    return g

def bezout(a,b):
    aa,bb=abs(a),abs(b)
    old_r,r,old_s,s,old_t,t=aa,bb,1,0,0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s*(1 if a>=0 else -1),old_t*(1 if b>=0 else -1)

def layers(ns,p,k):
    killed=lambda j:math.prod(math.gcd(n,p**j) for n in ns)
    q=killed(k)//killed(k-1)
    h=0
    while q>1:
        assert q%p==0
        q//=p
        h+=1
    return h

class AA17Regression(unittest.TestCase):
    def test_01_unique_labels(self):
        labels=re.findall(r"\\label\{([^}]+)\}",TEXT)
        self.assertEqual((len(labels),len(set(labels))),(16,16))

    def test_02_proofs_examples(self):
        self.assertEqual(TEXT.count(r"\begin{proof}"),9)
        self.assertEqual(TEXT.count(r"\end{proof}"),9)
        self.assertEqual(TEXT.count(r"\begin{przyklad}"),4)
        self.assertEqual(TEXT.count(r"\end{przyklad}"),4)

    def test_03_refs(self):
        self.assertEqual(len(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",TEXT)),11)

    def test_04_general_pid_smith(self):
        self.assertIn("odwracalne zmiany baz",TEXT)
        self.assertIn("nie zakładamy, że każdą taką",TEXT)
        self.assertIn(r"\label{aa:lem:pid-acc17}",TEXT)

    def test_05_bezout_signed_zero_cases(self):
        for a,b in itertools.product(range(-16,17),repeat=2):
            if a==b==0:continue
            d,u,v=bezout(a,b)
            self.assertEqual(d,math.gcd(a,b))
            self.assertEqual(u*a+v*b,d)

    def test_06_bezout_2x2_unimodularity(self):
        for a,b in itertools.product(range(-12,13),repeat=2):
            if a==b==0:continue
            d,u,v=bezout(a,b)
            a1,b1=a//d,b//d
            self.assertEqual(u*a1+v*b1,1)
            self.assertEqual((-b1)*a+a1*b,0)

    def test_07_determinantal_divisibility(self):
        for nr,nc in ((2,2),(3,3),(2,3),(3,2)):
            for _ in range(50):
                a=[[RNG.randint(-5,5) for _ in range(nc)] for _ in range(nr)]
                ds=[minors_gcd(a,k) for k in range(min(nr,nc)+1)]
                nonzero=[d for d in ds if d]
                self.assertTrue(all(y%x==0 for x,y in zip(nonzero,nonzero[1:])))

    def test_08_row_operations_preserve_minors(self):
        for _ in range(50):
            a=[[RNG.randint(-9,9) for _ in range(3)] for _ in range(3)]
            b=[row[:] for row in a]
            q=RNG.randint(-6,6)
            b[1]=[x+q*y for x,y in zip(b[1],b[0])]
            self.assertEqual([minors_gcd(a,k) for k in (1,2,3)],
                             [minors_gcd(b,k) for k in (1,2,3)])

    def test_09_column_operations_preserve_minors(self):
        for _ in range(50):
            a=[[RNG.randint(-7,7) for _ in range(3)] for _ in range(3)]
            b=[row[:] for row in a]
            q=RNG.randint(-6,6)
            for row in b:row[2]+=q*row[0]
            self.assertEqual([minors_gcd(a,k) for k in (1,2,3)],
                             [minors_gcd(b,k) for k in (1,2,3)])

    def test_10_first_integer_example(self):
        a=[[4,6],[10,14]]
        self.assertEqual((minors_gcd(a,1),minors_gcd(a,2)),(2,4))

    def test_11_second_integer_example(self):
        a=[[6,9],[0,15]]
        self.assertEqual((minors_gcd(a,1),minors_gcd(a,2)),(3,90))

    def test_12_singular_edge_cases(self):
        self.assertEqual(minors_gcd([[0,0],[0,0]],2),0)
        self.assertEqual(minors_gcd([[2,4],[3,6]],1),1)
        self.assertEqual(minors_gcd([[2,4],[3,6]],2),0)

    def test_13_prime_power_torsion_layers(self):
        for p in (2,3,5):
            for e in range(1,6):
                for k in range(1,e+3):
                    self.assertEqual(layers([p**e],p,k),int(k<=e))

    def test_14_coprime_torsion_vanishes(self):
        for p in (2,3,5):
            for n in (7,11,13,17,19):
                if n%p:
                    for k in range(1,5):
                        self.assertEqual(layers([n],p,k),0)

    def test_15_reconstruct_exponents(self):
        for p,es in ((2,[1,1,2,4]),(3,[1,2,2]),(5,[3])):
            ns=[p**e for e in es]
            h={k:layers(ns,p,k) for k in range(1,max(es)+2)}
            got=[k for k in range(1,max(es)+1)
                 for _ in range(h[k]-h.get(k+1,0))]
            self.assertEqual(got,sorted(es))

    def test_16_six_abelian_groups_order_72(self):
        groups=[[72],[3,24],[2,36],[6,12],[2,2,18],[2,6,6]]
        self.assertEqual(len({tuple(g) for g in groups}),6)
        for ns in groups:
            self.assertEqual(math.prod(ns),72)
            self.assertTrue(all(y%x==0 for x,y in zip(ns,ns[1:])))
        profiles=[tuple(layers(ns,p,k) for p in (2,3) for k in range(1,5))
                  for ns in groups]
        self.assertEqual(len(set(profiles)),6)

    def test_17_Z_t_and_zero_torsion(self):
        self.assertIn("$(2,t)=(f)$",TEXT)
        self.assertIn(r"\mathbb Z[t]\to\mathbb Z/2\mathbb Z",TEXT)
        self.assertIn("Jeśli $T(M)=0$, to $t=0$",TEXT)

    def test_18_acc_termination(self):
        self.assertIn("ściśle rosnący ideał główny",TEXT)
        self.assertIn(r"Lemat~\ref{aa:lem:pid-acc17}",TEXT)

if __name__=="__main__":
    unittest.main()
