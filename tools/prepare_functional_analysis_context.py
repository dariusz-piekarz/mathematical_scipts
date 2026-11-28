"""Build the chapter audit wrapper from the actual AF inventory."""
import argparse
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/pl/functional_analysis.tex"


def prepare(chapter):
    catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    active = any(b["id"] == "distribution_theory" for b in catalog["books"])
    book = BOOK.read_text(encoding="utf-8")
    assert book.count(r"\begin{document}") == 1
    pre = book.split(r"\begin{document}", 1)[0]
    inputs = re.findall(r"\\input\{(\.\./\.\./chapters/pl/functional_analysis/[^}]+)\}", book)
    ids = [f"{i:02d}" for i in range(1,16)] + ["15A","15B"] + [f"{i:02d}" for i in range(16,34)]
    if active:
        ids = [i for i in ids if not (i.isdigit() and 17 <= int(i) <= 25)]
    actual = [Path(p).name.split("-", 1)[0] for p in inputs]
    assert actual == ids, (actual, ids)
    # The last three historical audits deliberately use the full book.
    count = len(ids) if chapter >= 31 else ids.index(f"{chapter:02d}") + 1
    body = r"\begin{document}" + "\n"
    body += "\n".join(r"\input{" + name + "}" for name in inputs[:count])
    body += "\n" + r"\end{document}" + "\n"
    (BOOK.parent / f"functional_analysis_ch{chapter:02d}_context_ci.tex").write_text(
        pre + body, encoding="utf-8")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
            out.write(f"dt_active={'true' if active else 'false'}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter", type=int, choices=range(26,34))
    prepare(parser.parse_args().chapter)
