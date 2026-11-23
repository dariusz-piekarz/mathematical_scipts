"""Named unittest outcomes for the Atlas immutable-revision CI gate.

This reports *actual* skips; a skip is never silently converted to success.
The classifying allowlist is intentionally narrow and matched to test IDs
and exact skip reasons from the existing platform contracts.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import unittest

# Suite-specific skips have to be covered by the separate native/pinned jobs.
# Unknown test IDs or reasons are deliberately classified as 'unreviewed'.
EXPECTED_SKIPS = (
    ("tests.test_lean_windows_job.", "Native Windows Job Objects test", "windows_native"),
    ("tests.test_lean_run_lock.", "Native Windows file-sharing contract", "windows_native"),
    ("tests.test_lean_run_lock.", "Native Windows junction test", "windows_native"),
    ("tests.test_lean_run_lock.", "Windows cannot rename an open CRT lock file", "posix_native"),
    ("tests.test_lean_run_lock.", "Requires POSIX directory symlinks", "posix_native"),
    ("tests.test_lean_run_lock.", "POSIX O_NOFOLLOW requirement", "posix_native"),
    ("tests.test_lean_introspection_real.", "Lake/Mathlib unavailable; no real Lean execution", "pinned_lean"),
    ("tests.test_lean_introspection_core_real.", "Lean unavailable; no compiler execution", "pinned_lean"),
    ("tests.test_lean_cgroup.", "No delegated memory controller on this host", "host_cgroup"),
    ("tests.test_lean_cgroup.", "No write access to delegated cgroup v2", "host_cgroup"),
    ("tests.test_lean_cgroup.", "Linux cgroup v2 only", "linux_cgroup"),
    ("tests.test_local_theorem_compilation.", "pdflatex unavailable", "tex_host"),
)


def classify_skip(test_id: str, reason: str) -> str:
    # Discovery without -t returns 'test_module.Class.test'; explicit module
    # imports instead return 'tests.test_module.Class.test'. Both must match.
    normalized = test_id.removeprefix("tests.")
    for prefix, expected_reason, category in EXPECTED_SKIPS:
        if normalized.startswith(prefix.removeprefix("tests.")) and reason == expected_reason:
            return category
    return "unreviewed"


class NamedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.outcomes: list[dict[str, str]] = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.outcomes.append({"id": test.id(), "status": "passed"})

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.outcomes.append({
            "id": test.id(), "status": "skipped", "reason": reason,
            "classification": classify_skip(test.id(), reason),
        })

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.outcomes.append({"id": test.id(), "status": "failed"})

    def addError(self, test, err):
        super().addError(test, err)
        self.outcomes.append({"id": test.id(), "status": "error"})

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        self.outcomes.append({"id": test.id(), "status": "expected_failure"})

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self.outcomes.append({"id": test.id(), "status": "unexpected_success"})


def report(result: NamedResult, candidate_sha: str, *, pass_id: str) -> dict:
    skips = [x for x in result.outcomes if x["status"] == "skipped"]
    unreviewed = [x for x in skips if x["classification"] == "unreviewed"]
    return {
        "schema": 1,
        "candidate_sha": candidate_sha.lower(),
        "validation_pass": pass_id,
        "runner": sys.platform,
        "executed": result.testsRun,
        "outcome_count": len(result.outcomes),
        "failures": len(result.failures),
        "errors": len(result.errors),
        "unexpected_successes": len(result.unexpectedSuccesses),
        "skipped": len(skips),
        "unreviewed_skips": len(unreviewed),
        "outcomes": result.outcomes,
        "success": bool(result.wasSuccessful() and not unreviewed),
        "certificate": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--candidate-sha", required=True)
    parser.add_argument("--pass-id", default="push")
    parser.add_argument("--start", default="tests")
    args = parser.parse_args(argv)
    import re
    if not re.fullmatch(r"[0-9a-fA-F]{40}", args.candidate_sha):
        parser.error("candidate SHA must be a full 40-character Git commit ID")
    suite = unittest.defaultTestLoader.discover(args.start)
    result = unittest.TextTestRunner(verbosity=2, resultclass=NamedResult).run(suite)
    evidence = report(result, args.candidate_sha, pass_id=args.pass_id)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        key: evidence[key] for key in ("candidate_sha", "validation_pass", "executed",
                                      "skipped", "unreviewed_skips", "success", "certificate")
    }
    print("ATLAS_UNITTEST_REPORT " + json.dumps(summary, sort_keys=True))
    for item in evidence["outcomes"]:
        if item["status"] == "skipped":
            print("ATLAS_SKIPPED " + json.dumps(item, ensure_ascii=False, sort_keys=True))
    return 0 if evidence["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
