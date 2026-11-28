"""L1.5.4: strict parser for explicitly segmented mathematical pilot input.

No theorem-environment adapter, TeX expansion, Lean generation or execution.
"""
from __future__ import annotations

from dataclasses import dataclass
import json

from backend import lean_ast as ast
from backend import lean_lexer as lex

# precedence, associativity, AST kind
BINARY = {
    "IFF": (1, "non", "iff"), "IMPLIES": (2, "right", "implies"),
    "OR": (3, "left", "or"), "AND": (4, "left", "and"),
    "EQ": (5, "non", "eq"), "LT": (5, "non", "lt"),
    "GT": (5, "non", "lt"), "LE": (5, "non", "le"), "GE": (5, "non", "le"),
    "PLUS": (6, "left", "add"), "MINUS": (6, "left", "sub"),
    "MUL": (7, "left", "mul"),
}
MAX_SEGMENTS = ast.MAX_BINDINGS + ast.MAX_NODES
NUMERIC = {"Nat", "Int", "Real"}


class ParseError(ValueError):
    def __init__(self, code, span, status="unsupported"):
        self.code, self.span, self.status = code, list(span), status
        super().__init__(code)


def _fail(code, span, status="unsupported"):
    raise ParseError(code, span, status)


def _token_span(token):
    return [token.start, token.end]


def _partition(source, tokens, segments):
    """Validate caller-selected roles and partition one global token stream."""
    if type(segments) is not list or not 1 <= len(segments) <= MAX_SEGMENTS:
        _fail("invalid_segments", [0, len(source)], "invalid_input")
    ranks = {"parameter": 0, "assumption": 1, "conclusion": 2}
    previous_end = 0
    previous_rank = 0
    cursor = 0
    output = []
    for index, segment in enumerate(segments):
        if type(segment) is not dict or set(segment) != {"role", "span"}:
            _fail("invalid_segment_fields", [0, len(source)], "invalid_input")
        role, span = segment["role"], segment["span"]
        if type(role) is not str or role not in ranks:
            _fail("invalid_segment_role", [0, len(source)], "invalid_input")
        if (type(span) is not list or len(span) != 2
                or any(type(x) is not int for x in span)):
            _fail("invalid_segment_span", [0, len(source)], "invalid_input")
        start, end = span
        if not previous_end <= start < end <= len(source):
            _fail("invalid_segment_span", [0, len(source)], "invalid_input")
        if ranks[role] < previous_rank or (role == "conclusion") != (index == len(segments)-1):
            _fail("invalid_segment_order", span, "invalid_input")
        gap = source[previous_end:start]
        if any(c not in lex.WHITESPACE for c in gap):
            _fail("uncovered_source", [previous_end, start], "invalid_input")
        if index and not gap:
            _fail("missing_segment_separator", [start, start], "invalid_input")
        part = []
        while cursor < len(tokens)-1 and tokens[cursor].start < end:
            t = tokens[cursor]
            if t.start < start or t.end > end:
                _fail("split_token", _token_span(t), "invalid_input")
            part.append(t)
            cursor += 1
        if not part:
            _fail("empty_segment", span, "invalid_input")
        # An omitted whole token cannot be hidden by whitespace or by roles.
        output.append((role, tuple(part) + (lex.Token("EOF", "", end, end),)))
        previous_end, previous_rank = end, ranks[role]
    if cursor != len(tokens)-1 or any(c not in lex.WHITESPACE for c in source[previous_end:]):
        _fail("uncovered_source", [previous_end, len(source)], "invalid_input")
    return output


@dataclass
class _Expr:
    value: dict
    height: int


class _State:
    def __init__(self):
        self.nodes = 0
        self.bindings = 0
        self.rules = []

    def node(self, kind, typ, span, children=(), **fields):
        height = 1 + max((child.height for child in children), default=0)
        self.nodes += 1
        if self.nodes > ast.MAX_NODES:
            _fail("node_limit", span, "invalid_input")
        if height > ast.MAX_DEPTH:
            _fail("node_depth_limit", span, "invalid_input")
        return _Expr({"kind": kind, "type": typ, "span": list(span), **fields}, height)

    def binding(self, name, typ, span):
        self.bindings += 1
        if self.bindings > ast.MAX_BINDINGS:
            _fail("binding_limit", span, "invalid_input")
        return {"id": f"b{self.bindings}", "name": name, "type": typ, "span": list(span)}


class _Parser:
    def __init__(self, tokens, state, env):
        self.tokens, self.state, self.env = tokens, state, dict(env)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def take(self, kind=None):
        t = self.peek()
        if kind is not None and t.kind != kind:
            _fail("expected_" + kind.lower(), _token_span(t))
        if t.kind != "EOF":
            self.pos += 1
        return t

    def finish(self):
        if self.peek().kind != "EOF":
            _fail("unexpected_token", _token_span(self.peek()))

    def check_depth(self, depth):
        if depth > ast.MAX_DEPTH:
            _fail("syntax_depth_limit", _token_span(self.peek()), "invalid_input")

    def declaration(self):
        name = self.take("IDENT")
        self.take("COLON")
        typ = self.take("TYPE")
        self.finish()
        if name.value in self.env:
            _fail("duplicate_parameter", _token_span(name))
        return self.state.binding(name.value, typ.value, [name.start, typ.end])

    def formula(self):
        expr = self.expression(1, 1, True)
        self.finish()
        if expr.value["type"] != "Prop":
            _fail("expected_proposition", expr.value["span"])
        return expr.value

    def expression(self, minimum, depth, allow_quantifier=False):
        self.check_depth(depth)
        if allow_quantifier and self.peek().kind in ("FORALL", "EXISTS"):
            # A quantifier consumes the entire current formula, not just a term.
            return self.quantifier(depth)
        left = self.prefix(depth)
        nonassoc = set()
        while self.peek().kind in BINARY:
            t = self.peek()
            precedence, associativity, kind = BINARY[t.kind]
            if precedence < minimum:
                break
            if precedence in nonassoc:
                _fail("nonassociative_chain", _token_span(t))
            if associativity == "non":
                nonassoc.add(precedence)
            self.take()
            right = self.expression(precedence if associativity == "right" else precedence+1,
                                    depth+1)
            left = self.binary(t, kind, left, right)
        return left

    def quantifier(self, depth):
        q = self.take()
        name = self.take("IDENT")
        sep = self.take()
        if sep.kind not in ("COLON", "IN"):
            _fail("expected_binder_type", _token_span(sep))
        typ = self.take("TYPE")
        if sep.kind == "IN" and typ.value not in NUMERIC:
            _fail("unsupported_membership_type", _token_span(typ))
        self.take("COMMA")
        binding = self.state.binding(name.value, typ.value, [name.start, typ.end])
        old = self.env
        self.env = {**old, name.value: binding}
        try:
            body = self.expression(1, depth+1, True)
        finally:
            self.env = old
        if body.value["type"] != "Prop":
            _fail("expected_proposition", body.value["span"])
        if sep.kind == "IN":
            self.state.rules.append({"rule": "IN_WHOLE_NUMERIC_TYPE", "span": _token_span(sep)})
        return self.state.node(q.kind.lower(), "Prop", [q.start, body.value["span"][1]],
                               (body,), binding=binding, body=body.value)

    def prefix(self, depth):
        self.check_depth(depth)
        t = self.take()
        if t.kind == "IDENT":
            binding = self.env.get(t.value)
            if binding is None:
                _fail("unbound_variable", _token_span(t))
            return self.state.node("var", binding["type"], _token_span(t),
                                   binding_id=binding["id"])
        if t.kind in ("TRUE", "FALSE"):
            return self.state.node("truth" if t.kind == "TRUE" else "falsehood",
                                   "Prop", _token_span(t))
        if t.kind in ("NOT", "MINUS"):
            arg = self.prefix(depth+1)
            typ = arg.value["type"]
            if typ not in ({"Prop"} if t.kind == "NOT" else {"Int", "Real"}):
                _fail("type_mismatch", _token_span(t))
            return self.state.node("not" if t.kind == "NOT" else "neg", typ,
                                   [t.start, arg.value["span"][1]], (arg,), arg=arg.value)
        if t.kind == "LPAREN":
            if self.peek().kind == "DIGITS":
                digits = self.take()
                self.take("COLON")
                typ = self.take("TYPE")
                end = self.take("RPAREN")
                if typ.value not in NUMERIC:
                    _fail("type_mismatch", _token_span(typ))
                return self.state.node("numeral", typ.value, [t.start, end.end],
                                       digits=digits.value)
            inner = self.expression(1, depth+1, True)
            end = self.take("RPAREN")
            # Parentheses are syntax, not an extra AST operation.
            inner.value["span"] = [t.start, end.end]
            return inner
        if t.kind == "DIGITS":
            _fail("explicit_numeral_type_required", _token_span(t))
        _fail("expected_atom", _token_span(t))

    def binary(self, token, kind, left, right):
        l, r = left.value, right.value
        typ = l["type"]
        if typ != r["type"]:
            _fail("type_mismatch", _token_span(token))
        if kind in ("and", "or", "implies", "iff"):
            allowed, result_type = {"Prop"}, "Prop"
        elif kind == "eq":
            allowed, result_type = ast.TYPES, "Prop"
        elif kind in ("lt", "le"):
            allowed, result_type = NUMERIC, "Prop"
        else:
            allowed = {"Int", "Real"} if kind == "sub" else NUMERIC
            result_type = typ
        if typ not in allowed:
            _fail("type_mismatch", _token_span(token))
        span = [l["span"][0], r["span"][1]]
        if token.kind in ("GT", "GE"):
            self.state.rules.append({"rule": token.kind + "_REVERSE", "span": _token_span(token)})
            l, r = r, l
        return self.state.node(kind, result_type, span, (left, right), left=l, right=r)


def _parse(source, segments, formula_only):
    flags = {"grammar_version": lex.GRAMMAR_VERSION, "candidate_status": "not_generated",
             "proof_status": "not_run", "statement_status": "unreviewed",
             "certificate": False, "external_cost_minor_units": 0,
             "external_transfer_allowed": False, "lean_code": None, "ast": None}
    try:
        digest = lex.source_digest(source)
        tokens = lex.tokenize(source)
        if formula_only:
            segments = [{"role": "conclusion", "span": [0, len(source)]}]
        parts = _partition(source, tokens, segments)
        state = _State()
        env, params, assumptions = {}, [], []
        conclusion = None
        for role, part in parts:
            parser = _Parser(part, state, env)
            if role == "parameter":
                binding = parser.declaration()
                params.append(binding)
                env[binding["name"]] = binding
            elif role == "assumption":
                assumptions.append(parser.formula())
            else:
                conclusion = parser.formula()
        document = {"schema_version": ast.SCHEMA_VERSION, "source_sha256": digest,
                    "parameters": params, "assumptions": assumptions, "conclusion": conclusion}
        raw = json.dumps(document, ensure_ascii=True, separators=(",", ":")).encode("ascii")
        checked = ast.validate_ast(source, raw)
        if checked["status"] != "validated_ast":
            return {**flags, "status": checked["status"], "error": checked["error"],
                    "path": checked["path"]}
        return {**flags, "status": "parsed_formula" if formula_only else "parsed_pilot_statement",
                "coverage": "controlled_pilot_only", "source_sha256": digest,
                "ast_sha256": checked["ast_sha256"], "ast": checked["ast"],
                "node_count": checked["node_count"], "binding_count": checked["binding_count"],
                "trace": {"segments": [{"role": s["role"], "span": list(s["span"])} for s in segments],
                          "tokens": [{"kind": t.kind, "value": t.value, "span": _token_span(t)}
                                     for t in tokens], "rules": state.rules}}
    except lex.LexError as exc:
        return {**flags, "status": exc.status, "error": exc.code, "span": [exc.start, exc.end]}
    except ParseError as exc:
        return {**flags, "status": exc.status, "error": exc.code, "span": exc.span}
    except RecursionError:
        return {**flags, "status": "invalid_input", "error": "recursion_limit"}


def parse_formula(source: str) -> dict:
    """Closed formula only, no implicit parameters."""
    return _parse(source, None, True)


def parse_pilot_statement(source: str, segments: list) -> dict:
    """Explicit caller-selected segment roles; not an indexed theorem adapter."""
    return _parse(source, segments, False)
