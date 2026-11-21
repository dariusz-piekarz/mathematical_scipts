"""Export one LaTeX chapter from the compiled linear algebra textbook PDF.

Uses chapter-opening pages (not running page headers) as the source of truth.
Book pagination is preserved in the exported pages.

Usage:
  python tools/export_linear_algebra_chapter_pdf.py \
      --input books/pl/linear_algebra.pdf \
      --output books/pl/linear_algebra_aktualny_rozdzial.pdf --latest
  python tools/export_linear_algebra_chapter_pdf.py \
      --input books/pl/linear_algebra.pdf --chapter 14 --output /tmp/ch14.pdf

Requires: pypdf >= 5, < 6.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

from pypdf import PdfReader, PdfWriter
from pypdf.generic import Destination


OPENING = re.compile(r"^Rozdział\s+(\d+)\s*$")


def chapter_openings(reader: PdfReader) -> dict[int, int]:
    """Map chapter number to zero-based PDF page index, skipping TOC headers."""
    # Bookmarks are the fast path: the master book has one top-level bookmark
    # per numbered chapter, with section bookmarks nested below it.
    bookmarks = [item for item in reader.outline
                 if isinstance(item, Destination)]
    if bookmarks:
        found: dict[int, int] = {}
        for number, bookmark in enumerate(bookmarks, start=1):
            page_number = reader.get_destination_page_number(bookmark)
            first_line = (reader.pages[page_number].extract_text() or "").splitlines()
            if not first_line or not OPENING.fullmatch(first_line[0]) \
                    or int(first_line[0].split()[-1]) != number:
                found.clear()
                break
            found[number] = page_number
        if found:
            return found
    # Graceful fallback for PDFs generated without outline bookmarks.
    found = {}
    for page_number, page in enumerate(reader.pages):
        first_line = (page.extract_text() or "").splitlines()
        if not first_line:
            continue
        match = OPENING.fullmatch(first_line[0])
        if match:
            chapter = int(match.group(1))
            if chapter in found:
                raise ValueError(f"Duplicate opening for chapter {chapter}")
            found[chapter] = page_number
    return found


def export(pdf: Path, output: Path, chapter: int | None = None) -> tuple[int, int]:
    reader = PdfReader(str(pdf))
    starts = chapter_openings(reader)
    if not starts:
        raise ValueError(f"No chapter opening pages detected in {pdf}")
    if chapter is None:
        chapter = max(starts)
    if chapter not in starts:
        raise ValueError(f"Chapter {chapter} does not exist; available: {sorted(starts)}")

    start = starts[chapter]
    later = [page for number, page in starts.items() if number > chapter]
    stop = min(later, default=len(reader.pages))
    if not (0 <= start < stop <= len(reader.pages)):
        raise ValueError("Invalid chapter page range")

    writer = PdfWriter()
    for page_number in range(start, stop):
        writer.add_page(reader.pages[page_number])
    writer.add_metadata({
        "/Title": f"Algebra liniowa — rozdział {chapter}",
        "/Subject": "Samodzielny PDF rozdziału; numery stron zachowane z książki",
    })
    writer.add_outline_item(f"Rozdział {chapter}", 0)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as file:
        writer.write(file)
    # Verify the produced PDF: do not silently produce a misordered file.
    check = PdfReader(str(output))
    if len(check.pages) != stop - start:
        raise RuntimeError("Export has unexpected page count")
    first_line = (check.pages[0].extract_text() or "").splitlines()
    if not first_line or first_line[0] != f"Rozdział {chapter}":
        raise RuntimeError("Export does not start at the requested chapter")
    return chapter, stop - start


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--chapter", type=int)
    selection.add_argument("--latest", action="store_true")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"PDF missing: {args.input}")
    chapter, pages = export(args.input, args.output, None if args.latest else args.chapter)
    print(f"Exported chapter {chapter}: {pages} pages -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
