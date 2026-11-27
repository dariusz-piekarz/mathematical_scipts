#!/usr/bin/env python3
"""Audit 31: independent exact verification of source chapters 40--42.

Checks unit-arc path packing against all source cuts (including zero-capacity
arcs in the original graph), extremal clique bounds against all graphs up to
five vertices, and exact moments of small G(n,p) sample spaces.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from random import Random

RNG = Random(20261123031)


def all_directed_arcs(n):
    return [(u, v) for u in range(n) for v in range(n) if u != v]


def simple_path_masks(n, arcs, s=0, t=None):
    if t is None:
        t = n - 1
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(arcs):
        adj[u].append((v, i))
    result = []

    def visit(u, seen, used):
        if u == t:
            result.append(used)
            return
        for v, j in adj[u]:
            if not (seen >> v) & 1:
                visit(v, seen | (1 << v), used | (1 << j))

    visit(s, 1 << s, 0)
    return result


def packing_number(masks):
    @lru_cache(None)
    def search(i, taken):
        if i == len(masks):
            return 0
        best = search(i + 1, taken)
        if masks[i] & taken == 0:
            best = max(best, 1 + search(i + 1, taken | masks[i]))
        return best

    return search(0, 0)


def cut_number(n, arcs, s=0, t=None):
    if t is None:
        t = n - 1
    return min(
        sum((u in side and v not in side) for u, v in arcs)
        for mask in range(1 << (n - 2))
        for side in [set([s]) | {v for i, v in enumerate(range(1, n - 1)) if mask >> i & 1}]
    )


def graph_edges(n):
    return list(combinations(range(n), 2))


def is_clique(edges, vertices):
    return all((u, v) in edges for u, v in combinations(vertices, 2))


def independence_number(n, edges):
    return max((len(S) for k in range(n + 1) for S in combinations(range(n), k)
                if all((u, v) not in edges for u, v in combinations(S, 2))), default=0)


def turan_edges(n, r):
    a, b = divmod(n, r)
    sizes = [a + (j < b) for j in range(r)]
    return (n * n - sum(x * x for x in sizes)) // 2


def verify_packing():
    checked = 0
    # All positive-arc subgraphs on <=4 vertices, not using a max-flow solver.
    for n in range(2, 5):
        pool = all_directed_arcs(n)
        for mask in range(1 << len(pool)):
            positive = [a for i, a in enumerate(pool) if mask >> i & 1]
            assert packing_number(simple_path_masks(n, positive)) == cut_number(n, positive)
            checked += 1
    for _ in range(400):
        n = 5
        pool = all_directed_arcs(n)
        positive = [a for a in pool if RNG.randrange(3) == 0]
        assert packing_number(simple_path_masks(n, positive)) == cut_number(n, positive)
        checked += 1
    # Counterexample to the old statement if zero-capacity arcs are counted.
    original = [(0, 1)]
    capacities = [0]
    positive = [a for a, c in zip(original, capacities) if c > 0]
    assert packing_number(simple_path_masks(2, original)) == 1
    assert packing_number(simple_path_masks(2, positive)) == cut_number(2, positive) == 0
    print(f"PASS chapter 40: {checked} exact path-pack/cut identities + zero-capacity counterexample")


def verify_extremal():
    checked = 0
    for n in range(1, 6):
        pool = graph_edges(n)
        max_without = {r: 0 for r in range(1, n + 2)}
        for mask in range(1 << len(pool)):
            edges = {a for i, a in enumerate(pool) if mask >> i & 1}
            alpha = independence_number(n, edges)
            degrees = [sum(v in edge for edge in edges) for v in range(n)]
            caro = sum((Fraction(1, d + 1) for d in degrees), Fraction(0))
            assert alpha >= caro >= Fraction(n * n, n + 2 * len(edges))
            for r in max_without:
                if not any(is_clique(edges, S) for S in combinations(range(n), r + 1)):
                    max_without[r] = max(max_without[r], len(edges))
            checked += 1
        for r, observed in max_without.items():
            assert observed == turan_edges(n, r), (n, r, observed)
    # Caro--Wei equality on a disjoint union K2 union K3.
    edges = {(0, 1), (2, 3), (2, 4), (3, 4)}
    degrees = [sum(v in e for e in edges) for v in range(5)]
    assert independence_number(5, edges) == sum(Fraction(1, d + 1) for d in degrees) == 2
    print(f"PASS chapter 41: {checked} exhaustive graphs; Caro--Wei, Turan, and equality cases")


def verify_turan_equality():
    """Check all equality cases, including empty parts, through n=6."""
    checked = 0
    for n in range(7):
        pool = list(combinations(range(n), 2))
        for mask in range(1 << len(pool)):
            adj = [set() for _ in range(n)]
            for i, (u, v) in enumerate(pool):
                if mask >> i & 1:
                    adj[u].add(v)
                    adj[v].add(u)
            omega = max((len(S) for k in range(n + 1)
                         for S in combinations(range(n), k)
                         if all(v in adj[u] for u, v in combinations(S, 2))), default=0)
            for r in range(max(1, omega), n + 2):
                q, s = divmod(n, r)
                bound = (n*n - (r-s)*q*q - s*(q+1)**2)//2
                assert mask.bit_count() <= bound
                if mask.bit_count() != bound:
                    continue
                # Nonadjacency, including equality, must be an equivalence relation.
                parts = {frozenset(set(range(n)) - adj[v]) for v in range(n)}
                assert sum(map(len, parts)) == n
                assert all(not (a & b) for a, b in combinations(parts, 2))
                sizes = sorted([len(a) for a in parts] + [0]*(r-len(parts)))
                assert sizes == [q]*(r-s) + [q+1]*s
                checked += 1
    return checked


def connected(n, edges):
    reached = {0}
    while True:
        fresh = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if fresh == reached:
            return len(reached) == n
        reached = fresh


def verify_random_moments():
    checked = 0
    for n in range(3, 6):
        pool = graph_edges(n)
        m = len(pool)
        for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
            t1 = t2 = y1 = y2 = conn = Fraction(0)
            for mask in range(1 << m):
                edges = {a for i, a in enumerate(pool) if mask >> i & 1}
                weight = p ** len(edges) * (1 - p) ** (m - len(edges))
                triangles = sum(is_clique(edges, S) for S in combinations(range(n), 3))
                isolates = sum(not any(v in a for a in edges) for v in range(n))
                t1 += weight * triangles
                t2 += weight * triangles ** 2
                y1 += weight * isolates
                y2 += weight * isolates ** 2
                conn += weight * connected(n, edges)
                checked += 1
            q = (1 - p) ** (n - 1)
            expected_t = comb(n, 3) * p ** 3
            variance_t = comb(n, 3) * p ** 3 * (1 - p ** 3) + 2 * comb(n, 2) * comb(n - 2, 2) * p ** 5 * (1 - p)
            expected_y = n * q
            variance_y = n * q * (1 - q) + n * (n - 1) * p * (1 - p) ** (2 * n - 3)
            assert t1 == expected_t and t2 - t1 ** 2 == variance_t, (n, p, 'triangles')
            assert y1 == expected_y and y2 - y1 ** 2 == variance_y, (n, p, 'isolates')
            if n == 3:
                assert conn == 3 * p * p - 2 * p ** 3
    print(f"PASS chapter 42: {checked} exact G(n,p) graph probabilities and moment checks")


def verify_source_hypotheses():
    """Guard the precise repaired statement, not merely the numerical fact.

    The unqualified edge-disjoint-path claim is false when the original
    network includes zero-capacity arcs. This guard fails if the TeX source
    accidentally reverts to the erroneous statement, even if path-oracle
    tests continue to pass.
    """
    root = Path(__file__).resolve().parents[2]
    path = root / "chapters/pl/graph_and_knot_theory/40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex"
    chapter = path.read_text(encoding="utf-8")
    label = r"\label{thm:tg-flow-integral-paths}"
    assert chapter.count(label) == 1, "missing or duplicate integral path theorem"
    theorem = chapter.split(label, 1)[1].split(r"\end{twierdzenie}", 1)[0]
    proof = chapter.split(label, 1)[1].split(r"\end{proof}", 1)[0]
    required = (
        r"$k=|f|\geq0$",
        r"niech $D_+$ oznacza podgraf",
        r"o przepustowości $1$",
        r"w $D_+$",
        r"liczbie łuków $D_+$",
    )
    for fragment in required:
        assert fragment in theorem, f"missing key hypothesis: {fragment}"
    assert "Nie można w tym wniosku liczyć dróg" in proof
    assert "przepustowości $0$" in proof
    turan = (root / "chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex").read_text(encoding="utf-8")
    assert turan.count(r"\label{prop:tg-turan-unique}") == 1
    print("PASS chapter 40: repaired TeX hypotheses and conclusion explicitly guarded")


if __name__ == "__main__":
    verify_packing()
    verify_source_hypotheses()
    verify_extremal()
    print("PASS Turan equality cases:", verify_turan_equality())
    verify_random_moments()
    print("PASS audit 31 independent finite tests (not a substitute for mathematical proofs)")
