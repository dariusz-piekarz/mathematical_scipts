"""Integration checks: local theorem declarations and generated TeX."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from backend.generator import theorem_environment_audit


class LocalTheoremCompilationTests(unittest.TestCase):
    def test_local_environment_compiles_without_import(self):
        if not shutil.which('pdflatex'):
            self.skipTest('pdflatex unavailable')
        body = r'\newtheorem{locallemma}{Lemat}' + '\n' + r'\begin{locallemma}Test.\end{locallemma}'
        audit = theorem_environment_audit({'A':r'\documentclass{report}', 'B':r'\newtheorem{locallemma}{Lemat}'}, ['A'], {'A':body})
        self.assertEqual(audit['additions'], [])
        self.assertEqual(audit['conflicts'], [])
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td)
            (folder/'main.tex').write_text(r'\documentclass{report}'+'\n'+r'\begin{document}'+'\n'+body+'\n'+r'\end{document}',encoding='utf-8')
            p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=40)
            self.assertEqual(p.returncode,0,p.stdout.decode(errors='replace')[-2500:])
            self.assertTrue((folder/'main.pdf').is_file())

    def test_duplicate_local_declaration_is_flagged(self):
        body=r'\newtheorem{locallemma}{Lemat}'+'\n'+r'\newtheorem{locallemma}{Lemat}'
        audit=theorem_environment_audit({'A':''},['A'],{'A':body})
        self.assertTrue(any(e['reason']=='repeated_declaration_within_source' for e in audit['unresolved']))

if __name__=='__main__':unittest.main()