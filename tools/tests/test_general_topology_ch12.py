#!/usr/bin/env python3
"""Chapter 12: finite uniformities, metric examples, and LaTeX integration.

Finite checks do not replace mathematical proofs for arbitrary products,
nets, filters, or compact metric spaces.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = "chapters/pl/general_topology/12-przestrzenie-jednostajne.tex"
BOOK = ROOT / "books/pl/general_topology.tex"
STANDALONE = ROOT / "books/pl/general_topology_ch12.tex"
CATALOG = ROOT / "catalog/books.json"
PLAN = ROOT / "docs/pl/plan_topologii_ogolnej.md"


def set_partitions(n: int):
    """Canonical restricted-growth strings for all partitions of {0,...,n-1}."""
    if n == 0:
        yield ()
        return

    def walk(prefix: tuple[int, ...], k: int):
        if len(prefix) == n:
            yield prefix
            return
        for j in range(k + 2):
            yield from walk(prefix + (j,), max(k, j))

    yield from walk((0,), 0)


def compose(e: set[tuple[int, int]], f: set[tuple[int, int]], n: int):
    return {(i, k) for i in range(n) for j in range(n) for k in range(n)
            if (i, j) in e and (j, k) in f}


def finite_uniformity_models() -> int:
    cases = 0
    for n in range(5):
        diag = {(i, i) for i in range(n)}
        whole = set(product(range(n), repeat=2))
        for partition in set_partitions(n):
            relation = {(i, j) for i in range(n) for j in range(n)
                        if partition[i] == partition[j]}
            assert diag <= relation <= whole
            assert {(j, i) for i, j in relation} == relation
            assert compose(relation, relation, n) == relation
            # Principal entourage filter of an equivalence relation.
            # Every E containing R is an entourage, and R circ R = R.
            open_sets = [
                subset for subset in range(1 << n)
                if all((i, j) not in relation or not (subset & (1 << i))
                       or subset & (1 << j)
                       for i in range(n) for j in range(n))
            ]
            # Open sets are precisely unions of equivalence classes.
            for subset in open_sets:
                for i in range(n):
                    if subset & (1 << i):
                        assert all((i, j) not in relation
                                   or subset & (1 << j) for j in range(n))
            assert (len(open_sets) == 2 ** (max(partition) + 1)
                    if partition else len(open_sets) == 1)
            cases += 1
    assert cases == 24  # Bell numbers B(0)+...+B(4)
    return cases


def pseudometric_examples() -> int:
    checks = 0
    for n in range(1, 7):
        # Pseudometric identifying points of the same parity.
        p = lambda i, j: abs((i % 2) - (j % 2))
        for i in range(n):
            for j in range(n):
                assert p(i, j) == p(j, i)
                assert p(i, i) == 0
                for k in range(n):
                    assert p(i, k) <= p(i, j) + p(j, k)
                    checks += 1
        e_half = {(i, j) for i in range(n) for j in range(n)
                  if p(i, j) < .5}
        e_onehalf = {(i, j) for i in range(n) for j in range(n)
                     if p(i, j) < 1.5}
        assert compose(e_half, e_half, n) <= e_half
        assert e_half <= e_onehalf
        # A map f(i)=i mod 2 is uniformly continuous to discrete {0,1}.
        f = lambda i: i % 2
        assert all(f(i) == f(j) for i, j in e_half)
        if n > 2:
            # f(i)=i is not uniformly continuous from this pseudometric
            # to the discrete metric: p(0,2)=0, but 0 != 2.
            assert (0, 2) in e_half
    return checks


def product_examples() -> int:
    # For the product of two discrete finite spaces, basic entourages
    # constrain both coordinates and give the discrete product topology.
    n = 0
    for a, b in product(range(2), range(3)):
        for c, d in product(range(2), range(3)):
            in_a = a == c
            in_b = b == d
            in_product_diagonal = ((a, b) == (c, d))
            assert (in_a and in_b) == in_product_diagonal
            n += 1
    return n


def lint() -> tuple[int, int]:
    source = (ROOT / CHAPTER).read_text(encoding="utf-8")
    book = BOOK.read_text(encoding="utf-8")
    standalone = STANDALONE.read_text(encoding="utf-8")
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    plan = PLAN.read_text(encoding="utf-8")
    assert source.startswith(r"\chapter{Przestrzenie jednostajne")
    assert r"\setcounter{chapter}{11}" in standalone
    expected = r"\input{../../" + CHAPTER + "}"
    assert expected in book and expected in standalone
    target = next(b for b in catalog["books"] if b["id"] == "general_topology")
    assert target["chapters"][-1] == CHAPTER
    assert target["entrypoint"] == "books/pl/general_topology.tex"
    assert "zbieżności jednostajnej na zbiorach zwartych" in plan
    assert "uzwarcenie Čecha–Stone’a" in plan

    for env in ("twierdzenie", "lemat", "stwierdzenie", "wniosek",
                "definicja", "przyklad", "uwaga", "proof",
                "figure", "tikzpicture"):
        assert source.count(r"\begin{" + env + "}") == source.count(
            r"\end{" + env + "}"), env
    all_labels = []
    all_refs = []
    for chapter in target["chapters"]:
        tex = (ROOT / chapter).read_text(encoding="utf-8")
        all_labels += re.findall(r"\\label\{([^}]+)\}", tex)
        all_refs += re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", tex)
        assert not re.search(r"zwartościowani\w*|zbieżności\s+zwartej",
                             tex, flags=re.I), chapter
    assert len(all_labels) == len(set(all_labels)), "Duplicate labels"
    assert set(all_refs) <= set(all_labels), "Missing labels"
    assert r"\label{thm:topog-jednostajne-topologia}" in source
    assert r"\label{thm:topog-jednostajne-hausdorff}" in source
    assert r"\label{thm:topog-jednostajne-iloczyn}" in source
    assert r"\label{thm:topog-jednostajne-ogony}" in source
    assert r"\label{lem:topog-jednostajne-zwarta-ciagowa}" in source
    assert r"\ref{thm:topog-zwartosc-fip}" in source
    assert r"\label{thm:topog-jednostajne-heine-cantor}" in source
    return len(all_labels), len(all_refs)


if __name__ == "__main__":
    partitions = finite_uniformity_models()
    pseudo = pseudometric_examples()
    products = product_examples()
    labels, refs = lint()
    print(f"PASS Chapter 12: partition uniformities={partitions}; "
          f"pseudometric triangle tests={pseudo}; product cases={products}; "
          f"global labels={labels}; references={refs}")
