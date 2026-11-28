"""L1.5.4 lexer regressions; no parser, generation or Lean execution."""
import hashlib
import unittest

from backend import lean_lexer as lex


class LeanLexerTests(unittest.TestCase):
    def test_all_operator_aliases(self):
        cases = {
            "FORALL": [r"\forall", "∀"], "EXISTS": [r"\exists", "∃"],
            "IN": [r"\in", "∈"], "IFF": [r"\iff", r"\Leftrightarrow", "↔"],
            "IMPLIES": [r"\implies", r"\Rightarrow", r"\to", r"\rightarrow", "→"],
            "OR": [r"\lor", r"\vee", "∨"], "AND": [r"\land", r"\wedge", "∧"],
            "NOT": [r"\neg", r"\lnot", "¬"], "LE": [r"\le", r"\leq", "≤"],
            "GE": [r"\ge", r"\geq", "≥"], "LT": ["<"], "GT": [">"], "EQ": ["="],
            "MUL": [r"\cdot", r"\times", "×", "·"], "PLUS": ["+"], "MINUS": ["-"],
            "TRUE": [r"\top", "⊤"], "FALSE": [r"\bot", "⊥"],
            "LPAREN": ["("], "RPAREN": [")"], "COLON": [":"], "COMMA": [","],
        }
        for expected, aliases in cases.items():
            for alias in aliases:
                with self.subTest(alias=alias):
                    token, eof = lex.tokenize(alias)
                    self.assertEqual((token.kind, token.value, token.start, token.end),
                                     (expected, expected, 0, len(alias)))
                    self.assertEqual(eof.start, len(alias))

    def test_exact_types(self):
        for kind, forms in {
            "Prop": ["Prop"], "Nat": ["Nat", "ℕ", r"\mathbb{N}"],
            "Int": ["Int", "ℤ", r"\mathbb{Z}"], "Real": ["Real", "ℝ", r"\mathbb{R}"],
        }.items():
            for form in forms:
                with self.subTest(form=form):
                    t = lex.tokenize(form)[0]
                    self.assertEqual((t.kind, t.value), ("TYPE", kind))

    def test_original_offsets_and_digest(self):
        source = " \r\n∀ α:ℝ,α≥(2:Real)\t"
        result = lex.lex_formula(source)
        self.assertEqual(result["status"], "tokenized")
        self.assertEqual(result["source_sha256"], hashlib.sha256(source.encode()).hexdigest())
        self.assertEqual([source[a:b] for a,b in
                          [x["span"] for x in result["tokens"]]],
                         ["∀","α",":","ℝ",",","α","≥","(","2",":","Real",")",""])
        self.assertEqual(result, lex.lex_formula(source))
        self.assertIsNone(result["ast"])
        self.assertIsNone(result["lean_code"])
        self.assertFalse(result["certificate"])

    def test_greek_aliases_and_variants(self):
        for name, symbol in (("alpha", "α"), ("epsilon", "ϵ"), ("varepsilon", "ε"),
                             ("phi", "ϕ"), ("varphi", "φ")):
            self.assertEqual(lex.tokenize("\\"+name)[0].value, symbol)
            self.assertEqual(lex.tokenize(symbol)[0].value, symbol)
        self.assertNotEqual(lex.tokenize(r"\phi")[0].value,
                            lex.tokenize(r"\varphi")[0].value)

    def test_no_prefix_recognition_or_tex_execution(self):
        for source in (r"P\landscape Q", r"\input{file}", r"\def\x{P}",
                       r"\csname x\endcsname", r"\mathbb{Q}", r"\mathbb {R}",
                       r"\mathbb{RR}", r"\!", "P% hidden", "P\u00a0Q",
                       "Realx", "xy", "x_1", "x²", "$P$", "P𐐀",
                       r"\equiv", r"\left(P\right)", "P\\"):
            with self.subTest(source=source):
                result = lex.lex_formula(source)
                self.assertEqual(result["status"], "unsupported")
                self.assertIsNone(result["tokens"])
                self.assertFalse(result["certificate"])

    def test_invalid_numeral(self):
        for source in ("00", "01", "9"*65):
            self.assertEqual(lex.lex_formula(source)["error"], "invalid_numeral")
        self.assertEqual(lex.tokenize("9"*64)[0].value, "9"*64)
        self.assertEqual(lex.tokenize("0")[0].kind, "DIGITS")
        self.assertEqual(lex.lex_formula("١")["status"], "unsupported")

    def test_limits_and_bad_source(self):
        self.assertEqual(lex.lex_formula("")["error"], "invalid_source")
        self.assertEqual(lex.lex_formula(None)["error"], "invalid_source")
        self.assertEqual(lex.lex_formula("\ud800")["error"], "invalid_source_encoding")
        self.assertEqual(lex.lex_formula("α"*16385)["error"], "source_byte_limit")
        self.assertEqual(len(lex.tokenize("("*8192)), 8193)
        self.assertEqual(lex.lex_formula("("*8193)["error"], "token_limit")
        self.assertEqual(lex.lex_formula(" "*32768)["status"], "tokenized")
        self.assertEqual(lex.lex_formula(" "*32769)["error"], "source_byte_limit")

    def test_lexical_success_does_not_imply_valid_formula(self):
        for source in ("P Q", "x+2=x", "x<x<x", "(", "∀x:Real,"):
            result = lex.lex_formula(source)
            self.assertEqual(result["status"], "tokenized")
            self.assertEqual(result["coverage"], "lexical_only")
            self.assertEqual(result["statement_status"], "unreviewed")
            self.assertEqual(result["candidate_status"], "not_generated")
            self.assertEqual(result["proof_status"], "not_run")
            self.assertIsNone(result["ast"])

    def test_precise_error_after_valid_prefix(self):
        result = lex.lex_formula(r"P \landscape Q")
        self.assertEqual(result["error"], "unsupported_command")
        self.assertEqual(result["span"], [2, 12])
        self.assertIsNone(result["tokens"])


if __name__ == "__main__":
    unittest.main()
