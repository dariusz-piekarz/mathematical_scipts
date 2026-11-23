#!/usr/bin/env python3
"""Independent finite audit models for historical graph/knot chapters 16--18.

Pure standard library. Checks cochain Hodge rank with weighted inner products,
Cayley graph balls and C2*C3 Bass--Serre tree cosets, Laurent determinant
identities for Seifert stabilization, Fox colorings, Jones normalization,
and Arf Gauss sums. Finite arithmetic is NOT proof of cited global theorems.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
DIR=ROOT/"chapters/pl/graph_and_knot_theory"


def rank_q(mat):
    if not mat: return 0
    a=[[Fraction(x) for x in row] for row in mat]
    n=len(a);m=len(a[0]);i=0
    for j in range(m):
        k=next((k for k in range(i,n) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        pivot=a[i][j]
        a[i]=[v/pivot for v in a[i]]
        for k in range(n):
            if k!=i and a[k][j]:
                ratio=a[k][j]
                a[k]=[x-ratio*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==n:break
    return i


def transpose(a):
    return [list(x) for x in zip(*a)] if a else []


def matmul(a,b):
    if not a:return []
    if not b:return [[] for _ in a]
    assert len(a[0])==len(b)
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def matsum(a,b):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(a,b)]


def check_hodge(facets):
    # Independent chain matrices over Q; compare Hodge kernels to Betti numbers.
    S={tuple(sorted(sub)) for facet in facets
       for k in range(1,len(facet)+1) for sub in combinations(facet,k)}
    vs=sorted(x for x in S if len(x)==1)
    es=sorted(x for x in S if len(x)==2)
    fs=sorted(x for x in S if len(x)==3)
    index_v={x:i for i,x in enumerate(vs)}
    index_e={x:i for i,x in enumerate(es)}
    B1=[[int(v[0]==e[1])-int(v[0]==e[0]) for e in es] for v in vs]
    B2=[[sum((-1)**i for i,face in enumerate(combinations(f,2))
             if face==e) for f in fs] for e in es]
    # For each ordered triangle (a,b,c), ∂[abc]=[bc]-[ac]+[ab].
    B2=[[sum((1 if i!=1 else -1) for i,face
             in enumerate(((f[1],f[2]),(f[0],f[2]),(f[0],f[1])))
             if face==e) for f in fs] for e in es]
    assert matmul(B1,B2)==[[0]*len(fs) for _ in vs]
    r1=rank_q(B1);r2=rank_q(B2)
    b1=len(es)-r1-r2
    # Weighted adjoints δ0=W0^-1 B1 W1, δ1=W1^-1 B2 W2.
    # Δ1 = B1^T δ0 + δ1 B2^T.
    for weights in (False,True):
        w0=[(i+2 if weights else 1) for i in range(len(vs))]
        w1=[(i+3 if weights else 1) for i in range(len(es))]
        w2=[(i+4 if weights else 1) for i in range(len(fs))]
        delta0=[[Fraction(B1[i][j]*w1[j],w0[i])
                 for j in range(len(es))] for i in range(len(vs))]
        delta1=[[Fraction(B2[i][j]*w2[j],w1[i])
                 for j in range(len(fs))] for i in range(len(es))]
        upper=matmul(transpose(B1),delta0)
        lower=matmul(delta1,transpose(B2)) if fs else [
            [0]*len(es) for _ in es]
        lap=matsum(upper,lower)
        assert len(es)-rank_q(lap)==b1
        # Weighted self-adjointness: W1Δ1 is symmetric.
        weighted=[[w1[i]*lap[i][j] for j in range(len(es))]
                  for i in range(len(es))]
        assert weighted==transpose(weighted)
        for seed in range(4):
            x=[(-1)**(i+seed)*((i+seed)%3) for i in range(len(es))]
            assert sum(x[i]*weighted[i][j]*x[j]
                       for i in range(len(es)) for j in range(len(es)))>=0
    return len(es),b1


def reduce_word(word):
    out=[]
    for s in word:
        if out and out[-1]==-s:out.pop()
        else:out.append(s)
    return tuple(out)


def cayley_free_ball(rank,depth):
    alphabet=tuple(x for i in range(1,rank+1) for x in (i,-i))
    words={()}
    frontier={()}
    for _ in range(depth):
        nxt={reduce_word(w+(s,)) for w in frontier for s in alphabet}
        words|=nxt
        frontier=nxt
    edges={tuple(sorted((w,reduce_word(w+(s,)))))
           for w in words for s in alphabet if reduce_word(w+(s,)) in words}
    # Every non-root word has a unique parent obtained by deleting its last letter.
    assert len(edges)==len(words)-1
    assert all((w[:-1],w) in edges or (w,w[:-1]) in edges
               for w in words if w)
    return len(words)


def multiply_syllable(word,typ,val):
    mod=2 if typ=="A" else 3
    if val==0:return tuple(word)
    w=list(word)
    if w and w[-1][0]==typ:
        new=(w[-1][1]+val)%mod
        w.pop()
        if new:w.append((typ,new))
    else:w.append((typ,val))
    return tuple(w)


def c2c3_tree_ball(depth=5):
    words={()};frontier={()}
    letters=(("A",1),("B",1),("B",2))
    for _ in range(depth):
        nxt={multiply_syllable(w,*s) for w in frontier for s in letters}
        words|=nxt;frontier=nxt
    # Edge labeled g joins cosets gA and gB; canonical coset representative
    # removes the final syllable if it belongs to its corresponding subgroup.
    def coset(g,typ):
        return (typ, g[:-1] if g and g[-1][0]==typ else g)
    edges={(coset(w,"A"),coset(w,"B")) for w in words}
    vertices={v for edge in edges for v in edge}
    # The finite ball is a tree; interior degrees equal [C2:1]=2 and [C3:1]=3.
    assert len(edges)==len(vertices)-1
    incident={v:0 for v in vertices}
    for a,b in edges:incident[a]+=1;incident[b]+=1
    assert all(incident[v]==(2 if v[0]=="A" else 3)
               for v in vertices if len(v[1])<=depth-1)
    return len(vertices),len(edges)


def poly_add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}


def poly_mul(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():out[i+j]=out.get(i+j,0)+v*w
    return {k:v for k,v in out.items() if v}


def poly_scale(a,c):
    return {k:v*c for k,v in a.items() if v*c}


def poly_det(matrix):
    n=len(matrix)
    if not n:return {0:1}
    total={}
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        value={0:1}
        for i in range(n):value=poly_mul(value,matrix[i][perm[i]])
        total=poly_add(total,poly_scale(value,-1 if inversions%2 else 1))
    return total


def alexander_matrix(V):
    n=len(V)
    return [[poly_add({1:V[i][j]},{0:-V[j][i]})
             for j in range(n)] for i in range(n)]


def shifted(poly,k):
    return {degree+k:val for degree,val in poly.items()}


def enlarged(V,u,v,z,form):
    n=len(V)
    rows=[list(row)+[u[i],0] for i,row in enumerate(V)]
    rows.append(list(v)+[z,0 if form==0 else 1])
    rows.append([0]*n+[1 if form==0 else 0,0])
    return rows


def old_wrong_enlargement(V,u,v,form):
    n=len(V)
    if form==0:
        rows=[list(row)+[0,0] for row in V]
        rows.append(list(u)+[0,0]);rows.append(list(v)+[1,0])
    else:
        rows=[list(row)+[u[i],v[i]] for i,row in enumerate(V)]
        rows.append([0]*n+[0,1]);rows.append([0]*n+[0,0])
    return rows


def check_seifert_alexander():
    examples=(
        [[1,0],[-1,1]],
        [[1,0],[-1,-1]],
        [[1,0,0,0],[-1,1,0,0],[0,0,1,0],[0,0,-1,1]],
        [])
    count=0
    for V in examples:
        n=len(V)
        delta=poly_det(alexander_matrix(V))
        for mode in (0,1):
            for seed in (-2,-1,0,1,2):
                u=[(i+1)*seed for i in range(n)]
                v=[(i+2)*(seed-1) for i in range(n)]
                for z in (-2,0,3):
                    ext=enlarged(V,u,v,z,mode)
                    assert poly_det(alexander_matrix(ext))==shifted(delta,1)
                    count+=1
    trefoil=examples[0]; fig8=examples[1]
    assert poly_det(alexander_matrix(trefoil))=={2:1,1:-1,0:1}
    assert poly_det(alexander_matrix(fig8))=={2:-1,1:3,0:-1}
    assert sum(v*(-1)**k for k,v in poly_det(alexander_matrix(trefoil)).items())==3
    assert sum(v*(-1)**k for k,v in poly_det(alexander_matrix(fig8)).items())==-5
    # Regression: the two PREVIOUSLY printed matrix shapes were wrong.
    for mode in (0,1):
        bad=old_wrong_enlargement(trefoil,[1,0],[1,0],mode)
        assert poly_det(alexander_matrix(bad))=={2:1}
        assert poly_det(alexander_matrix(bad))!=shifted(
            poly_det(alexander_matrix(trefoil)),1)
    return count


def check_fox_coloring():
    # Trefoil: 2a=b+c, 2b=a+c, 2c=a+b (mod n).
    counts=[]
    for n in range(2,14):
        count=sum((2*a-b-c)%n==0 and
                  (2*b-a-c)%n==0 and
                  (2*c-a-b)%n==0
                  for a,b,c in product(range(n),repeat=3))
        assert count==n*gcd(n,3), (n,count)
        counts.append((n,count))
    return counts


def check_jones_trefoil():
    # Two-strand Temperley--Lieb: e²=δe, b=A1+A^-1e.
    delta={2:-1,-2:-1}
    b=({1:1},{-1:1})
    def multiply(x,y):
        a=poly_mul(x[0],y[0])
        mixed=poly_add(poly_mul(x[0],y[1]),poly_mul(x[1],y[0]))
        mixed=poly_add(mixed,poly_mul(delta,poly_mul(x[1],y[1])))
        return a,mixed
    cube=multiply(multiply(b,b),b)
    bracket=poly_add(poly_mul(cube[0],delta),cube[1])
    assert bracket=={5:-1,-3:-1,-7:1}
    normalized=shifted(poly_scale(bracket,-1),-9)
    assert normalized=={-4:1,-12:1,-16:-1}
    # substituting t=A^-4 gives V(t)=t+t³-t⁴.
    assert {(-e)//4:v for e,v in normalized.items()}=={1:1,3:1,4:-1}
    return bracket



def tl_reduce(word):
    """Reduce the 3-strand Temperley--Lieb basis word to (scalar, basis)."""
    w=list(word);scalar={0:1}
    while True:
        updated=False
        for i in range(len(w)-1):
            if w[i]==w[i+1]:
                scalar=poly_mul(scalar,{2:-1,-2:-1})  # e_i²=δe_i
                w=w[:i]+w[i+1:]
                updated=True
                break
        if updated:continue
        for i in range(len(w)-2):
            if w[i]==w[i+2] and w[i]!=w[i+1]:
                w=w[:i+1]+w[i+3:]  # e1 e2 e1=e1, e2 e1 e2=e2
                updated=True
                break
        if not updated:break
    assert tuple(w) in ((),(1,),(2,),(1,2),(2,1)),w
    return scalar,tuple(w)


def tl_add(a,b):
    out=dict(a)
    for basis,coefficient in b.items():
        out[basis]=poly_add(out.get(basis,{}),coefficient)
    return {basis:v for basis,v in out.items() if v}


def tl_mul(a,b):
    result={}
    for wa,pa in a.items():
        for wb,pb in b.items():
            scalar,word=tl_reduce(wa+wb)
            term=poly_mul(poly_mul(pa,pb),scalar)
            result[word]=poly_add(result.get(word,{}),term)
    return {word:v for word,v in result.items() if v}


def check_tl_reidemeister():
    identity={():{0:1}}
    braids={i:{():{1:1},(i,):{-1:1}} for i in (1,2)}
    inverses={i:{():{-1:1},(i,):{1:1}} for i in (1,2)}
    for i in (1,2):
        assert tl_mul(braids[i],inverses[i])==identity
        assert tl_mul(inverses[i],braids[i])==identity
    left=tl_mul(tl_mul(braids[1],braids[2]),braids[1])
    right=tl_mul(tl_mul(braids[2],braids[1]),braids[2])
    assert left==right
    assert left=={
        (): {3:1},
        (1,): {1:1},
        (2,): {1:1},
        (1,2): {-1:1},
        (2,1): {-1:1},
    },left
    return len(left)


def check_arf_gauss():
    cases=0
    for g in (1,2):
        for coefficients in product((0,1),repeat=2*g):
            val=0
            for x in product((0,1),repeat=2*g):
                q=sum(x[2*i]*x[2*i+1]+coefficients[2*i]*x[2*i]+
                      coefficients[2*i+1]*x[2*i+1] for i in range(g))%2
                val+=(-1)**q
            arf=sum(coefficients[2*i]*coefficients[2*i+1]
                    for i in range(g))%2
            assert val==(2**g)*(-1 if arf else 1)
            cases+=1
    return cases



def check_arf_enlargement_isometry():
    """Independent brute force over F2; checks every input to the shear isometry."""
    matrices=[
        [],[[1,0],[-1,1]],[[1,0],[-1,-1]],
        [[1,0,0,0],[-1,1,0,0],[0,0,1,0],[0,0,-1,1]],
    ]
    checked=0
    def q(matrix,vector):
        return sum(vector[i]*matrix[i][j]*vector[j]
                   for i in range(len(vector)) for j in range(len(vector)))%2
    for V in matrices:
        n=len(V)
        for u in product(range(2),repeat=n):
            for v in product(range(2),repeat=n):
                for z in (0,1):
                    for mode in (0,1):
                        Vp=enlarged(V,list(u),list(v),z,mode)
                        for x in product(range(2),repeat=n):
                            for sb,tb in product(range(2),repeat=2):
                                shear=(tb+sum((u[i]+v[i])*x[i]
                                              for i in range(n))+z*sb)%2
                                assert q(Vp,x+(sb,tb))==(q(V,x)+sb*shear)%2
                                checked+=1
    return checked


def check_conway_arf_congruence():
    """Algebraic consequence Δsym(-1)=∇(2i), modulo 8."""
    tests=0
    for a2 in range(-10,11):
        for a4 in (-3,0,4):
            for a6 in (-2,0,3):
                delta=1-4*a2+16*a4-64*a6
                assert delta%8==(1-4*(a2%2))%8
                assert ((delta%8==1) == (a2%2==0))
                tests+=1
    return tests


def test_source():
    names=[
        "16-od-triangulacji-do-topologii-i-geometrii-rozmaitosci.tex",
        "17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex",
        "18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex",
    ]
    a,b,c=[(DIR/name).read_text(encoding="utf-8") for name in names]
    assert "bazach dualnych" in a
    assert r"\label{thm:tg-finite-hodge}" in a
    assert r"\label{ch:tg-bass-serre}" in b
    assert r"\label{def:kt-four-ball-genus}" in c
    assert r"\label{thm:kt-signature-four-genus}" in c
    assert r"V&u&0\\ v^T&z&0\\0&1&0" in c
    assert r"V&u&0\\v^T&z&1\\0&0&0" in c
    assert r"b_1b_2b_1=b_2b_1b_2" in c
    assert r"\label{thm:kt-arf-conway-slice}" in c
    assert r"\label{def:kt-peripheral}" in c
    assert r"\label{thm:kt-peripheral-homology}" in c
    assert r"t'=t+(u+v)^Tx+zs" in c
    assert "Jawna przerwa na dolnym fragmencie" in c


if __name__=="__main__":
    test_source()
    print("PASS finite weighted Hodge cochain models:",
          [check_hodge(facets) for facets in (
              {(0,1),(1,2),(0,2)},
              {(0,1,2)},
              {(0,1,2),(0,1,3),(0,2,3),(1,2,3)})])
    print("PASS Cayley free balls:",[(r,cayley_free_ball(r,3)) for r in (1,2,3)])
    print("PASS C2*C3 Bass--Serre truncated coset tree:",c2c3_tree_ball())
    print("PASS Seifert S-enlargement Laurent determinant identities:",
          check_seifert_alexander())
    print("PASS Fox trefoil coloring moduli:",check_fox_coloring())
    print("PASS Jones trefoil TL bracket:",check_jones_trefoil())
    print("PASS Temperley--Lieb RII/RIII exact braid identities:",check_tl_reidemeister())
    print("PASS Arf quadratic Gauss sums:",check_arf_gauss())
    print("PASS Arf quadratic S-enlargement isometries over F2:",check_arf_enlargement_isometry())
    print("PASS Arf-Conway mod 8 congruences:",check_conway_arf_congruence())
