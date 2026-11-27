"""Conservative audit of literal declarations versus reader macro profiles."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

from scripts import install_math_renderer as renderer

DECL = re.compile(r"^\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator|def)\*?\s*(?:\{\s*)?(\\[A-Za-z@]+)")
IGNORED = {r"\proofname", r"\headrulewidth", r"\lstlistingname",
           r"\lstlistlistingname", r"\chaptermark", r"\atlasref",
           r"\thesection", r"\theHsection"}


def audit(root, profiles):
    findings = []
    counts = Counter()
    paths = sorted((root / "chapters/pl").rglob("*.tex"))
    preambles = sorted((root / "application/config/preambles").glob("*.tex"))
    for path in preambles + paths:
        book = path in preambles
        doc = path.stem if book else renderer.module_id(path)
        base = doc.split("-", 1)[0]
        counts["preambles" if book else "chapters"] += 1
        if base not in profiles:
            findings.append({"module": doc, "path": str(path.relative_to(root)),
                             "status": "missing_book_profile"})
        effective = {**profiles.get(base, {}), **profiles.get(doc, {})}
        header = True
        declared = dict(profiles.get(base, {})) if not book else {}
        for line in renderer.logical_macro_lines(path.read_text(encoding="utf-8-sig")):
            if not line:
                continue
            if not book and renderer.is_header_metadata(line):
                continue
            match = DECL.match(line)
            if not match:
                if not book:
                    header = False
                continue
            name = match[1]
            literal = renderer.add_literal_macro(line, declared)
            if name in IGNORED:
                status = "non_math_metadata"
            elif not book and not header:
                status = "late_declaration_review"
            elif not literal:
                status = "unsupported_declaration_review"
            elif name not in effective:
                status = "missing_profile_macro_review"
            elif effective[name] != declared[name]:
                status = "different_definition_review"
            else:
                status = "covered"
            counts[status] += 1
            if status not in {"covered", "non_math_metadata"}:
                findings.append({"module": doc, "path": str(path.relative_to(root)),
                                 "macro": name, "status": status,
                                 "declaration": line[:240]})
            if not book and not literal:
                header = False
    return {"counts": dict(counts), "findings": findings,
            "limitations": "Line-leading declarations only; not TeX expansion, scope proof or actual KaTeX rendering. Review items are not confirmed rendering errors."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    source = (args.root / "application/frontend/vendor/math-macro-profiles.js").read_text(encoding="utf-8")
    profiles = json.loads(source.removeprefix("window.atlasMathMacroProfiles = ").removesuffix(";\n"))
    report = audit(args.root, profiles)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
