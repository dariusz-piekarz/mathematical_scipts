"""Chapter 33: forcing theorem, definability, truth lemma and ZFC extension."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER_DIR = ROOT / "chapters/pl/logic_and_set_theory"
SOURCE = CHAPTER_DIR / "33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex"
TEXT = SOURCE.read_text(encoding="utf8")


class TestChapter33(unittest.TestCase):
    def test_integrated_book_catalog(self):
        entry = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf8")
        catalog = (ROOT / "catalog/books.json").read_text("utf8")
        self.assertIn(SOURCE.name, entry)
        self.assertIn(SOURCE.name, catalog)
        self.assertIn(r"\label{ch:forcing-theorem}", TEXT)
        self.assertIn(r"\ref{ch:forcing-foundations}", TEXT)

    def test_complete_environment_inventory(self):
        counts = {
            "definicja": 4, "lemat": 6, "twierdzenie": 6,
            "wniosek": 0, "przyklad": 3, "uwaga": 5,
            "proof": 12, "figure": 0,
        }
        stack = []
        for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", TEXT):
            if op == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for env, expected in counts.items():
            with self.subTest(environment=env):
                self.assertEqual(TEXT.count(r"\begin{" + env + "}"), expected)
                self.assertEqual(TEXT.count(r"\end{" + env + "}"), expected)
        labels = re.findall(r"\\label\{([^}]+)\}", TEXT)
        self.assertEqual(len(labels), 25)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(all(name.startswith(("ch:forcing-", "def:forcing33-",
            "lem:forcing33-", "thm:forcing33-", "rem:forcing33-",
            "ex:forcing33-")) for name in labels))

    def test_all_refs_resolve(self):
        all_labels = set()
        for path in CHAPTER_DIR.glob("*.tex"):
            all_labels.update(re.findall(
                r"\\label\{([^}]+)\}", path.read_text("utf8")
            ))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 26)
        self.assertEqual(set(refs) - all_labels, set())

    def test_recursion_and_atomic_clauses(self):
        self.assertIn(r"\label{def:forcing33-atomic}", TEXT)
        self.assertIn(r"p\Vdash\sigma\in\tau", TEXT)
        self.assertIn(r"p\Vdash\sigma=\tau", TEXT)
        self.assertIn(r"\mathbin{\#}", TEXT)
        self.assertIn("ściśle rosnąca", TEXT)
        self.assertIn(r"\label{lem:forcing33-atomic-monotone}", TEXT)
        self.assertIn(r"\label{lem:forcing33-atomic-dense}", TEXT)

    def test_schema_not_tarski_truth_predicate(self):
        self.assertIn(r"\label{thm:forcing33-definability}", TEXT)
        self.assertIn(r"\operatorname{Force}_\varphi", TEXT)
        self.assertIn("ustalonej", TEXT)
        self.assertIn("twierdzeniu Tarskiego", TEXT)
        self.assertNotIn("jednego predykatu prawdy dla wszystkich", TEXT)

    def test_truth_lemma_and_no_circular_zfc(self):
        self.assertIn(r"\label{thm:forcing33-atomic-truth}", TEXT)
        self.assertIn(r"\label{thm:forcing33-truth}", TEXT)
        self.assertIn(r"\label{thm:forcing33-main}", TEXT)
        self.assertIn(r"\label{lem:forcing33-decision}", TEXT)
        self.assertIn("nie korzystaliśmy", TEXT)
        self.assertIn(r"M[G]\models\mathrm{ZFC}", TEXT)

    def test_zfc_proof_works_in_correct_order(self):
        self.assertIn(r"\label{thm:forcing33-zfc}", TEXT)
        i0 = TEXT.index(r"\emph{Ekstensjonalność i ufundowanie.}")
        i1 = TEXT.index(r"\emph{Aksjomat sumy.}")
        i2 = TEXT.index(r"\emph{Schemat wyróżniania.}")
        i3 = TEXT.index(r"\emph{Aksjomat zbioru potęgowego.}")
        i4 = TEXT.index(r"\emph{Schemat zastępowania.}")
        i5 = TEXT.index(r"\emph{Aksjomat wyboru.}")
        self.assertLess(i0, i1)
        self.assertLess(i1, i2)
        self.assertLess(i2, i3)
        self.assertLess(i3, i4)
        self.assertLess(i4, i5)
        self.assertIn(r"\mathcal S_\tau", TEXT)
        self.assertIn(r"\theta_\rho", TEXT)
        self.assertIn(r"q_{\sigma,t}", TEXT)
        self.assertIn("najmniejszą rangę", TEXT)

    def test_minimality_and_limitations(self):
        self.assertIn(r"\label{thm:forcing33-minimal}", TEXT)
        self.assertIn(r"M[G]\subseteq N", TEXT)
        self.assertIn(r"\label{rem:forcing33-ch}", TEXT)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC})", TEXT)

    def test_finite_atomic_forcing_semantics(self):
        # All generics in a three-condition finite Cohen tree.
        top, left, right = (), (0,), (1,)
        P = (top, left, right)
        leq = lambda q, p: q[:len(p)] == p

        empty_name = frozenset()
        one_sided = frozenset({(empty_name, left)})

        def force_member(p, sigma, tau):
            return all(
                any(
                    leq(r, q) and leq(r, s) and force_equal(r, sigma, pi)
                    for r in P for (pi, s) in tau
                )
                for q in P if leq(q, p)
            )

        def force_equal(p, sigma, tau):
            return (
                all(
                    any(leq(r, q) and force_member(r, pi, tau) for r in P)
                    for (pi, s) in sigma for q in P
                    if leq(q, p) and leq(q, s)
                )
                and all(
                    any(leq(r, q) and force_member(r, pi, sigma) for r in P)
                    for (pi, s) in tau for q in P
                    if leq(q, p) and leq(q, s)
                )
            )

        def value(name, G):
            return frozenset(
                value(pi, G) for pi, p in name if p in G
            )

        self.assertTrue(force_equal(top, empty_name, empty_name))
        self.assertTrue(force_member(left, empty_name, one_sided))
        self.assertFalse(force_member(top, empty_name, one_sided))
        self.assertFalse(force_member(right, empty_name, one_sided))
        self.assertTrue(all(
            not force_member(q, empty_name, one_sided)
            for q in P if leq(q, right)
        ))
        for G in ({top, left}, {top, right}):
            truth = value(empty_name, G) in value(one_sided, G)
            witness = any(
                force_member(p, empty_name, one_sided)
                for p in G
            )
            neg_witness = any(
                all(
                    not force_member(q, empty_name, one_sided)
                    for q in P if leq(q, p)
                )
                for p in G
            )
            self.assertEqual(truth, witness)
            self.assertEqual(not truth, neg_witness)

    def test_local_dense_construction(self):
        top, l, r, ll, lr, rl, rr = (
            (), (0,), (1,), (0, 0), (0, 1), (1, 0), (1, 1),
        )
        P = {top, l, r, ll, lr, rl, rr}
        leq = lambda q, p: q[:len(p)] == p
        D = {ll, lr}
        self.assertTrue(all(
            any(leq(s, q) for s in D)
            for q in P if leq(q, l)
        ))
        self.assertFalse(all(
            any(leq(s, q) for s in D) for q in P
        ))
        I = {
            q for q in P
            if not any(leq(s, q) and leq(s, l) for s in P)
        }
        E = D | I
        self.assertTrue(all(
            any(leq(s, q) for s in E) for q in P
        ))

    def test_finite_names_singleton_pair_ordered_pair(self):
        top = "T"
        G = {top}

        def value(name):
            return frozenset(value(sigma) for sigma, p in name if p in G)

        def sing(x):
            return frozenset({(x, top)})

        def pair(x, y):
            return frozenset({(x, top), (y, top)})

        empty = frozenset()
        one = sing(empty)
        self.assertEqual(value(sing(empty)), frozenset({frozenset()}))
        self.assertEqual(value(pair(empty, one)),
                         frozenset({frozenset(), frozenset({frozenset()})}))
        op = pair(sing(empty), pair(empty, one))
        self.assertEqual(value(op),
                         frozenset({frozenset({frozenset()}),
                                    frozenset({frozenset(),
                                               frozenset({frozenset()})})}))


if __name__ == "__main__":
    unittest.main()
