#!/usr/bin/env python3
"""AA-X07: monic triangular normalization over finite fields and finite-module examples.

Exact sparse-polynomial arithmetic through SymPy, deterministic support families.
"""
from itertools import product
from math import comb
from random import Random
import sympy as sp


def multiindices(n, d):
    return [a for a in product(range(d+1), repeat=n) if 1<=sum(a)<=d]


def transformed_and_weighted(p, n, d, rng):
    X = sp.symbols('x0:'+str(n))
    Y = sp.symbols('y0:'+str(n))
    M = d+2
    weights = [M**(i+1) for i in range(n-1)] + [1]
    exponents=multiindices(n,d)
    # Degree <=d has unique weighted monomial supports by base-M representation.
    weight_set={sum(a*b for a,b in zip(alpha,weights)) for alpha in exponents}
    assert len(weight_set)==len(exponents)
    checks=1
    # Include complete single-monomial cases and deterministic mixed samples.
    chosen=[(alpha,) for alpha in exponents]
    chosen += [tuple(rng.sample(exponents, k)) for k in (2,3) if len(exponents)>=k for _ in range(18)]
    for support in chosen:
        coeffs=[rng.randrange(1,p) for _ in support]
        f=sum((c*sp.prod(x**a for x,a in zip(X,alpha)) for c,alpha in zip(coeffs,support)),sp.S(0))
        sub={X[i]:Y[i]+Y[-1]**weights[i] for i in range(n-1)}
        sub[X[-1]]=Y[-1]
        g=sp.Poly(sp.expand(f.subs(sub,simultaneous=True)),*Y,modulus=p)
        lead=max((sum(a*b for a,b in zip(alpha,weights)), c) for alpha,c in zip(support,coeffs))
        max_deg,cmax=lead
        assert g.degree(Y[-1])==max_deg, ('degree',p,n,d,support)
        assert int(g.coeff_monomial(Y[-1]**max_deg))%p==cmax%p
        assert all((exp[-1]!=max_deg or exp[:-1]==(0,)*(n-1)) for exp,_ in g.terms())
        checks+=3
        # The automorphism has an explicit triangular inverse.
        back={Y[i]:X[i]-X[-1]**weights[i] for i in range(n-1)}
        back[Y[-1]]=X[-1]
        h=sp.Poly(sp.expand(g.as_expr().subs(back,simultaneous=True)),*X,modulus=p)
        assert h==sp.Poly(f,*X,modulus=p)
        checks+=1
    return checks


def explicit_normalization_models(p):
    u,v=sp.symbols('u v')
    checks=0
    # AA-38: x^2+xy+y=0, u=x+y^4, v=y, works also in characteristic 2.
    f=sp.Poly(sp.expand((u+v**4)**2 + (u+v**4)*v+v),v,u,modulus=p)
    assert f.degree(v)==8 and int(f.coeff_monomial(v**8))%p==1
    checks+=1
    if p==2:
        assert f==sp.Poly(v**8+v**5+u*v+u**2+v,v,u,modulus=2)
        checks+=1
    # The monic equation implies a free K[u] basis 1,v,...,v^7.
    G=sp.groebner([f.as_expr()],v,u,order='lex',modulus=p)
    for j in range(8):
        assert G.reduce(v**j)[1]==v**j
        checks+=1
    for j in range(8,18):
        reduced=sp.Poly(G.reduce(v**j)[1],v,u,modulus=p)
        assert reduced.is_zero or reduced.degree(v)<8
        checks+=1
    for degree in range(1,8):
        h=sum(u**i for i in range(degree+1))
        assert sp.Poly(G.reduce(h)[1]-h,v,u,modulus=p).is_zero
        checks+=1
    # Cusp K[t^2,t^3] = K[x,y]/(y^2-x^3), finite over K[x], rank 2.
    cusp=sp.groebner([v**2-u**3],v,u,order='lex',modulus=p)
    for j in range(2,16):
        rem=sp.Poly(cusp.reduce(v**j)[1],v,u,modulus=p)
        assert rem.is_zero or rem.degree(v)<2
        checks+=1
    # Nilpotent algebra K[x,y]/(x^2,y^3) is finite over K, dimension 6.
    nil=sp.groebner([u**2,v**3],u,v,order='lex',modulus=p)
    base=[u**i*v**j for i in range(2) for j in range(3)]
    assert all(nil.reduce(mon)[1]==mon for mon in base)
    checks+=1
    assert all(nil.reduce(u**i*v**j)[1]==0 for i in range(2,5) for j in range(3,6))
    checks+=1
    return checks


def main():
    rng=Random(30740)
    cnt={'weighted_normalization':0,'explicit_models':0}
    for p in (2,3,5):
        for n in (2,3):
            for d in (1,2,3):
                cnt['weighted_normalization']+=transformed_and_weighted(p,n,d,rng)
        cnt['explicit_models']+=explicit_normalization_models(p)
    total=sum(cnt.values())
    print(f'AA-X07 finite-field triangular normalization: {total}/{total} PASS',cnt)


if __name__=='__main__':
    main()
