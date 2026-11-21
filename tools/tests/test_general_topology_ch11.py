#!/usr/bin/env python3
"""Chapter 11 regression checks.

Finite models verify the Baire property in the finite case.
They are not a proof of the infinite Baire category theorem:
the written proof needs a separate mathematical audit.
"""
from __future__ import annotations

from itertools import combinations
from math import isclose, pi, tan
from pathlib import Path
import re

from test_general_topology_ch07 import all_topologies

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex"
BOOK = ROOT / "books/pl/general_topology.tex"
STANDALONE = ROOT / "books/pl/general_topology_ch11.tex"


def closure(tau: set[int], n: int, a: int) -> int:
    universe = (1 << n) - 1
    closed = [universe ^ u for u in tau]
    result = universe
    for f in closed:
        if (f & a) == a:
            result &= f
    return result


def finite_baire_checks() -> tuple[int, int]:
    spaces = dense = 0
    for n in range(5):
        universe = (1 << n) - 1
        for family in all_topologies(n):
            tau = set(family)
            spaces += 1
            dense_open = [u for u in tau if closure(tau, n, u) == universe]
            intersection = universe
            for u in dense_open:
                intersection &= u
            assert closure(tau, n, intersection) == universe, (n, tau)
            dense += len(dense_open)
            nowhere = {
                a for a in range(1 << n)
                if not any(u and (u & closure(tau, n, a)) == u for u in tau)
            }
            union = 0
            for a in nowhere:
                union |= a
            assert not any(u and (u & union) == u for u in tau), (n, tau)
    assert spaces == 390
    return spaces, dense


def pullback_metric() -> int:
    grid = [0.1, 0.2, 0.35, 0.5, 0.7, 0.9]
    h = lambda x: tan(pi * (x - 0.5))
    d = lambda x, y: abs(h(x) - h(y))
    cases = 0
    for x in grid:
        assert d(x, x) == 0
        for y in grid:
            assert (d(x, y) > 0) == (x != y)
            assert isclose(d(x, y), d(y, x))
            for z in grid:
                assert d(x, z) <= d(x, y) + d(y, z) + 1e-12
                cases += 1
    return cases


def lint() -> tuple[int, int]:
    src = SRC.read_text(encoding="utf-8")
    book = BOOK.read_text(encoding="utf-8")
    standalone = STANDALONE.read_text(encoding="utf-8")
    assert src.startswith(r"\chapter{Zupełność przestrzeni metrycznych")
    expected = r"\input{../../chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex}"
    assert expected in book
    assert expected in standalone
    assert r"\setcounter{chapter}{10}" in standalone
    expected_labels = [
        "ch:topog-baire", "def:topog-baire-ciag-cauchyego",
        "thm:topog-baire-podprzestrzen-zupelna",
        "prop:topog-baire-rownowaznosci",
        "thm:topog-baire-metryczne",
        "thm:topog-baire-lokalnie-zwarte",
        "thm:topog-baire-wymierne-nie-gdelta",
        "cor:topog-baire-domkniete",
    ]
    for label in expected_labels:
        assert rf"\label{{{label}}}" in src, label
    for env in ("twierdzenie", "lemat", "stwierdzenie", "wniosek",
                "definicja", "przyklad", "uwaga", "proof",
                "figure", "tikzpicture"):
        assert src.count(r"\begin{" + env + "}") == src.count(
            r"\end{" + env + "}"), env
    labels = re.findall(r"\\label\{([^}]+)\}", src)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", src)
    assert len(labels) == len(set(labels)), "duplicate labels"
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))
    assert r"\overline W^{\,X}=\overline H^{\,K}" in src
    assert r"$K_1\supseteq K_2\supseteq\cdots$" in src
    assert r"$\Q$ jest pierwszej kategorii w sobie" in src
    assert not re.search(r"\b(?:sekwencj\w*|tensorowanie|zwartościowani\w*)\b", src, re.I)
    assert not re.search(r"\b(?:pierwszoprzeliczaln\w*|drugoprzeliczaln\w*)\b", src, re.I)
    return len(labels), len(refs)


if __name__ == "__main__":
    spaces, dense = finite_baire_checks()
    metric_cases = pullback_metric()
    labels, refs = lint()
    print(f"PASS Chapter 11: finite spaces={spaces}; dense open sets={dense}; "
          f"pullback-metric triples={metric_cases}; labels={labels}; refs={refs}")
