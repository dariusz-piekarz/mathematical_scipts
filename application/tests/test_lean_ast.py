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


    def test_exhaustive_binary_operator_type_matrix(self):
        # Independent signature table; do not derive the oracle from ast.FIELDS.
        types = ("Prop", "Nat", "Int", "Real")
        signatures = {}
        for op in ("and", "or", "implies", "iff"):
            signatures[op] = {("Prop", "Prop", "Prop")}
        signatures["eq"] = {(t, t, "Prop") for t in types}
        for op in ("lt", "le"):
            signatures[op] = {(t, t, "Prop") for t in types[1:]}
        for op in ("add", "mul"):
            signatures[op] = {(t, t, t) for t in types[1:]}
        signatures["sub"] = {(t, t, t) for t in ("Int", "Real")}

        def term(t):
            return node("truth") if t == "Prop" else num(t)

        for op, allowed in signatures.items():
            for left in types:
                for right in types:
                    for claimed in types:
                        with self.subTest(op=op, left=left, right=right, claimed=claimed):
                            expr = node(op, claimed, left=term(left), right=term(right))
                            # Wrap numerical expressions to keep the root Prop;
                            # otherwise the document boundary masks operator errors.
                            root = expr if claimed == "Prop" else node(
                                "eq", left=expr, right=term(claimed))
                            result = validate(doc(root))
                            if (left, right, claimed) in allowed:
                                self.assertEqual(result["status"], "validated_ast", result)
                            else:
                                self.assertEqual(result.get("error"), "type_mismatch", result)
                                self.assertIsNone(result["ast"])

    def test_unary_operator_type_matrix(self):
        types = ("Prop", "Nat", "Int", "Real")
        for op, allowed in (("not", {"Prop"}), ("neg", {"Int", "Real"})):
            for arg in types:
                for claimed in types:
                    with self.subTest(op=op, arg=arg, claimed=claimed):
                        term = node("truth") if arg == "Prop" else num(arg)
                        expr = node(op, claimed, arg=term)
                        root = expr if claimed == "Prop" else node(
                            "eq", left=expr, right=num(claimed))
                        result = validate(doc(root))
                        if arg in allowed and claimed == arg:
                            self.assertEqual(result["status"], "validated_ast")
                        else:
                            self.assertEqual(result.get("error"), "type_mismatch")

    def test_exact_accepted_resource_limits(self):
        deep = node("truth")
        for _ in range(ast.MAX_DEPTH - 1):
            deep = node("not", arg=deep)
        result = validate(doc(deep))
        self.assertEqual(result["status"], "validated_ast")
        self.assertEqual(result["node_count"], 64)

        params = [binding(f"p{i}") for i in range(128)]
        result = validate(doc(var("p127"), params=params))
        self.assertEqual(result["status"], "validated_ast")
        self.assertEqual(result["binding_count"], 128)
        self.assert_rejected(doc(node("forall", binding=binding("extra"),
                                      body=node("truth")), params=params), "binding_limit")

        value = doc(assumptions=[node("truth") for _ in range(2047)])
        raw = json.dumps(value, separators=(",", ":")).encode()
        result = ast.validate_ast(SOURCE, raw)
        self.assertEqual(result["status"], "validated_ast")
        self.assertEqual(result["node_count"], 2048)
        self.assert_rejected(doc(node("not", arg=node("truth")),
                                 assumptions=value["assumptions"]), "node_limit")

        self.assertEqual(validate(doc(node("eq", left=num(digits="9"*64),
                                           right=num())))["status"], "validated_ast")
        source = "é" * 16384
        value = doc(source=source)
        self.assertEqual(validate(value, source)["status"], "validated_ast")
        raw = json.dumps(doc(), separators=(",", ":")).encode()
        padded = raw + b" " * (131072 - len(raw))
        self.assertEqual(ast.validate_ast(SOURCE, padded)["status"], "validated_ast")
        self.assertEqual(ast.validate_ast(SOURCE, padded+b" ")["error"], "ast_byte_limit")

    def test_disjoint_quantifiers_and_assumptions_do_not_share_scope(self):
        q = node("forall", binding=binding("local"), body=var("local"))
        self.assert_rejected(doc(node("and", left=q, right=copy.deepcopy(q))),
                             "duplicate_binding")
        self.assert_rejected(doc(var("local"), assumptions=[q]), "unbound_variable")
        self.assert_rejected(doc(node("truth"), assumptions=[q, var("local")]),
                             "unbound_variable")
        other = node("exists", binding=binding("other"), body=var("other"))
        self.assertEqual(validate(doc(node("and", left=q, right=other)))["status"],
                         "validated_ast")

    def test_json_escaped_keys_and_delimiters(self):
        self.assertEqual(ast.validate_ast(SOURCE, br'{"x":1,"\u0078":2}')["error"],
                         "duplicate_json_key")
        self.assertEqual(ast.validate_ast(SOURCE, b'{"x":[}')["error"], "invalid_json")
        # Escaped quotes, backslashes and brackets are display metadata,
        # not structural JSON delimiters or executable names.
        value = doc(params=[binding("p", name='[{\"\\}]')])
        self.assertEqual(validate(value)["status"], "validated_ast")
        value["parameters"][0]["name"] = "\ud800"
        raw = json.dumps(value, ensure_ascii=True).encode()
        self.assertEqual(ast.validate_ast(SOURCE, raw)["error"], "invalid_display_name")

    def test_unicode_codepoint_offsets_and_exact_source_hash(self):
        source = "a𐐀b"
        value = doc(source=source)
        value["conclusion"]["span"] = [1, 2]
        result = validate(value, source)
        self.assertEqual(result["status"], "validated_ast")
        self.assertEqual(source[slice(*result["ast"]["conclusion"]["span"])], "𐐀")
        value["conclusion"]["span"] = [2, 4]
        self.assert_rejected(value, "span_outside_parent", source)
        value = doc(source="é")
        value["conclusion"]["span"] = [0, 1]
        self.assertEqual(validate(value, "é")["status"], "validated_ast")
        self.assert_rejected(value, "source_hash_mismatch", "e\u0301")

    def test_validated_ast_does_not_claim_source_coverage(self):
        source = "False"
        value = doc(source=source)
        value["conclusion"]["span"] = [0, 5]
        result = validate(value, source)
        self.assertEqual(result["status"], "validated_ast")
        self.assertEqual(result["statement_status"], "unreviewed")
        self.assertEqual(result["proof_status"], "not_run")
        self.assertEqual(result["candidate_status"], "not_generated")
        self.assertFalse(result["certificate"])
        self.assertIsNone(result["lean_code"])



if __name__ == "__main__":
    unittest.main()
