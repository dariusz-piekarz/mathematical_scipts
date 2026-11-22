"""Chapter 35 — Boolean-valued models and relative consistency of CH."""
import json
import re
import unittest
from functools import lru_cache
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/logic_and_set_theory"
SOURCE = CHAPTERS / "35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex"
TEXT = SOURCE.read_text(encoding="utf8")


class TestBooleanModelsChapter35(unittest.TestCase):
    def test_registered_in_book_and_catalog(self):
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf8")
        books = json.loads((ROOT / "catalog/books.json").read_text("utf8"))["books"]
        current = next(x for x in books if x["id"] == "logic_and_set_theory")
        self.assertGreaterEqual(len(current["chapters"]), 35)
        self.assertTrue(current["chapters"][34].endswith(SOURCE.name))
        self.assertIn(SOURCE.name, book)
        self.assertIn(r"\label{ch:boolean-valued-independence}", TEXT)

    def test_environment_nesting_and_inventory(self):
        counts = {
            "definicja": 8, "lemat": 8, "twierdzenie": 6,
            "uwaga": 4, "przyklad": 1, "proof": 14,
            "wniosek": 0, "figure": 0,
        }
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for env, count in counts.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), count)
                self.assertEqual(TEXT.count(r"\end{" + env + "}"), count)

        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 28)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(all(label.startswith((
            "ch:boolean-", "def:boolean35-", "lem:boolean35-",
            "thm:boolean35-", "rem:boolean35-", "ex:boolean35-"
        )) for label in labels))

    def test_all_references_exist(self):
        all_labels = set()
        for source in CHAPTERS.glob("*.tex"):
            all_labels.update(re.findall(
                r"\\label\{([^}]+)\}", source.read_text("utf8")
            ))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 30)
        self.assertEqual(set(refs) - all_labels, set())
        self.assertIn("ch:forcing-continuum", refs)
        self.assertIn("thm:boolean35-zfc", refs)

    def test_exact_relative_consistency_is_proved(self):
        self.assertIn(r"\label{thm:boolean35-relative-consistency}", TEXT)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC}+\mathrm{CH})", TEXT)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC}+\neg\mathrm{CH})", TEXT)
        self.assertIn(r"\label{thm:boolean35-two-algebras}", TEXT)
        self.assertIn(r"\label{thm:boolean35-quotient-zfc}", TEXT)
        self.assertIn("twierdzenia Gödla o pełności", TEXT)
        self.assertIn("nie będziemy zakładać", TEXT)

    def test_proper_classes_and_witness_selection(self):
        for mark in (
            r"\label{lem:boolean35-well-defined}",
            r"\label{lem:boolean35-mixing}",
            r"\label{thm:boolean35-fullness}",
            r"\label{thm:boolean35-quotient-truth}",
        ):
            self.assertIn(mark, TEXT)
        self.assertIn(r"S_\varphi", TEXT)
        self.assertIn(r"V_{\gamma+1}^{\mathbb B}", TEXT)
        self.assertIn("najmniejszą rangę", TEXT)
        self.assertIn("klasą właściwą", TEXT)
        self.assertIn("zastępowanie", TEXT)

    def test_zfc_axioms_addressed_explicitly(self):
        for name in (
            "Ekstensjonalność", "Pusty zbiór, para i nieskończoność",
            "Aksjomat sumy", "Schemat wyróżniania",
            "Aksjomat zbioru potęgowego", "Schemat zastępowania",
            "Aksjomat ufundowania", "Aksjomat wyboru",
        ):
            with self.subTest(axiom=name):
                self.assertIn(name, TEXT)
        self.assertIn(r"\Pi_\sigma", TEXT)
        self.assertIn(r"f_\tau(\rho)", TEXT)
        self.assertIn(r"\check\omega", TEXT)

    def test_not_confusing_countable_transitive_and_arbitrary_models(self):
        self.assertIn(r"|M|", TEXT)
        self.assertIn(r"\in^M", TEXT)
        self.assertIn(r"\mathbb B^M", TEXT)
        self.assertIn("nietranzytywnym", TEXT)
        self.assertIn("zewnętrznym ultrafiltrem", TEXT)
        self.assertIn(r"\label{rem:boolean35-ill-founded}", TEXT)
        self.assertIn("Mostowskiego", TEXT)

    def test_regular_open_completion_of_finite_fork(self):
        # Basic opens are downward-closed sets in a three-node fork.
        P = ("top", "left", "right")
        order = {
            ("top", "top"), ("left", "left"), ("right", "right"),
            ("left", "top"), ("right", "top"),
        }
        all_subsets = [
            frozenset(x)
            for size in range(len(P) + 1)
            for x in combinations(P, size)
        ]

        def leq(q, p):
            return (q, p) in order

        def interior(S):
            return frozenset(
                p for p in P
                if all(q in S for q in P if leq(q, p))
            )

        def closure(S):
            return frozenset(
                p for p in P
                if any(leq(q, p) and q in S for q in P)
            )

        ro = {
            S for S in all_subsets
            if interior(closure(S)) == S
        }
        empty, left, right, entire = (
            frozenset(), frozenset({"left"}),
            frozenset({"right"}), frozenset(P)
        )
        self.assertEqual(ro, {empty, left, right, entire})
        for A in ro:
            for B in ro:
                self.assertIn(A & B, ro)
                join = interior(closure(A | B))
                self.assertIn(join, ro)
        self.assertEqual(interior(closure(left | right)), entire)
        self.assertIn(r"\operatorname{RO}(\mathbb P)", TEXT)

    def test_exhaustive_four_valued_atomic_truth(self):
        # B=P({0,1}) encoded as bitmasks 0,1,2,3.
        # Truth at the principal ultrafilter on atom 1/2 must coincide
        # with evaluation of names as finite hereditarily finite sets.
        empty = frozenset()
        singleton = frozenset({(empty, 3)})
        pairs = [(name, b) for name in (empty, singleton) for b in (1, 2, 3)]
        names = list(dict.fromkeys(
            [empty, singleton] + [
                frozenset(selected)
                for k in range(3)
                for selected in combinations(pairs, k)
            ]
        ))

        @lru_cache(None)
        def atom_member(sigma, tau):
            result = 0
            for pi, value in tau:
                result |= value & atom_equal(sigma, pi)
            return result

        @lru_cache(None)
        def atom_equal(sigma, tau):
            result = 3
            for pi, value in sigma:
                result &= (3 ^ value) | atom_member(pi, tau)
            for pi, value in tau:
                result &= (3 ^ value) | atom_member(pi, sigma)
            return result

        @lru_cache(None)
        def evaluate(name, atom):
            return frozenset(
                evaluate(pi, atom)
                for pi, coefficient in name if coefficient & atom
            )

        total = 0
        for sigma in names:
            for tau in names:
                for atom in (1, 2):
                    x, y = evaluate(sigma, atom), evaluate(tau, atom)
                    self.assertEqual(
                        x in y, bool(atom_member(sigma, tau) & atom)
                    )
                    self.assertEqual(
                        x == y, bool(atom_equal(sigma, tau) & atom)
                    )
                    total += 2
        self.assertGreaterEqual(total, 1000)

    def test_mixing_and_fullness_with_two_atoms(self):
        # One name codes the empty set on the first atom and
        # its singleton on the second; existential witnesses can be mixed.
        empty = frozenset()
        one = frozenset({(empty, 3)})
        target = frozenset({(empty, 1), (one, 2)})
        mixture = frozenset({(empty, 2)})

        @lru_cache(None)
        def member(sigma, tau):
            return self.join([
                value & equal(sigma, pi) for pi, value in tau
            ])

        @lru_cache(None)
        def equal(sigma, tau):
            v = 3
            for pi, b in sigma:
                v &= (3 ^ b) | member(pi, tau)
            for pi, b in tau:
                v &= (3 ^ b) | member(pi, sigma)
            return v

        self.assertEqual(equal(mixture, empty) & 1, 1)
        self.assertEqual(equal(mixture, one) & 2, 2)
        self.assertEqual(member(empty, target), 1)
        self.assertEqual(member(one, target), 2)
        self.assertEqual(member(mixture, target), 3)

    @staticmethod
    def join(items):
        value = 0
        for item in items:
            value |= item
        return value

    def test_ultrafilter_quotient_soundness_on_boolean_propositions(self):
        B = range(4)
        U0, U1 = {1, 3}, {2, 3}
        for U in (U0, U1):
            self.assertIn(3, U)
            self.assertNotIn(0, U)
            for a in B:
                self.assertEqual((a in U), ((3 ^ a) not in U))
                for b in B:
                    self.assertEqual(
                        ((a & b) in U), (a in U and b in U)
                    )
        self.assertIn(1, U0)
        self.assertNotIn(1, U1)
        self.assertIn(2, U1)
        self.assertNotIn(2, U0)
        self.assertIn(r"\label{ex:boolean35-four}", TEXT)


if __name__ == "__main__":
    unittest.main()
