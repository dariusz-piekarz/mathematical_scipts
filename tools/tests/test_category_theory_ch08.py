"""CAT-08: finite universal properties and filtered-colimit regressions."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/08-granice-i-kogranice-wspolna-teoria-konstrukcji.tex"

def maps(n, m):
    return itertools.product(range(m), repeat=n)

def comp(g, f):
    return tuple(g[i] for i in f)

def classes(n, edges):
    labels = list(range(n))
    for a, b in edges:
        old, new = labels[a], labels[b]
        labels = [new if v == old else v for v in labels]
    return tuple(sorted(set(labels)).index(v) for v in labels)

class CategoryTheoryCh08(unittest.TestCase):
    def test_CAT_08_001_limit_universal(self):
        for a,b,c,n in itertools.product(range(3), repeat=4):
            for f,g in itertools.product(maps(a,c), maps(b,c)):
                L = [(i,j) for i,j in itertools.product(range(a),range(b)) if f[i]==g[j]]
                induced = {(tuple(L[k][0] for k in h),tuple(L[k][1] for k in h))
                           for h in maps(n,len(L))}
                cones = {(u,v) for u,v in itertools.product(maps(n,a),maps(n,b))
                         if comp(f,u)==comp(g,v)}
                self.assertEqual(induced,cones)
                self.assertEqual(len(induced),len(L)**n)

    def test_CAT_08_002_colimit_universal(self):
        for a,b,c,n in itertools.product(range(3),repeat=4):
            for f,g in itertools.product(maps(c,a),maps(c,b)):
                q=classes(a+b,((f[i],a+g[i]) for i in range(c)))
                induced={(comp(h,q[:a]),comp(h,q[a:])) for h in maps(len(set(q)),n)}
                cocones={(u,v) for u,v in itertools.product(maps(a,n),maps(b,n))
                         if comp(u,f)==comp(v,g)}
                self.assertEqual(induced,cocones)
                self.assertEqual(len(induced),n**len(set(q)))

    def test_CAT_08_003_chain_colimit(self):
        for a,b,c in itertools.product(range(4),repeat=3):
            for f,g in itertools.product(maps(a,b),maps(b,c)):
                q=classes(a+b+c,[(i,a+f[i]) for i in range(a)]+
                          [(a+j,a+b+g[j]) for j in range(b)])
                values=comp(g,f)+g+tuple(range(c))
                for i,j in itertools.product(range(a+b+c),repeat=2):
                    self.assertEqual(q[i]==q[j],values[i]==values[j])

    def test_CAT_08_004_pointwise_naturality(self):
        for a,b,c,d in itertools.product(range(3),repeat=4):
            for f,g,u,v in itertools.product(maps(a,b),maps(c,d),maps(a,c),maps(b,d)):
                if comp(g,u)!=comp(v,f):
                    continue
                for x in range(a):
                    self.assertEqual(g[u[x]],v[f[x]])

    def test_CAT_08_005_filtered_equalizer(self):
        for a,b,c,d in itertools.product(range(3),repeat=4):
            for f,g,u,v in itertools.product(maps(a,b),maps(a,b),maps(a,c),maps(b,d)):
                if comp(v,f)!=comp(v,g):
                    continue
                # Later equalizer of v f and v g contains all early elements.
                self.assertTrue(all(v[f[x]]==v[g[x]] for x in range(a)))

    def test_CAT_08_006_inverse_binary(self):
        for n in range(1,9):
            for k in range(2**n):
                residues=tuple(k%(2**i) for i in range(1,n+1))
                self.assertTrue(all(residues[i+1]%(2**(i+1))==residues[i]
                                    for i in range(n-1)))
            self.assertEqual(len({tuple(k%(2**i) for i in range(1,n+1))
                                  for k in range(2**n)}),2**n)

    def test_CAT_08_007_lim_one_finite_recurrence(self):
        for m in range(2,6):
            for b in itertools.product(range(m),repeat=3):
                a=[0]
                for x in b:
                    a.append((a[-1]-x)%m)
                self.assertEqual(tuple((a[i]-a[i+1])%m for i in range(3)),b)

    def test_CAT_08_008_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("def:limit","tw:limits-set","def:colimit","tw:colimits-set",
                      "cat:thm:limits-products","cat:thm:pointwise-limits",
                      "cat:thm:iterated-limits","cat:lem:filtered-equality",
                      "cat:thm:filtered-finite","cat:ex:inverse-not-exact",
                      "cat:rem:lim-one"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
