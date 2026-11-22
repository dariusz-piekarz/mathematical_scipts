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
        self.assertEqual(len(refs), 23)
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

    def test_maximal_antichain_predensity_for_deciding_values(self):
        # Finite counterpart of the ccc proof: the two conditions fixing
        # one bit form a maximal antichain of the dense decision set.
        conditions = [
            {i: x for i, x in enumerate(bits) if x is not None}
            for bits in product((None, 0, 1), repeat=3)
        ]

        def strengthens(q, p):
            return all(q.get(i) == x for i, x in p.items())

        def compatible(p, q):
            return all(p[i] == q[i] for i in p.keys() & q.keys())

        checked = 0
        for coordinate in range(3):
            D = [p for p in conditions if coordinate in p]
            antichain = [{coordinate: 0}, {coordinate: 1}]
            self.assertTrue(all(p in D for p in antichain))
            self.assertFalse(compatible(*antichain))
            for r in conditions:
                self.assertTrue(any(strengthens(d, r) for d in D))
                self.assertTrue(any(compatible(r, a) for a in antichain))
                self.assertTrue(
                    any(
                        strengthens(q, r) and
                        any(strengthens(q, a) for a in antichain)
                        for q in conditions
                    )
                )
                checked += 1
            for bits in product((0, 1), repeat=3):
                G = [
                    p for p in conditions
                    if all(bits[i] == v for i, v in p.items())
                ]
                meeting = [a for a in antichain if a in G]
                self.assertEqual(len(meeting), 1)
                self.assertEqual(meeting[0][coordinate], bits[coordinate])
        self.assertEqual(checked, 81)
        self.assertIn("maksymalność", TEXT)
        self.assertIn("Zastosowanie aksjomatu wyboru", TEXT)

    def test_exhaustive_maximal_antichains_in_finite_tree(self):
        # The key ccc proof implication is tested for *every* dense
        # subset D below p and every maximal antichain A contained in D,
        # not just an illustrative chosen antichain.
        P = ((), (0,), (1,), (0, 0), (0, 1), (1, 0), (1, 1))

        def below(q, p):
            return q[:len(p)] == p

        def compatible(q, p):
            return any(below(r, q) and below(r, p) for r in P)

        def subfamilies(items):
            return (
                frozenset(x)
                for k in range(len(items) + 1)
                for x in combinations(items, k)
            )

        dense_count = 0
        maximal_count = 0
        for p in P:
            cone = tuple(q for q in P if below(q, p))
            for D in subfamilies(cone):
                if not all(any(below(d, q) for d in D) for q in cone):
                    continue
                dense_count += 1
                for A in subfamilies(tuple(D)):
                    if any(compatible(a, b) for a, b in combinations(A, 2)):
                        continue
                    if any(
                        not any(compatible(d, a) for a in A) for d in D
                    ):
                        continue
                    maximal_count += 1
                    # Maximality within D gives predensity below p.
                    self.assertTrue(all(
                        any(compatible(q, a) for a in A) for q in cone
                    ))
                    # Local predensity gives a globally dense E.
                    E = {
                        q for q in P
                        if any(below(q, a) for a in A)
                        or not compatible(q, p)
                    }
                    self.assertTrue(all(
                        any(below(s, q) for s in E) for q in P
                    ))
                    # Every generic branch containing p meets A
                    # in exactly one condition.
                    for leaf in P[-4:]:
                        G = {q for q in P if below(leaf, q)}
                        if p in G:
                            self.assertEqual(len(A & G), 1)
        self.assertEqual(dense_count, 16)
        self.assertEqual(maximal_count, 32)

    def test_countable_closure_proof_restarts_below_every_condition(self):
        # Finite analogue of the corrected density argument:
        # every initial partial condition has a common strengthening
        # deciding all four coordinates, not merely the top condition.
        cases = 0
        for bits in product((None, 0, 1), repeat=4):
            initial = {
                n: value for n, value in enumerate(bits)
                if value is not None
            }
            chain = [initial]
            for n in range(4):
                next_condition = dict(chain[-1])
                next_condition.setdefault(n, 0)
                chain.append(next_condition)
            lower_bound = chain[-1]
            self.assertEqual(set(lower_bound), set(range(4)))
            for previous in chain:
                self.assertTrue(all(
                    lower_bound[n] == v for n, v in previous.items()
                ))
            cases += 1
        self.assertEqual(cases, 81)
        self.assertIn(r"\emph{dowolny}", TEXT)
        self.assertIn(r"q\Vdash\dot f=\check g", TEXT)
        self.assertIn("gęsty poniżej $p$", TEXT)

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
