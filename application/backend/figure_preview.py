"""Render indexed TikZ figures locally; the API never accepts arbitrary TeX."""
from __future__ import annotations
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import threading

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'data' / '.figure_cache'
RENDER_LOCK = threading.Lock()
PICTURE = re.compile(r'\\begin\s*\{(tikzpicture|tikzcd|picture)\}[\s\S]*?\\end\s*\{\1\}')

class FigureError(RuntimeError):
    pass

def figures(content: str) -> dict[str, str]:
    content = content.replace('\r\n', '\n')
    return {hashlib.sha256(m[0].encode('utf-8')).hexdigest(): m[0] for m in PICTURE.finditer(content)}

def declarations(source: str) -> str:
    """Copy only balanced literal macro/style declarations, never TeX includes."""
    result = []
    pattern = re.compile(r'\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\s*\{\\[A-Za-z]+\}(?:\[[0-9]+\])?\s*\{|\\(?:tikzset|pgfplotsset)\s*\{|\\definecolor\s*\{[^{}]+\}\s*\{[^{}]+\}\s*\{')
    source = re.sub(r'(?m)(?<!\\)%.*$', '', source)
    for match in pattern.finditer(source):
        depth, end = 1, match.end()
        while end < len(source) and depth:
            if source[end] == '\\':
                end += 2
                continue
            if source[end] == '{': depth += 1
            if source[end] == '}': depth -= 1
            end += 1
        if depth == 0:
            declaration = source[match.start():end]
            if declaration.startswith(r'\renewcommand'):
                name = re.search(r'\{(\\[A-Za-z]+)\}', declaration)[1]
                declaration = r'\providecommand{' + name + '}{}\n' + declaration
            result.append(declaration)
    return '\n'.join(result)

def preamble(module: str, content: str) -> str:
    # Bundled preambles remain available in the portable distribution.
    prefix = module.split('-')[0]
    if not re.fullmatch(r'[A-Z0-9]+', prefix):
        raise FigureError('Nieprawidłowy identyfikator rozdziału.')
    template = ROOT / 'config' / 'preambles' / (prefix + '.tex')
    book = template.read_text(encoding='utf-8-sig') if template.is_file() else ''
    libraries = {'arrows.meta', 'positioning', 'calc', 'decorations.pathreplacing', 'shapes.geometric', 'patterns', 'fit', 'matrix', 'quotes', 'angles', 'intersections', 'backgrounds'}
    for value in re.findall(r'\\usetikzlibrary\{([^{}]+)\}', book + '\n' + content):
        libraries.update(x.strip() for x in value.split(',') if re.fullmatch(r'[a-zA-Z0-9.]+', x.strip()))
    packages = r'\usepackage{pgfplots}\pgfplotsset{compat=1.18}' if '\\begin{axis}' in content or '\\pgfplots' in book else ''
    return '\n'.join([
        r'\documentclass[tikz,border=8pt]{standalone}',
        r'\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage[polish]{babel}',
        r'\usepackage{lmodern}',
        r'\usepackage{amsmath,amssymb,mathtools}',
        r'\AtBeginDocument{\shorthandoff{"}}',
        r'\usetikzlibrary{' + ','.join(sorted(libraries)) + '}', packages,
        r'\usepackage{tikz-cd}' if r'\begin{tikzcd}' in content else '',
        declarations(book.split(r'\begin{document}')[0]), declarations(content.split(r'\begin{tikzpicture}')[0]),
    ])

def render(module: str, content: str, figure_id: str) -> Path:
    picture = figures(content).get(figure_id)
    if picture is None:
        raise KeyError(figure_id)
    header = preamble(module, content)
    key = hashlib.sha256(('tikz-png-v1\n' + header + '\n' + picture).encode('utf-8')).hexdigest()
    target = CACHE / (key + '.png')
    with RENDER_LOCK:
        if target.is_file():
            return target
        compiler, converter = shutil.which('pdflatex'), shutil.which('pdftocairo')
        if not compiler or not converter:
            raise FigureError('Podgląd rysunków wymaga pdflatex i pdftocairo w PATH (MiKTeX/TeX Live oraz Poppler).')
        CACHE.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='tikz-', dir=CACHE) as folder:
            work = Path(folder)
            (work / 'figure.tex').write_text(header + '\n' + r'\begin{document}' + '\n' + picture + '\n' + r'\end{document}', encoding='utf-8')
            env = {**os.environ, 'openin_any': 'p', 'openout_any': 'p'}
            commands = [
                [compiler, *(['-disable-installer'] if 'miktex' in compiler.lower() else []), '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', 'figure.tex'],
                [converter, '-png', '-singlefile', '-r', '180', 'figure.pdf', 'figure'],
            ]
            for command in commands:
                try:
                    result = subprocess.run(command, cwd=work, env=env, stdin=subprocess.DEVNULL, capture_output=True, timeout=90,
                                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
                except subprocess.TimeoutExpired as exc:
                    raise FigureError('Przekroczono czas składania rysunku (90 s).') from exc
                if result.returncode:
                    output = (result.stdout + result.stderr).decode('utf-8', errors='replace')
                    errors = re.findall(r'(?m)^!.*(?:\n.*){0,3}', output)
                    raise FigureError('Nie udało się złożyć rysunku: ' + (' '.join(errors) or output[-900:]))
            png = work / 'figure.png'
            if not png.is_file():
                raise FigureError('Konwerter nie utworzył obrazu rysunku.')
            png.replace(target)
    return target
