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


def migrated_source(source, qualified):
    return SPLIT.get((source, qualified), SOURCES.get(source, source))


def migrated_target(target, label):
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
