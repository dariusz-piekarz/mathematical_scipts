"""Chapter 38: club/stationary sets, Mahlo and weak compactness.

These tests inspect integration and bounded combinatorial analogues only;
no finite calculation proves Fodor's lemma or large-cardinal existence.
"""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "chapters/pl/logic_and_set_theory"
FILENAME = "38-kardynaly-mahla-i-slaba-zwartosc.tex"
TEXT = (DIRECTORY / FILENAME).read_text(encoding="utf-8")


def homogeneous_triangle(edges, n):
    """Return a monochromatic triple, or None."""
    for a, b, c in itertools.combinations(range(n), 3):
        colors = {edges[(a, b)], edges[(a, c)], edges[(b, c)]}
        if len(colors) == 1:
            return (a, b, c)
    return None


def diagonal_intersection(sets):
    """Finite evaluation of the defining formula (without club claims)."""
    return frozenset(
        alpha for alpha in range(len(sets))
        if all(alpha in sets[xi] for xi in range(alpha))
    )


class TestChapter38(unittest.TestCase):
    def test_catalog_position_and_input(self):
        data = json.loads((ROOT / "catalog/books.json").read_text("utf-8"))
        book = next(b for b in data["books"] if b["id"] == "logic_and_set_theory")
        self.assertGreaterEqual(len(book["chapters"]), 38)
        self.assertEqual(book["chapters"][37],
                         f"chapters/pl/logic_and_set_theory/{FILENAME}")
        main = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf-8")
        self.assertIn(r"\input{../../chapters/pl/logic_and_set_theory/" +
                      FILENAME + "}", main)

    def test_exact_environment_inventory_and_balance(self):
        counts = {"definicja": 8, "lemat": 4, "twierdzenie": 5,
                  "wniosek": 1, "uwaga": 5, "przyklad": 2,
                  "proof": 10, "figure": 0}
        for env, expected in counts.items():
            self.assertEqual(TEXT.count(r"\begin{" + env + "}"), expected, env)
        stack = []
        for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if kind == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertEqual(stack, [])

    def test_labels_references_and_terminology(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 26)
        self.assertEqual(len(set(labels)), 26)
        self.assertEqual(len(refs), 19)
        existing = set()
        for path in DIRECTORY.glob("*.tex"):
            existing.update(re.findall(r"\\label\{([^}]+)\}",
                                       path.read_text("utf-8")))
        self.assertFalse(set(refs) - existing)
        for bad in ("unia zbiorów", "zwartościowanie", "sekwencyjny",
                    "pierwszoprzeliczalna", "drugoprzeliczalna",
                    "tensorowanie"):
            self.assertNotIn(bad, TEXT.lower())

    def test_required_results_and_no_unproven_converse(self):
        required = (
            "thm:lc38-fodor", "lem:lc38-club-intersections",
            "lem:lc38-diagonal-club", "def:lc38-mahlo",
            "def:lc38-weak-compact", "thm:lc38-measurable-tree",
            "thm:lc38-measurable-mahlo",
            "thm:lc38-measurable-partition", "cor:lc38-hierarchy",
        )
        for label in required:
            with self.subTest(label=label):
                self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn("Nie dowodziliśmy odwrotnych", TEXT)
        self.assertIn(r"\ref{thm:lc37-measurable-inaccessible}", TEXT)
        self.assertIn(r"\ref{lem:lc37-uniform}", TEXT)

    def test_binary_tree_level_sizes_and_branch_coherence(self):
        for height in range(1, 9):
            levels = [
                list(itertools.product((0, 1), repeat=alpha))
                for alpha in range(height)
            ]
            for alpha, level in enumerate(levels):
                self.assertEqual(len(level), 2 ** alpha)
                for node in level:
                    self.assertEqual(len(node), alpha)
            branch = [tuple(0 for _ in range(a)) for a in range(height)]
            self.assertTrue(all(branch[a] in levels[a]
                                for a in range(height)))
            self.assertTrue(all(branch[a] == branch[b][:a]
                                for a in range(height)
                                for b in range(a + 1, height)))

    def test_finite_diagonal_definition_exhaustive(self):
        points = frozenset(range(3))
        subsets = [
            frozenset(x for x in points if mask & (1 << x))
            for mask in range(8)
        ]
        checked = 0
        for family in itertools.product(subsets, repeat=3):
            d = diagonal_intersection(family)
            for alpha in range(3):
                self.assertEqual(alpha in d,
                                 all(alpha in family[xi]
                                     for xi in range(alpha)))
                checked += 1
        self.assertEqual(checked, 1536)

    def test_finite_ramsey_r33_is_six(self):
        """Every two-coloring of [6]^2 has a monochromatic triple."""
        pairs = tuple(itertools.combinations(range(6), 2))
        self.assertEqual(len(pairs), 15)
        for mask in range(1 << len(pairs)):
            edges = {
                pair: (mask >> k) & 1
                for k, pair in enumerate(pairs)
            }
            self.assertIsNotNone(homogeneous_triangle(edges, 6))

    def test_five_vertex_coloring_without_triangle(self):
        """The pentagon coloring shows the analogous 5-vertex claim fails."""
        edge_colors = {}
        for a, b in itertools.combinations(range(5), 2):
            edge_colors[(a, b)] = int((b - a) not in (1, 4) and
                                      (a - b) not in (1, 4))
        # The polygon edges are 0; diagonals are 1.
        edge_colors[(0, 4)] = 0
        self.assertIsNone(homogeneous_triangle(edge_colors, 5))

    def test_diagonal_intersection_tail_behavior(self):
        # A toy stress test of the strict index bound xi < alpha.
        for n in range(1, 8):
            family = [
                frozenset(range(xi + 1, n))
                for xi in range(n)
            ]
            d = diagonal_intersection(family)
            self.assertEqual(d, frozenset(range(n)))


if __name__ == "__main__":
    unittest.main()
