"""Chapter 37: inaccessible and measurable cardinals, ultrapowers.

Finite checks only. They cannot verify the existence of a large cardinal,
the class ultrapower theorem, or any consistency result.
"""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "chapters/pl/logic_and_set_theory"
NAME = "37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex"
SOURCE = DIRECTORY / NAME
TEXT = SOURCE.read_text("utf-8")


def powerset(items):
    items = tuple(items)
    return frozenset(
        frozenset(items[i] for i in range(len(items)) if mask & (1 << i))
        for mask in range(1 << len(items))
    )


def finite_principal_ultrafilter(n, at):
    universe = frozenset(range(n))
    return frozenset(
        x for x in powerset(universe) if at in x
    )


class TestLargeCardinalsChapter37(unittest.TestCase):
    def test_book_registration_and_catalog(self):
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf-8")
        doc = json.loads((ROOT / "catalog/books.json").read_text("utf-8"))
        entry = next(e for e in doc["books"] if e["id"] == "logic_and_set_theory")
        self.assertGreaterEqual(len(entry["chapters"]), 37)
        self.assertEqual(entry["chapters"][36], f"chapters/pl/logic_and_set_theory/{NAME}")
        self.assertIn(r"\input{../../chapters/pl/logic_and_set_theory/" + NAME + "}", book)
        self.assertIn(r"\label{ch:large-cardinals}", TEXT)

    def test_environment_inventory_and_reference_integrity(self):
        expected = {
            "definicja": 7, "lemat": 4, "twierdzenie": 7,
            "wniosek": 1, "uwaga": 5, "przyklad": 1, "proof": 12,
        }
        for env, count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), count)
        st = []
        for verb, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if verb == "begin":
                st.append(env)
            else:
                self.assertTrue(st)
                self.assertEqual(st.pop(), env)
        self.assertFalse(st)
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 26)
        self.assertEqual(len(set(labels)), 26)
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 18)
        all_labels = set()
        for chapter in DIRECTORY.glob("*.tex"):
            all_labels.update(re.findall(
                r"\\label\{([^}]+)\}", chapter.read_text("utf-8")))
        self.assertFalse(set(refs) - all_labels, set(refs) - all_labels)

    def test_mathematical_scope_and_terminology(self):
        required = [
            r"\label{thm:lc37-rank-model}",
            r"\label{thm:lc37-measurable-inaccessible}",
            r"\label{thm:lc37-los}",
            r"\label{thm:lc37-embedding}",
            r"\label{thm:lc37-normal-diagonal}",
            r"\label{thm:lc37-normal-exists}",
            r"\label{cor:lc37-inaccessible-con}",
            r"\ref{ch:second-incompleteness}",
            "niegłównym",
            "zbiorolokalna",
            "nie są formalizacją",
        ]
        for item in required:
            with self.subTest(item=item):
                self.assertIn(item, TEXT)
        for bad in ["unia zbiorów", "zwartościowanie", "sekwencyjny",
                    "pierwszoprzeliczalna", "drugoprzeliczalna"]:
            self.assertNotIn(bad, TEXT)

    def test_rank_hierarchy_small_finite_levels(self):
        ranks = [frozenset()]
        for _ in range(4):
            ranks.append(powerset(ranks[-1]))
        self.assertEqual([len(v) for v in ranks], [0, 1, 2, 4, 16])
        for i in range(1, len(ranks)):
            self.assertTrue(ranks[i - 1].issubset(ranks[i]))
        for i in range(1, len(ranks) - 1):
            self.assertEqual(len(ranks[i + 1]), 2 ** len(ranks[i]))

    def test_every_ultrafilter_on_finite_set_is_principal(self):
        for n in (1, 2, 3):
            universe = frozenset(range(n))
            subsets = tuple(powerset(universe))
            candidates = 0
            for mask in range(1 << len(subsets)):
                F = {subsets[i] for i in range(len(subsets)) if mask & (1 << i)}
                if universe not in F or frozenset() in F:
                    continue
                if any((A in F) == ((universe - A) in F) for A in subsets):
                    continue
                if any((A & B) not in F for A in F for B in F):
                    continue
                if any(B not in F for A in F for B in subsets if A <= B):
                    continue
                candidates += 1
                self.assertTrue(any(frozenset((p,)) in F for p in range(n)))
            self.assertEqual(candidates, n)

    def test_principal_ultrafilter_finite_los_boolean_clauses(self):
        # Each finite principal ultrapower is evaluation at its generator.
        n = 3
        I = frozenset(range(n))
        for at in range(n):
            U = finite_principal_ultrafilter(n, at)
            fs = tuple(itertools.product(range(3), repeat=n))
            for f in fs:
                for g in fs:
                    equality_indices = frozenset(i for i in I if f[i] == g[i])
                    membership_indices = frozenset(i for i in I if f[i] < g[i])
                    self.assertEqual(equality_indices in U, f[at] == g[at])
                    self.assertEqual(membership_indices in U, f[at] < g[at])
                    self.assertEqual((I - equality_indices) in U, f[at] != g[at])
            # Existential witnesses must be chosen as index-dependent functions.
            for f in fs:
                witnesses = tuple(itertools.product(range(3), repeat=n))
                satisfies = any(
                    frozenset(i for i in I if g[i] < f[i]) in U
                    for g in witnesses
                )
                indices = frozenset(i for i in I if f[i] > 0)
                self.assertEqual(satisfies, indices in U)

    def test_normality_diagonal_intersection_for_finite_principal_filters(self):
        n = 3
        for at in range(n):
            U = finite_principal_ultrafilter(n, at)
            for family in itertools.product(U, repeat=n):
                diag = frozenset(
                    a for a in range(n)
                    if all(a in family[b] for b in range(a))
                )
                self.assertIn(diag, U)

    def test_small_complements_analogy(self):
        # Finite analogue of intersecting complements of all singletons.
        I = frozenset(range(4))
        comps = [I - {a} for a in I]
        self.assertEqual(frozenset.intersection(*comps), frozenset())
        # This must NOT be used to claim nonprincipal finite filters exist.
        self.assertFalse(any(
            all(x in finite_principal_ultrafilter(4, a) for x in comps)
            for a in I
        ))


if __name__ == "__main__":
    unittest.main()
