#!/usr/bin/env python3
"""AA-X05: exact independent modular tests of Smith, splitting and tensor properties.

Pure standard library. Run: python tools/tests/test_abstract_algebra_cross_aa16_18.py
"""
from itertools import product
from math import gcd


def check(value, context, section, tally):
    if not value:
        raise AssertionError(context)
    tally[section] += 1


def smith_2x2(A):
    a, b, c, d = A
    first = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
    det = a*d - b*c
    if first == 0:
        return (0, 0)
    if det == 0:
        return (first, 0)
    assert abs(det) % first == 0
    second = abs(det)//first
    assert second % first == 0
    return (first, second)


def image_size_mod_n(A, n):
    a, b, c, d = A
    return len({((a*x+b*y) % n, (c*x+d*y) % n)
                for x, y in product(range(n), repeat=2)})


def cokernel_size_from_smith(A, n):
    d1, d2 = smith_2x2(A)
    return (gcd(d1, n) if d1 else n)*(gcd(d2, n) if d2 else n)


def main():
    tally = {name: 0 for name in (
        'first_isomorphism', 'splitting', 'tensor_cyclic',
        'tensor_exactness', 'tensor_hom', 'tensor_direct_sum',
        'smith_modular_cokernel', 'smith_invariants',
        'nonflatness', 'nonprojective_cyclic')}

    # The first isomorphism theorem for x |-> k*x on Z/n.
    for n in range(1, 31):
        for k in range(31):
            kernel = sum(1 for x in range(n) if k*x % n == 0)
            image = {k*x % n for x in range(n)}
            check(kernel == gcd(n,k) and kernel*len(image) == n,
                  f'First isomorphism n={n} k={k}',
                  'first_isomorphism', tally)

    # Exact 0 -> Z/a --*b--> Z/(ab) -> Z/b -> 0.
    # A section sends 1 to y with y mod b=1 and b*y mod ab=0.
    for a,b in product(range(1,19), repeat=2):
        N = a*b
        sections = [y for y in range(N) if y%b == 1%b
                    and b*y%N == 0]
        check(bool(sections) == (gcd(a,b) == 1),
              f'Splitting a={a}, b={b}', 'splitting', tally)

    # Z/m tensor_Z Z/n = (Z/n)/m(Z/n).
    for m,n in product(range(1,31), repeat=2):
        multiples = {m*x%n for x in range(n)}
        check(n%len(multiples) == 0 and n//len(multiples) == gcd(m,n),
              f'Tensor cyclic m={m}, n={n}', 'tensor_cyclic', tally)
        check(len(multiples)*gcd(m,n) == n,
              f'Right exactness m={m}, n={n}', 'tensor_exactness', tally)

    # Actual generator counts for the cyclic tensor-Hom adjunction.
    for m,n,k in product(range(1,16), repeat=3):
        d = gcd(m,n)
        left = sum(d*x%k == 0 for x in range(k))
        hom_nk = [x for x in range(k) if n*x%k == 0]
        right = sum(m*x%k == 0 for x in hom_nk)
        check(left == right == gcd(m,n,k),
              f'Tensor-Hom m={m}, n={n}, k={k}', 'tensor_hom', tally)

    for a,b,n in product(range(1,14), repeat=3):
        left = gcd(a,n)*gcd(b,n)
        im_a = {a*x%n for x in range(n)}
        im_b = {b*x%n for x in range(n)}
        right = (n//len(im_a))*(n//len(im_b))
        check(left == right, f'Direct sum a={a}, b={b}, n={n}',
              'tensor_direct_sum', tally)

    # Independently enumerate images mod n for 625 presentation matrices.
    # Compare with Smith determinantal invariants over Z.
    for A in product(range(-2,3), repeat=4):
        d1,d2 = smith_2x2(A)
        det = A[0]*A[3]-A[1]*A[2]
        check((d1 == 0 and det == 0) or (d2 == 0 and det == 0)
              or (d1 > 0 and d2%d1 == 0 and d1*d2 == abs(det)),
              f'Smith invariants A={A}', 'smith_invariants', tally)
        for n in range(2,12):
            image = image_size_mod_n(A,n)
            expected = cokernel_size_from_smith(A,n)
            check(n*n%image == 0 and n*n//image == expected,
                  f'Smith coker A={A}, n={n}, image={image}, expected={expected}',
                  'smith_modular_cokernel', tally)

    # Tensoring the injection *m:Z->Z with Z/m kills it.
    # Also Z/m is not projective over Z for m>1.
    for m in range(2,31):
        image = {m*x%m for x in range(m)}
        check(len(image) == 1, f'Nonflat Z/{m}', 'nonflatness', tally)
        check(all(m*x != 0 for x in range(-m,m+1) if x != 0),
              f'Nonprojective Z/{m}', 'nonprojective_cyclic', tally)

    expected = {
        'first_isomorphism': 930, 'splitting': 324,
        'tensor_cyclic': 900, 'tensor_exactness': 900,
        'tensor_hom': 3375, 'tensor_direct_sum': 2197,
        'smith_modular_cokernel': 6250, 'smith_invariants': 625,
        'nonflatness': 29, 'nonprojective_cyclic': 29}
    assert tally == expected, tally
    n = sum(tally.values())
    assert n == 15559
    print(f'AA-X05 module/Smith/tensor cross-audit: {n}/{n} PASS {tally}')


if __name__ == '__main__':
    main()
