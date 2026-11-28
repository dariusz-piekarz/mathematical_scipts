"""Check that a copied LaTeX fragment preserves all labels and references.

For exact source -> copy transfers (whole chapter or selected source fragment).
Counts multiplicity; ignores comments/verbatim using the library parser.
Does not modify either input. Exit 0 for equality, 1 on drift, 2 on input error.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.latex_parser import parse_document


def collect(text: str) -> tuple[Counter[str], Counter[tuple[str, str]]]:
    # The synthetic path is used only to satisfy the parser's module ID
    # convention; it does not change any input content or labels.
    document = parse_document(text, "chapters/pl/ALG-00--transfer.tex")
    labels = Counter(item.name for item in document.labels)
    references = Counter((item.command, item.target) for item in document.references)
    return labels, references


def compare(original: str, copied: str) -> dict:
    source_labels, source_refs = collect(original)
    copy_labels, copy_refs = collect(copied)

    def diff(a, b):
        return [
            {"name": (list(k) if isinstance(k, tuple) else k), "count": v}
            for k, v in sorted((a - b).items(), key=lambda item: str(item[0]))
        ]

    result = {
        "preserved": source_labels == copy_labels and source_refs == copy_refs,
        "missing_labels": diff(source_labels, copy_labels),
        "extra_labels": diff(copy_labels, source_labels),
        "missing_references": diff(source_refs, copy_refs),
        "extra_references": diff(copy_refs, source_refs),
        "original_label_count": sum(source_labels.values()),
        "copy_label_count": sum(copy_labels.values()),
        "original_reference_count": sum(source_refs.values()),
        "copy_reference_count": sum(copy_refs.values()),
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("copied", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    try:
        result = compare(args.original.read_text(encoding="utf-8-sig"),
                         args.copied.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2
    content = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(content + "\n", encoding="utf-8")
    else:
        print(content)
    return 0 if result["preserved"] else 1


if __name__ == "__main__":
    sys.exit(main())