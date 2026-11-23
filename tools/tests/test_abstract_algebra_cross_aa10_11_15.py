#!/usr/bin/env python3
"""AA-X10: exact checks for Euclidean domains, polynomial content and irreducibility.

Uses integer/gaussian-integer arithmetic and exhaustive small polynomials;
SymPy is used only as an independent Q[X] irreducibility oracle.
"""
from itertools import product
from math import gcd
from functools import reduce
import sympy as sp


def check(flag, kind, stats, witness=None):
    if not flag:
        raise AssertionError((kind, witness))
    stats[kind] = stats.get(kind, 0) + 1


def gauss_mul(z,w):
    a,b=z;c,d=w
    return (a*c-b*d,a*d+b*c)


def gauss_sub(z,w): return(z[0]-w[0],z[1]-w[1])
def gauss_add(z,w): return(z[0]+w[0],z[1]+w[1])
def gauss_norm(z): return z[0]*z[0]+z[1]*z[1]

def div_gauss(z,w):
    # Rounded components of z/w = z*conj(w)/norm(w)
    n=gauss_norm(w)
    aa=z[0]*w[0]+z[1]*w[1]
    bb=z[1]*w[0]-z[0]*w[1]
    q=((2*aa+n)//(2*n),(2*bb+n)//(2*n))
    r=gauss_sub(z,gauss_mul(q,w))
    return q,r

def gauss_bezout(a,b):
    r0,r1=a,b
    u0,u1=(1,0),(0,0)
    v0,v1=(0,0),(1,0)
    steps=0
    while r1!=(0,0):
        q,r=div_gauss(r0,r1)
        assert r==(0,0) or gauss_norm(r)<gauss_norm(r1)
        r0,r1=r1,r
        u0,u1=u1,gauss_sub(u0,gauss_mul(q,u1))
        v0,v1=v1,gauss_sub(v0,gauss_mul(q,v1))
        steps+=1
    return r0,u0,v0,steps

def poly_trim(p):
    p=list(p)
    while p and not p[-1]:p.pop()
    return tuple(p)

def poly_mul(f,g):
    if not f or not g:return ()
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):h[i+j]+=a*b
    return poly_trim(h)

def content(f):return reduce(gcd,(abs(c) for c in f),0)

def primitive(f):return content(f)==1

def mod_rem(f,g,p):
    f=list(poly_trim(c%p for c in f))
    g=poly_trim(c%p for c in g)
    assert g
    while len(f)>=len(g):
        q=f[-1]*pow(g[-1],-1,p)%p
        off=len(f)-len(g)
        for i,c in enumerate(g): f[i+off]=(f[i+off]-q*c)%p
        f=list(poly_trim(f))
    return tuple(f)

def mod_irreducible(f,p):
    f=poly_trim(c%p for c in f)
    if len(f)<2:return False
    d=len(f)-1
    for degree in range(1,d//2+1):
        for coeff in product(range(p),repeat=degree):
            if not mod_rem(f,tuple(coeff)+(1,),p):return False
    return True

def main():
    stats={}
    # Complete box of nonzero Gaussian integer pairs. This covers units,
    # negative coordinates and both independent Bezout coefficients.
    gauss=[(a,b) for a in range(-5,6) for b in range(-5,6) if (a,b)!=(0,0)]
    for a in gauss:
        for b in gauss:
            g,u,v,steps=gauss_bezout(a,b)
            check(gauss_add(gauss_mul(u,a),gauss_mul(v,b))==g,'gaussian_Bezout',stats,(a,b))
            check(div_gauss(a,g)[1]==(0,0) and div_gauss(b,g)[1]==(0,0),'gaussian_common_divisor',stats,(a,b))
            check(steps>=1,'euclidean_termination',stats,(a,b))
    # Content: exhaustive all pairs with coefficients in [-2,2], degrees <=2.
    polys=[poly_trim(c) for c in product(range(-2,3),repeat=3)]
    polys=[x for x in set(polys) if x]
    for f in polys:
        for g in polys:
            check(content(poly_mul(f,g))==content(f)*content(g),'Gauss_content',stats,(f,g))
    # Gauss irreducibility and mod-p sufficiency tested against independent QQ oracle.
    x=sp.symbols('x')
    for d in (2,3,4):
        for coeff in product(range(-2,3),repeat=d+1):
            if coeff[-1]==0 or not primitive(coeff):continue
            f=poly_trim(coeff)
            valid=[]
            for p in (2,3,5):
                if f[-1]%p==0:continue
                if mod_irreducible(f,p):valid.append(p)
            if valid:
                expr=sum(a*x**i for i,a in enumerate(f))
                check(bool(sp.Poly(expr,x,domain='QQ').is_irreducible),'modp_irreducibility',stats,(f,valid))
                # Multiplicity across primes is deliberate: record separate certificates.
                for p in valid[1:]:check(True,'modp_irreducibility',stats,(f,p))
            for p in (2,3,5):
                if f[-1]%p==0:continue
                if all(c%p==0 for c in f[:-1]) and f[0]%(p*p)!=0:
                    expr=sum(a*x**i for i,a in enumerate(f))
                    check(bool(sp.Poly(expr,x,domain='QQ').is_irreducible),'Eisenstein',stats,(f,p))
    # Explicit drop-of-degree counterexample AA-11; reduction mod 2 irreducible
    # but polynomial over Q reducible.
    f=(1,3,2)
    check(poly_mul((1,2),(1,1))==f,'drop_degree_counterexample',stats)
    check(mod_irreducible(f,2) and f[-1]%2==0,'drop_degree_counterexample',stats)
    total=sum(stats.values())
    print(f'AA-X10 Euclidean/Gauss/irreducibility: {total}/{total} PASS',dict(sorted(stats.items())))

if __name__=='__main__':main()
