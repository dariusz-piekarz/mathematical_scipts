"""Exact signed integral reductions and coefficient-sensitive homology."""
from itertools import combinations
from pathlib import Path
from test_graph_and_knot_morse_chain_reduction import tree_cotree_matching
from test_graph_and_knot_triangulation_reeb_forman import (
    simplices, hasse_edges, all_matchings, acyclic_via_hasse, faces_of_torus,
    surface_link_condition,
)

def initial(K):
    return {x: {x[:i]+x[i+1:]: (-1)**i for i in range(len(x))}
            if len(x)>1 else {} for x in K}

def chain(D):
    for x, bd in D.items():
        twice = {}
        for y, a in bd.items():
            assert y in D and len(y)==len(x)-1
            for z, b in D[y].items():
                twice[z] = twice.get(z,0)+a*b
        assert not any(twice.values())

def reduce(K, M):
    D = initial(K)
    chain(D)
    for a,b in M:
        pivot = D[b][a]
        assert abs(pivot)==1
        for x in list(D):
            if x!=b and len(x)==len(b):
                mu = D[x].get(a,0)
                for y,v in D[b].items():
                    D[x][y] = D[x].get(y,0)-mu*pivot*v
                D[x] = {y:v for y,v in D[x].items() if v}
            elif len(x)==len(b)+1:
                D[x].pop(b,None)
        del D[a]
        del D[b]
        chain(D)
    return D

def rank_mod(matrix, p):
    a = [list(row) for row in matrix]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r,len(a)) if a[k][j]%p),None)
        if k is None:
            continue
        a[r],a[k] = a[k],a[r]
        inv = pow(a[r][j]%p,-1,p)
        a[r] = [(v*inv)%p for v in a[r]]
        for k in range(r+1,len(a)):
            q = a[k][j]
            a[k] = [(u-q*v)%p for u,v in zip(a[k],a[r])]
        r += 1
    return r

def betti(D,p):
    bases = [[x for x in D if len(x)==d+1] for d in range(3)]
    ranks = [0]+[rank_mod([[D[x].get(y,0) for x in bases[d]]
                           for y in bases[d-1]],p) for d in (1,2)]+[0]
    return tuple(len(bases[d])-ranks[d]-ranks[d+1] for d in range(3))

def check(K,M):
    assert acyclic_via_hasse(K,M)
    D = reduce(K,M)
    for p in (2,3,5):
        assert betti(D,p)==betti(initial(K),p)
    return D

def main():
    count=0
    for facets in ({(0,1),(1,2),(0,2)}, {(0,1,2)}):
        K=simplices(facets)
        for M in all_matchings(hasse_edges(K)):
            if acyclic_via_hasse(K,M):
                check(K,M)
                count+=1
    # Minimal 6-vertex triangulation of the real projective plane.
    rp=simplices({(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,6),
                  (2,3,6),(2,4,5),(2,5,6),(3,4,5),(3,4,6)})
    assert surface_link_condition(rp)
    for name,K,expected in (
        ("sphere",simplices(set(combinations(range(4),3))),0),
        ("torus",simplices(faces_of_torus()),0),
        ("RP2",rp,2),
    ):
        D=check(K,tree_cotree_matching(K))
        top=[x for x in D if len(x)==3]
        assert len(top)==1
        vals=[abs(v) for v in D[top[0]].values()]
        assert (max(vals,default=0)==expected), (name,D)
        if name=="RP2":
            assert sorted(map(len,D))==[1,2,3]
            assert vals==[2]
            assert betti(D,2)==(1,1,1)
            assert betti(D,3)==(1,0,0)
    print(f"PASS: {count} signed small matchings; integral sphere, torus, RP2 pivot 2; GF(2), GF(3), GF(5)")

if __name__=="__main__":
    main()
