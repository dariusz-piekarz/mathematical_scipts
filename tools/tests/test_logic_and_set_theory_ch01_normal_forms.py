"""Exhaustive truth-table checks for normal forms and elementary connectives."""
import itertools
import unittest


class TestPropositionalNormalForms(unittest.TestCase):
    def test_all_truth_tables_up_to_three_variables(self):
        for n in range(1, 4):
            rows = tuple(itertools.product((False, True), repeat=n))
            for table in itertools.product((False, True), repeat=len(rows)):
                positive = [a for a, truth in zip(rows, table) if truth]
                negative = [a for a, truth in zip(rows, table) if not truth]
                for b, expected in zip(rows, table):
                    dnf = any(all(x == y for x, y in zip(a, b)) for a in positive)
                    cnf = all(any(x != y for x, y in zip(a, b)) for a in negative)
                    self.assertEqual(dnf, expected)
                    self.assertEqual(cnf, expected)

    def test_nand_nor_and_implication_bases(self):
        nand = lambda a, b: not (a and b)
        nor = lambda a, b: not (a or b)
        imp = lambda a, b: not a or b
        for a, b in itertools.product((False, True), repeat=2):
            self.assertEqual(nand(a, a), not a)
            self.assertEqual(nand(nand(a, b), nand(a, b)), a and b)
            self.assertEqual(nor(a, a), not a)
            self.assertEqual(nor(nor(a, b), nor(a, b)), a or b)
            self.assertEqual(imp(not a, b), a or b)
            self.assertEqual((not a and b) or (a and not b),
                             (a or b) and (not a or not b))

    def test_semantic_deduction_and_refutation(self):
        universe = frozenset(range(4))
        subsets = [frozenset(i for i in universe if mask & (1 << i))
                   for mask in range(16)]
        for g, a, b in itertools.product(subsets, repeat=3):
            self.assertEqual(g <= a, not (g & (universe - a)))
            self.assertEqual((g & a) <= b, g <= ((universe - a) | b))
            if g <= a and a <= b:
                self.assertTrue(g <= b)

    def test_chain_finite_support(self):
        for n in range(1, 9):
            def satisfies(row):
                return row[0] and all(not row[i] or row[i+1]
                                      for i in range(n-1))
            rows = tuple(itertools.product((False, True), repeat=n+1))
            models = [row for row in rows if satisfies(row)]
            self.assertTrue(models)
            self.assertTrue(all(row[n-1] for row in models))
            self.assertTrue(any(not row[n] for row in models))

    def test_monotonicity_obstruction(self):
        rows = tuple(itertools.product((False, True), repeat=2))
        functions = [lambda a,b:a, lambda a,b:b, lambda a,b:False,
                     lambda a,b:True, lambda a,b:a and b, lambda a,b:a or b]
        for x,y in itertools.product(rows, repeat=2):
            if all(a <= b for a,b in zip(x,y)):
                for f in functions:
                    self.assertLessEqual(f(*x), f(*y))
        self.assertGreater(not False, not True)


if __name__ == "__main__":
    unittest.main()
