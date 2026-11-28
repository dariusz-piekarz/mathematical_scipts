#!/usr/bin/env python3
"""AA-X04 independent exact cyclotomic discriminant, resultant and reduction checks."""
import sympy as sp

X = sp.Symbol("X")
N = 30
PRIMES = (2, 3, 5, 7, 11)


def main():
    counts = dict(discriminants=0, disc_resultant=0,
                  pair_resultants=0, modular_gcd=0)
    phi = {n: sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
           for n in range(2, N + 1)}

    def require(condition, reason, section):
        assert condition, reason
        counts[section] += 1

    for n in range(3, N + 1):
        f = phi[n]
        degree = int(sp.totient(n))
        disc = int(sp.discriminant(f.as_expr(), X))
        # Valid for n>=3; phi(n) is even.
        predicted = (-1) ** (degree // 2) * n ** degree
        for prime in sp.factorint(n):
            predicted //= prime ** (degree // (prime - 1))
        require(disc == predicted,
                f"cyclotomic discriminant n={n}", "discriminants")
        res = int(sp.resultant(f.as_expr(), sp.diff(f.as_expr(), X), X))
        require(disc == (-1) ** (degree * (degree - 1) // 2) * res,
                f"derivative resultant n={n}", "disc_resultant")
        for p in PRIMES:
            reduced = sp.Poly(f.as_expr(), X, modulus=p)
            squarefree = reduced.gcd(reduced.diff()).degree() == 0
            require(squarefree == (disc % p != 0),
                    f"modular squarefree n={n}, p={p}", "modular_gcd")

    for m in range(3, N + 1):
        for n in range(2, m):
            r = abs(int(sp.resultant(phi[m].as_expr(),
                                     phi[n].as_expr(), X)))
            expected = 1
            if m % n == 0:
                factorization = sp.factorint(m // n)
                if len(factorization) == 1:
                    prime = next(iter(factorization))
                    expected = prime ** int(sp.totient(n))
            require(r == expected,
                    f"Phi_{m} vs Phi_{n}: {r} != {expected}",
                    "pair_resultants")

    assert counts == {
        "discriminants": 28,
        "disc_resultant": 28,
        "pair_resultants": 406,
        "modular_gcd": 140,
    }, counts
    total = sum(counts.values())
    assert total == 602
    print(f"AA-X04 cyclotomic cross-audit: {total}/{total} PASS; {counts}")


if __name__ == "__main__":
    main()
