#!/usr/bin/env python3
"""Audit the ACTUAL algebraic-topology book, including TOP-00 and shared modules.

This is a structural/editorial validation, not a substitute for reading proofs.
"""
from __future__ import annotations

from collections import defaultdict
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/pl/algebraic_topology.tex"
INPUT = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\s*\{([^{}]+)\}")
BEGIN = re.compile(r"\\begin\s*\{([^{}]+)\}")
END = re.compile(r"\\end\s*\{([^{}]+)\}")
TITLE = re.compile(r"\\begin\{(twierdzenie|lemat|stwierdzenie|wniosek)\}(?:\[([^\]]+)\])?")
BAD_TERM = re.compile(r"\btensorowan\w*|\bsekwencj\w*|\bseskwilin\w*|\bdual\b", re.I | re.U)
MAP_WORD = re.compile(r"(?<!\w)(?:mapa|mapy|mapę|mapą|mapie)(?!\w)", re.I | re.U)
MAPPING_CHAPTERS = {"02", "12", "13", "14", "24", "27"}


def mask_comments(raw: str) -> str:
    lines = []
    for line in raw.splitlines(keepends=True):
        for i, ch in enumerate(line):
            if ch != "%":
                continue
            n = 0
            k = i-1
            while k >= 0 and line[k] == "\\":
                n += 1
                k -= 1
            if n % 2 == 0:
                line = line[:i] + " "*(len(line)-i-len("\n" if line.endswith("\n") else "")) + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def at(src: str, pos: int) -> int:
    return src.count("\n", 0, pos) + 1


def scan(root: Path = ROOT) -> dict:
    root = root.resolve()
    catalog = json.loads((root / "catalog/books.json").read_text(encoding="utf-8"))
    conf = [b for b in catalog["books"] if b["entrypoint"] == "books/pl/algebraic_topology.tex"]
    if len(conf) != 1:
        return {"errors":["Expected one algebraic-topology catalog entry"]}
    expected = conf[0]["chapters"]
    entry = root / "books/pl/algebraic_topology.tex"
    book = mask_comments(entry.read_text(encoding="utf-8"))
    actual = [(entry.parent/n).resolve() for n in INPUT.findall(book)]
    planned = [(root/n).resolve() for n in expected]
    errors = []
    warnings = []
    if len(expected) != 31 or [Path(n).name[:2] for n in expected] != [f"{i:02}" for i in range(31)]:
        errors.append("Catalog must list TOP-00 through TOP-30 in sequence")
    if actual != planned:
        errors.append("Actual book inputs differ from catalog ordering (including TOP-00)")
    if book.count(r"\begin{document}") != 1 or book.count(r"\end{document}") != 1:
        errors.append("Malformed book document environment")
    if book.count(r"\tableofcontents") != 1:
        errors.append("Expected exactly one table of contents")

    labels = defaultdict(list)
    refs = []
    titles = defaultdict(list)
    blocks = defaultdict(list)
    chapters = []
    shared = set()

    def visit(file: Path, chapter: str, depth=0):
        if depth > 5 or not file.is_file() or not file.is_relative_to(root):
            errors.append(f"Missing/recursive include: {file}")
            return
        src = mask_comments(file.read_text(encoding="utf-8-sig"))
        rel = file.relative_to(root).as_posix()
        chapters.append({
            "source":rel,"chapter":chapter,"lines":len(src.splitlines()),
            "proofs":src.count(r"\begin{proof}"),
            "figures":src.count(r"\begin{figure}"),
            "labels":len(LABEL.findall(src))})
        for m in LABEL.finditer(src):
            labels[m.group(1)].append((rel,at(src,m.start())))
        for m in REF.finditer(src):
            refs.append((m.group(1),rel,at(src,m.start())))
        for m in BAD_TERM.finditer(src):
            line = src.splitlines()[at(src,m.start())-1]
            # Historical LaTeX label IDs are stable identifiers, not prose.
            if r"\label{" not in line:
                warnings.append(f"Terminology {m.group(0)} {rel}:{at(src,m.start())}")
        if chapter in MAPPING_CHAPTERS:
            for m in MAP_WORD.finditer(src):
                line = src.splitlines()[at(src,m.start())-1]
                if not any(x in line for x in (r"\label{",r"\ref{",r"\eqref{")):
                    errors.append(f"Mapa used for an algebraic mapping {rel}:{at(src,m.start())}: {line.strip()}")
        events = sorted(
            [(m.start(),1,m.group(1)) for m in BEGIN.finditer(src)] +
            [(m.start(),-1,m.group(1)) for m in END.finditer(src)])
        stack = []
        for pos,kind,name in events:
            if kind == 1:
                stack.append((name,at(src,pos)))
            elif not stack or stack[-1][0] != name:
                errors.append(f"{rel}:{at(src,pos)} unmatched end{{{name}}}")
            else:
                stack.pop()
        for name,line in stack:
            errors.append(f"{rel}:{line} unclosed begin{{{name}}}")
        for m in TITLE.finditer(src):
            title = re.sub(r"\s+"," ",m.group(2) or "").strip().lower()
            if title:
                titles[title].append({"chapter":chapter,"source":rel,"line":at(src,m.start())})
        for paragraph in re.split(r"\n[ \t]*\n",src):
            norm = re.sub(r"\s+"," ",paragraph).strip()
            if 180 <= len(norm) <= 2400 and not norm.startswith(r"\begin{"):
                blocks[norm].append((chapter,rel))
        for m in INPUT.finditer(src):
            name = m.group(1)
            if "\\" in name or "#" in name:
                errors.append(f"Dynamic include needs review {rel}:{at(src,m.start())} {name}")
                continue
            child = (entry.parent/name).resolve()
            if child.is_relative_to(root):
                shared.add(child.relative_to(root).as_posix())
            visit(child,chapter,depth+1)

    for chapter,path in enumerate(planned):
        visit(path,f"{chapter:02}")
    for key,locations in labels.items():
        if len(locations)>1:
            errors.append(f"Duplicate label {key}: {locations}")
    for key,path,line in refs:
        if key not in labels:
            errors.append(f"Undefined reference {key} in {path}:{line}")
    intro = (root/expected[0]).read_text(encoding="utf-8")
    if r"\phantomsection" not in intro.split(r"\addcontentsline",1)[0]:
        errors.append("TOP-00: missing hyperref anchor for TOC")
    if chr(96)*2+"dowód oznacza" in intro:
        errors.append("TOP-00: unclosed quote before dowód")
    if "Wersja XIX" in book or "18 listopada 2026 r." in book:
        warnings.append("Main title page version/date is outdated")

    repeated = []
    for block,sites in blocks.items():
        different=sorted(set(ch for ch,_ in sites))
        if len(different)>1:
            repeated.append({"chapters":different,"sources":sorted(set(src for _,src in sites)),
                             "size":len(block),"snippet":block[:170]})
    repeated.sort(key=lambda x:-x["size"])
    title_repeats=[{"title":k,"locations":v} for k,v in titles.items()
                   if len(set(x["chapter"] for x in v))>1]
    return {
        "audit":"Global TOP-00–TOP-30 (actual main book and shared source)",
        "statistics":{
            "chapters":len(expected),"visited_sources":len(chapters),
            "source_lines":sum(x["lines"] for x in chapters),
            "proofs":sum(x["proofs"] for x in chapters),
            "figures":sum(x["figures"] for x in chapters),
            "unique_labels":len(labels),"references":len(refs),
            "shared_modules":sorted(shared)},
        "errors":errors,
        "warnings":warnings,
        "exact_duplicate_paragraphs":repeated[:100],
        "repeated_theorem_titles":title_repeats[:100],
        "per_chapter":chapters}

def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--report",type=Path,default=Path("/tmp/topology_global_audit.json"))
    args=parser.parse_args()
    result=scan()
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    display={k:result[k] for k in ("statistics","errors","warnings",
                                   "exact_duplicate_paragraphs","repeated_theorem_titles")}
    print(json.dumps(display,ensure_ascii=False,indent=2))
    print("Global audit:",len(result["errors"]),"errors,",len(result["warnings"]),"warnings")
    return int(bool(result["errors"]))

if __name__=="__main__":
    raise SystemExit(main())
