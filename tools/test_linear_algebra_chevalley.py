"""LA18 regression: generalized spectral projectors and Jordan--Chevalley.

All 2x2 matrices over F2,F3 and all 3x3 matrices over F2 are tested;
3x3 matrices over F3 are sampled reproducibly. Nonsplit minimal
polynomials are skipped because this chapter assumes splitting over K.
No third-party dependencies.
"""
from itertools import product
from random import Random
from math import exp, factorial


def identity(n, p):
    return tuple(int(i == j) % p for i in range(n) for j in range(n))


def zero(n):
    return (0,) * (n*n)


def mul(a, b, p, n):
    return tuple(sum(a[n*i+k] * b[n*k+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def add(a, b, p):
    return tuple((x+y) % p for x, y in zip(a, b))


def scaled(a, c, p):
    return tuple(c*x % p for x in a)


def power(a, k, p, n):
    out = identity(n, p)
    for _ in range(k):
        out = mul(out, a, p, n)
    return out


def eval_poly(coeffs, a, p, n):
    out = zero(n)
    x = identity(n, p)
    for coefficient in coeffs:
        out = add(out, scaled(x, coefficient, p), p)
        x = mul(x, a, p, n)
    return out


def minpoly(a, p, n):
    for deg in range(n+1):
        for coeffs in product(range(p), repeat=deg):
            candidate = (*coeffs, 1)
            if eval_poly(candidate, a, p, n) == zero(n):
                return candidate
    raise AssertionError("Minimal polynomial not found")


def factors_linear(poly, p):
    remainder = list(poly)
    factors = {}
    for lam in range(p):
        while len(remainder) > 1 and (
            sum(x * pow(lam, i, p) for i, x in enumerate(remainder)) % p == 0
        ):
            quotient = [0] * (len(remainder)-1)
            quotient[-1] = remainder[-1]
            for i in range(len(quotient)-2, -1, -1):
                quotient[i] = (remainder[i+1] + lam * quotient[i+1]) % p
            assert (remainder[0]+lam*quotient[0]) % p == 0
            factors[lam] = factors.get(lam, 0) + 1
            remainder = quotient
    if len(remainder) != 1:
        return None
    return factors


def taylor_coeff(poly, lam, j, p):
    # Coefficient of u**j in p(lam+u), valid also in char p.
    from math import comb
    return sum(poly[k] * comb(k, j) * pow(lam, k-j, p)
               for k in range(j, len(poly))) % p


def spectral_polynomials(factors, p):
    degree = sum(factors.values())
    result = {}
    for lam, multiplicity in factors.items():
        for q in product(range(p), repeat=degree):
            if all(
                taylor_coeff(q, nu, j, p) ==
                int(nu == lam and j == 0)
                for nu, a in factors.items() for j in range(a)
            ):
                result[lam] = q
                break
        assert lam in result, (factors, lam)
    return result


def check_case(a, p, n):
    minimal = minpoly(a, p, n)
    factors = factors_linear(minimal, p)
    if factors is None:
        return False
    polynomials = spectral_polynomials(factors, p)
    projectors = {lam: eval_poly(q, a, p, n)
                  for lam, q in polynomials.items()}
    total = zero(n)
    for lam, projector in projectors.items():
        assert mul(projector, projector, p, n) == projector
        assert mul(a, projector, p, n) == mul(projector, a, p, n)
        total = add(total, projector, p)
        for other, other_proj in projectors.items():
            if other != lam:
                assert mul(projector, other_proj, p, n) == zero(n)
    assert total == identity(n, p)
    semisimple = zero(n)
    for lam, projector in projectors.items():
        semisimple = add(semisimple, scaled(projector, lam, p), p)
    nilpotent = add(a, scaled(semisimple, -1, p), p)
    assert add(semisimple, nilpotent, p) == a
    assert mul(semisimple, nilpotent, p, n) == mul(nilpotent, semisimple, p, n)
    assert power(nilpotent, n, p, n) == zero(n)
    # Over Fp an endomorphism is diagonalizable with eigenvalues in
    # Fp if and only if S^p = S (since t^p-t has distinct roots).
    assert power(semisimple, p, p, n) == semisimple

    for polynomial in ((1, 2, 1), (0, 1), (2, 0, 1, 1), (1,)):
        direct = eval_poly(polynomial, a, p, n)
        via_projectors = zero(n)
        for lam, a_lam in factors.items():
            for j in range(a_lam):
                term = mul(power(nilpotent, j, p, n), projectors[lam], p, n)
                via_projectors = add(via_projectors, scaled(
                    term, taylor_coeff(polynomial, lam, j, p), p), p)
        assert direct == via_projectors, (p, n, a, polynomial)

    for k in range(5):
        direct = power(a, k, p, n)
        reconstructed = zero(n)
        from math import comb
        for lam, order in factors.items():
            for j in range(min(k, order-1)+1):
                coeff = comb(k, j) * pow(lam, k-j, p) % p
                term = mul(power(nilpotent, j, p, n), projectors[lam], p, n)
                reconstructed = add(reconstructed, scaled(term, coeff, p), p)
        assert direct == reconstructed, (p, n, a, k)

    if 0 not in factors:
        inverse = zero(n)
        for lam, order in factors.items():
            for j in range(order):
                coef = (-1)**j * pow(lam, -j-1, p) % p
                term = mul(power(nilpotent, j, p, n), projectors[lam], p, n)
                inverse = add(inverse, scaled(term, coef, p), p)
        assert mul(inverse, a, p, n) == identity(n, p)
        assert mul(a, inverse, p, n) == identity(n, p)
    return True


def check_exponential():
    t = 0.37
    a = ((2, 1, 0), (0, 2, 1), (0, 0, 2))
    expected = ((1, t, t*t/2), (0, 1, t), (0, 0, 1))
    expected = [[exp(2*t)*v for v in row] for row in expected]
    result = [[0.0]*3 for _ in range(3)]
    term = [[int(i == j) for j in range(3)] for i in range(3)]
    for k in range(70):
        if k:
            term = [[sum(term[i][h]*a[h][j] for h in range(3))*t/k
                     for j in range(3)] for i in range(3)]
        result = [[result[i][j]+term[i][j] for j in range(3)]
                  for i in range(3)]
    assert max(abs(result[i][j]-expected[i][j])
               for i in range(3) for j in range(3)) < 1e-12


def run():
    rng = Random(18018)
    stats = []
    for p, n, cases in (
        (2, 2, list(product(range(2), repeat=4))),
        (3, 2, list(product(range(3), repeat=4))),
        (2, 3, list(product(range(2), repeat=9))),
        (3, 3, [tuple(rng.randrange(3) for _ in range(9))
                for _ in range(400)]),
    ):
        split = sum(check_case(a, p, n) for a in cases)
        stats.append((p, n, len(cases), split))
    check_exponential()
    print("LA18 Jordan--Chevalley/functional calculus OK:", stats,
          "and analytic exponential.")


if __name__ == "__main__":
    run()
