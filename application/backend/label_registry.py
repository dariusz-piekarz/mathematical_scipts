"""Deterministic label ownership without rewriting canonical LaTeX.

A source occurrence is identified by (document_id, original label).  The
optional concept_id denotes mathematical identity only after manual review;
identical label strings alone never establish semantic equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

VOLUMES = {"P1": "I", "P2": "II", "P3": "III", "P4": "IV"}
VOLUME_PREFIXES = {f"{v}-": k for k, v in VOLUMES.items()}


@dataclass(frozen=True)
class Owner:
    document_id: str
    label: str
    entity_id: str | None = None

    @property
    def occurrence_id(self) -> str:
        return f"{self.document_id}::{self.label}"


@dataclass(frozen=True)
class Decision:
    status: str
    owner: Owner | None = None
    reason: str = ""


def family(document_id: str) -> str:
    """Stable source-script namespace, independent of translated domain names."""
    return document_id.split("-", 1)[0]


def resolve(
    source_document: str,
    target_label: str,
    owners: Sequence[Owner],
    *,
    aliases: Mapping[tuple[str, str], tuple[str, str]] | None = None,
) -> Decision:
    """Prefer local, same-script, then unique global ownership.

    Prefixes I-/II-/III-/IV- are interpreted ONLY for P1..P4 sources.
    Never choose arbitrarily between multiple owners; a curated alias
    must contain the original source-document and original target label.
    """
    pool = list(owners)
    alias = (aliases or {}).get((source_document, target_label))
    if alias is not None:
        target_doc, target_name = alias
        hits = [o for o in pool if o.document_id == target_doc and o.label == target_name]
        if len(hits) == 1:
            return Decision("alias_resolved", hits[0], "curated_alias")
        return Decision("missing", None, "stale_alias")

    scope = family(source_document)
    if scope in VOLUMES:
        for prefix, destination in VOLUME_PREFIXES.items():
            if target_label.startswith(prefix):
                label = target_label[len(prefix):]
                hits = [o for o in pool if family(o.document_id) == destination and o.label == label]
                if len(hits) == 1:
                    return Decision("external_resolved", hits[0], "xr_hyper_prefix")
                return Decision("ambiguous" if len(hits) > 1 else "missing", None,
                                "external_prefix_ambiguous" if len(hits) > 1 else "external_prefix_missing")

    hits = [o for o in pool if o.label == target_label]
    local = [o for o in hits if o.document_id == source_document]
    if len(local) == 1:
        return Decision("resolved", local[0], "same_document")
    if len(local) > 1:
        return Decision("ambiguous", None, "duplicate_local_label")
    same_script = [o for o in hits if family(o.document_id) == scope]
    if len(same_script) == 1:
        return Decision("resolved", same_script[0], "same_script")
    if len(same_script) > 1:
        return Decision("ambiguous", None, "multiple_same_script_owners")
    if len(hits) == 1:
        return Decision("resolved", hits[0], "unique_global_owner")
    if hits:
        return Decision("ambiguous", None, "multiple_foreign_script_owners")
    return Decision("missing", None, "no_indexed_label_owner")
