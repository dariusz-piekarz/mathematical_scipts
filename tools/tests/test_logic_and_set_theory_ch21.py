"""Regression audit for the reviewed logic & set theory chapter 21.

Finite arithmetic checks are sanity tests; they are not proofs inside PA.
"""
from pathlib import Path
import math
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
REPO_FILE = ROOT / 'chapters/pl/logic_and_set_theory/21-operacje-na-dowodach-i-warunki-wyprowadzalnosci.tex'
SOURCE = REPO_FILE if REPO_FILE.is_file() else Path('/mnt/data/logika_rozdzial_21_audyt_III.tex')
CHAPTERS = REPO_FILE.parent if REPO_FILE.is_file() else Path('/mnt/data/logic21_audit3_work/chapters')


def beta(a, b, i):
    return a % (1 + (i + 1) * b)


def crt(values, moduli):
    a, M = 0, 1
    for r, m in zip(values, moduli):
        assert math.gcd(M, m) == 1
        v = ((r - a) * pow(M, -1, m)) % m
        a, M = (a + M * v) % (M * m), M * m
    return a


class TestChapter21(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = SOURCE.read_text(encoding='utf-8')

    def test_environment_counts(self):
        for name, count in {'twierdzenie': 2, 'lemat': 5, 'wniosek': 0, 'proof': 7,
                            'definicja': 0, 'przyklad': 3, 'uwaga': 4, 'figure': 0}.items():
            with self.subTest(name=name):
                self.assertEqual(self.s.count('\\begin{' + name + '}'), count)
                self.assertEqual(self.s.count('\\end{' + name + '}'), count)

    def test_environment_nesting(self):
        stack = []
        for typ, name in re.findall(r'\\(begin|end)\{([^}]+)\}', self.s):
            if typ == 'begin':
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), name)
        self.assertFalse(stack)

    def test_label_uniqueness_and_resolved_targets(self):
        labels = re.findall(r'\\label\{([^}]+)\}', self.s)
        refs = re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}', self.s)
        self.assertEqual(len(labels), 8)
        self.assertEqual(len(set(labels)), 8)
        self.assertEqual(len(refs), 20)
        other = set()
        for f in CHAPTERS.glob('*.tex'):
            if f.name.startswith('21-'):
                continue
            other.update(re.findall(r'\\label\{([^}]+)\}', f.read_text(encoding='utf-8')))
        self.assertFalse(set(labels) & other)
        self.assertFalse(set(refs) - set(labels) - other)

    def test_beta_coprimality_empty_and_large_prefix(self):
        for n in range(10):
            a, b = 97 + n * 13, n + 1
            vals = [beta(a, b, i) for i in range(n)] + [3*n + 4]
            bound = max(vals)
            bp = math.factorial(n + 1) * (bound + 1)
            moduli = [1 + (i + 1) * bp for i in range(n + 1)]
            self.assertTrue(all(z < m for z, m in zip(vals, moduli)))
            self.assertTrue(all(math.gcd(moduli[i], moduli[j]) == 1
                                for i in range(n + 1) for j in range(i + 1, n + 1)))
            ap = crt(vals, moduli)
            self.assertEqual([beta(ap, bp, i) for i in range(n + 1)], vals)

    def test_beta_remainder_step(self):
        self.assertIn(r'a_{k+1}:=a_k+P_kv', self.s)
        self.assertIn(r'0\le v<m_k', self.s)
        self.assertIn(r'$r_i\le R$', self.s)
        self.assertNotIn(r'm_i\ge M+1', self.s)

    def test_pa_induction_not_q(self):
        self.assertIn('indukcję po liczbie $k$', self.s)
        self.assertIn('Nie', self.s)
        self.assertIn(r'\ref{lem:xi-append-beta}', self.s)
        self.assertIn(r'\mathrm{PA}\vdash\forall\vec x\,\exists!y', self.s)

    def test_mp_function_total_and_graph(self):
        self.assertIn(r'\forall p\,\forall q\,\exists!r', self.s)
        self.assertIn(r'M_{\varphi,\psi}(p,q,r)', self.s)
        self.assertIn(r'\operatorname{Prf}_T(r,', self.s)
        self.assertIn('Na niepoprawnych wejściach', self.s)

    def test_verifier_program_selected_constructively(self):
        self.assertIn('Wybieramy}', self.s)
        self.assertIn('z jego\nschematu pierwotnie rekurencyjnego', self.s)
        self.assertIn('czas działania nie musi być pierwotnie rekurencyjny', self.s)
        self.assertIn('pierwotnie rekurencyjne\nograniczenie liczby kroków', self.s)

    def test_mp_fixed_formula_proofs(self):
        self.assertIn(r'\operatorname{Prf}_T(p,\overline{\ulcorner\varphi\to\psi\urcorner})', self.s)
        self.assertIn(r'\operatorname{Prf}_T(q,\overline{\ulcorner\varphi\urcorner})', self.s)
        self.assertIn('certyfikat akceptacji nowego dowodu', self.s)

    def test_d2_uses_existence_of_new_proof(self):
        z = self.s.split(r'\begin{twierdzenie}[Warunek (D2)]',1)[1].split(r'\end{proof}',1)[0]
        for x in [r'\exists p\,\operatorname{Prf}_T',r'\exists q\,\operatorname{Prf}_T',r'\exists r\,\operatorname{Prf}_T']:
            self.assertIn(x, z)

    def test_delta_compiler_both_polarities_and_graph_form(self):
        z = self.s.split(r'\begin{lemat}[Sformalizowana prawdziwość $\Delta_0$]',1)[1].split(r'\end{proof}',1)[0]
        for x in [r'b_\delta^+',r'b_\delta^-',r'F_\delta^+(\vec x,p)',r'I_\delta(\vec x,z)',r'\neg\delta(\vec x)&\to']:
            self.assertIn(x, z)

    def test_bounded_quantifier_term_evaluation_proof(self):
        self.assertIn(r'$t(\overline{\vec n})=\overline k$', self.s)
        self.assertIn(r'$\overline u<t(\overline{\vec n})$', self.s)
        self.assertIn('Podstawienie równych termów', self.s)

    def test_bounded_quantifiers_leq_reduction(self):
        self.assertIn(r'$u\le t$', self.s)
        self.assertIn(r'\ref{res:4:6}', self.s)
        self.assertIn('jednej dodatkowej instancji', self.s)

    def test_implication_false_branch_explicit(self):
        self.assertIn(r'$\eta\to\theta$', self.s)
        self.assertIn(r'$\eta$ i $\neg\theta$', self.s)
        self.assertIn('gałąź ujemna', self.s)

    def test_empty_bounded_quantifier(self):
        for k in range(12):
            vals = [i % 3 == 1 for i in range(k)]
            self.assertEqual(all(vals), not any(not z for z in vals))
            self.assertEqual(any(vals), not all(not z for z in vals))
            if k == 0:
                self.assertTrue(all(vals))
                self.assertFalse(any(vals))
        self.assertIn('dla $k=0$', self.s)

    def test_compiler_pr_and_pa_induction(self):
        self.assertIn('Indukcja w PA formalizuje jej poprawność', self.s)
        self.assertIn('pierwotnie rekurencyjna', self.s)
        self.assertIn('Lemat~\\ref{lem:xi-append-beta}', self.s)

    def test_sigma1_and_d3(self):
        for x in ('lem:xi-delta-proofcompiler','lem:xi-formal-sigma1','thm:xi-hbl-verified'):
            self.assertIn(r'\label{'+x+'}',self.s)
        self.assertIn(r'\operatorname{Bew}_T(\overline g)\to',self.s)
        self.assertIn(r'\ref{lem:d1-provability}',self.s)
        self.assertIn(r'\ref{thm:xi-d2}',self.s)

    def test_no_new_claims_or_environments(self):
        self.assertEqual(self.s.count(r'\begin{twierdzenie}'), 2)
        self.assertEqual(self.s.count(r'\begin{lemat}'), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)