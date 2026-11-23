"""Paired microbenchmark: legacy and optimized .olean lexical path conversion.

This tool is diagnostic only. It reuses a single collected name population,
does not read .olean contents, and does NOT replace fingerprint/Lean verification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys
import time

APPLICATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION))

from backend import lean_environment
from scripts.benchmark_lean_fingerprint import _registered_inputs


def collect_names(lean_root: Path) -> list[tuple[str, Path, Path, tuple[str, ...]]]:
    """Collect trusted lexical .olean filenames once, without following symlinks."""
    _registered_inputs(lean_root)
    packages = lean_root / ".lake" / "packages"
    if packages.is_symlink():
        raise ValueError("Symlinked Lake packages root")
    roots = [("project", lean_root / ".lake" / "build" / "lib" / "lean")]
    if packages.exists():
        if not packages.is_dir():
            raise ValueError("Lake packages root is not a directory")
        for package in sorted(packages.iterdir(), key=lambda p: p.name):
            if package.is_symlink() or not package.is_dir():
                raise ValueError("Invalid Lake package directory")
            roots.append((f"package/{package.name}",
                          package / ".lake" / "build" / "lib" / "lean"))
    if len(roots) > lean_environment.MAX_PACKAGES + 1:
        raise ValueError("Too many Lake artifact roots")

    groups: list[tuple[str, Path, Path, tuple[str, ...]]] = []
    count = 0
    for label, root in roots:
        if root.is_symlink():
            raise ValueError("Symlinked Lake artifact root")
        if not root.exists():
            continue
        if not root.is_dir():
            raise ValueError("Lake artifact root is not a directory")
        for directory, dirs, names in os.walk(root, followlinks=False):
            base = Path(directory)
            if any((base / name).is_symlink() for name in dirs):
                raise ValueError("Symlinked Lake artifact directory")
            selected = tuple(
                name for name in names
                if name.endswith(".olean") and name != ".olean"
            )
            if not selected:
                continue
            for name in selected:
                if (base / name).is_symlink():
                    raise ValueError("Symlinked Lake .olean artifact")
            count += len(selected)
            if count > lean_environment.MAX_OLEAN_FILES:
                raise ValueError("Too many Lake .olean artifacts")
            groups.append((label, root, base, selected))
    if not count:
        raise ValueError("No .olean artifacts to benchmark")
    return groups


def convert_names(groups: list[tuple[str, Path, Path, tuple[str, ...]]],
                  *, optimized: bool) -> list[tuple[str, str]]:
    """Run only the lexical name conversion; never touch file contents."""
    result: list[tuple[str, str]] = []
    for label, root, base, names in groups:
        if optimized:
            directory = base.relative_to(root).as_posix()
            for name in names:
                result.append((label, name if directory == "."
                               else f"{directory}/{name}"))
        else:
            for name in names:
                result.append((label, (base / name).relative_to(root).as_posix()))
    return result


def benchmark(lean_root: Path, *, samples: int = 5,
              expected_candidates: int | None = None) -> dict:
    """Run both equivalent conversions in alternating order on one CPU."""
    if type(samples) is not int or not 2 <= samples <= 12:
        raise ValueError("samples must be an integer between 2 and 12")
    if expected_candidates is not None and (
            type(expected_candidates) is not int or expected_candidates < 0):
        raise ValueError("Invalid expected candidate count")
    groups = collect_names(lean_root)
    candidates = sum(len(names) for _, _, _, names in groups)
    if expected_candidates is not None and candidates != expected_candidates:
        raise RuntimeError("Lean artifact name population changed since fingerprint benchmark")
    baseline = convert_names(groups, optimized=False)
    if convert_names(groups, optimized=True) != baseline:
        raise RuntimeError("Optimized and legacy .olean lexical names disagree")
    seconds = {"legacy": [], "optimized": []}
    for run in range(samples):
        for mode in (("legacy", "optimized") if run % 2 == 0
                     else ("optimized", "legacy")):
            started = time.perf_counter()
            actual = convert_names(groups, optimized=(mode == "optimized"))
            seconds[mode].append(time.perf_counter() - started)
            if actual != baseline:
                raise RuntimeError("Lean .olean relative names changed during timing")
    digest = hashlib.sha256(
        json.dumps(sorted(baseline), ensure_ascii=False,
                   separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "purpose": "paired_lexical_path_microbenchmark_not_formalization_result",
        "certificate": False,
        "samples_per_method": samples,
        "olean_candidates": candidates,
        "populated_directories": len(groups),
        "legacy_relative_to_calls_per_sample": candidates,
        "optimized_relative_to_calls_per_sample": len(groups),
        "names_sha256": digest,
        "samples_seconds": {
            method: [round(v, 6) for v in values]
            for method, values in seconds.items()
        },
        "median_seconds": {
            method: round(statistics.median(values), 6)
            for method, values in seconds.items()
        },
        "method": (
            "Same pre-collected names and host, alternating timing order; "
            "only lexical relative path construction timed; no digest, "
            "filesystem read or security check bypassed in production"
        ),
        "scope": (
            "Microbenchmark, not a paired full fingerprint run; "
            "do not infer full fingerprint speedup from these times"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean-root", type=Path, default=APPLICATION / "lean")
    parser.add_argument("--samples", type=int, default=5)
    parser.add_argument("--compare-with", type=Path,
                        help="Existing full fingerprint report, for name count consistency")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    expected: int | None = None
    if args.compare_with is not None:
        if args.compare_with.stat().st_size > 2 * 1024 * 1024:
            raise ValueError("Unexpectedly large fingerprint evidence")
        previous = json.loads(args.compare_with.read_text(encoding="utf-8"))
        counts = previous["olean_io_samples"]
        if (not counts or previous.get("certificate") is not False
                or any(item != counts[0] for item in counts)):
            raise ValueError("Invalid or changing fingerprint scan population")
        expected = counts[0]["olean_name_candidates"]
    report = benchmark(
        args.lean_root, samples=args.samples, expected_candidates=expected)
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
