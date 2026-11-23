#!/usr/bin/env python3
"""Independent finite-model verification of Prim, Kruskal, DSU and MST lemmas.

No third-party packages. The optimization oracle enumerates all spanning
forests and verifies component connectivity using ordinary DFS, never DSU.
"""
from __future__ import annotations

import itertools
import json
import random
import re
from heapq import heappush, heappop
from math import inf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/39-minimalne-drzewa-rozpinajace-prim-kruskal-dsu.tex"


def connected_components(n, edges):
    adj = [set() for _ in range(n)]
    for u, v, _ in edges:
        adj[u].add(v)
        adj[v].add(u)
    labels = [-1] * n
    count = 0
    for root in range(n):
        if labels[root] >= 0:
            continue
        labels[root] = count
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if labels[v] == -1:
                    labels[v] = count
                    stack.append(v)
        count += 1
    return labels, count


def spanning(n, original, candidate):
    # Independent connectivity criterion. The edge count n-c implies acyclicity
    # once every original connected component stays connected.
    labels, count = connected_components(n, original)
    if len(candidate) != n - count:
        return False
    if not set(candidate).issubset(set(original)):
        return False
    new_labels, new_count = connected_components(n, candidate)
    if new_count != count:
        return False
    return all((labels[u] == labels[v]) == (new_labels[u] == new_labels[v])
               for u in range(n) for v in range(n))


def exhaustive_oracle(n, edges):
    _, count = connected_components(n, edges)
    best = inf
    optima = []
    for candidate in itertools.combinations(edges, n - count):
        if not spanning(n, edges, candidate):
            continue
        cost = sum(w for _, _, w in candidate)
        if cost < best:
            best = cost
            optima = [frozenset((u, v) for u, v, _ in candidate)]
        elif cost == best:
            optima.append(frozenset((u, v) for u, v, _ in candidate))
    assert optima, (n, edges, "no spanning forest")
    return best, optima


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True


def kruskal(n, edges):
    dsu = DSU(n)
    selected = []
    for u, v, w in sorted(edges, key=lambda edge: (edge[2], edge[0], edge[1])):
        if dsu.union(u, v):
            selected.append((u, v, w))
    return selected


def prim(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    selected = []
    visited = [False] * n
    for root in range(n):
        if visited[root]:
            continue
        visited[root] = True
        heap = []
        for v, w in adj[root]:
            heappush(heap, (w, root, v))
        while heap:
            w, u, v = heappop(heap)
            if visited[v]:
                continue
            visited[v] = True
            selected.append((min(u, v), max(u, v), w))
            for other, weight in adj[v]:
                if not visited[other]:
                    heappush(heap, (weight, v, other))
    return selected


def independent_dsu_invariants(n, edges):
    dsu = DSU(n)
    processed = []
    for u, v, _ in edges:
        dsu.union(u, v)
        processed.append((u, v, 0))
        labels, count = connected_components(n, processed)
        assert len({dsu.find(i) for i in range(n)}) == count
        for a in range(n):
            for b in range(n):
                assert (dsu.find(a) == dsu.find(b)) == (labels[a] == labels[b])
        for root in range(n):
            if dsu.parent[root] == root:
                assert dsu.size[root] == sum(dsu.find(i) == root for i in range(n))


def path_exists(n, selected, source, target):
    adj = [[] for _ in range(n)]
    for u, v, _ in selected:
        adj[u].append(v)
        adj[v].append(u)
    visited = {source}
    queue = [source]
    for v in queue:
        if v == target:
            return True
        for w in adj[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return False


def verify_exchange_lemmas(n, edges, optima):
    all_optimal = set.intersection(*(set(o) for o in optima))
    none_optimal = set((u, v) for u, v, _ in edges) - set.union(
        *(set(o) for o in optima)
    )
    for mask in range(1, (1 << n) - 1):
        crossing = [(u, v, w) for u, v, w in edges
                    if bool(mask & (1 << u)) != bool(mask & (1 << v))]
        if not crossing:
            continue
        smallest = min(w for _, _, w in crossing)
        lightest = [(u, v) for u, v, w in crossing if w == smallest]
        if len(lightest) == 1:
            assert lightest[0] in all_optimal, (n, edges, mask, lightest)
    for u, v, w in edges:
        strictly_lighter = [(x, y, z) for x, y, z in edges if z < w]
        if path_exists(n, strictly_lighter, u, v):
            assert (u, v) in none_optimal, (n, edges, "strict cycle maximum", (u, v))


def verify(n, edges, check_exchange=False):
    best, optima = exhaustive_oracle(n, edges)
    for algorithm in (kruskal, prim):
        actual = algorithm(n, edges)
        assert spanning(n, edges, actual), (algorithm.__name__, n, edges, actual)
        cost = sum(w for _, _, w in actual)
        assert cost == best, (algorithm.__name__, n, edges, cost, best)
        assert frozenset((u, v) for u, v, _ in actual) in optima
    independent_dsu_invariants(n, edges)
    if check_exchange:
        verify_exchange_lemmas(n, edges, optima)
    if len(set(w for _, _, w in edges)) == len(edges):
        assert len(optima) == 1, (n, edges, "nonunique despite distinct weights")
        assert frozenset((u, v) for u, v, _ in kruskal(n, edges)) == optima[0]


def exhaustive_small():
    cases = 0
    weights = (None, -2, 0, 3)
    for n in range(5):
        pairs = list(itertools.combinations(range(n), 2))
        for values in itertools.product(weights, repeat=len(pairs)):
            edges = [(u, v, w) for (u, v), w in zip(pairs, values)
                     if w is not None]
            verify(n, edges, check_exchange=True)
            cases += 1
    return cases


def seeded_larger():
    rnd = random.Random(20261123)
    cases = 0
    for n, iterations in ((5, 350), (6, 140)):
        pairs = list(itertools.combinations(range(n), 2))
        for _ in range(iterations):
            edges = [(u, v, rnd.randint(-9, 12)) for u, v in pairs
                     if rnd.random() < 0.51]
            verify(n, edges)
            # Edge-order independence is also checked for both algorithms.
            shuffled = list(edges)
            rnd.shuffle(shuffled)
            assert sum(e[2] for e in kruskal(n, shuffled)) == sum(
                e[2] for e in prim(n, shuffled)
            )
            cases += 1
    return cases


def special_cases():
    graph = [
        (0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 2),
        (0, 4, 9), (0, 2, 4), (1, 3, 5), (2, 4, 6)
    ]
    assert exhaustive_oracle(5, graph)[0] == 8
    assert exhaustive_oracle(3, [(0, 1, 1), (0, 2, 1), (1, 2, 1)])[1].__len__() == 3
    disconnected = [(0, 1, -3), (1, 2, 1), (0, 2, 4), (3, 4, 0)]
    assert exhaustive_oracle(6, disconnected)[0] == -2
    verify(6, disconnected)
    # The graph is itself a tree: repeated weights do not prevent uniqueness.
    assert len(exhaustive_oracle(3, [(0, 1, 7), (1, 2, 7)])[1]) == 1
    for n in range(7):
        verify(n, [])


def check_integration():
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in catalog["books"] if b["id"] == "graph_and_knot_theory")
    included = re.findall(
        r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
        (ROOT / book["entrypoint"]).read_text(encoding="utf-8"),
    )
    assert included == book["chapters"] and len(included) == 40
    assert included[6].endswith("37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex")
    assert included[7].endswith("38-najkrotsze-drogi-wazone-i-algorytmy-wyszukiwania-tras.tex")
    assert included[8] == CHAPTER
    assert all((ROOT / path).is_file() for path in included)
    content = (ROOT / CHAPTER).read_text(encoding="utf-8")
    for env in ("twierdzenie", "stwierdzenie", "wniosek", "definicja",
                "proof", "przyklad", "uwaga", "figure", "tikzpicture"):
        assert content.count("\\begin{" + env + "}") == content.count(
            "\\end{" + env + "}"
        ), env
    labels = re.findall(r"\\label\{([^}]+)\}", content)
    assert len(labels) == len(set(labels))
    assert r"\label{thm:tg-mst-cut}" in content
    assert r"\label{thm:tg-mst-kruskal}" in content
    assert r"\label{thm:tg-mst-prim}" in content
    assert r"\label{prop:tg-mst-dsu}" in content
    assert r"\label{fig:tg-mst-five}" in content


if __name__ == "__main__":
    check_integration()
    print(f"PASS exhaustive small graphs: {exhaustive_small()}")
    print(f"PASS seeded larger graphs: {seeded_larger()}")
    special_cases()
    print("PASS hand-calculated examples, DSU invariants, cut/cycle properties and book integration")
