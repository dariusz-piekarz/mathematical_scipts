#!/usr/bin/env python3
"""AA-X06: exact finite quotient, radical, localization and Artin-Nakayama checks.

This program uses integer arithmetic only. No source-specific regex assertions.
"""
from math import gcd, lcm, prod


def prime_powers(n):
    out = {}
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out[d] = e
        d += 1
    if n > 1:
        out[n] = 1
    return out


def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]


def radical(d):
    ans = 1
    for p in prime_powers(d):
        ans *= p
    return ans


def ideal(n,d):
    return frozenset(range(0,n,d))


def powers(n,s):
    seen = set()
    t = 1%n
    while t not in seen:
        seen.add(t)
        t = t*s%n
    return frozenset(seen)


def check(cond,what,counters,kind):
    assert cond, what
    counters[kind] += 1


def main():
    counts = {key:0 for key in ('radical','prime_intersection','radical_product',
        'localization_saturation','radical_localization','prime_correspondence',
        'fraction_equivalence','jacobson','nilpotent','crt')}
    for n in range(2,73):
        fac = prime_powers(n)
        ds = divisors(n)
        nilrad = radical(n)
        maximals = [ideal(n,p) for p in fac]
        jac = frozenset.intersection(*maximals)
        check(jac == ideal(n,nilrad),('jacobson',n),counts,'jacobson')
        check(all(pow(x,max(fac.values()),n)==0 for x in jac),
              ('nilpotent J',n),counts,'nilpotent')
        # CRT of all primary components Z/p^e: injectivity + cardinality.
        moduli = [p**e for p,e in fac.items()]
        images = {tuple(x%m for m in moduli) for x in range(n)}
        check(len(images)==n and n==prod(moduli),
              ('CRT',n),counts,'crt')
        for d in ds:
            i=ideal(n,d)
            radical_i=frozenset(a for a in range(n)
                if any(pow(a,k,n) in i for k in range(1,1+max(fac.values()))))
            expected=ideal(n,radical(d))
            check(radical_i==expected,('radical',n,d),counts,'radical')
            containing=[ideal(n,p) for p in fac if d%p==0]
            intersection=frozenset.intersection(*containing) if containing else frozenset(range(n))
            check(intersection==expected,('prime intersection',n,d),counts,'prime_intersection')
        for d in ds:
            for e in ds:
                # radical of IJ, I intersection J, and radical(I) intersection radical(J)
                product=ideal(n,gcd(n,d*e))
                lhs=ideal(n,radical(gcd(n,d*e)))
                rhs=ideal(n,lcm(radical(d),radical(e)))
                check(lhs==ideal(n,radical(lcm(d,e)))==rhs,
                      ('radical products',n,d,e),counts,'radical_product')
        for s in range(1,n):
            S=powers(n,s)
            if 0 in S:
                continue  # zero cannot be inverted in the convention of AA-12.
            retained={p:e for p,e in fac.items() if s%p!=0}
            m=prod(p**e for p,e in retained.items())
            assert m>1
            # Reduction Z/n -> Z/m defines localization; elements of S become units.
            assert all(gcd(u,m)==1 for u in S)
            for d in ds:
                saturation=frozenset(a for a in range(n)
                    if any(u*a%d==0 for u in S))
                stripped=d
                for p in fac:
                    if s%p==0:
                        while stripped%p==0:
                            stripped//=p
                check(saturation==ideal(n,stripped),
                      ('saturation',n,s,d,stripped),counts,'localization_saturation')
                rad_after=radical(stripped)
                check(ideal(n,rad_after)==frozenset(a for a in range(n)
                     if any(u*pow(a,max(fac.values()),n)%d==0 for u in S)),
                      ('radical commutation',n,s,d),counts,'radical_localization')
            check({p for p in fac if p not in retained}=={p for p in fac if s%p==0},
                  ('prime correspondence',n,s),counts,'prime_correspondence')
            if n<=16:
                # Complete relation on fractions (a,t),(b,u) in (Z/n)xS.
                # Independent reduction to Z/m with inverses there.
                pairs=[(a,t) for t in sorted(S) for a in range(n)]
                for a,t in pairs:
                    image_a=a*pow(t,-1,m)%m
                    for b,u in pairs:
                        rel=any(v*(a*u-b*t)%n==0 for v in S)
                        reduction=image_a==b*pow(u,-1,m)%m
                        check(rel==reduction,('fraction',n,s,a,t,b,u),
                              counts,'fraction_equivalence')
    total=sum(counts.values())
    print(f'AA-X06 exact finite rings: {total}/{total} PASS',counts)


if __name__=='__main__':
    main()
