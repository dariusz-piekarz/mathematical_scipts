"""CAT-02 finite-model regressions; the general arguments are in the chapter."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/02-izomorfizmy-monomorfizmy-i-epimorfizmy.tex"

class CategoryTheoryCh02(unittest.TestCase):
    def test_CAT_02_001_group_epi_witness(self):
        # All proper subgroups of S3, including nonnormal subgroups.
        G = list(itertools.permutations(range(3)))
        ident = (0,1,2)
        def mul(a,b):
            return tuple(a[b[i]] for i in range(3))
        X = list(itertools.product(G,range(2)))
        for mask in range(1,1<<len(G)):
            K = {g for i,g in enumerate(G) if mask>>i&1}
            if ident not in K or len(K)==len(G) or any(mul(a,b) not in K for a in K for b in K):
                continue
            def tau(p):
                x,i=p
                return (x,1-i) if x in K else p
            def u(h,p):
                x,i=p
                return mul(h,x),i
            def v(h,p):
                return tau(u(h,tau(p)))
            for a,b,p in itertools.product(G,G,X):
                self.assertEqual(v(mul(a,b),p),v(a,v(b,p)))
            for k,p in itertools.product(K,X):
                self.assertEqual(u(k,p),v(k,p))
            for h in set(G)-K:
                self.assertNotEqual(u(h,(ident,0)),v(h,(ident,0)))

    def test_CAT_02_002_set_regular_and_split(self):
        for n,m in itertools.product(range(4),repeat=2):
            for f in itertools.product(range(m),repeat=n):
                inj=len(set(f))==n
                surj=len(set(f))==m
                for t in itertools.product(range(m),repeat=2):
                    factors=[w for w in itertools.product(range(n),repeat=2)
                             if tuple(f[i] for i in w)==t]
                    if inj:
                        self.assertEqual(len(factors),int(all(i in f for i in t)))
                if surj:
                    for t in itertools.product(range(2),repeat=n):
                        constant=all(f[i]!=f[j] or t[i]==t[j] for i,j in itertools.product(range(n),repeat=2))
                        factors=[w for w in itertools.product(range(2),repeat=m)
                                 if tuple(w[i] for i in f)==t]
                        self.assertEqual(len(factors),int(constant))
                inverses=list(itertools.product(range(n),repeat=m))
                left=any(tuple(g[i] for i in f)==tuple(range(n)) for g in inverses)
                right=any(tuple(f[i] for i in g)==tuple(range(m)) for g in inverses)
                if (inj and right) or (surj and left):
                    self.assertTrue(inj and surj)

    def test_CAT_02_003_top_bimorphism(self):
        discrete={frozenset(),frozenset({0}),frozenset({1}),frozenset({0,1})}
        indiscrete={frozenset(),frozenset({0,1})}
        self.assertTrue(indiscrete <= discrete)
        self.assertFalse(discrete <= indiscrete)

    def test_CAT_02_004_module_quotient(self):
        # Z/n -> Z/n, x -> kx; quotient map detected by reduction mod gcd.
        from math import gcd
        for n in range(1,20):
            for k in range(n):
                d=gcd(n,k)
                image={k*x % n for x in range(n)}
                self.assertEqual(image,{x for x in range(n) if x%d==0})
                if d>1:
                    self.assertNotEqual(1%d,0)
                    self.assertTrue(all((k*x%n)%d==0 for x in range(n)))

    def test_CAT_02_005_source_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:morfizmy","def:mono-epi","tw:set-mono-epi","przyklad:epi-pierscienie",
                      "cat:thm:epi-grp","cat:thm:mono-epi-mod","cat:def:regularne"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
