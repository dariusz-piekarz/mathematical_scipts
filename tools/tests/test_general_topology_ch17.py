#!/usr/bin/env python3
"""Chapter 17: Aleksandrow and Čech–Stone compactification regressions."""
from __future__ import annotations

import json
import re
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex"

def finite_cofinite_neighborhoods() -> int:
    """Check algebra of cofinite neighborhoods in a finite set model."""
    base = set(range(6))
    finite_sets = [frozenset(c) for k in range(7)
                   for c in combinations(base, k)]
    # Intersections of neighborhoods N_F = {∞} ∪ (N\F)
    # correspond to unions of finite forbidden sets.
    for a in finite_sets:
        for b in finite_sets:
            assert a | b in finite_sets
            assert a & b in finite_sets
            assert (base - a) & (base - b) == base - (a | b)
            assert (base - a) | (base - b) == base - (a & b)
    return len(finite_sets)

def finite_discrete_stone_cech() -> int:
    """A finite discrete X is its own βX; indicator coordinates separate."""
    for n in range(1, 7):
        indicators = list(range(1 << n))
        profiles = [
            tuple((mask >> x) & 1 for mask in indicators)
            for x in range(n)
        ]
        assert len(set(profiles)) == n
        assert all(profiles[x] != profiles[y]
                   for x in range(n) for y in range(x+1, n))
    return 6

def sources() -> tuple[int, int]:
    src = (ROOT/CH).read_text(encoding="utf-8")
    entry = (ROOT/"books/pl/general_topology.tex").read_text(encoding="utf-8")
    standalone = (ROOT/"books/pl/general_topology_ch17.tex").read_text(encoding="utf-8")
    assert r"\input{../../"+CH+"}" in entry
    assert r"\input{../../"+CH+"}" in standalone
    assert r"\setcounter{chapter}{16}" in standalone
    required = (
        "def:topog-uzwarcenia-aleksandrow",
        "lem:topog-uzwarcenia-aleksandrow-topologia",
        "thm:topog-uzwarcenia-aleksandrow-kryterium",
        "thm:topog-uzwarcenia-aleksandrow-proper",
        "thm:topog-uzwarcenia-aleksandrow-minimalne",
        "cor:topog-uzwarcenia-aleksandrow-jednoznacznosc",
        "lem:topog-uzwarcenia-lokalna-tych",
        "def:topog-uzwarcenia-cech-stone",
        "thm:topog-uzwarcenia-cech-stone-uniwersalne",
        "cor:topog-uzwarcenia-cech-stone-funkcje",
        "thm:topog-uzwarcenia-cech-stone-maksymalne",
        "cor:topog-uzwarcenia-krance",
        "ex:topog-uzwarcenia-beta-n",
    )
    for label in required:
        assert r"\label{"+label+"}" in src, label
    assert r"\Phi(z)_g=z_{g\circ f}" in src
    assert r"\widehat f=e_L^{-1}\circ\Phi" in src
    assert r"\pi_f\colon[0,1]^I\to[0,1]" in src
    assert r"\lim_{t\to-\infty}2\arctan t=-\pi" in src
    assert r"\lim_{t\to+\infty}2\arctan t=\pi" in src
    assert r"\widetilde e^{-1}(V)" in src
    assert r"(X^\ast,\iota)\preccurlyeq(K,e)" in src
    for env in ("definicja","lemat","twierdzenie","wniosek",
                "przyklad","uwaga","proof","enumerate"):
        assert src.count(r"\begin{"+env+"}") == src.count(r"\end{"+env+"}"), env
    data=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    chapters=next(b["chapters"] for b in data["books"] if b["id"]=="general_topology")
    assert len(chapters)==17 and chapters[16]==CH
    joined="\n".join((ROOT/c).read_text(encoding="utf-8") for c in chapters)
    labels=re.findall(r"\\label\{([^}]+)\}",joined)
    refs=re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",joined)
    assert len(labels)==len(set(labels)), "duplicate label"
    assert set(refs)<=set(labels), sorted(set(refs)-set(labels))
    assert not re.search(r"zwartościowani|zbieżności\s+zwartej",src,re.I)
    return len(labels),len(refs)

if __name__=="__main__":
    n=finite_cofinite_neighborhoods()
    k=finite_discrete_stone_cech()
    labels,refs=sources()
    print(f"PASS ch17 cofinite models={n}; finite βX={k}; labels={labels}; refs={refs}")
