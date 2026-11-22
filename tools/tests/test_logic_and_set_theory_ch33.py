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
        self.assertIn(r"\operatorname{rk}(\tau)", TEXT)
        self.assertNotIn(r"\rho(\tau)", TEXT)
        self.assertIn("ściśle rosnąca", TEXT)
        self.assertIn(r"\label{lem:forcing33-atomic-monotone}", TEXT)
        self.assertIn(r"\label{lem:forcing33-atomic-dense}", TEXT)

    def test_schema_not_tarski_truth_predicate(self):
        self.assertIn(r"\label{thm:forcing33-definability}", TEXT)
        self.assertIn(r"\operatorname{Force}_\varphi", TEXT)
        self.assertIn("ustalonej", TEXT)
        self.assertIn("twierdzeniu Tarskiego", TEXT)
        self.assertIn("jednego predykatu prawdy", TEXT)

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
        self.assertIn(r"\emph{najmniejsza ranga}", TEXT)

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

    def test_union_name_on_branching_finite_forcing(self):
        P = ((), (0,), (1,))
        top, left, right = P
        leq = lambda q, p: q[:len(p)] == p

        def val(name, G):
            return frozenset(val(sigma, G) for sigma, p in name if p in G)

        empty = frozenset()
        singleton_empty = frozenset({(empty, top)})
        outer = frozenset({(singleton_empty, left)})
        u = frozenset(
            (sigma, p)
            for pi, q in outer
            for sigma, r in pi
            for p in P if leq(p, q) and leq(p, r)
        )
        for G in ({top, left}, {top, right}):
            interpreted_union = frozenset(
                element for part in val(outer, G) for element in part
            )
            self.assertEqual(val(u, G), interpreted_union)
        self.assertIn(r"B_\tau", TEXT)
        self.assertIn(r"B_\tau\times\mathbb P", TEXT)

    def test_power_set_name_bounded_search_on_small_forcing(self):
        # Check the canonical restricted-name construction for each
        # possible 1-step name rho in a finite forcing notion.
        from itertools import combinations
        P = ((), (0,), (1,))
        top, left, right = P
        leq = lambda q, p: q[:len(p)] == p
        empty = frozenset()
        tau = frozenset({(empty, top)})
        A = {sigma for sigma, p in tau}

        def value(name, G):
            return frozenset(value(sigma, G) for sigma, p in name if p in G)

        def force_mem(p, sigma, target):
            return all(
                any(
                    leq(r, q) and leq(r, s) and force_eq(r, sigma, pi)
                    for r in P for pi, s in target
                )
                for q in P if leq(q, p)
            )

        def force_eq(p, sigma, target):
            return (
                all(
                    any(leq(r, q) and force_mem(r, pi, target) for r in P)
                    for pi, s in sigma for q in P
                    if leq(q, p) and leq(q, s)
                )
                and all(
                    any(leq(r, q) and force_mem(r, pi, sigma) for r in P)
                    for pi, s in target for q in P
                    if leq(q, p) and leq(q, s)
                )
            )

        options = [(empty, p) for p in P]
        checked = 0
        for k in range(len(options) + 1):
            for pairs in combinations(options, k):
                rho = frozenset(pairs)
                theta_rho = frozenset(
                    (sigma, p) for sigma in A for p in P
                    if force_mem(p, sigma, tau)
                    and force_mem(p, sigma, rho)
                )
                self.assertTrue(all(
                    force_mem(p, sigma, tau) for sigma, p in theta_rho
                ))
                for G in ({top, left}, {top, right}):
                    a, b = value(tau, G), value(rho, G)
                    self.assertTrue(b <= a)
                    self.assertEqual(value(theta_rho, G), b)
                    checked += 1
        self.assertEqual(checked, 16)
        self.assertIn(r"\mathcal S_\tau", TEXT)
        self.assertIn(r"\theta_\rho", TEXT)

    def test_minimum_rank_class_choice_has_set_bound(self):
        self.assertIn(r"\alpha_{\sigma,t}", TEXT)
        self.assertIn(r"\mathbb P\times N_{\gamma+1}^M", TEXT)
        self.assertIn("zastępowania", TEXT)
        self.assertIn("aksjomatu wyboru w $M$", TEXT)
        self.assertIn(r"\emph{zbioru} $J$", TEXT)

    def test_forcing_depends_on_order_not_just_underlying_set(self):
        # Same P and same top, two different orders. The membership
        # relation changes: this guards against omitting <= from Force_phi.
        P = ("top", "left", "right")
        fork = {("top", "top"), ("left", "left"), ("right", "right"),
                ("left", "top"), ("right", "top")}
        chain = fork | {("left", "right")}
        empty = frozenset()
        target = frozenset({(empty, "left")})

        def forces_member_below_right(relation):
            def leq(q, p):
                return (q, p) in relation

            return all(
                any(leq(r, q) and leq(r, s) for _, s in target for r in P)
                for q in P if leq(q, "right")
            )

        self.assertFalse(forces_member_below_right(fork))
        self.assertTrue(forces_member_below_right(chain))
        self.assertIn(r"\operatorname{Force}_\varphi", TEXT)
        self.assertIn(r"(p,\tau_1,\ldots,\tau_n,\mathbb P,\leq)", TEXT)

    def test_exhaustive_rank_one_atomic_truth_lemma(self):
        # Exhaustively test 8 rank-one names and all their ordered pairs
        # against the atomic forcing relation for both generic branches.
        from functools import lru_cache
        from itertools import combinations

        P = ((), (0,), (1,))
        top, left, right = P
        leq = lambda q, p: q[:len(p)] == p
        empty = frozenset()
        names = tuple(
            frozenset((empty, p) for p in support)
            for k in range(len(P) + 1)
            for support in combinations(P, k)
        )
        self.assertEqual(len(names), 8)

        @lru_cache(None)
        def force_mem(p, sigma, tau):
            return all(
                any(
                    leq(r, q) and leq(r, s)
                    and force_eq(r, sigma, pi)
                    for r in P for pi, s in tau
                )
                for q in P if leq(q, p)
            )

        @lru_cache(None)
        def force_eq(p, sigma, tau):
            return (
                all(
                    any(leq(r, q) and force_mem(r, pi, tau) for r in P)
                    for pi, s in sigma for q in P
                    if leq(q, p) and leq(q, s)
                )
                and all(
                    any(leq(r, q) and force_mem(r, pi, sigma) for r in P)
                    for pi, s in tau for q in P
                    if leq(q, p) and leq(q, s)
                )
            )

        def value(name, G):
            return frozenset(value(pi, G) for pi, p in name if p in G)

        checked = 0
        for sigma in names:
            for tau in names:
                for G in ({top, left}, {top, right}):
                    x, y = value(sigma, G), value(tau, G)
                    self.assertEqual(
                        x in y, any(force_mem(p, sigma, tau) for p in G)
                    )
                    self.assertEqual(
                        x == y, any(force_eq(p, sigma, tau) for p in G)
                    )
                    checked += 2
        self.assertEqual(checked, 256)

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
