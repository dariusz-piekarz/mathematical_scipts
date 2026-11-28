#!/usr/bin/env python3
"""AA-X09: exact checks for Sylow, Jordan-Holder, nilpotence, semidirect products."""
from collections import defaultdict
from itertools import permutations, product
from math import gcd, prod

def ident(n): return tuple(range(n))
def mul(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    v=[0]*len(a)
    for i,x in enumerate(a): v[x]=i
    return tuple(v)
def generate(elems,n):
    gs=set(elems)|{inv(x) for x in elems}
    out={ident(n)};queue=[ident(n)]
    while queue:
        x=queue.pop()
        for g in gs:
            y=mul(x,g)
            if y not in out: out.add(y);queue.append(y)
    return frozenset(out)
def subgroups(G):
    unit=frozenset((ident(len(next(iter(G)))),))
    seen={unit};queue=[unit]
    while queue:
        H=queue.pop()
        for g in G-H:
            K=generate(list(H)+[g],len(g))
            if K not in seen:seen.add(K);queue.append(K)
    return sorted(seen,key=lambda H:(len(H),tuple(sorted(H))))
def conjugate(g,H): return frozenset(mul(mul(g,x),inv(g)) for x in H)
def bracket(a,b): return mul(mul(mul(a,b),inv(a)),inv(b))
def derived(H):return generate({bracket(x,y) for x in H for y in H},len(next(iter(H))))
def lower(H,G):return generate({bracket(x,y) for x in H for y in G},len(next(iter(G))))
def factors(n):
    out=[]
    for p in range(2,n+1):
        if n%p==0 and all(p%a for a in range(2,int(p**0.5)+1)):out.append(p)
    return out
def ppart(n,p):
    a=1
    while n%(a*p)==0:a*=p
    return a

def check_group(name,G,expected):
    G=frozenset(G);subs=subgroups(G);n=len(next(iter(G)))
    one=frozenset((ident(n),));counts=defaultdict(int)
    assert subs[0]==one and subs[-1]==G
    for x in G:
        power=ident(n)
        for k in range(1,len(G)+1):
            power=mul(x,power)
            if power==ident(n):break
        assert len(G)%k==0
        counts['element_orders']+=1
    for H in subs:
        assert len(G)%len(H)==0
        counts['subgroup_Lagrange']+=1
        cosets={frozenset(mul(g,x) for x in H) for g in G}
        assert len(cosets)==len(G)//len(H)
        assert sum(sum(frozenset(mul(g,x) for x in c)==c for c in cosets) for g in G)==len(G)
        counts['coset_action_Burnside']+=2
        NG=frozenset(g for g in G if conjugate(g,H)==H)
        assert len(G)%len(NG)==0 and all(mul(g,x) in NG for g in NG for x in H)
        assert (NG==G)==all(conjugate(g,H)==H for g in G)
        counts['normalizer']+=3
        if name=='D8' and H<G:
            assert len(NG)>len(H)
            counts['nilpotent_normalizer']+=1
    for p in factors(len(G)):
        P=[H for H in subs if len(H)==ppart(len(G),p)]
        assert len(P)==expected[p] and (len(P)-1)%p==0
        assert (len(G)//ppart(len(G),p))%len(P)==0
        assert set(P)=={conjugate(g,P[0]) for g in G}
        for H in subs:
            z=len(H)
            while z>1 and z%p==0:z//=p
            if z==1:
                assert any(H.issubset(K) for K in P)
                counts['Sylow_containment']+=1
        counts['Sylow_conjugacy']+=4
    ds=[G]
    while True:
        K=derived(ds[-1]);counts['derived_series']+=1
        if K==ds[-1]:break
        ds.append(K)
        if len(K)==1:break
    ls=[G]
    while True:
        K=lower(ls[-1],G);counts['lower_central_series']+=1
        if K==ls[-1]:break
        ls.append(K)
        if len(K)==1:break
    nil=len(ls[-1])==1
    assert nil==all(expected[p]==1 for p in factors(len(G)))
    counts['nilpotence_vs_Sylow']+=1
    if name=='S3':assert [len(x) for x in ds]==[6,3,1] and not nil
    if name=='S4':assert [len(x) for x in ds]==[24,12,4,1] and not nil
    if name=='A4':assert [len(x) for x in ds]==[12,4,1] and not nil
    if name=='D8':assert [len(x) for x in ds]==[8,2,1] and [len(x) for x in ls]==[8,2,1] and nil
    if name=='A5':
        assert ds==[G] and not nil
        assert {H for H in subs if all(conjugate(g,H)==H for g in G)}=={one,G}
        counts['A5_simple']+=1
    # Enumerate all maximal subnormal chains, compare Jordan-Holder factors.
    memo={}
    def types(K):
        if K==one:return [()]
        if K not in memo:
            normals=[H for H in subs if H<K and all(conjugate(g,H)==H for g in K)]
            maximal=[H for H in normals if not any(H<J<K for J in normals)]
            memo[K]=[(len(K)//len(H),)+w for H in maximal for w in types(H)]
        return memo[K]
    alltypes=types(G)
    assert alltypes and len({tuple(sorted(z)) for z in alltypes})==1
    for z in alltypes:
        assert prod(z)==len(G) and all(a in (2,3,5,60) for a in z)
        counts['Jordan_Holder_chains']+=1
    counts['example_series']+=1
    return counts,len(subs)

def semidirect():
    count=defaultdict(int)
    for p,q in ((2,3),(2,5),(2,7),(2,11),(3,7),(3,13)):
        autos=[a for a in range(1,q) if gcd(a,q)==1 and pow(a,p,q)==1 and a!=1]
        for a in autos:
            items=list(product(range(q),range(p)))
            def op(x,y):return ((x[0]+pow(a,x[1],q)*y[0])%q,(x[1]+y[1])%p)
            assert len(items)==p*q
            for x in items:
                for y in items:
                    for z in items:
                        assert op(op(x,y),z)==op(x,op(y,z))
                        count['semidirect_associativity']+=1
            is_inv={}
            for x in items:
                ys=[y for y in items if op(x,y)==(0,0) and op(y,x)==(0,0)]
                assert len(ys)==1
                is_inv[x]=ys[0]
                count['semidirect_inverses']+=1
            Q={(i,0) for i in range(q)}
            P={(0,i) for i in range(p)}
            assert all(op(op(g,h),is_inv[g]) in Q for g in items for h in Q)
            assert any(op(op(g,h),is_inv[g]) not in P for g in items for h in P)
            assert len(Q&P)==1
            count['semidirect_normality']+=3
    return count

def main():
    s3=frozenset(permutations(range(3)))
    s4=frozenset(permutations(range(4)))
    a4=frozenset(g for g in s4 if sum(g[i]>g[j] for i in range(4) for j in range(i+1,4))%2==0)
    a5=frozenset(g for g in permutations(range(5)) if sum(g[i]>g[j] for i in range(5) for j in range(i+1,5))%2==0)
    r=(1,2,3,0);s=(0,3,2,1);d8=generate((r,s),4)
    counters=defaultdict(int);sizes={}
    for name,G,expected in (('S3',s3,{2:3,3:1}),('S4',s4,{2:3,3:4}),
                            ('A4',a4,{2:1,3:4}),('D8',d8,{2:1}),('A5',a5,{2:5,3:10,5:6})):
        part,k=check_group(name,G,expected)
        sizes[name]={'order':len(G),'subgroups':k}
        for label,value in part.items():counters[label]+=value
    for label,value in semidirect().items():counters[label]+=value
    total=sum(counters.values())
    print(f'AA-X09 groups: {total}/{total} PASS',sizes,dict(sorted(counters.items())))

if __name__=='__main__':main()
