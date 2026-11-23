#!/usr/bin/env python3
"""AA-X05 independent confirmation via 3x3 integer presentation matrices.

Determinantal invariants from all 1x1, 2x2 and 3x3 minors are compared
with directly enumerated images modulo 2, 3 and 4. Standard library only.
"""
from itertools import product, combinations
from math import gcd

MINORS = tuple((r,c) for r in combinations(range(3),2)
               for c in combinations(range(3),2))


def delta(A):
    d1 = 0
    for v in A:
        d1 = gcd(d1,abs(v))
    d2 = 0
    for (r,s),(c,d) in MINORS:
        d2 = gcd(d2,abs(A[3*r+c]*A[3*s+d]-A[3*r+d]*A[3*s+c]))
    a,b,c,d,e,f,g,h,i = A
    d3 = abs(a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))
    return d1,d2,d3


def smith_invariants(A):
    d1,d2,d3 = delta(A)
    if d1 == 0:
        assert d2 == d3 == 0
        return (0,0,0)
    if d2 == 0:
        assert d3 == 0
        return (d1,0,0)
    assert d2 % d1 == 0
    if d3 == 0:
        return (d1,d2//d1,0)
    assert d3 % d2 == 0
    factors = (d1,d2//d1,d3//d2)
    assert factors[1] % factors[0] == 0
    assert factors[2] % factors[1] == 0
    return factors


def image_size(A,n):
    a,b,c,d,e,f,g,h,i = A
    return len({((a*x+b*y+c*z)%n,(d*x+e*y+f*z)%n,
                 (g*x+h*y+i*z)%n)
                for x,y,z in product(range(n),repeat=3)})


def main():
    ranks = [0,0,0,0]
    minor_checks = modular_checks = 0
    for A in product((-1,0,1),repeat=9):
        factors = smith_invariants(A)
        rank = sum(bool(f) for f in factors)
        ranks[rank] += 1
        minor_checks += 1
        for n in (2,3,4):
            actual = n**3 // image_size(A,n)
            expected = 1
            for d in factors:
                expected *= gcd(d,n) if d else n
            assert actual == expected, (A,n,factors,actual,expected)
            modular_checks += 1

    assert minor_checks == 19683
    assert modular_checks == 59049
    assert ranks == [1,338,7536,11808]
    print('AA-X05 independent 3x3 confirmation: 78732/78732 PASS')
    print('Ranks 0..3:',ranks)


if __name__ == '__main__':
    main()
