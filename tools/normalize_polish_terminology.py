#!/usr/bin/env python3
"""Unify Polish mathematical terminology in current source documents.

Canonical spelling: presnop / presnopy and all inflected forms.
Historical audit reports are intentionally preserved as records.
Usage:
  python3 tools/normalize_polish_terminology.py --fix
  python3 tools/normalize_polish_terminology.py --check
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
EXTENSIONS = {".tex", ".md", ".txt", ".html"}
SKIP_DIRECTORIES = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    "build", "dist", "out", "audits",
}
OBSOLETE = re.compile(r"przed-?snop", flags=re.IGNORECASE)


def canonical(match: re.Match[str]) -> str:
    term = match.group(0)
    if term.isupper():
        return "PRESNOP"
    if term[0].isupper():
        return "Presnop"
    return "presnop"


def active_sources():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRECTORIES for part in path.relative_to(ROOT).parts):
            continue
        yield path


def run(*, fix: bool) -> int:
    changed_files = 0
    occurrences = 0
    for path in active_sources():
        source = path.read_text(encoding="utf-8")
        revised, count = OBSOLETE.subn(canonical, source)
        if count:
            changed_files += 1
            occurrences += count
            print(f"{path.relative_to(ROOT)}: {count} -> presnop")
            if fix:
                path.write_text(revised, encoding="utf-8")
    print(f"Files: {changed_files}; obsolete terminology occurrences: {occurrences}")
    return int(bool(occurrences) and not fix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--fix", action="store_true", help="apply canonical spelling")
    mode.add_argument("--check", action="store_true", help="fail if obsolete spelling is found")
    args = parser.parse_args()
    raise SystemExit(run(fix=args.fix))
