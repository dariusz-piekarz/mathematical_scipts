#!/usr/bin/env python3
"""Global graph/knot audit: historical chapters 07--09 (exact finite models).

Independent checks for finite graph coverings, homotopy ranks, Kirchhoff's
matrix-tree theorem (weighted/unweighted), spectral determinant identity,
resistance and Dirichlet energy, planar rotation systems and face coloring.
No external dependencies, no random sampling, exact Fraction arithmetic.
These tests complement and DO NOT replace proofs for arbitrary finite graphs.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[2]


def edge_pairs(n):
    return tuple(combinations(range(n),2))


def components(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen=set()
    groups=[]
    for root in range(n):
        if root in seen:
            continue
        current={root}
        queue=[root]
        seen.add(root)
        for u in queue:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);current.add(v);queue.append(v)
        groups.append(current)
    return groups


def is_connected(n,edges):
    return n>=1 and len(components(n,edges))==1


def exact_determinant(matrix):
    """Rational elimination, preserving exactness and pivot signs."""
    n=len(matrix)
    if n==0:
        return Fraction(1)
    a=[[Fraction(x) for x in row] for row in matrix]
    out=Fraction(1)
    for col in range(n):
        pivot=next((r for r in range(col,n) if a[r][col]!=0),None)
        if pivot is None:
            return Fraction(0)
        if pivot!=col:
            a[col],a[pivot]=a[pivot],a[col]
            out=-out
        pivot_val=a[col][col]
        out*=pivot_val
        for i in range(col+1,n):
            if a[i][col]!=0:
                scale=a[i][col]/pivot_val
                for j in range(col+1,n):
                    a[i][j]-=scale*a[col][j]
                a[i][col]=0
    return out


def solve(matrix,rhs):
    """Independent Gaussian elimination over rational numbers."""
    n=len(rhs)
    if not n:
        return []
    a=[[Fraction(x) for x in row]+[Fraction(rhs[i])]
       for i,row in enumerate(matrix)]
    for col in range(n):
        piv=next((r for r in range(col,n) if a[r][col]),None)
        assert piv is not None, "Dirichlet system unexpectedly singular"
        a[col],a[piv]=a[piv],a[col]
        div=a[col][col]
        a[col]=[x/div for x in a[col]]
        for row in range(n):
            if row!=col:
                mult=a[row][col]
                if mult:
                    a[row]=[x-mult*y for x,y in zip(a[row],a[col])]
    return [a[i][-1] for i in range(n)]


def laplacian(n,edges,weights):
    L=[[Fraction(0) for j in range(n)] for i in range(n)]
    for (u,v),w in zip(edges,weights):
        L[u][u]+=w
        L[v][v]+=w
        L[u][v]-=w
        L[v][u]-=w
    return L


def tree_weight(n,edges,weights):
    if not n:
        return Fraction(0)
    if n==1:
        return Fraction(1)
    result=Fraction(0)
    for idx in combinations(range(len(edges)),n-1):
        selected=[edges[i] for i in idx]
        if is_connected(n,selected):
            term=Fraction(1)
            for i in idx:
                term*=weights[i]
            result+=term
    return result


def audit_kirchhoff(n,edges):
    m=len(edges)
    for weights in ([1]*m,[(i%3)+1 for i in range(m)]):
        L=laplacian(n,edges,weights)
        cofactor=exact_determinant([row[:-1] for row in L[:-1]])
        expected=tree_weight(n,edges,weights)
        assert cofactor==expected,(n,edges,weights,cofactor,expected)
        if is_connected(n,edges):
            # det(L+11^T/n) = n det(L_reduced), independently.
            shifted=[[L[i][j]+Fraction(1,n)
                      for j in range(n)] for i in range(n)]
            assert exact_determinant(shifted)==n*expected
    if n>=2 and is_connected(n,edges):
        weights=[(i%3)+1 for i in range(m)]
        L=laplacian(n,edges,weights)
        # Unit current source at 0, sink n-1, normalized f(n-1)=0.
        b=[Fraction(int(i==0)-int(i==n-1)) for i in range(n)]
        f=solve([row[:-1] for row in L[:-1]],b[:-1])+[Fraction(0)]
        current=[w*(f[u]-f[v]) for (u,v),w in zip(edges,weights)]
        assert all(
            sum(L[v][u]*f[u] for u in range(n))==b[v]
            for v in range(n)
        )
        resistance=f[0]-f[-1]
        assert resistance>0
        assert resistance==sum((j*j/Fraction(w) for j,w in zip(current,weights)),
                               Fraction(0))
        assert resistance==sum(
            (weights[i]*(f[u]-f[v])**2 for i,(u,v) in enumerate(edges)),
            Fraction(0)
        )
        # Dirichlet conditions f(0)=0, f(n-1)=1.
        boundary={0:Fraction(0),n-1:Fraction(1)}
        interior=list(range(1,n-1))
        x=solve([[L[u][v] for v in interior] for u in interior],
                [-sum(L[u][b]*value for b,value in boundary.items())
                 for u in interior])
        h=[boundary.get(v) for v in range(n)]
        for v,value in zip(interior,x):
            h[v]=value
        assert all(sum(L[u][v]*h[v] for v in range(n))==0 for u in interior)
        assert min(h)>=0 and max(h)<=1
        energy=lambda values:sum(
            (Fraction(w)*(values[u]-values[v])**2
             for (u,v),w in zip(edges,weights)),Fraction(0))
        baseline=energy(h)
        for u in interior:
            for offset in (-1,1):
                g=h[:];g[u]+=offset
                assert energy(g)>baseline
    return True


def graph_cover(n,base_edges,d,shifts):
    """Construct finite d-cover of simple base via voltage assignments mod d."""
    N=n*d
    lifted=[]
    for (u,v),shift in zip(base_edges,shifts):
        for sheet in range(d):
            lifted.append((d*u+sheet,d*v+(sheet+shift)%d))
    assert len(lifted)==d*len(base_edges)
    assert N==d*n
    # At each lifted vertex, one and only one incidence over each
    # base incidence is present (local graph-covering condition).
    for u in range(n):
        base_neigh={v for e in base_edges for v in e if u in e and v!=u}
        for sheet in range(d):
            incident=[(x,y) for x,y in lifted if d*u+sheet in (x,y)]
            assert len(incident)==len(base_neigh)
            images={((x if y==d*u+sheet else y)//d) for x,y in incident}
            assert images==base_neigh
    groups=components(N,lifted)
    beta=len(lifted)-N+len(groups)
    base_beta=len(base_edges)-n+1
    assert beta==d*(base_beta-1)+len(groups)
    if len(groups)==1:
        assert beta==1+d*(base_beta-1)
    return len(groups)==1


def audit_covers():
    total=connected_cases=0
    for n in range(1,5):
        all_e=edge_pairs(n)
        for mask in range(1<<len(all_e)):
            edges=[e for i,e in enumerate(all_e) if mask>>i &1]
            if not is_connected(n,edges):
                continue
            for d in (2,3):
                for shifts in product(range(d),repeat=len(edges)):
                    total+=1
                    if graph_cover(n,edges,d,shifts):
                        connected_cases+=1
    return total,connected_cases


def planar_rotation(n,edges):
    """Exhaustive oriented sphere-embedding search via cyclic edge orders.

    A rotation system determines faces as orbits of the
    (u->v) => (v->next_after_u_at_v) dart permutation.
    Connected orientable genus 0 iff n - m + face_count == 2.
    """
    assert is_connected(n,edges)
    if not edges:
        return [()],{}
    nbr=[[] for _ in range(n)]
    for u,v in edges:
        nbr[u].append(v);nbr[v].append(u)
    options=[]
    for neighbors in nbr:
        a=tuple(sorted(neighbors))
        options.append(tuple((a[0],)+p for p in permutations(a[1:])))
    for rotations in product(*options):
        next_dart={}
        for v in range(n):
            neigh=rotations[v]
            for i,u in enumerate(neigh):
                next_dart[(u,v)]=(v,neigh[(i+1)%len(neigh)])
        darts=set(next_dart)
        faces=[];face_of={}
        while darts:
            first=min(darts);cur=first;orbit=[]
            while cur in darts:
                darts.remove(cur)
                face_of[cur]=len(faces)
                orbit.append(cur)
                cur=next_dart[cur]
            assert cur==first
            faces.append(tuple(orbit))
        if n-len(edges)+len(faces)==2:
            return faces,face_of
    return None,None


def dual_faces_two_color(edges,nfaces,face_of):
    dual=[set() for _ in range(nfaces)]
    for u,v in edges:
        a=face_of[(u,v)];b=face_of[(v,u)]
        if a==b:
            return False
        dual[a].add(b);dual[b].add(a)
    colors={}
    for root in range(nfaces):
        if root in colors:
            continue
        colors[root]=0;todo=[root]
        for f in todo:
            for g in dual[f]:
                if g not in colors:
                    colors[g]=1-colors[f];todo.append(g)
                elif colors[g]==colors[f]:
                    return False
    return True


def audit_planarity():
    count=connected_count=planar_count=0
    for n in range(1,6):
        all_e=edge_pairs(n)
        for mask in range(1<<len(all_e)):
            edges=[e for i,e in enumerate(all_e) if mask>>i&1]
            count+=1
            if not is_connected(n,edges):
                continue
            connected_count+=1
            faces,face_of=planar_rotation(n,edges)
            if faces is None:
                assert n>=5
                continue
            planar_count+=1
            m=len(edges)
            assert n-m+len(faces)==2
            if n>=3:
                assert m<=3*n-6,(n,edges,"planar bound")
            adj=[set() for _ in range(n)]
            for u,v in edges:adj[u].add(v);adj[v].add(u)
            # Exhaustive vertex bipartitions, rather than relying on a BFS oracle.
            is_bip=any(all(colors[u]!=colors[v] for u,v in edges)
                       for colors in product((0,1),repeat=n))
            if is_bip and n>=3:
                assert m<=2*n-4,(n,edges,"bipartite planar bound")
            eulerian=all(len(row)%2==0 for row in adj)
            face_two_color=dual_faces_two_color(edges,len(faces),face_of)
            assert face_two_color==eulerian,(
                n,edges,eulerian,face_two_color,"face coloring"
            )
    assert planar_rotation(5,edge_pairs(5))[0] is None
    assert planar_rotation(5,edge_pairs(5)[:-1])[0] is not None
    k33=[(i,j) for i in range(3) for j in range(3,6)]
    assert planar_rotation(6,k33)[0] is None
    # Two triangles meeting at a vertex: Eulerian, two-colorable faces.
    butterfly=[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)]
    faces,face_of=planar_rotation(5,butterfly)
    assert faces is not None and dual_faces_two_color(butterfly,len(faces),face_of)
    return count,connected_count,planar_count


def source_integration():
    c=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book=next(x for x in c["books"] if x["id"]=="graph_and_knot_theory")
    assert len(book["chapters"])==44
    source={
        i:(ROOT/next(p for p in book["chapters"] if Path(p).name.startswith(i+"-")))
        .read_text(encoding="utf-8")
        for i in ("05","07","08","09","12","19")
    }
    assert r"\tau_V(G)" in source["05"] and r"\tau(G)" not in source["05"]
    assert r"\tau(G)" in source["08"] and r"\tau(G)" in source["12"]
    assert r"rem:tg-laplacian-conventions" in source["08"]
    for i in ("07","08","09"):
        assert source[i].count(r"\begin{proof}")==source[i].count(r"\end{proof}")
        assert source[i].count(r"\begin{tikzpicture}")==source[i].count(r"\end{tikzpicture}")
    assert r"thm:tg-free-pi1" in source["07"]
    assert r"thm:tg-kirchhoff" in source["08"]
    assert r"thm:tg-euler-plane" in source["09"]
    assert "Dwukolorowanie ścian bez dwudzielności grafu" in source["09"]


if __name__=="__main__":
    source_integration()
    graph_count=0
    for n in range(1,6):
        e=edge_pairs(n)
        for mask in range(1<<len(e)):
            edges=[edge for i,edge in enumerate(e) if mask>>i&1]
            audit_kirchhoff(n,edges)
            graph_count+=1
    print("PASS 07: covers, Euler characteristic, Nielsen-Schreier:",audit_covers())
    print("PASS 08: exact Kirchhoff/Dirichlet/Thomson models:",graph_count)
    print("PASS 09: exhaustive rotations, planar faces and coloring:",audit_planarity())
    print("PASS source conventions, notation and 44-chapter catalog")
