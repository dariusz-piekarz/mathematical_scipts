#!/usr/bin/env python3
"""Independent finite regressions of the complete Kuratowski proof.

Checks, without invoking Kuratowski or using external graph libraries:
  * agreement of K5/K3,3 minors and forbidden subdivisions on ALL
    labeled simple graphs on <= 6 vertices;
  * Thomassen's contractible-edge lemma and three-cut adjacency;
  * the cyclic-neighbour trichotomy used to split a contracted vertex;
  * four-terminal tree/branch-set lemma on all labeled trees <= 5 vertices.

These tests do not constitute a formal proof for arbitrary finite graphs.
"""
from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]


def pairs(n):
    return tuple(combinations(range(n),2))


def adjacency(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def components(n,edges,removed=frozenset()):
    adj=adjacency(n,edges)
    allowed=set(range(n))-set(removed)
    ans=[]
    while allowed:
        start=min(allowed);allowed.remove(start);comp={start}
        todo=[start]
        for u in todo:
            for v in adj[u] & allowed:
                allowed.remove(v);comp.add(v);todo.append(v)
        ans.append(comp)
    return ans


def three_connected(n,edges):
    if n<4:return False
    if len(components(n,edges))!=1:return False
    for sz in (1,2):
        for S in combinations(range(n),sz):
            if len(components(n,edges,frozenset(S)))>1:
                return False
    return True


def contract(n,edges,e):
    u,v=e
    assert u!=v
    representatives=[u if x==v else x for x in range(n)]
    keep=[x for x in range(n) if x!=v]
    index={x:i for i,x in enumerate(keep)}
    result=set()
    for a,b in edges:
        x=index[representatives[a]];y=index[representatives[b]]
        if x!=y:result.add(tuple(sorted((x,y))))
    return n-1,tuple(sorted(result))


def k5_clique(n,edges):
    E=set(edges)
    return any(all(tuple(sorted((u,v))) in E for u,v in combinations(S,2))
               for S in combinations(range(n),5))


def k33_subgraph(n,edges):
    E=set(edges)
    return any(all(tuple(sorted((u,v))) in E for u in L for v in R)
               for S in combinations(range(n),6)
               for L in combinations(S,3)
               for R in [tuple(v for v in S if v not in L)])


def forbidden_minor(n,edges):
    if n<5:return False
    if k5_clique(n,edges) or (n>=6 and k33_subgraph(n,edges)):
        return True
    if n==6:
        return any(k5_clique(*contract(n,edges,e)) for e in edges)
    return False


def forbidden_subdivision(n,edges):
    if n<5:return False
    if k5_clique(n,edges) or (n>=6 and k33_subgraph(n,edges)):
        return True
    if n==6:
        E=set(edges)
        for w in range(n):
            branch=[v for v in range(n) if v!=w]
            for u,v in combinations(branch,2):
                if (tuple(sorted((u,w))) in E and
                    tuple(sorted((v,w))) in E and
                    all(tuple(sorted((a,b))) in E
                        for a,b in combinations(branch,2)
                        if {a,b}!={u,v})):
                    return True
    return False


def graph_models():
    checked=threes=with_minor=0
    for n in range(1,7):
        es=pairs(n)
        for mask in range(1<<len(es)):
            edges=tuple(e for i,e in enumerate(es) if mask>>i&1)
            checked+=1
            minor=forbidden_minor(n,edges)
            topo=forbidden_subdivision(n,edges)
            assert minor==topo,(n,edges,minor,topo)
            with_minor+=minor
            if three_connected(n,edges):
                threes+=1
                if n==4:
                    assert len(edges)==6 # K4 only
                if n>=5:
                    good=[e for e in edges
                          if three_connected(*contract(n,edges,e))]
                    assert good,(n,edges,"No contractible edge")
                adj=adjacency(n,edges)
                for S in combinations(range(n),3):
                    remaining=components(n,edges,frozenset(S))
                    if len(remaining)<2:
                        continue
                    for v in S:
                        assert all(adj[v] & C for C in remaining),(
                            "three cut not adjacent",n,edges,S,v,remaining)
    return checked,threes,with_minor


def cyclic_arc(n,x,y):
    """Are all y in an arc with no x in its interior?"""
    X=sorted(x);Y=set(y);k=len(X)
    for i,a in enumerate(X):
        b=X[(i+1)%k]
        covered={a};t=(a+1)%n
        while True:
            covered.add(t)
            if t==b:break
            t=(t+1)%n
        if Y<=covered:return True
    return False


def alternating(n,X,Y):
    """Choose 4 distinct cycle points alternating memberships."""
    for a,b,c,d in combinations(range(n),4):
        if (a in Y and b in X and c in Y and d in X) or (
            a in X and b in Y and c in X and d in Y):
            return True
    return False


def cyclic_case_split():
    cases=0
    for n in range(4,9):
        subsets=[frozenset(i for i in range(n) if mask>>i&1)
                 for mask in range(1<<n)]
        for X in subsets:
            if len(X)<2:continue
            for Y in subsets:
                if len(Y)<2:continue
                a=cyclic_arc(n,X,Y)
                b=len(X&Y)>=3
                c=alternating(n,X,Y)
                assert a or b or c,(n,X,Y)
                cases+=1
    return cases


def all_trees(n):
    if n==1:
        yield ()
        return
    if n==2:
        yield ((0,1),)
        return
    for prufer in product(range(n),repeat=n-2):
        deg=[1]*n
        for x in prufer:deg[x]+=1
        edges=[]
        for x in prufer:
            leaf=next(i for i in range(n) if deg[i]==1)
            edges.append(tuple(sorted((leaf,x))))
            deg[leaf]-=1;deg[x]-=1
        u,v=[i for i in range(n) if deg[i]==1]
        edges.append((u,v))
        yield tuple(edges)


def tree_terminal_check():
    total=0
    for n in range(1,6):
        for edges in all_trees(n):
            for k in (3,4):
                for locations in product(range(n),repeat=k):
                    # An edge may split 4 labels into 2+2.
                    split=False
                    if k==4:
                        for e in edges:
                            reduced=tuple(a for a in edges if a!=e)
                            two=components(n,reduced)
                            assert len(two)==2
                            if sum(t in two[0] for t in locations)==2:
                                split=True
                                break
                    # At a centre z each component of T-z holds <= 1 label.
                    centre=any(
                        all(sum(loc in C for loc in locations)<=1
                            for C in components(n,edges,frozenset({z})))
                        for z in range(n)
                    )
                    assert split or centre,(n,edges,locations)
                    total+=1
    return total


def source_integration():
    cat=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book=next(b for b in cat["books"] if b["id"]=="graph_and_knot_theory")
    assert len(book["chapters"])==44
    source=(ROOT/next(p for p in book["chapters"] if
                 p.endswith("10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex")))
    txt=source.read_text(encoding="utf-8")
    assert r"\begin{proof}[Dowód implikacji" in txt
    assert r"\label{lem:tg-kuratowski-minor-to-subdivision}" in txt
    assert r"\label{lem:tg-kuratowski-contractible-edge}" in txt
    assert r"\label{lem:tg-kuratowski-gluing}" in txt
    assert r"\label{lem:tg-kuratowski-face-cycle}" in txt
    assert "Przyjmujemy ją tutaj jako klasyczne" not in txt
    assert txt.count(r"\begin{proof}") == txt.count(r"\end{proof}")
    assert txt.count(r"\begin{lemat}") == txt.count(r"\end{lemat}")


if __name__=="__main__":
    source_integration()
    print("PASS minor/subdivision and three-connected contractions:",graph_models())
    print("PASS all cyclic-neighbour attachment configurations:",cyclic_case_split())
    print("PASS all 3/4 terminal placements in small labeled trees:",tree_terminal_check())
    print("PASS chapter 10 integration, no external Kuratowski assumption")
