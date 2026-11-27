"""Install version-pinned local KaTeX assets; the browser uses no CDN."""
from pathlib import Path
import base64
import hashlib
import io
import json
import re
import shutil
import tarfile
import tempfile
import sys
from urllib.request import urlopen

# The launcher runs this file directly as well as importing it in tests.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.latex_parser import module_id

VERSION = "0.16.22"
REGISTRY = "https://registry.npmjs.org/katex/"
DEST = Path(__file__).resolve().parents[1] / "frontend/vendor/katex"
REQUIRED = ("katex.min.js", "katex.min.css", "contrib/auto-render.min.js", "LICENSE")


def ready(folder):
    return all((folder / p).is_file() for p in REQUIRED) and any((folder / "fonts").glob("*.woff2"))


# Deliberately limited to literal, single-line definitions. Optional default
# arguments, arbitrary TeX execution, and mid-chapter scopes are not supported.
COMMAND = re.compile(r"^\\(newcommand|providecommand)\*?\s*\{(\\[A-Za-z]+)\}\s*(?:\[(\d+)\])?\s*\{(.*)\}\s*$")
OPERATOR = re.compile(r"^\\DeclareMathOperator(\*)?\s*\{(\\[A-Za-z]+)\}\s*\{(.*)\}\s*$")
HEADER = re.compile(r"^\\(?:chapter\*?\{.*\}|label\{[^{}]*\}|begingroup)\s*$")


def add_literal_macro(line, macros):
    match = COMMAND.fullmatch(line)
    if match:
        if match[1] == "providecommand":
            macros.setdefault(match[2], match[4])
        else:
            macros[match[2]] = match[4]
        return True
    match = OPERATOR.fullmatch(line)
    if match:
        macros[match[2]] = "\\operatorname" + (match[1] or "") + "{" + match[3] + "}"
        return True
    return False


def write_macro_profiles():
    """Generate book profiles and chapter-header deltas, without executing TeX."""
    profiles = {}
    preambles = DEST.parents[2] / "config" / "preambles"
    for path in sorted(preambles.glob("*.tex")):
        macros = {}
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            add_literal_macro(line.strip(), macros)
        profiles[path.stem] = macros

    # Only declarations before the first substantive chapter content are
    # available to all its fragments. Do not leak later scoped declarations
    # into preceding equations or another chapter/book.
    chapters = DEST.parents[3] / "chapters" / "pl"
    for path in sorted(chapters.rglob("*.tex")):
        doc_id = module_id(path)
        base = profiles.get(doc_id.split("-", 1)[0])
        if base is None or "-" not in doc_id:
            continue
        macros = dict(base)
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if not line or line.startswith("%") or HEADER.fullmatch(line):
                continue
            if not add_literal_macro(line, macros):
                break
        delta = {key: value for key, value in macros.items() if base.get(key) != value}
        if delta:
            profiles[doc_id] = delta
    DEST.parent.mkdir(parents=True, exist_ok=True)
    (DEST.parent / "math-macro-profiles.js").write_text(
        "window.atlasMathMacroProfiles = " + json.dumps(profiles, ensure_ascii=True) + ";\n",
        encoding="utf-8",
    )


def install():
    write_macro_profiles()

    marker = DEST / ".version"
    if ready(DEST) and marker.is_file() and marker.read_text() == VERSION:
        return
    with urlopen(REGISTRY + VERSION, timeout=30) as response:
        metadata = json.load(response)
    url = REGISTRY + "-/katex-" + VERSION + ".tgz"
    if metadata["version"] != VERSION or metadata["dist"]["tarball"] != url:
        raise RuntimeError("Unexpected distribution")
    with urlopen(url, timeout=60) as response:
        data = response.read(20 * 1024 * 1024 + 1)
    digest = "sha512-" + base64.b64encode(hashlib.sha512(data).digest()).decode("ascii")
    if len(data) > 20 * 1024 * 1024 or digest != metadata["dist"]["integrity"]:
        raise RuntimeError("KaTeX archive integrity check failed")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=DEST.parent) as tmp:
        stage = Path(tmp) / "katex"
        stage.mkdir()
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            for member in archive:
                if not member.isfile():
                    continue
                if member.name == "package/LICENSE":
                    name = "LICENSE"
                elif member.name.startswith("package/dist/"):
                    name = member.name.removeprefix("package/dist/")
                else:
                    continue
                parts = name.split("/")
                if name not in REQUIRED and not (len(parts) == 2 and parts[0] == "fonts" and "\\" not in name and Path(parts[1]).suffix in {".woff", ".woff2", ".ttf"}):
                    continue
                target = stage / name
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open("wb") as output:
                    shutil.copyfileobj(source, output)
        if not ready(stage):
            raise RuntimeError("Incomplete KaTeX distribution")
        (stage / ".version").write_text(VERSION)
        if DEST.exists():
            shutil.rmtree(DEST)
        stage.rename(DEST)
    print("Local KaTeX", VERSION, "installed")


if __name__ == "__main__":
    install()
