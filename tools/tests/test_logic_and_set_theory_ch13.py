"""Regression checks for chapter 13 (Henkin). Finite cases are NOT a proof."""
from itertools import product
from pathlib import Path
import unittest

class TestHenkinChapter13(unittest.TestCase):
    def test_quantifier_duality_nonempty_finite_domains(self):
        count = 0
        for n in range(1, 5):
            A = tuple(range(n))
            for pmask, qmask in product(range(1 << n), repeat=2):
                P = {a for a in A if pmask & (1 << a)}
                Q = {a for a in A if qmask & (1 << a)}
                for relmask in range(1 << (n * n)) if n < 4 else (0, (1 << (n*n))-1):
                    R = {(a,b) for a,b in product(A, repeat=2) if relmask & (1 << (a*n+b))}
                    # phi(x) = P(x) and forall z (R(x,z) -> Q(z))
                    truth = {x: (x in P and all((x,z) not in R or z in Q for z in A)) for x in A}
                    self.assertEqual(not all(truth.values()), any(not v for v in truth.values()))
                    count += 1
        self.assertGreater(count, 4000)

    def test_finite_model_expands_to_satisfy_one_witness_axiom(self):
        count = 0
        for n in range(1, 5):
            A = tuple(range(n))
            for mask in range(1 << n):
                P = {a for a in A if mask & (1 << a)}
                # phi(x) = P(x); choose c as actual witness when present
                witness = min(P) if P else A[0]
                self.assertTrue(not bool(P) or witness in P)
                count += 1
        self.assertGreater(count, 20)

    def test_equality_congruence_of_finite_quotient(self):
        # Equivalence mod 3; function and predicate are well-defined.
        for a,b in product(range(9), repeat=2):
            if a % 3 == b % 3:
                self.assertEqual((a + 3) % 3, (b + 3) % 3)
                self.assertEqual(a % 3 == 0, b % 3 == 0)

    def test_source_side_conditions_and_inventory(self):
        src = (Path(__file__).resolve().parents[2] / "chapters/pl/logic_and_set_theory/13-twierdzenie-godla-o-pelnosci-i-konstrukcja-henkina.tex").read_text(encoding="utf-8")
        assert src.count(r"\begin{twierdzenie}") == 5
        assert src.count(r"\begin{lemat}") == 11
        assert src.count(r"\begin{definicja}") == 6
        assert src.count(r"\begin{przyklad}") == 6
        assert src.count(r"\begin{figure}") == 1
        for label in ("lem:henkin-constant-to-variable", "lem:henkin-parameters", "lem:henkin-quant-duality", "thm:henkin-truth", "thm:godel-completeness", "fig:henkin-chain"):
            self.assertIn(r"\label{" + label + "}", src)
        for phrase in ("warunek uboczny", "otwartych założeniach", "nie zostaje przechwycona", "Dwa etapy nadawania nazw świadkom", "Dlaczego trzeba ilorazować termy"):
            self.assertIn(phrase, src)

if __name__ == "__main__":
    unittest.main()