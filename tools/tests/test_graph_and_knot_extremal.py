#!/usr/bin/env python3
"""Independent finite verification of Mantel, Turan, Zykov and Ramsey.

Exhaustively enumerates all simple graphs on up to six vertices.
No NetworkX or other nonstandard dependency.
"""
from __future__ import annotations
import itertools
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex"


def pairs(n):
    return list(itertools.combinations(range(n), 2))


def edges_of(n, bitmask):
    return frozenset(edge for index, edge in enumerate(pairs(n))
                     if (bitmask >> index) & 1)


def complete(graph, subset):
    return all(tuple(sorted((u, v))) in graph
               for u, v in itertools.combinations(subset, 2))


def has_clique(n, graph, k):
    if k > n:
        return False
    return any(complete(graph, subset)
               for subset in itertools.combinations(range(n), k))


def turan_graph(n, r):
    assert r >= 1
    return frozenset((u, v) for u, v in pairs(n) if u % r != v % r)


def turan_edge_count(n, r):
    a, q = divmod(n, r)
    return (n * n - q * (a + 1)**2 - (r - q) * a**2) // 2


def color_ramsey(n, red, s, t):
    all_edges = frozenset(pairs(n))
    blue = all_edges.difference(red)
    return has_clique(n, red, s) or has_clique(n, blue, t)


def test_exhaustive_turan():
    total = 0
    for n in range(7):
        e = pairs(n)
        maxima = {r: -1 for r in range(1, 6)}
        witnesses = {r: 0 for r in range(1, 6)}
        for mask in range(1 << len(e)):
            graph = edges_of(n, mask)
            for r in maxima:
                if not has_clique(n, graph, r + 1):
                    if len(graph) > maxima[r]:
                        maxima[r] = len(graph)
                        witnesses[r] = 1
                    elif len(graph) == maxima[r]:
                        witnesses[r] += 1
            # Mantel's bound must apply to each triangle-free graph.
            if not has_clique(n, graph, 3):
                assert len(graph) <= (n*n)//4
            total += 1
        for r in maxima:
            expected = turan_edge_count(n, r)
            tg = turan_graph(n, r)
            assert len(tg) == expected
            assert not has_clique(n, tg, r + 1)
            assert maxima[r] == expected, (n, r, maxima[r], expected)
            assert witnesses[r] >= 1
        assert maxima[2] == n*n//4
    return total


def clone_vertex(n, graph, u, v):
    """Nonadjacent v is replaced by a clone of u."""
    assert u != v and tuple(sorted((u, v))) not in graph
    nu = {x for x in range(n) if tuple(sorted((u, x))) in graph}
    result = {e for e in graph if v not in e}
    result.update(tuple(sorted((v, x))) for x in nu)
    return frozenset(result)


def test_zykov():
    checked = 0
    for n in range(2, 6):
        for mask in range(1 << len(pairs(n))):
            graph = edges_of(n, mask)
            for u in range(n):
                for v in range(n):
                    if u == v or tuple(sorted((u, v))) in graph:
                        continue
                    d_u = sum(u in edge for edge in graph)
                    d_v = sum(v in edge for edge in graph)
                    changed = clone_vertex(n, graph, u, v)
                    assert len(changed) - len(graph) == d_u - d_v
                    for r in (1, 2, 3, 4):
                        if not has_clique(n, graph, r + 1):
                            assert not has_clique(n, changed, r + 1)
                    checked += 1
    return checked


def test_ramsey():
    all5 = frozenset(pairs(5))
    cycle = frozenset(tuple(sorted((i, (i+1) % 5))) for i in range(5))
    assert len(cycle) == 5
    assert not has_clique(5, cycle, 3)
    assert not has_clique(5, all5 - cycle, 3)
    assert not color_ramsey(5, cycle, 3, 3)

    count = 0
    for n in (5, 6):
        misses = 0
        for mask in range(1 << len(pairs(n))):
            red = edges_of(n, mask)
            if not color_ramsey(n, red, 3, 3):
                misses += 1
        if n == 5:
            assert misses > 0
        else:
            assert misses == 0, f"R(3,3) cannot exceed 6: {misses}"
        count += 1 << len(pairs(n))
    # Recurrence bound, symmetry and base cases, independently tabulated.
    bound = {}
    for s in range(1, 9):
        for t in range(1, 9):
            bound[s, t] = math.comb(s+t-2, s-1)
    for s in range(1, 9):
        for t in range(1, 9):
            assert bound[s, t] == bound[t, s]
    assert bound[3, 3] == 6
    for s in range(2, 9):
        for t in range(2, 9):
            assert bound[s, t] == bound[s-1, t] + bound[s, t-1]
    return count


def test_hand_examples():
    assert turan_edge_count(8, 2) == 16
    assert turan_edge_count(10, 3) == 33
    assert turan_edge_count(6, 2) == 9
    assert turan_edge_count(0, 4) == 0
    assert turan_edge_count(3, 10) == 3
    assert has_clique(6, turan_graph(6, 3), 3)
    assert not has_clique(6, turan_graph(6, 3), 4)


def test_integration():
    cat = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in cat["books"] if b["id"] == "graph_and_knot_theory")
    inp = re.findall(r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
                     (ROOT / book["entrypoint"]).read_text(encoding="utf-8"))
    assert book["chapters"] == inp
    assert len(inp) == 44, (len(inp), inp)
    assert inp[10] == CHAPTER
    assert all((ROOT / p).is_file() for p in inp)
    source = (ROOT / CHAPTER).read_text(encoding="utf-8")
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    assert len(labels) == len(set(labels))
    for env in ("definicja", "lemat", "twierdzenie", "stwierdzenie",
                "wniosek", "przyklad", "proof", "figure", "tikzpicture"):
        assert source.count(r"\begin{" + env + "}") == source.count(
            r"\end{" + env + "}"), env
    for label in ("ch:tg-extremal-ramsey", "thm:tg-mantel",
                  "thm:tg-turan", "lem:tg-zykov",
                  "thm:tg-ramsey-finite", "thm:tg-ramsey-33",
                  "thm:tg-ramsey-multicolor", "fig:tg-ramsey-c5"):
        assert label in labels

if __name__ == "__main__":
    test_integration()
    print("PASS all simple graphs n=0..6; Turan/Mantel:", test_exhaustive_turan())
    print("PASS nonedge symmetrization and clique-free preservation:", test_zykov())
    print("PASS red/blue K5 and K6 Ramsey colorings:", test_ramsey())
    test_hand_examples()
    print("PASS exact numeric examples, graph catalog and LaTeX structure")
