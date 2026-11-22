"""Fail-closed Lean pilot CI: require a kernel run and inspect #print axioms output.

This script does NOT certify semantic equivalence to the original LaTeX.
It audits only theorems in the explicitly registered Lean source files.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

ALLOWED_AXIOMS = frozenset({"propext", "Classical.choice", "Quot.sound"})
IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*\Z")
DECLARATION = re.compile(
    r"(?m)^[ \t]*(?:(?:private|protected|noncomputable)\s+)*"
    r"(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_'.]*)\b"
)
AXIOM_REPORT = re.compile(
    r"""['"]?(?P<name>[A-Za-z_][A-Za-z0-9_'.]*)['"]?\s+"""
    r"""(?:(?:depends\s+on\s+axioms:\s*\[(?P<axioms>[^\]]*)\])|"""
    r"""(?:does\s+not\s+depend\s+on\s+any\s+axioms))""",
    re.IGNORECASE,
)
MAX_LOG_BYTES = 1_000_000


def registered_files(manifest: Path, lean_root: Path) -> dict[str, list[str]]:
    raw = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("items"), list) or not raw["items"]:
        raise ValueError("No registered formalizations")
    root = (lean_root / "src").resolve()
    output: dict[str, list[str]] = {}
    for item in raw["items"]:
        if not isinstance(item, dict):
            raise ValueError("Invalid manifest entry")
        rel = item.get("lean_file")
        name = item.get("lean_theorem")
        if not isinstance(rel, str) or not rel.startswith("src/") or not rel.endswith(".lean"):
            raise ValueError("Invalid registered Lean path")
        if not isinstance(name, str) or not IDENTIFIER.fullmatch(name):
            raise ValueError("Invalid registered Lean theorem")
        resolved = (lean_root / rel).resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            raise ValueError("Untrusted or missing Lean file: " + rel)
        output.setdefault(rel, []).append(name)
    return output


def expected_theorems(lean_file: Path, registered: list[str]) -> list[str]:
    code = lean_file.read_text(encoding="utf-8")
    names = DECLARATION.findall(code)
    if not names:
        raise ValueError("No theorems found in " + str(lean_file))
    if len(names) != len(set(names)):
        raise ValueError("Repeated theorem name in " + str(lean_file))
    for name in registered:
        if name not in names:
            raise ValueError("Manifest theorem missing from Lean source: " + name)
    printed = set(re.findall(
        r"(?m)^[ \t]*#print[ \t]+axioms[ \t]+([A-Za-z_][A-Za-z0-9_'.]*)[ \t]*(?:--[^\n]*)?$",
        code,
    ))
    missing = sorted(set(names) - printed)
    if missing:
        raise ValueError("Missing #print axioms checks for: " + ", ".join(missing))
    return names


def inspect_log(log: str, theorems: list[str]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    expected = set(theorems)
    for match in AXIOM_REPORT.finditer(log):
        name = match.group("name")
        if name not in expected:
            continue
        if name in found:
            raise ValueError("Duplicate axiom output for " + name)
        axioms = [part.strip() for part in (match.group("axioms") or "").split(",")
                  if part.strip()]
        disallowed = sorted(set(axioms) - ALLOWED_AXIOMS)
        if disallowed:
            raise ValueError(name + " depends on forbidden axioms: " + ", ".join(disallowed))
        found[name] = axioms
    missing = sorted(expected - set(found))
    if missing:
        raise ValueError("No actual #print axioms output for: " + ", ".join(missing))
    return found


def audit(manifest: Path, lean_root: Path, logs_dir: Path) -> dict[str, Any]:
    registered = registered_files(manifest, lean_root)
    reports: list[dict[str, Any]] = []
    for rel, targets in sorted(registered.items()):
        names = expected_theorems(lean_root / rel, targets)
        log_file = logs_dir / (rel.replace("/", "_") + ".log")
        if not log_file.is_file() or log_file.stat().st_size > MAX_LOG_BYTES:
            raise ValueError("Missing or oversized real Lean log: " + str(log_file))
        parsed = inspect_log(log_file.read_text(encoding="utf-8"), names)
        reports.append({"file": rel, "theorems": parsed, "compiled": True,
                        "semantics_approved": False, "certificate": False})
    return {
        "schema_version": 1,
        "files_checked": len(reports),
        "theorems_checked": sum(len(report["theorems"]) for report in reports),
        "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "kernel_compilation_and_axiom_report": "passed",
        "latex_semantics_status": "not_certified",
        "certificate": False,
        "files": reports,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--lean-root", type=Path, required=True)
    p.add_argument("--logs-dir", type=Path)
    p.add_argument("--report", type=Path)
    p.add_argument("--list-files", action="store_true")
    args = p.parse_args(argv)
    try:
        entries = registered_files(args.manifest, args.lean_root)
        if args.list_files:
            for rel in sorted(entries):
                expected_theorems(args.lean_root / rel, entries[rel])
                print(rel)
            return 0
        if args.logs_dir is None:
            raise ValueError("--logs-dir is required for auditing")
        result = audit(args.manifest, args.lean_root, args.logs_dir)
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                                   encoding="utf-8")
        print(json.dumps({"files": result["files_checked"],
                          "theorems": result["theorems_checked"],
                          "axiom_check": "passed", "semantic_certificate": False}))
        return 0
    except (ValueError, OSError, UnicodeError, TypeError, json.JSONDecodeError) as exc:
        print("Lean CI audit failed: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
