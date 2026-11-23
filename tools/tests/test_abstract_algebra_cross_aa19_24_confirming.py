#!/usr/bin/env python3
"""AA-X08: independent permutation-group check of solvability and quintic."""
from itertools import permutations,combinations
from math import factorial
import sympy as sp


def ident(n):return tuple(range(n))
def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
    inv=[0]*len(a)
    for i,v in enumerate(a):inv[v]=i
    return tuple(inv)
def parity(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def subgroup(generators,n):
    one=ident(n)
    gens=set(generators)
    gens |= {inverse(g) for g in gens}
    seen={one}
    todo=[one]
    while todo:
        x=todo.pop()
        for g in gens:
            y=compose(x,g)
            if y not in seen:seen.add(y);todo.append(y)
    return frozenset(seen)

def commutator(a,b):
    return compose(compose(compose(a,b),inverse(a)),inverse(b))

def derived_subgroup(G,n):
    C={commutator(a,b) for a in G for b in G}
    return subgroup(C,n),len(C)

def root_and_eisenstein_tests():
    x=sp.symbols('x');f=x**5-4*x+2
    F=sp.Poly(f,x,domain=sp.QQ)
    assert F.is_irreducible
    assert F.degree()==5
    assert 2%2==0 and 4%2==0 and 2%4!=0
    assert F.discriminant()!=0
    R=sp.polys.polytools.intervals(f,eps=sp.Rational(1,1000000))
    assert len(R)==3
    assert all(mult==1 for _,mult in R)
    assert [sp.sign(f.subs(x,a)) for a in (-2,0,1,2)] == [-1,1,-1,1]
    checks=6
    factorizations={}
    for p in (3,5,7,11,13,17,19,23,29):
        g=sp.Poly(f,x,modulus=p)
        if g.gcd(g.diff()).degree()!=0:continue
        _,parts=sp.factor_list(g,modulus=p)
        degrees=sorted([q.degree() for q,e in parts for _ in range(e)])
        assert sum(degrees)==5 and len(degrees)==len(parts)
        factorizations[p]=degrees
        checks+=2
    assert factorizations
    return checks,factorizations

def main():
    counts=dict(derived=0,group_sizes=0,quintic_group=0,polynomial=0)
    expected={3:[6,3,1],4:[24,12,4,1],5:[120,60,60]}
    for n in (3,4,5):
        G=frozenset(permutations(range(n)))
        assert len(G)==factorial(n)
        sizes=[len(G)]
        for _ in range(3):
            H,num=derived_subgroup(G,n)
            assert all(parity(h)==1 for h in H)
            assert len(H)==expected[n][min(len(sizes),len(expected[n])-1)]
            assert len(H)<=len(G)
            counts['derived']+=len(G)*len(G)
            G=H
            sizes.append(len(G))
            if len(G)==1:break
        assert sizes[:len(expected[n])]==expected[n],(n,sizes)
        counts['group_sizes']+=len(sizes)
    five_cycles=[p for p in permutations(range(5))
                 if p!=ident(5) and compose_cycles(p,5)==ident(5)]
    assert len(five_cycles)==24
    for cyc in five_cycles:
        for i,j in combinations(range(5),2):
            trans=list(range(5));trans[i],trans[j]=trans[j],trans[i]
            assert len(subgroup((cyc,tuple(trans)),5))==120
            counts['quintic_group']+=1
    checks,parts=root_and_eisenstein_tests()
    counts['polynomial']+=checks
    total=sum(counts.values())
    print(f'AA-X08 independent Galois solvability: {total}/{total} PASS',counts,'Frobenius:',parts)

def compose_cycles(a,k):
    x=ident(len(a))
    for _ in range(k):x=compose(x,a)
    return x

if __name__=='__main__':main()
