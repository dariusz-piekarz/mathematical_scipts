#!/usr/bin/env python3
"""Independent finite audits of graph expansion, Cheeger and lazy random walks.

No third-party dependencies. The combinatorial oracle enumerates all cuts;
the spectral oracle is a self-contained symmetric Jacobi eigensolver.
The Markov-chain tests use exact Fraction arithmetic where possible.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import ceil, cos, log, pi, sqrt
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex"


def pairs(n):
    return list(combinations(range(n), 2))


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def components(adj):
    seen = set()
    count = 0
    for s in range(len(adj)):
        if s in seen:
            continue
        seen.add(s)
        stack = [s]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        count += 1
    return count


def exact_expansion(adj, d):
    n = len(adj)
    phi = None
    hE = None
    hV = None
    for mask in range(1, 1 << n):
        k = mask.bit_count()
        if k > n//2:
            continue
        outside = {v for v in range(n) if not mask >> v & 1}
        cut = sum(len(adj[u] & outside)
                  for u in range(n) if mask >> u & 1)
        boundary = len({v for v in outside
                        if any(mask >> u & 1 for u in adj[v])})
        edge_ratio = Fraction(cut, k)
        vertex_ratio = Fraction(boundary, k)
        conductance = Fraction(cut, d*k)
        hE = edge_ratio if hE is None else min(hE, edge_ratio)
        hV = vertex_ratio if hV is None else min(hV, vertex_ratio)
        phi = conductance if phi is None else min(phi, conductance)
    assert phi is not None
    return phi, hE, hV


def jacobi_eigenvalues(matrix):
    """All eigenvalues for a real symmetric matrix, without NumPy."""
    n = len(matrix)
    a = [list(map(float, row)) for row in matrix]
    for _ in range(60*n*n+1):
        p, q = 0, 1
        best = 0.0
        for i in range(n):
            for j in range(i+1, n):
                if abs(a[i][j]) > best:
                    best, p, q = abs(a[i][j]), i, j
        if best < 1e-13:
            break
        tau = (a[q][q]-a[p][p])/(2*a[p][q])
        tangent = (1 if tau >= 0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c = 1/sqrt(1+tangent*tangent)
        s = tangent*c
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = app-tangent*apq
        a[q][q] = aqq+tangent*apq
        a[p][q] = a[q][p] = 0.0
        for i in range(n):
            if i == p or i == q:
                continue
            aip, aiq = a[i][p], a[i][q]
            a[i][p] = a[p][i] = c*aip-s*aiq
            a[i][q] = a[q][i] = s*aip+c*aiq
    else:
        raise AssertionError("Jacobi did not converge")
    return sorted(a[i][i] for i in range(n))


def normalized_spectrum(adj, d):
    return jacobi_eigenvalues([
        [float((1 if u == v else 0) - Fraction(1,d)*int(v in adj[u]))
         for v in range(len(adj))]
        for u in range(len(adj))
    ])


def check_lazy_walk(adj, d, lambda2):
    n = len(adj)
    q = [[Fraction(int(u == v), 2)+Fraction(int(v in adj[u]),2*d)
          for v in range(n)] for u in range(n)]
    assert all(sum(row) == 1 for row in q)
    pi = Fraction(1,n)
    rate = max(0.0, 1.0-lambda2/2)
    for start in range(n):
        mu = [Fraction(int(v == start)) for v in range(n)]
        for t in range(9):
            tv = sum((abs(x-pi) for x in mu), Fraction(0))/2
            bound = sqrt(n-1)/2 * (rate**t)
            assert float(tv) <= bound+5e-9, (
                "lazy mixing inequality", n, d, start, t,
                float(tv), bound, lambda2
            )
            mu = [sum((mu[u]*q[u][v] for u in range(n)),Fraction(0))
                  for v in range(n)]


def analyze(n, edges, mixing=True):
    adj = adjacency(n, edges)
    degrees = [len(x) for x in adj]
    if min(degrees) < 1 or len(set(degrees)) != 1:
        return False
    d = degrees[0]
    phi, hE, hV = exact_expansion(adj, d)
    assert hV <= hE <= d*hV
    assert phi == hE/d
    assert phi <= hV <= d*phi
    eigenvalues = normalized_spectrum(adj, d)
    assert abs(eigenvalues[0]) < 1e-9
    assert all(-1e-9 <= v <= 2+1e-9 for v in eigenvalues)
    lambda2 = max(0.0,eigenvalues[1])
    assert lambda2 <= 2*float(phi)+1e-8, (
        "upper Cheeger", n, edges, phi, lambda2
    )
    assert float(phi)**2/2 <= lambda2+1e-8, (
        "lower Cheeger", n, edges, phi, lambda2
    )
    connected = components(adj) == 1
    assert (lambda2 > 1e-9) == connected, (n, edges, lambda2)
    assert (phi > 0) == connected
    # Independent exact energy identity on nonconstant test functions.
    for f in ([i % 3-1 for i in range(n)],
              [int(i == 0) for i in range(n)],
              [i*i-2*i for i in range(n)]):
        energy = sum((f[u]-f[v])**2 for u, v in edges)
        lap = [d*f[u]-sum(f[v] for v in adj[u]) for u in range(n)]
        assert energy == sum(f[u]*lap[u] for u in range(n))
    if connected:
        diameter = 0
        for root in range(n):
            distances = {root: 0}
            queue = [root]
            for u in queue:
                for v in adj[u]:
                    if v not in distances:
                        distances[v] = distances[u]+1
                        queue.append(v)
            diameter = max(diameter,max(distances.values()))
        bound = 2*(ceil(log(n)/log(1+float(hV)))+1)
        assert diameter <= bound
        if mixing:
            check_lazy_walk(adj,d,lambda2)
    return True


def exhaustive_small():
    checked, eligible = 0, 0
    for n in range(2, 7):
        edges_all = pairs(n)
        for mask in range(1 << len(edges_all)):
            edges = [edge for i, edge in enumerate(edges_all) if mask >> i & 1]
            checked += 1
            if analyze(n,edges,mixing=n<=5):
                eligible += 1
    return checked, eligible


def cycles_and_complete():
    checked = 0
    for n in range(3, 13):
        cyc = sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})
        assert len(cyc) == n
        ac = adjacency(n,cyc)
        phi, _, _ = exact_expansion(ac,2)
        eig = normalized_spectrum(ac,2)
        assert phi == Fraction(1,n//2)
        assert abs(eig[1]-(1-cos(2*pi/n))) < 1e-8, (n,eig)
        assert analyze(n,cyc,mixing=n<=6)
        complete = pairs(n)
        ac = adjacency(n,complete)
        phi, _, _ = exact_expansion(ac,n-1)
        eig = normalized_spectrum(ac,n-1)
        assert phi == Fraction(ceil(n/2),n-1)
        assert abs(eig[1]-n/(n-1)) < 1e-8
        assert analyze(n,complete,mixing=n<=5)
        checked += 2
    # Disconnected 2-regular C3+C3 has zero spectral gap and conductance.
    disconnected = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)]
    assert analyze(6,disconnected)
    return checked+1


def integration():
    cat = json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in cat["books"] if b["id"] == "graph_and_knot_theory")
    included = re.findall(
        r"\\input\{../../(chapters/pl/graph_and_knot_theory/[^}]+)\}",
        (ROOT/book["entrypoint"]).read_text(encoding="utf-8"),
    )
    assert included == book["chapters"] and len(included) == 44
    assert included[12] == CHAPTER
    assert all((ROOT/path).is_file() for path in included)
    source = (ROOT/CHAPTER).read_text(encoding="utf-8")
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    assert len(labels) == len(set(labels))
    for req in ("ch:tg-expanders","def:tg-expander-constants",
                "def:tg-expander-laplacian","lem:tg-expander-coarea",
                "thm:tg-expander-cheeger","thm:tg-expander-mixing",
                "thm:tg-expander-diameter","fig:tg-expander-cycle-cut"):
        assert req in labels
    for env in ("definicja","lemat","twierdzenie","stwierdzenie",
                "wniosek","przyklad","uwaga","proof","figure","tikzpicture"):
        assert source.count(r"\begin{"+env+"}") == source.count(
            r"\end{"+env+"}"),env


if __name__ == "__main__":
    integration()
    a,b = exhaustive_small()
    print(f"PASS exhaustive graph models: {a}, regular eligible: {b}")
    print(f"PASS spectral examples, disconnected example: {cycles_and_complete()}")
    print("PASS Cheeger, boundary relations, lazy-walk mixing, diameter, energy, catalog")
