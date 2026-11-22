"""Chapter 39: finite test models for tree / partition / logic equivalences.

These are bounded consistency checks for definitions and proof architecture.
They do not establish the infinite large-cardinal theorems or formalize them.
"""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "chapters/pl/logic_and_set_theory"
NAME = "39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex"
TEXT = (DIRECTORY / NAME).read_text(encoding="utf-8")


def finite_binary_tree(height):
    return tuple(
        node
        for level in range(height)
        for node in itertools.product((0, 1), repeat=level)
    )


def comparable(s, t):
    return s == t[:len(s)] or t == s[:len(t)]


def satisfaction_for_tree(nodes, chosen, height):
    level_clauses = all(
        any(node in chosen for node in nodes if len(node) == level)
        for level in range(height)
    )
    incompatibility_clauses = all(
        comparable(a, b) for a in chosen for b in chosen
    )
    return level_clauses and incompatibility_clauses


class Chapter39Audits(unittest.TestCase):
    def test_book_and_catalog(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text("utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "logic_and_set_theory")
        self.assertGreaterEqual(len(book["chapters"]), 39)
        self.assertEqual(book["chapters"][38],
                         f"chapters/pl/logic_and_set_theory/{NAME}")
        source = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf-8")
        self.assertIn(r"\input{../../chapters/pl/logic_and_set_theory/" + NAME + "}",
                      source)

    def test_env_inventory_and_balance(self):
        expected = {
            "definicja": 4, "lemat": 4, "twierdzenie": 6,
            "wniosek": 2, "uwaga": 4, "przyklad": 1,
            "proof": 12, "figure": 0,
        }
        stack = []
        for action, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if action == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertEqual(stack, [])
        for env, n in expected.items():
            self.assertEqual(TEXT.count(r"\begin{" + env + "}"), n, env)

    def test_labels_and_references(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 22)
        self.assertEqual(len(set(labels)), len(labels))
        self.assertEqual(len(refs), 25)
        all_labels = set()
        for path in DIRECTORY.glob("*.tex"):
            all_labels.update(re.findall(
                r"\\label\{([^}]+)\}", path.read_text("utf-8")))
        self.assertFalse(set(refs) - all_labels, set(refs) - all_labels)

    def test_no_abbreviated_cardinal_noun_in_any_chapter(self):
        # Every Polish chapter must use the full noun "liczba kardynalna".
        # This checks file contents, not legacy filenames or labels.
        bad = re.compile(r"(?iu)\bkardynał(?:u|em|owi|y|ów|ami|ach)?\b")
        for chapter in DIRECTORY.glob("*.tex"):
            src = chapter.read_text("utf-8")
            self.assertIsNone(bad.search(src), chapter.name)

    def test_required_equivalences_are_explicit(self):
        for label in (
            "thm:lc39-main-equivalence",
            "thm:lc39-tree-to-partition",
            "thm:lc39-partition-to-tree",
            "thm:lc39-tree-to-compactness",
            "thm:lc39-compactness-to-tree",
            "cor:lc39-tree-partition",
            "cor:lc39-compactness-equivalence",
            "thm:lc39-partition-regular",
        ):
            with self.subTest(label=label):
                self.assertIn(r"\label{" + label + "}", TEXT)
        self.assertIn("nie utożsamiamy jej bez dowodu", TEXT.lower())
        self.assertIn(r"$L_{\kappa,\kappa}$", TEXT)

    def test_profile_tree_restrictions_on_finite_colorings(self):
        # Every finite two-coloring induces a prefix-closed profile tree.
        for n in (3, 4):
            pairs = tuple(itertools.combinations(range(n), 2))
            for pattern in itertools.product((0, 1), repeat=len(pairs)):
                coloring = dict(zip(pairs, pattern))
                profiles = {
                    alpha: tuple(coloring[(xi, alpha)] for xi in range(alpha))
                    for alpha in range(n)
                }
                levels = [
                    {profiles[alpha][:delta] for alpha in range(delta, n)}
                    for delta in range(n)
                ]
                self.assertTrue(all(levels))
                for delta, level in enumerate(levels):
                    self.assertLessEqual(len(level), 2 ** delta)
                    for v in level:
                        for gamma in range(delta):
                            self.assertIn(v[:gamma], levels[gamma])

    def test_lexicographic_extension_separates_incompatible_cones(self):
        nodes = finite_binary_tree(5)
        for s in nodes:
            for t in nodes:
                if comparable(s, t) or not s < t:
                    continue
                ext_s = [u for u in nodes if u[:len(s)] == s]
                ext_t = [u for u in nodes if u[:len(t)] == t]
                self.assertTrue(all(u < v for u in ext_s for v in ext_t))

    def test_finite_propositional_branch_theory_iff_chain(self):
        # Propositional variables are nodes; clauses say there is a node
        # at each level and forbid simultaneously selecting incompatible ones.
        for height in (3, 4):
            nodes = finite_binary_tree(height)
            good = 0
            for mask in range(1 << len(nodes)):
                chosen = {
                    node for i, node in enumerate(nodes)
                    if mask & (1 << i)
                }
                value = satisfaction_for_tree(nodes, chosen, height)
                expected = (
                    all(any(len(t) == lev for t in chosen)
                        for lev in range(height))
                    and all(comparable(a, b)
                            for a in chosen for b in chosen)
                )
                self.assertEqual(value, expected)
                good += int(value)
            self.assertEqual(good, 2 ** (height - 1))

    def test_local_satisfaction_respects_small_support(self):
        # A finite analogue: if a formula uses only indices S, the
        # truth value is unaffected by changing coordinates outside S.
        n = 5
        support = {0, 2, 4}
        vals = list(itertools.product((0, 1), repeat=n))
        phi = lambda v: (v[0] and not v[2]) or v[4]
        for v in vals:
            for w in vals:
                if all(v[i] == w[i] for i in support):
                    self.assertEqual(phi(v), phi(w))


    def test_three_color_profile_bounds_finite(self):
        for n in (3, 4):
            pairs = tuple(itertools.combinations(range(n), 2))
            for pattern in itertools.product((0, 1, 2), repeat=len(pairs)):
                colors = dict(zip(pairs, pattern))
                profiles = {
                    a: tuple(colors[(b, a)] for b in range(a))
                    for a in range(n)
                }
                for delta in range(n):
                    nodes = {profiles[a][:delta] for a in range(delta, n)}
                    self.assertTrue(nodes)
                    self.assertLessEqual(len(nodes), 3 ** delta)
                    for node in nodes:
                        for gamma in range(delta):
                            self.assertIn(
                                node[:gamma],
                                {profiles[a][:gamma] for a in range(gamma, n)},
                            )

    def test_pruned_binary_tree_branch_constraints(self):
        # Exhaust all nonempty subsets of the four top-level leaves.
        full = finite_binary_tree(3)
        leaves = tuple(x for x in full if len(x) == 2)
        for mask in range(1, 1 << len(leaves)):
            kept_leaves = [x for i, x in enumerate(leaves) if mask & (1 << i)]
            nodes = tuple(
                x for x in full
                if any(leaf[:len(x)] == x for leaf in kept_leaves)
            )
            satisfying = 0
            for valuation in range(1 << len(nodes)):
                chosen = {
                    node for i, node in enumerate(nodes)
                    if valuation & (1 << i)
                }
                satisfying += int(satisfaction_for_tree(nodes, chosen, 3))
            self.assertEqual(satisfying, len(kept_leaves))



if __name__ == "__main__":
    unittest.main()
