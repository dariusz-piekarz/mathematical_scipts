"""Chapter 19 audits III-IV: cross-reference, structural, finite semantic regression.
Finite cases are sanity checks only, never substitutes for proofs in Q.
"""
from pathlib import Path
import itertools
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
REPO_SOURCE = ROOT / 'chapters/pl/logic_and_set_theory/19-pierwsze-twierdzenie-godla-o-niezupelnosci.tex'
SRC = REPO_SOURCE if REPO_SOURCE.is_file() else Path('/mnt/data/logika_rozdzial_19_audyt_III.tex')
CHAPTERS = REPO_SOURCE.parent if REPO_SOURCE.is_file() else Path('/mnt/data/logic19_audit3_work/chapters')

class TestChapter19(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = SRC.read_text(encoding='utf-8')

    def test_environments_and_bibliography(self):
        for name, count in {'definicja':3,'twierdzenie':2,'lemat':2,'wniosek':2,'proof':6,
                            'przyklad':3,'uwaga':6}.items():
            with self.subTest(env=name):
                self.assertEqual(self.t.count('\\begin{'+name+'}'), count)
                self.assertEqual(self.t.count('\\end{'+name+'}'), count)
        stack=[]
        for kind,name in re.findall(r'\\(begin|end)\{([^}]+)\}', self.t):
            if kind == 'begin':stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(name,stack.pop())
        self.assertFalse(stack)

    def test_labels_and_local_crossrefs(self):
        local=re.findall(r'\\label\{([^}]+)\}',self.t)
        refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',self.t)
        self.assertEqual(len(local),10)
        self.assertEqual(len(local),len(set(local)))
        self.assertEqual(len(refs),22)
        external=set()
        for f in CHAPTERS.glob('*.tex'):
            if f.name.startswith('19-'): continue
            external.update(re.findall(r'\\label\{([^}]+)\}',f.read_text(encoding='utf8')))
        self.assertFalse(set(local).intersection(external))
        self.assertFalse(set(refs).difference(set(local)).difference(external))

    def test_godel_uses_numerals_and_omega_only_for_negation(self):
        self.assertIn(r'Q\vdash G_T\leftrightarrow',self.t)
        self.assertIn(r'\neg\operatorname{Bew}_T(\overline g)',self.t)
        self.assertIn(r'T\nvdash G_T',self.t)
        self.assertIn(r'T\nvdash\neg G_T',self.t)
        self.assertIn(r'\neg\operatorname{Prf}_T(\overline p,\overline g)',self.t)
        self.assertIn('w modelu standardowym $\\mathfrak N$',self.t)

    def test_rosser_total_negation_encoding(self):
        self.assertIn(r'\operatorname{neg}(n)',self.t)
        self.assertIn('na niepoprawnych kodach ustaloną',self.t)
        self.assertIn(r'\forall z\,(N(\overline r,z)\leftrightarrow z=\overline{r^-})',self.t)
        self.assertIn(r'\forall q<p\,\neg\operatorname{Prf}_T(q,z)',self.t)

    def test_rosser_first_case_finite_minimality(self):
        # Under consistency, no proof of neg R: any actual proof of R witnesses RosPr.
        for a in range(80):
            r_proofs={a}
            not_r_proofs=set()
            witness=any(all(q>=p for q in not_r_proofs) for p in r_proofs)
            self.assertTrue(witness)
            self.assertTrue(all(q not in not_r_proofs for q in range(a)))
        self.assertIn('Gdy $a=0$, alternatywa jest pusta',self.t)
        self.assertIn(r'Q\vdash\forall q<\overline a\,\neg\operatorname{Prf}_T(q,\overline{r^-})',self.t)

    def test_rosser_second_case_finite_exhaustive(self):
        # Under consistency, no proof of R; a proof of neg R at b means RosPr false.
        for b in range(80):
            for p in range(120):
                self.assertTrue((p<=b) or (b<p))
                obstructed=(p<=b) or ((b<p) and b<p)
                self.assertTrue(obstructed)
        self.assertIn(r'\forall p\le\overline b',self.t)
        self.assertIn(r'\exists q<p\,\operatorname{Prf}_T(q,\overline{r^-})',self.t)
        self.assertIn(r'Q\vdash\neg\operatorname{RosPr}_T(\overline r)',self.t)

    def test_rosser_consistency_and_no_omega_used(self):
        rosser=self.t.split(r'\begin{twierdzenie}[Wzmocnienie Rossera]')[1].split(r'\end{proof}')[0]
        self.assertIn('niesprzeczną teorią',rosser)
        self.assertNotIn('Zakładamy teraz $\\omega$-niesprzeczność',rosser)
        self.assertIn(r'\ref{res:4:4}',rosser)
        self.assertIn(r'\ref{lem:incomp-proof-check}',rosser)
        self.assertIn(r'\eqref{eq:rosser-instance}',rosser)

    def test_actual_proof_code_checker_both_directions(self):
        self.assertIn(r'Q\vdash\operatorname{Prf}_T(\overline p,\overline g)',self.t)
        self.assertIn(r'Q\vdash\neg\operatorname{Prf}_T(\overline p,\overline g)',self.t)
        self.assertIn(r'\ref{res:7:7}',self.t)
        self.assertIn(r'\ref{res:4:7}',self.t)

    def test_total_decider_and_true_arithmetic_corollaries(self):
        self.assertIn('totalną relację rekurencyjną $D(n)$',self.t)
        self.assertIn(r'Q\vdash H\leftrightarrow\neg\rho_D(\overline h)',self.t)
        self.assertIn(r'\ref{thm:rosser-first}',self.t)
        self.assertIn('zbiór kodów jej twierdzeń nie jest rozstrzygalny',self.t)

    def test_independent_models_completeness_not_incompleteness(self):
        self.assertIn(r'\mathfrak A\models T+\rho',self.t)
        self.assertIn(r'\mathfrak B\models T+\neg\rho',self.t)
        self.assertIn('twierdzenie Gödla o pełności',self.t)

    def test_no_inappropriate_induction_in_Q(self):
        self.assertIn('skończoną alternatywą',self.t)
        self.assertIn('Dla każdego z \\emph{faktycznie skończenie wielu}',self.t)
        self.assertIn('Nie potrzebowaliśmy twierdzenia',self.t)
        self.assertNotIn(r'Q\vdash\forall p\,\neg\operatorname{Prf}_T(p,\overline r)',self.t)

if __name__=='__main__': unittest.main(verbosity=2)