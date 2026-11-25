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


def test_edge_mixing():
    # TG43-EM-01: independent oriented edge counts, including overlapping sets.
    count = 0
    for n in range(2, 6):
        E = pairs(n)
        for mask in range(1 << len(E)):
            adj = adjacency(n, [e for i,e in enumerate(E) if mask >> i & 1])
            d = len(adj[0])
            if d == 0 or any(len(row) != d for row in adj):
                continue
            theta = jacobi_eigenvalues([[int(v in adj[u]) for v in range(n)]
                                        for u in range(n)])
            Lambda = max(abs(x) for x in theta[:-1])
            sets = [{v for v in range(n) if mask >> v & 1}
                    for mask in range(1 << n)]
            for S in sets:
                for T in sets:
                    e = sum(len(adj[u] & T) for u in S)
                    delta = abs(e - Fraction(d*len(S)*len(T), n))
                    a = Fraction(len(S)*(n-len(S)), n)
                    b = Fraction(len(T)*(n-len(T)), n)
                    assert float(delta) <= Lambda*sqrt(float(a*b))+1e-8
                    count += 1
    return count


def test_weighted_cheeger_mixing():
    # TG43-WGT-01: irregular connected graphs; exact cuts and Markov steps.
    count = steps = 0
    for n in range(2, 6):
        E = pairs(n)
        for mask in range(1 << len(E)):
            edges = [e for i,e in enumerate(E) if mask >> i & 1]
            adj = adjacency(n, edges)
            if components(adj) != 1:
                continue
            deg = [len(a) for a in adj]
            if len(set(deg)) == 1:
                continue
            W = sum(deg)
            cuts = []
            for k in range(1, 1 << n):
                S = {v for v in range(n) if k >> v & 1}
                vol = sum(deg[v] for v in S)
                if 0 < 2*vol <= W:
                    cuts.append(Fraction(sum(len(adj[v]-S) for v in S), vol))
            phi = min(cuts)
            eig = jacobi_eigenvalues([[int(u == v)-int(v in adj[u])/sqrt(deg[u]*deg[v])
                                       for v in range(n)] for u in range(n)])
            assert abs(eig[0]) < 1e-8 and 0 < eig[1] <= 2+1e-8
            assert float(phi**2/2) <= eig[1]+1e-8
            assert eig[1] <= 2*float(phi)+1e-8
            Q = [[Fraction(int(u == v),2)+Fraction(int(v in adj[u]),2*deg[u])
                  for v in range(n)] for u in range(n)]
            pi = [Fraction(d,W) for d in deg]
            assert all(sum(row) == 1 for row in Q)
            assert all(pi[u]*Q[u][v] == pi[v]*Q[v][u]
                       for u in range(n) for v in range(n))
            assert [sum(pi[u]*Q[u][v] for u in range(n)) for v in range(n)] == pi
            for start in range(n):
                mu = [Fraction(int(v == start)) for v in range(n)]
                for t in range(5):
                    tv = sum(abs(mu[v]-pi[v]) for v in range(n))/2
                    bound = (max(0.0,1-eig[1]/2)**t
                             *sqrt(float(1/pi[start]-1))/2)
                    assert float(tv) <= bound+1e-8
                    mu = [sum(mu[u]*Q[u][v] for u in range(n)) for v in range(n)]
                    steps += 1
            count += 1
    return count, steps


def test_weighted_energy_density():
    # TG43-ENE-01: exact polarization and positive-part inequalities,
    # plus the density evolution identity for non-point-mass distributions.
    graphs = functions = distributions = 0
    for n in range(2, 5):
        E = pairs(n)
        for mask in range(1 << len(E)):
            edges = [e for i,e in enumerate(E) if mask >> i & 1]
            adj = adjacency(n, edges)
            if components(adj) != 1:
                continue
            deg = [len(a) for a in adj]
            W = sum(deg)
            pi = [Fraction(d,W) for d in deg]
            Q = [[Fraction(int(u == v),2)+Fraction(int(v in adj[u]),2*deg[u])
                  for v in range(n)] for u in range(n)]
            for f in product((-1,0,1,2), repeat=n):
                g = [max(a,0) for a in f]
                lap = [deg[v]*f[v]-sum(f[u] for u in adj[v])
                       for v in range(n)]
                mixed = sum((g[u]-g[v])*(f[u]-f[v]) for u,v in edges)
                energy = sum((g[u]-g[v])**2 for u,v in edges)
                assert sum(g[v]*lap[v] for v in range(n)) == mixed >= energy
                # Integrate the piecewise-constant boundary and volume exactly.
                levels = sorted({0, *(a*a for a in g)})
                boundary_integral = volume_integral = 0
                for lo, hi in zip(levels, levels[1:]):
                    S = {v for v in range(n) if g[v]**2 > lo}
                    boundary_integral += (hi-lo)*sum(len(adj[v]-S) for v in S)
                    volume_integral += (hi-lo)*sum(deg[v] for v in S)
                assert boundary_integral == sum(abs(g[u]**2-g[v]**2) for u,v in edges)
                assert volume_integral == sum(deg[v]*g[v]**2 for v in range(n))
                functions += 1
            for weights in product(range(3), repeat=n):
                total = sum(weights)
                if not total:
                    continue
                mu = [Fraction(w,total) for w in weights]
                h = [mu[v]/pi[v]-1 for v in range(n)]
                nu = [sum(mu[u]*Q[u][v] for u in range(n)) for v in range(n)]
                evolved = [sum(Q[v][u]*h[u] for u in range(n)) for v in range(n)]
                assert evolved == [nu[v]/pi[v]-1 for v in range(n)]
                assert sum(pi[v]*h[v] for v in range(n)) == 0
                distributions += 1
            graphs += 1
    return graphs, functions, distributions


def test_small_diameter_not_expansion():
    # TG43-DIA-01; ex:tg-expander-small-diameter.
    # Two full binary trees, leaf cycles and a single root bridge.
    count = 0
    for h in range(2, 7):
        m = 2**(h+1)-1
        n = 2*m
        edges = {(0, m)}
        for offset in (0, m):
            for v in range(1, m):
                edges.add((offset+(v-1)//2, offset+v))
            leaves = list(range(offset+2**h-1, offset+m))
            for u, v in zip(leaves, leaves[1:]+leaves[:1]):
                edges.add(tuple(sorted((u,v))))
        assert all(0 <= u < v < n for u, v in edges)
        adj = adjacency(n, edges)
        assert all(len(row) == 3 for row in adj)
        assert components(adj) == 1
        S = set(range(m))
        cut = sum(len(adj[v]-S) for v in S)
        assert cut == 1 and 2*len(S) == n
        assert Fraction(cut,3*len(S)) == Fraction(2,3*n)
        # Independent all-sources BFS, without an assumed tree metric.
        diameter = 0
        for root in range(n):
            distances = {root: 0}
            queue = [root]
            for u in queue:
                for v in adj[u]:
                    if v not in distances:
                        distances[v] = distances[u]+1
                        queue.append(v)
            assert len(distances) == n
            diameter = max(diameter, max(distances.values()))
        assert diameter == 2*h+1
        # Exhaustive independent cut oracle for the smallest model.
        if h == 2:
            phi, _, _ = exact_expansion(adj, 3)
            assert phi == Fraction(2, 3*n)
        count += 1
    return count


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
                "thm:tg-expander-diameter","fig:tg-expander-cycle-cut",
                "ex:tg-expander-small-diameter"):
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
    print("PASS TG43-EM-01 oriented edge count comparisons:", test_edge_mixing())
    print("PASS TG43-WGT-01 irregular graphs and exact walk steps:", test_weighted_cheeger_mixing())
    print("PASS TG43-ENE-01 graphs, functions, distributions:", test_weighted_energy_density())
    print("PASS TG43-DIA-01 cubic counterexample models:", test_small_diameter_not_expansion())
    print("PASS Cheeger, boundary relations, lazy-walk mixing, diameter, energy, catalog")
