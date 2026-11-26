"""CAT-27: finite models of ends/coends; not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/27-konce-i-kokonce.tex"


class CategoryTheoryCh27(unittest.TestCase):
    def test_CAT_27_001_end_natural_transformations(self):
        # A = 0 -> 1. Functors to Set are single functions.
        for a,b,c,d in itertools.product(range(3), repeat=4):
            for F in itertools.product(range(b), repeat=a):
                for G in itertools.product(range(d), repeat=c):
                    pairs = list(itertools.product(
                        itertools.product(range(c), repeat=a),
                        itertools.product(range(d), repeat=b)))
                    end = [(u,v) for u,v in pairs
                           if tuple(G[u[x]] for x in range(a)) ==
                              tuple(v[F[x]] for x in range(a))]
                    # Count natural transformations independently via fibers:
                    # for fixed v, choices for each u(x) lie in a fiber of G.
                    count = 0
                    for v in itertools.product(range(d),repeat=b):
                        prod = 1
                        for x in range(a):
                            prod *= sum(y == v[F[x]] for y in G)
                        count += prod
                    self.assertEqual(len(end), count)

    def test_CAT_27_002_coend_separable_bifunctor(self):
        # A = 0 -> 1, T(a,b)=P(a) x F(b) for a presheaf P
        # and a covariant set-valued functor F.
        for p0,p1,f0,f1 in itertools.product(range(3),repeat=4):
            for P in itertools.product(range(p0),repeat=p1):
                for F in itertools.product(range(f1),repeat=f0):
                    Z = ([(0,x,y) for x in range(p0) for y in range(f0)]
                         + [(1,x,y) for x in range(p1) for y in range(f1)])
                    parent = {z:z for z in Z}
                    def root(z):
                        while parent[z] != z:
                            z = parent[z]
                        return z
                    for x,y in itertools.product(range(p1),range(f0)):
                        parent[root((0,P[x],y))] = root((1,x,F[y]))
                    relations = [((0,P[x],y),(1,x,F[y]))
                                 for x,y in itertools.product(range(p1),range(f0))]
                    # Every compatible map from the diagonal factors uniquely
                    # through the quotient, checked for two-element targets.
                    roots = sorted({root(z) for z in Z})
                    compatible = {v for v in itertools.product(range(2),repeat=len(Z))
                                  if all(v[Z.index(z)]==v[Z.index(w)]
                                         for z,w in relations)}
                    induced = {tuple(v[roots.index(root(z))] for z in Z)
                               for v in itertools.product(range(2),repeat=len(roots))}
                    self.assertEqual(compatible,induced)

    def test_CAT_27_003_dinatural_noncomposition(self):
        # S constant singleton, T has empty (1,0), other entries singleton.
        # U has empty (1,0) and two distinct maps from diagonal to (0,1).
        def compose(g,f):
            return tuple(g[x] for x in f)
        def dinatural(S,T,alpha):
            left=compose(T[0],compose(alpha[0],S[2]))
            right=compose(T[1],compose(alpha[1],S[3]))
            return left==right
        # Entries: (diagonal -> upper) twice, (lower -> diagonal) twice.
        S=((0,),(0,),(0,),(0,))
        T=((0,),(0,),(),())
        U=((0,),(1,),(),())
        alpha=((0,),(0,))
        beta=((0,),(0,))
        self.assertTrue(dinatural(S,T,alpha))
        self.assertTrue(dinatural(T,U,beta))
        self.assertFalse(dinatural(S,U,tuple(compose(b,a)
                                            for a,b in zip(alpha,beta))))

    def test_CAT_27_005_co_yoneda_parallel_arrows(self):
        # A: 0 ==(p,q)==> 1. P contravariant, F covariant.
        # Both co-Yoneda formulas reduce to evaluation on representatives.
        for n0,n1 in itertools.product(range(3),repeat=2):
            for p,q in itertools.product(
                    itertools.product(range(n1),repeat=n0),repeat=2):
                # Covariant F, b=1. The two arrows give separate summands.
                Z=[(0,x,h) for x in range(n0) for h in (0,1)]
                Z += [(1,y,2) for y in range(n1)]
                parent={z:z for z in Z}
                def root(z):
                    while parent[z]!=z:
                        z=parent[z]
                    return z
                for x,h in itertools.product(range(n0),range(2)):
                    parent[root((0,x,h))]=root((1,(p,q)[h][x],2))
                val=lambda z:z[1] if z[0]==1 else (p,q)[z[2]][z[1]]
                self.assertEqual({val(z) for z in Z},set(range(n1)))
                for z,w in itertools.product(Z,repeat=2):
                    self.assertEqual(root(z)==root(w),val(z)==val(w))
                # Contravariant P on the opposite arrow category,
                # with b at its source, is the dual construction:
                # classes (a,x,h:b->a) map to P(h)(x).
                # Relabeling original objects exchanges 0 and 1.
                for z in Z:
                    self.assertEqual(root(z),root((1,val(z),2)))

    def test_CAT_27_006_fubini_coends(self):
        # Two arrow categories, separable diagram values indexed by a,b.
        # Compute the quotient of all diagonal points and the iterated
        # quotient; the relations act independently on the two indices.
        for m,n,p,q in itertools.product(range(1,3),repeat=4):
            for f in itertools.product(range(n),repeat=m):
                for g in itertools.product(range(q),repeat=p):
                    Z=[(a,x,b,y) for a,b in itertools.product(range(2),repeat=2)
                       for x in range((m,n)[a]) for y in range((p,q)[b])]
                    parent={z:z for z in Z}
                    def root(z):
                        while parent[z]!=z:
                            z=parent[z]
                        return z
                    for a,x,b,y in Z:
                        z=(a,x,b,y)
                        if a==0:
                            parent[root(z)]=root((1,f[x],b,y))
                        if b==0:
                            parent[root(z)]=root((a,x,1,g[y]))
                    left=lambda z:(f[z[1]] if z[0]==0 else z[1],
                                   g[z[3]] if z[2]==0 else z[3])
                    self.assertEqual(len({root(z) for z in Z}),n*q)
                    for z,w in itertools.product(Z,repeat=2):
                        self.assertEqual(root(z)==root(w),left(z)==left(w))

    def test_CAT_27_007_twisted_arrow_parallel_arrows(self):
        # A has two parallel arrows p,q:0->1 and the identities i0,i1.
        # Tw(A) has exactly two incoming nonidentity arrows at each p,q.
        arrows=[(0,0,"i0"),(1,1,"i1"),(0,1,"p"),(0,1,"q")]
        identities={0:arrows[0],1:arrows[1]}
        def compose(g,f):
            assert f[1]==g[0]
            if f[0]==f[1]:
                return g
            if g[0]==g[1]:
                return f
            raise AssertionError("unexpected composition")
        morphisms=[]
        for f,g,u,v in itertools.product(arrows,repeat=4):
            if (u[0],u[1],v[0],v[1]) != (g[0],f[0],f[1],g[1]):
                continue
            if compose(v,compose(f,u))==g:
                morphisms.append((f,g,u,v))
        self.assertEqual(len(morphisms),8)
        for n0,n1 in itertools.product(range(3),repeat=2):
            for p,q in itertools.product(
                    itertools.product(range(n1),repeat=n0),repeat=2):
                # T(a,b)=F(b). Compare the end with the ordinary
                # limit along Tw(A) including all morphisms.
                F={arrows[0]:tuple(range(n0)),arrows[1]:tuple(range(n1)),
                   arrows[2]:p,arrows[3]:q}
                end={(x,y) for x,y in itertools.product(range(n0),range(n1))
                     if p[x]==y==q[x]}
                cones=set()
                for xs in itertools.product(
                        *(range((n0,n1)[f[1]]) for f in arrows)):
                    if all(F[v][xs[arrows.index(f)]]==xs[arrows.index(g)]
                           for f,g,u,v in morphisms):
                        cones.add(xs)
                self.assertEqual({(xs[0],xs[1]) for xs in cones},end)
                self.assertEqual(len(cones),len(end))
                # Coend: T(b,a)=F(a), diagram on Tw(A)^op.
                nodes=[(f,x) for f in arrows for x in range((n0,n1)[f[0]])]
                parent={z:z for z in nodes}
                def root(z):
                    while parent[z]!=z:
                        z=parent[z]
                    return z
                for f,g,u,v in morphisms:
                    for x in range((n0,n1)[g[0]]):
                        parent[root((g,x))]=root((f,F[u][x]))
                # Ordinary colimit of F: identify p(x) and q(x).
                ordinary=list(range(n1))
                def rr(x):
                    while ordinary[x]!=x:
                        x=ordinary[x]
                    return x
                for x in range(n0):
                    ordinary[rr(p[x])]=rr(q[x])
                self.assertEqual(len({root(z) for z in nodes}),
                                 len({rr(y) for y in range(n1)}))
                for y,z in itertools.product(range(n1),repeat=2):
                    self.assertEqual(root((identities[1],y))==
                                     root((identities[1],z)),rr(y)==rr(z))

    def test_CAT_27_008_tensor_hom_group_actions(self):
        # Right and left C2-actions on finite sets given by involutions.
        # Compatible pairings into {0,1} are precisely orbit maps.
        for m,n in itertools.product(range(3),repeat=2):
            for r,l in itertools.product(itertools.permutations(range(m)),
                                         itertools.permutations(range(n))):
                if any(r[r[x]]!=x for x in range(m)):
                    continue
                if any(l[l[y]]!=y for y in range(n)):
                    continue
                pairs=list(itertools.product(range(m),range(n)))
                def orbit(x,y):
                    return min((x,y),(r[x],l[y]))
                orbits={orbit(x,y) for x,y in pairs}
                balanced=0
                for z in itertools.product(range(2),repeat=len(pairs)):
                    d=dict(zip(pairs,z))
                    if all(d[r[x],y]==d[x,l[y]] for x,y in pairs):
                        balanced+=1
                self.assertEqual(balanced,2**len(orbits))

    def test_CAT_27_009_twisted_arrow_general_bifunctors(self):
        # A = 0 -> 1; A^op x A is a commuting square, not necessarily
        # separable. L=T(1,0), A=T(0,0), B=T(1,1), U=T(0,1).
        def maps(m,n):
            return itertools.product(range(n),repeat=m)
        def partitions(nodes,edges):
            parent={z:z for z in nodes}
            def root(z):
                while parent[z]!=z:
                    z=parent[z]
                return z
            for x,y in edges:
                parent[root(x)]=root(y)
            return {frozenset(z for z in nodes if root(z)==r)
                    for r in {root(z) for z in nodes}}
        models=0
        for l,a,b,u in itertools.product(range(3),repeat=4):
            for p,q,s,t in itertools.product(maps(l,a),maps(l,b),
                                             maps(a,u),maps(b,u)):
                if any(s[p[x]]!=t[q[x]] for x in range(l)):
                    continue
                models+=1
                end={(x,y) for x,y in itertools.product(range(a),range(b))
                     if s[x]==t[y]}
                # Ordinary limit of Tw(A): id0 -> f <- id1.
                cones={(x,y,z) for x,y,z in
                       itertools.product(range(a),range(b),range(u))
                       if s[x]==z and t[y]==z}
                self.assertEqual({(x,y) for x,y,z in cones},end)
                self.assertEqual(len(cones),len(end))
                diagonal=[(0,x) for x in range(a)]+[(1,y) for y in range(b)]
                coend=partitions(diagonal,[((0,p[z]),(1,q[z]))
                                           for z in range(l)])
                # Ordinary colimit of Tw(A)^op: id0 <- f -> id1,
                # with T(1,0) at f, not T(0,1).
                nodes=diagonal+[(2,z) for z in range(l)]
                edges=[((2,z),(0,p[z])) for z in range(l)]
                edges += [((2,z),(1,q[z])) for z in range(l)]
                colimit=partitions(nodes,edges)
                self.assertEqual({cls.intersection(diagonal)
                                  for cls in colimit},coend)
        self.assertGreater(models,100)

    def test_CAT_27_004_structure(self):
        source = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",source)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",
                                         p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",source):
            self.assertEqual(all_labels.count(ref),1,ref)
        stack=[]
        for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",source):
            if kind=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}",source):
            self.assertTrue(source[m.end():].lstrip().startswith(r"\begin{proof}"))
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(),
                      (ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
