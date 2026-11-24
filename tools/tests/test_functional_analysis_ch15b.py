import unittest
from pathlib import Path
from fractions import Fraction

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex"

class TestChapter15B(unittest.TestCase):
    def test_latex_relations(self):
        source = SOURCE.read_text(encoding="utf-8")
        for relation in (r"u_n\to f", r"s_n\to f", r"f(s)\ne0"):
            self.assertIn(relation, source)
        self.assertNotIn("u_n\t" + "o f", source)
        self.assertNotIn("s_n\t" + "o f", source)
        self.assertNotIn("f(s)\n" + "e0", source)

    def test_diagonal_error_budget(self):
        for n in range(1, 20):
            tail = sum((Fraction(1, 2**k) for k in range(n, 40)), Fraction(0))
            self.assertLess(tail, Fraction(1, 2**(n-1)))
        self.assertIn("Borela--Cantellego daje", SOURCE.read_text(encoding="utf-8"))


    def test_fubini_rectangular_vector_integral(self):
        # Exact finite-atomic Bochner integral on a product space.
        mu = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        nu = [Fraction(2, 5), Fraction(3, 5)]
        f = [
            [(Fraction(1, 3), Fraction(-2, 5)), (Fraction(-1), Fraction(3))],
            [(Fraction(2), Fraction(1, 4)), (Fraction(-3, 2), Fraction(2))],
            [(Fraction(-2, 7), Fraction(1)), (Fraction(1, 3), Fraction(-1))],
        ]

        def vecsum(weighted):
            weighted = tuple(weighted)
            return tuple(sum((w * v[k] for w, v in weighted), Fraction(0))
                         for k in range(2))

        by_s = vecsum(
            (mu[i], vecsum((nu[j], f[i][j]) for j in range(len(nu))))
            for i in range(len(mu))
        )
        by_t = vecsum(
            (nu[j], vecsum((mu[i], f[i][j]) for i in range(len(mu))))
            for j in range(len(nu))
        )
        product = vecsum(
            (mu[i] * nu[j], f[i][j])
            for i in range(len(mu)) for j in range(len(nu))
        )
        self.assertEqual(product, (Fraction(-53, 210), Fraction(61, 50)))
        self.assertEqual(by_s, product)
        self.assertEqual(by_t, product)

    def test_vector_measure_variation_on_finite_atoms(self):
        # X=R^2 with l1 norm; variation of a Bochner density.
        mu = [Fraction(1, 2), Fraction(1, 4),
              Fraction(1, 8), Fraction(1, 8)]
        f = [(Fraction(3), Fraction(-4)),
             (Fraction(-1), Fraction(1, 2)),
             (Fraction(2), Fraction(0)),
             (Fraction(0), Fraction(-6))]

        def norm(v):
            return abs(v[0]) + abs(v[1])

        def m(indices):
            return tuple(sum((mu[i] * f[i][k] for i in indices), Fraction(0))
                         for k in range(2))

        def partitions(items):
            if not items:
                yield []
                return
            x, *rest = items
            for partition in partitions(rest):
                yield [[x]] + partition
                for j in range(len(partition)):
                    new = [block[:] for block in partition]
                    new[j].append(x)
                    yield new

        for mask in range(1 << len(mu)):
            atoms = [i for i in range(len(mu)) if mask & (1 << i)]
            value = max(
                (sum((norm(m(block)) for block in partition), Fraction(0))
                 for partition in partitions(atoms)),
                default=Fraction(0),
            )
            integral_norm = sum((mu[i] * norm(f[i]) for i in atoms), Fraction(0))
            self.assertEqual(value, integral_norm)

    def test_variation_lemma_and_fubini_cross_sections_present(self):
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\label{prop:variation-measure15b}", source)
        self.assertIn("przekroje usuniętego", source)
        self.assertIn(r"\int_S\sum_{n=1}^\infty", source)

if __name__ == "__main__":
    unittest.main()
