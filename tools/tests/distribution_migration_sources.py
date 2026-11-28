"""Locate historical distribution tests in AF or its staged/canonical DT successor."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AF = ROOT / "chapters/pl/functional_analysis"
DT_MODE = "ATLAS_TEST_DT_CANDIDATES"
MAP = {17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 7}
SPLIT = {23: (8, 10), 24: (9, 11), 25: (2, 3, 5, 7, 8, 11)}


def _migration():
    return json.loads((ROOT / "catalog/distribution_theory_migration.json")
                      .read_text(encoding="utf-8-sig"))["chapters"]


def _dt_paths():
    chapters = _migration()
    registered = {
        p for b in json.loads((ROOT / "catalog/books.json")
                              .read_text(encoding="utf-8-sig"))["books"]
        for p in b["chapters"]
    }
    active = [c["target_path"] in registered for c in chapters]
    if any(active) and not all(active):
        raise AssertionError("partial DT activation")
    key = "target_path" if all(active) else "staged_path"
    return {int(c["id"].split("-")[1]): ROOT / c[key] for c in chapters}, all(active)


def source_for(chapter):
    paths, active = _dt_paths()
    if active or os.environ.get(DT_MODE) == "1":
        return paths[MAP[chapter]]
    originals = list(AF.glob(f"{chapter:02d}-*.tex"))
    if len(originals) != 1:
        raise AssertionError(f"expected exactly one FA-{chapter} source: {originals}")
    return originals[0]


def reference_context(chapter, *, legacy_all=False):
    """Use preceding DT chapters and the surviving earlier AF foundations."""
    paths, active = _dt_paths()
    if active or os.environ.get(DT_MODE) == "1":
        sources = [p for p in sorted(AF.glob("*.tex"))
                   if p.name[:2].isdigit() and int(p.name[:2]) <= 16]
        sources.extend(paths[i] for i in sorted(paths) if i <= MAP[chapter])
    else:
        sources = [p for p in sorted(AF.glob("*.tex"))
                   if legacy_all or (p.name[:2].isdigit()
                                     and int(p.name[:2]) <= chapter)]
    return "\n".join(p.read_text(encoding="utf-8") for p in sources)


def using_dt():
    _, active = _dt_paths()
    return active or os.environ.get(DT_MODE) == "1"


def split_source(chapter, *ids):
    """Read only the mapped DT sections relevant to the historical assertion."""
    if not using_dt():
        return source_for(chapter).read_text(encoding="utf-8")
    paths, _ = _dt_paths()
    return "\n".join(paths[i].read_text(encoding="utf-8")
                     for i in (ids or SPLIT[chapter]))


def split_context(chapter):
    if not using_dt():
        return reference_context(chapter)
    paths, _ = _dt_paths()
    sources = [p for p in sorted(AF.glob("*.tex"))
               if p.name[:2].isdigit() and int(p.name[:2]) <= 16]
    sources.extend(paths[i] for i in sorted(paths) if i <= 11)
    return "\n".join(p.read_text(encoding="utf-8") for p in sources)
