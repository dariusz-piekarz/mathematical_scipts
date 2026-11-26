from pathlib import Path
import unittest


class AtlasRefOrder(unittest.TestCase):
    def test_fallback_precedes_first_use(self):
        root=Path(__file__).resolve().parents[4]
        source=(root/"chapters/pl/integration_theory/11-calka-lebesgue-a.tex").read_text(encoding="utf8")
        fallback=r"\providecommand{\atlasref}[2]{#2}"
        self.assertIn(fallback,source)
        self.assertLess(source.index(fallback),source.index(r"\atlasref{"))
        self.assertIn(r"\atlasref{ME-07::ch:calkowanie-lebesgue}",source)
        self.assertIn(r"\atlasref{ME-08::thm:dct}",source)
        self.assertIn(r"\atlasref{ME-12::thm:fubini-12}",source)

    def test_essential_scope_and_external_references(self):
        root = Path(__file__).resolve().parents[4]
        source = (root / "chapters/pl/integration_theory/11-calka-lebesgue-a.tex").read_text(encoding="utf8")
        for label in ("thm:mct", "thm:mct-ae", "thm:fatou", "thm:dct",
                      "cor:dct-l1", "cor:bct", "thm:sum-nonnegative-integrals",
                      "thm:sum-absolutely-integrable"):
            self.assertIn(r"\label{" + label + "}", source)
        for chapter, label in (("11", "ch:parametry-calki"),
                               ("12", "thm:fubini-12"),
                               ("13", "thm:change-variables-13"),
                               ("14", "thm:riesz-fischer-14"),
                               ("25", "thm:lebesgue-diff-25")):
            self.assertNotIn(r"\label{" + label + "}", source)
            self.assertIn(r"\atlasref{ME-" + chapter + "::" + label + "}", source)
            files = list((root / "chapters/pl/measure_theory").glob(chapter + "-*.tex"))
            self.assertEqual(len(files), 1)
            self.assertIn(r"\label{" + label + "}", files[0].read_text(encoding="utf8"))


if __name__=="__main__":
    unittest.main()
