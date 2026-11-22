#!/usr/bin/env python3
"""Regression and finite-model checks for Chapter 18 on mapping spaces."""
from __future__ import annotations

import json
import re
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/18-przestrzenie-odwzorowan-i-topologia-zwarto-otwarta.tex"


def metric_models() -> int:
    """Test weighted compact-exhaustion metric on finite function models."""
    functions = list(product(range(3), repeat=3))
    levels = ((0,), (0, 1), (0, 1, 2))

    def dist(f, g):
        return sum(
            (2.0 ** (-i)) * max(min(1, abs(f[x] - g[x])) for x in K)
            for i, K in enumerate(levels, 1)
        )

    for f in functions:
        assert dist(f, f) == 0
        for g in functions:
            assert dist(f, g) == dist(g, f)
            if f != g:
                assert dist(f, g) > 0
            for h in functions:
                assert dist(f, h) <= dist(f, g) + dist(g, h) + 1e-12
    return len(functions) ** 3


def escaping_bump_models() -> int:
    """Translating compactly supported tents vanish on each bounded K."""
    samples = 0
    for M in range(1, 16):
        K = [x / 2 for x in range(-2*M, 2*M+1)]
        for n in range(M+3, M+7):
            vals = [max(1-abs(x-n), 0) for x in K]
            assert max(vals) == 0
            assert max(1-abs(n-n), 0) == 1
            samples += 1
    return samples



def nonhausdorff_finite_models() -> tuple[int, int]:
    """Compact-open and compact-uniform neighborhoods for all 3-point topologies.

    With a finite discrete metric target, both topologies are discrete
    on the continuous maps, even when the domain is not Hausdorff.
    """
    whole = frozenset(range(3))
    subsets = [frozenset(i for i in range(3) if (mask >> i) & 1)
               for mask in range(8)]
    checked_topologies = 0
    checked_maps = 0
    for mask in range(1 << 8):
        tau = {subsets[i] for i in range(8) if (mask >> i) & 1}
        if frozenset() not in tau or whole not in tau:
            continue
        if any(a & b not in tau or a | b not in tau
               for a in tau for b in tau):
            continue
        checked_topologies += 1
        maps = [
            f for f in product(range(2), repeat=3)
            if all(frozenset(x for x in range(3) if f[x] == value) in tau
                   for value in range(2))
        ]
        for f in maps:
            # Singleton K={x} is compact even for a non-Hausdorff X.
            # Intersect the three compact-open subbasic neighborhoods:
            # [{x},{f(x)}]. This must isolate f inside C(X,{0,1}).
            isolated = {
                g for g in maps
                if all(g[x] == f[x] for x in range(3))
            }
            # For d(a,b)=abs(a-b), the compact-uniform ball with
            # K=X and epsilon=1/2 isolates exactly the same map.
            uniform_ball = {
                g for g in maps
                if all(abs(f[x]-g[x]) < 0.5 for x in range(3))
            }
            assert isolated == uniform_ball == {f}
            checked_maps += 1
    assert checked_topologies == 29, checked_topologies
    return checked_topologies, checked_maps


def source_integrity() -> tuple[int, int]:
    text = (ROOT / CH).read_text(encoding="utf-8")
    entry = (ROOT / "books/pl/general_topology.tex").read_text(encoding="utf-8")
    standalone = (ROOT / "books/pl/general_topology_ch18.tex").read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in entry
    assert r"\input{../../" + CH + "}" in standalone
    assert r"\setcounter{chapter}{17}" in standalone
    required = (
        "def:topog-odwzorowania-Ck",
        "prop:topog-odwzorowania-oddzielanie",
        "prop:topog-odwzorowania-skladanie",
        "def:topog-odwzorowania-jednostajna-zwarte",
        "thm:topog-odwzorowania-zwarto-otwarta-jednostajna",
        "cor:topog-odwzorowania-sieci",
        "ex:topog-odwzorowania-gorki-uciekajace",
        "thm:topog-odwzorowania-ewaluacja",
        "thm:topog-odwzorowania-wykladnicze",
        "ex:topog-odwzorowania-ewaluacja-q",
        "thm:topog-odwzorowania-metryka-wyczerpanie",
        "thm:topog-odwzorowania-zupelnosc",
        "ex:topog-odwzorowania-nieprzeliczalna",
    )
    for label in required:
        assert r"\label{" + label + "}" in text, label
    for formula in (
        r"Jest to rzeczywiście otoczenie",
        r"Wykażemy ilościowo jednostajną",
        r"B_K(f,\varepsilon)",
        r"\operatorname{ev}",
        r"C_k(X,Y)",
        r"\widehat F",
        r"\rho_n(f,g)",
        r"\sup_{x\in K_n}",
    ):
        assert formula in text, formula

    for env in ("definicja", "lemat", "twierdzenie",
                "stwierdzenie", "wniosek", "przyklad", "uwaga",
                "proof"):
        assert text.count(r"\begin{" + env + "}") == text.count(
            r"\end{" + env + "}"), env

    obj = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(
        b["chapters"] for b in obj["books"] if b["id"] == "general_topology"
    )
    assert len(chapters) >= 18 and chapters[17] == CH
    joined = "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in chapters
    )
    labels = re.findall(r"\\label\{([^}]+)\}", joined)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", joined)
    assert len(labels) == len(set(labels)), "Repeated chapter labels"
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))
    forbidden = (
        r"zwartościowani\w*",
        r"zbieżnoś(?:ć|ci|cią)\s+zwart\w*",
        r"pierwszo-?przeliczaln\w*",
        r"drugoprzeliczaln\w*",
    )
    for expression in forbidden:
        assert not re.search(expression, text, re.I), expression
    return len(labels), len(refs)


if __name__ == "__main__":
    cases = metric_models()
    topologies, continuous_maps = nonhausdorff_finite_models()
    bumps = escaping_bump_models()
    labels, refs = source_integrity()
    print(
        "PASS ch18: weighted-metric triples=%d, escaping bumps=%d, "
        "topologies=%d, maps=%d, labels=%d, refs=%d"
        % (cases, bumps, topologies, continuous_maps, labels, refs)
    )
