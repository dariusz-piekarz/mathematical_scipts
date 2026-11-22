"""Chapter 36 — symmetric Cohen models and the failure of AC.

Finite forcing tests are bounded regressions, not a proof of ZF or
a machine-checked formalization of relative consistency.
"""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/logic_and_set_theory"
NAME = "36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex"
SOURCE = CHAPTERS / NAME
TEXT = SOURCE.read_text(encoding="utf-8")


def compatible(p, q):
    """Partial Cohen functions are compatible iff their overlap agrees."""
    return all(point not in q or q[point] == bit for point, bit in p.items())


def apply_perm(p, pi):
    return {(pi.get(row, row), k): bit for (row, k), bit in p.items()}


class TestSymmetricChoiceChapter36(unittest.TestCase):
    def test_registered_in_book_and_catalog(self):
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf-8")
        catalog = json.loads((ROOT / "catalog/books.json").read_text("utf-8"))
        entry = next(b for b in catalog["books"] if b["id"] == "logic_and_set_theory")
        self.assertGreaterEqual(len(entry["chapters"]), 36)
        self.assertEqual(entry["chapters"][35], f"chapters/pl/logic_and_set_theory/{NAME}")
        self.assertIn(r"\input{../../chapters/pl/logic_and_set_theory/" + NAME + "}", book)
        self.assertIn(r"\label{ch:symmetric-choice}", TEXT)

    def test_environment_inventory_and_labels(self):
        counts = {
            "definicja": 5, "lemat": 7, "twierdzenie": 4,
            "uwaga": 3, "przyklad": 1, "proof": 12,
        }
        stack = []
        for act, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if act == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for env, expected in counts.items():
            with self.subTest(environment=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), expected)
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 21)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(all(name.startswith(
            ("ch:symmetric-", "def:sym36-", "lem:sym36-",
             "thm:sym36-", "rem:sym36-", "ex:sym36-")
        ) for name in labels))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 27)
        available = set()
        for chapter in CHAPTERS.glob("*.tex"):
            available.update(re.findall(
                r"\\label\{([^}]+)\}", chapter.read_text("utf-8")
            ))
        self.assertFalse(set(refs) - available, set(refs) - available)

    def test_critical_formulas_and_no_unwanted_conflation(self):
        for part in (
            r"\operatorname{Con}(\mathrm{ZFC})",
            r"\operatorname{Con}(\mathrm{ZF}+\neg\mathrm{AC})",
            r"\label{thm:sym36-truth}",
            r"\label{thm:sym36-zf}",
            r"\label{thm:sym36-dedekind}",
            r"\label{lem:sym36-arbitrary-model}",
            r"\label{thm:sym36-relative-consistency}",
            "daje automatycznie modelu ZF+AD",
        ):
            self.assertIn(part, TEXT)
        for bad in (
            "unia zbiorów", "zwartościowanie",
            "pierwszoprzeliczalna", "drugoprzeliczalna",
        ):
            self.assertNotIn(bad, TEXT)

    def test_permutation_preserves_order_and_compatibility(self):
        coords = [(i, k) for i in range(3) for k in range(2)]
        maps = []
        for values in itertools.product((None, 0, 1), repeat=len(coords)):
            maps.append({
                coordinate: bit for coordinate, bit in zip(coords, values)
                if bit is not None
            })
        perms = list(itertools.permutations(range(3)))
        for perm_tuple in perms:
            pi = dict(enumerate(perm_tuple))
            for i in range(0, len(maps), 23):
                p = maps[i]
                pp = apply_perm(p, pi)
                self.assertEqual(len(p), len(pp))
                for q in (maps[(i + 5) % len(maps)], maps[(i * 3 + 7) % len(maps)]):
                    self.assertEqual(compatible(p, q),
                                     compatible(pp, apply_perm(q, pi)))
                    if set(q.items()).issuperset(set(p.items())):
                        self.assertTrue(
                            set(apply_perm(q, pi).items()).issuperset(
                                set(pp.items()))
                        )

    def test_fresh_coordinate_always_distinguishes_two_rows(self):
        rows = (0, 1)
        coords = [(i, k) for i in rows for k in range(3)]
        checked = 0
        for values in itertools.product((None, 0, 1), repeat=len(coords)):
            p = {
                point: bit for point, bit in zip(coords, values)
                if bit is not None
            }
            free = 3
            self.assertNotIn((0, free), p)
            self.assertNotIn((1, free), p)
            q = dict(p)
            q[(0, free)] = 0
            q[(1, free)] = 1
            self.assertTrue(compatible(p, q))
            self.assertTrue(set(q.items()).issuperset(set(p.items())))
            self.assertNotEqual(q[(0, free)], q[(1, free)])
            checked += 1
        self.assertEqual(checked, 729)

    def test_finite_support_swap_compatible_with_original_condition(self):
        coords = [(row, k) for row in range(3) for k in range(2)]
        checked = 0
        for values in itertools.product((None, 0, 1), repeat=len(coords)):
            p = {
                point: bit for point, bit in zip(coords, values)
                if bit is not None
            }
            for E in (frozenset(), frozenset((0,)), frozenset((1,))):
                for k in range(3):
                    if k in E:
                        continue
                    ell = max([k, *E, *(row for row, _ in p)], default=0) + 1
                    pi = {k: ell, ell: k}
                    self.assertTrue(all(pi.get(x, x) == x for x in E))
                    self.assertTrue(compatible(p, apply_perm(p, pi)))
                    checked += 1
        self.assertEqual(checked, 729 * (3 + 2 + 2))

    def test_nontransitive_model_distinction_and_truth_lemma(self):
        self.assertIn("Nie zakładamy zewnętrznego dobrego ufundowania", TEXT)
        self.assertIn("przeliczalnym modelem zbiorowym", TEXT)
        self.assertIn(r"\sigma\equiv_G\tau", TEXT)
        self.assertIn(r"\Vdash_{\mathrm{HS}}", TEXT)
        self.assertIn("przez filtr generyczny", TEXT)
        self.assertIn("Klasy i relacja są \\emph{zbiorami zewnętrznymi}", TEXT)


    def test_atomic_row_membership_equivariance_and_dense_splitting(self):
        # A separate finite check of both bit values under S_3.
        # This does not prove genericity on the infinite Cohen forcing.
        coords = [(row, bit) for row in range(3) for bit in range(2)]
        conditions = [
            {
                cell: v for cell, v in zip(coords, assignment)
                if v != 2
            }
            for assignment in itertools.product((0, 1, 2), repeat=6)
        ]
        checked = 0
        for perm in itertools.permutations(range(3)):
            pi = dict(enumerate(perm))
            for p in conditions:
                q = apply_perm(p, pi)
                for row, k in coords:
                    self.assertEqual(
                        p.get((row, k)) == 1,
                        q.get((pi[row], k)) == 1,
                    )
                    self.assertEqual(
                        p.get((row, k)) == 0,
                        q.get((pi[row], k)) == 0,
                    )
                    checked += 2
        self.assertEqual(checked, 52488)

        split_checks = 0
        for p in conditions:
            for row in range(3):
                for other in range(row + 1, 3):
                    k = max(
                        (n for (r, n) in p if r in (row, other)),
                        default=-1,
                    ) + 1
                    q = dict(p)
                    q[(row, k)] = 0
                    q[(other, k)] = 1
                    self.assertTrue(compatible(p, q))
                    self.assertTrue(
                        set(q.items()).issuperset(set(p.items()))
                    )
                    self.assertNotEqual(q[(row, k)], q[(other, k)])
                    split_checks += 1
        self.assertEqual(split_checks, 2187)



if __name__ == "__main__":
    unittest.main()
