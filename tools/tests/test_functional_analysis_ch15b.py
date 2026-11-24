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

if __name__ == "__main__":
    unittest.main()
