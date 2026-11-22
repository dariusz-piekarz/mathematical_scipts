"""Cross-chapter regression for the forcing and independence block (32-36).

These tests guard source integrity, dependency order, and the exact scope
of metamathematical claims. They are NOT proofs of the infinitary theorems
and do NOT replace independent mathematical review or Lean formalization.
"""
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/logic_and_set_theory"
NAMES = {
    32: "32-podstawy-wymuszania-i-modele-generyczne.tex",
    33: "33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex",
    34: "34-hipoteza-continuum-i-zastosowania-wymuszania.tex",
    35: "35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex",
    36: "36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex",
}
SOURCES = {
    chapter: (CHAPTERS / filename).read_text(encoding="utf-8")
    for chapter, filename in NAMES.items()
}


def labels(source):
    return re.findall(r"\\label\{([^}]+)\}", source)


def references(source):
    return re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", source)


def theorem_body(source, label):
    """Return a theorem environment containing an exact LaTeX label."""
    for match in re.finditer(
        r"\\begin\{twierdzenie\}.*?\\end\{twierdzenie\}", source, re.S
    ):
        if r"\label{" + label + "}" in match.group():
            return match.group()
    raise AssertionError(f"Missing theorem environment: {label}")


class TestForcingIndependenceCrossChapter(unittest.TestCase):
    def test_all_five_chapters_are_imported_in_order(self):
        book = (ROOT / "books/pl/logic_and_set_theory.tex").read_text("utf-8")
        catalog = json.loads(
            (ROOT / "catalog/books.json").read_text("utf-8")
        )
        entry = next(b for b in catalog["books"] if b["id"] == "logic_and_set_theory")
        indices = []
        for chapter, name in NAMES.items():
            source_path = f"chapters/pl/logic_and_set_theory/{name}"
            self.assertEqual(entry["chapters"][chapter - 1], source_path)
            token = r"\input{../../" + source_path + "}"
            self.assertEqual(book.count(token), 1)
            indices.append(book.index(token))
        self.assertEqual(indices, sorted(indices))

    def test_cross_chapter_prerequisites_are_referenced(self):
        # A source reference must actually be present; checking that the
        # target label exists globally would not detect a lost dependency.
        edges = [
            (33, 32, "def:forcing-names"),
            (33, 32, "cor:countable-generic"),
            (33, 32, "thm:forcing-extension-first"),
            (34, 33, "thm:forcing33-zfc"),
            (34, 33, "thm:forcing33-definability"),
            (34, 33, "thm:forcing33-main"),
            (35, 33, "thm:forcing33-definability"),
            (35, 34, "ch:forcing-continuum"),
            (35, 35, "thm:boolean35-fullness"),
            (35, 35, "thm:boolean35-quotient-truth"),
            (36, 33, "thm:forcing33-definability"),
            (36, 35, "ch:boolean-valued-independence"),
            (36, 36, "lem:sym36-finite-range"),
            (36, 36, "lem:sym36-arbitrary-model"),
        ]
        for source, target, label in edges:
            with self.subTest(source=source, target=target, label=label):
                self.assertIn(label, references(SOURCES[source]))
                self.assertIn(label, labels(SOURCES[target]))

    def test_all_local_references_and_environments_are_valid(self):
        label_list = [label for text in SOURCES.values() for label in labels(text)]
        self.assertEqual(len(label_list), len(set(label_list)))
        external_labels = set()
        for chapter in (30, 31):
            filename = next(CHAPTERS.glob(f"{chapter:02d}-*.tex"))
            external_labels.update(labels(filename.read_text(encoding="utf-8")))
        all_labels = set(label_list) | external_labels
        for chapter, source in SOURCES.items():
            with self.subTest(chapter=chapter):
                self.assertFalse(set(references(source)) - all_labels)
                stack = []
                for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
                    if kind == "begin":
                        stack.append(env)
                    else:
                        self.assertTrue(stack)
                        self.assertEqual(stack.pop(), env)
                self.assertFalse(stack)
                # Polish terminology: standalone shortened noun is forbidden.
                self.assertIsNone(
                    re.search(r"\bkardynał\w*", source, re.IGNORECASE)
                )

    def test_different_consistency_hypotheses_remain_explicit(self):
        # Chapter 34 proves conditional existence from a countable transitive
        # model; chapter 35 obtains Con(ZFC) implications without that premise.
        model_statement = theorem_body(SOURCES[34], "thm:forcing34-two-models")
        self.assertRegex(model_statement, r"przeliczalny\s+tranzytywny")
        self.assertIn(r"\models\mathrm{ZFC}", model_statement)

        boolean_statement = theorem_body(
            SOURCES[35], "thm:boolean35-relative-consistency"
        )
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC})", boolean_statement)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC}+\mathrm{CH})",
                      boolean_statement)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC}+\neg\mathrm{CH})",
                      boolean_statement)
        self.assertIn("dowolnym modelem zbiorowym", SOURCES[35])

        symmetric_statement = theorem_body(
            SOURCES[36], "thm:sym36-relative-consistency"
        )
        self.assertIn(r"\operatorname{Con}(\mathrm{ZFC})", symmetric_statement)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZF})", symmetric_statement)
        self.assertIn(r"\operatorname{Con}(\mathrm{ZF}+\neg\mathrm{AC})",
                      symmetric_statement)

    def test_distinct_methods_and_ad_limitation_are_preserved(self):
        # ccc preserves cardinals; countable closure prevents new
        # omega-sequences. These cannot be silently merged.
        self.assertIn(
            "thm:forcing34-ccc-preserves", labels(SOURCES[34])
        )
        self.assertIn(
            "lem:forcing34-closed-no-sequences", labels(SOURCES[34])
        )
        self.assertIn(r"\operatorname{Add}(\omega,\kappa)", SOURCES[34])
        self.assertIn(r"\operatorname{Coll}(\omega_1,\lambda)", SOURCES[34])

        # The boolean quotient needs a full-witness theorem for existence.
        self.assertIn("thm:boolean35-fullness", references(SOURCES[35]))
        self.assertIn("thm:boolean35-quotient-zfc", labels(SOURCES[35]))

        # The symmetric model refutes AC, not automatically proves AD.
        self.assertIn("thm:sym36-dedekind", labels(SOURCES[36]))
        self.assertIn("rem:sym36-ac-ad", labels(SOURCES[36]))
        self.assertRegex(
            SOURCES[36],
            r"sam brak wyboru nie implikuje determinacji"
        )


if __name__ == "__main__":
    unittest.main()
