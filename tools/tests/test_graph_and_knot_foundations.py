#!/usr/bin/env python3
"""Independent finite audit for original chapters 01--03 of graph and knot theory.

Checks graph conventions (including the empty graph), handshake, complements,
odd-cycle/bipartite characterization, Havel--Hakimi, incidence rank and cycle
dimension, bridges, Euler walks and Robbins' orientation theorem.
No third-party packages or probabilistic sampling.
"""
from __future__ import annotations
from collections import deque
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]


def pairs(n):
    return list(combinations(range(n), 2))


def adj_of(n, edges):
    a = [set() for _ in range(n)]
    for u,v in edges:
        a[u].add(v)
        a[v].add(u)
    return a


def component_count(n, edges):
    a = adj_of(n,edges)
    seen=set()
    count=0
    for s in range(n):
        if s in seen:
            continue
        count += 1
        seen.add(s)
        q=[s]
        for u in q:
            for v in a[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return count


def binary_rank(rows, width):
    vecs = list(rows)
    rank=0
    for bit in range(width):
        pivot=next((i for i in range(rank,len(vecs)) if vecs[i]>>bit&1),None)
        if pivot is None:
            continue
        vecs[rank],vecs[pivot]=vecs[pivot],vecs[rank]
        for i in range(len(vecs)):
            if i!=rank and vecs[i]>>bit&1:
                vecs[i]^=vecs[rank]
        rank+=1
    return rank


def is_bipartite_by_bruteforce(n,edges):
    for colors in product((0,1),repeat=n):
        if all(colors[u]!=colors[v] for u,v in edges):
            return True
    return False


def has_odd_simple_cycle(n,edges):
    edge_set=set(edges)
    for k in range(3,n+1,2):
        for cyc in permutations(range(n),k):
            if cyc[0]!=min(cyc):
                continue
            if all(tuple(sorted((cyc[i],cyc[(i+1)%k]))) in edge_set
                   for i in range(k)):
                return True
    return False


def havel_hakimi(seq):
    a=sorted(seq,reverse=True)
    while a:
        if a[0]==0:
            return True
        d,*tail=a
        if d<0 or d>len(tail):
            return False
        tail=[x-(i<d) for i,x in enumerate(tail)]
        if min(tail,default=0)<0:
            return False
        a=sorted(tail,reverse=True)
    return True


def euler_trail_exists_bruteforce(n,edges,closed):
    m=len(edges)
    if not m:
        return False  # Historical theorem assumes at least one edge.
    starts={v for e in edges for v in e}
    full=(1<<m)-1
    a=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        a[u].append((v,i))
        a[v].append((u,i))
    for start in starts:
        @lru_cache(maxsize=None)
        def possible(u,used):
            if used==full:
                return (u==start) if closed else True
            return any(possible(v,used | (1<<i))
                       for v,i in a[u] if not used >> i & 1)
        if possible(start,0):
            return True
    return False


def has_bridge(n,edges):
    c=component_count(n,edges)
    return any(component_count(n,edges[:i]+edges[i+1:])>c
               for i in range(len(edges)))


def path_avoiding_edge(n,edges,skip_index):
    u,v=edges[skip_index]
    adj=adj_of(n,edges[:skip_index]+edges[skip_index+1:])
    q=[u]
    seen={u}
    for x in q:
        if x==v:
            return True
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append(y)
    return False


def strong_orientation_exists(n,edges):
    m=len(edges)
    for mask in range(1<<m):
        directed=[(v,u) if mask>>i & 1 else (u,v)
                  for i,(u,v) in enumerate(edges)]
        a=[set() for _ in range(n)]
        for u,v in directed:
            a[u].add(v)
        def reach(s):
            seen={s}
            q=[s]
            for u in q:
                for v in a[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            return len(seen)==n
        if all(reach(s) for s in range(n)):
            return True
    return False


def audit_graph(n,edges):
    a=adj_of(n,edges)
    m=len(edges)
    assert sum(map(len,a))==2*m, (n,edges,"handshake")
    assert sum(len(a[v])%2 for v in range(n))%2==0
    comp=pairs(n)
    complement=[edge for edge in comp if edge not in set(edges)]
    assert len(complement)+m==n*(n-1)//2
    assert all(len(a[v])+len(adj_of(n,complement)[v])==n-1
               for v in range(n))
    assert is_bipartite_by_bruteforce(n,edges)==(not has_odd_simple_cycle(n,edges))
    c=component_count(n,edges)
    incidence_rows=[
        sum(1<<i for i,(u,v) in enumerate(edges) if w in (u,v))
        for w in range(n)
    ]
    rank=binary_rank(incidence_rows,m)
    assert rank==n-c, (n,edges,rank,n-c)
    assert m-rank==m-n+c>=0
    assert (m-n+c==0)==all(
        not path_avoiding_edge(n,edges,i) for i in range(m)
    ), (n,edges,"cycle rank and forest criterion")
    for i in range(m):
        # Removing a bridge increments component count; it is also
        # characterized by the nonexistence of an alternative endpoint path.
        assert (component_count(n,edges[:i]+edges[i+1:])>c)==(
            not path_avoiding_edge(n,edges,i))
    if m:
        degrees=[len(x) for x in a]
        active=[v for v in range(n) if degrees[v]]
        active_component=set()
        q=[active[0]]
        active_component.add(active[0])
        for u in q:
            for v in a[u]:
                if v not in active_component:
                    active_component.add(v)
                    q.append(v)
        connected_on_active=(len(active_component)==len(active))
        odd=sum(d%2 for d in degrees)
        assert euler_trail_exists_bruteforce(n,edges,closed=True)==(
            connected_on_active and odd==0)
        assert euler_trail_exists_bruteforce(n,edges,closed=False)==(
            connected_on_active and odd in (0,2))
    if 2<=n<=4:
        # Robbins for nonempty simple graphs with n>=2.
        expect=(c==1 and not has_bridge(n,edges))
        assert strong_orientation_exists(n,edges)==expect, (n,edges,expect)


def test_all_small():
    examined=0
    graph_degree_sets={}
    for n in range(1,6):
        graphical=set()
        for mask in range(1<<(n*(n-1)//2)):
            es=[e for i,e in enumerate(pairs(n)) if mask>>i&1]
            audit_graph(n,es)
            degrees=tuple(sorted(map(len,adj_of(n,es)),reverse=True))
            graphical.add(degrees)
            examined+=1
        graph_degree_sets[n]=graphical
    seqs=0
    for n in range(1,6):
        for seq in product(range(n),repeat=n):
            expected=tuple(sorted(seq,reverse=True)) in graph_degree_sets[n]
            assert havel_hakimi(seq)==expected, (n,seq,expected)
            seqs+=1
    return examined,seqs


def test_source_consistency():
    catalog=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book=next(x for x in catalog["books"] if x["id"]=="graph_and_knot_theory")
    assert len(book["chapters"])==44
    intro=(ROOT/"chapters/pl/graph_and_knot_theory/01-podstawy-teorii-grafow.tex").read_text(encoding="utf-8")
    assert "dopuszczamy także $V=\\varnothing$" in intro
    assert "jeśli $V\\ne\\varnothing$ oraz każda para" in intro
    assert "Drzewo" in (ROOT/"chapters/pl/graph_and_knot_theory/02-drzewa-mosty-i-cykle-fundamentalne.tex").read_text(encoding="utf-8")
    assert "Euler" in (ROOT/"chapters/pl/graph_and_knot_theory/03-przechodzenie-po-wszystkich-krawedziach-teoria-eulera.tex").read_text(encoding="utf-8")


if __name__=="__main__":
    test_source_consistency()
    n,sequences=test_all_small()
    print(f"PASS historical graphs 01-03: {n} graphs, {sequences} degree sequences")
    print("PASS handshake, complement, odd cycles, incidence rank, bridges, Euler, Robbins, Havel-Hakimi")
