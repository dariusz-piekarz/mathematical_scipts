#!/usr/bin/env python3
"""Exact regression audit: Ford-Fulkerson, Edmonds-Karp, Dinic and min-cut.

The oracle independently enumerates all s/t cuts. Algorithms operate on
edge-indexed residual graphs, preserving identity of antiparallel and
parallel arcs. Integer and Fraction capacities are handled exactly.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import random
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex"


def independent_min_cut(n, arcs, s, t):
    best = None
    best_sets = []
    for mask in range(1 << n):
        if not ((mask >> s) & 1) or ((mask >> t) & 1):
            continue
        capacity = sum(
            (c for u, v, c in arcs
             if ((mask >> u) & 1) and not ((mask >> v) & 1)),
            start=0,
        )
        if best is None or capacity < best:
            best, best_sets = capacity, [mask]
        elif capacity == best:
            best_sets.append(mask)
    assert best is not None
    return best, best_sets


class Residual:
    def __init__(self, n, arcs):
        self.adj = [[] for _ in range(n)]
        self.original = []
        for u, v, c in arcs:
            assert u != v and c >= 0
            ui, vi = len(self.adj[u]), len(self.adj[v])
            self.adj[u].append([v, c, vi])
            self.adj[v].append([u, 0, ui])
            self.original.append((u, ui, c))

    def augment(self, path, amount):
        for u, index in path:
            edge = self.adj[u][index]
            assert 0 < amount <= edge[1]
            edge[1] -= amount
            reverse = self.adj[edge[0]][edge[2]]
            reverse[1] += amount

    def bfs(self, s):
        distance = [-1] * len(self.adj)
        distance[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and distance[v] == -1:
                    distance[v] = distance[u] + 1
                    q.append(v)
        return distance

    def check_flow(self, s, t, claimed):
        balance = [0] * len(self.adj)
        for u, index, cap in self.original:
            v, remaining, reverse_index = self.adj[u][index]
            flow = cap - remaining
            assert 0 <= flow <= cap
            assert self.adj[v][reverse_index][1] == flow, (
                u, v, cap, flow
            )
            balance[u] += flow
            balance[v] -= flow
        assert balance[s] == claimed
        assert balance[t] == -claimed
        assert all(x == 0 for v, x in enumerate(balance) if v not in (s, t))
        reachable = self.bfs(s)
        assert reachable[t] == -1
        return {v for v, d in enumerate(reachable) if d >= 0}


def edmonds_karp(n, arcs, s, t):
    residual = Residual(n, arcs)
    value = 0
    rounds = 0
    while True:
        parent = [None] * n
        parent[s] = (-1, -1)
        q = deque([s])
        while q and parent[t] is None:
            u = q.popleft()
            for i, (v, remaining, _) in enumerate(residual.adj[u]):
                if remaining > 0 and parent[v] is None:
                    parent[v] = (u, i)
                    q.append(v)
        if parent[t] is None:
            break
        path = []
        bottleneck = None
        v = t
        while v != s:
            u, index = parent[v]
            path.append((u, index))
            capacity = residual.adj[u][index][1]
            bottleneck = capacity if bottleneck is None else min(bottleneck, capacity)
            v = u
        assert bottleneck > 0
        prev_dist = residual.bfs(s)
        residual.augment(path, bottleneck)
        new_dist = residual.bfs(s)
        assert all(new_dist[v] == -1 or
                   (prev_dist[v] >= 0 and new_dist[v] >= prev_dist[v])
                   for v in range(n)), ("EK distance decreased", arcs, prev_dist, new_dist)
        value += bottleneck
        rounds += 1
        assert rounds <= 2 * len(arcs) * max(1, n) + 2
    cut = residual.check_flow(s, t, value)
    return value, cut, rounds


def dinic(n, arcs, s, t):
    residual = Residual(n, arcs)
    flow = 0
    phases = 0
    last_distance = 0
    while True:
        level = residual.bfs(s)
        if level[t] < 0:
            break
        phases += 1
        assert level[t] > last_distance
        last_distance = level[t]
        current = [0] * n

        def push(u, amount):
            if u == t:
                return amount
            while current[u] < len(residual.adj[u]):
                index = current[u]
                v, cap, _ = residual.adj[u][index]
                if cap > 0 and level[v] == level[u] + 1:
                    passed = push(v, min(amount, cap))
                    if passed > 0:
                        residual.augment([(u, index)], passed)
                        return passed
                current[u] += 1
            return 0

        while True:
            amount = push(s, sum((c for u, v, c in arcs if u == s), 0) + 1)
            if amount == 0:
                break
            flow += amount
        assert phases < n, ("Dinic too many phases", arcs, phases)
    cut = residual.check_flow(s, t, flow)
    return flow, cut, phases


def ford_fulkerson_depth_first(n, arcs, s, t):
    residual = Residual(n, arcs)
    value = 0
    steps = 0
    while True:
        visited = {s}
        path = []

        def find(u):
            if u == t:
                return True
            for i, (v, remaining, _) in enumerate(residual.adj[u]):
                if remaining > 0 and v not in visited:
                    visited.add(v)
                    path.append((u, i))
                    if find(v):
                        return True
                    path.pop()
            return False

        if not find(s):
            break
        bottleneck = min(residual.adj[u][i][1] for u, i in path)
        residual.augment(path, bottleneck)
        value += bottleneck
        steps += 1
        assert steps <= sum(c for u, v, c in arcs if u == s), (
            "integral Ford Fulkerson exceeded upper bound", steps, arcs
        )
    cut = residual.check_flow(s, t, value)
    return value, cut, steps


def validate(n, arcs, source=0, sink=None, include_ford=True):
    if sink is None:
        sink = n - 1
    expected, cut_masks = independent_min_cut(n, arcs, source, sink)
    a, cut_a, rounds_a = edmonds_karp(n, arcs, source, sink)
    b, cut_b, phases_b = dinic(n, arcs, source, sink)
    assert expected == a == b, (n, arcs, source, sink, expected, a, b)
    for cut in (cut_a, cut_b):
        capacity = sum(c for u, v, c in arcs if u in cut and v not in cut)
        assert capacity == expected, (arcs, cut, capacity, expected)
        assert sum(1 << v for v in cut) in cut_masks
    if include_ford:
        c, cut_c, steps_c = ford_fulkerson_depth_first(n, arcs, source, sink)
        assert c == expected
        assert sum(c for u, v, c in arcs if u in cut_c and v not in cut_c) == expected
    return expected


def test_exhaustive():
    checked = 0
    # Include isolated/disconnected graphs, zero capacities and antiparallel arcs.
    for n in range(2, 4):
        arcs_all = [(u, v) for u in range(n) for v in range(n) if u != v]
        for caps in product((0, 1, 2), repeat=len(arcs_all)):
            arcs = [(u, v, c) for (u, v), c in zip(arcs_all, caps) if c]
            validate(n, arcs)
            checked += 1
    # Exhaustive four-vertex DAGs plus a fixed antiparallel challenge below.
    n = 4
    arcs_all = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for caps in product((0, 1, 2), repeat=len(arcs_all)):
        arcs = [(u, v, c) for (u, v), c in zip(arcs_all, caps) if c]
        validate(n, arcs)
        checked += 1
    return checked


def test_seeded():
    rnd = random.Random(20261123)
    count = 0
    for n, repeats in ((4, 450), (5, 350), (6, 250)):
        for _ in range(repeats):
            arcs = [(u, v, rnd.randrange(0, 7))
                    for u in range(n) for v in range(n)
                    if u != v and rnd.random() < 0.43]
            # Exercise parallel original arcs and antiparallel arcs.
            if rnd.random() < 0.4 and arcs:
                arcs.append(arcs[rnd.randrange(len(arcs))])
            source, sink = rnd.sample(range(n), 2)
            validate(n, arcs, source, sink)
            count += 1
    return count


def test_rational():
    rnd = random.Random(234422)
    count = 0
    for n in range(2, 6):
        for _ in range(170):
            arcs = [(u, v, Fraction(rnd.randrange(0, 13), rnd.randrange(1, 9)))
                    for u in range(n) for v in range(n)
                    if u != v and rnd.random() < 0.43]
            validate(n, arcs, include_ford=False)
            count += 1
    return count


def test_backward_path():
    arcs = [(0, 1, 1), (0, 2, 1), (1, 2, 1),
            (1, 3, 1), (2, 3, 1)]
    residual = Residual(4, arcs)
    # First send 0->1->2->3.
    residual.augment([(0, 0), (1, 1), (2, 2)], 1)
    # Then use residual 0->2->1->3; the 2->1 arc is the reverse
    # of original 1->2, cancelling its previously assigned flow.
    rev_index = next(i for i, e in enumerate(residual.adj[2])
                     if e[0] == 1 and e[1] > 0)
    index_02 = next(i for i, e in enumerate(residual.adj[0])
                    if e[0] == 2 and e[1] > 0)
    index_13 = next(i for i, e in enumerate(residual.adj[1])
                    if e[0] == 3 and e[1] > 0)
    residual.augment([(0, index_02), (2, rev_index), (1, index_13)], 1)
    residual.check_flow(0, 3, 2)
    assert validate(4, arcs) == 2
    example = [(0, 1, 3), (0, 2, 2), (1, 2, 1),
               (1, 3, 2), (2, 3, 3)]
    assert validate(4, example) == 5
    assert validate(4, []) == 0


def test_integration():
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in catalog["books"] if b["id"] == "graph_and_knot_theory")
    includes = re.findall(r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
                          (ROOT / book["entrypoint"]).read_text(encoding="utf-8"))
    assert book["chapters"] == includes, (len(book["chapters"]), len(includes))
    assert len(includes) == 44
    assert includes[9] == CHAPTER
    assert all((ROOT / path).is_file() for path in includes)
    source = (ROOT / CHAPTER).read_text(encoding="utf-8")
    for env in ("twierdzenie", "lemat", "stwierdzenie", "definicja",
                "wniosek", "proof", "przyklad", "uwaga", "figure",
                "tikzpicture", "itemize", "enumerate"):
        assert source.count("\\begin{" + env + "}") == source.count(
            "\\end{" + env + "}"
        ), env
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    assert len(labels) == len(set(labels))
    for label in ("ch:tg-flow-algorithms", "thm:tg-flow-certificate",
                  "thm:tg-flow-ek", "thm:tg-flow-dinic",
                  "fig:tg-flow-backward", "fig:tg-flow-cut-five"):
        assert label in labels


if __name__ == "__main__":
    test_integration()
    print("PASS exhaustive directed small networks:", test_exhaustive())
    print("PASS seeded directed networks incl antiparallel/parallel:", test_seeded())
    print("PASS exact fractional capacities:", test_rational())
    test_backward_path()
    print("PASS reverse residual cancellation, hand-computed cuts and integration")
