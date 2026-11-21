"""Exact Clifford algebra tests, e_i^2 = -1 (no third-party packages)."""
from itertools import product
from random import Random

rng = Random(302026)

def mul(n, mask_a, mask_b):
    assert 0 <= mask_a < 1 << n and 0 <= mask_b < 1 << n
    swaps = sum((mask_a >> i & 1) * sum(mask_b >> j & 1 for j in range(i))
                for i in range(n))
    repeated = (mask_a & mask_b).bit_count()
    return (-1 if (swaps + repeated) & 1 else 1), mask_a ^ mask_b

def apply_generator(n, i, mask):
    smaller = (mask & ((1 << i) - 1)).bit_count()
    if mask & (1 << i):
        return (-1 if (smaller + 1) & 1 else 1), mask ^ (1 << i)
    return (-1 if smaller & 1 else 1), mask | (1 << i)

def apply_monomial(n, mask_word, mask_state):
    sign, result = 1, mask_state
    for i in range(n - 1, -1, -1):
        if mask_word & (1 << i):
            s, result = apply_generator(n, i, result)
            sign *= s
    return sign, result

pairs = 0
triple_checks = 0
representation_checks = 0
for n in range(7):
    # The 2^n normal monomials form a basis, witnessed by c(e_I)1 = e_I.
    for a in range(1 << n):
        assert apply_monomial(n, a, 0) == (1, a)
        for b in range(1 << n):
            x = mul(n, a, b)
            assert apply_monomial(n, a, b) == x
            pairs += 1

    if n <= 4:
        triples = product(range(1 << n), repeat=3)
    else:
        triples = ((rng.randrange(1 << n), rng.randrange(1 << n),
                    rng.randrange(1 << n)) for _ in range(1000))
    for a, b, c in triples:
        s1, ab = mul(n, a, b)
        s2, left = mul(n, ab, c)
        s3, bc = mul(n, b, c)
        s4, right = mul(n, a, bc)
        assert (s1 * s2, left) == (s3 * s4, right)
        triple_checks += 1

    for i in range(n):
        for j in range(n):
            for state in range(1 << n):
                s1, p1 = apply_generator(n, j, state)
                s2, p2 = apply_generator(n, i, p1)
                u1, q1 = apply_generator(n, i, state)
                u2, q2 = apply_generator(n, j, q1)
                found = {}
                found[p2] = found.get(p2, 0) + s1 * s2
                found[q2] = found.get(q2, 0) + u1 * u2
                found = {k: v for k, v in found.items() if v}
                expected = {state: -2} if i == j else {}
                assert found == expected
                representation_checks += 1

# Concrete examples: Cl_1 = C (e^2=-1); Cl_2 = H (i*j=-j*i).
assert mul(1, 1, 1) == (-1, 0)
assert mul(2, 1, 2) == (1, 3)
assert mul(2, 2, 1) == (-1, 3)
assert mul(2, 3, 3) == (-1, 0)

print(f"Clifford product pairs: {pairs} PASS")
print(f"Associativity checks: {triple_checks} PASS")
print(f"Exterior-contraction representation checks: {representation_checks} PASS")
