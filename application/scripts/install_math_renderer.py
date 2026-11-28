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
HEADER_COMMAND = re.compile(r"\\(?:chapter|section|label|index)\*?\s*(?=\{)")



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


def is_header_metadata(line):
    """Recognize only complete title/label/index commands, including nested braces."""
    if line == r"\begingroup":
        return True
    cursor = 0
    while cursor < len(line):
        match = HEADER_COMMAND.match(line, cursor)
        if not match:
            return False
        end = match.end()
        depth = 1
        end += 1
        while end < len(line) and depth:
            if line[end] == "\\":
                end += 2
                continue
            if line[end] == "{":
                depth += 1
            elif line[end] == "}":
                depth -= 1
            end += 1
        if depth:
            return False
        cursor = end
        while cursor < len(line) and line[cursor].isspace():
            cursor += 1
    return bool(line)


def logical_macro_lines(source):
    """Join literal macro bodies spanning lines; leave other TeX untouched."""
    lines = source.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        clean = without_tex_comment(raw).strip()
        if re.match(r"^\\(?:newcommand|providecommand|DeclareMathOperator)\*?(?![A-Za-z])", clean):
            while i < len(lines):
                balance = brace_balance(clean)
                if balance < 0 or (balance == 0 and
                        (COMMAND.fullmatch(clean) or OPERATOR.fullmatch(clean))):
                    break
                following = lines[i]
                part = without_tex_comment(following)
                # With balanced braces, only continue through whitespace,
                # comments and possible braced/optional arguments. Do not
                # consume the next prose line or independent declaration.
                if balance == 0 and part.strip() and not part.lstrip().startswith(("{", "[")):
                    break
                if balance == 0 and not part.strip():
                    i += 1
                    continue
                i += 1
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
            if not line or line.startswith("%") or is_header_metadata(line):
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
