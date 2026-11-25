"""CI-only Mathlib source-closure evidence, not an offline image attestation.

Lake's generated manifest is compared with the reviewed source lock and the
manifest tracked at the pinned Mathlib commit. No dependency is executed here.
Ignored build/cache bytes are NOT authenticated by this source-only check.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib

from backend import lean_environment as environment

PIN = "2df2f0150c275ad53cb3c90f7c98ec15a56a1a67"
TOOLCHAIN = "leanprover/lean4:v4.26.0"
MATHLIB_URL = "https://github.com/leanprover-community/mathlib4"
UPSTREAM = MATHLIB_URL + "/blob/" + PIN + "/lake-manifest.json"
MAX_JSON_BYTES = 256 * 1024
NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,63}\Z")
REV = re.compile(r"[0-9a-f]{40}\Z")
URL = re.compile(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def read_json(path: Path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("Expected regular source manifest")
    with path.open("rb") as handle:
        raw = handle.read(MAX_JSON_BYTES + 1)
    if len(raw) > MAX_JSON_BYTES:
        raise ValueError("Source manifest exceeds byte budget")
    return json.loads(raw, object_pairs_hook=unique_object)


def package_map(records, *, lake: bool) -> dict:
    if type(records) is not list or not 1 <= len(records) <= environment.MAX_PACKAGES:
        raise ValueError("Invalid source package count")
    result = {}
    for row in records:
        if type(row) is not dict:
            raise ValueError("Invalid package record")
        name, url, rev = (row.get(k) for k in ("name", "url", "rev"))
        if (type(name) is not str or not NAME.fullmatch(name)
                or type(url) is not str or not URL.fullmatch(url)
                or type(rev) is not str or not REV.fullmatch(rev)
                or name in result):
            raise ValueError("Invalid or duplicate package identity")
        if lake:
            if row.get("type") != "git" or "subDir" not in row or row["subDir"] is not None:
                raise ValueError("Expected whole Git package")
        elif set(row) != {"name", "url", "rev"}:
            raise ValueError("Unexpected lock record fields")
        result[name] = {"url": url, "rev": rev}
    return result


def manifest_map(manifest, *, name: str) -> dict:
    if (type(manifest) is not dict or manifest.get("name") != name
            or manifest.get("version") != "1.1.0"
            or manifest.get("packagesDir") != ".lake/packages"
            or manifest.get("lakeDir") != ".lake"):
        raise ValueError("Unexpected Lake manifest identity")
    return package_map(manifest.get("packages"), lake=True)


def validate_lock(lock) -> dict:
    if (type(lock) is not dict
            or set(lock) != {"schema", "lean_toolchain", "mathlib_manifest_source", "packages"}
            or type(lock["schema"]) is not int or lock["schema"] != 1
            or lock["lean_toolchain"] != TOOLCHAIN or lock["mathlib_manifest_source"] != UPSTREAM):
        raise ValueError("Unexpected source lock identity")
    packages = package_map(lock["packages"], lake=False)
    if packages.get("mathlib") != {"url": MATHLIB_URL, "rev": PIN} or len(packages) != 9:
        raise ValueError("Incorrect pinned Mathlib closure")
    return packages


def inspect_sources(root: Path, *, expected_sha: str) -> dict:
    if not REV.fullmatch(expected_sha) or environment._git(root, "rev-parse", "HEAD") != expected_sha:
        raise ValueError("Checkout identity mismatch")
    if (root / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise ValueError("Toolchain pin mismatch")
    with (root / "lakefile.toml").open("rb") as handle:
        config = tomllib.load(handle)
    if config.get("name") != "AtlasFormalization" or config.get("require") != [
            {"name": "mathlib", "scope": "leanprover-community", "rev": PIN}]:
        raise ValueError("Project dependency pin mismatch")
    lock = read_json(root / "mathlib-source-lock.json")
    expected = validate_lock(lock)
    actual = manifest_map(read_json(root / "lake-manifest.json"), name="AtlasFormalization")
    if actual != expected:
        raise ValueError("Generated Lake manifest differs from pinned closure")
    lake = root / ".lake"
    packages = lake / "packages"
    if lake.is_symlink() or packages.is_symlink() or not packages.is_dir():
        raise ValueError("Invalid installed package root")
    if {p.name for p in packages.iterdir()} != set(expected):
        raise ValueError("Installed dependency set differs from pinned closure")
    # Reuse the existing clean-checkout and exact Git root check.
    clean_digest = environment.external_packages_sha256(root)
    for name, record in expected.items():
        if environment._git(packages / name, "rev-parse", "HEAD") != record["rev"]:
            raise ValueError("Installed dependency revision mismatch: " + name)
    upstream = manifest_map(read_json(packages / "mathlib" / "lake-manifest.json"), name="mathlib")
    if upstream != {k: v for k, v in expected.items() if k != "mathlib"}:
        raise ValueError("Pinned upstream manifest differs from reviewed closure")
    return {"schema": 1, "status": "mathlib_source_closure_verified",
            "checkout_sha": expected_sha, "lean_toolchain": TOOLCHAIN,
            "mathlib_revision": PIN, "package_count": len(expected),
            "packages": [{"name": k, **v} for k, v in sorted(expected.items())],
            "lock_sha256": environment._digest(lock),
            "clean_checkout_sha256": clean_digest,
            "artifact_bytes_verified": False, "offline_ready": False,
            "execution_allowed": False, "certificate": False}


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python -m scripts.lean_mathlib_source_probe CHECKOUT_SHA REPORT")
    root = Path(__file__).resolve().parents[1] / "lean"
    report = inspect_sources(root, expected_sha=sys.argv[1])
    raw = (json.dumps(report, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")
    with Path(sys.argv[2]).open("xb") as handle:
        handle.write(raw)
    if read_json(Path(sys.argv[2])) != report:
        raise ValueError("Source closure report roundtrip mismatch")
    print("ATLAS_MATHLIB_SOURCE_CLOSURE " + raw.decode("ascii").strip(), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
