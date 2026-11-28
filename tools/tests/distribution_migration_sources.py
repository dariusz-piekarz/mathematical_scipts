"""Locate historical distribution tests in AF or its staged/canonical DT successor."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AF = ROOT / "chapters/pl/functional_analysis"
DT_MODE = "ATLAS_TEST_DT_CANDIDATES"
RESTRUCTURE_MODE = "ATLAS_TEST_DT_RESTRUCTURED"


class _JoinedSource:
    """Read several successor chapters through the historical source interface."""

    def __init__(self, paths):
        self.paths = paths

    def read_text(self, *, encoding="utf-8"):
        return "\n".join(p.read_text(encoding=encoding) for p in self.paths)


def _structure_plan():
    return json.loads((ROOT / "catalog/distribution_theory_structure_plan.json")
                      .read_text(encoding="utf-8"))


def _restructured():
    return (os.environ.get(RESTRUCTURE_MODE) == "1"
            or _structure_plan()["status"] == "active")


def _successor_sources(old_ids):
    plan = _structure_plan()
    wanted = {f"DT-{n:02d}" for n in old_ids}
    numbers = {row["planned_chapter"] for row in plan["label_map"]
               if row["old_document"] in wanted}
    if not numbers:
        raise AssertionError(f"no successors for {old_ids}")
    key = "target_path" if plan["status"] == "active" else "candidate_path"
    return [ROOT / row[key] for row in plan["chapters"]
            if row["number"] in numbers]


def _restructured_context():
    plan = _structure_plan()
    key = "target_path" if plan["status"] == "active" else "candidate_path"
    sources = [p for p in sorted(AF.glob("*.tex"))
               if p.name[:2].isdigit() and int(p.name[:2]) <= 16]
    sources.extend(ROOT / row[key] for row in plan["chapters"]
                   if row.get(key))
    return "\n".join(p.read_text(encoding="utf-8") for p in sources)

MAP = {17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 7}
SPLIT = {23: (8, 10), 24: (9, 11), 25: (2, 3, 5, 7, 8, 11)}


def _migration():
    return json.loads((ROOT / "catalog/distribution_theory_migration.json")
                      .read_text(encoding="utf-8-sig"))["chapters"]


def _dt_paths():
    if _restructured():
        plan = _structure_plan()
        key = "target_path" if plan["status"] == "active" else "candidate_path"
        return {row["number"]: ROOT / row[key] for row in plan["chapters"]
                if row.get(key)}, plan["status"] == "active"
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
    if _restructured():
        return _JoinedSource(_successor_sources((MAP[chapter],)))
    paths, active = _dt_paths()
    if active or os.environ.get(DT_MODE) == "1":
        return paths[MAP[chapter]]
    originals = list(AF.glob(f"{chapter:02d}-*.tex"))
    if len(originals) != 1:
        raise AssertionError(f"expected exactly one FA-{chapter} source: {originals}")
    return originals[0]


def reference_context(chapter, *, legacy_all=False):
    """Use preceding DT chapters and the surviving earlier AF foundations."""
    if _restructured():
        return _restructured_context()
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
    if _restructured():
        return True
    _, active = _dt_paths()
    return active or os.environ.get(DT_MODE) == "1"


def split_source(chapter, *ids):
    """Read only the mapped DT sections relevant to the historical assertion."""
    if _restructured():
        return _JoinedSource(_successor_sources(ids or SPLIT[chapter])).read_text()
    if not using_dt():
        return source_for(chapter).read_text(encoding="utf-8")
    paths, _ = _dt_paths()
    return "\n".join(paths[i].read_text(encoding="utf-8")
                     for i in (ids or SPLIT[chapter]))


def split_context(chapter):
    if _restructured():
        return _restructured_context()
    if not using_dt():
        return reference_context(chapter)
    paths, _ = _dt_paths()
    sources = [p for p in sorted(AF.glob("*.tex"))
               if p.name[:2].isdigit() and int(p.name[:2]) <= 16]
    sources.extend(paths[i] for i in sorted(paths) if i <= 11)
    return "\n".join(p.read_text(encoding="utf-8") for p in sources)
