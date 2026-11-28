"""Exact regressions for arbitrary integral flows, not just optimal unit flows."""
from itertools import product, combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "chapters/pl/graph_and_knot_theory"


def balance(n, arcs, f):
    b = [0] * n
    for (u, v), x in zip(arcs, f):
        b[u] += x
        b[v] -= x
    return b


def path(n, arcs, f, u, t, seen):
    if u == t:
        return []
    for i, (a, v) in enumerate(arcs):
        if a == u and f[i] and v not in seen:
            p = path(n, arcs, f, v, t, seen | {v})
            if p is not None:
                return [i] + p
    return None


def decompose(n, arcs, original):
    f = list(original)
    k = balance(n, arcs, f)[0]
    assert k >= 0
    r = k
    paths = []
    while r:
        p = path(n, arcs, f, 0, n - 1, {0})
        assert p
        q = min(r, min(f[i] for i in p))
        for i in p:
            f[i] -= q
        paths.append((p, q))
        r -= q
        assert balance(n, arcs, f) == [r] + [0]*(n-2) + [-r]
        assert len(paths) <= len(arcs) + 1
    assert balance(n, arcs, f) == [0]*n
    cycles = []
    while any(f):
        i = next(i for i, x in enumerate(f) if x)
        u, v = arcs[i]
        p = path(n, arcs, f, v, u, {v})
        assert p
        c = [i] + p
        q = min(f[j] for j in c)
        for j in c:
            f[j] -= q
        cycles.append((c, q))
        assert balance(n, arcs, f) == [0]*n
        assert len(cycles) <= len(arcs)
    reconstructed = [0]*len(arcs)
    for p, q in paths + cycles:
        for i in p:
            reconstructed[i] += q
    assert reconstructed == list(original)
    assert sum(q for p, q in paths) == k


def test_flows():
    count = 0
    for n in (2, 3):
        arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
        for f in product(range(4), repeat=len(arcs)):
            b = balance(n, arcs, f)
            if b[0] >= 0 and not any(b[1:-1]):
                decompose(n, arcs, f)
                count += 1
    # Old subtraction rule overshoots when both terminal arcs carry flow.
    assert min([2]) > balance(2, [(0,1),(1,0)], [2,1])[0]
    decompose(2, [(0,1),(1,0)], [2,1])
    print(f"PASS: {count} arbitrary integral flows including terminal circulations")


def subsets(n):
    return [{i for i in range(n) if m >> i & 1} for m in range(1 << n)]


def test_matching_cuts():
    count = 0
    for a in range(4):
        for b in range(4):
            pool = list(product(range(a), range(b)))
            for mask in range(1 << len(pool)):
                edges = [e for i, e in enumerate(pool) if mask >> i & 1]
                nu = max((len(M) for size in range(min(a,b)+1)
                          for M in combinations(edges,size)
                          if len({u for u,v in M}) == len({v for u,v in M}) == size))
                tau = min(len(S)+len(T) for S in subsets(a) for T in subsets(b)
                          if all(u in S or v in T for u,v in edges))
                delta = max(len(S)-len({v for u,v in edges if u in S})
                            for S in subsets(a))
                # Unit terminal arcs and high capacity a+1 on middle arcs.
                cut = min(a-len(S)+len(T)+(a+1)*sum(u in S and v not in T for u,v in edges)
                          for S in subsets(a) for T in subsets(b))
                assert nu == tau == a-delta == cut
                count += 1
    print(f"PASS: {count} bipartite graphs, matching/cover/Hall/mincut identities")


if __name__ == "__main__":
    test_flows()
    test_matching_cuts()
    source = next(CH.glob("40-*.tex")).read_text(encoding="utf-8")
    assert r"q=\min\{r,\min_{a\in P}f(a)\}" in source
    assert "albo kończy tę fazę" in source
    assert "Cyrkulacja przechodząca przez źródło i ujście" in source
