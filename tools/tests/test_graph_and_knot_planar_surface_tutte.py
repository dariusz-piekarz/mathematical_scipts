#!/usr/bin/env python3
"""Graph-and-knot global audit: historical 10-12, finite exact counterexample search.

Independent constructions:
- spherical cellular rotation systems and genus from permutations;
- boundary-chain homology ranks over the rationals;
- Tutte subset formula vs independent deletion/contraction recursion;
- chromatic inclusion-exclusion vs direct colorings;
- orientable sphere duality and flow/color bijection.
No external dependencies, no Monte Carlo. These are finite tests, not
substitutes for the difficult Kuratowski direction or other general proofs.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]


def pairs(n):
    return tuple(combinations(range(n),2))


def count_components(n, edges):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for u,v in edges:
        parent[root(u)]=root(v)
    return len({root(u) for u in range(n)})


def tutte_subset(n, edges, x, y):
    m=len(edges)
    kE=count_components(n, edges)
    total=0
    for mask in range(1<<m):
        selected=[e for i,e in enumerate(edges) if mask>>i&1]
        kA=count_components(n,selected)
        total+=(x-1)**(kA-kE)*(y-1)**(len(selected)-n+kA)
    return total


def contract(n, edges, idx):
    u,v=edges[idx]
    assert u!=v
    mapping=[(-1 if w==v else w-(w>v)) for w in range(n)]
    mapping[v]=mapping[u]
    return n-1,tuple(sorted(tuple(sorted((mapping[a],mapping[b])))
                            for i,(a,b) in enumerate(edges) if i!=idx))


@lru_cache(maxsize=None)
def tutte_recursive(n, edges, x, y):
    if not edges:
        return 1
    u,v=edges[0]
    removal=tuple(edges[1:])
    if u==v:
        return y*tutte_recursive(n,removal,x,y)
    nc,ec=contract(n,edges,0)
    if count_components(n,removal)>count_components(n,edges):
        return x*tutte_recursive(nc,ec,x,y)
    return (tutte_recursive(n,removal,x,y)+
            tutte_recursive(nc,ec,x,y))


def chromatic_direct(n, edges, q):
    return sum(all(color[u]!=color[v] for u,v in edges)
               for color in product(range(q),repeat=n))


def chromatic_inclusion(n, edges, q):
    return sum((-1)**len(s)*q**count_components(n,[edges[i] for i in s])
               for k in range(len(edges)+1)
               for s in combinations(range(len(edges)),k))


def rotation_faces(n, edges, limit=None):
    """Enumerate oriented ribbon graph rotations (including all cell genera)."""
    nbr=[[] for _ in range(n)]
    for u,v in edges:
        assert u!=v
        nbr[u].append(v);nbr[v].append(u)
    opts=[]
    for ns in nbr:
        q=tuple(sorted(ns))
        opts.append(tuple((q[0],)+tail for tail in permutations(q[1:])) if q else ((),))
    for idx, rot in enumerate(product(*opts)):
        if limit is not None and idx>=limit:
            return
        successor={}
        for v, order in enumerate(rot):
            for i,u in enumerate(order):
                successor[(u,v)]=(v,order[(i+1)%len(order)])
        unseen=set(successor)
        faces=[];face_of={}
        while unseen:
            first=min(unseen)
            cur=first
            face=[]
            while cur in unseen:
                unseen.remove(cur)
                face_of[cur]=len(faces)
                face.append(cur)
                cur=successor[cur]
            assert cur==first
            faces.append(tuple(face))
        yield faces,face_of,rot


def first_sphere_rotation(n,edges):
    # Necessary Euler bound prevents factorial rotation enumeration of K5.
    if n>=3 and len(edges)>3*n-6:
        return None
    for faces,face_of,rot in rotation_faces(n,edges):
        if n-len(edges)+len(faces)==2:
            return faces,face_of,rot
    return None


def rank_q(mat):
    if not mat:return 0
    a=[[Fraction(v) for v in row] for row in mat]
    n=len(a);m=len(a[0]);r=0
    for col in range(m):
        pivot=next((i for i in range(r,n) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        scale=a[r][col]
        a[r]=[t/scale for t in a[r]]
        for i in range(n):
            if i!=r and a[i][col]:
                factor=a[i][col]
                a[i]=[x-factor*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r


def check_surface_complex(n, edges, faces):
    m=len(edges);f=len(faces)
    B1=[[int(v==w)-int(u==w) for u,v in edges] for w in range(n)]
    index={e:i for i,e in enumerate(edges)}
    B2=[[0 for j in range(f)] for i in range(m)]
    for fi,face in enumerate(faces):
        for u,v in face:
            e=tuple(sorted((u,v)))
            i=index[e]
            B2[i][fi]+=1 if e==(u,v) else -1
    assert all(sum(B1[i][j]*B2[j][k] for j in range(m))==0
               for i in range(n) for k in range(f))
    r1=rank_q(B1)
    r2=rank_q(B2)
    assert r1==n-1 and r2==f-1
    g2=2-n+m-f
    assert g2>=0 and g2%2==0
    assert m-r1-r2==g2
    assert n-r1==1 and f-r2==1
    return g2//2


def dual_edges(edges, face_of):
    # Preserve original edge indices: each edge e corresponds to dual e*.
    # Sorting the dual edge *sequence* would corrupt complementary-tree tests.
    return tuple(tuple(sorted((face_of[(u,v)],face_of[(v,u)])))
                 for u,v in edges)


def count_flows(n, edges, q):
    total=0
    for j in product(range(q),repeat=len(edges)):
        if any(x==0 for x in j):
            continue
        boundary=[0]*n
        for (u,v),t in zip(edges,j):
            boundary[u]-=t
            boundary[v]+=t
        if all(b%q==0 for b in boundary):
            total+=1
    return total


def test_simple_tutte():
    graphs=0
    chromatic_cases=0
    for n in range(0,6):
        E=pairs(n)
        for mask in range(1<<len(E)):
            edges=tuple(e for i,e in enumerate(E) if mask>>i&1)
            for x,y in ((2,2),(2,1),(1,1),(3,4)):
                a=tutte_subset(n,edges,x,y)
                b=tutte_recursive(n,edges,x,y)
                assert a==b,(n,edges,x,y,a,b)
            for q in (2,3,4):
                direct=chromatic_direct(n,edges,q)
                incl=chromatic_inclusion(n,edges,q)
                c=count_components(n,edges)
                via_tutte=(-1)**(n-c)*(q**c)*tutte_subset(n,edges,1-q,0)
                assert direct==incl==via_tutte,(n,edges,q,direct,incl,via_tutte)
                chromatic_cases+=1
            # T(1,1) counts maximal spanning forests; if connected, trees.
            forests=sum(count_components(n,[edges[i] for i in range(len(edges))
                                               if mask>>i&1])==count_components(n,edges)
                        and len([i for i in range(len(edges)) if mask>>i&1])
                            ==n-count_components(n,edges)
                        for mask in range(1<<len(edges)))
            assert tutte_subset(n,edges,1,1)==forests
            graphs+=1
    # A loop and a multiedge: not covered by simple graph enumeration.
    specials=[(1,((0,0),)),(2,((0,1),(0,1))),
              (2,((0,1),(0,1),(0,1))),(2,((0,1),(0,1),(0,0)))]
    for n,edges in specials:
        for x,y in ((2,2),(1,1),(3,4)):
            assert tutte_recursive(n,edges,x,y)==tutte_subset(n,edges,x,y)
        for q in (2,3):
            assert chromatic_direct(n,edges,q)==chromatic_inclusion(n,edges,q)
    return graphs,chromatic_cases


def test_surface_and_dual():
    connected=0
    spherical=0
    rotations=0
    duals=0
    max_genus=0
    for n in range(2,6):
        E=pairs(n)
        for mask in range(1<<len(E)):
            edges=tuple(e for i,e in enumerate(E) if mask>>i&1)
            if not edges or len(edges)>7 or count_components(n,edges)!=1:
                continue
            connected+=1
            found_sphere=False
            for faces, face_of, rot in rotation_faces(n,edges):
                rotations+=1
                genus=check_surface_complex(n,edges,faces)
                max_genus=max(max_genus,genus)
                if genus:
                    continue
                if found_sphere:
                    continue
                found_sphere=True
                spherical+=1
                de=dual_edges(edges,face_of)
                f=len(faces)
                for x,y in ((2,3),(3,2),(1,1)):
                    assert tutte_subset(n,edges,y,x)==tutte_subset(f,de,x,y), (
                        "Tutte sphere dual",n,edges,faces
                    )
                for q in (2,3):
                    colors=chromatic_direct(f,de,q)
                    flows=count_flows(n,edges,q)
                    assert colors==q*flows,("color-flow",n,edges,q,colors,flows)
                # For each spanning tree, complement in the dual must be a tree.
                for idx in combinations(range(len(edges)),n-1):
                    if count_components(n,[edges[i] for i in idx])!=1:
                        continue
                    comp=[de[i] for i in range(len(edges)) if i not in idx]
                    assert len(comp)==f-1 and count_components(f,comp)==1
                duals+=1
    # Rotation of theta multigraph: three faces on sphere vs one on torus.
    darts=("a1","a2","a3","b1","b2","b3")
    alpha={f"a{i}":f"b{i}" for i in (1,2,3)}
    alpha.update({v:k for k,v in list(alpha.items())})
    def theta_cycles(b_order):
        a_order=("a1","a2","a3")
        successor={}
        for order in (a_order,b_order):
            for i,x in enumerate(order):
                successor[x]=order[(i+1)%3]
        unseen=set(darts)
        cycles=[]
        while unseen:
            start=min(unseen);x=start;one=[]
            while x in unseen:
                unseen.remove(x);one.append(x);x=successor[alpha[x]]
            assert x==start
            cycles.append(one)
        return cycles
    assert len(theta_cycles(("b1","b3","b2")))==3
    assert len(theta_cycles(("b1","b2","b3")))==1
    # Nonplanar K5 and K3,3; K4 is planar and not outerplanar.
    assert first_sphere_rotation(5,pairs(5)) is None
    k33=tuple((i,j) for i in range(3) for j in range(3,6))
    assert first_sphere_rotation(6,k33) is None
    assert first_sphere_rotation(4,pairs(4)) is not None
    return connected,rotations,spherical,duals,max_genus


def test_outerplanar_and_five_color():
    checked=0;outer=0
    for n in range(2,6):
        E=pairs(n)
        for mask in range(1<<len(E)):
            edges=tuple(e for i,e in enumerate(E) if mask>>i&1)
            if count_components(n,edges)!=1 or len(edges)>7:
                continue
            rotation=first_sphere_rotation(n,edges)
            if rotation is None:
                continue
            checked+=1
            # Face is outer if each vertex is incident to at least one dart
            # in that facial orbit.
            found=False
            for faces,__,_ in rotation_faces(n,edges):
                if n-len(edges)+len(faces)!=2:
                    continue
                if any(len({u for arc in face for u in arc})==n for face in faces):
                    found=True
                    break
            if found:
                outer+=1
                assert len(edges)<=2*n-3,("outerplanar bound",n,edges)
                assert chromatic_direct(n,edges,3)>0,("outerplanar 3 coloring",n,edges)
            assert chromatic_direct(n,edges,5)>0
    # The 4-clique cannot have all vertices on one face.
    assert all(not any(len({u for arc in face for u in arc})==4 for face in faces)
               for faces,_,_ in rotation_faces(4,pairs(4))
               if 4-6+len(faces)==2)
    # K2,3 is not outerplanar (but is planar).
    k23=tuple((i,j) for i in range(2) for j in range(2,5))
    assert first_sphere_rotation(5,k23) is not None
    assert all(not any(len({u for arc in face for u in arc})==5 for face in faces)
               for faces,_,_ in rotation_faces(5,k23)
               if 5-len(k23)+len(faces)==2)
    # A wheel on six vertices has a 5-coloring, still a finite check.
    wheel=tuple(sorted(set([(i,(i+1)%5) for i in range(5)]+[(i,5) for i in range(5)])))
    assert first_sphere_rotation(6,wheel) is not None
    assert chromatic_direct(6,wheel,5)>0
    return checked,outer


def source_integration():
    cat=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    bk=next(b for b in cat["books"] if b["id"]=="graph_and_knot_theory")
    assert len(bk["chapters"])==44
    paths={Path(p).name[:2]:ROOT/p for p in bk["chapters"]}
    for c in ("10","11","12"):
        s=paths[c].read_text(encoding="utf-8")
        assert s.count(r"\begin{proof}")==s.count(r"\end{proof}")
    a=paths["10"].read_text(encoding="utf-8")
    b=paths["11"].read_text(encoding="utf-8")
    c=paths["12"].read_text(encoding="utf-8")
    assert "Odwrotna implikacja" in a and "Przyjmujemy ją tutaj" in a
    assert r"thm:tg-rotation-genus" in b and r"thm:tg-surface-homology" in b
    assert r"thm:tg-tutte-recursion" in c and r"thm:tg-flow-color-dual" in c
    assert r"\tau_V(G)" in paths["05"].read_text(encoding="utf-8")
    assert r"\tau(G)" in c and r"\tau(G)" in paths["08"].read_text(encoding="utf-8")


if __name__=="__main__":
    source_integration()
    print("PASS Tutte recursion, chromatic and forests:",test_simple_tutte())
    print("PASS rotations, cellular homology and planar duals:",test_surface_and_dual())
    print("PASS outerplanarity/five colors:",test_outerplanar_and_five_color())
    print("PASS source declarations and 44-source integration")
