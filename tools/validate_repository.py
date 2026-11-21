#!/usr/bin/env python3
"""Validate locale-aware LaTeX imports and uploaded source copies.

Run from any working directory after cloning the complete repository.
The script does not modify documents or compile LaTeX.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import sys

from audit_chapter_dependencies import audit as audit_dependencies

ROOT = Path(__file__).resolve().parents[1]
INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


def validate_books() -> list[str]:
    """Return missing-import errors for every book and shared chapter."""
    errors: list[str] = []
    for book in sorted((ROOT / "books").glob("*/*.tex")):
        text = book.read_text(encoding="utf-8")
        for relative in INPUT_RE.findall(text):
            # TeX resolves input paths relative to the compilation directory.
            target = (book.parent / relative).resolve()
            if not target.is_file():
                errors.append(f"Missing import in {book.relative_to(ROOT)}: {relative}")
            elif target.suffix != ".tex":
                errors.append(f"Import is not a TeX file: {target}")
        # Files included by the book may import shared modules. Those paths
        # are also relative to the book's working directory, not to a chapter.
        for relative in INPUT_RE.findall(text):
            chapter = (book.parent / relative).resolve()
            if chapter.is_file():
                try:
                    child_text = chapter.read_text(encoding="utf-8")
                except UnicodeError:
                    errors.append(f"Non UTF-8 chapter: {chapter}")
                    continue
                for nested in INPUT_RE.findall(child_text):
                    if not (book.parent / nested).resolve().is_file():
                        errors.append(f"Missing nested import in {chapter.relative_to(ROOT)}: {nested}")
    return errors


def validate_attachments() -> list[str]:
    """Check that all 20 uploaded chapters match their normalized sources."""
    errors: list[str] = []
    manifest_path = ROOT / "catalog/new_chapters.json"
    if not manifest_path.exists():
        return ["Missing catalog/new_chapters.json"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if len(manifest) != 20:
        errors.append(f"Expected 20 attached chapters, found {len(manifest)}")
    for item in manifest:
        chapter = ROOT / item["canonical_path"]
        source = ROOT / item["source_copy"]
        if not (chapter.is_file() and source.is_file()):
            errors.append(f"Missing canonical or source file: {item['source']}")
            continue
        normalize = lambda b: b.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
        left = normalize(chapter.read_bytes())
        right = normalize(source.read_bytes())
        if left != right:
            errors.append(f"Source copy differs from canonical chapter: {item['source']}")
        digest = hashlib.sha256(left).hexdigest()
        if digest != item["repository_normalized_sha256"]:
            errors.append(f"Normalized SHA-256 mismatch: {item['source']}")
    return errors


def main() -> int:
    """Print a concise validation report; return a failing exit code on error."""
    errors = validate_books() + validate_attachments() + audit_dependencies(ROOT)['errors']
    for error in errors:
        print("ERROR:", error)
    if errors:
        print(f"Validation failed: {len(errors)} issues")
        return 1
    print("Validation passed: imports, 20 normalized source copies, chapter assets and catalog")
    return 0


if __name__ == "__main__":
    sys.exit(main())
