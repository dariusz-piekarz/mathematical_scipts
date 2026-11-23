#!/usr/bin/env python3
"""Independent algebraic Morse cancellation audit (historical chapter 15).

Check the Schur-complement construction, not only V-path acyclicity.
Use actual boundary maps over GF(2), verify d^2=0 after each elimination,
and compare Betti numbers to an independent rank oracle.
Tests: all partial matchings of a triangle and its boundary; a cyclic
matching; tree/cotree matchings on the tetrahedral sphere and 3x3 torus.
This finite check does not prove the general Forman theorem.
"""
from collections import Counter, defaultdict
from itertools import combinations

from test_graph_and_knot_triangulation_reeb_forman import (
    acyclic_via_hasse, all_matchings, betti_gf2, faces_of_torus,
    hasse_edges, pieces, rank_gf2, simplices,
)

def initial_boundary(K):
    return {x: (set(combinations(x, len(x)-1)) if len(x)>1 else set())
            for x in K}

def assert_chain_complex(D):
    for x, bd in D.items():
        assert all(y in D and len(y)==len(x)-1 for y in bd), ("degree", x, bd)
        twice = set()
        for y in bd:
            twice.symmetric_difference_update(D[y])
        assert not twice, ("d^2", x, twice)

def betti_of_reduced(D, top=2):
    ranks = {}
    dimensions = {p: sum(len(x)==p+1 for x in D) for p in range(top+1)}
    for p in range(1,top+1):
        lower = sorted(x for x in D if len(x)==p)
        coords = {x:i for i,x in enumerate(lower)}
        cols = [sum(1<<coords[y] for y in D[x])
                for x in D if len(x)==p+1]
        ranks[p] = rank_gf2(cols)
    return tuple(dimensions[p]-ranks.get(p,0)-ranks.get(p+1,0)
                 for p in range(top+1))

def eliminate_matching(K, matching):
    D = initial_boundary(K)
    assert_chain_complex(D)
    for a,b in matching:
        assert a in D and b in D, ("pair deleted already", a,b)
        assert len(b)==len(a)+1, (a,b)
        pivot = a in D[b]
        assert pivot, ("matched coefficient became zero", a,b, matching)
        column = set(D[b])
        for x in list(D):
            if x!=b and len(x)==len(b) and a in D[x]:
                D[x].symmetric_difference_update(column)
        for x in list(D):
            if x!=b and len(x)==len(b)+1:
                D[x].discard(b)
        del D[a]
        del D[b]
        assert_chain_complex(D)
    return D

def check_morse(K, matching):
    assert acyclic_via_hasse(K, matching)
    D=eliminate_matching(K, matching)
    used={x for pair in matching for x in pair}
    assert set(D)==set(K)-used
    critical=Counter(len(x)-1 for x in D)
    c=tuple(critical[i] for i in range(3))
    b=betti_gf2(K)
    assert b==betti_of_reduced(D), ("homology", c, b, betti_of_reduced(D))
    assert all(c[i]>=b[i] for i in range(3)), ("weak", c,b)
    for p in range(3):
        assert sum((-1)**(p-i)*c[i] for i in range(p+1)) >= (
            sum((-1)**(p-i)*b[i] for i in range(p+1))
        ), ("strong", p,c,b)
    assert sum((-1)**i*c[i] for i in range(3)) == sum(
        (-1)**i*b[i] for i in range(3))
    return c

def tree_cotree_matching(K):
    """Rooted primal tree + rooted dual tree on remaining edges."""
    verts = sorted(x[0] for x in pieces(K,0))
    edges = pieces(K,1)
    tris = pieces(K,2)
    adjacency = defaultdict(list)
    for edge in edges:
        u,v=edge
        adjacency[u].append((v,edge))
        adjacency[v].append((u,edge))
    root=verts[0]
    parent={root:None}
    todo=[root]
    vpairs=[]
    tree_edges=set()
    for u in todo:
        for v,e in adjacency[u]:
            if v not in parent:
                parent[v]=u
                tree_edges.add(e)
                vpairs.append(((v,),e))
                todo.append(v)
    assert len(parent)==len(verts)

    face_ids={t:i for i,t in enumerate(tris)}
    edge_faces=defaultdict(list)
    for t in tris:
        for e in combinations(t,2):
            edge_faces[e].append(face_ids[t])
    assert all(len(ids)==2 for ids in edge_faces.values())
    dual_adj=defaultdict(list)
    for e,ids in edge_faces.items():
        if e not in tree_edges:
            u,v=ids
            dual_adj[u].append((v,e))
            dual_adj[v].append((u,e))
    parent_faces={0:None}
    todo=[0]
    fpairs=[]
    for f in todo:
        for g,e in dual_adj[f]:
            if g not in parent_faces:
                parent_faces[g]=f
                fpairs.append((e,tris[g]))
                todo.append(g)
    assert len(parent_faces)==len(tris), "dual complement must be connected"
    return tuple(vpairs+fpairs)

def test_exhaustive_small_matchings():
    cycle=simplices({(0,1),(1,2),(0,2)})
    disk=simplices({(0,1,2)})
    total=acyclic=nonacyclic=0
    for K in (cycle,disk):
        for M in all_matchings(hasse_edges(K)):
            total+=1
            if acyclic_via_hasse(K,M):
                acyclic+=1
                check_morse(K,M)
            else:
                nonacyclic+=1
    assert total==60, total
    assert nonacyclic>0
    # Reversing the three matched edges on the cycle creates a closed V-path.
    bad=(((0,),(0,1)),((1,),(1,2)),((2,),(0,2)))
    assert not acyclic_via_hasse(cycle,bad)
    return total, acyclic, nonacyclic

def test_tree_cotree():
    tetra=simplices({(0,1,2),(0,1,3),(0,2,3),(1,2,3)})
    torus=simplices(faces_of_torus())
    result=[]
    for name,K,c in (("sphere",tetra,(1,0,1)),("torus",torus,(1,2,1))):
        M=tree_cotree_matching(K)
        actual=check_morse(K,M)
        assert actual==c,(name,actual,c)
        result.append((name,len(M),actual))
    return result

def test_source():
    from pathlib import Path
    source=(Path(__file__).resolve().parents[2]/
            "chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex")
    text=source.read_text(encoding="utf-8")
    assert r"\label{thm:tg-forman-algebraic-cancellation}" in text
    assert r"\label{thm:tg-forman-tree-cotree}" in text
    assert r"\xrightarrow{\lambda}" in text
    assert r"\ref{thm:tg-forman-algebraic-cancellation}" in text

if __name__=="__main__":
    test_source()
    print("PASS small matchings total/acyclic/cyclic:",test_exhaustive_small_matchings())
    print("PASS independently reduced surface Morse complexes:",test_tree_cotree())
