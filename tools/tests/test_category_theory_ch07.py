"""CAT-07 regressions for finite models of universal constructions."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/07-equalizatory-koequalizatory-i-kwadraty-kartezjanskie.tex"

def maps(n,m):
    return list(itertools.product(range(m),repeat=n))

def comp(g,f):
    return tuple(g[i] for i in f)

def quotient(n,pairs):
    labels=list(range(n))
    for a,b in pairs:
        old,new=labels[a],labels[b]
        labels=[new if x==old else x for x in labels]
    return tuple(sorted(set(labels)).index(x) for x in labels)

class CategoryTheoryCh07(unittest.TestCase):
    def test_CAT_07_001_equalizer(self):
        for a,b,n in itertools.product(range(3),repeat=3):
            for f,g in itertools.product(maps(a,b),repeat=2):
                e=tuple(i for i in range(a) if f[i]==g[i])
                self.assertEqual({comp(e,h) for h in maps(n,len(e))},
                                 {u for u in maps(n,a) if comp(f,u)==comp(g,u)})
                self.assertEqual(len({comp(e,h) for h in maps(n,len(e))}),len(maps(n,len(e))))

    def test_CAT_07_002_coequalizer(self):
        for a,b,n in itertools.product(range(3),repeat=3):
            for f,g in itertools.product(maps(a,b),repeat=2):
                q=quotient(b,zip(f,g))
                self.assertEqual(comp(q,f),comp(q,g))
                hs=maps(len(set(q)),n)
                self.assertEqual({comp(h,q) for h in hs},
                                 {u for u in maps(b,n) if comp(u,f)==comp(u,g)})
                self.assertEqual(len({comp(h,q) for h in hs}),len(hs))

    def test_CAT_07_003_pullback_pasting(self):
        for x,y,z,r in itertools.product(range(3),repeat=4):
            for u,v,w in itertools.product(maps(x,y),maps(y,z),maps(r,z)):
                q=[(j,k) for j,k in itertools.product(range(y),range(r)) if v[j]==w[k]]
                p=[(i,k) for i,(j,k) in itertools.product(range(x),q) if u[i]==j]
                direct=[(i,k) for i,k in itertools.product(range(x),range(r)) if v[u[i]]==w[k]]
                self.assertEqual(sorted(p),sorted(direct))
                self.assertEqual(len(p),len(set(p)))

    def test_CAT_07_004_pushout_epi_and_pullback_mono(self):
        for a,b,c in itertools.product(range(4),repeat=3):
            for f,g in itertools.product(maps(a,c),maps(b,c)):
                if len(set(g))==b:
                    p=[i for i,j in itertools.product(range(a),range(b)) if f[i]==g[j]]
                    self.assertEqual(len(p),len(set(p)))
            for f,g in itertools.product(maps(c,a),maps(c,b)):
                if set(g)==set(range(b)):
                    q=quotient(a+b,((f[i],a+g[i]) for i in range(c)))
                    self.assertEqual(set(q[:a]),set(q))

    def test_CAT_07_005_module_pushout(self):
        # Cyclic modules over Z/n; compatibility kills the relation (f,-g).
        for n in range(1,8):
            for f,g,u,v in itertools.product(range(n),repeat=4):
                if (u*f-v*g)%n:
                    continue
                for a,b,t in itertools.product(range(n),repeat=3):
                    self.assertEqual((u*a+v*b)%n,(u*(a+t*f)+v*(b-t*g))%n)

    def test_CAT_07_006_manifold_crossing(self):
        # Algebraic ingredient of the differential obstruction, not a manifold proof.
        for x,y in itertools.product(range(-10,11),repeat=2):
            self.assertEqual(x*x==y*y,x==y or x==-y)
        self.assertNotEqual(1*(-1)-1*1,0)

    def test_CAT_07_007_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:equalizatory","def:equalizer","def:coeq","def:pullback",
                      "def:pushout","przyklad:włokna","cat:prop:pullback-equalizer",
                      "cat:thm:pullback-pasting","cat:prop:base-change-mono",
                      "cat:prop:base-change-iso","cat:ex:manifold-pullback"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
