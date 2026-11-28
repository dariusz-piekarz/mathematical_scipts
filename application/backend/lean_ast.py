"""L1.5.3: bounded, offline validation of explicitly typed intermediate AST.

This is not a LaTeX parser, a Lean generator, or semantic certification.
Only bytes containing JSON are accepted, never arbitrary Python objects.
"""
from __future__ import annotations

import hashlib
import json
import re

SCHEMA_VERSION = 1
MAX_SOURCE_BYTES = 32768
MAX_AST_BYTES = 131072
MAX_NODES = 2048
MAX_DEPTH = 64
MAX_BINDINGS = 128
MAX_DIGITS = 64
MAX_JSON_DEPTH = MAX_DEPTH + 5
TYPES = frozenset(("Prop", "Nat", "Int", "Real"))
NUMERIC = TYPES - {"Prop"}
FIELDS = {
    "var": {"binding_id"}, "numeral": {"digits"},
    "truth": set(), "falsehood": set(),
    "not": {"arg"}, "neg": {"arg"},
    **{op: {"left", "right"} for op in
       ("and", "or", "implies", "iff", "eq", "lt", "le", "add", "mul", "sub")},
    "forall": {"binding", "body"}, "exists": {"binding", "body"},
}
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,63}")
DIGITS = re.compile(r"0|[1-9][0-9]{0,63}")


class Rejected(ValueError):
    def __init__(self, code: str, path: str, status: str = "invalid_input"):
        self.code, self.path, self.status = code, path, status
        super().__init__(f"{code}: {path}")


def reject(code, path, status="invalid_input"):
    raise Rejected(code, path, status)


def _json_depth(data):
    # Bound parser recursion before json.loads, ignoring escaped delimiters
    # inside strings. Syntax validation remains the JSON decoder's job.
    depth = 0
    quoted = escaped = False
    for byte in data:
        if quoted:
            if escaped:
                escaped = False
            elif byte == 92:
                escaped = True
            elif byte == 34:
                quoted = False
        elif byte == 34:
            quoted = True
        elif byte in (123, 91):
            depth += 1
            if depth > MAX_JSON_DEPTH:
                reject("json_depth_limit", "$")
        elif byte in (125, 93):
            depth -= 1
            if depth < 0:
                reject("invalid_json", "$")


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            reject("duplicate_json_key", "$")
        result[key] = value
    return result


def _integer(value):
    # The schema only uses small integers for versions and offsets.
    if len(value) > 10:
        reject("integer_limit", "$")
    return int(value)


def _noninteger(_):
    reject("noninteger_json_number", "$")


def _decode(data):
    if type(data) is not bytes:
        reject("ast_must_be_bytes", "$")
    if len(data) > MAX_AST_BYTES:
        reject("ast_byte_limit", "$")
    _json_depth(data)
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=_pairs,
                          parse_int=_integer, parse_float=_noninteger,
                          parse_constant=_noninteger)
    except (UnicodeError, json.JSONDecodeError, RecursionError):
        reject("invalid_json", "$")


def _fields(value, expected, path):
    if type(value) is not dict or set(value) != expected:
        reject("invalid_fields", path)


def _type(value, path):
    if type(value) is not str or value not in TYPES:
        reject("unsupported_type", path, "unsupported")
    return value


def _span(value, parent, path):
    if (type(value) is not list or len(value) != 2
            or any(type(i) is not int for i in value)):
        reject("invalid_span", path)
    start, end = value
    if not parent[0] <= start < end <= parent[1]:
        reject("span_outside_parent", path)
    return start, end


def _id(value, path):
    if type(value) is not str or IDENTIFIER.fullmatch(value) is None:
        reject("invalid_binding_id", path)
    return value


class _Validator:
    def __init__(self, source):
        self.source_span = (0, len(source))
        self.nodes = 0
        self.seen = set()

    def binding(self, value, parent, path):
        _fields(value, {"id", "name", "type", "span"}, path)
        ident = _id(value["id"], path + ".id")
        if ident in self.seen:
            reject("duplicate_binding", path)
        if len(self.seen) >= MAX_BINDINGS:
            reject("binding_limit", path)
        name = value["name"]
        # Display metadata only. It must never become executable Lean code.
        if (type(name) is not str or not 1 <= len(name) <= 64
                or not name.isprintable() or not name.strip()):
            reject("invalid_display_name", path + ".name")
        _span(value["span"], parent, path + ".span")
        typ = _type(value["type"], path + ".type")
        self.seen.add(ident)
        return ident, typ

    def node(self, value, parent, env, path, depth=1):
        if depth > MAX_DEPTH:
            reject("node_depth_limit", path)
        self.nodes += 1
        if self.nodes > MAX_NODES:
            reject("node_limit", path)
        if type(value) is not dict:
            reject("invalid_node", path)
        op = value.get("kind")
        if type(op) is not str or op not in FIELDS:
            reject("unsupported_kind", path, "unsupported")
        _fields(value, {"kind", "type", "span"} | FIELDS[op], path)
        span = _span(value["span"], parent, path + ".span")
        claimed = _type(value["type"], path + ".type")

        def child(key, scope=env):
            return self.node(value[key], span, scope, path + "." + key, depth+1)

        if op == "var":
            ident = _id(value["binding_id"], path + ".binding_id")
            if ident not in env:
                reject("unbound_variable", path)
            inferred = env[ident]
        elif op == "numeral":
            digits = value["digits"]
            if (type(digits) is not str or len(digits) > MAX_DIGITS
                    or DIGITS.fullmatch(digits) is None):
                reject("invalid_numeral", path)
            if claimed not in NUMERIC:
                reject("type_mismatch", path)
            inferred = claimed
        elif op in ("truth", "falsehood"):
            inferred = "Prop"
        elif op in ("forall", "exists"):
            ident, typ = self.binding(value["binding"], span, path + ".binding")
            if child("body", {**env, ident: typ}) != "Prop":
                reject("type_mismatch", path)
            inferred = "Prop"
        elif op in ("not", "neg"):
            arg = child("arg")
            allowed = {"Prop"} if op == "not" else {"Int", "Real"}
            if arg not in allowed:
                reject("type_mismatch", path)
            inferred = arg
        else:
            left, right = child("left"), child("right")
            if left != right:
                reject("type_mismatch", path)
            if op in ("and", "or", "implies", "iff"):
                if left != "Prop":
                    reject("type_mismatch", path)
                inferred = "Prop"
            elif op == "eq":
                inferred = "Prop"
            elif op in ("lt", "le", "add", "mul", "sub"):
                allowed = {"Int", "Real"} if op == "sub" else NUMERIC
                if left not in allowed:
                    reject("type_mismatch", path)
                inferred = "Prop" if op in ("lt", "le") else left
            else:  # defensive: adding a kind requires an explicit rule
                reject("unsupported_kind", path, "unsupported")
        if inferred != claimed:
            reject("type_mismatch", path + ".type")
        return inferred

    def document(self, value, digest):
        _fields(value, {"schema_version", "source_sha256", "parameters",
                        "assumptions", "conclusion"}, "$")
        if type(value["schema_version"]) is not int or value["schema_version"] != SCHEMA_VERSION:
            reject("unsupported_schema", "$.schema_version", "unsupported")
        if value["source_sha256"] != digest:
            reject("source_hash_mismatch", "$.source_sha256")
        params, assumptions = value["parameters"], value["assumptions"]
        if type(params) is not list or type(assumptions) is not list:
            reject("invalid_document_lists", "$")
        if len(params) > MAX_BINDINGS:
            reject("binding_limit", "$.parameters")
        if len(assumptions) >= MAX_NODES:
            reject("node_limit", "$.assumptions")
        env = {}
        for i, binding in enumerate(params):
            ident, typ = self.binding(binding, self.source_span, f"$.parameters[{i}]")
            env[ident] = typ
        for i, assumption in enumerate(assumptions):
            path = f"$.assumptions[{i}]"
            if self.node(assumption, self.source_span, env, path) != "Prop":
                reject("expected_proposition", path)
        if self.node(value["conclusion"], self.source_span, env, "$.conclusion") != "Prop":
            reject("expected_proposition", "$.conclusion")


def validate_ast(source: str, ast_json: bytes) -> dict:
    """Validate an explicit AST, preserving all ordered lists and source spans.

    A validated AST is not evidence that a LaTeX parser has covered the source.
    """
    result = {"schema_version": SCHEMA_VERSION, "candidate_status": "not_generated",
              "proof_status": "not_run", "statement_status": "unreviewed",
              "certificate": False, "external_cost_minor_units": 0,
              "external_transfer_allowed": False, "lean_code": None}
    try:
        if type(source) is not str or not source:
            reject("invalid_source", "$.source")
        if len(source) > MAX_SOURCE_BYTES:
            reject("source_byte_limit", "$.source")
        try:
            encoded = source.encode("utf-8")
        except UnicodeError:
            reject("invalid_source_encoding", "$.source")
        if len(encoded) > MAX_SOURCE_BYTES:
            reject("source_byte_limit", "$.source")
        digest = hashlib.sha256(encoded).hexdigest()
        value = _decode(ast_json)
        validator = _Validator(source)
        validator.document(value, digest)
        canonical = json.dumps(value, ensure_ascii=True, sort_keys=True,
                               separators=(",", ":")).encode("ascii")
        if len(canonical) > MAX_AST_BYTES:
            reject("canonical_byte_limit", "$")
        return {**result, "status": "validated_ast", "source_sha256": digest,
                "ast_sha256": hashlib.sha256(canonical).hexdigest(),
                "ast": value, "node_count": validator.nodes,
                "binding_count": len(validator.seen)}
    except Rejected as exc:
        return {**result, "status": exc.status, "error": exc.code,
                "path": exc.path, "ast": None}
