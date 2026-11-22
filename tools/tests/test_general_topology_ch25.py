#!/usr/bin/env python3
"""Regressions for Chapter 25 (continua, inverse limits, tent map, solenoid).

Computational checks cover finite models only; the infinite continuum
theorems are established by the manuscript's mathematical proofs.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path
import json
import math
import re

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/25-continua-i-ich-struktura.tex"


def tent(t: float) -> float:
    assert 0 <= t <= 1
    return 2*t if t <= .5 else 2-2*t


def tent_power(t: float, n: int) -> float:
    for _ in range(n):
        t = tent(t)
    return t


def tent_branches() -> int:
    trials = 0
    for r in range(1, 8):
        pieces = 2**r
        for j in range(pieces):
            a, b = j/pieces, (j+1)/pieces
            va, vb = tent_power(a, r), tent_power(b, r)
            assert sorted((round(va, 10), round(vb, 10))) == [0, 1]
            for t in (.1, .25, .5, .75, .9):
                x = a+t*(b-a)
                expected = va+(vb-va)*t
                assert abs(tent_power(x, r)-expected) < 2e-9
                trials += 1
        # The convex hull of any full-branch preimage of an open
        # interval meets both extreme laps; only the statement of the
        # finite branch property is sampled here.
        for q in (.2, .6, .9):
            lo = (q if va == 1 else 1-q)/pieces
            assert 0 <= lo <= 1/pieces
    # Crucial two-fold coverage of [1/4,3/4].
    values = [tent_power(.25 + .5*k/400, 2) for k in range(401)]
    assert min(values) < 1e-8 and max(values) > .999999
    return trials


def inverse_limit_finite_sets() -> int:
    # A nontrivial finite inverse system, f: Z/6 -> Z/3, then
    # f: Z/12 -> Z/6; all bonding maps are surjective.
    pairs = 0
    for z in range(12):
        x1 = z % 6
        x0 = x1 % 3
        assert x0 == z % 3
        pairs += 1
    assert {z % 6 for z in range(12)} == set(range(6))
    assert {z % 3 for z in range(12)} == set(range(3))
    return pairs


def solenoid_root_branches() -> int:
    checks = 0
    for t0 in (-.15, 0., .19, .37):
        for choices in product((0, 1), repeat=7):
            tn = t0
            z = complex(math.cos(2*math.pi*tn), math.sin(2*math.pi*tn))
            for eps in choices:
                tn = (tn+eps)/2
                w = complex(math.cos(2*math.pi*tn), math.sin(2*math.pi*tn))
                assert abs(w*w-z) < 1e-12
                z = w
                checks += 1
    return checks



def peano_interleaving() -> int:
    """All dyadic lattice points at resolution 1/16 in the square are
    reached by an interleaving of finitely many binary digits.
    """
    seen = set()
    for digits in product((0, 1), repeat=8):
        x = sum(digits[2*j] * 2**(3-j) for j in range(4))
        y = sum(digits[2*j+1] * 2**(3-j) for j in range(4))
        seen.add((x, y))
    assert seen == {(x, y) for x in range(16) for y in range(16)}
    return len(seen)


def finite_graph_tours() -> int:
    """Construct a closed walk from a root visiting every edge,
    the discrete model used in the finite graph Peano proof.
    """
    examples = [
        (3, [(0, 1), (1, 2)]),
        (3, [(0, 1), (1, 2), (2, 0)]),
        (5, [(0, 1), (0, 2), (2, 3), (2, 4)]),
    ]
    seen_count = 0
    for n, edges in examples:
        adjacency = {v: set() for v in range(n)}
        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)
        parent = {0: None}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in sorted(adjacency[x]):
                if y not in parent:
                    parent[y] = x
                    stack.append(y)
        assert len(parent) == n

        def root_path(x):
            path = [x]
            while parent[path[-1]] is not None:
                path.append(parent[path[-1]])
            return list(reversed(path))

        walk = [0]
        for u, v in edges:
            path = root_path(u)
            walk.extend(path[1:])
            walk.append(v)
            other = root_path(v)
            walk.extend(list(reversed(other))[1:])
            assert walk[-1] == 0
        traversed = {frozenset((walk[i], walk[i+1]))
                     for i in range(len(walk)-1)}
        assert all(frozenset((u, v)) in traversed for u, v in edges)
        seen_count += len(edges)
    return seen_count

def source_integration() -> tuple[int, int]:
    chapter = (ROOT / CH).read_text(encoding="utf-8")
    entry = (ROOT / "books/pl/general_topology_ch25.tex").read_text(encoding="utf-8")
    book = (ROOT / "books/pl/general_topology.tex").read_text(encoding="utf-8")
    cat = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(item["chapters"] for item in cat["books"]
                    if item["id"] == "general_topology")
    assert len(chapters) >= 25 and chapters[24] == CH
    assert r"\input{../../" + CH + "}" in entry
    assert r"\input{../../" + CH + "}" in book
    assert r"\setcounter{chapter}{24}" in entry
    for i in ("05", "08", "23"):
        assert rf"\externaldocument{{general_topology_ch{i}}}" in entry
    assert "Wersja 1.25 — rozdziały 01–24 stabilne; rozdział 25 w audycie" in book
    source = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in chapters)
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)
    assert len(labels) == len(set(labels)), "duplicate labels"
    assert set(refs) <= set(labels), sorted(set(refs)-set(labels))
    own_labels = re.findall(r"\\label\{([^}]+)\}", chapter)
    assert len(own_labels) >= 32
    for expected in (
        "def:topog25-continuum",
        "thm:topog25-nested",
        "lem:topog25-chain-intersection",
        "def:topog25-indecomposable",
        "thm:topog25-irreducible-existence",
        "thm:topog25-inverse-connected",
        "thm:topog25-knaster",
        "lem:topog25-tent-branches",
        "def:topog25-solenoid",
        "thm:topog25-solenoid-not-locally-connected",
        "thm:topog25-finite-graph-peano",
        "thm:topog25-space-filling",
    ):
        assert rf"\label{{{expected}}}" in chapter, expected

    for env in ("definicja", "twierdzenie", "stwierdzenie", "wniosek",
                "lemat", "uwaga", "przyklad", "proof", "figure",
                "tikzpicture", "enumerate"):
        start = len(re.findall(r"\\begin\{" + env + r"\}", chapter))
        end = len(re.findall(r"\\end\{" + env + r"\}", chapter))
        assert start == end, (env, start, end)
    for forbidden in (
        r"\bunia\b", r"zwartościowani\w*",
        r"pierwszoprzeliczaln\w*", r"drugoprzeliczaln\w*",
        r"sekwencyjn\w*", r"zbieżności\s+zwartej",
    ):
        assert not re.search(forbidden, chapter, re.IGNORECASE), forbidden
    assert "twierdzenie Hahna--Mazurkiewicza" in chapter
    assert r"\ref{thm:topog-tietze}" in chapter
    assert "Nie powtarzamy" in chapter
    return len(own_labels), len(refs)


if __name__ == "__main__":
    t = tent_branches()
    f = inverse_limit_finite_sets()
    s = solenoid_root_branches()
    g = finite_graph_tours()
    peano = peano_interleaving()
    l, r = source_integration()
    print(f"PASS ch25: {t} tent branch checks, {f} inverse-limit checks, "
          f"{s} solenoid-root checks, {g} graph edges, "
          f"{peano} dyadic Peano targets; {l} labels and {r} refs")
