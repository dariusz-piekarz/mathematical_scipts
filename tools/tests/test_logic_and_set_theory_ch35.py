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
        self.assertEqual(len(refs), 34)
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

    def test_canonical_names_preserve_atomic_truth_and_successor(self):
        # Independent finite Boolean semantics of ground-model check names.
        # Checks equality, membership, pairing, and ordinal successors.
        naturals = [frozenset()]
        for _ in range(1, 7):
            naturals.append(frozenset(naturals))
        ground = list(dict.fromkeys(naturals + [
            frozenset({naturals[2]}),
            frozenset({naturals[1], naturals[3]}),
        ]))

        @lru_cache(None)
        def check(a):
            return frozenset((check(y), 7) for y in a)

        @lru_cache(None)
        def membership(a, b):
            result = 0
            for child, coef in b:
                result |= coef & equality(a, child)
            return result

        @lru_cache(None)
        def equality(a, b):
            result = 7
            for child, coef in a:
                result &= (7 ^ coef) | membership(child, b)
            for child, coef in b:
                result &= (7 ^ coef) | membership(child, a)
            return result

        for a in ground:
            for b in ground:
                self.assertEqual(equality(check(a), check(b)), 7 if a == b else 0)
                self.assertEqual(
                    membership(check(a), check(b)), 7 if a in b else 0,
                )
                pair = frozenset({(check(a), 7), (check(b), 7)})
                for eta in ground:
                    self.assertEqual(
                        membership(check(eta), pair),
                        7 if eta == a or eta == b else 0,
                    )
        for n in range(6):
            self.assertEqual(
                naturals[n] | {naturals[n]}, naturals[n + 1],
            )
            self.assertEqual(
                membership(check(naturals[n + 1]), check(naturals[6])),
                7 if n + 1 < 6 else 0,
            )
        self.assertIn(r"\llbracket\check a\in\check b\rrbracket", TEXT)
        self.assertIn(r"\llbracket\check 0\in", TEXT)

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
        self.assertIn(r"T_\sigma", TEXT)
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

    def test_regular_open_algebra_excludes_empty_space(self):
        # RO(empty) is trivial, whereas the chapter assumes 0 != 1.
        self.assertIn(
            r"Dla każdej \emph{niepustej} przestrzeni",
            TEXT,
        )
        self.assertEqual(len({frozenset()}), 1)
        point = frozenset({0})
        self.assertEqual(len({frozenset(), point}), 2)

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

    def test_ro_completion_for_every_small_preorder(self):
        # Includes non-separative preorders, not only partial orders.
        # For n=1,2,3,4 there are respectively 1,4,29,355
        # preorders on labelled elements.
        from itertools import product

        count = {}
        for n in (1, 2, 3, 4):
            off = [
                (i, j) for i in range(n)
                for j in range(n) if i != j
            ]
            checked = 0
            for bits in product((0, 1), repeat=len(off)):
                rel = {(i, i) for i in range(n)}
                rel.update(
                    pair for pair, bit in zip(off, bits) if bit
                )
                if any(
                    (a, c) not in rel
                    for a, b in rel
                    for b2, c in rel if b == b2
                ):
                    continue
                checked += 1
                universe = set(range(n))
                below = {
                    p: {q for q in universe if (q, p) in rel}
                    for p in universe
                }

                def closure(s):
                    return {p for p in universe if below[p] & s}

                def interior(s):
                    return {p for p in universe if below[p] <= s}

                def regularize(s):
                    return frozenset(interior(closure(s)))

                subsets = [
                    frozenset(p for p in universe if mask & (1 << p))
                    for mask in range(1 << n)
                ]
                ro = {s for s in subsets if regularize(s) == s}
                top = frozenset(universe)
                self.assertIn(frozenset(), ro)
                self.assertIn(top, ro)

                for a in ro:
                    complement = frozenset(universe - closure(a))
                    self.assertIn(complement, ro)
                    self.assertFalse(a & complement)
                    self.assertEqual(regularize(a | complement), top)
                    for b in ro:
                        self.assertIn(frozenset(a & b), ro)
                        self.assertIn(regularize(a | b), ro)

                images = {p: regularize(below[p]) for p in universe}
                for val in images.values():
                    self.assertIn(val, ro)
                    self.assertTrue(val)
                for b in ro:
                    join = frozenset()
                    for image in images.values():
                        if image <= b:
                            join = regularize(join | image)
                    self.assertEqual(join, b)

                    for p in universe:
                        if images[p] & b:
                            self.assertTrue(any(
                                (q, p) in rel and images[q] <= b
                                for q in universe
                            ))

                for p in universe:
                    for q in universe:
                        compatible = any(
                            (r, p) in rel and (r, q) in rel
                            for r in universe
                        )
                        self.assertEqual(
                            bool(images[p] & images[q]), compatible
                        )
            count[n] = checked
        self.assertEqual(count, {1: 1, 2: 4, 3: 29, 4: 355})
        self.assertIn(r"\operatorname{RO}(\mathbb P)", TEXT)

    def test_atomic_forcing_truth_for_all_small_preorders(self):
        # Check the original order-theoretic clauses from chapter 33
        # against the Boolean recursion, without assuming separativity.
        from itertools import product

        count, identities = {}, 0
        for n in (2, 3):
            off = [(i, j) for i in range(n)
                   for j in range(n) if i != j]
            count[n] = 0
            for bits in product((0, 1), repeat=len(off)):
                order = {(i, i) for i in range(n)}
                order.update(pair for pair, bit in zip(off, bits) if bit)
                if any((a, c) not in order
                       for a, b in order
                       for b2, c in order if b == b2):
                    continue
                count[n] += 1
                P = range(n)
                down = {p: frozenset(q for q in P if (q, p) in order)
                        for p in P}

                def closure(s):
                    return frozenset(p for p in P if down[p] & s)

                def interior(s):
                    return frozenset(p for p in P if down[p] <= s)

                def ro(s):
                    return interior(closure(s))

                def join(*args):
                    return ro(frozenset().union(*args))

                def neg(s):
                    return interior(set(P) - closure(s))

                def implies(a, b):
                    return join(neg(a), b)

                embed = {p: ro(down[p]) for p in P}
                zero = frozenset()

                @lru_cache(None)
                def translated(name):
                    co = {}
                    for child, p in name:
                        key = translated(child)
                        co[key] = join(co.get(key, zero), embed[p])
                    return frozenset(co.items())

                @lru_cache(None)
                def boolean_member(a, b):
                    return join(*(coef & boolean_equal(a, child)
                                  for child, coef in b))

                @lru_cache(None)
                def boolean_equal(a, b):
                    value = frozenset(P)
                    for child, coef in a:
                        value &= implies(coef, boolean_member(child, b))
                    for child, coef in b:
                        value &= implies(coef, boolean_member(child, a))
                    return value

                @lru_cache(None)
                def order_member(p, a, b):
                    return all(
                        any((r, q) in order and (r, s) in order
                            and order_equal(r, a, child)
                            for r in P for child, s in b)
                        for q in P if (q, p) in order
                    )

                @lru_cache(None)
                def order_equal(p, a, b):
                    return (
                        all(
                            any((r, q) in order
                                and order_member(r, child, b)
                                for r in P)
                            for child, s in a
                            for q in P
                            if (q, p) in order and (q, s) in order
                        )
                        and all(
                            any((r, q) in order
                                and order_member(r, child, a)
                                for r in P)
                            for child, s in b
                            for q in P
                            if (q, p) in order and (q, s) in order
                        )
                    )

                empty = frozenset()
                first = [
                    frozenset((empty, p) for p in P if mask & (1 << p))
                    for mask in range(1 << n)
                ]
                second = [
                    frozenset({(first[j], p)})
                    for j in range(min(3, len(first))) for p in P
                ]
                second.append(frozenset({
                    (first[1], 0), (first[2], min(1, n - 1))
                }))
                names = list(dict.fromkeys(first + second))
                for a in names:
                    for b in names:
                        for p in P:
                            with self.subTest(n=n, p=p, a=a, b=b):
                                self.assertEqual(
                                    order_member(p, a, b),
                                    embed[p] <= boolean_member(
                                        translated(a), translated(b)
                                    )
                                )
                                self.assertEqual(
                                    order_equal(p, a, b),
                                    embed[p] <= boolean_equal(
                                        translated(a), translated(b)
                                    )
                                )
                            identities += 2
        self.assertEqual(count, {2: 4, 3: 29})
        self.assertEqual(identities, 40446)

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

    def test_power_set_all_restricted_names_in_four_element_algebra(self):
        # Every one of the 64 tested names, including names with values
        # outside sigma, must agree with the restricted-name power set.
        from itertools import product

        empty = frozenset()
        one = frozenset({(empty, 3)})
        two = frozenset({(one, 3)})
        sigma = frozenset({(empty, 3), (one, 2)})
        restricted = [
            frozenset({(empty, a), (one, b)})
            for a in range(4) for b in (0, 2)
        ]
        Pi = frozenset((f, 3) for f in restricted)

        @lru_cache(None)
        def member(sigma, tau):
            return self.join(
                b & equal(sigma, pi) for pi, b in tau
            )

        @lru_cache(None)
        def equal(sigma, tau):
            v = 3
            for pi, b in sigma:
                v &= (3 ^ b) | member(pi, tau)
            for pi, b in tau:
                v &= (3 ^ b) | member(pi, sigma)
            return v

        @lru_cache(None)
        def value(name, atom):
            return frozenset(
                value(pi, atom) for pi, b in name if b & atom
            )

        checked = 0
        for coefficients in product(range(4), repeat=3):
            tau = frozenset(zip((empty, one, two), coefficients))
            f_tau = frozenset(
                (rho, b & member(rho, tau)) for rho, b in sigma
            )
            self.assertIn(f_tau, restricted)
            for atom in (1, 2):
                subset = value(tau, atom) <= value(sigma, atom)
                self.assertEqual(
                    subset, bool(member(tau, Pi) & atom)
                )
                if subset:
                    self.assertTrue(equal(tau, f_tau) & atom)
                checked += 1
        self.assertEqual(checked, 128)
        self.assertIn(r"T_\sigma", TEXT)
        self.assertIn(r"\llbracket\tau=f_\tau\rrbracket", TEXT)

    def test_founding_element_uses_minimal_rank_among_all_names(self):
        # The least-rank representative of an element of sigma need
        # not occur literally in dom(sigma).
        from itertools import product

        empty = frozenset()
        one = frozenset({(empty, 3)})
        two = frozenset({(one, 3)})
        high_empty = frozenset({(two, 0)})

        @lru_cache(None)
        def rank(name):
            return 0 if not name else 1 + max(
                rank(pi) for pi, _ in name
            )

        @lru_cache(None)
        def value(name, atom):
            return frozenset(
                value(pi, atom) for pi, b in name if b & atom
            )

        example = frozenset({(high_empty, 3)})
        self.assertEqual(value(high_empty, 1), value(empty, 1))
        self.assertNotIn(empty, {name for name, _ in example})
        self.assertLess(rank(empty), rank(high_empty))

        candidates = (empty, one, two, high_empty)
        checked = 0
        for coefficients in product(range(4), repeat=len(candidates)):
            sigma = frozenset(zip(candidates, coefficients))
            for atom in (1, 2):
                interpreted = value(sigma, atom)
                if not interpreted:
                    continue
                eligible = [
                    name for name in candidates
                    if value(name, atom) in interpreted
                ]
                witness = min(eligible, key=rank)
                self.assertIn(value(witness, atom), interpreted)
                self.assertFalse(value(witness, atom) & interpreted)
                checked += 1
        self.assertGreater(checked, 300)
        self.assertIn("Rozpatrzmy \\emph{wszystkie nazwy}", TEXT)
        self.assertIn(r"\operatorname{rk}(\eta)", TEXT)

    def test_boolean_replacement_image_for_singleton_operation(self):
        # Finite instance of replacement phi(x,y): y={x}, with
        # names and Boolean truth evaluated at both ultrafilters.
        from itertools import product

        empty = frozenset()
        one = frozenset({(empty, 3)})
        two = frozenset({(one, 3)})

        @lru_cache(None)
        def value(name, atom):
            return frozenset(
                value(pi, atom) for pi, b in name if b & atom
            )

        count = 0
        for coefficients in product(range(4), repeat=3):
            sigma = frozenset(zip((empty, one, two), coefficients))
            R = frozenset(
                (frozenset({(pi, 3)}), b) for pi, b in sigma
            )
            for atom in (1, 2):
                expected = frozenset(
                    frozenset({x}) for x in value(sigma, atom)
                )
                self.assertEqual(value(R, atom), expected)
                count += 1
        self.assertEqual(count, 128)
        self.assertIn(r"R_\sigma(\rho)", TEXT)
        self.assertIn(r"\exists!y", TEXT)

    @staticmethod
    def join(items):
        value = 0
        for item in items:
            value |= item
        return value

    def test_every_fork_boolean_coefficient_has_poset_pullback(self):
        # RO of the three-node fork: the two leaves are atoms.
        # Every Boolean name coefficient must be a join of
        # images of conditions, or the existential translation fails.
        cone = {"top": 3, "left": 1, "right": 2}
        for b in range(4):
            images_below = [
                val for val in cone.values() if (val & b) == val
            ]
            self.assertEqual(self.join(images_below), b)

        checked = 0
        for a in range(4):
            for b in range(4):
                original = {"empty": a, "one": b}
                poset_name = {
                    (rho, p)
                    for rho, coeff in original.items()
                    for p, val in cone.items()
                    if (val & coeff) == val
                }
                reconstructed = {
                    rho: self.join(
                        cone[p] for name, p in poset_name
                        if name == rho
                    ) for rho in original
                }
                self.assertEqual(reconstructed, original)
                checked += 1
        self.assertEqual(checked, 16)
        self.assertIn(r"\tau^{\mathbb P}=", TEXT)
        self.assertIn(r"(\tau^{\mathbb P})^{\mathbb B}", TEXT)

    def test_choice_via_least_preimage_on_both_atoms(self):
        # A finite Boolean analogue of the ZF construction:
        # ordinal-indexed surjection -> least representatives -> well order.
        from itertools import product

        empty = frozenset()
        one = frozenset({(empty, 3)})
        two = frozenset({(one, 3)})
        domain = (empty, one, two)

        @lru_cache(None)
        def value(name, atom):
            return frozenset(
                value(pi, atom) for pi, coefficient in name
                if coefficient & atom
            )

        checks = 0
        for coefficients in product(range(4), repeat=len(domain)):
            sigma = frozenset(zip(domain, coefficients))
            for atom in (1, 2):
                interpreted = value(sigma, atom)
                K = [
                    i for i, coefficient in enumerate(coefficients)
                    if coefficient & atom
                ]
                F = {i: value(domain[i], atom) for i in K}
                self.assertEqual(set(F.values()), set(interpreted))
                K0 = [
                    i for i in K
                    if not any(j < i and F[j] == F[i] for j in K)
                ]
                self.assertEqual(len(K0), len(interpreted))
                self.assertEqual(
                    {F[i] for i in K0}, set(interpreted)
                )
                self.assertEqual(len(set(F[i] for i in K0)), len(K0))
                checks += 1
        self.assertEqual(checks, 128)
        self.assertIn(r"\check\kappa", TEXT)
        self.assertIn(r"F|_{K_0}", TEXT)
        self.assertIn(r"\sigma(e(\xi))", TEXT)
        self.assertIn(r"\dot a(\check\varnothing)=\{0\}", TEXT)

    def test_three_atom_name_semantics_power_set_and_foundation(self):
        # Independent eight-element Boolean algebra check (three atoms).
        # Fixed seed makes all 16,000 name pairs reproducible.
        from itertools import product
        from random import Random

        empty = frozenset()
        one = frozenset({(empty, 7)})
        two = frozenset({(one, 7)})
        three = frozenset({(two, 7)})
        bases = (empty, one, two)
        names = [
            frozenset(zip(bases, coefficients))
            for coefficients in product(range(8), repeat=3)
        ]

        @lru_cache(None)
        def member(a, b):
            return self.join(coefficient & equal(a, child)
                             for child, coefficient in b)

        @lru_cache(None)
        def equal(a, b):
            result = 7
            for child, coefficient in a:
                result &= (7 ^ coefficient) | member(child, b)
            for child, coefficient in b:
                result &= (7 ^ coefficient) | member(child, a)
            return result

        @lru_cache(None)
        def interpreted(name, atom):
            return frozenset(
                interpreted(child, atom)
                for child, coefficient in name
                if coefficient & atom
            )

        @lru_cache(None)
        def rank(name):
            return 0 if not name else 1 + max(
                rank(child) for child, _ in name
            )

        rng = Random(35)
        for _ in range(16000):
            a, b = rng.choice(names), rng.choice(names)
            for atom in (1, 2, 4):
                self.assertEqual(
                    bool(equal(a, b) & atom),
                    interpreted(a, atom) == interpreted(b, atom)
                )
                self.assertEqual(
                    bool(member(a, b) & atom),
                    interpreted(a, atom) in interpreted(b, atom)
                )

        foundation_checks = 0
        for name in names:
            for atom in (1, 2, 4):
                content = interpreted(name, atom)
                if content:
                    eligible = [
                        candidate for candidate in
                        (empty, one, two, three)
                        if interpreted(candidate, atom) in content
                    ]
                    self.assertTrue(eligible)
                    minimal = min(eligible, key=rank)
                    self.assertTrue(
                        interpreted(minimal, atom).isdisjoint(content)
                    )
                    foundation_checks += 1
        self.assertEqual(foundation_checks, 1344)

        sigma = frozenset(((empty, 3), (one, 5), (two, 6)))
        restricted = [
            frozenset(((empty, a), (one, b), (two, c)))
            for a in range(8) for b in range(8) for c in range(8)
            if (a & 3) == a and (b & 5) == b and (c & 6) == c
        ]
        self.assertEqual(len(restricted), 64)
        powerset = frozenset((name, 7) for name in restricted)

        power_checks = 0
        for tau in names:
            witness = frozenset(
                (rho, coefficient & member(rho, tau))
                for rho, coefficient in sigma
            )
            self.assertIn(witness, restricted)
            for atom in (1, 2, 4):
                subset = interpreted(tau, atom) <= interpreted(sigma, atom)
                self.assertEqual(
                    bool(member(tau, powerset) & atom), subset
                )
                if subset:
                    self.assertTrue(equal(tau, witness) & atom)
                power_checks += 1
        self.assertEqual(power_checks, 1536)

    def test_three_atom_decision_of_finite_named_real(self):
        # Finite Boolean analogue of the no-new-reals argument:
        # every named subset is decided by a ground subset on each atom.
        from itertools import product

        cases = 0
        for coefficients in product(range(8), repeat=4):
            equality_values = []
            for ground_subset in range(16):
                truth = 7
                for n, coefficient in enumerate(coefficients):
                    if ground_subset & (1 << n):
                        truth &= coefficient
                    else:
                        truth &= 7 ^ coefficient
                equality_values.append(truth)

            joint = 0
            for value in equality_values:
                joint |= value
            self.assertEqual(joint, 7)
            for atom in (1, 2, 4):
                possible = [
                    x for x, value in enumerate(equality_values)
                    if value & atom
                ]
                self.assertEqual(len(possible), 1)
                expected = sum(
                    (1 << n) for n, coefficient in enumerate(coefficients)
                    if coefficient & atom
                )
                self.assertEqual(possible[0], expected)
                cases += 1
        self.assertEqual(cases, 12288)

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


    def test_mixing_for_nonmaximal_antichains_and_zero_coefficients(self):
        # Independent 8-element Boolean-algebra regression of the mixing lemma.
        # Covers nonmaximal antichains, zero coefficients, and literal
        # name collisions without reducing to canonical ground names.
        from itertools import product

        empty = frozenset()
        one = frozenset({(empty, 7)})
        two = frozenset({(one, 7)})
        bases = (empty, one, two)
        names = [
            frozenset(zip(bases, coefficients))
            for coefficients in product(range(8), repeat=3)
        ]

        @lru_cache(None)
        def membership(sigma, tau):
            return self.join(
                coefficient & equality(sigma, child)
                for child, coefficient in tau
            )

        @lru_cache(None)
        def equality(sigma, tau):
            result = 7
            for child, coefficient in sigma:
                result &= (7 ^ coefficient) | membership(child, tau)
            for child, coefficient in tau:
                result &= (7 ^ coefficient) | membership(child, sigma)
            return result

        checks = 0
        for antichain in ((1, 2, 4), (3, 4), (1, 6), (7,)):
            for k in range(120):
                chosen = {
                    a: names[(41 * k + 9 * a) % len(names)]
                    for a in antichain
                }
                support = set().union(*(
                    {name for name, _ in chosen[a]} for a in antichain
                ))
                mixed = frozenset((
                    name,
                    self.join(
                        a & dict(chosen[a]).get(name, 0)
                        for a in antichain
                    )
                ) for name in support)
                for a, target in chosen.items():
                    self.assertEqual(
                        a & equality(mixed, target), a,
                        (antichain, k, a),
                    )
                    checks += 1

        self.assertEqual(checks, 960)
        self.assertIn(r"\label{lem:boolean35-mixing}", TEXT)


if __name__ == "__main__":
    unittest.main()
