#!/usr/bin/env python3
"""AA-X04 independent confirming audit: cyclotomic splitting and modular collisions.

Checks use irreducible factors over finite fields and polynomial gcd, not
the exact integer resultant/discriminant calculation of the first AA-X04.
"""
from math import gcd

import sympy as sp

X = sp.Symbol("X")
PRIMES = tuple(map(int, sp.primerange(2, 32)))
PHI = {n: sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
       for n in range(1, 31)}


def main():
    counts = {"divisor_identity": 0, "split_frobenius": 0,
              "modular_collisions": 0}

    def check(condition, context, section):
        assert condition, context
        counts[section] += 1

    for n in range(1, 31):
        result = sp.Poly(1, X, domain=sp.ZZ)
        for d in sp.divisors(n):
            result *= PHI[d]
        check(result == sp.Poly(X**n-1, X),
              f"cyclotomic divisor product n={n}", "divisor_identity")

    for n in range(2, 31):
        for p in PRIMES:
            if gcd(n, p) != 1:
                continue
            order = int(sp.n_order(p, n))
            factors = sp.factor_list(sp.Poly(PHI[n].as_expr(), X, modulus=p))[1]
            check(
                all(mult == 1 and q.degree() == order for q, mult in factors)
                and len(factors) * order == int(sp.totient(n)),
                f"cyclotomic factorization n={n}, p={p}",
                "split_frobenius",
            )

    for m in range(3, 31):
        for n in range(2, m):
            ratio_factors = sp.factorint(m//n) if m % n == 0 else {}
            # Positive-degree gcd precisely when p divides the integral
            # resultant of Phi_m and Phi_n.
            for p in PRIMES:
                predicted = len(ratio_factors) == 1 and p in ratio_factors
                fm = sp.Poly(PHI[m].as_expr(), X, modulus=p)
                fn = sp.Poly(PHI[n].as_expr(), X, modulus=p)
                observed = fm.gcd(fn).degree() > 0
                check(observed == predicted,
                      f"modular collision m={m}, n={n}, p={p}",
                      "modular_collisions")

    assert counts == {
        "divisor_identity": 30,
        "split_frobenius": 276,
        "modular_collisions": 4466,
    }, counts
    total = sum(counts.values())
    print(f"AA-X04 independent confirmation: {total}/{total} PASS {counts}")


if __name__ == "__main__":
    main()
