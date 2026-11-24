#!/usr/bin/env python3
"""Independent finite audit for chapters 01--05 of graph and knot theory.

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


def test_chapter02_bfs():
    """Compare FIFO BFS with independent all-pairs shortest paths."""
    graphs=roots=runs=distances=edge_checks=0
    for n in range(1,6):
        es=pairs(n)
        for mask in range(1<<len(es)):
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            a=adj_of(n,edges)
            # Floyd--Warshall, with n as a sentinel above any finite distance.
            d=[[0 if u==v else 1 if v in a[u] else n
                for v in range(n)] for u in range(n)]
            for k in range(n):
                for u in range(n):
                    for v in range(n):
                        d[u][v]=min(d[u][v],d[u][k]+d[k][v])
            if n in d[0]:
                continue
            graphs+=1
            for r in range(n):
                roots+=1
                for reverse in (False,True):
                    runs+=1
                    h=[None]*n
                    parent=[None]*n
                    h[r]=0
                    q=deque([r])
                    processed=[]
                    while q:
                        u=q.popleft()
                        processed.append(h[u])
                        for v in sorted(a[u],reverse=reverse):
                            if h[v] is None:
                                h[v]=h[u]+1
                                parent[v]=u
                                q.append(v)
                        levels=[h[v] for v in q]
                        assert levels==sorted(levels)
                        assert not levels or levels[-1]-levels[0]<=1
                    assert len(processed)==n
                    assert processed==sorted(processed)
                    assert h==d[r], (n,edges,r,h,d[r])
                    assert parent[r] is None
                    for v in range(n):
                        distances+=1
                        u=v
                        visited=set()
                        while u!=r:
                            assert u not in visited
                            visited.add(u)
                            p=parent[u]
                            assert p in a[u] and h[p]==h[u]-1
                            u=p
                        assert len(visited)==h[v]
                    for u,v in edges:
                        edge_checks+=1
                        assert abs(h[u]-h[v])<=1
    return graphs,roots,runs,distances,edge_checks


def test_chapter03_euler_multigraphs():
    """Compare Euler criteria with exact enumeration of edge-identity trails."""
    directed_count=undirected_count=closed=open_count=orientations=0
    for directed in (False,True):
        for n in range(1,4):
            types=[(u,v) for u in range(n)
                   for v in range(0 if directed else u,n)]
            for multiplicities in product(range(3),repeat=len(types)):
                m=sum(multiplicities)
                if not 1<=m<=6:
                    continue
                edges=[e for e,k in zip(types,multiplicities) for _ in range(k)]
                if directed:
                    directed_count+=1
                else:
                    undirected_count+=1
                deg=[0]*n
                balance=[0]*n
                for u,v in edges:
                    deg[u]+=1
                    deg[v]+=1
                    balance[u]+=1
                    balance[v]-=1
                active={v for v in range(n) if deg[v]}
                adj=adj_of(n,edges)
                seen={min(active)}
                q=list(seen)
                for u in q:
                    for v in adj[u]:
                        if v not in seen:
                            seen.add(v)
                            q.append(v)
                connected=active==seen
                odd={v for v in range(n) if deg[v]%2}
                full=(1<<m)-1

                @lru_cache(None)
                def endpoints(u,used):
                    if used==full:
                        return 1<<u
                    result=0
                    for i,(a,b) in enumerate(edges):
                        if used>>i&1:
                            continue
                        if a==u:
                            result |= endpoints(b,used|(1<<i))
                        elif not directed and b==u:
                            result |= endpoints(a,used|(1<<i))
                    return result

                for start in range(n):
                    actual=endpoints(start,0)
                    for finish in range(n):
                        if start==finish:
                            closed+=1
                            expected=(connected and start in active and
                                      (not any(balance) if directed else not odd))
                        else:
                            open_count+=1
                            expected=(connected and
                                      (all(balance[v]==(int(v==start)-int(v==finish))
                                           for v in range(n))
                                       if directed else odd=={start,finish}))
                        assert bool(actual>>finish&1)==bool(expected), (
                            directed,n,edges,start,finish,expected)
                endpoints.cache_clear()
                if not directed:
                    orientations+=1
                    balanced=False
                    for mask in range(1<<m):
                        b=[0]*n
                        for i,(u,v) in enumerate(edges):
                            if mask>>i&1:
                                u,v=v,u
                            b[u]+=1
                            b[v]-=1
                        if not any(b):
                            balanced=True
                            break
                    assert balanced==(not odd), (n,edges)
    assert (directed_count,undirected_count,closed,open_count,orientations)==(
        3137,462,10688,21166,462)
    return directed_count,undirected_count,closed,open_count,orientations


def test_chapter03_constructions():
    """Validate constructive DFS orientations and Hierholzer splicing."""
    graphs=dfs_runs=hier_runs=incidence_reads=0
    for n in range(2,6):
        es=pairs(n)
        for mask in range(1<<len(es)):
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            if component_count(n,edges)!=1:
                continue
            graphs+=1
            expected=all(component_count(n,edges[:i]+edges[i+1:])==1
                         for i in range(len(edges)))
            adj=adj_of(n,edges)
            for root in range(n):
                for reverse in (False,True):
                    dfs_runs+=1
                    parent=[None]*n
                    depth=[-1]*n
                    depth[root]=0

                    def dfs(u):
                        for v in sorted(adj[u],reverse=reverse):
                            if depth[v]<0:
                                parent[v]=u
                                depth[v]=depth[u]+1
                                dfs(v)

                    dfs(root)
                    assert all(d>=0 for d in depth)
                    directed=[[] for _ in range(n)]
                    for u,v in edges:
                        if parent[v]==u:
                            directed[u].append(v)
                        elif parent[u]==v:
                            directed[v].append(u)
                        else:
                            x,y=(u,v) if depth[u]>depth[v] else (v,u)
                            z=x
                            while z is not None and z!=y:
                                z=parent[z]
                            assert z==y, (edges,root,x,y)
                            directed[x].append(y)
                    strong=True
                    for start in range(n):
                        seen={start}
                        q=[start]
                        for u in q:
                            for v in directed[u]:
                                if v not in seen:
                                    seen.add(v)
                                    q.append(v)
                        strong &= len(seen)==n
                    assert strong==expected, (edges,root,reverse)
    for n in range(1,4):
        types=[(u,v) for u in range(n) for v in range(u,n)]
        for counts in product(range(3),repeat=len(types)):
            m=sum(counts)
            if not 1<=m<=6:
                continue
            edges=[e for e,k in zip(types,counts) for _ in range(k)]
            adj=[[] for _ in range(n)]
            for i,(u,v) in enumerate(edges):
                adj[u].append((v,i))
                adj[v].append((u,i))
            if any(len(a)%2 for a in adj):
                continue
            active={u for u in range(n) if adj[u]}
            if component_count(n,edges)!=n-len(active)+1:
                continue
            for start in sorted(active):
                for reverse in (False,True):
                    hier_runs+=1
                    lists=[list(reversed(a)) if reverse else a for a in adj]
                    pos=[0]*n
                    used=set()
                    # Nodes are indices into arrays; splice by changing links.
                    vertex=[start]
                    incoming=[None]
                    link=[None]
                    q=deque([0])
                    reads=0

                    def next_edge(u):
                        nonlocal reads
                        while pos[u]<len(lists[u]):
                            v,i=lists[u][pos[u]]
                            pos[u]+=1
                            reads+=1
                            if i not in used:
                                used.add(i)
                                return v,i
                        return None

                    while q:
                        node=q.popleft()
                        u=vertex[node]
                        tail=node
                        old=link[node]
                        while (step:=next_edge(u)) is not None:
                            v,i=step
                            fresh=len(vertex)
                            vertex.append(v)
                            incoming.append(i)
                            link.append(None)
                            link[tail]=fresh
                            tail=fresh
                            q.append(fresh)
                            u=v
                        assert u==vertex[node]
                        link[tail]=old
                    assert len(vertex)==m+1 and reads<=2*m
                    ids=[]
                    node=0
                    while link[node] is not None:
                        nxt=link[node]
                        i=incoming[nxt]
                        u,v=edges[i]
                        assert (vertex[node],vertex[nxt]) in ((u,v),(v,u))
                        ids.append(i)
                        assert len(ids)<=m
                        node=nxt
                    assert vertex[node]==start
                    assert sorted(ids)==list(range(m))
                    incidence_reads+=reads
    assert (graphs,dfs_runs,hier_runs,incidence_reads)==(771,7612,456,4320)
    return graphs,dfs_runs,hier_runs,incidence_reads


def test_chapter04_menger():
    """Independent packing of simple paths versus enumerated separators."""
    def reachable(n,edges,start,finish,removed=0):
        adj=adj_of(n,edges)
        seen={start}
        q=[start]
        for u in q:
            for v in adj[u]:
                if not (removed>>v&1) and v not in seen:
                    seen.add(v)
                    q.append(v)
        return finish in seen

    def parameters(n,edges):
        k=n-1
        for mask in range(1<<n):
            size=mask.bit_count()
            if size>=k:
                continue
            live=[v for v in range(n) if not (mask>>v&1)]
            if any(not reachable(n,edges,live[0],v,mask) for v in live[1:]):
                k=size
        lam=min(sum(((mask>>u)&1)!=((mask>>v)&1) for u,v in edges)
                for mask in range(1,(1<<n)-1))
        delta=min(len(a) for a in adj_of(n,edges))
        return k,lam,delta

    def pack(masks):
        # Each distinct simple path is considered exactly once, including st.
        best={0:0}
        for p in masks:
            new=best.copy()
            for used,count in best.items():
                if not (used&p):
                    new[used|p]=max(new.get(used|p,0),count+1)
            best=new
        return max(best.values())

    graphs=pair_count=adjacent=0
    for n in range(2,6):
        es=pairs(n)
        for mask in range(1<<len(es)):
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            if component_count(n,edges)!=1:
                continue
            graphs+=1
            k,lam,delta=parameters(n,edges)
            assert k<=lam<=delta
            adj=[[] for _ in range(n)]
            for i,(u,v) in enumerate(edges):
                adj[u].append((v,i))
                adj[v].append((u,i))
            vertex_min=edge_min=n
            for start,finish in es:
                pair_count+=1
                vm=[]
                em=[]
                endpoints=(1<<start)|(1<<finish)

                def dfs(u,seen,used):
                    if u==finish:
                        vm.append(seen&~endpoints)
                        em.append(used)
                        return
                    for v,i in adj[u]:
                        if not (seen>>v&1):
                            dfs(v,seen|(1<<v),used|(1<<i))

                dfs(start,1<<start,0)
                rv,re=pack(vm),pack(em)
                vertex_min=min(vertex_min,rv)
                edge_min=min(edge_min,re)
                ec=min(sum(((cut>>u)&1)!=((cut>>v)&1) for u,v in edges)
                       for cut in range(1,(1<<n)-1)
                       if (cut>>start&1) and not (cut>>finish&1))
                assert re==ec, (n,edges,start,finish)
                is_adjacent=(start,finish) in edges
                h=[e for e in edges if e!=(start,finish)]
                sep=min(cut.bit_count() for cut in range(1<<n)
                        if not cut&endpoints and
                        not reachable(n,h,start,finish,cut))
                assert rv==sep+int(is_adjacent), (n,edges,start,finish)
                adjacent+=int(is_adjacent)
            assert (vertex_min,edge_min)==(k,lam)
    examples=[
        (9,pairs(4)+[(u+4,v+4) for u,v in pairs(4)]
           +[(0,8),(1,8),(4,8),(5,8)],(1,2,3)),
        (5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],(1,2,2)),
        (8,pairs(4)+[(u+4,v+4) for u,v in pairs(4)]+[(0,4)],(1,1,3)),
    ]
    for n,edges,expected in examples:
        assert parameters(n,edges)==expected
    assert (graphs,pair_count,adjacent)==(771,7521,4294)
    return graphs,pair_count,adjacent,len(examples)


def test_chapter05_hall_hamilton():
    """Enumerate indexed set families, matchings, covers and Hamilton cycles."""
    families=sdr_count=graphs=ham_count=component_checks=0
    for n in range(5):
        for m in range(4):
            for sets in product(range(1<<m),repeat=n):
                families+=1
                deficiency=0
                for selected in range(1<<n):
                    union=0
                    for i,a in enumerate(sets):
                        if selected>>i&1:
                            union|=a
                    deficiency=max(deficiency,selected.bit_count()-union.bit_count())

                @lru_cache(None)
                def maximum(i,used):
                    if i==n:
                        return 0
                    return max([maximum(i+1,used)]+[
                        1+maximum(i+1,used|(1<<j))
                        for j in range(m) if sets[i]>>j&1 and not (used>>j&1)])

                nu=maximum(0,0)
                maximum.cache_clear()
                assert nu==n-deficiency
                sdr_count+=int(nu==n)
                edges=[(i,n+j) for i,a in enumerate(sets)
                       for j in range(m) if a>>j&1]
                tau=min(c.bit_count() for c in range(1<<(n+m))
                        if all((c>>u&1) or (c>>v&1) for u,v in edges))
                assert tau==nu
    for n in range(3,6):
        es=pairs(n)
        for mask in range(1<<len(es)):
            graphs+=1
            edges=[e for i,e in enumerate(es) if mask>>i&1]
            adj=adj_of(n,edges)
            ham=any(all(v in adj[u] for u,v in zip(
                    (0,)+p,p+(0,))) for p in permutations(range(1,n)))
            dirac=2*min(map(len,adj))>=n
            ore=all(len(adj[u])+len(adj[v])>=n
                    for u,v in es if v not in adj[u])
            assert not dirac or ore
            assert not ore or ham
            if not ham:
                continue
            ham_count+=1
            for removed in range(1,1<<n):
                component_checks+=1
                live=[v for v in range(n) if not (removed>>v&1)]
                index={v:i for i,v in enumerate(live)}
                residual=[(index[u],index[v]) for u,v in edges
                          if u in index and v in index]
                assert component_count(len(live),residual)<=removed.bit_count()
    assert (families,sdr_count,graphs,ham_count,component_checks)==(
        5058,315,1096,229,6915)
    return families,sdr_count,graphs,ham_count,component_checks


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
    g,r,b,d,e=test_chapter02_bfs()
    print(f"PASS chapter 02 BFS: {g} connected graphs, {r} roots, {b} runs, {d} distances, {e} edge checks")

    d,u,c,o,b=test_chapter03_euler_multigraphs()
    print(f"PASS chapter 03 Euler: {d} directed, {u} undirected multigraphs, {c} closed endpoint pairs, {o} open endpoint pairs, {b} balanced orientation cases")

    g,d,h,i=test_chapter03_constructions()
    print(f"PASS chapter 03 constructions: {g} graphs, {d} DFS orientations, {h} Hierholzer runs, {i} incidence reads")

    g,p,a,e=test_chapter04_menger()
    print(f"PASS chapter 04 Menger: {g} connected graphs, {p} endpoint pairs, {a} adjacent endpoint pairs, {e} strict Whitney examples")

    f,s,g,h,c=test_chapter05_hall_hamilton()
    print(f"PASS chapter 05 Hall/Hamilton: {f} families, {s} SDR cases, {g} graphs, {h} Hamiltonian graphs, {c} component checks; deficiency, Konig, Dirac, Ore")
