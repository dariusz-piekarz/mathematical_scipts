"""Rozdzial 22: kontrole referencji, struktury i elementarnych etapow dowodow.

Testy skryptowe NIE zastepuja dowodow metamatematycznych w PA.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER_DIR = ROOT / "chapters/pl/logic_and_set_theory"
SOURCE_FILE = CHAPTER_DIR / "22-drugie-twierdzenie-godla-i-twierdzenie-loba.tex"
SOURCE = SOURCE_FILE.read_text(encoding="utf-8")


class TestLogicChapter22(unittest.TestCase):
    def test_chapter_is_imported(self):
        self.assertTrue(SOURCE_FILE.is_file())
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text(encoding="utf-8")
        self.assertIn(r"\input{../../chapters/pl/logic_and_set_theory/" + SOURCE_FILE.name + "}", book)
        self.assertIn(r"\label{ch:second-incompleteness}", SOURCE)

    def test_environment_balance(self):
        stack = []
        for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", SOURCE):
            if kind == "begin":
                stack.append(name)
            else:
                self.assertTrue(stack, name)
                self.assertEqual(stack.pop(), name)
        self.assertEqual(stack, [])

    def test_inventory_preserved_from_existing_chapter(self):
        expected = {
            "definicja": 1, "przyklad": 2, "lemat": 2, "proof": 6,
            "uwaga": 5, "twierdzenie": 3, "wniosek": 1
        }
        for env, count in expected.items():
            with self.subTest(env=env):
                self.assertEqual(SOURCE.count(r"\begin{" + env + "}"), count)
                self.assertEqual(SOURCE.count(r"\end{" + env + "}"), count)

    def test_references_exist_and_labels_unique(self):
        files = sorted(CHAPTER_DIR.glob("*.tex"))
        labels = []
        for path in files:
            labels.extend(re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")))
        refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", SOURCE)
        own = re.findall(r"\\label\{([^}]+)\}", SOURCE)
        self.assertEqual(len(own), 13)
        self.assertEqual(len(refs), 24)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertFalse(set(refs) - set(labels))

    def test_con_is_closed_sentence_and_pi1(self):
        text = SOURCE.split(r"\begin{definicja}[Formalna niesprzeczność]", 1)[1].split(r"\end{definicja}", 1)[0]
        self.assertIn(r"\operatorname{Bew}_T(\overline b)", text)
        self.assertIn(r"\operatorname{Con}_T", text)
        self.assertIn(r"\Pi_1", text)
        self.assertNotIn(r"\operatorname{Bew}_T(b)", text)

    def test_meta_consistency_uses_explosion_and_q(self):
        text = SOURCE.split(r"\begin{lemat}[Znaczenie niesprzeczności", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertIn("zasada eksplozji", text)
        self.assertIn(r"\mathfrak N\models", text)
        self.assertIn(r"\mathrm{PA}", text)

    def test_d1_d2_d3_appear_in_internal_proof(self):
        proof = SOURCE.split(r"\begin{lemat}[Wewnętrzne rozumowanie", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertIn(r"G\to\neg\Box G", proof)
        self.assertIn(r"\Box\neg\Box G", proof)
        self.assertIn(r"\Box\Box G", proof)
        self.assertIn(r"\Box\bot", proof)
        for condition in ("(D1)", "(D2)", "(D3)"):
            self.assertIn(condition, proof)

    def test_second_incompleteness_is_conditional(self):
        text = SOURCE.split(r"\begin{twierdzenie}[Drugie twierdzenie Gödla", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertIn("niesprzeczną", text)
        self.assertIn("efektywnie", text)
        self.assertIn(r"\mathrm{PA}", text)
        self.assertIn(r"T\nvdash\operatorname{Con}_T", text)
        self.assertIn(r"\ref{lem:second-box-g}", text)
        self.assertIn(r"\ref{res:8:1}", text)
        self.assertIn("wbrew", text)

    def test_loeb_uses_fixed_point_and_three_stages(self):
        text = SOURCE.split(r"\begin{twierdzenie}[Twierdzenie Löba]", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertIn(r"\operatorname{Bew}_T(x)", text)
        self.assertIn(r"L\leftrightarrow(\Box L\to\varphi)", text)
        self.assertIn(r"\Box L\to\Box\varphi", text)
        for step in ("Krok 1", "Krok 2", "Krok 3"):
            self.assertIn(step, text)
        self.assertIn("Nie zakładamy niesprzeczności", text)

    def test_loeb_propositional_consequences(self):
        # The key fixed-point implications are checked propositionally,
        # conditional on the previously established provability steps.
        for box_L in (False, True):
            for box_phi in (False, True):
                for phi in (False, True):
                    for L in (False, True):
                        fixed = L == ((not box_L) or phi)
                        lemma = (not box_L) or box_phi
                        assumption = (not box_phi) or phi
                        if fixed and lemma and assumption:
                            self.assertTrue((not box_L) or L)

    def test_model_argument_is_finite_to_universal_gap(self):
        proof = SOURCE.split(r"\begin{twierdzenie}[Niestandardowe modele", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertIn(r"\ref{thm:godel-second}", proof)
        self.assertIn(r"\ref{thm:godel-completeness}", proof)
        self.assertIn(r"\mathfrak N\models", proof)
        witness = SOURCE.split(r"\begin{uwaga}[Skąd bierze się niestandardowy świadek?]", 1)[1].split(r"\end{uwaga}", 1)[0]
        self.assertIn(r"\overline n", witness)
        self.assertIn(r"\ref{lem:incomp-proof-check}", witness)

    def test_not_any_provability_predicate(self):
        self.assertIn(r"\ref{def:rosser-predicate}", SOURCE)
        self.assertIn("Formuły zgodne w standardowym modelu", SOURCE)
        self.assertIn("nie zakładamy poprawności", SOURCE)


if __name__ == "__main__":
    unittest.main()
