import sqlite3
import unittest
from pathlib import Path
from backend.generator import project_files

ROOT = Path(__file__).resolve().parents[1]

class CrossPreambleTests(unittest.TestCase):
    def test_table_packages_are_explicit_in_generated_main_and_aux(self):
        con = sqlite3.connect(ROOT / 'data/biblioteka.db')
        con.row_factory = sqlite3.Row
        try:
            files, manifest = project_files(con, ['P1-03', 'P4-17'], [], 'Próba międzytomowa')
        finally:
            con.close()
        self.assertGreater(manifest['references_external'], 0)
        for name, body in files.items():
            if name == 'main.tex' or name.startswith('aux/') and name.endswith('.tex'):
                tex = body.decode('utf-8')
                self.assertRegex(tex, r'\\usepackage(?:\[[^]]*\])?\{[^}]*\barray\b[^}]*\}')
                self.assertRegex(tex, r'\\usepackage(?:\[[^]]*\])?\{[^}]*\bbooktabs\b[^}]*\}')

if __name__ == '__main__':
    unittest.main()

class TheoremRegistryTests(unittest.TestCase):
    def test_secondary_environment_is_imported_with_style_and_counter(self):
        con=sqlite3.connect(ROOT / 'data/biblioteka.db');con.row_factory=sqlite3.Row
        try: files,manifest=project_files(con,['P1-03','P4-17'],[],'Test')
        finally: con.close()
        audit=manifest['theorem_environment_audit']
        self.assertEqual([x['environment'] for x in audit['additions']],['zadanie'])
        main=files['main.tex'].decode()
        self.assertIn(r'\theoremstyle{definition}'+'\n'+r'\newtheorem{zadanie}{Zadanie rozwiązane}[chapter]',main)
        self.assertNotIn(r'\externaldocument[II-]',main)
        self.assertIn(r'\externaldocument[ext-P4-03-]',main)

    def test_conflicting_environment_is_not_silently_merged(self):
        from backend.generator import theorem_environment_audit
        t={'A':r'\newtheorem{zadanie}{Zadanie}[chapter]',
           'B':r'\newtheorem{zadanie}{Ćwiczenie}[section]',
           'C':r'\newtheorem{twierdzenie}{Twierdzenie}[chapter]'}
        result=theorem_environment_audit(t,['C','A','B'],{'C':r'\begin{zadanie}x\end{zadanie}'})
        self.assertEqual(result['additions'],[])
        self.assertEqual(result['conflicts'][0]['environment'],'zadanie')