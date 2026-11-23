#!/usr/bin/env python3
"""Chapter 21: finite hyperspace models, Hausdorff distance, integration."""
from __future__ import annotations

import json
import re
from itertools import combinations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/21-topologie-na-rodzinach-podzbiorow.tex"
BOOK = "books/pl/general_topology.tex"
STANDALONE = "books/pl/general_topology_ch21.tex"


def subsets(values: tuple[int, ...], include_empty: bool):
    start = 0 if include_empty else 1
    return [
        frozenset(s)
        for k in range(start, len(values) + 1)
        for s in combinations(values, k)
    ]


def hdist(a: frozenset[int], b: frozenset[int]) -> int:
    # The ambient metric is |x-y| on the discrete finite subspace of R.
    directed_ab = max(min(abs(x - y) for y in b) for x in a)
    directed_ba = max(min(abs(x - y) for x in a) for y in b)
    return max(directed_ab, directed_ba)


def finite_hausdorff_models() -> int:
    tests = 0
    for points in ((0,), (0, 1), (0, 2, 5), (-3, 0, 2, 7)):
        compact = subsets(points, include_empty=False)
        for a in compact:
            assert hdist(a, a) == 0
            for b in compact:
                assert hdist(a, b) == hdist(b, a)
                assert (hdist(a, b) == 0) == (a == b)
                for c in compact:
                    assert hdist(a, c) <= hdist(a, b) + hdist(b, c)
                    tests += 1
    return tests


def finite_vietoris_fell_models() -> int:
    count = 0
    for points in ((0,), (0, 1), (0, 1, 2), (0, 2, 5, 7)):
        all_closed = subsets(points, include_empty=True)
        nonempty = subsets(points, include_empty=False)
        whole = frozenset(points)
        # In a finite discrete space each Vietoris singleton is isolated
        # by its hit constraints for members and an upper condition.
        for k in nonempty:
            isolated_vietoris = {
                a for a in nonempty
                if a <= k and all(a & {x} for x in k)
            }
            assert isolated_vietoris == {k}
            # The Fell hit-and-miss constraints isolate exactly k as well.
            isolated_fell = {
                f for f in all_closed
                if all(f & {x} for x in k) and not (f & (whole - k))
            }
            assert isolated_fell == {k}
            count += 1
        # The Fell empty set is isolated for compact X:
        assert {f for f in all_closed if not (f & whole)} == {frozenset()}
        count += 1
    return count


def escaping_sets() -> None:
    # Fell on R admits the empty limit and forgets distant points;
    # Hausdorff distance keeps the distant points visible.
    fixed = frozenset({0})
    for n in range(1, 101):
        moving = frozenset({0, n})
        assert hdist(moving, fixed) == n
        if n > 10:
            # Every fixed compact interval [-10,10] is eventually
            # missed by the escaping singleton {n}.
            assert n not in range(-10, 11)


def test_integration() -> tuple[int, int]:
    ch = (ROOT / CH).read_text(encoding="utf-8")
    book = (ROOT / BOOK).read_text(encoding="utf-8")
    entry = (ROOT / STANDALONE).read_text(encoding="utf-8")
    assert r"\input{../../" + CH + "}" in book
    assert r"\input{../../" + CH + "}" in entry
    assert r"\setcounter{chapter}{20}" in entry
    for previous in ("07", "14", "18"):
        assert rf"\externaldocument{{general_topology_ch{previous}}}" in entry
    stable = re.search(r"rozdziały 01–(\d+) stabilne", book)
    assert stable and int(stable.group(1)) >= 21

    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(
        x["chapters"] for x in catalog["books"]
        if x["id"] == "general_topology"
    )
    assert len(chapters) >= 21 and chapters[20] == CH
    assert len(chapters) == len(set(chapters))
    all_text = "\n".join(
        (ROOT / name).read_text(encoding="utf-8") for name in chapters
    )
    labels = re.findall(r"\\label\{([^}]+)\}", all_text)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", all_text)
    assert len(labels) == len(set(labels))
    assert set(refs) <= set(labels), sorted(set(refs) - set(labels))

    for label in (
        "def:topog21-kx",
        "prop:topog21-vietoris-basis",
        "thm:topog21-vietoris-hausdorff",
        "thm:topog21-complete",
        "thm:topog21-compact-metric",
        "thm:topog21-vietoris-compact",
        "def:topog21-fell",
        "lem:topog21-alexander",
        "thm:topog21-fell-compact",
        "thm:topog21-fell-hausdorff",
        "prop:topog21-fell-nets",
        "thm:topog21-fell-vietoris",
        "ex:topog21-escaping",
    ):
        assert rf"\label{{{label}}}" in ch, label
    for env in ("twierdzenie", "lemat", "stwierdzenie",
                "wniosek", "definicja", "przyklad",
                "uwaga", "proof", "figure"):
        assert ch.count(r"\begin{" + env + "}") == ch.count(
            r"\end{" + env + "}"), env
    assert "F=X\\setminus\\bigcup_{i\\in I}U_i" in ch
    assert "C_j\\cap F\\neq\\varnothing" in ch
    assert "c_{e(s,t)}>0" not in ch
    for forbidden in (
        r"zwartościowani\w*",
        r"zbieżnoś(?:ć|ci|cią)\s+zwart\w*",
        r"pierwszo-?przeliczaln\w*",
        r"drugo-?przeliczaln\w*",
        r"\bunia\b",
    ):
        assert not re.search(forbidden, ch, re.IGNORECASE), forbidden
    # Visual regression: A/B labels in the Hausdorff-distance figure
    # formerly overlapped by about 3 PDF points. The figure has y=1cm,
    # so enforce at least 0.45cm between their TikZ center positions.
    visual = re.search(
        r'\\begin\{tikzpicture\}\[x=3\.05cm,y=1cm\](.*?)\\end\{tikzpicture\}',
        ch,
        re.DOTALL,
    )
    assert visual, "missing Hausdorff-distance figure"
    nodes = {
        label: (float(x), float(y))
        for x, y, label in re.findall(
            r'\\node\[[^]]+\]\s+at\s+\(([-\d.]+),([-\d.]+)\)\s+\{([^{}]+)\};',
            visual.group(1),
        )
    }
    assert '$A

if __name__ == "__main__":
    metric_checks = finite_hausdorff_models()
    finite_checks = finite_vietoris_fell_models()
    escaping_sets()
    labels, refs = test_integration()
    print(
        f"PASS ch21: {metric_checks} Hausdorff triangle checks, "
        f"{finite_checks} finite Vietoris/Fell cases; "
        f"{labels} labels, {refs} refs"
    )
 in nodes and '$B

if __name__ == "__main__":
    metric_checks = finite_hausdorff_models()
    finite_checks = finite_vietoris_fell_models()
    escaping_sets()
    labels, refs = test_integration()
    print(
        f"PASS ch21: {metric_checks} Hausdorff triangle checks, "
        f"{finite_checks} finite Vietoris/Fell cases; "
        f"{labels} labels, {refs} refs"
    )
 in nodes, nodes
    assert nodes['$A

if __name__ == "__main__":
    metric_checks = finite_hausdorff_models()
    finite_checks = finite_vietoris_fell_models()
    escaping_sets()
    labels, refs = test_integration()
    print(
        f"PASS ch21: {metric_checks} Hausdorff triangle checks, "
        f"{finite_checks} finite Vietoris/Fell cases; "
        f"{labels} labels, {refs} refs"
    )
][1] - nodes['$B

if __name__ == "__main__":
    metric_checks = finite_hausdorff_models()
    finite_checks = finite_vietoris_fell_models()
    escaping_sets()
    labels, refs = test_integration()
    print(
        f"PASS ch21: {metric_checks} Hausdorff triangle checks, "
        f"{finite_checks} finite Vietoris/Fell cases; "
        f"{labels} labels, {refs} refs"
    )
][1] >= 0.45, nodes

    return len(labels), len(refs)


if __name__ == "__main__":
    metric_checks = finite_hausdorff_models()
    finite_checks = finite_vietoris_fell_models()
    escaping_sets()
    labels, refs = test_integration()
    print(
        f"PASS ch21: {metric_checks} Hausdorff triangle checks, "
        f"{finite_checks} finite Vietoris/Fell cases; "
        f"{labels} labels, {refs} refs"
    )
