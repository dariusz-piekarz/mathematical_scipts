r"""Static, read-only provenance for labels imported with TeX \input.

This does not execute TeX conditionals: an imported label denotes a
possible definition in a physically included file, not proof that a
conditional \label will execute in every compiled document.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

INPUT_RE = re.compile(r"\\input\s*\{([^{}]+)\}")
LABEL_RE = re.compile(r"\\label\s*\{([^{}]+)\}")
MAX_INCLUDE_DEPTH = 12


@dataclass(frozen=True)
class IncludedLabel:
    name: str
    source_document: str
    relative_path: str
    line: int
    offset: int
    excerpt: str


def included_labels_for_document(
    source_text: str,
    document_id: str,
    *,
    repo_root: Path,
    masked_source,
) -> list[IncludedLabel]:
    r"""Scan literal \input with compilation-root-relative paths.

    Only existing files inside repo_root may contribute. The project
    compiles books from books/pl; a literal \input path in a chapter is
    resolved with respect to that TeX compilation root, NOT the chapter.
    Dynamic expressions, missing files and recursive includes are ignored.
    """
    repo_root = repo_root.resolve()
    tex_cwd = repo_root / "books" / "pl"
    if not tex_cwd.is_dir():
        return []
    result: list[IncludedLabel] = []
    visited: set[Path] = set()

    def scan(body: str, depth: int) -> None:
        if depth > MAX_INCLUDE_DEPTH:
            return
        masked = masked_source(body)
        for match in INPUT_RE.finditer(masked):
            raw = match.group(1).strip()
            if not raw or "\\" in raw or "#" in raw:
                continue  # not a literal TeX filename
            candidate = (tex_cwd / raw).resolve()
            if not candidate.suffix:
                candidate = candidate.with_suffix(".tex")
            if (candidate in visited or not candidate.is_relative_to(repo_root)
                    or not candidate.is_file() or candidate.suffix != ".tex"):
                continue
            visited.add(candidate)
            text = candidate.read_text(encoding="utf-8-sig")
            rel = candidate.relative_to(repo_root).as_posix()
            masked_included = masked_source(text)
            for label_match in LABEL_RE.finditer(masked_included):
                name = label_match.group(1).strip()
                if name:
                    pos = label_match.start()
                    result.append(IncludedLabel(
                        name=name, source_document=document_id, relative_path=rel,
                        line=text.count("\n", 0, pos) + 1, offset=pos,
                        excerpt=" ".join(text[max(0, pos-100):pos+220].split())[:270],
                    ))
            scan(text, depth + 1)

    scan(source_text, 0)
    return result
