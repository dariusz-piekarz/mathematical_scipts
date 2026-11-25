"""CAT-26: finite poset models and source structure, not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/26-rozszerzenia-kana.tex"


class CategoryTheoryCh26(unittest.TestCase):
    def test_CAT_26_001_pointwise_poset_adjunction(self):
        # A finite chain, B finite chain, C a four-element chain.
        # Nat is pointwise order. Empty supremum = 0, infimum = 3.
        A = range(3)
        B = range(4)
        C = range(4)
        monotone = lambda n, values: list(
            itertools.combinations_with_replacement(values, n))
        maps = monotone(len(A), C)
        targets = monotone(len(B), C)
        le = lambda f, g: all(x <= y for x, y in zip(f, g))
        for K in monotone(len(A), B):
            for F in maps:
                L = tuple(max((F[a] for a in A if K[a] <= b), default=0)
                          for b in B)
                R = tuple(min((F[a] for a in A if b <= K[a]), default=3)
                          for b in B)
                self.assertIn(L, targets)
                self.assertIn(R, targets)
                self.assertTrue(le(F, tuple(L[K[a]] for a in A)))
                self.assertTrue(le(tuple(R[K[a]] for a in A), F))
                for H in targets:
                    HK = tuple(H[K[a]] for a in A)
                    self.assertEqual(le(L, H), le(F, HK))
                    self.assertEqual(le(H, R), le(HK, F))

    def test_CAT_26_003_full_faithful_and_composition(self):
        chain = range(4)
        mono = lambda n: list(itertools.combinations_with_replacement(chain, n))
        def lan(K, F):
            return tuple(max((F[a] for a in range(len(K)) if K[a] <= b),
                             default=0) for b in chain)
        def ran(K, F):
            return tuple(min((F[a] for a in range(len(K)) if b <= K[a]),
                             default=3) for b in chain)
        for n in range(5):
            for K in itertools.combinations(chain, n):
                for F in mono(n):
                    L, R = lan(K, F), ran(K, F)
                    self.assertEqual(tuple(L[b] for b in K), F)
                    self.assertEqual(tuple(R[b] for b in K), F)
                    for H in mono(4):
                        if tuple(H[b] for b in K) == F:
                            self.assertTrue(all(l <= h <= r for l, h, r
                                                in zip(L, H, R)))
        for K, F, M in itertools.product(mono(3), mono(3), mono(4)):
            MK = tuple(M[k] for k in K)
            self.assertEqual(lan(MK, F), lan(M, lan(K, F)))
            self.assertEqual(ran(MK, F), ran(M, ran(K, F)))

    def test_CAT_26_004_adjoint_criterion_poset(self):
        # For each monotone K:A -> B, compute potential adjoints.
        A, B = range(3), range(4)
        for K in itertools.combinations_with_replacement(B, len(A)):
            lower = [tuple(a for a in A if K[a] <= b) for b in B]
            upper = [tuple(a for a in A if b <= K[a]) for b in B]
            if all(lower):
                T = tuple(max(s) for s in lower)
                for a, b in itertools.product(A, B):
                    self.assertEqual(K[a] <= b, a <= T[b])
            if all(upper):
                S = tuple(min(s) for s in upper)
                for a, b in itertools.product(A, B):
                    self.assertEqual(b <= K[a], S[b] <= a)

    def test_CAT_26_005_group_actions_set_models(self):
        # C2 -> C4, either trivial or injective. C2 acts on a finite
        # set X via an involution. Check quotient and compatible families.
        H = range(4)
        for shift in (0, 2):
            for n in range(4):
                X = range(n)
                for involution in itertools.permutations(X):
                    if any(involution[involution[x]] != x for x in X):
                        continue
                    def act(g, x):
                        return x if g == 0 else involution[x]
                    points = list(itertools.product(H, X))
                    parent = {p: p for p in points}
                    def root(p):
                        while parent[p] != p:
                            p = parent[p]
                        return p
                    for h, x in points:
                        parent[root(((h+shift) % 4, x))] = root((h, act(1,x)))
                    classes = {root(p) for p in points}
                    for h, x in points:
                        for t in H:
                            self.assertEqual(root(((t+h+shift)%4,x)),
                                             root(((t+h)%4,act(1,x))))
                    families = [v for v in itertools.product(X,repeat=4)
                                if all(v[(h+shift)%4]==act(1,v[h]) for h in H)]
                    for v, t in itertools.product(families,H):
                        self.assertIn(tuple(v[(h+t)%4] for h in H), families)
                    if shift == 2:
                        self.assertEqual(len(classes),2*n)
                        self.assertEqual(len(families),n*n)
                    else:
                        orbits = {min(x,involution[x]) for x in X}
                        fixed = sum(x==involution[x] for x in X)
                        self.assertEqual(len(classes),4*len(orbits))
                        self.assertEqual(len(families),fixed**4)

    def test_CAT_26_006_yoneda_density_arrow(self):
        # A is 0 -> 1. A presheaf is a function P(1) -> P(0).
        for n0,n1 in itertools.product(range(4),repeat=2):
            for p in itertools.product(range(n0),repeat=n1):
                for t in (0,1):
                    triples = [(a,x) for a,n in enumerate((n0,n1))
                               for x in range(n) if t<=a]
                    parent={z:z for z in triples}
                    def root(z):
                        while parent[z]!=z:
                            z=parent[z]
                        return z
                    if t==0:
                        for x in range(n1):
                            parent[root((1,x))]=root((0,p[x]))
                    value=lambda z: p[z[1]] if t==0 and z[0]==1 else z[1]
                    self.assertEqual({value(z) for z in triples},
                                     set(range((n0,n1)[t])))
                    for z,w in itertools.product(triples,repeat=2):
                        self.assertEqual(root(z)==root(w),value(z)==value(w))

    def test_CAT_26_007_induction_coinduction_modules(self):
        # Trivial subgroup of C2, k=F2, V=k and W=k^2 with swap action.
        # Enumerate all linear maps between the two-dimensional modules.
        vectors=list(itertools.product(range(2),repeat=2))
        swap=lambda v:(v[1],v[0])
        def linear(cols,v):
            return tuple((cols[0][i]*v[0]+cols[1][i]*v[1])%2
                         for i in range(2))
        equivariant=[cols for cols in itertools.product(vectors,repeat=2)
                     if all(linear(cols,swap(v))==swap(linear(cols,v))
                            for v in vectors)]
        # Induction: a:k->W is determined by arbitrary w in W.
        self.assertEqual(set(equivariant),{(w,swap(w)) for w in vectors})
        # Coinduction: a:W->k is a functional, bar a(v)=(a(v),a(sv)).
        for coeff in vectors:
            a=lambda v:sum(x*y for x,y in zip(coeff,v))%2
            cols=tuple((a(v),a(swap(v))) for v in ((1,0),(0,1)))
            self.assertIn(cols,equivariant)
            for v in vectors:
                self.assertEqual(linear(cols,v),(a(v),a(swap(v))))
                self.assertEqual(linear(cols,v)[0],a(v))

    def test_CAT_26_008_nonabelian_group_action_order(self):
        # C2 embedded in S3. X is the two-element regular C2-set.
        # Test the actual left H-actions on induced classes and coinduced
        # compatible functions, including order-sensitive compositions.
        H = list(itertools.permutations(range(3)))
        mul = lambda h, k: tuple(h[k[i]] for i in range(3))
        e, s = (0,1,2), (1,0,2)
        X = range(2)
        def canonical(h,x):
            return min((h,x),(mul(h,s),1-x))
        classes = {canonical(h,x) for h,x in itertools.product(H,X)}
        self.assertEqual(len(classes),6)
        def ind(t,c):
            h,x = c
            return canonical(mul(t,h),x)
        families = [f for f in itertools.product(X,repeat=len(H))
                    if all(f[H.index(mul(s,h))] == 1-f[H.index(h)]
                           for h in H)]
        self.assertEqual(len(families),8)
        def coind(t,f):
            return tuple(f[H.index(mul(h,t))] for h in H)
        for t,u in itertools.product(H,repeat=2):
            for c in classes:
                self.assertEqual(ind(t,ind(u,c)),ind(mul(t,u),c))
                self.assertEqual(ind(e,c),c)
            for f in families:
                self.assertIn(coind(t,f),families)
                self.assertEqual(coind(t,coind(u,f)),coind(mul(t,u),f))
                self.assertEqual(coind(e,f),f)
        self.assertTrue(any(coind(t,coind(u,f)) != coind(u,coind(t,f))
                            for t,u,f in itertools.product(H,H,families)))
        # Evaluation at the identity intertwines the restricted C2-action.
        for f in families:
            self.assertEqual(coind(s,f)[H.index(e)],1-f[H.index(e)])

    def test_CAT_26_002_structure(self):
        source = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = []
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",
                                         p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source):
            self.assertEqual(all_labels.count(ref), 1, ref)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}",
                             source):
            self.assertTrue(source[m.end():].lstrip().startswith(r"\begin{proof}"))
        book = (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8")
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(), book)


if __name__ == "__main__":
    unittest.main()
