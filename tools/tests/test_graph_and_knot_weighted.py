#!/usr/bin/env python3
"""Independent finite-model audit of weighted shortest paths and routing methods.

No external packages; deterministic exhaustive small models and seeded cases.
"""
from __future__ import annotations

from collections import deque
from heapq import heappush, heappop
from itertools import combinations, permutations, product
from math import inf
from pathlib import Path
import json
import random
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/38-najkrotsze-drogi-wazone-i-algorytmy-wyszukiwania-tras.tex"

def dijkstra(graph, source):
    distance = {v: inf for v in graph}
    distance[source] = 0
    heap = [(0, source)]
    settled = set()
    while heap:
        d, u = heappop(heap)
        if u in settled or d != distance[u]:
            continue
        settled.add(u)
        for v, w in graph[u].items():
            assert w >= 0
            if d + w < distance[v]:
                distance[v] = d + w
                heappush(heap, (distance[v], v))
    return distance

def reverse_graph(graph):
    rev = {u: {} for u in graph}
    for u in graph:
        for v, weight in graph[u].items():
            rev[v][u] = weight
    return rev

def bellman_ford(graph, source):
    distance = {v: inf for v in graph}
    distance[source] = 0
    arcs = [(u, v, w) for u in graph for v, w in graph[u].items()]
    for _ in range(max(0, len(graph)-1)):
        changed = False
        for u, v, w in arcs:
            if distance[u] != inf and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                changed = True
        if not changed:
            break
    negative_reachable = any(
        distance[u] != inf and distance[u] + w < distance[v]
        for u, v, w in arcs
    )
    return distance, negative_reachable

def floyd_warshall(graph):
    vertices = list(graph)
    d = {u: {v: 0 if u == v else graph[u].get(v, inf) for v in vertices}
         for u in vertices}
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if d[i][k] != inf and d[k][j] != inf:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def a_star(graph, source, goal, heuristic):
    """A* with reopening, required when heuristic is only admissible."""
    g = {v: inf for v in graph}
    g[source] = 0
    heap = [(heuristic[source], 0, source)]
    while heap:
        _, cost, u = heappop(heap)
        if cost != g[u]:
            continue
        if u == goal:
            return cost
        for v, w in graph[u].items():
            assert w >= 0
            candidate = cost + w
            if candidate < g[v]:
                g[v] = candidate
                heappush(heap, (candidate + heuristic[v], candidate, v))
    return inf

def bidirectional_dijkstra(graph, source, target):
    rev = reverse_graph(graph)
    dist_f = {v: inf for v in graph}
    dist_b = {v: inf for v in graph}
    dist_f[source] = 0
    dist_b[target] = 0
    pq_f, pq_b = [(0, source)], [(0, target)]
    seen_f, seen_b = set(), set()
    mu = inf

    def top(heap, seen, dist):
        while heap and (heap[0][1] in seen or heap[0][0] != dist[heap[0][1]]):
            heappop(heap)
        return heap[0][0] if heap else inf

    while True:
        kf = top(pq_f, seen_f, dist_f)
        kb = top(pq_b, seen_b, dist_b)
        if kf == inf or kb == inf or kf + kb >= mu:
            break
        forward = kf <= kb
        heap, seen = (pq_f, seen_f) if forward else (pq_b, seen_b)
        dist, other = (dist_f, dist_b) if forward else (dist_b, dist_f)
        adj = graph if forward else rev
        cost, u = heappop(heap)
        seen.add(u)
        if other[u] != inf:
            mu = min(mu, cost + other[u])
        for v, w in adj[u].items():
            candidate = cost + w
            if candidate < dist[v]:
                dist[v] = candidate
                heappush(heap, (candidate, v))
            if other[v] != inf:
                mu = min(mu, dist[v] + other[v])
    return mu

def contraction_hierarchy_query(graph, rank, source, target):
    """Exact no-witness contraction of UNDIRECTED positive-weight graphs."""
    active = set(graph)
    current = {u: dict(graph[u]) for u in graph}
    augmented = {u: dict(graph[u]) for u in graph}
    for v in sorted(graph, key=lambda u: rank[u]):
        neighbors = sorted(u for u in active if u != v and u in current[v])
        for u, z in combinations(neighbors, 2):
            candidate = current[u][v] + current[v][z]
            if candidate < current[u].get(z, inf):
                current[u][z] = current[z][u] = candidate
                augmented[u][z] = augmented[z][u] = candidate
        active.remove(v)
    upward = {u: {v: w for v, w in augmented[u].items() if rank[u] < rank[v]}
              for u in augmented}
    f = dijkstra(upward, source)
    b = dijkstra(upward, target)
    return min((f[x] + b[x] for x in graph), default=inf)

def test_exhaustive_nonnegative():
    count = 0
    for n in range(1, 4):
        arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
        for values in product((None, 0, 1, 3), repeat=len(arcs)):
            graph = {u: {} for u in range(n)}
            for (u, v), weight in zip(arcs, values):
                if weight is not None:
                    graph[u][v] = weight
            fw = floyd_warshall(graph)
            for s in graph:
                dij = dijkstra(graph, s)
                bf, negative = bellman_ford(graph, s)
                assert not negative
                assert dij == bf == fw[s], (graph, s, dij, bf, fw[s])
                for t in graph:
                    dist_to_t = dijkstra(reverse_graph(graph), t)
                    # Perfect h is consistent. Also test admissible
                    # but possibly inconsistent heuristics separately.
                    h = {v: 0 if dist_to_t[v] == inf else dist_to_t[v] for v in graph}
                    assert a_star(graph, s, t, h) == dij[t]
                    assert a_star(graph, s, t, {v: 0 for v in graph}) == dij[t]
                    assert bidirectional_dijkstra(graph, s, t) == dij[t]
            count += 1
    return count

def test_negative():
    rnd = random.Random(20261123)
    count = 0
    for n in range(2, 7):
        for _ in range(350):
            graph = {u: {} for u in range(n)}
            for u in graph:
                for v in graph:
                    if u != v and rnd.random() < 0.42:
                        graph[u][v] = rnd.randint(-6, 9)
            fw = floyd_warshall(graph)
            for s in graph:
                _, flag = bellman_ford(graph, s)
                reachable_negative = any(
                    fw[k][k] < 0 and fw[s][k] != inf
                    for k in graph
                )
                assert flag == reachable_negative, (n, graph, s)
                if not flag:
                    dist, _ = bellman_ford(graph, s)
                    # Compare only destinations not reachable
                    # from a negative cycle: this is true for all
                    # destinations when no negative cycle is reachable.
                    assert dist == fw[s], (n, graph, s, dist, fw[s])
            count += 1
    return count

def test_astar_reopen():
    rnd = random.Random(41033)
    count = 0
    for n in range(2, 9):
        for _ in range(170):
            graph = {u: {} for u in range(n)}
            for u in graph:
                for v in graph:
                    if u != v and rnd.random() < 0.39:
                        graph[u][v] = rnd.randrange(1, 14)
            for t in graph:
                true_h = dijkstra(reverse_graph(graph), t)
                h = {v: rnd.randrange(true_h[v] + 1)
                     if true_h[v] != inf else 0
                     for v in graph}
                for s in graph:
                    assert a_star(graph, s, t, h) == dijkstra(graph, s)[t]
            count += 1
    # A deliberately inconsistent but admissible heuristic.
    sample = {0: {1: 2, 2: 1}, 1: {3: 1}, 2: {1: 0, 3: 8}, 3: {}}
    h = {0: 2, 1: 0, 2: 1, 3: 0}
    assert h[0] <= 1+h[2] and h[2] > 0+h[1]
    assert a_star(sample, 0, 3, h) == dijkstra(sample, 0)[3] == 2
    # An admissible but inconsistent heuristic forces a reopening:
    # without it, node 1 would be permanently closed at cost 4,
    # although the optimal route 0->2->1->3 has cost 13.
    counterexample = {
        0: {1: 4, 2: 2},
        1: {3: 10},
        2: {1: 1, 3: 30},
        3: {}
    }
    h_reopen = {0: 0, 1: 0, 2: 10, 3: 0}
    assert h_reopen[2] > counterexample[2][1] + h_reopen[1]
    assert a_star(counterexample, 0, 3, h_reopen) == 13
    return count

def test_ch():
    count = 0
    for n in range(1, 5):
        edges = list(combinations(range(n), 2))
        for values in product((None, 1, 4), repeat=len(edges)):
            graph = {u: {} for u in range(n)}
            for (u, v), w in zip(edges, values):
                if w is not None:
                    graph[u][v] = graph[v][u] = w
            true = {s: dijkstra(graph, s) for s in graph}
            for order in permutations(range(n)):
                rank = {v: i for i, v in enumerate(order)}
                for s in graph:
                    for t in graph:
                        actual = contraction_hierarchy_query(graph, rank, s, t)
                        assert actual == true[s][t], (graph, rank, s, t, actual, true[s][t])
            count += 1
    return count

def test_integrity():
    book = next(b for b in json.loads((ROOT / "catalog/books.json").read_text())["books"]
                if b["id"] == "graph_and_knot_theory")
    content = (ROOT / book["entrypoint"]).read_text(encoding="utf-8")
    included = re.findall(r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
                          content)
    assert book["chapters"] == included, (len(book["chapters"]), len(included))
    assert len(included) == 42
    assert included[6].endswith("37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex")
    assert included[7] == CHAPTER
    assert all((ROOT / path).is_file() for path in included)
    source = (ROOT / CHAPTER).read_text(encoding="utf-8")
    assert r"\label{ch:tg-shortest-paths}" in source
    for env in ("twierdzenie", "lemat", "stwierdzenie", "definicja",
                "proof", "przyklad", "uwaga", "figure", "tikzpicture"):
        assert source.count("\\begin{" + env + "}") == source.count("\\end{" + env + "}"), env
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    assert len(labels) == len(set(labels)), "duplicate labels"

if __name__ == "__main__":
    test_integrity()
    print("PASS nonnegative directed exhaustive:", test_exhaustive_nonnegative())
    print("PASS seeded negative weighted directed:", test_negative())
    print("PASS A* admissible possibly inconsistent:", test_astar_reopen())
    print("PASS undirected CH all rank orders:", test_ch())
