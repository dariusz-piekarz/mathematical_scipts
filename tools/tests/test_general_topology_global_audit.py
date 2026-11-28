#!/usr/bin/env python3
"""Cross-chapter structural audit for Polish general topology.

Checks chapter/catalog/book alignment; unique labels; resolved cross-references;
theorem and proof environment balance; local \begin/\end syntax and forbidden
editorial terminology. Does NOT establish the correctness of mathematical proofs.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "catalog/books.json"
BOOK = ROOT / "books/pl/general_topology.tex"
CHAPTER_DIR = ROOT / "chapters/pl/general_topology"
ENVS = (
    "twierdzenie", "lemat", "stwierdzenie", "wniosek", "definicja",
    "przyklad", "uwaga", "proof", "figure", "tikzpicture",
    "enumerate", "itemize", "align", "align*", "equation",
    "equation*", "center", "minipage", "tabular",
)
FORBIDDEN = (
    (re.compile(r"\bunia\b", re.IGNORECASE), "unia"),
    (re.compile(r"\bzwartościowani\w*", re.IGNORECASE), "zwartościowanie"),
    (re.compile(r"\bpierwszoprzeliczaln\w*", re.IGNORECASE), "pierwszoprzeliczalny"),
    (re.compile(r"\bdrugoprzeliczaln\w*", re.IGNORECASE), "drugoprzeliczalny"),
    (re.compile(r"\bsekwencyjn\w*", re.IGNORECASE), "sekwencyjny"),
    (re.compile(r"\bzbieżnoś\w*\s+zwart\w*", re.IGNORECASE), "zbieżność zwarta"),
)


def stripped_source(text: str) -> str:
    """Remove nonescaped TeX comments for source-level structural checks."""
    clean = []
    for line in text.splitlines(keepends=True):
        before = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
        clean.append(before + ("\n" if not before.endswith("\n") else ""))
    return "".join(clean)


def run() -> None:
    books = json.loads(CATALOG.read_text(encoding="utf-8"))["books"]
    selected = [b for b in books if b["id"] == "general_topology"]
    assert len(selected) == 1, "general_topology must appear exactly once"
    chapters = selected[0]["chapters"]
    assert selected[0]["entrypoint"] == "books/pl/general_topology.tex"
    assert len(chapters) >= 22
    expected = sorted(p.as_posix().replace(ROOT.as_posix() + "/", "")
                      for p in CHAPTER_DIR.glob("*.tex"))
    assert sorted(chapters) == expected, ("catalog mismatch", expected, chapters)
    assert len(chapters) == len(set(chapters))
    assert all(Path(path).name.startswith(f"{i:02d}-")
               for i, path in enumerate(chapters, start=1))

    book = BOOK.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{\.\./\.\./(chapters/pl/general_topology/[^}]+)\}", book)
    assert inputs == chapters, ("book imports are out of order", inputs, chapters)

    global_labels: dict[str, str] = {}
    refs: list[tuple[str, str]] = []
    total_proofs = 0
    total_figures = 0
    total_lines = 0
    for path in chapters:
        raw = (ROOT / path).read_text(encoding="utf-8")
        assert raw.startswith(r"\chapter{"), path
        text = stripped_source(raw)
        total_lines += len(raw.splitlines())
        for env in ENVS:
            open_count = len(re.findall(r"\\begin\{" + re.escape(env) + r"\}", text))
            close_count = len(re.findall(r"\\end\{" + re.escape(env) + r"\}", text))
            assert open_count == close_count, (path, env, open_count, close_count)
            if env == "proof":
                total_proofs += open_count
            if env == "figure":
                total_figures += open_count
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            assert label not in global_labels, (label, global_labels.get(label), path)
            global_labels[label] = path
        refs += [(ref, path) for ref in re.findall(
            r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text
        )]
        for i, line in enumerate(text.splitlines(), start=1):
            # All forbidden patterns apply to prose and captions, not to
            # frozen LaTeX label identifiers.
            line = re.sub(r"\\(?:label|ref|eqref|pageref)\{[^}]*\}", "", line)
            for rx, name in FORBIDDEN:
                assert not rx.search(line), (name, path, i, line)

    missing = [(label, path) for label, path in refs if label not in global_labels]
    assert not missing, ("unresolved labels", missing)
    assert len(global_labels) >= 600, "unexpected global label loss"
    assert total_proofs >= 250, "unexpected proof loss"
    assert total_figures >= 15, "unexpected diagram loss"
    print(
        f"PASS global topology audit: {len(chapters)} chapters, "
        f"{total_lines} lines, {len(global_labels)} labels, "
        f"{len(refs)} refs, {total_proofs} proof environments, "
        f"{total_figures} figures"
    )


if __name__ == "__main__":
    run()
