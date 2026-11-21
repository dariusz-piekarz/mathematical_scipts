"""Repository-wide audit of Polish "chart" terminology.

Coordinate chart = "mapa" (not "karta"); mapping = "odwzorowanie".
This script reports every literal occurrence of Polish "karta" inflections
in TeX sources. Review the mathematical context before replacing: ordinary
uses such as playing cards are valid and must not be altered.
Historical \label/\ref identifiers are intentionally ignored.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

CARD_WORD = re.compile(
    r"\b(?:karta|karty|karcie|kartę|kartą|kartom|kartami|kartach|kart)\b",
    re.IGNORECASE,
)
REFERENCE = re.compile(
    r"\\(?:label|ref|eqref|pageref|autoref|nameref)\s*\{[^{}]*\}"
)


# Reviewed legitimate meanings: real playing cards in probability examples.
# Any new chart-like use in other TeX files is a terminology regression.
# Caps intentionally prevent silently growing the exceptions.
CARD_GAME_EXCEPTIONS = {
    "chapters/pl/probability_volume_i/01-kombinatoryka-i-modele-skonczone.tex": 17,
    "chapters/pl/probability_volume_i/04-zmienne-losowe-i-rozklady-prawdopodobienstwa.tex": 2,
    "sources/pl/rachunek_prawdopodobienstwa_tom_I.tex": 19,
}


def unexpected_matches(
    findings: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Classify occurrences outside the reviewed playing-card examples."""
    grouped: dict[str, list[dict[str, object]]] = {}
    for item in findings:
        grouped.setdefault(str(item["path"]), []).append(item)
    result: list[dict[str, object]] = []
    for path, items in grouped.items():
        allowance = CARD_GAME_EXCEPTIONS.get(path, 0)
        result.extend(items[allowance:])
    return result


def scan(root: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in sorted(root.rglob("*.tex")):
        if any(part in (".git", ".venv", "node_modules", "__pycache__")
               for part in path.parts):
            continue
        try:
            content = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(content.splitlines(), 1):
            checked = REFERENCE.sub(lambda m: " " * len(m.group()), line)
            for match in CARD_WORD.finditer(checked):
                findings.append({
                    "path": str(path.relative_to(root)).replace("\\", "/"),
                    "line": line_number,
                    "word": match.group(),
                    "context": line.strip()[:260],
                })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[2])
    parser.add_argument("--report", type=Path)
    parser.add_argument("--strict", action="store_true",
                        help="fail if unreviewed occurrences remain outside playing-card examples")
    args = parser.parse_args()
    root = args.root.resolve()
    findings = scan(root)
    unexpected = unexpected_matches(findings)
    report = {
        "scope": "all repository TeX sources",
        "rule": "coordinate chart = mapa; mapping = odwzorowanie",
        "total_occurrences": len(findings),
        "files": len({entry["path"] for entry in findings}),
        "reviewed_non_chart_occurrences": len(findings) - len(unexpected),
        "unexpected_occurrences": len(unexpected),
        "findings": findings,
        "unexpected": unexpected,
    }
    if args.report:
        out = args.report.resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print(f"Polish chart terminology scan: {report['total_occurrences']} "
          f"literal occurrences in {report['files']} TeX files; "
          f"{len(unexpected)} unexpected, "
          f"{report['reviewed_non_chart_occurrences']} playing-card usages.")
    for entry in unexpected:
        print(f"UNEXPECTED {entry['path']}:{entry['line']}: "
              f"{entry['word']}: {entry['context']}")
    return 1 if unexpected and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
