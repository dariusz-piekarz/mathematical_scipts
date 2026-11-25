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
