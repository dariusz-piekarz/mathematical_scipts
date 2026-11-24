"""Synchronize self-contained LaTeX preambles with the global code style."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "% BEGIN GLOBAL CODE LISTINGS (generated from latex/pl/code-listings.tex)"
END = "% END GLOBAL CODE LISTINGS"
BLOCK = re.compile(r"(?ms)^" + re.escape(BEGIN) + r"\n.*?^" + re.escape(END) + r"\n?")
def targets():
    yield from sorted((ROOT / "books/pl").glob("*.tex"))
    yield from sorted((ROOT / "application/config/preambles").glob("*.tex"))

def synchronize(source, canonical):
    # Deliberately refuse unknown legacy configurations rather than silently
    # deleting a package option, an unrelated style, or a chapter's code.
    if BEGIN in source or END in source:
        if len(BLOCK.findall(source)) != 1:
            raise ValueError("invalid generated block")
        remaining = BLOCK.sub("", source).partition(r"\begin{document}")[0]
        if re.search(r"\\(?:lstset|lstdefinestyle|lstdefinelanguage)\b|\\usepackage(?:\[[^\]]*\])?\{[^}]*\blistings\b", remaining):
            raise ValueError("local listings override outside generated block")
        return BLOCK.sub(lambda _: canonical, source)
    head, sep, body = source.partition(r"\begin{document}")
    head = re.sub(r"(?m)^\\usepackage\{listings\}\s*\n", "", head)
    head = re.sub(r"(?m)^\\definecolor\{code(?:bg|border|comment|keyword)\}\{RGB\}\{[^}]*\}\s*\n", "", head)
    head = re.sub(r"(?ms)^\\lstdefinelanguage\{Julia\}\{.*?^\}\s*\n", "", head)
    head = re.sub(r"(?ms)^\\lstdefinestyle\{(?:skrypt|pythonpde)\}\{.*?^\s*[^{}\n]*\}\s*\n", "", head)
    head = re.sub(r"(?m)^\\lstset\{[^\n]*\}\s*\n", "", head)
    head = re.sub(r"(?m)^\\renewcommand\{\\lst(?:listingname|listlistingname)\}\{[^}]*\}\s*\n", "", head)
    if re.search(r"\\(?:lstset|lstdefinestyle|lstdefinelanguage)\b|\\usepackage(?:\[[^\]]*\])?\{[^}]*\blistings\b", head):
        raise ValueError("unknown listings configuration")
    return head.rstrip() + "\n\n" + canonical + sep + body

def main():
    p = argparse.ArgumentParser()
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = p.parse_args()
    canonical = (ROOT / "latex/pl/code-listings.tex").read_text(encoding="utf-8")
    assert canonical.startswith(BEGIN + "\n") and canonical.endswith(END + "\n")
    stale = []
    for path in targets():
        source = path.read_text(encoding="utf-8")
        result = synchronize(source, canonical)
        if result != source:
            stale.append(path.relative_to(ROOT))
            if args.write:
                path.write_text(result, encoding="utf-8")
    print(f"Checked {len(list(targets()))} preambles; stale: {len(stale)}")
    for path in stale:
        print(path)
    if args.check and stale:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
