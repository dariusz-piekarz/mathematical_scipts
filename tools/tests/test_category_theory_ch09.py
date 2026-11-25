"""CAT-09: finite models of representing pairs and naturality."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/09-wlasnosci-uniwersalne-jako-reprezentowanie-funktorow.tex"

def maps(n,m):
    return itertools.product(range(m),repeat=n)

def comp(g,f):
    return tuple(g[i] for i in f)

class CategoryTheoryCh09(unittest.TestCase):
    def test_CAT_09_001_covariant_universal(self):
        for a,b,x in itertools.product(range(3),repeat=3):
            for u in maps(b,a):
                mediators=list(maps(a,x))
                images=[comp(f,u) for f in mediators]
                is_rep=len(images)==len(set(images)) and set(images)==set(maps(b,x))
                if len(set(u))==a and len(u)==a:
                    self.assertTrue(is_rep)
                if x==2:
                    self.assertEqual(is_rep,a==b and len(set(u))==a)

    def test_CAT_09_002_contravariant(self):
        for a,b,x in itertools.product(range(3),repeat=3):
            for u in maps(a,b):
                images=[comp(u,f) for f in maps(x,a)]
                is_rep=len(images)==len(set(images)) and set(images)==set(maps(x,b))
                if x==1:
                    self.assertEqual(is_rep,a==b and len(set(u))==b)
                if a==b and len(set(u))==b:
                    self.assertTrue(is_rep)

    def test_CAT_09_003_pointed_naturality(self):
        for x,y in itertools.product(range(1,5),repeat=2):
            for h in maps(x,y):
                if h[0]!=0:
                    continue
                pointed=[f for f in maps(2,x) if f[0]==0]
                self.assertEqual({f[1] for f in pointed},set(range(x)))
                self.assertEqual(len(pointed),x)
                for f in pointed:
                    self.assertEqual(comp(h,f),(0,h[f[1]]))

    def test_CAT_09_004_free_module(self):
        for m in range(2,6):
            for a,b in maps(2,m):
                candidate=lambda x,y:(a*x+b*y)%m
                for x,y,z,w,r in itertools.product(range(m),repeat=5):
                    self.assertEqual(candidate(x+z,y+w),(candidate(x,y)+candidate(z,w))%m)
                    self.assertEqual(candidate(r*x,r*y),r*candidate(x,y)%m)
                self.assertEqual((candidate(1,0),candidate(0,1)),(a,b))

    def test_CAT_09_005_localization(self):
        # Z/6 localized at powers of 2 is Z/3, with nontrivial kernel.
        S=(1,2,4)
        pairs=list(itertools.product(range(6),S))
        def image(a,s):
            return a*pow(s,-1,3)%3
        for (a,s),(b,t) in itertools.product(pairs,repeat=2):
            self.assertEqual(image(a,s)==image(b,t),any(u*(a*t-b*s)%6==0 for u in S))
            self.assertEqual(image((a*t+b*s)%6,s*t%6),(image(a,s)+image(b,t))%3)
            self.assertEqual(image(a*b%6,s*t%6),image(a,s)*image(b,t)%3)

    def test_CAT_09_006_balanced_tensor(self):
        # Z/2 tensor_Z Z/2 -> Z/m: all biadditive maps by value on (1,1).
        for m in range(1,7):
            expected={(0,0,0,t) for t in range(m) if 2*t%m==0}
            actual=set()
            for b in maps(4,m):
                ev=lambda x,y:b[2*x+y]
                if all(ev((x+z)%2,y)==(ev(x,y)+ev(z,y))%m and
                       ev(x,(y+z)%2)==(ev(x,y)+ev(x,z))%m
                       for x,y,z in itertools.product(range(2),repeat=3)):
                    actual.add(b)
            self.assertEqual(actual,expected)

    def test_CAT_09_007_power_set(self):
        for x,y in itertools.product(range(4),repeat=2):
            for f in maps(y,x):
                for chi in maps(x,2):
                    A={i for i,v in enumerate(chi) if v}
                    pre={j for j in range(y) if f[j] in A}
                    self.assertEqual(comp(chi,f),tuple(int(j in pre) for j in range(y)))
        self.assertEqual(len(list(maps(1,2))),2)
        for n in range(5):
            self.assertEqual(len(list(maps(n,1))),1)

    def test_CAT_09_009_unique_representing_pair(self):
        # Two universal elements of Hom(B,-), or Hom(-,B), are bijections.
        for n in range(5):
            for u,v in itertools.product(itertools.permutations(range(n)),repeat=2):
                cov=[a for a in maps(n,n) if comp(a,u)==v]
                contra=[a for a in maps(n,n) if comp(v,a)==u]
                for candidates in (cov,contra):
                    self.assertEqual(len(candidates),1)
                    self.assertEqual(len(set(candidates[0])),n)

    def test_CAT_09_010_kahler_dual_numbers(self):
        # A = F2[e]/(e^2). Enumerate F2-derivations into the regular module A.
        # In characteristic 2, d(e) is arbitrary; d(0)=d(1)=0.
        def mul(a,b):
            return ((a&1)*(b&1)) | ((((a&1)*(b>>1)+(a>>1)*(b&1))%2)<<1)
        actual=set()
        for d in maps(4,4):
            if d[0]!=0 or d[1]!=0:
                continue
            if all(d[a^b]==(d[a]^d[b]) and
                   d[mul(a,b)]==(mul(a,d[b])^mul(b,d[a]))
                   for a,b in itertools.product(range(4),repeat=2)):
                actual.add(d)
        self.assertEqual(actual,{(0,0,v,v) for v in range(4)})
        # A-linear maps A -> A are precisely multiplication by v.
        linear=set()
        for f in maps(4,4):
            if all(f[a^b]==(f[a]^f[b]) and f[mul(a,b)]==mul(a,f[b])
                   for a,b in itertools.product(range(4),repeat=2)):
                linear.add(f)
        images=[(0,0,f[1],f[1]) for f in linear]
        self.assertEqual(set(images),actual)
        self.assertEqual(len(images),len(actual))

    def test_CAT_09_008_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for name in ("sec:reprezentacja","def:representable","tw:univ-element",
                     "cat:thm:contra-univ-element","cat:thm:representing-unique",
                     "cat:def:elements","cat:prop:elements-representable",
                     "cat:ex:free-module-rep","cat:ex:localization-rep",
                     "cat:ex:tensor-rep","cat:ex:kahler-rep","cat:ex:nonrepresentable"):
            self.assertIn(name,labels)
        stack=[]
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin": stack.append(env)
            else: self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
