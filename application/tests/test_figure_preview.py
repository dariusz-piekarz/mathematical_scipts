"""Contracts for indexed figure rendering; no installed TeX is needed here."""
import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from backend import figure_preview as renderer

SOURCE = r'\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}'

class FigurePreviewTests(unittest.TestCase):
    def test_figures_address_only_exact_indexed_source(self):
        figure_id = hashlib.sha256(SOURCE.encode()).hexdigest()
        self.assertEqual(renderer.figures(SOURCE), {figure_id: SOURCE})
        with self.assertRaises(KeyError):
            renderer.render('ALG-08', SOURCE, '../anything')
        for environment in ('tikzcd', 'picture'):
            self.assertEqual(len(renderer.figures(SOURCE.replace('tikzpicture', environment))), 1)

    def test_balanced_declarations_exclude_external_inputs(self):
        source = r'\input{private} \newcommand{\Q}{\mathbb{Q}} \tikzset{a/.style={draw,fill=blue}}'
        result = renderer.declarations(source)
        self.assertNotIn('input', result)
        self.assertIn(r'\newcommand{\Q}{\mathbb{Q}}', result)
        self.assertIn(r'\tikzset{a/.style={draw,fill=blue}}', result)

    def test_later_figure_uses_preceding_declarations_only(self):
        first = r'\begin{tikzpicture}\newcommand{\inside}{X}\end{tikzpicture}'
        second = r'\begin{tikzcd}A\arrow[r]&\later\end{tikzcd}'
        source = (r'\newcommand{\early}{E}' + '\n' + first + '\n'
                  + r'\newcommand{\later}{L}' + '\n' + second + '\n'
                  + r'\newcommand{\future}{F}')
        first_id = hashlib.sha256(first.encode()).hexdigest()
        second_id = hashlib.sha256(second.encode()).hexdigest()
        first_header = renderer.preamble('AM1-36', source, first_id)
        second_header = renderer.preamble('AM1-36', source, second_id)
        self.assertIn(r'\newcommand{\early}{E}', first_header)
        self.assertNotIn(r'\newcommand{\later}{L}', first_header)
        self.assertIn(r'\newcommand{\early}{E}', second_header)
        self.assertIn(r'\newcommand{\later}{L}', second_header)
        self.assertNotIn(r'\newcommand{\inside}{X}', second_header)
        self.assertNotIn(r'\newcommand{\future}{F}', second_header)

    def test_explicit_groups_do_not_leak_declarations(self):
        source = (r'\newcommand{\outer}{O}\begingroup'
                  r'\newcommand{\local}{L}\begingroup'
                  r'\newcommand{\nested}{N}\endgroup'
                  r'\newcommand{\body}{\begingroup X\endgroup}')
        active = renderer.declarations(source)
        self.assertIn(r'\newcommand{\outer}{O}', active)
        self.assertIn(r'\newcommand{\local}{L}', active)
        self.assertNotIn(r'\newcommand{\nested}{N}', active)
        self.assertIn(r'\newcommand{\body}{\begingroup X\endgroup}', active)
        closed = renderer.declarations(source + r'\endgroup')
        self.assertEqual(closed, r'\newcommand{\outer}{O}')

    def test_graph_and_knot_preamble_matches_book_and_has_styles(self):
        book = (renderer.ROOT.parent / "books/pl/graph_and_knot_theory.tex").read_text(encoding="utf-8-sig")
        template = (renderer.ROOT / "config/preambles/GW.tex").read_text(encoding="utf-8-sig")
        self.assertEqual(template.strip(), book.split(r"\begin{document}", 1)[0].strip())
        source = r"\begin{tikzpicture}\node[tgBlueVertex] (a) at (0,0) {}; \draw[tgEdge] (a)--(1,1);\end{tikzpicture}"
        header = renderer.preamble("GW-01", source, next(iter(renderer.figures(source))))
        for declaration in (r"\definecolor{tgBlue}", r"tgBlueVertex/.style", r"tgEdge/.style", r"\definecolor{ktInk}"):
            self.assertIn(declaration, header)

    def test_mathscr_package_in_standalone_preamble(self):
        source = r'\begin{tikzpicture}\node {$\mathscr B$};\end{tikzpicture}'
        self.assertIn(r'\usepackage{mathrsfs}', renderer.preamble('AM2-15', source))

    def test_render_cache_and_failed_compilation(self):
        key = next(iter(renderer.figures(SOURCE)))
        with tempfile.TemporaryDirectory() as temp, patch.object(renderer, 'CACHE', Path(temp)), patch.object(renderer.shutil, 'which', side_effect=lambda name: name):
            def run(command, **kwargs):
                self.assertEqual(kwargs['stdin'], subprocess.DEVNULL)
                self.assertEqual(kwargs['timeout'], 90)
                if command[0] == 'pdflatex':
                    self.assertIn('-no-shell-escape', command)
                else:
                    (Path(kwargs['cwd']) / 'figure.png').write_bytes(b'png-test')
                return subprocess.CompletedProcess(command, 0, b'', b'')
            with patch.object(renderer.subprocess, 'run', side_effect=run) as mocked:
                image = renderer.render('ALG-08', SOURCE, key)
                self.assertEqual(image.read_bytes(), b'png-test')
                self.assertEqual(renderer.render('ALG-08', SOURCE, key), image)
                self.assertEqual(mocked.call_count, 2)
            with patch.object(renderer.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, b'! Broken drawing', b'')):
                with self.assertRaisesRegex(renderer.FigureError, 'Broken drawing'):
                    renderer.render('ALG-08', SOURCE.replace('(1,1)', '(2,2)'), next(iter(renderer.figures(SOURCE.replace('(1,1)', '(2,2)')))))

    def test_worker_limit_is_conservative_and_bounded(self):
        for raw, expected in [('0', 1), ('1', 1), ('2', 2), ('3', 3), ('100', 3), ('bad', 1)]:
            with self.subTest(raw=raw), patch.dict(renderer.os.environ, {'ATLAS_TIKZ_WORKERS': raw}):
                self.assertEqual(renderer._render_limit(), expected)

    def test_cached_hit_does_not_wait_for_compilation_slot(self):
        from concurrent.futures import ThreadPoolExecutor
        import threading
        key = next(iter(renderer.figures(SOURCE)))
        with tempfile.TemporaryDirectory() as temp, patch.object(renderer, 'CACHE', Path(temp)), patch.object(renderer, 'RENDER_SLOTS', threading.BoundedSemaphore(1)):
            def compile_image(header, picture, target):
                target.write_bytes(b'cached')
                return target
            with patch.object(renderer, '_compile_figure', side_effect=compile_image) as compile_mock:
                expected = renderer.render('ALG-08', SOURCE, key)
                with ThreadPoolExecutor(max_workers=1) as pool:
                    renderer.RENDER_SLOTS.acquire()
                    try:
                        future = pool.submit(renderer.render, 'ALG-08', SOURCE, key)
                        self.assertEqual(future.result(timeout=3), expected)
                    finally:
                        renderer.RENDER_SLOTS.release()
                self.assertEqual(compile_mock.call_count, 1)

    def test_identical_concurrent_requests_compile_once(self):
        from concurrent.futures import ThreadPoolExecutor
        import threading
        key = next(iter(renderer.figures(SOURCE)))
        started, release = threading.Event(), threading.Event()
        with tempfile.TemporaryDirectory() as temp, patch.object(renderer, 'CACHE', Path(temp)), patch.object(renderer, 'RENDER_SLOTS', threading.BoundedSemaphore(2)):
            def compile_image(header, picture, target):
                started.set()
                if not release.wait(5):
                    raise AssertionError('test compilation release timed out')
                target.write_bytes(b'complete')
                return target
            with patch.object(renderer, '_compile_figure', side_effect=compile_image) as compile_mock, ThreadPoolExecutor(max_workers=6) as pool:
                futures = [pool.submit(renderer.render, 'ALG-08', SOURCE, key) for _ in range(6)]
                try:
                    self.assertTrue(started.wait(3))
                finally:
                    release.set()
                results = [f.result(timeout=5) for f in futures]
                self.assertEqual(len(set(results)), 1)
                self.assertEqual(compile_mock.call_count, 1)
                self.assertEqual(results[0].read_bytes(), b'complete')

    def test_distinct_compilations_respect_slots_and_retry_failure(self):
        from concurrent.futures import ThreadPoolExecutor
        import threading
        sources = [SOURCE.replace('(1,1)', f'({i},{i})') for i in range(1, 200)]
        distinct = {}
        for source in sources:
            key = next(iter(renderer.figures(source)))
            header = renderer.preamble('ALG-08', source, key)
            digest = hashlib.sha256(('tikz-png-v1\n' + header + '\n' + source).encode()).hexdigest()
            distinct.setdefault(int(digest[:8], 16) % len(renderer.RENDER_KEY_LOCKS), (source, key))
            if len(distinct) == 4:
                break
        pairs = list(distinct.values())
        self.assertEqual(len(pairs), 4)
        guard, release, two_started = threading.Lock(), threading.Event(), threading.Event()
        active = peak = 0
        with tempfile.TemporaryDirectory() as temp, patch.object(renderer, 'CACHE', Path(temp)), patch.object(renderer, 'RENDER_SLOTS', threading.BoundedSemaphore(2)):
            def compile_image(header, picture, target):
                nonlocal active, peak
                with guard:
                    active += 1
                    peak = max(peak, active)
                    if active == 2:
                        two_started.set()
                try:
                    if not release.wait(5):
                        raise AssertionError('test compilation release timed out')
                    target.write_bytes(b'complete')
                    return target
                finally:
                    with guard:
                        active -= 1
            with patch.object(renderer, '_compile_figure', side_effect=compile_image), ThreadPoolExecutor(max_workers=4) as pool:
                futures = [pool.submit(renderer.render, 'ALG-08', source, key) for source, key in pairs]
                try:
                    self.assertTrue(two_started.wait(3))
                finally:
                    release.set()
                self.assertEqual(len({f.result(timeout=5) for f in futures}), 4)
                self.assertEqual(peak, 2)
            source, key = pairs[0]
            for image in Path(temp).glob('*.png'):
                image.unlink()
            with patch.object(renderer, '_compile_figure', side_effect=renderer.FigureError('fixture')):
                with self.assertRaisesRegex(renderer.FigureError, 'fixture'):
                    renderer.render('ALG-08', source, key)
            with patch.object(renderer, '_compile_figure', side_effect=compile_image):
                self.assertTrue(renderer.render('ALG-08', source, key).is_file())

if __name__ == '__main__':
    unittest.main()
