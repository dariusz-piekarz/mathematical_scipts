"""Mathematical regression tests for AA-07: free words and Schreier graphs."""
from itertools import permutations,product
from collections import deque
from pathlib import Path
import unittest,re

ROOT=Path(__file__).resolve().parents[2]
SRC=(ROOT/"chapters/pl/abstract_algebra/07-grupy-wolne-prezentacje-i-twierdzenie-nielsena-schreiera.tex").read_text("utf8")
def opp(x,r=2):return (x+r)%(2*r)
def red(w,r=2):
    out=[]
    for x in w:
        if out and out[-1]==opp(x,r):out.pop()
        else:out.append(x)
    return tuple(out)
def inverse(w,r=2):return tuple(opp(x,r) for x in reversed(w))
def words(n,r=2):
    for k in range(n+1):yield from product(range(2*r),repeat=k)
def p_inv(p):return tuple(p.index(i) for i in range(len(p)))
def p_mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def basis(ps):
    d=len(ps[0]);r=len(ps)
    trans=tuple(ps)+tuple(p_inv(a) for a in ps)
    paths={0:()};q=deque([0]);tree=set()
    while q:
        v=q.popleft()
        for a in range(2*r):
            w=trans[a][v]
            if w not in paths:
                paths[w]=paths[v]+(a,);q.append(w)
                tree.add((v,a) if a<r else (w,a-r))
    if len(paths)!=d:return None
    gens={}
    for v in range(d):
        for a in range(r):
            if (v,a) not in tree:
                w=trans[a][v]
                g=red(paths[v]+(a,)+inverse(paths[w],r),r)
                assert g
                gens[v,a]=g
    assert len(gens)==d*r-(d-1)
    return paths,trans,tree,gens
def terminal(w):
    seen={w};pending=[w];ends=set()
    while pending:
        q=pending.pop();out=[q[:i]+q[i+2:] for i in range(len(q)-1) if q[i]==opp(q[i+1])]
        if not out:ends.add(q)
        for a in out:
            if a not in seen:seen.add(a);pending.append(a)
    return ends
def at0(word,ps):
    v=0
    for x in word:v=ps[x][v]
    return v

class AA07Regression(unittest.TestCase):
    def test_01_source_structure(self):
        ls=re.findall(r"\\label\{([^}]+)\}",SRC)
        self.assertEqual((len(ls),len(set(ls))), (28,28))
        self.assertEqual((SRC.count(r"\begin{proof}"),SRC.count(r"\end{proof}")),(15,15))
    def test_02_internal_references(self):
        ls=set(re.findall(r"\\label\{([^}]+)\}",SRC))
        rs=set(re.findall(r"\\(?:ref|eqref|autoref|pageref|nameref)\{([^}]+)\}",SRC))
        self.assertTrue(rs<=ls)
    def test_03_reduction_confluence(self):
        for w in words(7):self.assertEqual(terminal(w),{red(w)})
    def test_04_inverse_pair_insertion(self):
        for w in words(5):
            for i in range(len(w)+1):
                for x in range(4):self.assertEqual(red(w),red(w[:i]+(x,opp(x))+w[i:]))
    def test_05_associative_reduced_product(self):
        short=[w for w in words(2) if w==red(w)]
        for a,b,c in product(short,repeat=3):self.assertEqual(red(red(a+b)+c),red(a+red(b+c)))
    def test_06_inverse_and_identity(self):
        for w in words(5):
            w=red(w)
            self.assertEqual(red(w+inverse(w)),())
            self.assertEqual(red(inverse(w)+w),())
            self.assertEqual(red(w+()),w)
    def test_07_reduced_word_count(self):
        for n in range(1,7):self.assertEqual(sum(len(w)==n and w==red(w) for w in words(n)),4*3**(n-1))
    def test_08_universal_hom_s3(self):
        G=tuple(permutations(range(3)))
        for a,b in product(G,repeat=2):
            imgs=(a,b,p_inv(a),p_inv(b))
            def value(w):
                x=(0,1,2)
                for s in w:x=p_mul(x,imgs[s])
                return x
            for w in words(4):self.assertEqual(value(w),value(red(w)))
    def test_09_cyclic_dihedral_relations(self):
        for n in (3,4,5,6,7):
            r=tuple((i+1)%n for i in range(n));s=tuple((-i)%n for i in range(n))
            self.assertEqual(p_mul(p_mul(s,r),s),p_inv(r))
    def test_10_nontrivial_free_commutator(self):
        self.assertNotEqual(red((0,1,2,3)),())
        self.assertNotEqual(red((0,0)),())
    def test_11_index_two_basis(self):
        data=basis(((1,0),(0,1)))
        self.assertEqual(set(data[3].values()),{(0,0),(1,),(0,1,2)})
    def test_12_all_transitive_actions_small(self):
        for d in range(1,5):
            G=tuple(permutations(range(d)))
            for a,b in product(G,repeat=2):
                g=basis((a,b))
                if g is not None:self.assertEqual(len(g[3]),d+1)
    def test_13_infinite_index_generators(self):
        g=[red((0,)*n+(1,)+(2,)*n) if n>=0 else red((2,)*(-n)+(1,)+(0,)*(-n)) for n in range(-5,6)]
        self.assertEqual(len(set(g)),11)
    def test_14_ranks_count_homomorphisms(self):
        for r in range(6):self.assertEqual(len(tuple(product((0,1),repeat=r))),2**r)
    def test_15_normal_closure_s3(self):
        G=tuple(permutations(range(3)));t=(1,0,2);c=(1,2,0)
        def conj(x,g):return p_mul(p_mul(g,x),p_inv(g))
        self.assertEqual(len({conj(t,g) for g in G}),3)
        self.assertEqual(len({conj(c,g) for g in G}),2)
    def test_16_schreier_rewriting_all_small_loops(self):
        for d in range(1,4):
            for a,b in product(permutations(range(d)),repeat=2):
                data=basis((a,b))
                if data is None:continue
                paths,ps,tree,gens=data
                for w in words(5):
                    w=red(w)
                    if at0(w,ps):continue
                    v=0;written=()
                    for s in w:
                        u=ps[s][v]
                        factor=gens.get((v,s),()) if s<2 else inverse(gens.get((u,s-2),()))
                        written=red(written+factor);v=u
                    self.assertEqual(written,w)
    def test_17_no_short_relations_in_schreier_generators(self):
        checked=0
        for d in range(1,5):
            for a,b in product(permutations(range(d)),repeat=2):
                data=basis((a,b))
                if data is None:continue
                pos=list(data[3].values());m=len(pos);syms=pos+[inverse(x) for x in pos]
                for k in range(1,4):
                    for choice in product(range(2*m),repeat=k):
                        if any((choice[i]+m)%(2*m)==choice[i+1] for i in range(k-1)):continue
                        self.assertNotEqual(red(tuple(x for t in choice for x in syms[t])),())
                checked+=1
        self.assertGreater(checked,100)
    def test_18_schreier_ranks_one_and_three(self):
        for r in (1,3):
            for d in range(1,5):
                shift=tuple((i+1)%d for i in range(d));fix=tuple(range(d))
                self.assertEqual(len(basis((shift,)+(fix,)*(r-1))[3]),1+d*(r-1))
    def test_19_parallel_positive_edges(self):
        paths,ps,tree,gens=basis(((1,0),(1,0)))
        self.assertEqual(len(tree),1)
        self.assertNotEqual(gens[0,1],gens[1,1])
    def test_20_empty_alphabet(self):
        self.assertEqual(red((),0),())
        self.assertEqual(1+1*(0-1),0)
    def test_21_infinite_family_short_relations(self):
        g={n:red((0,)*n+(1,)+(2,)*n) if n>=0 else red((2,)*(-n)+(1,)+(0,)*(-n)) for n in range(-12,13)}
        self.assertEqual(len(set(g.values())),25)
        for i,j,k in product((-8,-3,0,2,7),repeat=3):
            if i==j or j==k:continue
            self.assertNotEqual(red(g[i]+inverse(g[j])+g[k]),())

if __name__=="__main__":unittest.main()
