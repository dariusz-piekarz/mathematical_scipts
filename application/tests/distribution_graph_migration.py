"""Catalog-aware migration of historical reading-edge expectations."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {"FA-17": "DT-01", "FA-18": "DT-02", "FA-19": "DT-03",
           "FA-20": "DT-04", "FA-21": "DT-05", "FA-22": "DT-07"}
SPLIT = {
    ("FA-23", "GT-07::thm:topog-zwartosc-sieci"): "DT-08",
    ("FA-23", "LA-10::thm:lin10-istnienie"): "DT-10",
    ("FA-25", "PDE-07::def:pde7-test"): "DT-08",
    ("FA-25", "KAT-09::cat:ex:tensor-rep"): "DT-11",
}


def active(catalog):
    return any(b["id"] == "distribution_theory" for b in catalog["books"])


def structure_plan():
    return json.loads((ROOT / "catalog/distribution_theory_structure_plan.json")
                      .read_text(encoding="utf-8"))


def restructured():
    return structure_plan()["status"] == "active"


def successor_source(source, qualified):
    """Locate a historical reading link in its actual successor chapter.

    A split can move two links from the same old chapter to different owners.
    Require exactly one successor, not a guessed mapping by chapter number.
    """
    if not source.startswith("DT-"):
        return source
    plan = structure_plan()
    key = "target_path" if restructured() else "candidate_path"
    candidates = []
    for row in plan["chapters"]:
        if source not in row["source_modules"] or not row.get(key):
            continue
        text = (ROOT / row[key]).read_text(encoding="utf-8")
        if r"\atlasref{" + qualified + "}" in text:
            candidates.append(f"DT-{row['number']:02d}")
    if len(candidates) != 1:
        raise AssertionError((source, qualified, candidates))
    return candidates[0]


def migrated_source(source, qualified):
    original = SPLIT.get((source, qualified), SOURCES.get(source, source))
    return successor_source(original, qualified) if restructured() else original


def migrated_target(target, label):
    if restructured():
        plan = structure_plan()
        mapped = {(a["old_document"], a["old_label"]): a["target_document"]
                  for a in plan["planned_qualified_aliases"]}
        return mapped.get((target, label), target)
    migration = json.loads((ROOT / "catalog/distribution_theory_migration.json")
                           .read_text(encoding="utf-8"))
    mapped = {(a["old_document"], a["old_label"]): a["target_document"]
              for a in migration["qualified_label_aliases"]}
    return mapped.get((target, label), target)


def migrate_required(required, catalog):
    if not active(catalog):
        return required
    result = set()
    for source, qualified, target in required:
        label = qualified.split("::", 1)[1]
        new_target = migrated_target(target, label)
        result.add((migrated_source(source, qualified),
                    new_target + "::" + label, new_target))
    if len(result) != len(required):
        raise AssertionError("reading-edge regression collapsed")
    return result
