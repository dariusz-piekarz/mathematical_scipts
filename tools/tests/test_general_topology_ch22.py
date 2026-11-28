#!/usr/bin/env python3
"""Finite-model and source regression for general topology, Chapter 22.

Computational checks validate finite examples only. They do not constitute
proofs of the general theorems about infinite or noncompact metric spaces.
"""
from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import json
import math
import re

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex"
BOOK = "books/pl/general_topology.tex"
ENTRY = "books/pl/general_topology_ch22.tex"


def finite_kuratowski_models() -> int:
    """In a finite discrete topology: Li = eventually always, Ls = infinitely often."""
    X = (0, 1, 2)
    subsets = [frozenset(c) for k in range(4) for c in combinations(X, k)]
    count = 0
    # Eventually periodic families: prefix followed by an infinitely repeated cycle.
    for prefix in product(subsets, repeat=2):
        for period in product(subsets, repeat=2):
            li = frozenset(x for x in X if all(x in a for a in period))
            ls = frozenset(x for x in X if any(x in a for a in period))
            assert li <= ls
            assert all(x in li for x in X if all(x in a for a in period))
            assert all(x in ls for x in X if any(x in a for a in period))
            assert all(x not in ls for x in X if all(x not in a for a in period))
            if period == (frozenset({0}), frozenset({1})):
                assert li == frozenset() and ls == frozenset({0, 1})
            count += 1
    return count


def simple_hausdorff(a: set[float], b: set[float]) -> float:
    return max(
        max(min(abs(x - y) for y in b) for x in a),
        max(min(abs(y - x) for x in a) for y in b),
    )


def proper_real_escape() -> int:
    checks = 0
    for m in range(1, 7):
        for n in range(2 * m + 1, 2 * m + 9):
            # On [-m,m], distance to {0,n} equals distance to {0}.
            for t in range(-10 * m, 10 * m + 1):
                x = t / 10
                assert min(abs(x), abs(x - n)) == abs(x)
                checks += 1
            assert simple_hausdorff({0, float(n)}, {0}) == n
    return checks


def discrete_wijsman_aw() -> int:
    # Equidistant countable discrete X, F_n=X\{n}, F=X.
    X = set(range(1, 301))
    for n in range(1, 151):
        fn = X - {n}
        assert fn
        # At the removed point, the distance differs by one.
        assert min(0 if n == k else 1 for k in fn) == 1
        for fixed in range(1, 31):
            if n > fixed:
                assert fixed in fn  # Pointwise Wijsman eventual equality.
    return 150


def nonproper_local_compact_counterexample() -> int:
    # p=0, q=1, y_k=k+1; all distinct distances 1 except d(p,q)=2.
    points = tuple(range(0, 25))
    def d(i: int, j: int) -> int:
        return 0 if i == j else (2 if {i, j} == {0, 1} else 1)

    tri = 0
    for a, b, c in product(points, repeat=3):
        assert d(a, c) <= d(a, b) + d(b, c)
        tri += 1
    for y in range(2, 25):
        fn = {0, y}
        f = {0}
        assert min(d(1, z) for z in fn) == 1
        assert min(d(1, z) for z in f) == 2
    return tri


def source_integration() -> tuple[int, int]:
    chapter = (ROOT / CH).read_text(encoding="utf-8")
    book = (ROOT / BOOK).read_text(encoding="utf-8")
    standalone = (ROOT / ENTRY).read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in book
    assert r"\input{../../" + CH + "}" in standalone
    assert r"\setcounter{chapter}{21}" in standalone
    for i in ("14", "21"):
        assert rf"\externaldocument{{general_topology_ch{i}}}" in standalone
    stable = re.search(r"rozdziały 01–(\d+) stabilne", book)
    assert stable and int(stable.group(1)) >= 22

    cat = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(
        item["chapters"] for item in cat["books"]
        if item["id"] == "general_topology"
    )
    assert len(chapters) >= 22 and chapters[21] == CH
    assert len(chapters) == len(set(chapters))
    entire = "\n".join(
        (ROOT / src).read_text(encoding="utf-8") for src in chapters
    )
    labels = re.findall(r"\\label\{([^}]+)\}", entire)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", entire)
    assert len(labels) == len(set(labels)), "Duplicate LaTeX labels"
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))

    for name in (
        "def:topog22-kuratowski",
        "prop:topog22-kuratowski-dist",
        "def:topog22-wijsman",
        "thm:topog22-wijsman-metrizable",
        "thm:topog22-wijsman-kuratowski",
        "prop:topog22-wijsman-fell",
        "def:topog22-aw",
        "thm:topog22-aw-metric",
        "prop:topog22-aw-wijsman",
        "def:topog22-proper",
        "thm:topog22-proper-wijsman-aw",
        "thm:topog22-fell-kuratowski",
        "thm:topog22-proper-equivalences",
        "ex:topog22-nonproper",
        "ex:topog22-strict-aw",
    ):
        assert rf"\label{{{name}}}" in chapter, name
    for env in ("twierdzenie", "lemat", "stwierdzenie", "wniosek",
                "definicja", "przyklad", "uwaga", "proof", "figure"):
        assert chapter.count(r"\begin{" + env + "}") == chapter.count(
            r"\end{" + env + "}"), env

    for forbidden in (
        r"zwartościowani\w*",
        r"zbieżnoś(?:ć|ci|cią)\s+zwart\w*",
        r"pierwszo-?przeliczaln\w*",
        r"drugo-?przeliczaln\w*",
        r"\bunia\b",
    ):
        assert not re.search(forbidden, chapter, re.IGNORECASE), forbidden

    # Scope: important distinction between Fella allowing empty and
    # Wijsman/AW restricting to nonempty closed subsets.
    assert r"\mathcal F_*(X)" in chapter
    assert r"d(x,\varnothing)=+\infty" in chapter
    assert "lokalnie zwartą" in chapter
    assert r"\overline B_d(x,r)" in chapter
    return len(labels), len(refs)


if __name__ == "__main__":
    k = finite_kuratowski_models()
    real = proper_real_escape()
    dis = discrete_wijsman_aw()
    np = nonproper_local_compact_counterexample()
    labs, refs = source_integration()
    print(
        f"PASS general topology ch22: {k} finite Kuratowski patterns, "
        f"{real} proper real distance checks, {dis} Wijsman/AW checks, "
        f"{np} nonproper triangle checks, {labs} labels, {refs} refs"
    )
