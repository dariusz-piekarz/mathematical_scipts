"""L1.5.4: bounded lexer for the mathematical pilot, not TeX execution."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re

from backend.lean_ast import MAX_SOURCE_BYTES, MAX_DIGITS

GRAMMAR_VERSION = 1
MAX_TOKENS = 8192
WHITESPACE = " \t\r\n"
COMMANDS = {
    "forall": "FORALL", "exists": "EXISTS", "in": "IN",
    "iff": "IFF", "Leftrightarrow": "IFF",
    "implies": "IMPLIES", "Rightarrow": "IMPLIES", "to": "IMPLIES",
    "rightarrow": "IMPLIES", "lor": "OR", "vee": "OR",
    "land": "AND", "wedge": "AND", "neg": "NOT", "lnot": "NOT",
    "le": "LE", "leq": "LE", "ge": "GE", "geq": "GE",
    "cdot": "MUL", "times": "MUL", "top": "TRUE", "bot": "FALSE",
}
SYMBOLS = {
    "∀": "FORALL", "∃": "EXISTS", "∈": "IN", "↔": "IFF",
    "→": "IMPLIES", "∨": "OR", "∧": "AND", "¬": "NOT",
    "≤": "LE", "≥": "GE", "<": "LT", ">": "GT", "=": "EQ",
    "×": "MUL", "·": "MUL", "+": "PLUS", "-": "MINUS",
    "⊤": "TRUE", "⊥": "FALSE", "(": "LPAREN", ")": "RPAREN",
    ":": "COLON", ",": "COMMA",
}
TYPES = {"Prop": "Prop", "Nat": "Nat", "Int": "Int", "Real": "Real",
         "ℕ": "Nat", "ℤ": "Int", "ℝ": "Real"}
MATHBB = {"{N}": "Nat", "{Z}": "Int", "{R}": "Real"}
GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ",
    "epsilon": "ϵ", "varepsilon": "ε", "theta": "θ", "vartheta": "ϑ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π",
    "rho": "ρ", "sigma": "σ", "tau": "τ", "phi": "ϕ", "varphi": "φ",
    "psi": "ψ", "omega": "ω",
}
GREEK_CHARS = frozenset(GREEK.values())
LETTERS = re.compile(r"[A-Za-z]+")
DECIMAL = re.compile(r"[0-9]+")


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    start: int
    end: int


class LexError(ValueError):
    def __init__(self, code, start, end, status="unsupported"):
        self.code, self.start, self.end, self.status = code, start, end, status
        super().__init__(f"{code}: [{start},{end})")


def source_digest(source: str) -> str:
    if type(source) is not str or not source:
        raise LexError("invalid_source", 0, 0, "invalid_input")
    if len(source) > MAX_SOURCE_BYTES:
        raise LexError("source_byte_limit", 0, 0, "invalid_input")
    try:
        raw = source.encode("utf-8")
    except UnicodeError as exc:
        raise LexError("invalid_source_encoding", 0, 0, "invalid_input") from exc
    if len(raw) > MAX_SOURCE_BYTES:
        raise LexError("source_byte_limit", 0, 0, "invalid_input")
    return hashlib.sha256(raw).hexdigest()


def tokenize(source: str) -> tuple[Token, ...]:
    """Consume entire input or raise; use original code point offsets.

    Limit excludes EOF. IN is a token, not a general membership operator.
    """
    source_digest(source)
    result = []
    i = 0
    while i < len(source):
        start = i
        char = source[i]
        if char in WHITESPACE:
            i += 1
            continue
        if len(result) >= MAX_TOKENS:
            raise LexError("token_limit", start, start+1, "invalid_input")
        if char == "\\":
            match = LETTERS.match(source, i+1)
            if match is None:
                raise LexError("unsupported_control_symbol", start, min(start+2, len(source)))
            command = match.group()
            i = match.end()
            if command == "mathbb":
                suffix = source[i:i+3]
                if suffix not in MATHBB:
                    raise LexError("unsupported_mathbb", start, min(i+3, len(source)))
                i += 3
                kind, value = "TYPE", MATHBB[suffix]
            elif command in COMMANDS:
                kind = value = COMMANDS[command]
            elif command in GREEK:
                kind, value = "IDENT", GREEK[command]
            else:
                raise LexError("unsupported_command", start, i)
        elif char in SYMBOLS:
            i += 1
            kind = value = SYMBOLS[char]
        elif char in TYPES or char in GREEK_CHARS:
            i += 1
            kind, value = ("TYPE", TYPES[char]) if char in TYPES else ("IDENT", char)
        elif (match := LETTERS.match(source, i)) is not None:
            value = match.group()
            i = match.end()
            if value in TYPES:
                kind, value = "TYPE", TYPES[value]
            elif len(value) == 1:
                kind = "IDENT"
            else:
                raise LexError("unsupported_identifier", start, i)
        elif (match := DECIMAL.match(source, i)) is not None:
            value = match.group()
            i = match.end()
            if len(value) > MAX_DIGITS or (len(value) > 1 and value[0] == "0"):
                raise LexError("invalid_numeral", start, i, "invalid_input")
            kind = "DIGITS"
        else:
            raise LexError("unsupported_character", start, start+1)
        result.append(Token(kind, value, start, i))
    result.append(Token("EOF", "", len(source), len(source)))
    return tuple(result)


def lex_formula(source: str) -> dict:
    """Diagnostic envelope: lexical success alone is not a valid formula."""
    flags = {"grammar_version": GRAMMAR_VERSION, "candidate_status": "not_generated",
             "proof_status": "not_run", "statement_status": "unreviewed",
             "certificate": False, "external_cost_minor_units": 0,
             "external_transfer_allowed": False, "lean_code": None, "ast": None}
    try:
        digest = source_digest(source)
        tokens = tokenize(source)
        return {**flags, "status": "tokenized", "source_sha256": digest,
                "tokens": [{"kind": t.kind, "value": t.value,
                            "span": [t.start, t.end]} for t in tokens],
                "coverage": "lexical_only"}
    except LexError as exc:
        return {**flags, "status": exc.status, "error": exc.code,
                "span": [exc.start, exc.end], "tokens": None}
