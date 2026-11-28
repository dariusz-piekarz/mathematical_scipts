#!/usr/bin/env python3
"""Exact finite-model audit for G(n,p), graph thresholds and Ramsey first moment.

Independently enumerates all labelled simple graphs for n<=6.
Probability sums use fractions.Fraction: no Monte Carlo or floating-point
tolerances and no third-party libraries.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, factorial, floor, log, sqrt
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/42-grafy-losowe-i-metoda-probabilistyczna.tex"


def all_pairs(n):
    return tuple(combinations(range(n), 2))


def graph_statistics(n, mask, edges, triples):
    """Independent labelled graph observer; returns m, triangles, isolates, connected."""
    m = mask.bit_count()
    degrees = [0] * n
    adj = [set() for _ in range(n)]
    selected = set()
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            degrees[u] += 1
            degrees[v] += 1
            adj[u].add(v)
            adj[v].add(u)
            selected.add((u, v))
    triangles = sum(all(tuple(sorted(e)) in selected
                        for e in combinations(tri, 2))
                    for tri in triples)
    isolates = sum(d == 0 for d in degrees)
    reached = set()
    if n:
        reached.add(0)
        stack = [0]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in reached:
                    reached.add(v)
                    stack.append(v)
    connected = n >= 1 and len(reached) == n
    return m, triangles, isolates, connected


def connectivity_recurrence(n, p):
    """Independent exact component-of-vertex-0 decomposition."""
    q = 1 - p
    connected = [Fraction(0) for _ in range(n + 1)]
    if n >= 1:
        connected[1] = Fraction(1)
    for k in range(2, n + 1):
        excluded = sum(
            (comb(k - 1, j - 1) * connected[j] * q ** (j * (k - j))
             for j in range(1, k)),
            start=Fraction(0)
        )
        connected[k] = 1 - excluded
    return connected[n] if n else Fraction(0)


def moments_of_graph(n, p):
    """Exact moments: enumerate every graph once, weighting by p^m(1-p)^(N-m)."""
    edges = all_pairs(n)
    triples = tuple(combinations(range(n), 3))
    N = len(edges)
    mu_e = Fraction(0)
    second_e = Fraction(0)
    mu_tri = Fraction(0)
    second_tri = Fraction(0)
    mu_iso = Fraction(0)
    second_iso = Fraction(0)
    probability_conn = Fraction(0)
    probability_tri = Fraction(0)
    probability_iso = Fraction(0)
    total = Fraction(0)
    for mask in range(1 << N):
        m, triangles, isolates, connected = graph_statistics(n, mask, edges, triples)
        probability = p ** m * (1-p) ** (N-m)
        total += probability
        mu_e += probability * m
        second_e += probability * m * m
        mu_tri += probability * triangles
        second_tri += probability * triangles * triangles
        mu_iso += probability * isolates
        second_iso += probability * isolates * isolates
        if connected:
            probability_conn += probability
        if triangles:
            probability_tri += probability
        if isolates:
            probability_iso += probability

    assert total == 1, (n, p, total)
    expected_edges = comb(n, 2) * p
    expected_triangle = comb(n, 3) * p**3
    expected_isolates = n * (1-p)**(n-1) if n >= 1 else 0

    assert mu_e == expected_edges, (n,p,"edge expectation")
    assert second_e - mu_e**2 == comb(n,2)*p*(1-p), (n,p,"edge variance")

    variance_tri = (
        comb(n,3)*p**3*(1-p**3) +
        2*comb(n,2)*comb(n-2,2)*p**5*(1-p)
        if n >= 3 else Fraction(0)
    )
    assert mu_tri == expected_triangle, (n,p,"triangle expectation")
    assert second_tri - mu_tri**2 == variance_tri, (n,p,"triangle variance")

    if n >= 2:
        q = (1-p)**(n-1)
        variance_isolates = (
            n*q*(1-q)+n*(n-1)*p*(1-p)**(2*n-3)
        )
    else:
        variance_isolates = 0
    assert mu_iso == expected_isolates, (n,p,"isolates expectation")
    assert second_iso - mu_iso**2 == variance_isolates, (n,p,"isolates variance")
    assert probability_conn == connectivity_recurrence(n,p), (
        n,p,"connectivity recurrence",probability_conn
    )
    # First- and second-moment inequalities are independently checked.
    assert probability_tri <= expected_triangle, (n,p,"first moment bound")
    if expected_triangle > 0:
        assert 1-probability_tri <= variance_tri/expected_triangle**2, (
            n,p,"triangle second moment"
        )
    if expected_isolates > 0:
        assert 1-probability_iso <= variance_isolates/expected_isolates**2, (
            n,p,"isolate second moment"
        )
    if n > 1 and probability_conn:
        assert probability_conn <= 1-probability_iso
    return 1 << N


def test_exhaustive():
    count = 0
    for n in range(7):
        # With 2^15 labelled graphs for n=6, p=1/2 keeps exact sums light;
        # smaller n cover p=0,1/3,1/2,2/3,1 and degenerate cases.
        parameters = (Fraction(1,2),) if n == 6 else (
            Fraction(0),Fraction(1,3),Fraction(1,2),
            Fraction(2,3),Fraction(1)
        )
        for p in parameters:
            count += moments_of_graph(n,p)
    return count


def test_ramsey_first_moment():
    checked = 0
    # In K_n, color all edges independently red/blue and enumerate all
    # colorings to verify the expected monochromatic K_k count.
    for n in range(2, 7):
        pairs = all_pairs(n)
        N = len(pairs)
        for k in range(2, min(n,4)+1):
            subsets = list(combinations(range(n),k))
            mono_count = 0
            for mask in range(1<<N):
                red = {e for i,e in enumerate(pairs) if mask>>i & 1}
                for S in subsets:
                    clique_edges = tuple(combinations(S,2))
                    c = sum(e in red for e in clique_edges)
                    mono_count += c == 0 or c == len(clique_edges)
            actual = Fraction(mono_count,1<<N)
            expected = Fraction(comb(n,k),2**(comb(k,2)-1))
            assert actual == expected, (n,k,actual,expected)
            checked += 1
    for k in range(3,27):
        n = floor(2**((k-1)/2))
        expected = Fraction(comb(n,k),2**(comb(k,2)-1)) if n>=k else 0
        assert expected < 1
        assert n**k * 2 <= factorial(k) * (2**comb(k,2))
        checked += 1
    return checked


def test_finite_examples():
    assert comb(4,2)*Fraction(1,2) == 3
    assert comb(4,2)*Fraction(1,2)*Fraction(1,2) == Fraction(3,2)
    assert connectivity_recurrence(3,Fraction(1,2)) == Fraction(1,2)
    assert connectivity_recurrence(1,Fraction(0)) == 1
    # Finite threshold sanity checks: no heuristic claimed as exact proof.
    for n in (1000,10000,100000):
        a = sqrt(log(n))
        pminus = (log(n)-a)/n
        pplus = (log(n)+a)/n
        assert 0 < pminus < pplus < 1
        expected_minus = n*(1-pminus)**(n-1)
        expected_plus = n*(1-pplus)**(n-1)
        assert expected_minus > expected_plus


def test_fixed_edge_model():
    # TG42-GNM-01: exact conditional laws and joint edge inclusion.
    count = 0
    for n in range(2, 6):
        N = comb(n, 2)
        for m in range(N+1):
            graphs = [mask for mask in range(1 << N) if mask.bit_count() == m]
            assert len(graphs) == comb(N, m)
            for h in range(N+1):
                F = (1 << h)-1
                actual = Fraction(sum(mask & F == F for mask in graphs), len(graphs))
                expected = Fraction(comb(N-h, m-h), comb(N, m)) if h <= m else 0
                assert actual == expected
                count += 1
            for p in (Fraction(1,3), Fraction(2,3)):
                weights = [p**mask.bit_count()*(1-p)**(N-mask.bit_count())
                           for mask in graphs]
                total = sum(weights)
                assert all(w/total == Fraction(1,len(graphs)) for w in weights)
    return count


def test_fixed_subgraph_moments():
    # TG42-H-01: independent enumeration of labelled embeddings and their overlaps.
    from itertools import permutations
    cases = 0
    for v, H in [(3, [(0,1),(1,2)]), (3, [(0,1),(0,2),(1,2)]),
                 (4, [(0,1),(0,2),(1,2),(2,3)]), (4, [(0,1),(2,3)])]:
        n = 5
        pairs = all_pairs(n)
        bit = {e: 1 << i for i,e in enumerate(pairs)}
        embeddings = [sum(bit[tuple(sorted((phi[u],phi[w])))] for u,w in H)
                      for phi in permutations(range(n),v)]
        rho = max(Fraction(sum(u in S and w in S for u,w in H),len(S))
                  for j in range(1,v+1) for S in combinations(range(v),j))
        for p in (Fraction(1,3), Fraction(1,2), Fraction(2,3)):
            mean = second = Fraction(0)
            for mask in range(1 << len(pairs)):
                k = sum(mask & E == E for E in embeddings)
                weight = p**mask.bit_count() * (1-p)**(len(pairs)-mask.bit_count())
                mean += weight*k
                second += weight*k*k
            assert mean == len(embeddings)*p**len(H)
            overlap_second = sum((p**((E|F).bit_count())
                                  for E in embeddings for F in embeddings), Fraction(0))
            assert second == overlap_second
            assert rho >= Fraction(len(H),v)
            cases += 1
    return cases


def test_monotone_coupling():
    # TG42-COUP-01: enumerate joint edge states with exact probabilities.
    from itertools import product
    cases = 0
    for n in range(1, 5):
        edges = all_pairs(n)
        triples = tuple(combinations(range(n), 3))
        N = len(edges)
        stats = [graph_statistics(n, mask, edges, triples)
                 for mask in range(1 << N)]
        for p, q in [(Fraction(0), Fraction(1)), (Fraction(1,3), Fraction(2,3)),
                     (Fraction(1,2), Fraction(1,2)), (Fraction(0), Fraction(1,2)),
                     (Fraction(1,2), Fraction(1))]:
            marginal_p = [Fraction(0)] * (1 << N)
            marginal_q = [Fraction(0)] * (1 << N)
            weights = (1-q, q-p, p)
            for states in product(range(3), repeat=N):
                lo = sum(1 << i for i, state in enumerate(states) if state == 2)
                hi = sum(1 << i for i, state in enumerate(states) if state >= 1)
                weight = Fraction(1)
                for state in states:
                    weight *= weights[state]
                assert lo & hi == lo
                assert stats[lo][1] <= stats[hi][1]
                assert stats[lo][3] <= stats[hi][3]
                marginal_p[lo] += weight
                marginal_q[hi] += weight
                cases += 1
            for mask in range(1 << N):
                m = mask.bit_count()
                assert marginal_p[mask] == p**m * (1-p)**(N-m)
                assert marginal_q[mask] == q**m * (1-q)**(N-m)
            assert sum(marginal_p) == sum(marginal_q) == 1
    return cases


def test_integrity():
    cat = json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in cat["books"] if b["id"]=="graph_and_knot_theory")
    includes = re.findall(
        r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
        (ROOT/book["entrypoint"]).read_text(encoding="utf-8")
    )
    assert includes == book["chapters"]
    assert len(includes) == 42 and includes[11] == CHAPTER
    assert all((ROOT/path).is_file() for path in includes)
    s = (ROOT/CHAPTER).read_text(encoding="utf-8")
    labels = re.findall(r"\\label\{([^}]+)\}",s)
    assert len(labels)==len(set(labels))
    for label in (
        "ch:tg-random-graphs", "def:tg-random-gnp",
        "prop:tg-random-triangle-moments",
        "thm:tg-random-triangle-threshold",
        "thm:tg-random-connectivity",
        "thm:tg-random-ramsey-bound",
        "fig:tg-random-realization"
    ):
        assert label in labels
    for env in ("definicja","twierdzenie","stwierdzenie","lemat","wniosek",
                "uwaga","przyklad","proof","figure","tikzpicture","itemize"):
        assert s.count(r"\begin{"+env+"}") == s.count(r"\end{"+env+"}"),env


if __name__ == "__main__":
    test_integrity()
    print("PASS exact weighted enumeration G(n,p) and triangle/isolate/edge moments:",test_exhaustive())
    print("PASS exact monochromatic Ramsey first moments:",test_ramsey_first_moment())
    print("PASS TG42-GNM-01 fixed edge inclusion and conditional laws:", test_fixed_edge_model())
    print("PASS TG42-H-01 fixed subgraph embedding moment cases:", test_fixed_subgraph_moments())
    print("PASS TG42-COUP-01 exact monotone joint edge states:", test_monotone_coupling())
    test_finite_examples()
    print("PASS exact connectivity recurrence, threshold sanity and 43-source integration")
