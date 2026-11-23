#!/usr/bin/env python3
"""Independent second audit 37--39: edge-ID multigraph DFS, Johnson,
and exact margin/uniqueness of minimum spanning forests.
These finite tests are mathematical regressions, not formal proofs.
"""
from collections import defaultdict
from fractions import Fraction
from heapq import heappop, heappush
from itertools import combinations
from math import inf
from pathlib import Path
from random import Random

RNG=Random(20261123029)
ROOT=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def comps(n,edges,drop_v=-1,drop_e=-1):
    a=[[] for _ in range(n)]
    for eid,(u,v) in enumerate(edges):
        if eid==drop_e or u==drop_v or v==drop_v:continue
        a[u].append(v);a[v].append(u)
    seen={drop_v};c=0
    for v in range(n):
        if v in seen:continue
        c+=1;seen.add(v);stack=[v]
        while stack:
            for w in a[stack.pop()]:
                if w not in seen:seen.add(w);stack.append(w)
    return c


def tarjan(n,edges):
    a=[[] for _ in range(n)]
    for eid,(u,v) in enumerate(edges):
        a[u].append((v,eid));a[v].append((u,eid))
    tin=[-1]*n;low=[-1]*n;bridges=set();art=set();t=0
    def dfs(v,parent_e,parent):
        nonlocal t
        tin[v]=low[v]=t;t+=1;children=0
        for w,eid in a[v]:
            if eid==parent_e:continue
            if tin[w]>=0:low[v]=min(low[v],tin[w]);continue
            children+=1;dfs(w,eid,v);low[v]=min(low[v],low[w])
            if low[w]>tin[v]:bridges.add(eid)
            if parent!=-1 and low[w]>=tin[v]:art.add(v)
        if parent==-1 and children>=2:art.add(v)
    for v in range(n):
        if tin[v]<0:dfs(v,-1,-1)
    return bridges,art


def check_multigraphs():
    graphs=edges_checked=vertices_checked=0
    for n in range(1,10):
        all_edges=list(combinations(range(n),2))
        for i in range(420):
            edges=[all_edges[RNG.randrange(len(all_edges))]
                   for _ in range(RNG.randrange(0,min(18,3*len(all_edges))+1))] if all_edges else []
            base=comps(n,edges)
            want_bridges={e for e in range(len(edges)) if comps(n,edges,drop_e=e)>base}
            want_art={v for v in range(n) if comps(n,edges,drop_v=v)>base}
            assert tarjan(n,edges)==(want_bridges,want_art),(n,edges)
            graphs+=1;edges_checked+=len(edges);vertices_checked+=n
    assert tarjan(2,[(0,1),(0,1)])==(set(),set())
    return graphs,edges_checked,vertices_checked


def floyd(n,arcs):
    d=[[inf]*n for _ in range(n)]
    for i in range(n):d[i][i]=0
    for u,v,w in arcs:d[u][v]=min(d[u][v],w)
    for k in range(n):
        for i in range(n):
            if d[i][k]==inf:continue
            for j in range(n):
                if d[k][j]!=inf:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d


def johnson(n,arcs):
    p=[0]*n # virtual source q -> every v with weight 0
    for i in range(n):
        changed=False
        for u,v,w in arcs:
            if p[v]>p[u]+w:p[v]=p[u]+w;changed=True
        if not changed:break
        if i==n-1:return None,None
    adj=[[] for _ in range(n)]
    for u,v,w in arcs:
        reduced=w+p[u]-p[v]
        assert reduced>=0
        adj[u].append((v,reduced))
    out=[]
    for s in range(n):
        d=[inf]*n;d[s]=0;heap=[(0,s)]
        while heap:
            c,u=heappop(heap)
            if c!=d[u]:continue
            for v,w in adj[u]:
                if c+w<d[v]:d[v]=c+w;heappush(heap,(d[v],v))
        out.append([x-p[s]+p[v] if x!=inf else inf for v,x in enumerate(d)])
    return out,p


def check_johnson():
    good=bad=pairs=0
    for n in range(2,10):
        for i in range(420):
            dag=i%2==0
            arcs=[(u,v,RNG.randint(-7,9))
                  for u in range(n) for v in range(n)
                  if u!=v and (not dag or u<v) and RNG.randrange(10)<3+i%5]
            d=floyd(n,arcs);negative=any(d[v][v]<0 for v in range(n))
            got,p=johnson(n,arcs)
            if negative:assert got is None;bad+=1;continue
            assert got is not None
            for u in range(n):
                for v in range(n):assert got[u][v]==d[u][v];pairs+=1
            good+=1
    assert good>1800 and bad>100
    got,p=johnson(3,[(0,1,-2),(0,2,5),(1,2,1),(2,1,4)])
    assert p==[0,-2,-1] and got[0]==[0,-2,-1]
    return good,bad,pairs


def forest(n,edges,subset,component_count):
    if len(subset)!=n-component_count:return False
    parent=list(range(n))
    def find(x):
        while x!=parent[x]:x=parent[x]
        return x
    for eid in subset:
        u,v,_=edges[eid];ru,rv=find(u),find(v)
        if ru==rv:return False
        parent[ru]=rv
    return all(find(u)==find(v) for u,v,_ in edges)


def all_forests(n,edges):
    # Independent graph connectivity under all available edges.
    a=[[] for _ in range(n)]
    for u,v,_ in edges:a[u].append(v);a[v].append(u)
    seen=set();count=0
    for v in range(n):
        if v in seen:continue
        count+=1;seen.add(v);stack=[v]
        while stack:
            for w in a[stack.pop()]:
                if w not in seen:seen.add(w);stack.append(w)
    return [frozenset(subset) for subset in combinations(range(len(edges)),n-count)
            if forest(n,edges,subset,count)]


def optima(forests,edges):
    costs=[sum(edges[i][2] for i in F) for F in forests]
    minimum=min(costs)
    return [F for F,c in zip(forests,costs) if c==minimum]


def fundamental_path(n,edges,T,s,t):
    a=[[] for _ in range(n)]
    for eid in T:
        u,v,_=edges[eid];a[u].append((v,eid));a[v].append((u,eid))
    queue=[(s,())];seen={s}
    while queue:
        v,path=queue.pop()
        if v==t:return path
        for w,eid in a[v]:
            if w not in seen:seen.add(w);queue.append((w,path+(eid,)))
    raise AssertionError("not a spanning tree path")


def check_mst_margin():
    graphs=forests_checked=positive=boundary=0
    for n in range(1,8):
        all_edges=list(combinations(range(n),2))
        for it in range(175):
            edges=[(u,v,Fraction(RNG.randint(-7,13))) for u,v in all_edges
                   if RNG.randrange(10)<3+it%5][:10]
            candidates=all_forests(n,edges)
            assert candidates
            F=optima(candidates,edges);T=F[0]
            margins=[]
            for eid,(u,v,w) in enumerate(edges):
                if eid in T:continue
                path=fundamental_path(n,edges,T,u,v)
                heavy=max(path,key=lambda k:edges[k][2])
                margins.append((w-edges[heavy][2],eid,heavy))
            if not margins:
                assert len(candidates)==1
            else:
                gap,eid,heavy=min(margins)
                assert gap>=0
                assert (gap>0)==(len(F)==1)
                if gap>0:
                    positive+=1;eps=gap/3
                    changed=[(u,v,w+eps if RNG.randrange(2) else w-eps)
                             for u,v,w in edges]
                    assert optima(candidates,changed)==[T]
                    halfway=gap/2;changed=edges.copy()
                    u,v,w=changed[eid];changed[eid]=(u,v,w-halfway)
                    u,v,w=changed[heavy];changed[heavy]=(u,v,w+halfway)
                    new_opt=optima(candidates,changed)
                    assert T in new_opt and len(new_opt)>1,(n,edges,T,gap)
                    boundary+=1
            graphs+=1;forests_checked+=len(candidates)
    assert forests_checked>10000 and positive>100
    return graphs,forests_checked,positive,boundary


def source_anchors():
    files=["37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex",
           "38-najkrotsze-drogi-wazone-i-algorytmy-wyszukiwania-tras.tex",
           "39-minimalne-drzewa-rozpinajace-prim-kruskal-dsu.tex"]
    labels=[r"\label{prop:tg-dfs-multigraph-edges}",
            r"\label{thm:tg-weighted-johnson}",
            r"\label{cor:tg-mst-stability-gap}"]
    for name,label in zip(files,labels):
        assert label in (ROOT/name).read_text(encoding="utf-8")


if __name__=="__main__":
    source_anchors()
    print("PASS multigraph Tarjan vs deletion of real edges/vertices:",check_multigraphs())
    print("PASS Johnson vs Floyd-Warshall and negative cycles:",check_johnson())
    print("PASS MST gap under perturbations vs exhaustive forest oracle:",check_mst_margin())
