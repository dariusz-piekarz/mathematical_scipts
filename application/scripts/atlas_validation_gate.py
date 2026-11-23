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

SHA = re.compile(r"[0-9a-f]{40}\Z")
EXPECTED_PASSES = ("1", "2", "3")
REQUIRED_L11_TEST = "test_real_olean_growth_during_read_fails_closed"


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


def validate_unit_report(document: dict, sha: str, pass_id: str) -> list[str]:
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
    if not isinstance(document.get("executed"), int) or document["executed"] < 1:
        problems.append("empty or malformed test suite")
    for key in ("failures", "errors", "unexpected_successes", "unreviewed_skips"):
        if type(document.get(key)) is not int or document[key] != 0:
            problems.append(f"nonzero or missing {key}")
    outcomes = document.get("outcomes")
    if not isinstance(outcomes, list) or not outcomes:
        return problems + ["missing per-test outcomes"]
    skipped = []
    observed = set()
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
            if not entry.get("reason") or entry.get("classification") in (None, "unreviewed"):
                problems.append("unreviewed or unreasoned skip")
        if name.endswith(REQUIRED_L11_TEST) and status == "passed":
            observed.add(name)
    if not observed:
        problems.append("mandatory L1.1 real-file growth regression not passed")
    if len(skipped) != document.get("skipped"):
        problems.append("skip count does not match named outcomes")
    if document.get("outcome_count") != len(outcomes):
        problems.append("outcome count mismatch")
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
            issues = validate_unit_report(doc, sha, pass_id)
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
