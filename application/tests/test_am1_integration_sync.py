"""Protect the audited AM1-36 → CAL migration baseline.

New AM1 results may be developed independently; this regression protects the
128 source labels that have already been synchronized.
"""
from collections import Counter
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
LABEL = re.compile(r"\\label\{([^}]+)\}")
REF = re.compile(r"\\(?:ref|eqref)\{(ma1:kh:[^}]+)\}")
BASELINE = frozenset((
    "it:cor:acg-bv",
    "it:cor:denjoy-hk",
    "it:cor:mcshane-lattice",
    "it:cor:mcshane-lebesgue-consequences",
    "it:cor:mcshane-uniform",
    "it:cor:rs-classical-substitution",
    "it:ex:ks-atom-convergence",
    "it:ex:rs-gluing-failure",
    "it:ex:rs-substitution-atom",
    "it:ex:rs-substitution-reverse",
    "it:lem:ac-affine-extension",
    "it:lem:approx-derivative",
    "it:lem:ks-saks-henstock",
    "it:lem:perron-null-correction",
    "it:thm:acg-uniqueness",
    "it:thm:acstar-closure-algebra",
    "it:thm:denjoy-bv-ac",
    "it:thm:ks-equiintegrability",
    "it:thm:ks-locality",
    "it:thm:ks-uniform",
    "it:thm:mcshane-absolute",
    "it:thm:mcshane-basic",
    "it:thm:mcshane-equiintegrability",
    "it:thm:mcshane-lebesgue",
    "it:thm:perron-hk",
    "it:thm:rs-integrator-substitution",
    "it:thm:rs-locality",
    "it:thm:rs-oscillation",
    "it:thm:rs-reparametrization",
    "it:thm:rs-tools",
    "lem:ks-indicators",
    "lem:ks-point",
    "lem:ks-summation",
    "lem:ks-var",
    "lem:perron-scisle",
    "ma1:ch:kurzweil-henstock",
    "ma1:kh:cor:acgstar-null-variation",
    "ma1:kh:cor:ks-measure-limits",
    "ma1:kh:cor:ks-order-limits-monotone",
    "ma1:kh:cor:ks-variation-measure-l1",
    "ma1:kh:cor:wide-denjoy-ibp-ac",
    "ma1:kh:cor:wide-denjoy-limits",
    "ma1:kh:cor:wide-denjoy-uniform",
    "ma1:kh:def:kh-gauge",
    "ma1:kh:def:kh-integral",
    "ma1:kh:ex:conditional-derivative",
    "ma1:kh:ex:denjoy-strict",
    "ma1:kh:ex:dirichlet",
    "ma1:kh:ex:ks-cancelled-spikes",
    "ma1:kh:ex:ks-nonsummable-spikes",
    "ma1:kh:ex:ks-variation-defect",
    "ma1:kh:ex:rs-dominated-failure",
    "ma1:kh:lem:acstar-affine-extension",
    "ma1:kh:lem:acstar-null-variation",
    "ma1:kh:lem:bvstar-null-to-acstar",
    "ma1:kh:lem:fivefold-cover",
    "ma1:kh:lem:hk-uzupelnianie",
    "ma1:kh:lem:integral-ac",
    "ma1:kh:lem:kh-bvstar-cover",
    "ma1:kh:lem:kh-cousin",
    "ma1:kh:lem:kh-null-modification",
    "ma1:kh:lem:kh-null-variation",
    "ma1:kh:lem:kh-saks-henstock",
    "ma1:kh:lem:ks-point-spikes",
    "ma1:kh:lem:perron-order",
    "ma1:kh:lem:variation-additivity",
    "ma1:kh:prop:kh-unique",
    "ma1:kh:sec:comparison",
    "ma1:kh:st:denjoy-sklejanie",
    "ma1:kh:st:hk-zbieznosc-jednostajna",
    "ma1:kh:thm:ac-lebesgue-primitive",
    "ma1:kh:thm:acg-algebra",
    "ma1:kh:thm:acgstar-derivative-integrable",
    "ma1:kh:thm:acstar-ae-differentiable",
    "ma1:kh:thm:bv-multiplier",
    "ma1:kh:thm:integral-hierarchy",
    "ma1:kh:thm:kh-absolute",
    "ma1:kh:thm:kh-acgstar-characterization",
    "ma1:kh:thm:kh-cauchy",
    "ma1:kh:thm:kh-equiintegrability",
    "ma1:kh:thm:kh-hake",
    "ma1:kh:thm:kh-locality",
    "ma1:kh:thm:kh-order-limits",
    "ma1:kh:thm:kh-primitive-derivative",
    "ma1:kh:thm:ks-absolute-monotone",
    "ma1:kh:thm:ks-discrete-spikes",
    "ma1:kh:thm:ks-integrator-limit",
    "ma1:kh:thm:ks-measure-criteria-equivalence",
    "ma1:kh:thm:ks-positive-measure-l1",
    "ma1:kh:thm:ks-signed-measure-l1",
    "ma1:kh:thm:ks-variation-measure-defect",
    "ma1:kh:thm:rs-integrator-limit",
    "ma1:kh:thm:rs-uniform",
    "ma1:kh:thm:wide-denjoy-hake",
    "ma1:kh:thm:wide-denjoy-multiplier",
    "ma1:kh:thm:wide-denjoy-positive",
    "ma1:kh:thm:wide-denjoy-substitution",
    "ma1:kh:tw:denjoy-countable",
    "ma1:kh:tw:hk-oscylacyjne",
    "ma1:kh:tw:hk-podstawienie",
    "ma1:kh:tw:hk-zbieznosc-dct",
    "ma1:kh:wn:hk-ibp-ac",
    "prz:ac-kontra-acstar",
    "sec:kurzweil-stieltjes",
    "st:denjoy-szeroka-lokalnosc",
    "st:perron-sumy",
    "tw:denjoy-szeroka-ftc",
    "tw:ks-bv-reg",
    "tw:ks-bv-split",
    "tw:ks-cauchy",
    "tw:ks-chain",
    "tw:ks-decomp",
    "tw:ks-ibp",
    "tw:ks-measure",
    "tw:ks-primitive",
    "tw:ks-quadrature",
    "tw:ks-reg-bv",
    "tw:ks-step",
    "tw:ks-substitution",
    "tw:mcshane-indykator",
    "tw:perron-wyjatki",
    "tw:rs-blad-kwadratury",
    "tw:rs-jeden-skok",
    "wn:ks-ac-jumps",
    "wn:ks-ibp-ac",
    "wn:mcshane-proste",
    "wn:perron-kawalkami",
    "wn:rs-suma-skokow",
))


class AM1IntegrationSyncTest(unittest.TestCase):
    def test_synchronized_source_labels_and_local_dependencies(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "integration_theory")
        source = ROOT / "chapters/pl/mathematical_analysis_i/36-calka-kurzweila-henstocka.tex"
        self.assertEqual(len(BASELINE), 128)
        source_labels = set(LABEL.findall(source.read_text(encoding="utf-8-sig")))
        self.assertFalse(BASELINE - source_labels, "removed original AM1-36 labels")
        counts = Counter()
        refs = set()
        for path in book["chapters"]:
            content = (ROOT / path).read_text(encoding="utf-8-sig")
            counts.update(LABEL.findall(content))
            refs.update(REF.findall(content))
        self.assertFalse(BASELINE - counts.keys(), "missing migrated AM1-36 labels")
        self.assertEqual({label: n for label, n in counts.items() if n > 1}, {})
        self.assertFalse(refs - counts.keys(), "unresolved local AM1-36 dependencies in CAL")


if __name__ == "__main__":
    unittest.main()
