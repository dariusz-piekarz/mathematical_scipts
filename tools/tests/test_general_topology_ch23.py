#!/usr/bin/env python3
"""Chapter 23: finite covers, Cantor coordinates and grid-triangulation checks.

Finite numerical models are regression tests, not replacements for the
infinite/compactness proofs in the manuscript.
"""
from __future__ import annotations

import json
import re
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/23-wymiar-topologiczny.tex"
BOOK = "books/pl/general_topology.tex"
ENTRY = "books/pl/general_topology_ch23.tex"


def zero_dim_finite_discrete() -> int:
    # For every finite discrete set X, test each set of nonempty opens
    # covering X. The singleton cover refines every such cover and has order 1.
    tested = 0
    for n in range(1, 5):
        whole = frozenset(range(n))
        subsets = [
            frozenset(s) for k in range(1, n + 1)
            for s in combinations(range(n), k)
        ]
        for cover_len in range(1, len(subsets) + 1):
            # All finite open covers, represented by bitmasks of subsets,
            # would give 2^(2^n-1) cases; sample at most 4 members.
            if cover_len > 4:
                break
            for cover in combinations(subsets, cover_len):
                if frozenset().union(*cover) != whole:
                    continue
                singletons = tuple(frozenset({x}) for x in whole)
                assert all(any(s <= u for u in cover) for s in singletons)
                assert all(len([s for s in singletons if x in s]) == 1
                           for x in whole)
                tested += 1
    return tested


def cantor_cylinders() -> int:
    samples = 0
    for length in range(1, 8):
        words = list(product((0, 1), repeat=length))
        for a in words:
            # Cylinders at fixed depth are disjoint and partition words.
            assert sum(tuple(w[:length]) == a for w in words) == 1
            samples += 1
        # Codes with first differing digit are injective at infinite depth:
        # minimal separation >= 3^(-index), as proved in the chapter.
        for a in words:
            for b in words:
                if a == b:
                    continue
                i = next(i for i, (x, y) in enumerate(zip(a, b))
                         if x != y) + 1
                finite_difference = abs(sum(
                    2 * (x - y) * 3 ** (-k)
                    for k, (x, y) in enumerate(zip(a, b), 1)
                ))
                assert finite_difference >= 3 ** (-i) - 1e-10
    return samples


def freudenthal_simplex() -> int:
    checked = 0
    for n in (1, 2, 3, 4):
        # Every point in [0,1]^n belongs to a simplex with n+1
        # vertices corresponding to the decreasing order of coordinates.
        values = (0., .2, .5, .8, 1.)
        for coords in product(values, repeat=n):
            order = sorted(range(n), key=lambda j: coords[j], reverse=True)
            ordered = [coords[j] for j in order]
            weights = [1 - ordered[0]]
            weights += [ordered[k] - ordered[k+1] for k in range(n-1)]
            weights += [ordered[-1]]
            vertices = [tuple([0] * n)]
            for index in order:
                next_vertex = list(vertices[-1])
                next_vertex[index] = 1
                vertices.append(tuple(next_vertex))
            assert len(vertices) == n + 1
            assert abs(sum(weights) - 1) < 1e-10
            assert all(x >= -1e-10 for x in weights)
            reconstructed = [
                sum(weights[i] * vertices[i][j] for i in range(n+1))
                for j in range(n)
            ]
            assert all(abs(x-y) < 1e-10 for x, y in zip(coords, reconstructed))
            assert sum(w > 1e-10 for w in weights) <= n+1
            checked += 1
    return checked


def interval_grid_overlap() -> int:
    checks = 0
    for h in (.05, .1, .2):
        centers = [k*h for k in range(-100, 101)]
        for m in range(-20, 21):
            x = m / 20.
            covered = [c for c in centers if abs(x-c) < h-1e-10]
            assert 1 <= len(covered) <= 2
            checks += 1
    return checks


def source_integration() -> tuple[int, int]:
    chapter = (ROOT / CH).read_text(encoding="utf-8")
    book = (ROOT / BOOK).read_text(encoding="utf-8")
    standalone = (ROOT / ENTRY).read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in book
    assert r"\input{../../" + CH + "}" in standalone
    assert r"\setcounter{chapter}{22}" in standalone
    assert r"\externaldocument{general_topology_ch07}" in standalone
    assert "rozdziały 01–22 stabilne; rozdział 23 w audycie" in book
    cat = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(x["chapters"] for x in cat["books"]
                    if x["id"] == "general_topology")
    assert len(chapters) >= 23 and chapters[22] == CH
    source = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in chapters)
    labels = re.findall(r"\\label\{([^}]+)\}", source)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)
    assert len(labels) == len(set(labels)), "Duplicate chapter labels"
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))
    for label in (
        "def:topog23-order", "def:topog23-dim",
        "prop:topog23-homeomorphism", "lem:topog23-closed-shrinking",
        "thm:topog23-closed-monotone", "thm:topog23-zero-clopen",
        "prop:topog23-zero-products", "ex:topog23-cantor",
        "thm:topog23-connected-positive", "def:topog23-ind",
        "def:topog23-Ind", "thm:topog23-three-zero",
        "lem:topog23-lebesgue-number", "thm:topog23-real-upper",
        "thm:topog23-interval", "def:topog23-nerve",
        "thm:topog23-canonical-nerve",
        "lem:topog23-grid-triangulation",
        "thm:topog23-euclidean-upper",
        "thm:topog23-cantor-surjection",
    ):
        assert rf"\label{{{label}}}" in chapter, label
    for env in (
        "definicja", "twierdzenie", "stwierdzenie", "lemat",
        "uwaga", "wniosek", "przyklad", "proof", "figure",
        "tikzpicture", "enumerate",
    ):
        assert chapter.count(r"\begin{" + env + "}") == chapter.count(
            r"\end{" + env + "}"), env
    for forbidden in (
        r"\bunia\b", r"zwartościowani\w*",
        r"pierwszo-?przeliczaln\w*", r"drugo-?przeliczaln\w*",
        r"zbieżności\s+zwartej",
    ):
        assert not re.search(forbidden, chapter, re.IGNORECASE), forbidden
    # This first installment proves the upper Euclidean bound, not the
    # general n-dimensional cube lower bound.
    assert "wymaga również dolnego oszacowania" in chapter
    assert "Nerwem" in chapter
    return len(labels), len(refs)


if __name__ == "__main__":
    f = zero_dim_finite_discrete()
    c = cantor_cylinders()
    t = freudenthal_simplex()
    g = interval_grid_overlap()
    labs, refs = source_integration()
    print(f"PASS ch23: {f} finite covers, {c} Cantor words, "
          f"{t} simplex points, {g} grid points, "
          f"{labs} labels and {refs} refs")
