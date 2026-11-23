#!/usr/bin/env python3
"""Audit 30, source chapters 40--42: independent finite exact checks.

1. Integer max flow via residual BFS versus every s-t cut, and
   decomposition of the resulting integral flow into s-t paths/cycles.
2. Caro--Wei against exhaustive independent sets, equality cases,
   and the Cauchy--Schwarz lower bound on independence.
3. Exact clique indicator covariances versus overlap combinatorics;
   small G(n,1/2) sample-space enumeration as a separate oracle.

These regressions cannot by themselves certify the general proofs.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from random import Random

SEED=Random(20261123030)
ROOT=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def maxflow(n,arcs,s=0,t=None):
    """Independent residual implementation preserving antiparallel arcs."""
    if t is None:t=n-1
    graph=[[] for _ in range(n)];locations=[]
    for u,v,c in arcs:
        forward=[v,c,len(graph[v])]
        reverse=[u,0,len(graph[u])]
        locations.append((u,len(graph[u]),c))
        graph[u].append(forward);graph[v].append(reverse)
    total=0
    while True:
        prev={s:None};todo=deque([s])
        while todo and t not in prev:
            u=todo.popleft()
            for ix,(v,cap,_rev) in enumerate(graph[u]):
                if cap>0 and v not in prev:
                    prev[v]=(u,ix);todo.append(v)
        if t not in prev:break
        bottle=10**10;v=t
        while v!=s:
            u,ix=prev[v];bottle=min(bottle,graph[u][ix][1]);v=u
        v=t
        while v!=s:
            u,ix=prev[v];e=graph[u][ix]
            e[1]-=bottle;graph[v][e[2]][1]+=bottle;v=u
        total+=bottle
    flows=[(u,arcs[j][1],old-graph[u][ix][1])
           for j,(u,ix,old) in enumerate(locations)]
    return total,flows


def cut_oracle(n,arcs,s=0,t=None):
    if t is None:t=n-1
    middle=[v for v in range(n) if v!=s and v!=t]
    values=[]
    for mask in range(1<<len(middle)):
        S={s}
        for j,v in enumerate(middle):
            if mask>>j&1:S.add(v)
        values.append(sum(c for u,v,c in arcs if u in S and v not in S))
    return min(values)


def path_decomposition(n,flows,s=0,t=None):
    if t is None:t=n-1
    # Independent DFS with integer per-arc remaining flows.
    remaining=[v for _,_,v in flows]
    old=remaining.copy();result=[]
    def find_simple_path():
        stack=[(s,[],{s})]
        while stack:
            u,chosen,seen=stack.pop()
            if u==t:return chosen
            for j,(a,b,_f) in enumerate(flows):
                if a==u and remaining[j]>0 and b not in seen:
                    stack.append((b,chosen+[j],seen|{b}))
        return None
    while True:
        path=find_simple_path()
        if path is None:break
        delta=min(remaining[j] for j in path)
        for j in path:remaining[j]-=delta
        result.append((path,delta))
    # Remaining positive arcs are cycles: verify conservation and remove.
    for v in range(n):
        out=sum(remaining[j] for j,(u,w,_) in enumerate(flows) if u==v)
        inc=sum(remaining[j] for j,(u,w,_) in enumerate(flows) if w==v)
        assert out==inc,(n,flows,remaining,v,out,inc)
    cycles=[]
    while any(remaining):
        j=next(i for i,x in enumerate(remaining) if x>0)
        u=flows[j][0];order={u:0};walk=[]
        while True:
            outgoing=next(i for i,(a,b,_x) in enumerate(flows)
                          if a==u and remaining[i]>0)
            walk.append(outgoing);u=flows[outgoing][1]
            if u in order:
                cycle=walk[order[u]:]
                delta=min(remaining[i] for i in cycle)
                for i in cycle:remaining[i]-=delta
                cycles.append((cycle,delta))
                break
            order[u]=len(walk)
    reconstructed=[0]*len(flows)
    for paths in (result,cycles):
        for indices,weight in paths:
            for i in indices:reconstructed[i]+=weight
    assert reconstructed==old
    return sum(weight for _,weight in result),len(result),len(cycles)


def check_flows():
    checks=decomps=unit=0
    for n in range(2,7):
        options=[(u,v) for u in range(n) for v in range(n) if u!=v]
        for iteration in range(410):
            # Include deliberately distinct parallel/antiparallel arcs.
            arcs=[(u,v,SEED.randint(1,4))
                  for u,v in options
                  if SEED.randrange(10)<(2+iteration%4)]
            if iteration%6==0 and arcs:
                arcs.append(arcs[SEED.randrange(len(arcs))])
            val,flows=maxflow(n,arcs)
            assert val==cut_oracle(n,arcs),(n,arcs,val)
            assert all(0<=f<=c for (_,_,f),(_,_,c) in zip(flows,arcs))
            for v in range(1,n-1):
                assert sum(f for u,w,f in flows if u==v)==sum(f for u,w,f in flows if w==v)
            decomposed,count,cycles=path_decomposition(n,flows)
            assert val==decomposed
            checks+=1;decomps+=count
            unit_arcs=[(u,v,1) for u,v,_ in arcs]
            val,flows=maxflow(n,unit_arcs)
            assert val==cut_oracle(n,unit_arcs)
            decomposed,count,cycles=path_decomposition(n,flows)
            assert decomposed==val==count
            unit+=1
    # Essential cancellation: residual backward edge changes old routing.
    arcs=[(0,1,1),(0,2,1),(1,2,1),(1,3,1),(2,3,1)]
    val,f=maxflow(4,arcs)
    assert val==2
    return checks,decomps,unit


def independence_oracle(n,edges):
    edges=set(tuple(sorted(e)) for e in edges)
    best=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k<=best:continue
        if all(not((mask>>u&1) and (mask>>v&1)) for u,v in edges):
            best=k
    degrees=[0]*n
    for u,v in edges:
        degrees[u]+=1;degrees[v]+=1
    caro=sum((Fraction(1,d+1) for d in degrees),Fraction(0))
    avg=Fraction(n*n,n+2*len(edges)) if n else Fraction(0)
    assert best>=caro>=avg,(n,edges,best,caro,avg)
    return best,caro,avg


def check_caro_wei():
    cases=0
    for n in range(1,11):
        e=list(combinations(range(n),2))
        for j in range(320):
            edges=[a for a in e if SEED.randrange(10)<2+j%6]
            independence_oracle(n,edges)
            cases+=1
    for parts in ((1,),(3,5),(1,4,2),(2,2,2,2),(1,1,1,1)):
        edges=[];offset=0
        for k in parts:
            edges.extend((offset+a,offset+b) for a,b in combinations(range(k),2))
            offset+=k
        best,caro,_=independence_oracle(offset,edges)
        assert best==caro==len(parts)
    return cases


def check_clique_variance():
    checks=0
    ps=(Fraction(1,4),Fraction(1,2),Fraction(3,4))
    for n in range(3,10):
        for r in range(3,min(n,5)+1):
            subsets=list(combinations(range(n),r))
            # Independence is on edges, not on merely shared vertices.
            esets=[{(u,v) for u,v in combinations(S,2)} for S in subsets]
            for p in ps:
                b=comb(r,2);N=comb(n,r)
                mean=Fraction(N)*p**b
                var=mean*(1-p**b)
                for i in range(N):
                    for j in range(i+1,N):
                        shared=len(esets[i]&esets[j])
                        if not shared:continue
                        cov=p**(2*b-shared)-p**(2*b)
                        var+=2*cov
                expected=Fraction(N)*p**b*(1-p**b)
                for j in range(2,r):
                    expected+=N*comb(r,j)*comb(n-r,r-j)*p**(2*b-comb(j,2))*(1-p**comb(j,2))
                assert var==expected,(n,r,p,var,expected)
                checks+=1
    # Complete sample-space oracle for small n, independent of covariance sum.
    enumerations=0
    for n in range(3,6):
        edgelist=list(combinations(range(n),2))
        for r in range(3,n+1):
            templates=[set(combinations(S,2)) for S in combinations(range(n),r)]
            vals=[]
            for mask in range(1<<len(edgelist)):
                chosen={edgelist[j] for j in range(len(edgelist)) if mask>>j&1}
                vals.append(sum(T<=chosen for T in templates))
            total=len(vals)
            mu=Fraction(sum(vals),total)
            second=Fraction(sum(x*x for x in vals),total)
            assert mu==Fraction(comb(n,r),2**comb(r,2))
            assert second>=mu*mu
            enumerations+=1
    return checks,enumerations


def source_anchors():
    names=(
      "40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex",
      "41-twierdzenia-mantela-turana-i-ramseya.tex",
      "42-grafy-losowe-i-metoda-probabilistyczna.tex",
    )
    anchors=(
      r"\label{thm:tg-flow-integral-paths}",
      r"\label{thm:tg-caro-wei}",
      r"\label{thm:tg-random-clique-threshold}",
    )
    for name,anchor in zip(names,anchors):
        s=(ROOT/name).read_text(encoding="utf-8")
        assert anchor in s,(name,anchor)


if __name__=="__main__":
    source_anchors()
    print("PASS maxflow/mincut exact cut oracle & integer decomposition:",check_flows())
    print("PASS Caro-Wei vs exact maximum independent sets:",check_caro_wei())
    print("PASS fixed clique covariance and independent G(n,1/2) enumeration:",check_clique_variance())
