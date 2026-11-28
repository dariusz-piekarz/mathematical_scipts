"""CAT-06 finite-model regression checks, not substitutes for universal proofs."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/06-iloczyny-koprodukty-i-konstrukcje-uniwersalne.tex"

def maps(n,m):
    return list(itertools.product(range(m),repeat=n))

def comp(g,f):
    return tuple(g[i] for i in f)

class CategoryTheoryCh06(unittest.TestCase):
    def test_CAT_06_001_set_product(self):
        for n,a,b in itertools.product(range(4),repeat=3):
            pairs=list(itertools.product(range(a),range(b)))
            p=tuple(x for x,y in pairs)
            q=tuple(y for x,y in pairs)
            images={}
            for h in maps(n,len(pairs)):
                key=(comp(p,h),comp(q,h))
                self.assertNotIn(key,images)
                images[key]=h
            self.assertEqual(set(images),set(itertools.product(maps(n,a),maps(n,b))))

    def test_CAT_06_002_set_coproduct(self):
        for a,b,n in itertools.product(range(4),repeat=3):
            images={}
            for h in maps(a+b,n):
                key=(h[:a],h[a:])
                self.assertNotIn(key,images)
                images[key]=h
            self.assertEqual(set(images),set(itertools.product(maps(a,n),maps(b,n))))

    def test_CAT_06_003_bifunctor(self):
        fs=maps(2,2)
        for f,g,h,k in itertools.product(fs,repeat=4):
            for a,b in itertools.product(range(2),repeat=2):
                self.assertEqual((h[f[a]],k[g[b]]),(comp(h,f)[a],comp(k,g)[b]))
            for tag,x in itertools.product(range(2),repeat=2):
                ff=(f,g)[tag]
                gg=(h,k)[tag]
                self.assertEqual((tag,gg[ff[x]]),(tag,comp(gg,ff)[x]))

    def test_CAT_06_004_group_comparison(self):
        e=(0,1,2)
        s=(1,0,2)
        t=(0,2,1)
        self.assertEqual(comp(s,s),e)
        self.assertEqual(comp(t,t),e)
        self.assertNotEqual(comp(s,t),comp(t,s))
        self.assertNotEqual(comp(comp(s,t),comp(s,t)),e)

    def test_CAT_06_005_module_biproduct(self):
        # F2^a and F2^b; injections and projections of the finite sum.
        for a,b in itertools.product(range(4),repeat=2):
            for v in itertools.product(range(2),repeat=a+b):
                i1=v[:a]+(0,)*b
                i2=(0,)*a+v[a:]
                self.assertEqual(tuple((x+y)%2 for x,y in zip(i1,i2)),v)
                self.assertEqual(i1[a:],(0,)*b)
                self.assertEqual(i2[:a],(0,)*a)

    def test_CAT_06_006_associator_naturality(self):
        for f,g,h in itertools.product(maps(2,2),repeat=3):
            for x,y,z in itertools.product(range(2),repeat=3):
                def assoc(p):
                    (a,b),c=p
                    return a,(b,c)
                def left(p):
                    (a,b),c=p
                    return (f[a],g[b]),h[c]
                def right(p):
                    a,(b,c)=p
                    return f[a],(g[b],h[c])
                self.assertEqual(assoc(left(((x,y),z))),right(assoc(((x,y),z))))

    def test_CAT_06_007_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:produkty","def:produkt","tw:produkt-unique","def:koprodukt",
                      "cat:def:indexed-products","cat:ex:indexed-set-top",
                      "cat:ex:module-indexed","cat:prop:product-functor",
                      "cat:prop:product-coherence","cat:prop:coprod-product"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
