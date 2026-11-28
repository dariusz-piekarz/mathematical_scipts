#!/usr/bin/env python3
"""Audit 28: independent small-graph oracle checks for chapters 37-39.

Exhaustive edge-set MST oracles, Floyd-Warshall oracle for Bellman-Ford
negative-infinity propagation, and vertex-deletion oracle for Tarjan
articulation points. Only finite graph computations are verified.
"""
from itertools import combinations
from math import inf
from pathlib import Path
from random import Random

ROOT=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"
RANDOM=Random(20261123028)


def component_count(n,edges,deleted=None):
    adj=[[] for _ in range(n)]
    for u,v,*_ in edges:
        if u==deleted or v==deleted:continue
        adj[u].append(v);adj[v].append(u)
    vis=set()
    count=0
    for s in range(n):
        if s==deleted or s in vis:continue
        count+=1;vis.add(s);stack=[s]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in vis:
                    vis.add(v);stack.append(v)
    return count


def articulation_dfs(n,edges):
    adj=[[] for _ in range(n)]
    for u,v,*_ in edges:
        adj[u].append(v);adj[v].append(u)
    tin=[-1]*n;low=[-1]*n;out=set();clock=0
    def visit(v,parent):
        nonlocal clock
        tin[v]=low[v]=clock;clock+=1;children=0
        for w in adj[v]:
            if w==parent:continue
            if tin[w]!=-1:
                low[v]=min(low[v],tin[w])
            else:
                children+=1;visit(w,v)
                low[v]=min(low[v],low[w])
                if parent!=-1 and low[w]>=tin[v]:
                    out.add(v)
        if parent==-1 and children>=2:out.add(v)
    for v in range(n):
        if tin[v]==-1:visit(v,-1)
    return out


def verify_dfs_articulation():
    cases=0
    for n in range(1,10):
        edge_universe=list(combinations(range(n),2))
        for iteration in range(740):
            edges=[(u,v) for u,v in edge_universe
                   if RANDOM.randrange(10)<(2+iteration%6)]
            count=component_count(n,edges)
            oracle={v for v in range(n)
                    if component_count(n,edges,v)>count}
            assert articulation_dfs(n,edges)==oracle,(n,edges,oracle)
            cases+=1
    # Distinguish bridges and articulation points: two triangles
    example=[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2)]
    assert articulation_dfs(5,example)=={2}
    for e in example:
        assert component_count(5,[x for x in example if x!=e])==1
    return cases+1


def bellman_negative_reach(n,arcs,source):
    d=[inf]*n;d[source]=0
    for _ in range(n-1):
        for u,v,w in arcs:
            if d[u]<inf and d[u]+w<d[v]:
                d[v]=d[u]+w
    marked={v for u,v,w in arcs if d[u]<inf and d[u]+w<d[v]}
    adj=[[] for _ in range(n)]
    for u,v,w in arcs:adj[u].append(v)
    seen=set(marked);stack=list(marked)
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:seen.add(v);stack.append(v)
    return d,seen


def floyd_negative_oracle(n,arcs,source):
    D=[[inf]*n for _ in range(n)]
    for i in range(n):D[i][i]=0
    for u,v,w in arcs:D[u][v]=min(D[u][v],w)
    for k in range(n):
        for i in range(n):
            if D[i][k]==inf:continue
            for j in range(n):
                if D[k][j]!=inf:
                    D[i][j]=min(D[i][j],D[i][k]+D[k][j])
    bad={v for v in range(n)
         if any(D[source][k]<inf and D[k][k]<0 and D[k][v]<inf
                for k in range(n))}
    return D[source],bad


def verify_bellman_ford_infinities():
    cases=0
    for n in range(1,9):
        for iteration in range(580):
            arcs=[(u,v,RANDOM.randint(-6,7))
                  for u in range(n) for v in range(n) if u!=v
                  and RANDOM.randrange(10)<(2+iteration%6)]
            source=RANDOM.randrange(n)
            d,marked=bellman_negative_reach(n,arcs,source)
            oracle,bad=floyd_negative_oracle(n,arcs,source)
            assert marked==bad,(n,arcs,source,marked,bad)
            for v in range(n):
                if v not in bad: assert d[v]==oracle[v],(n,arcs,source,v,d[v],oracle[v])
            cases+=1
    ex=[(0,1,1),(1,2,-3),(2,1,1),(2,3,2),(0,4,5)]
    d,bad=bellman_negative_reach(5,ex,0)
    assert bad=={1,2,3} and d[0]==0 and d[4]==5
    return cases+1


def is_spanning_forest(n,edges,chosen):
    # Ensure selected edges connect precisely the components of G.
    if len(chosen)!=n-component_count(n,edges):return False
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for u,v,*_ in chosen:
        ru,rv=root(u),root(v)
        if ru==rv:return False
        parent[ru]=rv
    return all(root(u)==root(v) for u,v,*_ in edges)


def certificate(n,edges,chosen):
    adj=[[] for _ in range(n)]
    selected={(min(u,v),max(u,v)) for u,v,*_ in chosen}
    for u,v,w in chosen:adj[u].append((v,w));adj[v].append((u,w))
    if not is_spanning_forest(n,edges,chosen):return False,False
    strict=True
    for u,v,w in edges:
        if (min(u,v),max(u,v)) in selected:continue
        # Find max edge weight on unique T-path with an independent DFS.
        stack=[(u,None)]
        seen={u}
        maximum=None
        while stack:
            x,M=stack.pop()
            if x==v:maximum=M;break
            for y,weight in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append((y,max(M,weight) if M is not None else weight))
        assert maximum is not None
        if w<maximum:return False,False
        if w==maximum:strict=False
    return True,strict


def verify_mst_certificate():
    cases=0;checked_trees=0
    for n in range(1,7):
        universe=list(combinations(range(n),2))
        for iteration in range(520):
            edges=[(u,v,RANDOM.randint(-4,6))
                   for u,v in universe
                   if RANDOM.randrange(10)<(3+iteration%5)]
            # Bound the enumeration for a predictable CI duration.
            if len(edges)>9:edges=edges[:9]
            required=n-component_count(n,edges)
            candidates=[]
            for es in combinations(edges,required):
                if is_spanning_forest(n,edges,es):
                    candidates.append((sum(w for _,_,w in es),es))
            assert candidates
            minimum=min(weight for weight,_ in candidates)
            num_min=sum(weight==minimum for weight,_ in candidates)
            for weight,forest in candidates:
                optimal,unique=certificate(n,edges,forest)
                assert optimal==(weight==minimum)
                assert unique==(weight==minimum and num_min==1)
                checked_trees+=1
            cases+=1
    assert checked_trees>10000
    return cases,checked_trees


def source_anchors():
    names=[
        "37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex",
        "38-najkrotsze-drogi-wazone-i-algorytmy-wyszukiwania-tras.tex",
        "39-minimalne-drzewa-rozpinajace-prim-kruskal-dsu.tex",
    ]
    contents=[(ROOT/n).read_text(encoding="utf-8") for n in names]
    for s,needle in zip(contents,(
        r"\label{thm:tg-dfs-articulation}",
        r"\label{thm:tg-weighted-bellman-negative-reach}",
        r"\label{thm:tg-mst-certificate}",
    )):
        assert needle in s


if __name__=="__main__":
    source_anchors()
    print("PASS DFS articulation versus vertex-removal oracle:",verify_dfs_articulation())
    print("PASS Bellman-Ford minus-infinity versus Floyd-Warshall oracle:",verify_bellman_ford_infinities())
    cases,forests=verify_mst_certificate()
    print("PASS MST certificate versus exhaustive spanning forests:",cases,forests)
