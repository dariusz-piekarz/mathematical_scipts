"""Protect the canonical destinations of the retired CAL-13 material."""
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
CANONICAL = {
    "ME-20": "chapters/pl/measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex",
    "ME-21": "chapters/pl/measure_theory/21-twierdzenie-riesza-markowa-kakutaniego.tex",
    "ME-32": "chapters/pl/measure_theory/32-calka-daniella-stone-a.tex",
    "FA-12": "chapters/pl/functional_analysis/12-klasyczne-przestrzenie-banacha-i-ich-duale.tex"
}
LEGACY_LABELS = {
    "ME-20": [
        "ch:radon-measures-20",
        "def:borel-locfinite-20",
        "rem:compact-finiteness-20",
        "def:regularity-20",
        "eq:outer-regular-20",
        "eq:inner-compact-20",
        "def:radon-measure-20",
        "lem:radon-sigmafinite-inner-20",
        "thm:finite-metric-regular-20",
        "eq:finite-regular-error-20",
        "thm:lch-secondcountable-radon-20",
        "it:ex:radon-two-regularities",
        "lem:cutoff-radon-20",
        "thm:uniqueness-cc-20",
        "tw:radon-unikalnosc",
        "eq:cc-open-sup-20",
        "it:lem:radon-dominated"
    ],
    "ME-21": [
        "ch:riesz-markov-21",
        "thm:riesz-positive-21",
        "eq:riesz-representation-21",
        "it:lem:radon-local-bound",
        "it:eq:radon-open-content-general",
        "it:eq:radon-outer-general",
        "it:eq:radon-outer-inner-general",
        "it:cor:radon-compact-inf",
        "def:metric-outer-21",
        "lem:metric-outer-borel-21",
        "eq:metric-outer-sep-21",
        "thm:compact-riesz-21",
        "eq:open-content-21",
        "eq:riesz-outer-21",
        "eq:riesz-upper-sum-21",
        "eq:riesz-lower-sum-21",
        "lem:exhaustion-21",
        "eq:gluing-measures-21",
        "lem:density-cc-c0-21",
        "thm:riesz-c0-positive-21",
        "it:lem:radon-cc-l1",
        "idx:21:definicja:08",
        "thm:riesz-complex-21"
    ],
    "ME-32": [
        "it:thm:daniell-radon-comparison",
        "it:ex:radon-baire-daniell",
        "it:cor:radon-cc-l1-general"
    ],
    "FA-12": [
        "prop:ck-banach12"
    ]
}


def labels(text):
    return re.findall(r"\\label\{([^}]+)\}", text)


class RadonMigration(unittest.TestCase):
    def test_original_labels_survive_in_canonical_chapters(self):
        for document, path in CANONICAL.items():
            with self.subTest(document=document):
                actual = labels((ROOT / path).read_text(encoding="utf-8"))
                self.assertEqual(len(actual), len(set(actual)))
                self.assertTrue(set(LEGACY_LABELS[document]) <= set(actual))

    def test_canonical_chapters_are_in_catalog(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        for document, path in CANONICAL.items():
            with self.subTest(document=document):
                owners = [b for b in catalog["books"] if path in b["chapters"]]
                self.assertEqual(len(owners), 1)
                entry = ROOT / owners[0]["entrypoint"]
                includes = re.findall(r"\\input\{([^}]+)\}", entry.read_text(encoding="utf-8"))
                self.assertIn((ROOT / path).resolve(),
                              [(entry.parent / name).resolve() for name in includes])

    def test_remaining_cal_references_use_canonical_targets(self):
        owner = {label: document for document, items in LEGACY_LABELS.items()
                 for label in items}
        for path in (ROOT / "chapters/pl/integration_theory").glob("*.tex"):
            if path.name == "13-calka-radona.tex":
                continue
            source = path.read_text(encoding="utf-8")
            refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", source))
            self.assertFalse(refs & owner.keys(), path.name)
            for document, label in re.findall(r"\\atlasref\{([^}:]+)::([^}]+)\}", source):
                if label in owner:
                    self.assertEqual(document, owner[label], path.name)


if __name__ == "__main__":
    unittest.main()
