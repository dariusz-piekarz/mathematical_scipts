"""Fail-closed Atlas 2+1 evidence aggregator.

Three independent full suites are executed against a *single full commit SHA*.
Successful CI is not a mathematical Lean/LaTeX certificate, nor is it an
independent skeptical review. The latter must be explicitly documented.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess

# This module is both imported as `scripts.atlas_validation_gate` from tests
# and executed as `python application/scripts/atlas_validation_gate.py` in CI.
# Direct file execution has no parent `scripts` package on sys.path.
if __package__:
    from .atlas_ci_report import classify_skip
else:
    from atlas_ci_report import classify_skip

SHA = re.compile(r"[0-9a-f]{40}\Z")
EXPECTED_PASSES = ("1", "2", "3")
REQUIRED_L11_TEST = "test_real_olean_growth_during_read_fails_closed"
# Explicit regression identities: never derive this list from discovered tests.
# unittest discover and module invocation use these two exact prefixes.
REQUIRED_L15_TESTS = frozenset((
    "test_lean_concepts.LeanConceptTests.test_scope_disambiguates_syntax_and_propositions",
    "test_lean_concepts.LeanConceptTests.test_context_required_even_for_unique_match",
    "test_lean_concepts.LeanConceptTests.test_no_scope_fallback_or_fuzzy_resolution",
    "test_lean_concepts.LeanConceptTests.test_input_limits",
    "test_lean_concepts.LeanConceptTests.test_pins_and_deterministic_fingerprint",
    "test_lean_concepts.LeanConceptTests.test_registry_integrity",
    "test_lean_concepts.LeanConceptTests.test_results_not_certificates_or_executable_code",
    "test_lean_concepts.LeanConceptTests.test_returned_metadata_cannot_mutate_registry",
    "test_lean_concepts.LeanConceptTests.test_existing_local_syntax_declarations",
    "test_lean_concept_fixture.LeanConceptFixtureTests.test_every_dictionary_declaration_has_exact_fixture_entry",
    "test_lean_concept_fixture.LeanConceptFixtureTests.test_fixture_is_not_executable_browser_input",
    "test_lean_concept_context.LeanConceptContextTests.test_real_indexed_definitions_and_trace",
    "test_lean_concept_context.LeanConceptContextTests.test_stale_source_and_unknown_context",
    "test_lean_concept_context.LeanConceptContextTests.test_wrong_index_owner_or_digest_is_refused",
    "test_lean_concept_context.LeanConceptContextTests.test_duplicate_occurrence_is_refused",
    "test_lean_concept_context.LeanConceptContextTests.test_modified_definition_even_with_updated_digest_is_refused",
    "test_lean_theorem_context.LeanTheoremContextTests.test_real_registered_theorem_context",
    "test_lean_theorem_context.LeanTheoremContextTests.test_missing_consent_stale_digest_and_unsupported_theorem",
    "test_lean_theorem_context.LeanTheoremContextTests.test_registry_approval_cannot_bypass_source_pin",
    "test_lean_theorem_context.LeanTheoremContextTests.test_unreviewed_and_duplicate_mappings_are_refused",
    "test_lean_theorem_context.LeanTheoremContextTests.test_definition_collision_blocks_entire_context",
    "test_lean_theorem_context.LeanTheoremContextTests.test_truncated_theorem_span_cannot_inherit_approval",
    "test_lean_draft_transport.DraftTransportTests.test_rt10_container_healthcheck_disabled_before_start",
))


def require_sha(value: str) -> str:
    if not SHA.fullmatch(value):
        raise ValueError("Expected an exact lowercase 40-character SHA")
    return value


def verify_ancestor(candidate_sha: str, *, branch: str) -> None:
    """Validate SHA via git, never by interpolating an input into a shell."""
    sha = require_sha(candidate_sha)
    subprocess.run(["git", "cat-file", "-e", f"{sha}^{{commit}}"], check=True)
    subprocess.run(["git", "merge-base", "--is-ancestor", sha, f"origin/{branch}"],
                   check=True)


def validate_unit_report(document: dict, sha: str, pass_id: str, *, fragment: str | None = None) -> list[str]:
    problems: list[str] = []
    if document.get("schema") != 1:
        problems.append("invalid unit report schema")
    if document.get("candidate_sha") != sha:
        problems.append("unit report SHA does not match candidate")
    if document.get("validation_pass") != pass_id:
        problems.append("unit report pass ID does not match")
    if document.get("certificate") is not False:
        problems.append("unit report must declare certificate=false")
    if document.get("success") is not True:
        problems.append("unit tests did not succeed")
    if type(document.get("executed")) is not int or document["executed"] < 1:
        problems.append("empty or malformed test suite")
    for key in ("failures", "errors", "unexpected_successes", "unreviewed_skips"):
        if type(document.get(key)) is not int or document[key] != 0:
            problems.append(f"nonzero or missing {key}")
    outcomes = document.get("outcomes")
    if not isinstance(outcomes, list) or not outcomes:
        return problems + ["missing per-test outcomes"]
    skipped = []
    observed = set()
    observed_l15 = set()
    ids = set()
    for entry in outcomes:
        if not isinstance(entry, dict):
            problems.append("non-object test result")
            continue
        name, status = entry.get("id"), entry.get("status")
        if not isinstance(name, str) or not name:
            problems.append("unnamed test result")
            continue
        if name in ids:
            problems.append("duplicate test identity")
        ids.add(name)
        if status not in ("passed", "skipped", "expected_failure"):
            problems.append("failed or unrecognized test outcome")
        if status == "skipped":
            skipped.append(entry)
            reason = entry.get("reason")
            if not isinstance(reason, str) or not reason.strip():
                problems.append("unreviewed or unreasoned skip")
            else:
                # The report's category is untrusted. Recompute it from the
                # exact test identity and skip reason using the allowlist.
                expected = classify_skip(name, reason)
                if expected == "unreviewed" or entry.get("classification") != expected:
                    problems.append("skip classification does not match reviewed allowlist")
        if status == "passed":
            canonical = name.removeprefix("tests.")
            if canonical in REQUIRED_L15_TESTS:
                if canonical in observed_l15:
                    problems.append("duplicate canonical L1.5 regression identity")
                observed_l15.add(canonical)
        if name.endswith(REQUIRED_L11_TEST) and status == "passed":
            observed.add(name)
    if not observed:
        problems.append("mandatory L1.1 real-file growth regression not passed")
    if fragment == "L1.5":
        for missing in sorted(REQUIRED_L15_TESTS - observed_l15):
            problems.append("mandatory L1.5 regression not passed: " + missing)
    if type(document.get("skipped")) is not int or len(skipped) != document["skipped"]:
        problems.append("skip count does not match named outcomes")
    if type(document.get("outcome_count")) is not int or document["outcome_count"] != len(outcomes):
        problems.append("outcome count mismatch")
    if type(document.get("executed")) is int and document["executed"] != len(outcomes):
        problems.append("executed test count does not match per-test outcomes")
    return problems


def evaluate(
    candidate_sha: str, fragment: str, report_root: Path,
    *, application: str, native: str, lean: str, skeptic: str,
    review: dict | None = None,
) -> dict:
    sha = require_sha(candidate_sha)
    problems: list[str] = []
    passes = []
    for pass_id in EXPECTED_PASSES:
        path = report_root / f"atlas-unittest-{pass_id}" / "report.json"
        if not path.is_file():
            problems.append(f"missing unit evidence for pass {pass_id}")
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(doc, dict):
                raise ValueError("expected an object")
            issues = validate_unit_report(doc, sha, pass_id, fragment=fragment)
            problems.extend(f"pass {pass_id}: {issue}" for issue in issues)
            passes.append({
                "pass": pass_id, "tests": doc.get("executed"),
                "skips": doc.get("skipped"),
                "unreviewed_skips": doc.get("unreviewed_skips"),
                "passed": not issues,
            })
        except (OSError, ValueError) as err:
            problems.append(f"invalid unit evidence for pass {pass_id}: {err}")
    statuses = {
        "application": application, "linux_windows": native,
        "pinned_lean_mathlib": lean, "skeptical_regression_suite": skeptic,
    }
    for key, result in statuses.items():
        if result != "success":
            problems.append(f"{key} workflow result is {result!r}, not success")
    review_state = "pending"
    if review is not None:
        if not isinstance(review, dict):
            problems.append("skeptical review must be a JSON object")
        elif (review.get("candidate_sha") == sha
                and review.get("fragment") == fragment
                and review.get("decision") == "approved"
                and isinstance(review.get("reviewer"), str)
                and len(review["reviewer"].strip()) > 2
                and isinstance(review.get("checks"), list)
                and len(review["checks"]) >= 2
                and all(isinstance(c, str) and c.strip() for c in review["checks"])
                and review.get("critical_findings") == []
                and review.get("independent") is True):
            # This JSON has no cryptographic signature, GitHub-protected
            # reviewer identity or independently verified approval channel.
            # It is useful as a review *claim*, never as proof of independence.
            review_state = "documented_unverified"
        else:
            problems.append("skeptical review record invalid or not approved")
    # No in-repository JSON may unilaterally promote a fragment to stable.
    # Stability requires an independently authenticated reviewer decision
    # recorded by a trusted, protected approval process outside this gate.
    status = "blocked" if problems else "stabilizing"
    return {
        "schema": 1,
        "candidate_sha": sha,
        "fragment": fragment,
        "status": status,
        "passes": passes,
        "workflow_results": statuses,
        "skeptical_review": review_state,
        "problems": problems,
        "certificate": False,
        "policy": ("2+1 on immutable SHA; unverified review JSON cannot "
                   "grant stable; requires separately authenticated independent "
                   "review and manual advancement; no Lean/LaTeX certificate"),
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    check = sub.add_parser("verify-sha")
    check.add_argument("--sha", required=True)
    check.add_argument("--branch", default="biblioteka-matematyczna-iteracja-6")
    gate = sub.add_parser("gate")
    gate.add_argument("--sha", required=True)
    gate.add_argument("--fragment", required=True)
    gate.add_argument("--reports", required=True, type=Path)
    for field in ("application", "native", "lean", "skeptic"):
        gate.add_argument(f"--{field}", required=True)
    gate.add_argument("--review", type=Path)
    gate.add_argument("--output", type=Path, required=True)
    args = p.parse_args(argv)
    if args.command == "verify-sha":
        verify_ancestor(args.sha, branch=args.branch)
        print(args.sha)
        return 0
    # Review lives in the *control* revision, not in the frozen source under test.
    # Absence is legitimate and forces 'stabilizing', never 'stable'.
    review = (json.loads(args.review.read_text(encoding="utf-8"))
              if args.review is not None and args.review.is_file() else None)
    value = evaluate(args.sha, args.fragment, args.reports,
                     application=args.application, native=args.native,
                     lean=args.lean, skeptic=args.skeptic, review=review)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("ATLAS_STABILIZATION " + json.dumps(value, ensure_ascii=False, sort_keys=True))
    return 1 if value["status"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
