"""Chapter 31: constructible universe, finite Gödel operations, condensation, GCH."""
from itertools import combinations
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "chapters/pl/logic_and_set_theory"
FILE = DIR / "31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex"
TEXT = FILE.read_text(encoding="utf8")


class TestChapter31(unittest.TestCase):
    def test_registered_as_last_chapter(self):
        self.assertIn(FILE.name, (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf8"))
        self.assertIn(FILE.name, (ROOT / "catalog/books.json").read_text("utf8"))
        self.assertIn(r"\label{ch:constructible}", TEXT)

    def test_inventory_and_environment_balance(self):
        expected = {
            "definicja": 6, "lemat": 27, "przyklad": 9,
            "twierdzenie": 5, "uwaga": 16, "wniosek": 2,
            "proof": 34,
        }
        for env, num in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), num)
                self.assertEqual(TEXT.count(r"\end{" + env + "}"), num)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 68)
        self.assertEqual(len(set(labels)), len(labels))

    def test_references_have_targets_and_counts(self):
        all_labels = set()
        for path in DIR.glob("*.tex"):
            all_labels.update(re.findall(r"\\label\{([^}]+)\}", path.read_text("utf8")))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 87)
        self.assertEqual(set(refs) - all_labels, set())

    def test_first_finite_hierarchy_levels(self):
        # For finite n: L_n = V_n, hence sizes 0,1,2,4,16.
        def pset(seq):
            values = list(seq)
            return frozenset(
                frozenset(values[i] for i in range(len(values)) if (mask >> i) & 1)
                for mask in range(1 << len(values))
            )
        levels = [frozenset()]
        for _ in range(4):
            levels.append(pset(levels[-1]))
        self.assertEqual([len(L) for L in levels], [0, 1, 2, 4, 16])
        self.assertTrue(all(levels[i] <= levels[i + 1] for i in range(4)))
        # Each level is transitive: elements of elements belong to the level.
        for level in levels:
            for a in level:
                self.assertTrue(all(b in level for b in a))
        self.assertIn(r"\operatorname{Def}(\varnothing):=\{\varnothing\}", TEXT)
        self.assertIn(r"\mathcal P(L_2)", TEXT)
        self.assertIn("każdy jego podzbiór", TEXT)
        self.assertIn("schemat zastępowania", TEXT)

    def test_definition_is_relative_to_set_structures(self):
        for value in (
            r"\operatorname{Sat}_M", r"\operatorname{Def}(M)",
            r"\mathcal P(M)", r"M^{<\omega}", "schemat zastępowania",
        ):
            with self.subTest(value=value):
                self.assertIn(value, TEXT)
        self.assertIn("o uniwersum $M$", TEXT)

    def test_delta0_and_reflection_proofs(self):
        for label in (
            "def:delta0", "thm:delta0-absolute", "lem:l-finite-reflection",
            "thm:l-model-zf", "lem:l-hierarchy-internal",
        ):
            with self.subTest(label=label):
                self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn("ZFC", TEXT)
        self.assertIn("wyróżnianie", TEXT)
        self.assertIn("zastępowanie", TEXT)

    def test_condensation_does_not_assume_internal_full_zf(self):
        for label in (
            "lem:l-elementary-section-75",
            "lem:l-collapse-def-compatibility",
            "lem:l-finite-godel-term-absoluteness-78",
            "lem:l-all-stage-histories-78",
            "lem:l-finite-condensation-package",
            "lem:l-condensation",
            "lem:l-expanded-hull-condensation",
        ):
            with self.subTest(label=label):
                self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn(r"\mathsf{Hist}", TEXT)
        self.assertIn(r"\mathsf{Def}_G", TEXT)
        self.assertIn(r"\sigma_*", TEXT)
        self.assertIn("skończon", TEXT)
        self.assertIn("Nie zakładamy", TEXT)

    def test_gch_is_relative_to_internal_cardinals(self):
        self.assertIn(r"\label{thm:l-gch}", TEXT)
        self.assertIn(r"\label{cor:l-relative-consistency}", TEXT)
        self.assertIn(r"L\models 2^\kappa=\kappa^+", TEXT)
        self.assertIn(r"\kappa\subseteq X", TEXT)
        self.assertIn(r"\kappa\in X", TEXT)
        self.assertIn(r"\pi(A)", TEXT)
        self.assertIn(r"L_{\kappa^+}", TEXT)

    def test_stage_code_uniqueness_and_limits(self):
        for label in (
            "def:l-stage-code-32", "lem:l-stage-code-unique-32",
            "lem:l-hierarchy-delta1-derived-75",
            "lem:l-all-stage-histories-78",
        ):
            with self.subTest(label=label):
                self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn(r"h(0)=\varnothing", TEXT)
        self.assertIn(r"\operatorname{Def}", TEXT)
        self.assertIn(r"\bigcup_{\xi<\lambda}", TEXT)

    def test_polish_terminology_and_zero_forward_links(self):
        for bad in ("zwartościowanie", "tensorowanie", "pierwszo-przeliczalna"):
            self.assertNotIn(bad, TEXT.lower())
        self.assertFalse(re.search(r"\\ref\{ch:constructible-future", TEXT))


if __name__ == "__main__":
    unittest.main()
