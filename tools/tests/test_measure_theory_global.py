"""MTG-001–003: global terminology and notation source regressions."""
import re
import unittest
from test_measure_theory_book_integrity import corpus, without_comments

# Strip only machine identifiers, not visible titles of hyperlinks.
IDENTIFIER = re.compile(r"\\(?:label|ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\{[^{}]+\}|\\hyperref\[[^\]]+\]")
FORBIDDEN = re.compile(
    r"\\(?:mathbf|mathbb|mathds|mathbbm)\s*\{\s*1\s*\}"
    r"|\\(?:mathds|mathbbm)\s+1\b"
    r"|\bindykator\w*|\bsekwenc\w*|\bzwartościowan\w*"
    r"|\b(?:pierwszo|drugo)[ -]?przeliczaln\w*|\bdual\b"
    r"|\btensorowan\w*|\bzbieżnoś[ćc]\w*\s+zwart\w*|\bseskwilini\w*",
    re.IGNORECASE,
)

class MeasureTheoryGlobal(unittest.TestCase):
    def test_mtg_001_terminology_and_characteristic_functions(self):
        sources = corpus()
        self.assertEqual(len(sources), 33)
        for path, body in sources.items():
            visible = IDENTIFIER.sub("", body)
            with self.subTest(file=path.name):
                self.assertIsNone(FORBIDDEN.search(visible))

    def test_mtg_002_machine_ids_are_not_prose(self):
        body = r"\label{def:dual-lp-15} \ref{def:dual-lp-15} \hyperref[def:dual-lp-15]{Dualność}"
        self.assertIsNone(FORBIDDEN.search(IDENTIFIER.sub("", body)))
        for body in (r"\mathbf{1}_A",r"\mathbb { 1 }", "dual ilorazu",
                     "sekwencja", "drugoprzeliczalna", "tensorowanie",
                     "zbieżność zwarta", "seskwiliniowa", "zwartościowanie",
                     "indykator"):
            self.assertIsNotNone(FORBIDDEN.search(body), body)
        self.assertIsNone(FORBIDDEN.search(r"\chi_A, przestrzeń dualna, ciąg, uzwarcenie"))

    def test_mtg_003_glossary_measure_types(self):
        sources = corpus()
        body = next(s for p,s in sources.items() if p.name == "spis_oznaczen.tex")
        for phrase in (r"Miara zewnętrzna na $\mathcal P(X)$",
                       "mierzalnych w sensie Carathéodory'ego jest miarą",
                       "Miara zewnętrzna Hausdorffa przy ograniczeniu średnic",
                       "ta ostatnia jest miarą na zbiorach borelowskich",
                       r"$\|\nu\|_{\mathrm{sv}}(A)$"):
            self.assertIn(phrase,body)

if __name__ == "__main__":
    unittest.main()
