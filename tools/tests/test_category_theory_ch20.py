"""CAT-20: finite checks of normalization and list strictification."""
import functools
import itertools
import re
import unittest
from pathlib import Path
CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/20-koherencja-i-funktory-monoidalne.tex"
I = "I"

def word(t):
    if isinstance(t, str):
        return () if t == I else (t,)
    return word(t[0]) + word(t[1])

def norm(w):
    return I if not w else w[0] if len(w)==1 else (w[0], norm(w[1:]))

def measure(t):
    if isinstance(t,str):
        return (1,0)
    n,w=measure(t[0])
    m,v=measure(t[1])
    return (n+m,w+v+n)

@functools.lru_cache(None)
def trees(w):
    if len(w)==1:
        return (w[0],)
    return tuple((a,b) for k in range(1,len(w))
                 for a in trees(w[:k]) for b in trees(w[k:]))

def steps(t):
    if isinstance(t,str):
        return set()
    a,b=t
    result=set()
    if isinstance(a,tuple):
        result.add((a[0],(a[1],b)))
    if a==I:
        result.add(b)
    if b==I:
        result.add(a)
    result.update((u,b) for u in steps(a))
    result.update((a,v) for v in steps(b))
    return result

@functools.lru_cache(None)
def normal_forms(t):
    s=steps(t)
    if not s:
        return frozenset((t,))
    return frozenset().union(*(normal_forms(u) for u in s))

class CategoryTheoryCh20(unittest.TestCase):
    def test_CAT_20_001_normalization(self):
        for n in range(1,7):
            for w in itertools.product(("A","I"),repeat=n):
                for t in trees(w):
                    self.assertEqual(normal_forms(t),frozenset((norm(word(t)),)))
                    for u in steps(t):
                        self.assertLess(measure(u),measure(t))
                        self.assertEqual(word(t),word(u))

    def test_CAT_20_002_unit_overlaps(self):
        for t in (("I","I"),(("I","A"),"B"),
                  (("A","I"),"B"),(("A","B"),"I"),
                  ((("A","B"),"C"),"D")):
            # At I⊗I, the two distinct rules have the same target.
            self.assertEqual(len(steps(t)),1 if t==(I,I) else 2)
            self.assertEqual(normal_forms(t),frozenset((norm(word(t)),)))

    def test_CAT_20_003_list_strictification(self):
        # Evaluation of tensor morphisms in finite Cartesian models.
        def flatten(t):
            if t==():
                return ()
            if isinstance(t,int):
                return (t,)
            return flatten(t[0])+flatten(t[1])
        def pack(w):
            return () if not w else w[0] if len(w)==1 else (w[0],pack(w[1:]))
        def ten(f,g,n):
            return lambda x: pack(flatten(f(pack(flatten(x)[:n])))+
                                  flatten(g(pack(flatten(x)[n:]))))
        fs=(lambda x:x,lambda x:pack(tuple(1-a for a in flatten(x))))
        for u,v,w in itertools.product(range(3),repeat=3):
            for f,g,h in itertools.product(fs,repeat=3):
                for x in itertools.product(range(2),repeat=u+v+w):
                    self.assertEqual(ten(ten(f,g,u),h,u+v)(pack(x)),
                                     ten(f,ten(g,h,v),u)(pack(x)))

    def test_CAT_20_005_distinct_rule_occurrences(self):
        # Keep rule names and addresses, even when the targets agree.
        def moves(t, address=()):
            if isinstance(t,str):
                return []
            a,b=t
            out=[]
            if isinstance(a,tuple):
                out.append(("alpha",address,(a[0],(a[1],b))))
            if a==I:
                out.append(("lambda",address,b))
            if b==I:
                out.append(("rho",address,a))
            out.extend((rule,pos,(u,b)) for rule,pos,u in moves(a,address+(0,)))
            out.extend((rule,pos,(a,v)) for rule,pos,v in moves(b,address+(1,)))
            return out
        self.assertEqual({(rule,pos) for rule,pos,_ in moves((I,I))},
                         {("lambda",()),("rho",())})
        for n in range(1,6):
            for w in itertools.product(("A","I"),repeat=n):
                for t in trees(w):
                    self.assertEqual({u for _,_,u in moves(t)},steps(t))
                    for _,_,u in moves(t):
                        self.assertLess(measure(u),measure(t))

    def test_CAT_20_006_cartesian_comparisons(self):
        # Powers X^n preserve finite products. Compare the two composites
        # for consecutive power functors by evaluating every entry.
        for n,m in itertools.product(range(4),repeat=2):
            if n*m > 6:
                continue
            for a in itertools.product(range(2),repeat=n*m):
                for b in itertools.product(range(2),repeat=n*m):
                    nested=tuple(tuple((a[i*m+j],b[i*m+j])
                                       for j in range(m)) for i in range(n))
                    direct=(tuple(tuple(a[i*m+j] for j in range(m)) for i in range(n)),
                            tuple(tuple(b[i*m+j] for j in range(m)) for i in range(n)))
                    separated=tuple((tuple(x for x,y in row),tuple(y for x,y in row))
                                    for row in nested)
                    self.assertEqual(direct,(tuple(x for x,y in separated),
                                             tuple(y for x,y in separated)))

    def test_CAT_20_004_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertIn("cat:thm:mac-lane-coherence",labels)
        self.assertIn("cat:thm:strictification",labels)
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels+=re.findall(r"\\label\{([^}]+)\}",p.read_text(encoding="utf-8"))
        for label in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",s):
            self.assertEqual(all_labels.count(label),1)
        stack=[]
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
