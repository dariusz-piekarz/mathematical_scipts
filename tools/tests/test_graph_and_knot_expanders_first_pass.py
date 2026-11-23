#!/usr/bin/env python3
"""Audit 32, chapter 43: independent finite checks of expander assertions.

Enumerate every simple graph on 2..6 vertices; select regular graphs and
compare exact edge/vertex cuts, normalized Cheeger inequalities, a separately
implemented Jacobi eigenvalue solver, BFS diameter and lazy-walk mixing.
No third-party Python libraries are needed. Finite models do not prove the
general theorems.
"""
from fractions import Fraction
from itertools import combinations
from math import ceil, log, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex"


def spectrum_jacobi(matrix):
    """Eigenvalues of a real symmetric matrix, using plane rotations."""
    a = [[float(x) for x in row] for row in matrix]
    n = len(a)
    for _ in range(120 * n * n):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-13:
            break
        tau = (a[q][q] - a[p][p]) / (2 * a[p][q])
        t = (1 if tau >= 0 else -1) / (abs(tau) + sqrt(1 + tau * tau))
        c = 1 / sqrt(1 + t * t)
        s = t * c
        off = a[p][q]
        a[p][p] -= t * off
        a[q][q] += t * off
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k in (p, q):
                continue
            x, y = a[k][p], a[k][q]
            a[k][p] = a[p][k] = c * x - s * y
            a[k][q] = a[q][k] = s * x + c * y
    else:
        raise AssertionError("Jacobi diagonalization did not converge")
    return sorted(a[i][i] for i in range(n))


def all_cuts(n, edges):
    edge_best = None
    vertex_best = None
    for mask in range(1, 1 << n):
        k = mask.bit_count()
        if k > n // 2:
            continue
        boundary_edges = [(u, v) for u, v in edges if bool(mask >> u & 1) != bool(mask >> v & 1)]
        boundary_vertices = set()
        for u, v in boundary_edges:
            boundary_vertices.add(v if mask >> u & 1 else u)
        e, v = Fraction(len(boundary_edges), k), Fraction(len(boundary_vertices), k)
        edge_best = e if edge_best is None else min(edge_best, e)
        vertex_best = v if vertex_best is None else min(vertex_best, v)
    assert edge_best is not None and vertex_best is not None
    return edge_best, vertex_best


def bfs_distances(n, edges, root):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    dist = {root: 0}
    queue = [root]
    for u in queue:
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def diameter(n, edges):
    all_dist = [bfs_distances(n, edges, v) for v in range(n)]
    if any(len(d) != n for d in all_dist):
        return None
    return max(max(d.values()) for d in all_dist)


def check_lazy_mixing(n, edges, d, lam2):
    adj = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj[u][v] = adj[v][u] = 1
    pi = Fraction(1, n)
    contraction = max(0.0, 1 - lam2 / 2)
    for start in range(n):
        mu = [Fraction(int(i == start)) for i in range(n)]
        for t in range(11):
            tv = Fraction(1, 2) * sum(abs(x - pi) for x in mu)
            assert float(tv) <= 0.5 * sqrt(n - 1) * contraction ** t + 2e-9, (n, d, start, t, tv)
            nxt = []
            for v in range(n):
                nxt.append(mu[v] / 2 + sum(mu[u] for u in range(n) if adj[u][v]) / (2 * d))
            assert sum(nxt) == 1
            mu = nxt


def check_graph(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    if len(set(deg)) != 1 or deg[0] == 0:
        return False
    d = deg[0]
    h_e, h_v = all_cuts(n, edges)
    phi = h_e / d
    assert h_v <= h_e <= d * h_v
    assert phi <= h_v <= d * phi

    adj = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj[u][v] = adj[v][u] = 1
    L = [[Fraction(int(u == v)) - Fraction(adj[u][v], d) for v in range(n)] for u in range(n)]
    values = spectrum_jacobi(L)
    assert min(values) > -2e-10 and max(values) < 2 + 2e-10
    gap = max(0.0, values[1])
    assert gap / 2 <= float(phi) + 2e-9, ("Cheeger upper", n, d, edges)
    assert float(phi) <= sqrt(2 * gap) + 2e-8, ("Cheeger lower", n, d, edges)
    diam = diameter(n, edges)
    assert (diam is None) == (gap < 1e-9)
    if diam is not None:
        assert h_v > 0
        radius = ceil(log(n) / log(1 + float(h_v))) + 1
        assert diam <= 2 * radius
        check_lazy_mixing(n, edges, d, gap)
    return True


def verify_exhaustive():
    total = 0
    connected = 0
    for n in range(2, 7):
        candidates = list(combinations(range(n), 2))
        for mask in range(1 << len(candidates)):
            edges = [edge for k, edge in enumerate(candidates) if mask >> k & 1]
            if check_graph(n, edges):
                total += 1
                if diameter(n, edges) is not None:
                    connected += 1
    assert total == 193 and connected >= 150, (total, connected)
    print(f"PASS chapter 43: {total} exhaustive positive-regular graphs; {connected} connected mixing/diameter checks")


def verify_examples_and_source():
    for n in range(3, 13):
        cycle = [(i, (i + 1) % n) for i in range(n)]
        e, v = all_cuts(n, cycle)
        assert e == Fraction(2, n // 2)
        assert v >= e / 2
        lam = spectrum_jacobi([[Fraction(int(i == j)) -
                                 Fraction(int((i - j) % n in (1, n - 1)), 2)
                                 for j in range(n)] for i in range(n)])[1]
        assert abs(lam - (1 - __import__("math").cos(2 * __import__("math").pi / n))) < 1e-9
    for n in range(2, 9):
        complete = list(combinations(range(n), 2))
        h_e, _ = all_cuts(n, complete)
        assert h_e / (n - 1) == Fraction((n + 1) // 2, n - 1)
    # Confirm the hypotheses that make the mixing theorem true, including
    # laziness and connectedness; simple non-lazy walks fail on bipartite K2.
    text = CHAPTER.read_text(encoding="utf-8")
    assert text.count(r"\label{thm:tg-expander-mixing}") == 1
    assert r"Q=(I+P)/2" in text
    assert r"Niech $G$ będzie spójnym grafem" in text
    assert r"\lambda_2(G)" in text
    assert r"\label{thm:tg-expander-cheeger}" in text
    assert r"\label{thm:tg-expander-diameter}" in text
    print("PASS chapter 43: complete graphs, cycles, bipartite laziness and TeX hypotheses")


if __name__ == "__main__":
    verify_exhaustive()
    verify_examples_and_source()
    print("PASS chapter 43 first independent audit (finite regressions, not general proofs)")
