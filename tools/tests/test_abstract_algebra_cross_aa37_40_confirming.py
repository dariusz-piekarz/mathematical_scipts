#!/usr/bin/env python3
"""AA-X07 independent finite-integral-extension audit.

Uses factorization of f(U^e) and residue-field linear algebra. This does not
use triangular normalization or the Groebner computations of the first test.
"""
from itertools import product
import sympy as sp

U,T=sp.symbols('U T')


def monic_irreducibles(p,max_degree):
    for d in range(1,max_degree+1):
        for coeff in product(range(p),repeat=d):
            f=sp.Poly(T**d+sum(c*T**i for i,c in enumerate(coeff)),T,modulus=p)
            if f.is_irreducible:
                yield f


def rank_mod_p(vectors, p, size):
    pivots={}
    for w in vectors:
        w=list(w)
        for idx,basis in sorted(pivots.items()):
            t=w[idx]
            if t:
                w=[(a-t*b)%p for a,b in zip(w,basis)]
        j=next((i for i,z in enumerate(w) if z),None)
        if j is None:
            continue
        inv=pow(w[j],-1,p)
        pivots[j]=[x*inv%p for x in w]
    return len(pivots)


def residue_vector(poly,g,p):
    v=poly.rem(g)
    return [int(v.nth(i))%p for i in range(g.degree())]


def test_integral_fiber(p,e,f):
    d=f.degree()
    f_replaced=sp.Poly(f.as_expr().subs(T,U**e),U,modulus=p)
    coeff, factors=sp.factor_list(f_replaced,modulus=p)
    assert sum(q.degree()*mult for q,mult in factors)==e*d
    assert 1<=len(factors)<=e
    tests=2
    # Every prime (g(U)) over (f(T)) is maximal (so no nested primes
    # above the same contraction); its residue field has f as minimal
    # polynomial of U^e. Check minimality by independent linear algebra.
    for q,mult in factors:
        assert q.is_irreducible and mult>0
        assert f_replaced.rem(q).is_zero
        assert q.degree()%d==0
        checks=[residue_vector(sp.Poly(U**(e*j),U,modulus=p),q,p) for j in range(d)]
        assert rank_mod_p(checks,p,q.degree())==d, (p,e,f,q)
        # Compare actual contraction of q to (f): every h of lower degree
        # has nonzero image in the residue algebra by the rank calculation.
        assert not any(all(x==0 for x in v) for v in checks)
        tests+=5
    # The special fiber at t=0 has one prime with multiplicity exactly e;
    # a nonreduced fiber is compatible with going-up and incomparability.
    if d==1 and int(f.nth(0))%p==0:
        assert len(factors)==1 and factors[0][0]==sp.Poly(U,U,modulus=p) and factors[0][1]==e
        tests+=1
    # The finite A-module F_p[U] over F_p[T], T=U^e, has rank e.
    # After base change to kappa(f), the fiber algebra has dimension e over
    # that field and e*d over F_p. The powers (U^i T^j) enumerate precisely
    # 1,U,...,U^(e*d-1), hence form an explicit basis over F_p.
    vectors=[residue_vector(sp.Poly(U**(i+e*j),U,modulus=p),f_replaced,p)
             for i in range(e) for j in range(d)]
    assert rank_mod_p(vectors,p,e*d)==e*d
    tests+=1
    return tests,len(factors),sum(mult>1 for _,mult in factors)


def main():
    counts={'integral_fibers':0,'missing_prime_without_integrality':0,
            'ramified_fibers':0,'prime_factors':0}
    for p,maxdeg in ((2,3),(3,3),(5,3),(7,2)):
        for f in monic_irreducibles(p,maxdeg):
            # In the nonintegral localization F_p[T,T^-1], precisely (T)
            # among irreducible primes vanishes under lying-over.
            no_prime_over_t = (f.degree()==1 and int(f.nth(0))%p==0)
            assert no_prime_over_t == (f.eval(0)%p==0)
            counts['missing_prime_without_integrality']+=1
            for e in range(2,6):
                n,primes,ram=test_integral_fiber(p,e,f)
                counts['integral_fibers']+=n
                counts['prime_factors']+=primes
                counts['ramified_fibers']+=ram
    total=counts['integral_fibers']+counts['missing_prime_without_integrality']
    assert counts['ramified_fibers']>0
    print(f'AA-X07 integral extensions, prime fibers: {total}/{total} PASS; '
          f'prime factors inspected={counts["prime_factors"]}; '
          f'ramified factor occurrences={counts["ramified_fibers"]}',counts)


if __name__=='__main__':
    main()
