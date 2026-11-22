#!/usr/bin/env python3
"""Chapter 19: Polish spaces, G_delta, Borel sigma algebra and hierarchy."""
from __future__ import annotations

import json
import re
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/19-przestrzenie-polskie-i-zbiory-borelowskie.tex"


def finite_borel_models() -> tuple[int, int]:
    """Enumerate all three-point topologies, generated sigma-algebras and traces."""
    points = frozenset(range(3))
    subs = [frozenset(i for i in points if mask & (1 << i))
            for mask in range(8)]

    def sigma_closure(family):
        family = set(family) | {frozenset(), points}
        while True:
            expanded = family | {points - a for a in family}
            expanded |= {a | b for a in expanded for b in expanded}
            if expanded == family:
                return family
            family = expanded

    n_topologies = 0
    n_traces = 0
    for mask in range(1 << 8):
        tau = {subs[i] for i in range(8) if mask & (1 << i)}
        if frozenset() not in tau or points not in tau:
            continue
        if any((a | b) not in tau or (a & b) not in tau
               for a in tau for b in tau):
            continue
        n_topologies += 1
        borel = sigma_closure(tau)
        for a in subs:
            tau_a = {a & u for u in tau}
            # Sigma-algebra on A computed independently, not by trace.
            rel = {frozenset(), a} | tau_a
            while True:
                expanded = rel | {a - q for q in rel}
                expanded |= {q | z for q in expanded for z in expanded}
                if expanded == rel:
                    break
                rel = expanded
            trace = {a & z for z in borel}
            assert trace == rel, (tau, a)
            n_traces += 1
    assert n_topologies == 29
    assert n_traces == 29 * 8
    return n_topologies, n_traces


def cantor_ultrametric_models() -> int:
    """Check ultrametric inequality for all binary words of length four."""
    words = list(product((0, 1), repeat=4))

    def dist(x, y):
        for k, (a, b) in enumerate(zip(x, y), 1):
            if a != b:
                return 2.0 ** -k
        return 0.0

    for x in words:
        for y in words:
            assert dist(x, y) == dist(y, x)
            assert (dist(x, y) == 0) == (x == y)
            for z in words:
                assert dist(x, z) <= max(dist(x, y), dist(y, z))
    return len(words) ** 3


def gdelta_boundary_metric_models() -> int:
    """Reciprocal distance prevents a Cauchy sequence from escaping (0,1).

    This is a finite numerical model of the complete metric built
    for G_delta sets: U_1=(0,infinity), U_2=(-infinity,1).
    """
    def rho(x, y):
        return (
            abs(x-y)
            + 0.5 * min(1.0, abs(1/x-1/y))
            + 0.25 * min(1.0, abs(1/(1-x)-1/(1-y)))
        )
    for n in range(2, 102):
        x, y = 1.0/n, 1.0/(2*n)
        assert rho(x, y) >= 0.5
        assert abs(x-y) < 1.0/n
    return 100


def check_source() -> tuple[int, int]:
    text = (ROOT / CH).read_text(encoding="utf-8")
    full = (ROOT / "books/pl/general_topology.tex").read_text(encoding="utf-8")
    entry = (ROOT / "books/pl/general_topology_ch19.tex").read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in full
    assert r"\input{../../" + CH + "}" in entry
    assert r"\setcounter{chapter}{18}" in entry

    names = (
        "def:topog-polskie",
        "prop:topog-polskie-drugi-aksjomat",
        "ex:topog-polskie-cantor-baire",
        "thm:topog-polskie-iloczyn",
        "def:topog-polskie-fsigma-gdelta",
        "lem:topog-polskie-otwarte-fsigma",
        "thm:topog-polskie-gdelta",
        "ex:topog-polskie-wymierne",
        "def:topog-polskie-borel",
        "prop:topog-polskie-borel-slad",
        "prop:topog-polskie-borel-przeliczalna-baza",
        "def:topog-polskie-odwzorowanie-borelowskie",
        "prop:topog-polskie-borelowskie-kryterium",
        "def:topog-polskie-hierarchia-skonczona",
        "prop:topog-polskie-hierarchia-wlasnosci",
        "def:topog-polskie-hierarchia-porzadkowa",
        "thm:topog-polskie-borel-wyczerpanie",
    )
    for name in names:
        assert r"\label{" + name + "}" in text, name
    for necessary in (
        r"\boldsymbol\Sigma^0_\alpha",
        r"\boldsymbol\Pi^0_{\alpha_n+1}",
        r"\omega_1",
        r"\operatorname{diam}_{\sigma}",
        r"\rho(x,y)=",
        r"\mathcal B(A)=",
        r"\mathcal B(X)=",
        "metryzowalną",
        "nie należy utożsamiać",
    ):
        assert necessary.lower() in text.lower(), necessary

    for fragment in (
        r"$\rho(x_j,x)<\varepsilon$.",
        r"$\sigma(a_m,a_l)<2^{-n}<\varepsilon$",
        "dla dowolnych",
        r"\boldsymbol\Pi^0_{\alpha_n+1}",
    ):
        assert fragment in text, fragment

    for env in ("definicja", "twierdzenie", "lemat", "stwierdzenie",
                "przyklad", "uwaga", "proof"):
        assert text.count(r"\begin{" + env + "}") == text.count(
            r"\end{" + env + "}"), env

    data = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(
        b["chapters"] for b in data["books"] if b["id"] == "general_topology"
    )
    assert len(chapters) == 19 and chapters[18] == CH
    joined = "\n".join((ROOT / p).read_text(encoding="utf-8")
                       for p in chapters)
    labels = re.findall(r"\\label\{([^}]+)\}", joined)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", joined)
    assert len(labels) == len(set(labels)), "duplicate labels"
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))
    for forbidden in (
        r"zwartościowani\w*",
        r"zbieżnoś(?:ć|ci|cią)\s+zwart\w*",
        r"pierwszo-?przeliczaln\w*",
        r"drugoprzeliczaln\w*",
    ):
        assert not re.search(forbidden, text, re.I), forbidden
    return len(labels), len(refs)


if __name__ == "__main__":
    topologies, traces = finite_borel_models()
    triples = cantor_ultrametric_models()
    boundary = gdelta_boundary_metric_models()
    labels, refs = check_source()
    print("PASS ch19: finite topologies=%d, Borel traces=%d, "
          "Cantor ultrametric triples=%d, G-delta boundary cases=%d, labels=%d, refs=%d"
          % (topologies, traces, triples, boundary, labels, refs))
