"""Compile every canonical figure in a selected book with the Atlas renderer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend import figure_preview as renderer
from backend.latex_parser import module_id


def verify_png(path: Path) -> None:
    """Check PNG integrity and decode all pixels, not just its signature."""
    with Image.open(path) as image:
        if image.format != 'PNG':
            raise ValueError('Expected PNG image')
        image.verify()
    with Image.open(path) as image:
        image.load()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", default="graph_and_knot_theory",
                        choices=("graph_and_knot_theory", "mathematical_analysis_ii"))
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    catalog = json.loads((ROOT.parent / "catalog/books.json").read_text(encoding="utf-8"))
    book = next(b for b in catalog["books"] if b["id"] == args.book)
    report = {"book": args.book, "chapters": len(book["chapters"]), "figures": 0, "passed": 0, "failures": []}
    # Fresh isolated cache: do not count previously compiled images as evidence.
    with tempfile.TemporaryDirectory(prefix="atlas-book-figures-") as temp:
        renderer.CACHE = Path(temp)
        for relative in book["chapters"]:
            path = ROOT.parent / relative
            module = module_id(path)
            source = path.read_text(encoding="utf-8-sig")
            figures = renderer.figures(source)
            report["figures"] += len(figures)
            for key in figures:
                try:
                    output = renderer.render(module, source, key)
                    verify_png(output)
                    report["passed"] += 1
                except (renderer.FigureError, OSError, ValueError, SyntaxError, Image.DecompressionBombError) as exc:
                    report["failures"].append({"module": module, "figure": key, "error": str(exc)})
            print(f"{module}: {len(figures)} figures checked", flush=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["figures"] and not report["failures"] else 1


if __name__ == "__main__":
    sys.exit(main())
