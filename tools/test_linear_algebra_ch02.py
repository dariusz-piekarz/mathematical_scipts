"""LA-02: exact finite-field regression for quotient/direct-sum identities."""
from itertools import combinations, product


def plus(x, y, p):
    return tuple((a + b) % p for a, b in zip(x, y))


def span(gens, p, n):
    v = {tuple([0] * n)}
    for g in gens:
        v = {plus(a, tuple((c * x) % p for x in g), p)
             for a in v for c in range(p)}
    return frozenset(v)


def subspaces(p, n):
    nonzero = list(product(range(p), repeat=n))[1:]
    return set(span(gen, p, n)
               for size in range(n + 1)
               for gen in combinations(nonzero, size))


def dim(U, p):
    d = 0
    while p ** d < len(U):
        d += 1
    assert p ** d == len(U)
    return d


def coset(v, U, p):
    return frozenset(plus(v, x, p) for x in U)


def verify(p, n, expected):
    spaces = subspaces(p, n)
    assert len(spaces) == expected, (p, n, len(spaces))
    all_vec = frozenset(product(range(p), repeat=n))
    zero = tuple([0] * n)
    checks = 0
    for U in spaces:
        assert zero in U
        # Greedy construction of an independent spanning family.
        basis = []
        for u in sorted(U):
            if u not in span(basis, p, n):
                basis.append(u)
        assert len(basis) == dim(U, p) and span(basis, p, n) == U
        cosets = {coset(v, U, p) for v in all_vec}
        assert len(cosets) == p ** (n - dim(U, p))
        assert set().union(*cosets) == set(all_vec)
        assert all(a == b or a.isdisjoint(b) for a in cosets for b in cosets)
        checks += 1

    for U in spaces:
        for W in spaces:
            intersection = U & W
            total = frozenset(plus(u, w, p) for u in U for w in W)
            assert intersection in spaces and total in spaces
            assert dim(total, p) + dim(intersection, p) == dim(U, p) + dim(W, p)
            # The sum map U x W -> U + W has |U intersect W| preimages.
            multiplicity = {}
            for u in U:
                for w in W:
                    z = plus(u, w, p)
                    multiplicity[z] = multiplicity.get(z, 0) + 1
            assert set(multiplicity) == set(total)
            assert set(multiplicity.values()) == {len(intersection)}
            assert (set(multiplicity.values()) == {1}) == (intersection == frozenset({zero}))
            # Well-defined bijection U/(U intersect W) -> (U+W)/W.
            f = {}
            for u in U:
                source, dest = coset(u, intersection, p), coset(u, W, p)
                if source in f:
                    assert f[source] == dest
                else:
                    f[source] = dest
            assert len(f) == len(set(f.values()))
            assert set(f.values()) == {coset(z, W, p) for z in total}
            checks += 1
    return len(spaces), checks


if __name__ == "__main__":
    a, x = verify(2, 4, 67)
    b, y = verify(3, 3, 28)
    print(f"PASS: {a} + {b} subspaces, {x+y} exact tests")
