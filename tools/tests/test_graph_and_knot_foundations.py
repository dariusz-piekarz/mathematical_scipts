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
    if any(x<0 for x in a):
        return False
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


def erdos_gallai(seq):
    d=sorted(seq,reverse=True)
    n=len(d)
    if any(x<0 or x>=n for x in d) or sum(d)%2:
        return False
    return all(sum(d[:k])<=k*(k-1)+sum(min(k,x) for x in d[k:])
               for k in range(1,n+1))


def test_chapter01_regressions():
    graphs=sequences=0
    for n in range(7):
        es=pairs(n)
        realized=set()
        for mask in range(1<<len(es)):
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            a=adj_of(n,edges)
            realized.add(tuple(sorted(map(len,a),reverse=True)))
            if n<=5:
                # Count closed walks independently of unordered triangles.
                trace=sum(u in a[w] for u in range(n)
                          for v in a[u] for w in a[v])
                triangles=sum(v in a[u] and w in a[v] and u in a[w]
                              for u,v,w in combinations(range(n),3))
                assert trace==6*triangles, (n,edges,trace,triangles)
            graphs+=1
        for seq in product(range(n),repeat=n):
            expected=tuple(sorted(seq,reverse=True)) in realized
            assert erdos_gallai(seq)==expected, (n,seq,"EG")
            assert havel_hakimi(seq)==expected, (n,seq,"HH")
            sequences+=1
    assert not erdos_gallai((3,3,1,1))
    assert not erdos_gallai((0,-1))
    assert erdos_gallai(())
    assert component_count(0,[])==0
    return graphs,sequences


def test_chapter02_regressions():
    graphs=forests=spanning=coordinates=dual=0
    for n in range(6):
        es=pairs(n)
        for mask in range(1<<len(es)):
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            m=len(edges)
            c=component_count(n,edges)
            # Independent parity model of the entire cycle space.
            even=set()
            for x in range(1<<m):
                parity=0
                for i,(u,v) in enumerate(edges):
                    if x>>i&1:
                        parity^=(1<<u)|(1<<v)
                if parity==0:
                    even.add(x)
            assert len(even)==1<<(m-n+c)
            found=0
            for t in range(1<<m):
                te=[e for i,e in enumerate(edges) if t>>i&1]
                ct=component_count(n,te)
                if len(te)!=n-ct:
                    continue
                forests+=1
                maximal=all(component_count(n,te+[e])==ct
                            for i,e in enumerate(edges) if not t>>i&1)
                assert maximal==(ct==c)==(len(te)==n-c)
                if ct!=c:
                    continue
                spanning+=1
                found+=1
                outside=((1<<m)-1)^t
                assert len({x&outside for x in even})==len(even)
                assert len(even)==1<<outside.bit_count()
                coordinates+=len(even)
                basis=[]
                adj=[[] for _ in range(n)]
                for i,(u,v) in enumerate(edges):
                    if t>>i&1:
                        adj[u].append((v,i))
                        adj[v].append((u,i))
                for j,(u,v) in enumerate(edges):
                    if t>>j&1:
                        continue
                    # Unique forest path, independent of cut enumeration.
                    stack=[(u,-1,0)]
                    p=None
                    while stack:
                        w,prev,bits=stack.pop()
                        if w==v:
                            p=bits
                            break
                        for y,i in adj[w]:
                            if y!=prev:
                                stack.append((y,w,bits|(1<<i)))
                    assert p is not None
                    cycle=p|(1<<j)
                    assert cycle in even
                    basis.append(cycle)
                    for i,(a,b) in enumerate(edges):
                        if not t>>i&1:
                            continue
                        # Reachability after deletion of the tree edge.
                        seen={u}
                        q=[u]
                        for w in q:
                            for y,k in adj[w]:
                                if k!=i and y not in seen:
                                    seen.add(y)
                                    q.append(y)
                        assert (v not in seen)==bool(p>>i&1)
                        dual+=1
                generated={0}
                for b in basis:
                    generated |= {x^b for x in generated}
                assert generated==even
            assert found>0
            graphs+=1
    return graphs,forests,spanning,coordinates,dual


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
    graphs,seqs=test_chapter01_regressions()
    print(f"PASS chapter 01: {graphs} graphs, {seqs} degree sequences; EG, HH, triangle trace, empty graph")
    g,f,t,x,d=test_chapter02_regressions()
    print(f"PASS chapter 02: {g} graphs, {f} forests, {t} spanning forests, {x} coordinates, {d} fundamental duality cases")
