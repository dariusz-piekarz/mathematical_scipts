#!/usr/bin/env python3
"""Independent exhaustive audit for historical graph-and-knot chapters 04--06.

Not a formal proof: finite counterexample search for Menger (edge/vertex),
Whitney inequalities, max-flow=min-cut via paths, Berge/Hall/Konig/deficit,
Dirac/Ore, and incidence/cut/cycle algebra over Q and GF(2).
No third-party dependencies. Uses independent combinatorial oracles.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from collections import deque
import json
import re

ROOT = Path(__file__).resolve().parents[2]


def pairs(n):
    return list(combinations(range(n),2))


def adjacent(n,edges):
    A=[set() for _ in range(n)]
    for u,v in edges:
        A[u].add(v);A[v].add(u)
    return A


def connected(n,edges,s,t,removed_v=frozenset(),removed_e=frozenset()):
    if s in removed_v or t in removed_v: return False
    A=[set() for _ in range(n)]
    for idx,(u,v) in enumerate(edges):
        if idx not in removed_e and u not in removed_v and v not in removed_v:
            A[u].add(v); A[v].add(u)
    seen={s};todo=[s]
    for u in todo:
        for v in A[u]:
            if v not in seen:
                seen.add(v);todo.append(v)
    return t in seen


def components(n,edges,removed_v=frozenset(),removed_e=frozenset()):
    avail=set(range(n))-set(removed_v)
    count=0
    for s in list(avail):
        if s not in avail: continue
        count+=1;queue=[s];avail.remove(s)
        for u in queue:
            for i,(a,b) in enumerate(edges):
                if i in removed_e: continue
                v=(b if a==u else a if b==u else None)
                if v in avail:
                    avail.remove(v);queue.append(v)
    return count


def simple_paths(n,edges,s,t):
    A=adjacent(n,edges)
    paths=[]
    def go(v,path):
        if v==t:
            paths.append(tuple(path))
            return
        for w in A[v]:
            if w not in path:
                go(w,path+[w])
    go(s,[s])
    return paths


def maximum_disjoint(paths,edge):
    objects=[]
    for path in paths:
        if edge:
            used=frozenset(tuple(sorted((a,b))) for a,b in zip(path,path[1:]))
        else:
            used=frozenset(path[1:-1])
        objects.append(used)
    def search(i,occupied):
        if i==len(objects): return 0
        best=search(i+1,occupied)
        if not occupied.intersection(objects[i]):
            best=max(best,1+search(i+1,occupied|objects[i]))
        return best
    return search(0,frozenset())


def local_edge_cut(n,edges,s,t):
    m=len(edges)
    for k in range(m+1):
        for choice in combinations(range(m),k):
            if not connected(n,edges,s,t,removed_e=frozenset(choice)):
                return k
    raise AssertionError("Unseparable pair")


def local_vertex_cut(n,edges,s,t):
    avail=tuple(v for v in range(n) if v not in (s,t))
    for k in range(len(avail)+1):
        for choice in combinations(avail,k):
            if not connected(n,edges,s,t,removed_v=frozenset(choice)):
                return k
    raise AssertionError("Nonadjacent pair not separated")


def vertex_connectivity(n,edges):
    if n<2:return 0
    if components(n,edges)>1:return 0
    for k in range(n):
        for removed in combinations(range(n),k):
            if n-k<=1 or components(n,edges,removed_v=frozenset(removed))>1:
                return k
    raise AssertionError


def edge_connectivity(n,edges):
    if n<2:return 0
    if components(n,edges)>1:return 0
    for k in range(len(edges)+1):
        for removed in combinations(range(len(edges)),k):
            if components(n,edges,removed_e=frozenset(removed))>1:
                return k
    raise AssertionError


def audit_menger_whitney(n,edges):
    A=adjacent(n,edges)
    for s,t in combinations(range(n),2):
        P=simple_paths(n,edges,s,t)
        ec=local_edge_cut(n,edges,s,t)
        assert ec==maximum_disjoint(P,edge=True),(n,edges,s,t,"edge Menger")
        if t not in A[s]:
            vc=local_vertex_cut(n,edges,s,t)
            assert vc==maximum_disjoint(P,edge=False),(n,edges,s,t,"vertex Menger")
    kappa=vertex_connectivity(n,edges)
    lamb=edge_connectivity(n,edges)
    delta=min(map(len,A)) if n else 0
    assert kappa<=lamb<=delta,(n,edges,kappa,lamb,delta)


def max_matching(edges,na,nb):
    E=set(edges)
    best=0
    for k in range(min(na,nb)+1):
        for left in combinations(range(na),k):
            for right in permutations(range(nb),k):
                if all((u,v) in E for u,v in zip(left,right)):
                    best=max(best,k)
    return best


def vertex_cover_min(edges,na,nb):
    N=na+nb
    for k in range(N+1):
        for cover in combinations(range(N),k):
            C=set(cover)
            if all(u in C or na+v in C for u,v in edges):
                return k
    raise AssertionError


def matching_has_augmenting_path(edges,na,nb,matching):
    M=set(matching);G=set(edges)
    partnerA={a:b for a,b in matching};partnerB={b:a for a,b in matching}
    def walk_left(a,seen):
        for x,y in G:
            if x!=a or (x,y) in M or y in seen:
                continue
            if y not in partnerB:
                return True
            if walk_left(partnerB[y],seen|{y}):
                return True
        return False
    return any(walk_left(a,set()) for a in range(na) if a not in partnerA)


def audit_bipartite(na,nb,edges):
    nu=max_matching(edges,na,nb)
    tau=vertex_cover_min(edges,na,nb)
    assert nu==tau,("Konig",na,nb,edges,nu,tau)
    deficit=max(
        k-len({v for u,v in edges if u in S})
        for k in range(na+1) for S in combinations(range(na),k)
    )
    assert nu==na-deficit,("Hall deficit",na,nb,edges)
    hall=all(
        len({v for u,v in edges if u in S})>=len(S)
        for k in range(na+1) for S in combinations(range(na),k)
    )
    assert hall==(nu==na),("Hall",na,nb,edges)
    # Berge: exhaust all matchings and independently search alternating paths.
    E=set(edges)
    for bits in range(1<<len(edges)):
        M={e for i,e in enumerate(edges) if bits>>i&1}
        if len({e[0] for e in M})!=len(M) or len({e[1] for e in M})!=len(M):
            continue
        has=matching_has_augmenting_path(E,na,nb,M)
        assert has==(len(M)<nu),("Berge",na,nb,edges,M,nu)


def has_hamilton(n,edges):
    if n<3:return False
    E=set(edges)
    return any(
        all(tuple(sorted((route[i],route[(i+1)%n]))) in E for i in range(n))
        for tail in permutations(range(1,n))
        for route in [(0,)+tail]
    )


def audit_hamilton(n,edges):
    if n<3:return
    adj=adjacent(n,edges);deg=list(map(len,adj))
    maxgap=[(a,b) for a,b in pairs(n) if b not in adj[a]]
    dirac=min(deg)*2>=n
    ore=all(deg[u]+deg[v]>=n for u,v in maxgap)
    if dirac or ore:
        assert has_hamilton(n,edges),(n,edges,dirac,ore)


def rank_Q(M):
    if not M:return 0
    A=[[Fraction(z) for z in row] for row in M]
    n=len(A);m=len(A[0]);r=0
    for j in range(m):
        piv=next((i for i in range(r,n) if A[i][j]!=0),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        scale=A[r][j];A[r]=[x/scale for x in A[r]]
        for i in range(n):
            if i!=r and A[i][j]:
                f=A[i][j]
                A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r


def rank_GF2(rows,cols):
    A=list(rows);r=0
    for j in range(cols):
        piv=next((i for i in range(r,len(A)) if A[i]>>j&1),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(len(A)):
            if i!=r and A[i]>>j&1:A[i]^=A[r]
        r+=1
    return r


def audit_incidence(n,edges):
    c=components(n,edges)
    # Deterministic index orientation u -> v with u < v.
    B=[[(-1 if u==vtx else 1 if v==vtx else 0)
         for u,v in edges] for vtx in range(n)]
    m=len(edges)
    assert rank_Q(B)==n-c,("integer incidence rank",n,edges)
    B2=[sum(1<<i for i,z in enumerate(row) if z!=0) for row in B]
    assert rank_GF2(B2,m)==n-c,("GF2 rank",n,edges)
    cycles=[mask for mask in range(1<<m) if all((row&mask).bit_count()%2==0 for row in B2)]
    cuts={sum((1<<i) for i,(u,v) in enumerate(edges)
              if bool(S>>u&1)!=bool(S>>v&1))
          for S in range(1<<n)}
    assert len(cycles)==2**(m-n+c)
    assert len(cuts)==2**(n-c)
    assert all(((x&y).bit_count()%2)==0 for x in cycles for y in cuts)
    # Over GF2, orthogonal complements need not form a direct sum.
    # Use brute-force comparison of the annihilators for exactness.
    full=set(range(1<<m))
    cycle_orth={mask for mask in full
                if all((mask&x).bit_count()%2==0 for x in cycles)}
    cut_orth={mask for mask in full
              if all((mask&y).bit_count()%2==0 for y in cuts)}
    assert cycle_orth==cuts
    assert cut_orth==set(cycles)
    # Construct a spanning forest and one integral fundamental cycle
    # for every non-forest edge. Each signed cycle must have zero boundary.
    parent=list(range(n))
    def find(u):
        while parent[u]!=u:
            u=parent[u]
        return u
    forest=set()
    for i,(u,v) in enumerate(edges):
        ru,rv=find(u),find(v)
        if ru!=rv:
            parent[ru]=rv
            forest.add(i)
    tree=[(edges[i][0],edges[i][1],i) for i in sorted(forest)]
    all_z=[]
    for i,(u,v) in enumerate(edges):
        if i in forest:
            continue
        todo=deque([(v,[])])
        seen={v}
        route=None
        while todo:
            w,path=todo.popleft()
            if w==u:
                route=path
                break
            for x,y,j in tree:
                neighbour=y if x==w else x if y==w else None
                if neighbour is not None and neighbour not in seen:
                    seen.add(neighbour)
                    todo.append((neighbour,path+[(w,neighbour,j)]))
        assert route is not None
        z=[0]*m
        z[i]=1  # non-tree edge directed u -> v
        for x,y,j in route: # tree route returns v -> u
            z[j]=1 if edges[j]==(x,y) else -1
        assert all(sum(B[w][j]*z[j] for j in range(m))==0 for w in range(n))
        all_z.append(z)
    assert len(all_z)==m-n+c
    for f in ([i%3-1 for i in range(n)],list(range(n))):
        grad=[f[v]-f[u] for u,v in edges]
        energy=sum((f[u]-f[v])**2 for u,v in edges)
        assert energy==sum(x*x for x in grad)
        for z in all_z:
            assert sum(x*y for x,y in zip(grad,z))==0


def test_small_graphs():
    count=0
    for n in range(2,6):
        p=pairs(n)
        for mask in range(1<<len(p)):
            edges=[e for i,e in enumerate(p) if mask>>i&1]
            audit_menger_whitney(n,edges)
            audit_hamilton(n,edges)
            audit_incidence(n,edges)
            count+=1
    return count


def test_bipartite():
    count=0
    for na in range(1,4):
        for nb in range(1,4):
            p=[(a,b) for a in range(na) for b in range(nb)]
            for mask in range(1<<len(p)):
                edges=[e for i,e in enumerate(p) if mask>>i&1]
                audit_bipartite(na,nb,edges)
                count+=1
    return count


def test_integrity():
    cat=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    bk=next(x for x in cat["books"] if x["id"]=="graph_and_knot_theory")
    assert len(bk["chapters"])==44
    targets=("04-spojnosc-przekroje-i-twierdzenie-mengera.tex",
             "05-skojarzenia-systemy-reprezentantow-i-cykle-hamiltona.tex",
             "06-macierze-incydencji-cykle-i-przekroje.tex")
    names={Path(x).name:x for x in bk["chapters"]}
    assert all(x in names for x in targets)
    for name in targets:
        s=(ROOT/names[name]).read_text(encoding="utf-8")
        assert "\\chapter{" in s
        assert s.count(r"\begin{proof}")>=3


if __name__=="__main__":
    test_integrity()
    n=test_small_graphs()
    k=test_bipartite()
    print(f"PASS historical 04-06: {n} graph cases (edge/vertex Menger, Whitney, Dirac, Ore, incidence algebra)")
    print(f"PASS historical 05: {k} bipartite graphs (Hall, deficiency, Konig, Berge)")
