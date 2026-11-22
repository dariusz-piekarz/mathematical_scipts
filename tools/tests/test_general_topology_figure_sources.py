#!/usr/bin/env python3
"""Static quality gates for figures in the general topology book.

This detects missing captions/labels and duplicated figure IDs. It is not
a replacement for visual inspection of compiled PDFs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIGURE = re.compile(
    r"\\begin\{figure\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{figure\}"
)
LABEL = re.compile(r"\\label\{([^}]+)\}")
CAPTION = re.compile(r"\\caption(?:\[[^\]]*\])?\s*\{")
TIKZ = re.compile(r"\\begin\{tikzpicture\}")


def check() -> None:
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(b["chapters"] for b in catalog["books"]
                    if b["id"] == "general_topology")
    seen: dict[str, str] = {}
    count = 0
    illustrated = set()
    for chapter in chapters:
        source = (ROOT / chapter).read_text(encoding="utf-8")
        figures = list(FIGURE.finditer(source))
        if figures:
            illustrated.add(chapter)
        for figure in figures:
            body = figure.group(1)
            captions = list(CAPTION.finditer(body))
            labels = list(LABEL.finditer(body))
            assert len(captions) == 1, (chapter, "figure needs exactly one caption")
            assert len(labels) == 1, (chapter, "figure needs exactly one label")
            assert labels[0].start() > captions[0].start(), (
                chapter, "put figure label after caption")
            assert TIKZ.search(body), (chapter, "figure has no TikZ visualization")
            key = labels[0].group(1)
            assert key.startswith("fig:"), (chapter, key)
            assert key not in seen, (key, seen.get(key), chapter)
            seen[key] = chapter
            count += 1

    assert len(chapters) == 26
    assert count == 27, ("illustration inventory changed", count)
    assert len(illustrated) == 17, ("illustrated chapter set changed", len(illustrated))
    print(f"PASS figure source inventory: {count} captioned, labeled TikZ figures "
          f"in {len(illustrated)} chapters")


if __name__ == "__main__":
    check()
