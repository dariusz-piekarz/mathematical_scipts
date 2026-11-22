#!/usr/bin/env python3
"""Chapter 15: structural and finite-model tests of partition constructions."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex"
BOOK = ROOT / "books/pl/general_topology.tex"
STANDALONE = ROOT / "books/pl/general_topology_ch15.tex"


def test_telescoping() -> int:
    # Verify the finite product identity behind the partition of unity,
    # plus a cutoff equal to 1 enforcing all subsequent coefficients zero.
    tests = 0
    alphabet = (0.0, 0.125, 0.5, 0.875, 1.0)
    from itertools import product
    for values in product(alphabet, repeat=5):
        residual = 1.0
        terms = []
        for f in values:
            terms.append(f * residual)
            residual *= 1 - f
        assert abs(sum(terms) + residual - 1) < 1e-12
        assert all(0 <= t <= 1 for t in terms)
        for j, f in enumerate(values):
            if f == 1:
                assert all(v == 0 for v in terms[j + 1:])
                assert abs(sum(terms) - 1) < 1e-12
                break
        tests += 1
    return tests


def test_hat_partition() -> int:
    # h_n(x)=max(0,1-|x-n|), n in Z: finite-support partition of R.
    cases = 0
    for tick in range(-50, 51):
        x = tick / 7
        weights = [max(0.0, 1 - abs(x - n)) for n in range(-10, 11)]
        assert abs(sum(weights) - 1) < 1e-12, (tick, weights)
        assert sum(w > 0 for w in weights) <= 2
        cases += 1
    return cases


def test_stone_finite_discrete() -> int:
    """Enumerate finite open covers, checking Rudin's recursive balls.

    In the discrete metric, d(x,y)=1 for x!=y. At radius 2^-2,
    every 3r_n-ball is a singleton and admissible centers cover all X.
    """
    cases = 0
    for n in range(1, 5):
        universe = (1 << n) - 1
        opens = list(range(1, universe + 1))
        for mask in range(1, 1 << len(opens)):
            cover = [u for j, u in enumerate(opens) if (mask >> j) & 1]
            union = 0
            for u in cover:
                union |= u
            if union != universe:
                continue
            prior_centers: set[int] = set()
            result: list[tuple[int, int, frozenset[int]]] = []
            for level in range(1, 5):
                radius = 2 ** (-level)
                current_centers: set[int] = set()
                for alpha, u in enumerate(cover):
                    centers = set()
                    for x in range(n):
                        if x in prior_centers or not ((u >> x) & 1):
                            continue
                        if any(((v >> x) & 1) for v in cover[:alpha]):
                            continue
                        ball = {y for y in range(n)
                                if (0 if x == y else 1) < 3 * radius}
                        if all(((u >> y) & 1) for y in ball):
                            centers.add(x)
                    expanded = frozenset(
                        y for x in centers for y in range(n)
                        if (0 if x == y else 1) < radius
                    )
                    if expanded:
                        assert all((u >> y) & 1 for y in expanded)
                        result.append((level, alpha, expanded))
                    current_centers.update(centers)
                prior_centers.update(current_centers)
            assert set().union(*(part for _, _, part in result)) == set(range(n))
            # At each fixed level distinct alpha sets have distance >= 2^-level.
            for level in range(1, 5):
                layer = [(alpha, part) for lev, alpha, part in result if lev == level]
                for j, (_, a) in enumerate(layer):
                    for _, b in layer[j + 1:]:
                        assert a.isdisjoint(b)
            cases += 1
    return cases


def test_sources() -> tuple[int, int]:
    text = (ROOT / CH).read_text(encoding="utf-8")
    book = BOOK.read_text(encoding="utf-8")
    standalone = STANDALONE.read_text(encoding="utf-8")
    ref = r"\input{../../" + CH + "}"
    assert ref in book and ref in standalone
    assert r"\setcounter{chapter}{14}" in standalone
    for needle in (
        "def:topog-parazwartosc-lokalnie-skonczona",
        "def:topog-parazwartosc-definicja",
        "prop:topog-parazwartosc-domkniecia",
        "def:topog-parazwartosc-podzial",
        "prop:topog-parazwartosc-jednosc-pokrycie",
        "lem:topog-parazwartosc-odciecia",
        "thm:topog-parazwartosc-lindelof",
        "cor:topog-parazwartosc-klasy",
        "ex:topog-parazwartosc-prosta",
        "thm:topog-parazwartosc-stone",
        "def:topog-parazwartosc-sigma-lokalnie-skonczona-baza",
        "thm:topog-parazwartosc-nagata-smirnow",
        "rem:topog-parazwartosc-nagata-urysohn",
    ):
        assert rf"\label{{{needle}}}" in text, needle
    assert r"\prod_{j=1}^{n-1}(1-f_j)" in text
    assert r"\operatorname{supp}\varphi_n" in text
    assert r"E_{\alpha,n}" in text
    assert r"V_{\alpha,n}" in text
    assert r"2r_M<\rho" in text
    assert r"d(y,z)\ge3r_i" in text
    for formula in (
        r"\mathcal B=\bigcup_{n\ge1}\mathcal B_n",
        r"\overline{P_n}^{\,X}",
        r"F_n(G)=",
        r"f_{n,B}=2^{-n}g_B",
        r"F:X\to\ell^\infty(J)",
        r"\|F(y)-F(x)\|_\infty",
        r"\label{thm:topog-parazwartosc-nagata-smirnow}",
    ):
        assert formula in text, formula

    for env in ("twierdzenie", "lemat", "stwierdzenie", "wniosek",
                "definicja", "przyklad", "uwaga", "proof", "enumerate"):
        assert text.count(r"\begin{" + env + "}") == text.count(
            r"\end{" + env + "}"), env
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(b["chapters"] for b in catalog["books"] if b["id"]=="general_topology")
    assert chapters[-1] == CH and len(chapters) == 15
    all_text = "\n".join((ROOT / c).read_text(encoding="utf-8") for c in chapters)
    labels = re.findall(r"\\label\{([^}]+)\}", all_text)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", all_text)
    assert len(labels) == len(set(labels))
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))
    assert not re.search(r"zwartościowani\w*|zbieżności\s+zwartej", text, re.I)
    return len(labels), len(refs)


if __name__ == "__main__":
    finite = test_stone_finite_discrete()
    n = test_telescoping()
    m = test_hat_partition()
    labels, refs = test_sources()
    print(f"PASS chapter 15 Stone finite covers={finite}, telescoping={n}, hat={m}, labels={labels}, refs={refs}")
