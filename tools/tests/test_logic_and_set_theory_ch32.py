"""Chapter 32: basic forcing, generic filters, Cohen reals and valuations."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/logic_and_set_theory"
SOURCE = CHAPTERS / "32-podstawy-wymuszania-i-modele-generyczne.tex"
TEXT = SOURCE.read_text(encoding="utf8")


class TestChapter32(unittest.TestCase):
    def test_registered_in_book_and_catalog(self):
        entry = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf8")
        catalog = (ROOT / "catalog/books.json").read_text("utf8")
        self.assertIn(SOURCE.name, entry)
        self.assertIn(SOURCE.name, catalog)
        self.assertIn(r"\label{ch:forcing-foundations}", TEXT)

    def test_environments_and_labels(self):
        counts = {
            "definicja": 11, "lemat": 7, "twierdzenie": 4,
            "wniosek": 1, "przyklad": 4, "uwaga": 4,
            "proof": 12, "figure": 1, "tikzpicture": 1,
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
        self.assertEqual(len(labels), 33)
        self.assertEqual(len(set(labels)), len(labels))

    def test_references_have_targets(self):
        all_labels = {
            label
            for path in CHAPTERS.glob("*.tex")
            for label in re.findall(r"\\label\{([^}]+)\}", path.read_text("utf8"))
        }
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", TEXT)
        self.assertEqual(len(refs), 11)
        self.assertEqual(set(refs) - all_labels, set())

    def test_rasiowa_sikorski_general_poset_and_countable_family(self):
        self.assertIn(r"\label{thm:rasiowa-sikorski}", TEXT)
        self.assertIn(r"\label{cor:countable-generic}", TEXT)
        self.assertIn("niekoniecznie", TEXT)
        self.assertIn("przeliczalnym", TEXT)
        self.assertIn(r"\emph{dobre uporządkowanie}", TEXT)
        self.assertIn(r"p_{\max(m,n)}", TEXT)
        self.assertIn(r"G\cap D_n", TEXT)
        self.assertNotIn(r"Ustalmy enumerację \mathbb P", TEXT)

        # A finite model of the lemma: extension order on binary sequences.
        poset = [(), (0,), (1,), (0, 0), (0, 1), (1, 0), (1, 1)]
        stronger = lambda q, p: q[:len(p)] == p
        dense = [
            {p for p in poset if len(p) >= 1},
            {p for p in poset if len(p) == 2},
        ]
        self.assertTrue(all(
            any(stronger(q, p) for q in D)
            for D in dense for p in poset
        ))
        chain = [()]
        for D in dense:
            chain.append(next(q for q in poset if q in D and stronger(q, chain[-1])))
        G = {q for q in poset if any(stronger(p, q) for p in chain)}
        self.assertIn((), G)
        self.assertTrue(all(G & D for D in dense))
        self.assertTrue(all(
            any(stronger(r, p) and stronger(r, q) for r in G)
            for p in G for q in G
        ))

    def test_compatibility_of_finite_binary_conditions(self):
        def compatible(p, q):
            return all(p[i] == q[i] for i in p.keys() & q.keys())
        p = {0: 0, 3: 1}
        q = {1: 1, 3: 1}
        r = {3: 0}
        self.assertTrue(compatible(p, q))
        self.assertFalse(compatible(p, r))
        self.assertEqual(p | q, {0: 0, 1: 1, 3: 1})
        self.assertIn(r"q\supseteq p", TEXT)

    def test_cohen_real_is_new_and_total(self):
        self.assertIn(r"\label{thm:cohen-new-real}", TEXT)
        self.assertIn(r"n\in\operatorname{dom}c_G", TEXT)
        self.assertIn(r"c_G\notin M", TEXT)
        self.assertIn(r"p\cup\{(n,1-x(n))\}", TEXT)
        self.assertIn(r"\label{ex:cohen-filter-recovery}", TEXT)

    def test_dense_suborder_transfer(self):
        self.assertIn(r"\label{thm:forcing-dense-suborder}", TEXT)
        self.assertIn(r"D_{\mathbb Q}", TEXT)
        self.assertIn(r"2^{<\omega}", TEXT)

    def test_name_hierarchy_and_extension_discipline(self):
        self.assertIn(r"N_{\alpha+1}=\mathcal P(N_\alpha\times\mathbb P)", TEXT)
        self.assertIn(r"\label{lem:forcing-valuation-exists}", TEXT)
        self.assertIn(r"\check x", TEXT)
        self.assertIn(r"\dot G", TEXT)
        self.assertIn(r"\label{thm:forcing-extension-first}", TEXT)
        self.assertIn(r"M\subseteq M[G]", TEXT)
        self.assertIn(r"G\in M[G]", TEXT)
        self.assertIn("nie udowodniliśmy", TEXT)
        self.assertIn(r"M[G]\models\mathrm{ZFC}", TEXT)

    def test_small_forcing_names_and_valuations(self):
        # Toy model of names and valuations for two conditions.
        empty = frozenset()
        one = frozenset({empty})  # 1={0} as a von Neumann ordinal
        conditions = {empty, one}
        top = empty
        G = conditions

        def check(x):
            return frozenset((check(y), top) for y in x)

        def value(name):
            return frozenset(value(sigma) for sigma, p in name if p in G)

        dot_G = frozenset((check(p), p) for p in conditions)
        self.assertEqual(value(check(empty)), empty)
        self.assertEqual(value(check(one)), one)
        self.assertEqual(value(dot_G), frozenset(G))
        self.assertIn("Schemat zastępowania", TEXT)
        self.assertIn("rangi są wspólnie ograniczone", TEXT)
        self.assertIn(r"X\in N_{\alpha+1}", TEXT)

    def test_poset_without_greatest_element(self):
        # A valid forcing preorder may have incompatible minimal elements
        # and no largest element; the Rasiowa-Sikorski lemma still applies.
        P = {"a", "b"}
        leq = lambda p, q: p == q
        self.assertTrue(all(leq(p, p) for p in P))
        self.assertFalse(any(all(leq(p, top) for p in P) for top in P))
        dense = [set(P), set(P)]
        G = {"a"}
        self.assertTrue(all(
            any(leq(q, p) for q in D) for D in dense for p in P
        ))
        self.assertTrue(all(G & D for D in dense))
        self.assertTrue(all(
            any(leq(r, p) and leq(r, q) for r in G)
            for p in G for q in G
        ))
        self.assertIn("ani istnienia", TEXT)
        self.assertIn(r"1_{\mathbb P}", TEXT)
        self.assertIn(r"\label{thm:rasiowa-sikorski}", TEXT)

    def test_name_recognition_absoluteness_is_explicit(self):
        # Syntactic regression, not a formal proof of set-theoretic absoluteness.
        self.assertIn(r"\emph{absolutność bycia nazwą}", TEXT)
        self.assertIn(r"N_{\alpha+1}^M", TEXT)
        self.assertIn("wewnętrznym i zewnętrznym", TEXT)
        self.assertIn("po zwykłej randze", TEXT)

    def test_no_unproved_forcing_theorem(self):
        self.assertNotIn(r"\begin{twierdzenie}[M[G] spełnia ZFC]", TEXT)
        self.assertIn(r"p\Vdash\varphi", TEXT)


if __name__ == "__main__":
    unittest.main()
