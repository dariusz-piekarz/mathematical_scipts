"""Tests of read-only project generation, provenance, references and output archive."""
import io
import json
import sqlite3
import unittest
import zipfile
from fastapi.testclient import TestClient
from backend.api import app, ROOT
from backend.generator import GenerationError, project_files, zip_project, deduplicate_fragments, Fragment


class GeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.con=sqlite3.connect(ROOT/'data'/'biblioteka.db');cls.con.row_factory=sqlite3.Row
        cls.client=TestClient(app)

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def test_module_keeps_exact_source(self):
        files,report=project_files(self.con,['ALG-09'],[],'Analiza zesp.')
        self.assertEqual(report['references_external'],5)
        self.assertEqual(len(report['external_targets']),4)
        self.assertIn('ext-ALG-05-ch:ga5-rozdmuchania',files['rozdzialy/ALG-09.tex'].decode())
        self.assertIn('\\externaldocument[ext-ALG-05-]{aux/ALG-05}',files['main.tex'].decode())
        self.assertNotIn('\\externaldocument[ext-ALG-09-]',files['main.tex'].decode())
        self.assertTrue(files['aux/ALG-05.tex'].startswith(b'%'))
        self.assertEqual(report['source_sha256']['ALG-09'],self.con.execute('SELECT sha256 FROM documents WHERE id=?',('ALG-09',)).fetchone()[0])

    def test_fragment_not_entire_chapter(self):
        eid='ALG-09/proof/0004'
        files,report=project_files(self.con,[],[eid],'Proba')
        self.assertEqual(report['fragments']['ALG-09'],[eid])
        self.assertEqual(report['references_external'],1)
        self.assertEqual(report['external_targets'],{'ALG-09':['tw:ga9-gaga']})
        content=files['rozdzialy/ALG-09.tex'].decode()
        self.assertIn('\\ref{ext-ALG-09-tw:ga9-gaga}',content)
        self.assertNotIn('\\chapter{Geometria algebraiczna',content)
        self.assertIn('\\externaldocument[ext-ALG-09-]{aux/ALG-09}',files['main.tex'].decode())

    def test_section_includes_its_nested_objects(self):
        eid='label:sec:ga9-analityczne'
        files,report=project_files(self.con,[],[eid],'Proba')
        self.assertIn('\\section{Zbiory analityczne',files['rozdzialy/ALG-09.tex'].decode())
        self.assertEqual(report['references_external'],3)

    def test_overlap_within_parent_suppressed(self):
        x=deduplicate_fragments([Fragment(0,200,'parent'),Fragment(30,100,'child')]);self.assertEqual(len(x),1)
        with self.assertRaises(GenerationError):deduplicate_fragments([Fragment(0,100,'a'),Fragment(90,200,'b')])

    def test_duplicate_module_entity_module_wins(self):
        files,r=project_files(self.con,['ALG-09'],['ALG-09/proof/0004'],'Test')
        self.assertFalse(r['fragments'])
        self.assertEqual(len(r['whole_modules']),1)

    def test_selection_closure(self):
        files,report=project_files(self.con,['ALG-09'],[],'Próba',closure_depth=1)
        self.assertIn('ALG-05',report['modules'])
        self.assertLess(report['references_external'],5)

    def test_unknown_module_or_entity_rejected(self):
        with self.assertRaises(GenerationError):project_files(self.con,['../main'],[],'Bad')
        with self.assertRaises(GenerationError):project_files(self.con,[],['non-existent'],'Bad')
        with self.assertRaises(GenerationError):project_files(self.con,[],[],'Bad')

    def test_title_escaped(self):
        files,report=project_files(self.con,['BT-00'],[],r'Błąd $x_1$ & TeX')
        self.assertIn(r'Błąd \$x\_1\$ \& TeX',files['main.tex'].decode())

    def test_zip_paths_safe(self):
        data=zip_project({'main.tex':b'hello','rozdzialy/a.tex':b'chapter'})
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            self.assertTrue(z.testzip() is None)
            self.assertEqual(z.read('main.tex'),b'hello')
        with self.assertRaises(GenerationError):zip_project({'../bad.tex':b'123'})

    def test_http_zip_and_manifest(self):
        request={'title':'Test','modules':['BT-00'],'entities':[],'closure_depth':0}
        r=self.client.post('/api/generate/manifest',json=request)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['external_targets']['BT-04'],['subsec:so3'])
        r=self.client.post('/api/generate',json=request)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.headers['content-type'],'application/zip')
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            self.assertIsNone(z.testzip())
            self.assertIn('main.tex',z.namelist())
            self.assertIn('aux/BT-04.tex',z.namelist())
        self.assertEqual(self.client.post('/api/generate',json={'title':'Test','modules':['UNKNOWN']}).status_code,422)


if __name__=='__main__':unittest.main()

class CrossPreambleAuditTests(unittest.TestCase):
    def test_synthetic_package_and_command_conflicts(self):
        from backend.generator import preamble_compatibility
        templates={'ALG-01':r'\usepackage[unicode]{hyperref}\newcommand{\foo}{x}',
                   'TOP-01':r'\usepackage[colorlinks]{hyperref}\newcommand{\foo}{y}'}
        report=preamble_compatibility(templates,['ALG-01','TOP-01'])
        self.assertEqual(report['status'],'requires_review')
        self.assertEqual({x['type'] for x in report['conflicts']},{'package_options','command_definition'})

    def test_real_cross_domain_report_in_archive(self):
        con=sqlite3.connect(ROOT/'data'/'biblioteka.db');con.row_factory=sqlite3.Row
        try:
            files,manifest=project_files(con,['ALG-09','TOP-01'],[],'Łączony')
        finally:con.close()
        self.assertEqual(manifest['preamble_compatibility']['status'],'requires_review')
        self.assertIn('preamble_audit.json',files)
        self.assertTrue(manifest['preamble_compatibility']['not_merged'])
        self.assertEqual(json.loads(files['preamble_audit.json'])['groups'],['ALG','TOP'])

class MacroUsageAuditTests(unittest.TestCase):
    def test_cross_template_macro_use_detected(self):
        from backend.generator import macro_usage_audit
        t={'ALG-01':r'\newcommand{\alphahelper}{A}', 'TOP-01':r'\newcommand{\tophelper}{T}'}
        r=macro_usage_audit(t,['ALG-01','TOP-01'],{'ALG-01':r'\tophelper', 'TOP-01':r'\tophelper'})
        self.assertEqual(r['candidate_count'],2)
        self.assertEqual(r['candidates'][0]['macro'],r'\tophelper')
        self.assertEqual(r['candidates'][0]['providers'],['TOP-01'])

    def test_real_archive_has_macro_audit(self):
        con=sqlite3.connect(ROOT/'data'/'biblioteka.db');con.row_factory=sqlite3.Row
        try: files,manifest=project_files(con,['ALG-09','TOP-01'],[],'Łączony')
        finally: con.close()
        self.assertIn('macro_usage_audit.json',files)
        self.assertEqual(json.loads(files['macro_usage_audit.json']),manifest['macro_usage_audit'])

class LexicalMacroAuditTests(unittest.TestCase):
    def test_comments_and_escaped_percent(self):
        from backend.generator import scan_tex_code
        s='\\foo % \\ghost\n\\% \\real\n'
        out=scan_tex_code(s)
        self.assertIn('\\foo',out)
        self.assertNotIn('\\ghost',out)
        self.assertIn('\\real',out)

    def test_verbatim_and_inline_verb(self):
        from backend.generator import scan_tex_code
        s=r'\verb|\ghost| \begin{verbatim}\ghost\end{verbatim} \real'
        out=scan_tex_code(s)
        self.assertNotIn('\\ghost',out)
        self.assertIn('\\real',out)

    def test_local_macro_definition_suppresses_false_positive(self):
        from backend.generator import macro_usage_audit
        templates={'ALG-01':r'\newcommand{\first}{a}', 'TOP-01':r'\newcommand{\tophelper}{b}'}
        contents={'ALG-01':r'\newcommand{\tophelper}{locally} \tophelper', 'TOP-01':r'\tophelper'}
        r=macro_usage_audit(templates,['ALG-01','TOP-01'],contents)
        self.assertEqual(r['candidate_count'],1)
        self.assertEqual(r['candidates'][0]['module'],'TOP-01')

    def test_comment_and_literal_not_counted(self):
        from backend.generator import macro_usage_audit
        templates={'ALG-01':'','TOP-01':r'\newcommand{\tophelper}{b}'}
        contents={'ALG-01':r'% \tophelper'+'\n'+r'\verb|\tophelper|', 'TOP-01':''}
        self.assertEqual(macro_usage_audit(templates,['ALG-01','TOP-01'],contents)['candidate_count'],0)
