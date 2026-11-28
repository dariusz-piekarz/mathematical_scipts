"""L1.5.4 parser: concrete AST, scope, complete source and resource bounds."""
import copy
import hashlib
import json
import unittest

from backend import lean_ast as ast
from backend import lean_parser as parser


def pilot(parameters=(), assumptions=(), conclusion="⊤"):
    chunks = [(r, s) for r, seq in (("parameter", parameters),
                                    ("assumption", assumptions),
                                    ("conclusion", [conclusion])) for s in seq]
    segments, texts = [], []
    offset = 0
    for role, s in chunks:
        segments.append({"role": role, "span": [offset, offset+len(s)]})
        texts.append(s)
        offset += len(s)+1
    return "\n".join(texts), segments


def parse(parameters=(), assumptions=(), conclusion="⊤"):
    return parser.parse_pilot_statement(*pilot(parameters, assumptions, conclusion))


def shape(n):
    kind = n["kind"]
    if kind == "var":
        return n["binding_id"]
    if kind == "numeral":
        return kind, n["type"], n["digits"]
    if kind in ("truth", "falsehood"):
        return kind
    if kind in ("forall", "exists"):
        return kind, n["binding"]["id"], n["binding"]["type"], shape(n["body"])
    if "arg" in n:
        return kind, shape(n["arg"])
    return kind, shape(n["left"]), shape(n["right"])


class LeanParserTests(unittest.TestCase):
    def assert_shape(self, result, expected):
        self.assertIn(result["status"], ("parsed_formula", "parsed_pilot_statement"), result)
        self.assertEqual(shape(result["ast"]["conclusion"]), expected)
        self.assertFalse(result["certificate"])
        self.assertIsNone(result["lean_code"])

    def assert_refused(self, result, code=None):
        self.assertIn(result["status"], ("unsupported", "invalid_input"), result)
        if code:
            self.assertEqual(result["error"], code, result)
        self.assertIsNone(result["ast"])
        self.assertIsNone(result["lean_code"])
        self.assertFalse(result["certificate"])

    def test_precedence_and_associativity(self):
        p = ["P:Prop", "Q:Prop", "R:Prop"]
        for formula, expected in [
            (r"P\to Q\to R", ("implies", "b1", ("implies", "b2", "b3"))),
            (r"(P\to Q)\to R", ("implies", ("implies", "b1", "b2"), "b3")),
            (r"P\lor Q\land R", ("or", "b1", ("and", "b2", "b3"))),
            (r"\neg(P\land Q)", ("not", ("and", "b1", "b2"))),
            ("P=Q", ("eq", "b1", "b2")),
            (r"P\iff Q", ("iff", "b1", "b2")),
            ("P∧Q∧R", ("and", ("and", "b1", "b2"), "b3")),
        ]:
            with self.subTest(formula=formula):
                self.assert_shape(parse(p, conclusion=formula), expected)

    def test_arithmetic_and_reverse_relations(self):
        p = ["x:Int", "y:Int", "z:Int"]
        self.assert_shape(parse(p, conclusion="x-y-z=x"),
                          ("eq", ("sub", ("sub", "b1", "b2"), "b3"), "b1"))
        self.assert_shape(parse(p, conclusion=r"x+y\cdot z=x"),
                          ("eq", ("add", "b1", ("mul", "b2", "b3")), "b1"))
        r = parse(p, conclusion=r"x\geq y")
        self.assert_shape(r, ("le", "b2", "b1"))
        self.assertEqual(r["trace"]["rules"][0]["rule"], "GE_REVERSE")
        self.assert_shape(parse(["x:Real"], conclusion="x+(2:Real)=x"),
                          ("eq", ("add", "b1", ("numeral", "Real", "2")), "b1"))
        self.assert_shape(parse(["x:Int"], conclusion="-(2:Int)=x"),
                          ("eq", ("neg", ("numeral", "Int", "2")), "b1"))

    def test_quantifier_scope_and_whole_type(self):
        self.assert_shape(parser.parse_formula(r"\forall x:Real,\exists x:Real,x=x"),
                          ("forall", "b1", "Real", ("exists", "b2", "Real", ("eq", "b2", "b2"))))
        r = parser.parse_formula(r"\forall x\in\mathbb{R},x=x")
        self.assert_shape(r, ("forall", "b1", "Real", ("eq", "b1", "b1")))
        self.assertEqual(r["trace"]["rules"][0]["rule"], "IN_WHOLE_NUMERIC_TYPE")
        self.assert_shape(parse(["x:Real"], conclusion="(∀x:Real,x=x)∧x=x"),
                          ("and", ("forall", "b2", "Real", ("eq", "b2", "b2")),
                           ("eq", "b1", "b1")))
        self.assert_refused(parser.parse_formula("(∃x:Real,x=x)∧x=x"), "unbound_variable")
        self.assert_refused(parser.parse_formula("∀x∈Prop,x"), "unsupported_membership_type")
        self.assert_refused(parse(["x:Real"], conclusion="x∈ℝ"), "unexpected_token")

    def test_all_source_and_duplicate_assumptions(self):
        source, segments = pilot(["P:Prop", "Q:Prop"], ["P", "P"], r"P\to Q")
        r = parser.parse_pilot_statement(source, segments)
        self.assert_shape(r, ("implies", "b1", "b2"))
        self.assertEqual([shape(a) for a in r["ast"]["assumptions"]], ["b1", "b1"])
        self.assertNotEqual(*[a["span"] for a in r["ast"]["assumptions"]])
        self.assertEqual(r["source_sha256"], hashlib.sha256(source.encode()).hexdigest())
        self.assertEqual(r, parser.parse_pilot_statement(source, segments))
        raw = json.dumps(r["ast"]).encode()
        self.assertEqual(ast.validate_ast(source, raw)["ast_sha256"], r["ast_sha256"])
        self.assert_refused(parser.parse_pilot_statement(source, segments[:2]+segments[3:]),
                            "uncovered_source")
        self.assert_refused(parser.parse_pilot_statement(source+" P", segments), "uncovered_source")
        self.assert_refused(parser.parse_pilot_statement(source, segments[:-1]), "invalid_segment_order")
        bad = copy.deepcopy(segments)
        bad[1]["span"][0] = bad[0]["span"][0]
        self.assert_refused(parser.parse_pilot_statement(source, bad), "invalid_segment_span")
        bad = copy.deepcopy(segments)
        bad[0]["span"][1] -= 1
        self.assert_refused(parser.parse_pilot_statement(source, bad), "split_token")

    def test_token_boundaries_and_global_lexing(self):
        source = "P:PropQ:Prop P"
        segments = [{"role": "parameter", "span": [0,6]},
                    {"role": "parameter", "span": [6,12]},
                    {"role": "conclusion", "span": [13,14]}]
        self.assert_refused(parser.parse_pilot_statement(source, segments),
                            "unsupported_identifier")
        source = r"P:Prop Q:Prop P\land Q"
        segments = [{"role": "parameter", "span": [0,6]},
                    {"role": "parameter", "span": [7,13]},
                    {"role": "assumption", "span": [14,17]},
                    {"role": "conclusion", "span": [17,len(source)]}]
        self.assert_refused(parser.parse_pilot_statement(source, segments), "split_token")
        self.assert_refused(parser.parse_pilot_statement("  ⊤", [
            {"role":"assumption","span":[0,1]}, {"role":"conclusion","span":[2,3]}]),
            "empty_segment")
        self.assert_refused(parser.parse_pilot_statement("⊤⊤", [
            {"role":"assumption","span":[0,1]}, {"role":"conclusion","span":[1,2]}]),
            "missing_segment_separator")

    def test_type_and_syntax_refusals(self):
        for p, formula, error in [
            (["x:Nat"], "x-x=x", "type_mismatch"),
            (["x:Real","n:Nat"], "x=n", "type_mismatch"),
            (["x:Real"], "x+2=x", "explicit_numeral_type_required"),
            (["x:Real"], "x<x<x", "nonassociative_chain"),
            (["P:Prop","Q:Prop"], "P↔Q↔P", "nonassociative_chain"),
            (["x:Real"], r"\neg x<x", "type_mismatch"),
            (["P:Prop"], r"P\landscape P", "unsupported_command"),
            (["P:Prop"], "P P", "unexpected_token"),
            (["P:Prop"], "P%hidden", "unsupported_character"),
            (["P:Prop"], r"P\input{file}", "unsupported_command"),
            (["P:Prop"], "(P", "expected_rparen"),
            (["x:Real"], "x", "expected_proposition"),
            (["P:Prop"], "P→∀x:Real,x=x", "expected_atom"),
            ([], "(2:Prop)=(2:Prop)", "type_mismatch"),
        ]:
            with self.subTest(formula=formula):
                self.assert_refused(parse(p, conclusion=formula), error)
        self.assert_refused(parse(["P:Prop","P:Prop"], conclusion="P"), "duplicate_parameter")
        self.assert_refused(parse(["x:Real"], ["x"], "⊤"), "expected_proposition")
        self.assert_refused(parse([], ["∀x:Real,x=x"], "x=x"), "unbound_variable")

    def test_source_offsets_and_trace(self):
        source = r"\forall \alpha:\mathbb{R},\alpha≥α"
        r = parser.parse_formula(source)
        self.assert_shape(r, ("forall", "b1", "Real", ("le", "b1", "b1")))
        body = r["ast"]["conclusion"]["body"]
        self.assertEqual(source[slice(*body["left"]["span"])], "α")
        self.assertEqual(source[slice(*body["right"]["span"])], r"\alpha")
        for t in r["trace"]["tokens"][:-1]:
            self.assertTrue(source[slice(*t["span"])])
        self.assertEqual(r["coverage"], "controlled_pilot_only")

    def test_bounded_recursion_and_nodes(self):
        self.assert_refused(parser.parse_formula("("*65+"⊤"+")"*65), "syntax_depth_limit")
        self.assert_refused(parser.parse_formula("¬"*65+"⊤"), "syntax_depth_limit")
        self.assert_refused(parser.parse_formula("⊤→"*65+"⊤"), "syntax_depth_limit")
        self.assert_refused(parser.parse_formula("⊤∧"*64+"⊤"), "node_depth_limit")
        self.assert_refused(parse(assumptions=["⊤"]*2048), "node_limit")
        self.assert_refused(parser.parse_formula("("*8193), "token_limit")
        self.assert_refused(parser.parse_formula(" "*32769), "source_byte_limit")

    def test_invalid_segments_and_whitespace(self):
        for segments in (None, [], {}, [{"role":"conclusion","span":[True,1]}],
                         [{"role":"conclusion","span":[0,1],"extra":True}],
                         [{"role":[],"span":[0,1]}]):
            self.assert_refused(parser.parse_pilot_statement("⊤", segments))
        self.assert_refused(parser.parse_formula(" \r\n\t"), "empty_segment")
        self.assert_shape(parser.parse_formula(" \r\n⊤\t"), "truth")


    def test_independent_parenthesized_formula_oracle(self):
        # Build the expected tree independently of the parser's precedence
        # table. Explicit grouping removes any ambiguity in the generator.
        operators = {"and": "∧", "or": "∨", "implies": "→",
                     "iff": "↔", "eq": "="}
        leaves = ("P", "Q", "⊤", "⊥")
        names = {"P": "b1", "Q": "b2", "⊤": "truth", "⊥": "falsehood"}

        def render(tree):
            if isinstance(tree, str):
                return tree
            if tree[0] == "not":
                return "¬(" + render(tree[1]) + ")"
            op, left, right = tree
            return "(" + render(left) + operators[op] + render(right) + ")"

        def expected(tree):
            if isinstance(tree, str):
                return names[tree]
            return (tree[0], *(expected(child) for child in tree[1:]))

        trees = [(op, l, r) for op in operators for l in leaves for r in leaves]
        trees += [(outer, (inner, "P", "Q"), "P")
                  for outer in operators for inner in operators]
        trees += [(outer, "P", (inner, "Q", "P"))
                  for outer in operators for inner in operators]
        trees += [("not", tree) for tree in trees[:80]]
        self.assertEqual(len(trees), 210)
        for tree in trees:
            with self.subTest(tree=tree):
                self.assert_shape(parse(["P:Prop", "Q:Prop"], conclusion=render(tree)),
                                  expected(tree))

    def test_exact_parser_resource_boundaries(self):
        # Syntax depth and AST height differ for parentheses.
        self.assert_shape(parser.parse_formula("("*63 + "⊤" + ")"*63), "truth")
        self.assert_refused(parser.parse_formula("("*64 + "⊤" + ")"*64),
                            "syntax_depth_limit")
        r = parser.parse_formula("¬"*63+"⊤")
        self.assertEqual(r["status"], "parsed_formula", r)
        self.assertEqual(r["node_count"], 64)
        self.assert_refused(parser.parse_formula("¬"*64+"⊤"), "syntax_depth_limit")
        r = parser.parse_formula("⊤∧"*63+"⊤")
        self.assertEqual(r["status"], "parsed_formula", r)
        self.assertEqual(r["node_count"], 127)
        self.assert_refused(parser.parse_formula("⊤∧"*64+"⊤"), "node_depth_limit")
        # Separate assumptions may reuse a display name, but never an ID.
        quantified = ["∀x:Real,x=x"]*128
        r = parse(assumptions=quantified)
        self.assertEqual(r["status"], "parsed_pilot_statement", r)
        self.assertEqual(r["binding_count"], 128)
        self.assertEqual([a["binding"]["id"] for a in r["ast"]["assumptions"]],
                         [f"b{i}" for i in range(1, 129)])
        self.assert_refused(parse(assumptions=quantified+quantified[:1]), "binding_limit")
        r = parse(assumptions=["⊤"]*2047)
        self.assertEqual(r["status"], "parsed_pilot_statement", r)
        self.assertEqual(r["node_count"], 2048)
        self.assert_refused(parse(assumptions=["⊤"]*2048), "node_limit")

    def test_lexical_aliases_and_binder_identity(self):
        r = parse([r"\alpha:Real"], conclusion="α=α")
        self.assert_shape(r, ("eq", "b1", "b1"))
        self.assert_refused(parse([r"\alpha:Real", "α:Real"], conclusion="α=α"),
                            "duplicate_parameter")
        self.assert_shape(parse([r"\phi:Real", r"\varphi:Real"], conclusion="ϕ=φ"),
                          ("eq", "b1", "b2"))
        r = parse(["x:Real", "y:Real"], conclusion="x>y")
        self.assert_shape(r, ("lt", "b2", "b1"))
        self.assertEqual(r["trace"]["rules"][0]["rule"], "GT_REVERSE")

    def test_mixed_relations_and_explicit_grouping(self):
        self.assert_shape(parse(["x:Real", "y:Real", "z:Real"],
                                conclusion="x<y∧y≤z"),
                          ("and", ("lt", "b1", "b2"), ("le", "b2", "b3")))
        self.assert_refused(parse(["x:Real", "y:Real", "z:Real"],
                                  conclusion="x<y≤z"), "nonassociative_chain")
        self.assert_shape(parse(["P:Prop", "Q:Prop", "R:Prop"], conclusion="(P↔Q)↔R"),
                          ("iff", ("iff", "b1", "b2"), "b3"))
        self.assert_shape(parse(["P:Prop", "Q:Prop", "R:Prop"], conclusion="P↔(Q↔R)"),
                          ("iff", "b1", ("iff", "b2", "b3")))
        self.assert_refused(parse(["P:Prop", "Q:Prop", "R:Prop"], conclusion="P=Q=R"),
                            "nonassociative_chain")

    def test_actual_theorem_envelopes_are_not_formula_input(self):
        # These resemble the existing LST source constructs; none is claimed
        # to be a complete automatic transcription of a theorem.
        for source in (
            r"\begin{twierdzenie}Dla dowolnych formuł $p,q$ zachodzi "
            r"\neg(p\land q)\equiv(\neg p\lor\neg q).\end{twierdzenie}",
            r"\neg(p\land q)\equiv(\neg p\lor\neg q)",
            r"\exists!x\in D,P(x)",
            r"\forall x\in D,P(x)",
            r"\begin{align*}P&\iff Q\\Q&\iff P\end{align*}",
        ):
            with self.subTest(source=source):
                self.assert_refused(parser.parse_formula(source))



if __name__ == "__main__":
    unittest.main()
