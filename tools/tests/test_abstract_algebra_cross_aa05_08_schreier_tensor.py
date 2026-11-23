#!/usr/bin/env python3
"""AA-X09: independent finite-index Schreier rewrites and abelian tensor checks."""
from collections import defaultdict,deque
from itertools import product
from math import gcd,lcm

def reduce_word(word):
    stack=[]
    for a in word:
        if stack and stack[-1]==-a:stack.pop()
        else:stack.append(a)
    return tuple(stack)
def invword(w):return tuple(-x for x in reversed(w))
def mulword(a,b):return reduce_word(a+b)
def permutation_inverses(ps):
    out=[]
    for p in ps:
        q=[0]*len(p)
        for i,j in enumerate(p):q[j]=i
        out.append(tuple(q))
    return out

def schreier(perms):
    r=len(perms);d=len(perms[0]);inverse=permutation_inverses(perms)
    assert all(sorted(g)==list(range(d)) for g in perms)
    def step(v,k):return perms[k-1][v] if k>0 else inverse[-k-1][v]
    def endpoint(w):
        v=0
        for k in w:v=step(v,k)
        return v
    letters=tuple(range(1,r+1))+tuple(range(-1,-r-1,-1))
    walks={0:()};tree=set();queue=deque([0])
    while queue:
        v=queue.popleft()
        for k in letters:
            w=step(v,k)
            edge=(v,k) if k>0 else (w,-k)
            if w not in walks:
                walks[w]=walks[v]+(k,)
                tree.add(edge)
                queue.append(w)
    assert len(walks)==d and len(tree)==d-1
    all_edges=[(v,k) for v in range(d) for k in range(1,r+1)]
    free=[e for e in all_edges if e not in tree]
    assert len(free)==1+d*(r-1)
    gen=[]
    for v,k in free:
        w=step(v,k)
        g=reduce_word(walks[v]+(k,)+invword(walks[w]))
        assert endpoint(g)==0 and g
        gen.append(g)
    idx={e:i+1 for i,e in enumerate(free)}
    def rewrite(word):
        pos=0;out=[]
        for k in word:
            w=step(pos,k)
            edge=(pos,k) if k>0 else (w,-k)
            if edge in idx:out.append(idx[edge]*(1 if k>0 else -1))
            pos=w
        return pos,reduce_word(tuple(out))
    checks=defaultdict(int)
    checks['Schreier_edges']+=len(all_edges)
    checks['Schreier_rank_formula']+=1
    for length in range(7):
        for word in product(letters,repeat=length):
            if reduce_word(word)!=word:continue
            pos,rep=rewrite(word)
            if pos==0:
                expanded=()
                for sym in rep:
                    g=gen[abs(sym)-1]
                    expanded=mulword(expanded,g if sym>0 else invword(g))
                assert expanded==word,(word,rep,expanded)
                checks['Schreier_rewriting']+=1
    symbols=tuple(range(1,len(free)+1))+tuple(range(-1,-len(free)-1,-1))
    for length in range(1,4):
        for word in product(symbols,repeat=length):
            if reduce_word(word)!=word:continue
            expanded=()
            for sym in word:
                g=gen[abs(sym)-1]
                expanded=mulword(expanded,g if sym>0 else invword(g))
            assert expanded and endpoint(expanded)==0
            checks['Schreier_independence']+=1
    return checks,(r,d,len(free))

def prime_powers(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            power=1
            while n%p==0:n//=p;power*=p
            out.append((p,power))
        p+=1
    if n>1:out.append((n,n))
    return out

def order_mod(a,n):return n//gcd(a,n)

def primary_decomposition():
    checks=defaultdict(int)
    for m in range(1,21):
        for n in range(1,21):
            primes=sorted({p for k in (m,n) for p,_ in prime_powers(k)})
            primary={}
            for p in primes:
                primary[p]=set()
                for a,b in product(range(m),range(n)):
                    order=lcm(order_mod(a,m),order_mod(b,n))
                    while order>1 and order%p==0:order//=p
                    if order==1:primary[p].add((a,b))
                e=next((v for q,v in prime_powers(m) if q==p),1)
                f=next((v for q,v in prime_powers(n) if q==p),1)
                assert len(primary[p])==e*f
                checks['primary_component_size']+=1
            E=lcm(m,n)
            projections={}
            for p,pk in prime_powers(E):
                t=E//pk
                e=(t*pow(t,-1,pk))%E
                assert e%pk==1%pk
                assert all(e%qq==0 for q,qq in prime_powers(E) if q!=p)
                projections[p]=e
                checks['CRT_projection']+=1
            for a,b in product(range(m),range(n)):
                components={p:(e*a%m,e*b%n) for p,e in projections.items()}
                assert (sum(x for x,_ in components.values())%m,
                        sum(y for _,y in components.values())%n)==(a,b)
                assert all(z in primary[p] for p,z in components.items())
                checks['primary_decomposition']+=1
    return checks

def cyclic_tensor():
    checks=defaultdict(int)
    for m in range(1,61):
        for n in range(1,61):
            d=gcd(m,n)
            for k in range(1,13):
                values={a for a in range(k) if m*a%k==0 and n*a%k==0}
                assert len(values)==gcd(d,k)
                assert values=={((k//gcd(d,k))*a)%k for a in range(k)}
                checks['bilinear_universal_property']+=1
            for a in range(d):
                assert (m*a)%d==0 and (n*a)%d==0
                checks['tensor_cyclic_relations']+=1
    return checks

def main():
    actions=[
        ('index2',((1,0),(0,1))),
        ('index3_normal',((1,2,0),(0,1,2))),
        ('index3_nonnormal',((1,2,0),(1,0,2))),
        ('index4_nonnormal',((1,2,3,0),(1,0,2,3))),
        ('rank3_index3',((1,2,0),(1,0,2),(0,2,1)))]
    counts=defaultdict(int);models=[]
    for name,action in actions:
        part,data=schreier(action);models.append((name,data))
        for k,v in part.items():counts[k]+=v
    for block in (primary_decomposition(),cyclic_tensor()):
        for k,v in block.items():counts[k]+=v
    total=sum(counts.values())
    print(f'AA-X09 Schreier and abelian tensor: {total}/{total} PASS',models,dict(sorted(counts.items())))

if __name__=='__main__':main()
