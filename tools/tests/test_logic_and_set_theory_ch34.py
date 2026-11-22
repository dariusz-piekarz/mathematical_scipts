"""Regression checks for chapter 34: forcing, ccc and the continuum hypothesis."""
import json
import re
import unittest
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/logic_and_set_theory"
PATH = CHAPTERS / "34-hipoteza-continuum-i-zastosowania-wymuszania.tex"
TEXT = PATH.read_text(encoding="utf8")


class TestContinuumForcingChapter34(unittest.TestCase):
    def test_book_and_catalog_integration(self):
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf8")
        catalog = json.loads((ROOT / "catalog/books.json").read_text("utf8"))
        logic = next(b for b in catalog["books"] if b["id"] == "logic_and_set_theory")
        self.assertEqual(len(logic["chapters"]), 34)
        self.assertTrue(logic["chapters"][-1].endswith(PATH.name))
        self.assertIn(PATH.name, book)
        self.assertIn(r"\label{ch:forcing-continuum}", TEXT)

    def test_environment_structure_and_inventory(self):
        expected = {
            "definicja": 5, "lemat": 7, "twierdzenie": 5,
            "przyklad": 2, "uwaga": 3, "proof": 12, "wniosek": 0,
            "figure": 0,
        }
        stack = []
        for action, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if action == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for env, count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), count)
                self.assertEqual(TEXT.count(r"\end{" + env + "}"), count)

        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 23)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(all(label.startswith((
            "ch:forcing-", "def:forcing34-", "lem:forcing34-",
            "thm:forcing34-", "ex:forcing34-", "rem:forcing34-"
        )) for label in labels))

    def test_all_references_resolve(self):
        all_labels = set()
        for source in CHAPTERS.glob("*.tex"):
            all_labels.update(re.findall(
                r"\\label\{([^}]+)\}", source.read_text("utf8")
            ))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 22)
        self.assertFalse(set(refs) - all_labels, set(refs) - all_labels)
        self.assertIn("ch:constructible", refs)
        self.assertIn("thm:forcing33-zfc", refs)

    def test_no_wrong_relative_consistency_claim(self):
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC})", TEXT)
        self.assertIn("przeliczalnego", TEXT)
        self.assertIn("modelem", TEXT)
        self.assertIn("Nie jest to jeszcze dowód", TEXT)
        self.assertIn("wewnątrz} $M$ istnieje", TEXT)
        self.assertIn(r"\omega_2^M", TEXT)

    def test_delta_system_case_analysis(self):
        section = TEXT[TEXT.index(r"\label{lem:forcing34-delta}"):
                       TEXT.index(r"\end{proof}", TEXT.index(r"\label{lem:forcing34-delta}"))]
        self.assertIn("regularności", section)
        self.assertIn("Indukujemy po $n$", section)
        self.assertIn(r"R\cup\{x\}", section)
        self.assertIn("parami", section)
        # A sample nontrivial delta system: a common root and disjoint petals.
        family = [
            frozenset({0, 1, 2}),
            frozenset({0, 3, 4}),
            frozenset({0, 5, 6}),
            frozenset({0, 7, 8}),
        ]
        intersections = {
            a & b for a, b in combinations(family, 2)
        }
        self.assertEqual(intersections, {frozenset({0})})

    def test_exhaustive_finite_cohen_compatibility(self):
        # All 3^4 finite partial 2-valued functions on four coordinates.
        coords = range(4)
        conditions = []
        for choices in product((None, 0, 1), repeat=len(coords)):
            conditions.append({
                k: value for k, value in zip(coords, choices)
                if value is not None
            })
        checked = 0
        for p in conditions:
            for q in conditions:
                compatible = all(
                    p[k] == q[k] for k in p.keys() & q.keys()
                )
                extensions = [
                    r for r in conditions
                    if all(r.get(k) == value for k, value in p.items())
                    and all(r.get(k) == value for k, value in q.items())
                ]
                self.assertEqual(compatible, bool(extensions))
                if compatible:
                    union = p | q
                    self.assertIn(union, extensions)
                checked += 1
        self.assertEqual(checked, 81 * 81)
        self.assertIn(r"\operatorname{Add}(\omega,\kappa)^M", TEXT)
        self.assertIn(r"\label{lem:forcing34-add-ccc}", TEXT)

    def test_different_cohen_reals_have_dense_witnesses(self):
        # Any finite two-row assignment can be extended so the rows differ.
        for left in product((None, 0, 1), repeat=3):
            for right in product((None, 0, 1), repeat=3):
                support = {
                    (a, n): v
                    for a, row in ((0, left), (1, right))
                    for n, v in enumerate(row) if v is not None
                }
                n = 3
                extension = support | {(0, n): 0, (1, n): 1}
                self.assertTrue(all(extension[k] == v
                                    for k, v in support.items()))
                self.assertNotEqual(extension[0, n], extension[1, n])
        self.assertIn(r"D_{\alpha,\beta}", TEXT)

    def test_cohen_reals_new_even_if_some_ground_sequences_exist(self):
        # A finite-prefix analogue of the dense set E_{alpha,x}.
        for old in product((0, 1), repeat=5):
            for initial_size in range(5):
                for decided in product((0, 1), repeat=initial_size):
                    p = {(0, i): v for i, v in enumerate(decided)}
                    q = p | {(0, initial_size): 1 - old[initial_size]}
                    self.assertNotEqual(q[0, initial_size], old[initial_size])
                    self.assertTrue(all(q[k] == v for k, v in p.items()))
        self.assertIn(r"E_{\alpha,x}", TEXT)
        self.assertIn(r"c_\alpha\notin M", TEXT)

    def test_finite_analogue_countable_closure(self):
        # A small closure check: any decreasing chain of extensions has
        # a union lower bound. The infinite theorem needs closure in M.
        all_conditions = [
            {i: v for i, v in enumerate(choice) if v is not None}
            for choice in product((None, 0, 1), repeat=3)
        ]
        for a in all_conditions:
            for b in all_conditions:
                if not all(b.get(k) == v for k, v in a.items()):
                    continue
                for c in all_conditions:
                    if not all(c.get(k) == v for k, v in b.items()):
                        continue
                    u = a | b | c
                    self.assertIn(u, all_conditions)
                    self.assertTrue(all(u.get(k) == v
                                        for p in (a, b, c)
                                        for k, v in p.items()))
        self.assertIn(r"\label{lem:forcing34-closed-no-sequences}", TEXT)

    def test_collapse_dense_value_and_coordinate_sets(self):
        # Finite analogue of extending a countable domain inside omega_1:
        # restrict to domains of size <= 2 within an available 4-point set.
        for k in range(3):
            for dom in combinations(range(4), k):
                for values in product(range(3), repeat=k):
                    p = dict(zip(dom, values))
                    for missing in set(range(4)) - p.keys():
                        extended = p | {missing: 0}
                        self.assertIn(missing, extended)
                    for target in range(3):
                        new_coord = min(set(range(4)) - p.keys())
                        q = p | {new_coord: target}
                        self.assertIn(target, q.values())
                        self.assertTrue(all(q[i] == v
                                            for i, v in p.items()))
        self.assertIn(r"\operatorname{Coll}(\omega_1,\lambda)", TEXT)
        self.assertIn(r"\label{thm:forcing34-ch}", TEXT)

    def test_proof_contains_cardinal_preservation_and_ch_dichotomy(self):
        for label in (
            "lem:forcing34-no-ordinals", "lem:forcing34-add-ccc",
            "lem:forcing34-decide-ordinal", "thm:forcing34-ccc-preserves",
            "thm:forcing34-not-ch", "lem:forcing34-collapse-closed",
            "lem:forcing34-closed-no-sequences",
            "lem:forcing34-collapse-surjection",
            "thm:forcing34-ch", "thm:forcing34-two-models",
        ):
            self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn(r"\omega_1^{M[G]}=\omega_1^M", TEXT)
        self.assertIn(r"\mathcal P(\omega)^{M[H]}", TEXT)
        self.assertIn(r"\mathcal P(\omega)^M", TEXT)
        self.assertIn("maksymalny", TEXT)
        self.assertIn(r"\operatorname{ran}f^H\subseteq S", TEXT)


if __name__ == "__main__":
    unittest.main()
