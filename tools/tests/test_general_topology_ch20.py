#!/usr/bin/env python3
"""Topologia ogólna, rozdział 20: Suslin, analytic sets and no overlap."""
from __future__ import annotations

from itertools import product
from pathlib import Path
from random import Random
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex"
BOOK = "books/pl/general_topology.tex"
STANDALONE = "books/pl/general_topology_ch20.tex"


def finite_suslin_models() -> int:
    """Finite-depth identity: projections versus branches through closed sections.

    All subsets of a finite discrete space are closed. Test reconstruction
    of the sets F_s from a relation H, including empty and full relations.
    This does not prove the infinite Suslin theorem.
    """
    rng = Random(20261122)
    words = list(product((0, 1), repeat=4))
    points = range(3)
    pairs = list(product(points, words))
    samples = [set(), set(pairs)]
    samples += [
        {item for item in pairs if rng.getrandbits(1)}
        for _ in range(512)
    ]
    for relation in samples:
        closed_prefixes: dict[tuple[int, ...], set[int]] = {}
        for length in range(1, 5):
            for s in product((0, 1), repeat=length):
                closed_prefixes[s] = {
                    x for x, word in relation if word[:length] == s
                }
        suslin = {
            x for x in points
            if any(
                all(x in closed_prefixes[word[:length]]
                    for length in range(1, 5))
                for word in words
            )
        }
        projection = {x for x, _ in relation}
        assert suslin == projection, (suslin, projection)
    return len(samples)


def projection_not_closed_model() -> None:
    """Sample points (x,1/x) lie in the closed hyperbola, projection excludes 0."""
    for x in (-2.0, -0.5, 0.1, 0.25, 1.0, 3.0):
        y = 1 / x
        assert abs(x * y - 1.0) < 1e-12
    assert all(x != 0.0 for x in (-2.0, -0.5, 0.1, 0.25, 1.0, 3.0))


def integration_and_source() -> tuple[int, int]:
    text = (ROOT / CH).read_text(encoding="utf-8")
    book = (ROOT / BOOK).read_text(encoding="utf-8")
    stand = (ROOT / STANDALONE).read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in book
    assert r"\input{../../" + CH + "}" in stand
    assert r"\setcounter{chapter}{19}" in stand

    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(
        item["chapters"] for item in catalog["books"]
        if item["id"] == "general_topology"
    )
    assert len(chapters) == 20 and chapters[-1] == CH
    assert len(chapters) == len(set(chapters))

    all_text = "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in chapters
    )
    labels = re.findall(r"\\label\{([^}]+)\}", all_text)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", all_text)
    assert len(labels) == len(set(labels))
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))

    for label in (
        "lem:topog20-surjection",
        "def:topog20-analityczny",
        "thm:topog20-rzut",
        "thm:topog20-closure",
        "cor:topog20-borel",
        "def:topog20-suslin",
        "thm:topog20-suslin",
        "lem:topog20-universal",
        "thm:topog20-nonborel",
        "cor:topog20-projection",
    ):
        assert rf"\label{{{label}}}" in text, label

    for env in ("twierdzenie", "lemat", "definicja",
                "stwierdzenie", "wniosek", "uwaga", "przyklad", "proof"):
        assert text.count(r"\begin{" + env + "}") == text.count(
            r"\end{" + env + "}"), env

    for forbidden in (
        r"zwartościowani\w*",
        r"zbieżnoś(?:ć|ci|cią)\s+zwart\w*",
        r"pierwszo-?przeliczaln\w*",
        r"drugo-?przeliczaln\w*",
        r"\bunia\b",
    ):
        assert not re.search(forbidden, text, re.I), forbidden
    assert "redukcjom Wadge'a" in text
    assert r"\emph{nie} stanowi" in text and "mierzalności" in text
    return len(labels), len(refs)


if __name__ == "__main__":
    models = finite_suslin_models()
    projection_not_closed_model()
    labels, refs = integration_and_source()
    print(f"PASS general topology ch20: {models} finite Suslin relations, "
          f"projection example, {labels} labels, {refs} refs")
