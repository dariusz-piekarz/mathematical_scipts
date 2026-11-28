#!/usr/bin/env python3
"""Check that canonical LaTeX chapters use only packaged assets.

Run from any directory: python tools/audit_chapter_dependencies.py
Chapter files remain TeX fragments; book entrypoints own the preambles.
This deliberately checks *file* dependencies, not cross-chapter references.
"""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_NAME = re.compile(r"\d{2}[AB]?-[a-z0-9-]+\.tex\Z")
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
ASSET_RE = re.compile(
    r"\\(includegraphics|lstinputlisting|verbatiminput|includepdf|"
    r"includestandalone|includesvg|addbibresource|bibliography)\*?\s*"
    r"(?:\[[^\]]*\]\s*)?\{([^{}]+)\}"
)
MINTED_RE = re.compile(r"\\inputminted\s*(?:\[[^\]]*\]\s*)?\{[^{}]+\}\s*\{([^{}]+)\}")
VERBATIM_RE = re.compile(
    r"\\begin\s*\{(lstlisting|verbatim|Verbatim|minted|filecontents\*?)\}"
    r".*?\\end\s*\{\1\}", re.DOTALL
)
GRAPHICS_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".eps")


def _mask(text: str) -> str:
    """Remove verbatim blocks and comments, preserving line positions."""
    text = VERBATIM_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    out: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "%":
            backslashes = 0
            k = i - 1
            while k >= 0 and text[k] == "\\":
                backslashes += 1
                k -= 1
            if backslashes % 2 == 0:
                end = text.find("\n", i)
                if end < 0:
                    end = len(text)
                out.append(" " * (end - i))
                i = end
                continue
        out.append(text[i])
        i += 1
    return "".join(out)


def _candidates(root: Path, tex: Path, kind: str, name: str) -> list[Path]:
    """Resolve assets relative to the book's TeX working directory."""
    location = root / "books" / "pl" / name
    if kind == "includegraphics" and not Path(name).suffix:
        return [location.with_suffix(ext) for ext in GRAPHICS_EXTENSIONS]
    if kind == "includesvg" and not Path(name).suffix:
        return [location.with_suffix(".svg")]
    if kind in {"includestandalone", "bibliography"} and not Path(name).suffix:
        return [location.with_suffix(".tex" if kind == "includestandalone" else ".bib")]
    return [location]


def audit(root: Path = ROOT) -> dict:
    """Return machine-readable errors; does not modify the working tree."""
    root = root.resolve()
    errors: list[str] = []
    catalog_path = root / "catalog" / "books.json"
    if not catalog_path.is_file():
        return {"errors": ["Missing catalog/books.json"], "chapters": 0, "books": 0}
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    books = catalog["books"]
    declared: set[str] = set()
    for book in books:
        entry = root / book["entrypoint"]
        expected = book["chapters"] + book.get("supplements", [])
        if not entry.is_file():
            errors.append(f"Missing book entrypoint: {book['entrypoint']}")
            continue
        source = _mask(entry.read_text(encoding="utf-8"))
        inputs = [x.replace("\\", "/") for x in INPUT_RE.findall(source)]
        resolved = [(entry.parent / x).resolve() for x in inputs]
        listed = [(root / x).resolve() for x in expected]
        chapter_order = [(root / x).resolve() for x in book["chapters"]]
        if (len(resolved) != len(listed) or set(resolved) != set(listed)
                or [p for p in resolved if p in chapter_order] != chapter_order):
            errors.append(f"Entrypoint imports differ from catalog: {book['entrypoint']}")
        for path in expected:
            if path in declared:
                errors.append(f"Chapter appears in more than one catalog position: {path}")
            declared.add(path)
            if not (root / path).is_file():
                errors.append(f"Missing registered module: {path}")
            if "/supplements/" not in path and not CHAPTER_NAME.fullmatch(Path(path).name):
                errors.append(f"Invalid numbered chapter name: {path}")

    actual = {p.relative_to(root).as_posix() for p in (root / "chapters" / "pl").rglob("*.tex")}
    for missing in sorted(actual - declared):
        errors.append(f"Unregistered chapter/supplement: {missing}")
    for missing in sorted(declared - actual):
        errors.append(f"Catalog entry without chapter: {missing}")

    # These are canonical source references, not future shared-module targets.
    registry = root / "catalog" / "topic_registry.json"
    if registry.is_file():
        data = json.loads(registry.read_text(encoding="utf-8"))
        for module in data.get("canonical_modules", []):
            for source in module.get("sources", []):
                path = source.get("path")
                if path and not (root / path).exists():
                    errors.append(f"Stale registry source path: {path}")

    files = sorted((root / "chapters" / "pl").rglob("*.tex"))
    files += sorted((root / "shared" / "pl").rglob("*.tex"))
    files += sorted((root / "books" / "pl").glob("*.tex"))
    for tex in files:
        source = _mask(tex.read_text(encoding="utf-8"))
        for match in ASSET_RE.finditer(source):
            kind, arg = match.groups()
            # \bibliography{a,b} is special: each .bib must be packaged.
            names = arg.split(",") if kind == "bibliography" else [arg]
            for name in names:
                name = name.strip()
                line = source.count("\n", 0, match.start()) + 1
                if not name or "\\" in name or "#" in name:
                    errors.append(f"Dynamic asset requires review: {tex.relative_to(root)}:{line} {kind}{{{name}}}")
                    continue
                paths = _candidates(root, tex, kind, name)
                if not any(p.is_file() and p.resolve().is_relative_to(root) for p in paths):
                    errors.append(f"Missing asset: {tex.relative_to(root)}:{line} {kind}{{{name}}}")
        for match in MINTED_RE.finditer(source):
            name = match.group(1)
            location = (root / "books" / "pl" / name).resolve()
            if not location.is_file() or not location.is_relative_to(root):
                line = source.count("\n", 0, match.start()) + 1
                errors.append(f"Missing inputminted source: {tex.relative_to(root)}:{line} {name}")
        if re.search(r"\\(?:tikzexternalize|write18)\b", source):
            errors.append(f"External TeX execution/cache dependency: {tex.relative_to(root)}")
    return {"errors": errors, "chapters": len(actual), "books": len(books)}


def main() -> int:
    report = audit()
    for problem in report["errors"]:
        print("ERROR:", problem)
    print(f"Dependency audit: {report['chapters']} TeX modules, {report['books']} books, {len(report['errors'])} errors")
    return int(bool(report["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
