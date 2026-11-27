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

if __name__ == '__main__':
    unittest.main()
