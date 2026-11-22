"""Finite-field regression for linear maps, quotients, Hom and projections (LA-03).

Exhausts all F_2^3 -> F_2^3 and F_3^2 -> F_3^2 linear maps.
Uses exact arithmetic without dependencies.
"""
from itertools import combinations, product
from functools import lru_cache


def add(x, y, p):
    return tuple((u + v) % p for u, v in zip(x, y))


def subtract(x, y, p):
    return tuple((u - v) % p for u, v in zip(x, y))


def span(vectors, p, n):
    S = {tuple([0] * n)}
    for vec in vectors:
        S = {add(v, tuple((a * x) % p for x in vec), p)
             for v in S for a in range(p)}
    return frozenset(S)


def subspaces(vecs, p, n):
    return set(span(gens, p, n)
               for k in range(n + 1)
               for gens in combinations(vecs[1:], k))


def dim(space, p):
    result = 0
    while p**result < len(space):
        result += 1
    assert p**result == len(space)
    return result


def coset(x, U, p):
    return frozenset(add(x, u, p) for u in U)


def validate(p, n, expected_maps, expected_projections, expected_subspaces):
    vectors = list(product(range(p), repeat=n))
    zero = tuple([0] * n)
    all_maps = product(vectors, repeat=n)  # images of standard basis
    subsp = subspaces(vectors, p, n)
    assert len(subsp) == expected_subspaces, (p, n, len(subsp))
    all_sets = []
    for mask in range(1 << len(vectors)):
        A = frozenset(vectors[i] for i in range(len(vectors)) if mask & (1 << i))
        all_sets.append((A, span(A, p, n)))

    maps_checked = projections = factorization_checks = span_checks = 0
    for columns in all_maps:
        def T(v):
            return tuple(sum(v[i] * columns[i][j] for i in range(n)) % p
                         for j in range(n))

        values = {v: T(v) for v in vectors}
        image = frozenset(values.values())
        kernel = frozenset(v for v in vectors if values[v] == zero)
        assert len(kernel) * len(image) == len(vectors)
        assert dim(kernel, p) + dim(image, p) == n
        assert image in subsp and kernel in subsp

        # First isomorphism theorem: class -> image is well-defined,
        # injective and onto; the quotient classes partition the domain.
        induced = {}
        for v in vectors:
            c = coset(v, kernel, p)
            if c in induced:
                assert induced[c] == values[v]
            else:
                induced[c] = values[v]
        assert len(induced) == len(image)
        assert frozenset(induced.values()) == image

        # U <= ker(T) iff T factors through V/U.
        for U in subsp:
            compatible = {}
            well_defined = True
            for v in vectors:
                c, y = coset(v, U, p), values[v]
                if c in compatible and compatible[c] != y:
                    well_defined = False
                    break
                compatible[c] = y
            assert well_defined == U.issubset(kernel)
            if well_defined:
                # The factor map preserves both vector-space operations.
                representatives = {coset(v, U, p): v for v in vectors}
                for a, va in representatives.items():
                    for b, vb in representatives.items():
                        assert compatible[coset(add(va, vb, p), U, p)] == add(compatible[a], compatible[b], p)
            factorization_checks += 1

        # Image of a spanned set equals the span of its image.
        for A, span_A in all_sets:
            left = frozenset(values[x] for x in span_A)
            right = span((values[x] for x in A), p, n)
            assert left == right
            span_checks += 1

        # Algebraic projection iff im(T) + ker(T) = V, with trivial
        # intersection, and T acts as identity on its image.
        is_proj = all(values[values[v]] == values[v] for v in vectors)
        total = frozenset(add(x, y, p) for x in image for y in kernel)
        is_direct = (
            total == frozenset(vectors)
            and image & kernel == frozenset({zero})
            and all(values[y] == y for y in image)
        )
        assert is_proj == is_direct
        projections += int(is_proj)
        maps_checked += 1

    assert maps_checked == expected_maps, (maps_checked, expected_maps)
    assert projections == expected_projections, (projections, expected_projections)
    return maps_checked, projections, factorization_checks, span_checks


if __name__ == "__main__":
    a = validate(2, 3, 512, 58, 16)
    b = validate(3, 2, 81, 14, 6)
    print("LA-03 PASS: maps=%s projections=%s quotient-factorizations=%s span-identities=%s" % (
        a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]
    ))
