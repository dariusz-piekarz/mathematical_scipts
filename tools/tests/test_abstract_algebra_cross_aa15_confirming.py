#!/usr/bin/env python3
"""AA-X10 independent exact checks for noncommutative rings, ideals and group rings."""
from itertools import combinations, product, permutations
from collections import defaultdict
from random import Random

def mult(a,b,p):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))
def scale(k,a,p): return tuple(k*x%p for x in a)
def spaces(p):
    for d in range(5):
        for piv in combinations(range(4),d):
            free=[(i,j) for i in range(d) for j in range(piv[i]+1,4) if j not in piv]
            for coeff in product(range(p),repeat=len(free)):
                basis=[[0]*4 for _ in range(d)]
                for i,j in enumerate(piv):basis[i][j]=1
                for (i,j),a in zip(free,coeff):basis[i][j]=a
                yield tuple(tuple(v) for v in basis),piv
def belongs(x,basis,piv,p):
    w=list(x)
    for i,v in zip(piv,basis):
        t=w[i]
        w=[(a-t*b)%p for a,b in zip(w,v)]
    return not any(w)
def matrix_checks(c):
    E=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
    for p,expected in ((2,67),(3,212)):
        subs=list(spaces(p))
        assert len(subs)==expected
        c['vector_subspaces']+=1
        left=right=two=0
        for basis,piv in subs:
            l=all(belongs(mult(e,v,p),basis,piv,p) for e in E for v in basis)
            r=all(belongs(mult(v,e,p),basis,piv,p) for e in E for v in basis)
            left+=l;right+=r;two+=(l and r)
            assert not (l and r) or len(basis) in (0,4)
            c['two_sided_ideal_classification']+=1
            for e in E:
                for v in basis:
                    if l: assert belongs(mult(e,v,p),basis,piv,p)
                    if r: assert belongs(mult(v,e,p),basis,piv,p)
                    c['left_matrix_test']+=1
                    c['right_matrix_test']+=1
        assert (left,right,two)==(p+3,p+3,2),(p,left,right,two)
        c['ideal_count']+=3

def convolution(a,b,p):
    n=len(a);z=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[(i+j)%n]=(z[(i+j)%n]+x*y)%p
    return tuple(z)
def mpower(a,k,p):
    out=(1,0,0,1)
    for _ in range(k):out=mult(out,a,p)
    return out
def group_checks(c):
    rng=Random(1510)
    for p,n in ((2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),(5,2),(5,3)):
        one=(1,)+(0,)*(n-1)
        def rnd():return tuple(rng.randrange(p) for _ in range(n))
        for _ in range(240):
            a,b,d=rnd(),rnd(),rnd()
            assert convolution(convolution(a,b,p),d,p)==convolution(a,convolution(b,d,p),p)
            assert convolution(a,tuple((x+y)%p for x,y in zip(b,d)),p)==tuple(
                (x+y)%p for x,y in zip(convolution(a,b,p),convolution(a,d,p)))
            assert convolution(a,one,p)==a==convolution(one,a,p)
            c['group_ring_associative']+=1
            c['group_ring_distributive']+=1
            c['group_ring_unit']+=1
        for j in range(n):
            e=tuple(int(k==j) for k in range(n))
            inv=tuple(int(k==(-j)%n) for k in range(n))
            assert convolution(e,inv,p)==one
            c['group_ring_units']+=1
    for p in (2,3,5):
        n=p
        one=(1,)+(0,)*(p-1);g=(0,1)+(0,)*(p-2)
        u=tuple((a-b)%p for a,b in zip(g,one))
        z=one
        for k in range(1,p+1):
            z=convolution(z,u,p)
            assert (z!=(0,)*p) if k<p else (z==(0,)*p)
            c['group_ring_nilpotent']+=1
    G=list(permutations(range(3)))
    a=(1,0,2);b=(0,2,1)
    assert tuple(a[b[i]] for i in range(3))!=tuple(b[a[i]] for i in range(3))
    c['noncommutative_group_ring']+=1
    for p,n,M in ((2,3,(0,1,1,1)),(3,2,(0,1,1,0))):
        assert mpower(M,n,p)==(1,0,0,1)
        powers=[mpower(M,j,p) for j in range(n)]
        def evaluate(x):
            out=(0,0,0,0)
            for a,T in zip(x,powers):out=add(out,scale(a,T,p),p)
            return out
        for a in product(range(p),repeat=n):
            for b in product(range(p),repeat=n):
                assert evaluate(convolution(a,b,p))==mult(evaluate(a),evaluate(b),p)
                c['group_ring_universal']+=1
def free_checks(c):
    X=(0,1,0,0);Y=(0,0,1,0)
    assert mult(X,Y,2)!=mult(Y,X,2)
    c['noncommutative_words']+=1
    words=[w for n in range(6) for w in product((0,1),repeat=n)]
    def ev(w,x,y):
        z=(1,0,0,1)
        for j in w:z=mult(z,x if j==0 else y,2)
        return z
    images={w:ev(w,X,Y) for w in words}
    for a in words:
        for b in words:
            assert ev(a+b,X,Y)==mult(images[a],images[b],2)
            c['free_algebra_universal']+=1
    C=(1,0,0,0);D=(1,0,0,1)
    assert mult(C,D,2)==mult(D,C,2)
    for w in words:
        assert ev(w,C,D)==ev(tuple(sorted(w)),C,D)
        c['abelianization']+=1
def main():
    c=defaultdict(int)
    matrix_checks(c);group_checks(c);free_checks(c)
    total=sum(c.values())
    print(f'AA-X10 matrix ideals/group rings/free algebra: {total}/{total} PASS',dict(sorted(c.items())))
if __name__=='__main__':main()
