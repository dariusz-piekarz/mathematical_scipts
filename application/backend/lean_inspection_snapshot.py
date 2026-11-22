"""Versioned, content-addressed evidence for *completed* Lean inspections.

The snapshot is reproducible metadata of one result from actual Lean MetaM,
not a proof certificate, stored execution record, or semantic equivalence check.
Never call this on blocked/failed/timeout results.
"""
from __future__ import annotations

import hashlib
import json
import re

SCHEMA_VERSION = 1
METHOD = "Lean.ConstantInfo.getUsedConstantsAsSet"
DIGEST = re.compile(r"[0-9a-f]{64}\Z")
NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*\Z")
IDENTIFIER = re.compile(r"[A-Za-z0-9_-]{1,100}\Z")
DIGEST_FIELDS = (
    "source_document_sha256",
    "source_binding_sha256",
    "lean_sha256",
    "project_sources_sha256",
    "external_packages_sha256",
    "compiled_artifacts_sha256",
    "executable_toolchain_sha256",
    "toolchain_sha256",
)
FINGERPRINT_FIELDS = DIGEST_FIELDS + ("declared_toolchain",)
MAX_THEOREMS = 16
MAX_CONSTANTS = 160


def _validated_references(value: object, names: list[str]) -> dict[str, list[str]]:
    if not isinstance(value, dict) or set(value) != set(names):
        raise ValueError("Incomplete inspected declaration set")
    result: dict[str, list[str]] = {}
    for name in sorted(names):
        refs = value[name]
        if (not isinstance(refs, list) or len(refs) > MAX_CONSTANTS
                or any(not isinstance(ref, str) or not NAME.fullmatch(ref)
                       for ref in refs)
                or len(refs) != len(set(refs))):
            raise ValueError("Invalid inspected constant references")
        result[name] = sorted(refs)
    return result


def describe(identifier: str, names: list[str], *,
             classified: bool, fingerprint: dict[str, str],
             constants: dict[str, list[str]],
             type_constants: dict[str, list[str]] | None = None,
             value_constants: dict[str, list[str]] | None = None) -> dict:
    """Compute a canonical snapshot ID, refusing incomplete provenance.

    Names, environment, output and inspection mode all contribute to the hash.
    Order of compiler log events does not: references are normalized.
    """
    if (not isinstance(identifier, str) or not IDENTIFIER.fullmatch(identifier)
            or not isinstance(names, list)
            or not 1 <= len(names) <= MAX_THEOREMS
            or any(not isinstance(name, str) or not NAME.fullmatch(name)
                   for name in names)
            or len(set(names)) != len(names)
            or type(classified) is not bool):
        raise ValueError("Invalid inspection identity")
    if (not isinstance(fingerprint, dict)
            or any(not isinstance(fingerprint.get(field), str)
                   or not DIGEST.fullmatch(fingerprint[field])
                   for field in DIGEST_FIELDS)
            or not isinstance(fingerprint.get("declared_toolchain"), str)
            or len(fingerprint["declared_toolchain"]) > 160):
        raise ValueError("Incomplete inspection environment fingerprint")
    provenance = {key: fingerprint[key] for key in FINGERPRINT_FIELDS}
    total = _validated_references(constants, names)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "extraction_method": METHOD,
        "formalization_id": identifier,
        "declarations": sorted(names),
        "classified": classified,
        "fingerprint": provenance,
        "constants": total,
    }
    if classified:
        types = _validated_references(type_constants, names)
        values = _validated_references(value_constants, names)
        if any(set(total[name]) != set(types[name]) | set(values[name])
               for name in names):
            raise ValueError("Classified references disagree with total")
        payload["type_constants"] = types
        payload["value_constants"] = values
    elif type_constants is not None or value_constants is not None:
        raise ValueError("Unclassified inspection cannot have classified evidence")
    digest = hashlib.sha256(json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()
    return {
        "inspection_schema_version": SCHEMA_VERSION,
        "inspection_snapshot_sha256": digest,
        "inspection_provenance": provenance,
    }
