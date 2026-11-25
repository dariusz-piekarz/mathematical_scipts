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


if __name__=="__main__":
    unittest.main()
