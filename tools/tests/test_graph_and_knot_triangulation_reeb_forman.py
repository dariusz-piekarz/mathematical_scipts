#!/usr/bin/env python3
"""Independent finite checks for historical chapters 13--15.

Tests simplicial manifold links, boundary homology over GF(2), dual graphs,
Pachner 1-3 and 2-2 moves, and Forman matchings via two unrelated cycle
criteria. Reeb checks verify numerical Morse/graph identities only.
Finite evidence is NOT a proof of Pachner's or Forman's general theorems.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "chapters/pl/graph_and_knot_theory"


def simplices(facets):
    return frozenset(tuple(sorted(s)) for face in facets
                     for k in range(1, len(face) + 1)
                     for s in combinations(face, k))


def pieces(K, d):
    return sorted(x for x in K if len(x) == d + 1)


def faces_of_torus(m=3):
    assert m >= 3
    v = lambda i, j: (i % m) * m + j % m
    return {tuple(sorted(t)) for i in range(m) for j in range(m)
            for t in [(v(i, j), v(i + 1, j), v(i + 1, j + 1)),
                      (v(i, j), v(i, j + 1), v(i + 1, j + 1))]}


def connected(vertices, edges):
    if not vertices:
        return False
    todo = [next(iter(vertices))]
    visited = set(todo)
    for u in todo:
        for a, b in edges:
            w = b if a == u else a if b == u else None
            if w in vertices and w not in visited:
                visited.add(w)
                todo.append(w)
    return visited == set(vertices)


def surface_link_condition(K):
    if not pieces(K, 2):
        return False
    for (v,) in pieces(K, 0):
        neighbors = {u for e in pieces(K, 1) if v in e for u in e if u != v}
        link_edges = [tuple(x for x in t if x != v)
                      for t in pieces(K, 2) if v in t]
        degrees = Counter(u for e in link_edges for u in e)
        if not neighbors or any(degrees[u] != 2 for u in neighbors):
            return False
        if not connected(neighbors, link_edges):
            return False
    return True


def dual_check(K):
    triangles = pieces(K, 2)
    edge_to_faces = {e: [i for i, t in enumerate(triangles)
                         if set(e) <= set(t)] for e in pieces(K, 1)}
    assert all(len(ids) == 2 for ids in edge_to_faces.values())
    dual = [tuple(ids) for ids in edge_to_faces.values()]
    assert all(sum(i in x for x in dual) == 3 for i in range(len(triangles)))
    assert connected(set(range(len(triangles))), dual)
    assert 3 * len(triangles) == 2 * len(dual)


def rank_gf2(vectors):
    basis = {}
    for value in vectors:
        x = value
        while x:
            p = x.bit_length() - 1
            if p not in basis:
                basis[p] = x
                break
            x ^= basis[p]
    return len(basis)


def betti_gf2(K):
    V, E, F = (pieces(K, d) for d in range(3))
    indices_v = {t[0]: i for i, t in enumerate(V)}
    indices_e = {t: i for i, t in enumerate(E)}
    d1 = [(1 << indices_v[u]) ^ (1 << indices_v[v]) for u, v in E]
    d2 = [sum(1 << indices_e[e] for e in combinations(t, 2)) for t in F]
    for boundary in d2:
        total = 0
        for i, col in enumerate(d1):
            if boundary & (1 << i):
                total ^= col
        assert total == 0, "boundary of boundary must vanish"
    r1, r2 = rank_gf2(d1), rank_gf2(d2)
    return (len(V)-r1, len(E)-r1-r2, len(F)-r2)


def has_directed_cycle(adj):
    marks = {}
    def visit(x):
        if marks.get(x) == 1:
            return True
        if marks.get(x) == 2:
            return False
        marks[x] = 1
        if any(visit(y) for y in adj[x]):
            return True
        marks[x] = 2
        return False
    return any(visit(x) for x in adj if x not in marks)


def hasse_edges(K):
    return [(a, b) for b in K if len(b) >= 2
            for a in combinations(b, len(b)-1)]


def acyclic_via_hasse(K, matching):
    M = set(matching)
    adj = {s: [] for s in K}
    for a, b in hasse_edges(K):
        if (a, b) in M:
            adj[b].append(a)
        else:
            adj[a].append(b)
    return not has_directed_cycle(adj)


def acyclic_via_vpaths(matching):
    """Independent oracle: transitions between matched lower-dimensional cells."""
    by_lower = {a: b for a, b in matching}
    adj = {a: [] for a in by_lower}
    for a, b in matching:
        adj[a] = [other for other in combinations(b, len(a))
                  if other != a and other in by_lower]
    return not has_directed_cycle(adj)


def all_matchings(incidences):
    # Exhaust all disjoint subsets of Hasse incidences, not just maximal ones.
    def search(i, used, chosen):
        if i == len(incidences):
            yield tuple(chosen)
            return
        yield from search(i+1, used, chosen)
        a, b = incidences[i]
        if a not in used and b not in used:
            chosen.append((a, b))
            yield from search(i+1, used | {a, b}, chosen)
            chosen.pop()
    yield from search(0, set(), [])


def check_matching(K, matching, expected_critical=None):
    assert all(a in K and b in K and len(b) == len(a)+1 and
               set(a) <= set(b) for a, b in matching)
    flattened = [x for pair in matching for x in pair]
    assert len(flattened) == len(set(flattened))
    assert acyclic_via_hasse(K, matching) == acyclic_via_vpaths(matching)
    if expected_critical is not None:
        critical = Counter(len(x)-1 for x in K if x not in flattened)
        assert tuple(critical[i] for i in range(3)) == expected_critical
        assert acyclic_via_hasse(K, matching)
        b = betti_gf2(K)
        assert all(expected_critical[i] >= b[i] for i in range(3))
        assert (expected_critical[0] - expected_critical[1] +
                expected_critical[2] == b[0] - b[1] + b[2])


def test_triangulations():
    tetra = {(0,1,2),(0,1,3),(0,2,3),(1,2,3)}
    octa = {tuple(sorted(x)) for x in product((0,1),(2,3),(4,5))}
    examples = [(tetra,(4,6,4),(1,0,1)),
                (octa,(6,12,8),(1,0,1)),
                (faces_of_torus(),(9,27,18),(1,2,1))]
    for facets, expected_f, expected_b in examples:
        K = simplices(facets)
        assert tuple(len(pieces(K, d)) for d in range(3)) == expected_f
        assert surface_link_condition(K)
        dual_check(K)
        assert betti_gf2(K) == expected_b
        assert sum((-1)**d * expected_f[d] for d in range(3)) == (
            expected_b[0]-expected_b[1]+expected_b[2])
    wedge = simplices({(0,1,2),(0,3,4)})
    assert not surface_link_condition(wedge)  # link at 0 disconnected
    disk = simplices({(0,1,2)})
    assert not surface_link_condition(disk)   # boundary links are paths
    # Bistellar 1->3, then a legal 2->2 move using the new vertex 4.
    split = (tetra - {(0,1,2)}) | {(0,1,4),(0,2,4),(1,2,4)}
    flipped = (split - {(0,1,3),(0,1,4)}) | {(0,3,4),(1,3,4)}
    for facets in (split, flipped):
        K = simplices(facets)
        assert surface_link_condition(K)
        dual_check(K)
        assert betti_gf2(K) == (1,0,1)
        assert tuple(len(pieces(K,d)) for d in range(3)) == (5,9,6)
    return len(examples)+2


def test_forman():
    cycle = simplices({(0,1),(1,2),(0,2)})
    disk = simplices({(0,1,2)})
    n = 0
    for K in (cycle, disk):
        for M in all_matchings(hasse_edges(K)):
            check_matching(K, M)
            n += 1
    check_matching(cycle, (((1,),(0,1)),((2,),(1,2))), (1,1,0))
    check_matching(disk, (((1,),(0,1)),((2,),(1,2)),
                          ((0,2),(0,1,2))), (1,0,0))
    tetra = simplices({(0,1,2),(0,1,3),(0,2,3),(1,2,3)})
    check_matching(tetra,
                   (((1,),(0,1)),((2,),(0,2)),((3,),(0,3)),
                    ((1,2),(0,1,2)),((1,3),(0,1,3)),
                    ((2,3),(0,2,3))), (1,0,1))
    return n


def test_reeb_degree_arithmetic():
    # Numerical consequences of c0-c1+c2=2-2g and degrees 1/3.
    checks = 0
    for genus in range(5):
        for c0, c2 in ((1,1),(2,1),(1,3),(3,2)):
            c1 = c0+c2-2+2*genus
            assert c1 >= 0
            vertices = c0+c1+c2
            edges_twice = c0+c2+3*c1
            assert edges_twice % 2 == 0
            assert edges_twice//2 - vertices + 1 == genus
            checks += 1
    return checks


def test_source_integration():
    names = (
        "13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex",
        "14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex",
        "15-dyskretna-teoria-morse-a-formana.tex")
    a, b, c = [(BASE/n).read_text(encoding="utf-8") for n in names]
    for source in (a,b,c):
        assert source.count(r"\begin{proof}") == source.count(r"\end{proof}")
    assert "Każdy skończony graf prosty" in a
    assert r"\label{thm:tg-link-surface}" in a
    assert r"\label{lem:tg-reeb-critical-band}" in b
    assert r"\label{thm:tg-reeb-betti}" in b
    assert r"H_u(t_0,\ldots,t_p,s)" in c
    assert r"\label{thm:tg-forman-ineq}" in c


if __name__ == "__main__":
    test_source_integration()
    print("PASS manifold links, dual incidence, GF(2) homology, bistellar moves:",
          test_triangulations())
    print("PASS independently compared Hasse cycles vs V-paths on all small matchings:",
          test_forman())
    print("PASS Reeb degree/Euler arithmetic checks:", test_reeb_degree_arithmetic())
