#!/usr/bin/env python3
"""Audit 33: second independent chapter-43 regressions.

Different graph families and oracles from audit 32: exact cut enumeration
against independent combinatorial formulas, coarea layer-cake identity over
integer-valued functions, discrete Cheeger energy, and exact rational
Markov-chain evolution on complete bipartite graphs and hypercubes.

These finite regressions do not replace the mathematical proofs.
"""
from fractions import Fraction
from itertools import combinations
from math import cos, log, pi, sqrt
from pathlib import Path
from random import Random

RNG = Random(20261124033)
ROOT = Path(__file__).resolve().parents[2]
TEX = ROOT / "chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex"


def cube(d):
    n = 1 << d
    return n, [(v, v ^ (1 << i)) for v in range(n)
               for i in range(d) if v < (v ^ (1 << i))], d


def bipartite(m):
    return 2 * m, [(u, m + v) for u in range(m) for v in range(m)], m


def cycle(n):
    return n, [(v, (v + 1) % n) for v in range(n)], 2


def cut_values(n, edges):
    """Independent exact enumeration of edge and external vertex boundaries."""
    h_e = h_v = None
    for mask in range(1, 1 << n):
        size = mask.bit_count()
        if size > n // 2:
            continue
        boundary = [(u, v) for u, v in edges
                    if ((mask >> u) ^ (mask >> v)) & 1]
        ext = {v if mask >> u & 1 else u for u, v in boundary}
        ev, vv = Fraction(len(boundary), size), Fraction(len(ext), size)
        h_e = ev if h_e is None else min(h_e, ev)
        h_v = vv if h_v is None else min(h_v, vv)
    return h_e, h_v


def check_closed_form_families():
    counter = 0
    for d in range(1, 5):
        n, edges, degree = cube(d)
        e, v = cut_values(n, edges)
        assert e == 1, (d, "hypercube", e)
        assert e / degree == Fraction(1, d)
        assert Fraction(1, d) <= v <= e
        gap = Fraction(2, d)  # Q_d adjacency eigenvalues d-2j
        assert gap / 2 <= e / degree
        assert (e / degree) ** 2 <= 2 * gap
        counter += 1

    for m in range(1, 7):
        n, edges, degree = bipartite(m)
        e, v = cut_values(n, edges)
        # A k-subset with a left and b right vertices has
        # exactly m(a+b)-2ab crossing edges; optimize independently.
        expected = min(Fraction(m * (a + b) - 2 * a * b, a + b)
                       for a in range(m + 1)
                       for b in range(m + 1)
                       if 1 <= a + b <= m)
        assert e == expected, (m, e, expected)
        assert e / m <= v <= e
        gap = Fraction(2 if m == 1 else 1)
        assert gap / 2 <= e / m
        assert (e / m) ** 2 <= 2 * gap
        counter += 1

    for n in range(3, 13):
        _, edges, d = cycle(n)
        e, _ = cut_values(n, edges)
        assert e == Fraction(2, n // 2), (n, e)
        assert e / d == Fraction(1, n // 2)
        gap = 1 - cos(2 * pi / n)
        assert gap / 2 <= float(e / d) + 1e-12
        assert float((e / d) ** 2) <= 2 * gap + 1e-12
        counter += 1
    print(f"PASS chapter 43 second pass: {counter} exact structured-family cut/spectral checks")


def coarea_layers(n, edges, g):
    """Layer-cake formula: integral of boundaries of {g²>t}."""
    squares = [x * x for x in g]
    levels = sorted(set([0] + squares))
    total = 0
    for lo, hi in zip(levels, levels[1:]):
        inside = {v for v, x in enumerate(squares) if x > lo}
        crossing = sum((u in inside) != (v in inside) for u, v in edges)
        total += (hi - lo) * crossing
    return total


def verify_coarea():
    checked = 0
    families = [cube(4), bipartite(5), cycle(10), cube(3), bipartite(3)]
    for n, edges, d in families:
        assert len(edges) * 2 == n * d
        h_e, _ = cut_values(n, edges)
        phi = h_e / d
        for _ in range(300):
            g = [0] * n
            support = RNG.sample(range(n), RNG.randrange(1, n // 2 + 1))
            for i in support:
                g[i] = RNG.randrange(1, 9)
            norm_sq = sum(x * x for x in g)
            sum_abs = sum(abs(g[u] ** 2 - g[v] ** 2) for u, v in edges)
            energy = sum((g[u] - g[v]) ** 2 for u, v in edges)
            plus_sq = sum((g[u] + g[v]) ** 2 for u, v in edges)
            assert sum_abs == coarea_layers(n, edges, g), "coarea integral"
            assert sum_abs >= d * phi * norm_sq, "level-set expansion"
            assert sum_abs ** 2 <= energy * plus_sq, "Cauchy-Schwarz"
            assert plus_sq <= 2 * d * norm_sq, "sum-of-squares"
            assert Fraction(energy) >= Fraction(d, 2) * phi * phi * norm_sq, "Cheeger coarea"
            checked += 1
    print(f"PASS chapter 43 second pass: {checked} exact coarea/energy function tests")


def lazy_walk(n, edges, d, start, iterations):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    mu = [Fraction(int(i == start)) for i in range(n)]
    for t in range(iterations + 1):
        yield t, mu
        mu = [mu[v] / 2 + sum((mu[u] for u in adj[v]), Fraction(0)) / (2 * d)
              for v in range(n)]


def verify_mixing():
    checks = 0
    families = [cube(1), cube(2), cube(3), cube(4)]
    families += [bipartite(m) for m in range(1, 6)]
    families += [cycle(n) for n in range(3, 10)]
    for n, edges, d in families:
        if n == 1 << d and len(edges) == n * d // 2 and (n, edges, d) in families[:4]:
            gap = 2 / d
        elif n == 2 * d and (n, edges, d) in families[4:9]:
            gap = 2 if d == 1 else 1
        else:
            gap = 1 - cos(2 * pi / n)
        contraction = 1 - gap / 2
        assert 0 <= contraction < 1
        for start in range(n):
            for t, mu in lazy_walk(n, edges, d, start, 12):
                assert sum(mu) == 1 and all(p >= 0 for p in mu)
                tv = float(sum((abs(x - Fraction(1, n)) for x in mu), Fraction(0)) / 2)
                bound = sqrt(n - 1) / 2 * contraction ** t
                assert tv <= bound + 1e-10, (n, d, start, t, tv, bound)
                checks += 1
    # The non-lazy walk on K2 never converges: its law alternates
    # between the two point masses, while the lazy walk mixes at t=1.
    assert all(Fraction(1, 2) == Fraction(1, 2) for _ in range(10))
    non_lazy = [Fraction(1), Fraction(0)]
    for _ in range(12):
        assert sum(abs(p - Fraction(1, 2)) for p in non_lazy) / 2 == Fraction(1, 2)
        non_lazy = non_lazy[::-1]
    assert next(mu for t, mu in lazy_walk(2, [(0, 1)], 1, 0, 1) if t == 1) == [Fraction(1, 2)] * 2
    print(f"PASS chapter 43 second pass: {checks} exact lazy-mixing checks and K2 nonlazy obstruction")


def verify_source():
    text = TEX.read_text(encoding="utf-8")
    assert text.count(r"\label{thm:tg-expander-cheeger}") == 1
    assert text.count(r"\label{thm:tg-expander-mixing}") == 1
    assert text.count(r"\label{lem:tg-expander-coarea}") == 1
    assert text.count(r"\label{thm:tg-expander-diameter}") == 1
    cheeger = text.split(r"\label{thm:tg-expander-cheeger}", 1)[1].split(r"\end{twierdzenie}", 1)[0]
    assert r"\lambda_2(G)" in cheeger and r"\Phi(G)" in cheeger
    mixing = text.split(r"\label{thm:tg-expander-mixing}", 1)[1].split(r"\end{twierdzenie}", 1)[0]
    assert r"spójnym grafem" in mixing and r"$d$-regularnym" in mixing
    assert r"\|\mu Q^t-\pi\|_{\mathrm{TV}}" in mixing
    assert r"Q=(I+P)/2" in text
    print("PASS chapter 43 second pass: exact hypotheses and stable TeX labels")


if __name__ == "__main__":
    check_closed_form_families()
    verify_coarea()
    verify_mixing()
    verify_source()
    print("PASS chapter 43 second independent regression suite")
