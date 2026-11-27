"""Prevent source-book preambles from drifting away from portable templates."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class PortablePreambleSyncTests(unittest.TestCase):
    def test_selected_canonical_preambles_remain_in_sync(self):
        # Probability templates intentionally have project-specific xr imports.
        # These volumes are exact mirrors; all definitions, styles and packages
        # must follow the canonical book, not a stale hand-maintained subset.
        pairs = {
            "AM2": "mathematical_analysis_ii",
            "GT": "general_topology",
            "GW": "graph_and_knot_theory",
            "KAT": "category_theory",
            "LA": "linear_algebra",
            "LST": "logic_and_set_theory",
            "ME": "measure_theory",
        }
        for key, book in pairs.items():
            with self.subTest(template=key):
                canonical = (ROOT / "books/pl" / f"{book}.tex").read_text(encoding="utf-8-sig")
                template = (ROOT / "application/config/preambles" / f"{key}.tex").read_text(encoding="utf-8-sig")
                self.assertIn(r"\begin{document}", canonical)
                self.assertEqual(template.strip(), canonical.split(r"\begin{document}", 1)[0].strip())


if __name__ == "__main__":
    unittest.main()
