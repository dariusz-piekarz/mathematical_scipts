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


# Deliberately limited to literal definitions. Optional default arguments,
# arbitrary TeX execution, and mid-chapter scopes are not supported.
COMMAND = re.compile(r"^\\(newcommand|providecommand)\*?\s*\{(\\[A-Za-z]+)\}\s*(?:\[(\d+)\])?\s*\{(.*)\}\s*$")
OPERATOR = re.compile(r"^\\DeclareMathOperator(\*)?\s*\{(\\[A-Za-z]+)\}\s*\{(.*)\}\s*$")
HEADER = re.compile(r"^\\(?:chapter\*?\{.*\}|label\{[^{}]*\}|begingroup)\s*$")



def without_tex_comment(line):
    """Remove unescaped percent comments, preserving escaped percent signs."""
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
        elif line[i] == "%":
            return line[:i]
        else:
            i += 1
    return line


def brace_balance(line):
    """Count only unescaped grouping braces."""
    depth = 0
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
            continue
        if line[i] == "{":
            depth += 1
        elif line[i] == "}":
            depth -= 1
        i += 1
    return depth


def logical_macro_lines(source):
    """Join literal macro bodies spanning lines; leave other TeX untouched."""
    lines = iter(source.splitlines())
    for raw in lines:
        clean = without_tex_comment(raw).strip()
        if re.match(r"^\\(?:newcommand|providecommand|DeclareMathOperator)\*?(?![A-Za-z])", clean):
            # A percent comment suppresses the end-of-line space in TeX.
            # Ordinary newlines are spaces, unless a control word absorbs them.
            while brace_balance(clean) > 0:
                try:
                    following = next(lines)
                except StopIteration:
                    break
                part = without_tex_comment(following)
                clean += ("" if len(without_tex_comment(raw)) < len(raw) else " ") + part.lstrip()
                raw = following
        yield clean


def add_literal_macro(line, macros):
    if brace_balance(line) != 0:
        return False
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
        for line in logical_macro_lines(path.read_text(encoding="utf-8-sig")):
            add_literal_macro(line, macros)
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
        for line in logical_macro_lines(path.read_text(encoding="utf-8-sig")):
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
