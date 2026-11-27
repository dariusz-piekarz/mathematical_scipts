import tempfile
from pathlib import Path
import unittest

from scripts.audit_math_macros import audit


class MacroAuditTests(unittest.TestCase):
    def test_separates_covered_late_and_unsupported_declarations(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            preamble = root / "application/config/preambles/AM1.tex"
            preamble.parent.mkdir(parents=True)
            preamble.write_text(r"\newcommand{\R}{\mathbb R}", encoding="utf-8")
            chapter = root / "chapters/pl/mathematical_analysis_i/99-test.tex"
            chapter.parent.mkdir(parents=True)
            chapter.write_text("\n".join((
                r"\chapter{Fixture}",
                r"\providecommand{\local}{L}",
                r"\providecommand{\missing}{M}",
                r"\newcommand{\optional}[1][x]{#1}",
                "Prose",
                r"\newcommand{\late}{T}",
            )), encoding="utf-8")
            result = audit(root, {"AM1": {r"\R": r"\mathbb R"},
                                  "AM1-99": {r"\local": "L"}})
            self.assertEqual(result["counts"]["chapters"], 1)
            self.assertEqual(result["counts"]["preambles"], 1)
            self.assertEqual(result["counts"]["covered"], 2)
            self.assertEqual({row["macro"]: row["status"] for row in result["findings"]},
                             {r"\missing": "missing_profile_macro_review",
                              r"\optional": "unsupported_declaration_review",
                              r"\late": "late_declaration_review"})
