"""Regression tests for source/AUX index identity, independent of PyMuPDF."""
import unittest
from tools.measure_theory_pdf_preflight import expected_destinations


class MeasureTheoryPdfIndexTests(unittest.TestCase):
    def setUp(self):
        self.index = "\\hyperref[a]{A}\n\\hyperref[b]{B}\n"
        self.aux = (
            r"\newlabel{a}{{1.1}{3}{Title with {nested} braces}{twierdzenie.1.1}{}}" + "\n"
            + r"\newlabel{b}{{2.4}{8}{Other title}{twierdzenie.2.4}{}}" + "\n"
            + r"\newlabel{example}{{2.5}{8}{Not indexed}{twierdzenie.2.5}{}}" + "\n"
        )

    def test_exact_destinations_and_growth(self):
        self.assertEqual(expected_destinations(self.index, self.aux),
                         {"twierdzenie.1.1", "twierdzenie.2.4"})
        self.assertEqual(len(expected_destinations(
            self.index + "\\hyperref[example]{C}\n", self.aux)), 3)

    def test_reject_duplicate_missing_and_wrong_kind(self):
        for index, aux in (
            (self.index + "\\hyperref[a]{Again}\n", self.aux),
            (self.index + "\\hyperref[c]{Missing}\n", self.aux),
            (self.index, self.aux.replace("twierdzenie.2.4", "section.2.4")),
            (self.index, self.aux.replace("twierdzenie.2.4", "twierdzenie.1.1")),
            (self.index, self.aux + self.aux),
            ("", self.aux),
        ):
            with self.subTest(index=index, aux=aux):
                with self.assertRaises(ValueError):
                    expected_destinations(index, aux)


if __name__ == "__main__":
    unittest.main()
