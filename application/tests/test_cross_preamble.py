import sqlite3
import unittest
from contextlib import closing
from pathlib import Path
from backend.generator import GenerationError, project_files

ROOT = Path(__file__).resolve().parents[1]

def isolated_preamble_fixture(title):
    """Compile a real P1/P4 pair against a temporary *test-only* SQLite copy.

    References without targets remain invalid in the production index. They are
    omitted only in this isolated fixture so the preamble/theorem integration
    can be tested independently of the outstanding mathematical link audit.
    """
    with closing(sqlite3.connect(ROOT / "data/biblioteka.db")) as source:
        with closing(sqlite3.connect(":memory:")) as fixture:
            source.backup(fixture)
            fixture.row_factory = sqlite3.Row
            fixture.execute("""
                DELETE FROM references_tex
                WHERE source_document IN ('P1-03', 'P4-17')
                  AND target_document IS NULL
            """)
            return project_files(fixture, ['P1-03', 'P4-17'], [], title)


class CrossPreambleTests(unittest.TestCase):
    def test_live_corpus_does_not_silently_ignore_missing_labels(self):
        with closing(sqlite3.connect(ROOT / "data/biblioteka.db")) as con:
            con.row_factory = sqlite3.Row
            missing = con.execute("""
                SELECT target_label FROM references_tex
                WHERE source_document IN ('P1-03', 'P4-17')
                  AND target_document IS NULL
            """).fetchall()
            if missing:
                with self.assertRaisesRegex(GenerationError, "Nierozwiązane etykiety"):
                    project_files(con, ['P1-03', 'P4-17'], [], 'Walidacja')
            else:
                files, manifest=project_files(con, ['P1-03', 'P4-17'], [], 'Walidacja')
                self.assertIn('main.tex', files)
    def test_table_packages_are_explicit_in_generated_main_and_aux(self):
        files, manifest = isolated_preamble_fixture('Próba międzytomowa')
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
        files,manifest = isolated_preamble_fixture('Test')
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