#!/usr/bin/env python3
"""Global Polish math editorial check: polynomial *factorization*, not splitting.

Checks all canonical LaTeX manuscripts in chapters/pl as well as sources/pl.
"Rozszczepienie" is correct for split exact sequences, morphisms, bundles,
and other mathematically distinct constructions and must be preserved.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

BAD = (
    re.compile(r"\brozszczep\w*\s+wielomian\w*", re.IGNORECASE),
    re.compile(
        r"\bwielomian\w*(?:\s+(?:minimalny|charakterystyczny))?\s+"
        r"rozszczep\w*", re.IGNORECASE
    ),
    re.compile(r"\\\((?:m_T|\\chi_T)\\\)\s+rozszczep\w*", re.IGNORECASE),
    re.compile(r"\brozszczep\w*\s+\\\((?:m_T|\\chi_T)\\\)", re.IGNORECASE),
)


def check_text(text: str) -> list[tuple[int, str]]:
    # Preserve offsets for precise line numbers; allow line-wrapped phrases.
    normalized = text.replace("\r", " ").replace("\n", " ")
    problems = {}
    for pattern in BAD:
        for match in pattern.finditer(normalized):
            line = text.count("\n", 0, match.start()) + 1
            problems[(line, match.group(0))] = True
    return sorted(problems)


def main() -> int:
    for valid in (
        "Wielomian rozkłada się na czynniki liniowe nad K.",
        "Krótki ciąg dokładny rozszczepia się.",
        "Zasada rozszczepienia wiązek wektorowych.",
        "Rozszczepiony epimorfizm ma prawą odwrotność.",
    ):
        assert not check_text(valid), valid
    for invalid in (
        "Wielomian rozszczepia się nad K.",
        "Rozszczepienie wielomianu minimalnego.",
        "Rozszczepiony wielomian charakterystyczny.",
        "Gdy \\(m_T\\) rozszczepia się nad K.",
        "Warunek rozszczepienia\nwielomianu charakterystycznego.",
    ):
        assert check_text(invalid), invalid

    all_tex = sorted((ROOT / "chapters/pl").rglob("*.tex"))
    all_tex += sorted((ROOT / "sources/pl").rglob("*.tex"))
    errors = []
    for path in all_tex:
        content = path.read_text(encoding="utf-8-sig")
        for lineno, bad in check_text(content):
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: {bad}")
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        print(f"Polish terminology FAIL: {len(errors)} occurrences")
        return 1
    print(f"Polish polynomial-factorization terminology OK: {len(all_tex)} TeX files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
