#!/usr/bin/env python3
"""Finite, independent verification of BFS, DFS and chapter integration."""
from __future__ import annotations
import itertools
import json
import re
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REL = "chapters/pl/graph_and_knot_theory/37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex"

def components(adj):
    count, seen = 0, set()
    for root in adj:
        if root in seen:
            continue
        count += 1
        seen.add(root)
        pending = [root]
        for u in pending:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    pending.append(v)
    return count

def bfs(adj, source):
    d = {v: None for v in adj}
    parent = {v: None for v in adj}
    queue = deque([source])
    d[source] = 0
    while queue:
        u = queue.popleft()
        for v in sorted(adj[u]):
            if d[v] is None:
                d[v] = d[u] + 1
                parent[v] = u
                queue.append(v)
    return d, parent

def independent_shortest_paths(adj, source):
    # Dynamic programming by the number of edges, not BFS.
    d = {v: None for v in adj}
    d[source] = 0
    for _ in range(len(adj)):
        next_d = d.copy()
        for u in adj:
            if d[u] is not None:
                for v in adj[u]:
                    candidate = d[u] + 1
                    if next_d[v] is None or candidate < next_d[v]:
                        next_d[v] = candidate
        d = next_d
    return d

def dfs(adj, directed=False):
    color = {v: 0 for v in adj}
    parent = {v: None for v in adj}
    tin, tout, low = {}, {}, {}
    clock, back = 0, False

    def visit(u):
        nonlocal clock, back
        clock += 1
        tin[u] = low[u] = clock
        color[u] = 1
        for v in sorted(adj[u]):
            if color[v] == 0:
                parent[v] = u
                visit(v)
                low[u] = min(low[u], low[v])
            elif color[v] == 1 and (directed or v != parent[u]):
                back = True
                if not directed:
                    low[u] = min(low[u], tin[v])
        clock += 1
        tout[u] = clock
        color[u] = 2

    for root in adj:
        if color[root] == 0:
            visit(root)
    bridges = set()
    if not directed:
        for v, u in parent.items():
            if u is not None and low[v] > tin[u]:
                bridges.add(tuple(sorted((u, v))))
    return tin, tout, parent, bridges, back

def check_undirected():
    checked = 0
    for n in range(1, 6):
        edges = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            adj = {v: set() for v in range(n)}
            for i, (u, v) in enumerate(edges):
                if mask >> i & 1:
                    adj[u].add(v)
                    adj[v].add(u)
            edge_count = sum(map(len, adj.values())) // 2
            cc = components(adj)
            tin, tout, parent, bridges, back = dfs(adj)
            assert back == (edge_count > n - cc), (n, mask, "cycle")
            for v, u in parent.items():
                if u is not None:
                    assert tin[u] < tin[v] < tout[v] < tout[u]
            expected_bridges = set()
            for u, v in edges:
                if v not in adj[u]:
                    continue
                adj[u].remove(v)
                adj[v].remove(u)
                if components(adj) > cc:
                    expected_bridges.add((u, v))
                adj[u].add(v)
                adj[v].add(u)
            assert bridges == expected_bridges, (n, mask, bridges, expected_bridges)
            # Compare BFS to a separate path relaxation algorithm.
            for source in adj:
                d, parents = bfs(adj, source)
                assert d == independent_shortest_paths(adj, source), (n, mask, source)
                for v, distance in d.items():
                    if distance is None or v == source:
                        assert parents[v] is None
                    else:
                        assert parents[v] in adj[v]
                        assert d[parents[v]] == distance - 1
            # Compare BFS parity coloring to exhaustive 2-colorability.
            colorable = any(
                all(((colors >> u) & 1) != ((colors >> v) & 1)
                    for u, v in edges if v in adj[u])
                for colors in range(1 << n)
            )
            parity_ok = True
            seen = set()
            for source in adj:
                if source in seen:
                    continue
                dist, _ = bfs(adj, source)
                reachable = {v for v in adj if dist[v] is not None}
                seen |= reachable
                if any((dist[u] % 2) == (dist[v] % 2)
                       for u in reachable for v in adj[u]):
                    parity_ok = False
            assert parity_ok == colorable, (n, mask, "bipartite")
            checked += 1
    return checked

def independent_dag(adj):
    indegree = {v: 0 for v in adj}
    for u in adj:
        for v in adj[u]:
            indegree[v] += 1
    queue = deque(v for v in adj if indegree[v] == 0)
    removed = 0
    while queue:
        u = queue.popleft()
        removed += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return removed == len(adj)

def check_directed():
    checked = 0
    for n in range(1, 5):
        arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
        for mask in range(1 << len(arcs)):
            adj = {v: set() for v in range(n)}
            for i, (u, v) in enumerate(arcs):
                if mask >> i & 1:
                    adj[u].add(v)
            tin, tout, parent, bridges, back = dfs(adj, directed=True)
            dag = independent_dag(adj)
            assert dag != back, (n, mask, "DAG")
            if dag:
                order = sorted(adj, key=lambda v: -tout[v])
                pos = {v: i for i, v in enumerate(order)}
                assert all(pos[u] < pos[v] for u in adj for v in adj[u])
            checked += 1
    return checked

def check_integration():
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    match = [entry for entry in catalog["books"]
             if entry["id"] == "graph_and_knot_theory"]
    assert len(match) == 1
    book = match[0]
    inputs = re.findall(r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
                        (ROOT / book["entrypoint"]).read_text(encoding="utf-8"))
    assert book["chapters"] == inputs, (len(book["chapters"]), len(inputs))
    assert all((ROOT / path).exists() for path in inputs)
    assert inputs[6] == REL and len(inputs) == 43
    src = (ROOT / REL).read_text(encoding="utf-8")
    for env in ["proof", "twierdzenie", "lemat", "stwierdzenie",
                "definicja", "przyklad", "tikzpicture", "figure"]:
        assert src.count(r"\begin{" + env + "}") == src.count(
            r"\end{" + env + "}"), env
    labels = re.findall(r"\\label\{([^}]+)\}", src)
    assert len(labels) == len(set(labels)), "duplicate labels in chapter"
    assert "fig:tg-bfs-layers" in labels
    assert r"\caption{" in src

if __name__ == "__main__":
    check_integration()
    u = check_undirected()
    d = check_directed()
    print(f"PASS: chapter integration + {u} simple undirected and {d} "
          f"loopless directed exhaustive cases")
