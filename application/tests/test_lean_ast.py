"""L1.5.3: explicit AST contract, no LaTeX parser or Lean execution."""
import copy
import hashlib
import json
import unittest

from backend import lean_ast as ast

SOURCE = "∀ x ∈ ℝ, α → β " + "x" * 100
SPAN = [0, len(SOURCE)]


def node(kind, typ="Prop", **fields):
    return {"kind": kind, "type": typ, "span": SPAN[:], **fields}


def binding(ident, typ="Prop", name="x"):
    return {"id": ident, "name": name, "type": typ, "span": [2, 3]}


def var(ident, typ="Prop"):
    return node("var", typ, binding_id=ident)


def num(typ="Nat", digits="0"):
    return node("numeral", typ, digits=digits)


def doc(conclusion=None, params=None, assumptions=None, source=SOURCE):
    return {"schema_version": 1, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "parameters": params or [], "assumptions": assumptions or [],
            "conclusion": conclusion if conclusion is not None else node("truth")}


def validate(value, source=SOURCE):
    return ast.validate_ast(source, json.dumps(value, ensure_ascii=False).encode())


class LeanASTTests(unittest.TestCase):
    def assert_rejected(self, value, error, source=SOURCE):
        result = validate(value, source)
        self.assertNotEqual(result["status"], "validated_ast", result)
        self.assertEqual(result["error"], error)
        self.assertIsNone(result["ast"])
        self.assertIsNone(result["lean_code"])
        self.assertFalse(result["certificate"])

    def test_logic_and_deterministic_digest(self):
        p, q = var("p"), var("q")
        implication = node("implies", left=node("and", left=p, right=q),
                           right=node("or", left=p, right=node("not", arg=q)))
        value = doc(implication, [binding("p"), binding("q")], [p, q, p])
        a = validate(value)
        self.assertEqual(a["status"], "validated_ast")
        self.assertEqual(a, validate(value))
        self.assertEqual(a["ast"]["assumptions"], [p, q, p])
        self.assertEqual(a["candidate_status"], "not_generated")
        self.assertFalse(a["certificate"])
        self.assertFalse(a["external_transfer_allowed"])
        value["assumptions"] = [q, p, p]
        self.assertNotEqual(a["ast_sha256"], validate(value)["ast_sha256"])
        value["conclusion"]["span"] = [0, len(SOURCE)-1]
        self.assert_rejected(value, "span_outside_parent")

    def test_quantifier_scope_and_shadowing(self):
        body = node("forall", binding=binding("outer", "Real"),
                    body=node("exists", binding=binding("inner", "Real"),
                              body=node("eq", left=var("outer", "Real"),
                                        right=var("inner", "Real"))))
        self.assertEqual(validate(doc(body))["status"], "validated_ast")
        self.assert_rejected(doc(node("and", left=body, right=var("inner"))),
                             "unbound_variable")
        bad = copy.deepcopy(body)
        bad["body"]["binding"]["id"] = "outer"
        self.assert_rejected(doc(bad), "duplicate_binding")
        self.assert_rejected(doc(var("unknown")), "unbound_variable")

    def test_numeric_types_and_no_coercions(self):
        for typ in ("Nat", "Int", "Real"):
            with self.subTest(typ=typ):
                a = node("add", typ, left=num(typ), right=num(typ, "2"))
                b = node("mul", typ, left=num(typ), right=a)
                self.assertEqual(validate(doc(node("le", left=a, right=b)))["status"],
                                 "validated_ast")
        for op in ("neg", "sub"):
            fields = {"arg": num()} if op == "neg" else {"left": num(), "right": num()}
            self.assert_rejected(doc(node("eq", left=node(op, "Nat", **fields),
                                          right=num())), "type_mismatch")
        self.assert_rejected(doc(node("eq", left=num(), right=num("Int"))), "type_mismatch")
        for typ in ("Int", "Real"):
            neg = node("neg", typ, arg=num(typ))
            sub = node("sub", typ, left=num(typ), right=neg)
            self.assertEqual(validate(doc(node("lt", left=neg, right=sub)))["status"],
                             "validated_ast")
        self.assert_rejected(doc(node("truth", "Nat")), "type_mismatch")

    def test_prop_equality_distinct_from_iff(self):
        eq = doc(node("eq", left=node("truth"), right=node("falsehood")))
        iff = doc(node("iff", left=node("truth"), right=node("falsehood")))
        a, b = validate(eq), validate(iff)
        self.assertEqual(a["status"], "validated_ast")
        self.assertEqual(b["status"], "validated_ast")
        self.assertNotEqual(a["ast_sha256"], b["ast_sha256"])

    def test_closed_schema(self):
        for kind in ("pow", "div", "unknown", "by"):
            self.assert_rejected(doc(node(kind)), "unsupported_kind")
        self.assert_rejected(doc(node("truth", injected="code")), "invalid_fields")
        self.assert_rejected(doc(node("truth", "String")), "unsupported_type")
        self.assert_rejected(doc(num()), "expected_proposition")
        self.assert_rejected(doc(assumptions=[num()]), "expected_proposition")
        self.assert_rejected(doc(node("forall", binding=binding("x"), body=num())),
                             "type_mismatch")
        value = doc()
        value["schema_version"] = True
        self.assert_rejected(value, "unsupported_schema")

    def test_numerals(self):
        for digits in ("00", "-1", "1.2", "1; run", "١", "9"*65, 1, True):
            with self.subTest(digits=digits):
                self.assert_rejected(doc(node("eq", left=num(digits=digits), right=num())),
                                     "invalid_numeral")

    def test_source_spans_and_hash(self):
        value = doc()
        self.assert_rejected(value, "source_hash_mismatch", SOURCE+"!")
        for span in ([True, 2], [-1, 2], [1, 1], [0, len(SOURCE)+1]):
            bad = doc(node("truth"))
            bad["conclusion"]["span"] = span
            result = validate(bad)
            self.assertNotEqual(result["status"], "validated_ast")
        bad = doc()
        bad["conclusion"]["span"] = [0, 1]
        good = validate(bad)
        self.assertEqual(good["status"], "validated_ast")
        self.assertNotEqual(good["ast_sha256"], validate(value)["ast_sha256"])
        self.assertEqual(ast.validate_ast("", b"{}")["error"], "invalid_source")
        self.assertEqual(ast.validate_ast("é"*16385, b"{}")["error"], "source_byte_limit")
        self.assertEqual(ast.validate_ast("\ud800", b"{}")["error"], "invalid_source_encoding")

    def test_json_boundary(self):
        for data, error in [
            (b'{"x":1,"x":2}', "duplicate_json_key"),
            (b'{"x":NaN}', "noninteger_json_number"),
            (b'{"x":1.0}', "noninteger_json_number"),
            (b'{"x":12345678901}', "integer_limit"),
            (b'\xff', "invalid_json"),
            (b'['*100+b']'*100, "json_depth_limit"),
            (b' '* (ast.MAX_AST_BYTES+1), "ast_byte_limit"),
            ({}, "ast_must_be_bytes"),
        ]:
            self.assertEqual(ast.validate_ast(SOURCE, data)["error"], error)

    def test_depth_and_binding_limits(self):
        deep = node("truth")
        for _ in range(ast.MAX_DEPTH):
            deep = node("not", arg=deep)
        self.assert_rejected(doc(deep), "node_depth_limit")
        self.assert_rejected(doc(params=[binding(f"p{i}") for i in range(129)]),
                             "binding_limit")
        self.assert_rejected(doc(params=[binding("p"), binding("p")]), "duplicate_binding")
        self.assert_rejected(doc(params=[binding("p;code")]), "invalid_binding_id")

    def test_node_limit(self):
        # Compact JSON stays below byte cap; the independent node cap triggers.
        value = doc(assumptions=[node("truth") for _ in range(ast.MAX_NODES)])
        raw = json.dumps(value, separators=(",", ":")).encode()
        self.assertLessEqual(len(raw), ast.MAX_AST_BYTES)
        self.assertEqual(ast.validate_ast(SOURCE, raw)["error"], "node_limit")

    def test_canonical_expansion_limit(self):
        # ASCII escaping expands display-only non-ASCII names.
        params = [binding(f"p{i}", name="𐐀"*64) for i in range(128)]
        value = doc(params=params, assumptions=[node("truth") for _ in range(700)])
        raw = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()
        self.assertLessEqual(len(raw), ast.MAX_AST_BYTES)
        self.assertEqual(ast.validate_ast(SOURCE, raw)["error"], "canonical_byte_limit")


if __name__ == "__main__":
    unittest.main()
