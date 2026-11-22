#!/usr/bin/env python3
"""Check agreed terminology in added or modified mathematical LaTeX sources.

By default, check only changed .tex files rather than failing on untouched
legacy content. --all performs an explicit full-tree audit; --paths checks
only selected paths. Intended for GitHub Actions and local use.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

BANNED = {
    "presnop (use this spelling; rejected old variant)": re.compile(
        r"\bprzed-?snop\w*\b", flags=re.IGNORECASE),
    "zwartościowanie (use uzwarcenie)": re.compile(
        r"\bzwartościowani\w*\b", flags=re.IGNORECASE),
    "zbieżność zwarta (use zbieżność jednostajna na zbiorach zwartych)": re.compile(
        r"\bzbieżnoś\w*\s+zwarte\w*\b", flags=re.IGNORECASE),
    "nazwa uzwarcenia (use uzwarcenie Čecha–Stone’a)": re.compile(
        r"Stone[’\x27]a\s*[-–—]\s*Čecha", flags=re.IGNORECASE),
}


def git(*args: str) -> list[str]:
    p = subprocess.run(["git", *args], cwd=ROOT, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       check=True)
    return p.stdout.splitlines()


def is_source(path: Path) -> bool:
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return False
    return (path.suffix.lower() == ".tex"
            and relative.parts[:2] in (("chapters", "pl"), ("books", "pl"))
            and path.is_file())


def changed_paths(before: str | None) -> list[Path]:
    after = os.environ.get("GITHUB_SHA", "HEAD")
    if before and before != "0" * 40:
        lines = git("diff", "--name-only", "--diff-filter=ACMRT", before,
                    after, "--", "chapters/pl", "books/pl")
    else:
        try:
            lines = git("diff", "--name-only", "--diff-filter=ACMRT",
                        "HEAD^", "HEAD", "--", "chapters/pl", "books/pl")
        except subprocess.CalledProcessError:
            lines = git("ls-files", "chapters/pl", "books/pl")
    return [ROOT / s for s in lines]


def validate(paths: list[Path]) -> tuple[int, list[str]]:
    inspected = 0
    errors: list[str] = []
    for path in sorted(set(paths)):
        if not is_source(path):
            continue
        inspected += 1
        source = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for line_number, line in enumerate(source.splitlines(), 1):
            for description, pattern in BANNED.items():
                if pattern.search(line):
                    errors.append(f"{relative}:{line_number}: {description}")
    return inspected, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true",
                        help="check all LaTeX sources (including untouched legacy)")
    parser.add_argument("--changed-from", default=None,
                        help="base commit of push; compare with current SHA")
    parser.add_argument("--paths", nargs="+", default=None,
                        help="check named paths instead of commit differences")
    args = parser.parse_args()
    if args.paths is not None:
        paths = [(ROOT / s).resolve() for s in args.paths]
    elif args.all:
        paths = list((ROOT / "chapters/pl").rglob("*.tex"))
        paths += list((ROOT / "books/pl").rglob("*.tex"))
    else:
        paths = changed_paths(args.changed_from)

    inspected, errors = validate(paths)
    for error in errors:
        print("TERM ERROR:", error)
    print(f"Terminology audit: files={inspected}; violations={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
