"""CAT-10: finite models for Yoneda and its naturality."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER=Path(__file__).resolve().parents[2]/"chapters/pl/category_theory/10-lemat-yonedy-obiekt-poznajemy-przez-wszystkie-morfizmy.tex"

def maps(n,m):
    return itertools.product(range(m),repeat=n)

def comp(g,f):
    return tuple(g[i] for i in f)

class CategoryTheoryCh10(unittest.TestCase):
    def test_CAT_10_001_covariant_evaluation(self):
        # For representable F=Hom(B,-), each element a:B->A
        # yields a distinct family; evaluation at id_A recovers a.
        for a,b in itertools.product(range(4),repeat=2):
            elems=list(maps(b,a))
            signatures=[]
            for u in elems:
                signature=tuple(comp(f,u) for x in range(4) for f in maps(a,x))
                signatures.append(signature)
                self.assertEqual(comp(tuple(range(a)),u),u)
            self.assertEqual(len(set(signatures)),len(elems))

    def test_CAT_10_002_contravariant_evaluation(self):
        for a,b in itertools.product(range(4),repeat=2):
            elems=list(maps(a,b))
            signatures=[tuple(comp(u,f) for x in range(4) for f in maps(x,a)) for u in elems]
            self.assertEqual(len(set(signatures)),len(elems))
            for u in elems:
                self.assertEqual(comp(u,tuple(range(a))),u)

    def test_CAT_10_003_naturality_in_object(self):
        for a,b,c,x in itertools.product(range(3),repeat=4):
            for r,u,f in itertools.product(maps(a,b),maps(c,a),maps(b,x)):
                self.assertEqual(comp(comp(f,r),u),comp(f,comp(r,u)))
            for r,u,f in itertools.product(maps(a,b),maps(b,c),maps(x,a)):
                self.assertEqual(comp(u,comp(r,f)),comp(comp(u,r),f))

    def test_CAT_10_004_naturality_in_functor(self):
        for a,b,c,x in itertools.product(range(3),repeat=4):
            for r,u,f in itertools.product(maps(c,b),maps(b,a),maps(a,x)):
                self.assertEqual(comp(comp(f,u),r),comp(f,comp(u,r)))
            for r,u,f in itertools.product(maps(b,c),maps(a,b),maps(x,a)):
                self.assertEqual(comp(r,comp(u,f)),comp(comp(r,u),f))

    def test_CAT_10_005_tuple_operations(self):
        for n,m in itertools.product(range(1,4),repeat=2):
            operations=list(maps(m,n))
            self.assertEqual(len(set(operations)),n**m)
            for x,y in itertools.product(range(3),repeat=2):
                for h,f,op in itertools.product(maps(x,y),maps(n,x),operations):
                    self.assertEqual(comp(h,comp(f,op)),comp(comp(h,f),op))

    def test_CAT_10_006_power_set_operations(self):
        for x,y in itertools.product(range(4),repeat=2):
            for f in maps(x,y):
                for a in range(x):
                    self.assertEqual({f[i] for i in {a}},{f[a]})
                    self.assertFalse({f[i] for i in set()})

    def test_CAT_10_007_group_words(self):
        # Noncommutative finite group S3: xy and yx differ, and
        # conjugation preserves multiplication and commutator words.
        G=list(itertools.permutations(range(3)))
        e=tuple(range(3))
        inv=lambda a:tuple(a.index(i) for i in range(3))
        comm=lambda a,b:comp(comp(comp(a,b),inv(a)),inv(b))
        self.assertTrue(any(comp(a,b)!=comp(b,a) for a,b in itertools.product(G,repeat=2)))
        for g,a,b in itertools.product(G,repeat=3):
            h=lambda x:comp(comp(g,x),inv(g))
            self.assertEqual(h(comp(a,b)),comp(h(a),h(b)))
            self.assertEqual(h(comm(a,b)),comm(h(a),h(b)))
            self.assertEqual(h(e),e)

    def test_CAT_10_009_enumerate_all_natural_families(self):
        # Walking-arrow category: arbitrary Set-valued functors on it,
        # not just families already obtained from the Yoneda formula.
        for n,m in itertools.product(range(4),repeat=2):
            for transition in maps(n,m):
                # The opposite walking arrow is isomorphic by interchanging objects.
                for represented in (0,1):
                    H=(1,1) if represented==0 else (0,1)
                    # H has the unique arrow H(0)->H(1).
                    h=(0,) if H[0] else ()
                    natural=[]
                    for a,b in itertools.product(maps(H[0],n),maps(H[1],m)):
                        if comp(transition,a)==comp(b,h):
                            natural.append((a,b))
                    expected=[((u,),(transition[u],)) for u in range(n)] if represented==0 else [((),(u,)) for u in range(m)]
                    self.assertEqual(set(natural),set(expected))

    def test_CAT_10_010_nonrepresentable_target_monoid(self):
        # One-object category with monoid {1,z}, z^2=z.
        # Every action on X is an idempotent map T.
        # Enumerate *all* maps alpha from the two-element regular action.
        for n in range(5):
            for T in maps(n,n):
                if comp(T,T)!=T:
                continue
                natural=[a for a in maps(2,n) if comp(T,a)==(a[1],a[1])]
                self.assertEqual(set(natural),{(x,T[x]) for x in range(n)})
                self.assertEqual(len(natural),n)

    def test_CAT_10_011_all_tuple_operations(self):
        # Enumerate every candidate at the two-element test object;
        # naturality under all maps of 0,1,2 rules out nonprojections.
        X=list(maps(2,2))
        candidates=[]
        for op in maps(4,2):
            if all(op[X.index(comp(h,p))]==h[op[i]]
                   for i,p in enumerate(X) for h in maps(2,2)):
                candidates.append(op)
        self.assertEqual(set(candidates),{tuple(p[i] for p in X) for i in range(2)})

    def test_CAT_10_008_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:yoneda","tw:yoneda","przyklad:yoneda-tuple","tw:yoneda-embedding",
                      "cat:thm:yoneda-contra","cat:thm:yoneda-natural","cat:prop:yoneda-cov-embedding","cat:ex:yoneda-group-words"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin": stack.append(env)
            else: self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
