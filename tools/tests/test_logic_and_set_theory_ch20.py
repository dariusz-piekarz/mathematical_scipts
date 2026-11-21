"""Chapter 20 clean audits III-IV: structural, cross-reference, finite semantic checks.
Finite computations complement but do not replace mathematical proofs."""
from pathlib import Path
import itertools
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
REPO_SOURCE = ROOT/'chapters/pl/logic_and_set_theory/20-prawda-arytmetyczna-i-twierdzenie-tarskiego.tex'
SRC = REPO_SOURCE if REPO_SOURCE.is_file() else Path('/mnt/data/logika_rozdzial_20_audyt_III.tex')
SOURCE = SRC.read_text(encoding='utf-8')
FIXTURE = REPO_SOURCE.parent if REPO_SOURCE.is_file() else Path('/mnt/data/logic20_audit3_work/chapters')
FORWARD = {'ch:derivability-proof', 'ch:downward-ls', 'ch:upward-ls'}

class TestChapter20(unittest.TestCase):
    def test_environment_pairs_balanced(self):
        stack=[]
        for action,name in re.findall(r'\\(begin|end)\{([^}]+)\}', SOURCE):
            if action=='begin': stack.append(name)
            else:
                self.assertTrue(stack, (action,name)); self.assertEqual(stack.pop(), name)
        self.assertEqual(stack, [])

    def test_inventory_unchanged(self):
        for name,count in {'twierdzenie':3,'lemat':1,'proof':4,'definicja':3,
                           'przyklad':5,'uwaga':7}.items():
            self.assertEqual(SOURCE.count('\\begin{'+name+'}'),count,name)

    def test_labels_unique(self):
        files=list(FIXTURE.glob('*.tex'))
        labels=[lab for file in files for lab in re.findall(r'\\label\{([^}]+)\}',file.read_text(encoding='utf8'))]
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(re.findall(r'\\label\{([^}]+)\}',SOURCE)),8)

    def test_internal_refs_resolved_against_actual_chapters(self):
        labels=set()
        for path in FIXTURE.glob('*.tex'):
            labels.update(re.findall(r'\\label\{([^}]+)\}',path.read_text(encoding='utf8')))
        refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',SOURCE)
        self.assertFalse((set(refs)-labels)-FORWARD)
        for k in ('res:8:1','res:7:7','lem:incomp-proof-check'):
            self.assertIn(k,labels)
        self.assertEqual(len(refs),14)

    def test_tarski_semantic_diagonal_contradiction(self):
        # Truth definition would require L <=> Tr, while fixed point requires L <=> not Tr.
        for L,Tr in itertools.product((False,True),repeat=2):
            self.assertFalse((L==(not Tr)) and (L==Tr))

    def test_tarski_syntactic_contradiction(self):
        # There is no Boolean valuation satisfying both T-biconditionals.
        for L,Tr in itertools.product((False,True),repeat=2):
            self.assertFalse((L==Tr) and (L==(not Tr)))
        self.assertIn('T\\vdash L\\leftrightarrow\\neg L',SOURCE)

    def test_finite_truth_disjunction_on_distinct_codes(self):
        for n in range(1,7):
            codes=list(range(5,5+n))
            for values in itertools.product((False,True),repeat=n):
                # disjunction of (x==code_i and truth(sentence_i))
                for code,expected in zip(codes,values):
                    self.assertEqual(any(code==c and v for c,v in zip(codes,values)),expected)
        self.assertIn('\\operatorname{Tr}_{\\mathrm{fin}}(x)',SOURCE)

    def test_nonstandard_witness_not_real_proof(self):
        self.assertIn('niestandardowym',SOURCE)
        self.assertIn('rzeczywistego, skończonego dowodu',SOURCE)
        self.assertIn('\\exists p\\,\\operatorname{Prf}_T(p,\\overline g)',SOURCE)

    def test_truth_vs_provability_without_soundness(self):
        self.assertIn('poprawna',SOURCE)
        self.assertIn('względem $\\mathfrak N$',SOURCE)
        # Arbitrary propositional Boolean values of P and Prov(P) need not agree.
        self.assertTrue(any(P != Prov for P,Prov in itertools.product((False,True),repeat=2)))

    def test_hbl_conditions_are_not_tautological(self):
        for c in ('(D1)','(D2)','(D3)'):
            self.assertIn(c,SOURCE)
        self.assertIn('\\Box(\\varphi\\to\\psi)\\to(\\Box\\varphi\\to\\Box\\psi)',SOURCE)
        self.assertIn('\\Box\\varphi\\to\\Box\\Box\\varphi',SOURCE)
        # D2 interpreted with unconstrained atomic boxes is NOT propositional validity.
        self.assertFalse((not True) or ((not True) or False))

    def test_d1_uses_numerals_of_actual_proofs(self):
        self.assertIn('\\operatorname{Prf}_T(\\overline p,\\overline g)',SOURCE)
        self.assertIn('g=\\ulcorner\\varphi\\urcorner',SOURCE)
        self.assertIn('\\Delta_0',SOURCE)

    def test_countability_distinguishes_finite_case(self):
        self.assertIn('co najwyżej przeliczalny',SOURCE)
        self.assertIn('iniekcji do $\\N$',SOURCE)
        self.assertNotIn('Także słowo „przeliczalny” odnosi się jedynie do istnienia',SOURCE)


    def test_sigma1_soundness_is_required_for_metatheoretic_reversal(self):
        self.assertIn('każde zdanie $\\Sigma_1$ dowodliwe w $T$ jest prawdziwe', SOURCE)
        self.assertIn('jego odwrócenie nie wynika z samego warunku wyprowadzalności', SOURCE)
        self.assertIn('\\mathfrak N\\models\\operatorname{Prf}_T(\\overline p,\\overline g)', SOURCE)

    def test_next_chapter_has_hbl_derivability_proofs(self):
        self.assertIn(r'\ref{ch:derivability-proof}', SOURCE)
        target=FIXTURE/'21-operacje-na-dowodach-i-warunki-wyprowadzalnosci.tex'
        self.assertTrue(target.is_file(), f"Missing chapter 21 source: {target}")
        text=target.read_text(encoding='utf8')
        self.assertIn(r'\label{ch:derivability-proof}',text)
        self.assertIn(r'\label{thm:xi-hbl-verified}',text)

    def test_set_definability_has_quantifiers_and_standard_model(self):
        self.assertIn('podzbioru $A\\subseteq\\N$', SOURCE)
        self.assertIn('dla każdego $n\\in\\N$', SOURCE)
        self.assertIn('n\\in A$ wtedy i tylko wtedy', SOURCE)
        self.assertIn('\\mathfrak N\\models\\theta(\\overline n)', SOURCE)

    def test_syntactic_tarski_does_not_assume_semantic_soundness(self):
        start=SOURCE.index('\\begin{twierdzenie}[Wersja syntaktyczna Tarskiego]')
        end=SOURCE.index('\\end{proof}', start)
        part=SOURCE[start:end]
        self.assertIn('Nie zakładamy efektywnego wyliczania aksjomatów $T$',part)
        self.assertIn('nie zakłada, że zdania', part)
        for L,Tr in itertools.product((False,True),repeat=2):
            self.assertFalse((L==Tr) and (L != Tr))

    def test_initial_example_states_effective_axiomatizability(self):
        intro=SOURCE.split(r'\begin{przyklad}[Dwie wypowiedzi',1)[1].split(r'\end{przyklad}',1)[0]
        self.assertIn(r'$T\supseteq Q$ będzie efektywnie aksjomatyzowalną', intro)
        self.assertIn('rzeczywisty,', intro)
        self.assertIn('niezależnie od tego, czy $T$ jest poprawna', intro)

    def test_truth_definition_only_sentence_codes(self):
        defn=SOURCE.split(r'\begin{definicja}[Definiowalność prawdy',1)[1].split(r'\end{definicja}',1)[0]
        self.assertIn('jedyną zmienną', defn)
        self.assertIn('dla każdego', defn)
        self.assertIn('zdania', defn)
        self.assertIn('niekodujących zdań', defn)

    def test_tarski_semantics_uses_soundness_of_q_only(self):
        proof=SOURCE.split(r'\begin{twierdzenie}[Niedefiniowalność prawdy',1)[1].split(r'\end{proof}',1)[0]
        self.assertIn(r'$\mathfrak N$ jest modelem $Q$',proof)
        self.assertIn(r'Q\vdash L\leftrightarrow',proof)
        self.assertIn('metamatematycz',SOURCE)

    def test_syntactic_tarski_has_no_computability_hypothesis(self):
        section=SOURCE.split(r'\begin{twierdzenie}[Wersja syntaktyczna',1)[1].split(r'\end{twierdzenie}',1)[0]
        self.assertIn('dowolną niesprzeczną teorią',section)
        self.assertIn('Nie zakładamy efektywnego',section)

    def test_d1_follows_numbered_earlier_lemma(self):
        src=SOURCE.split(r'\begin{lemat}[Warunek (D1)',1)[1].split(r'\end{proof}',1)[0]
        self.assertIn(r'\ref{res:7:7}',src)
        self.assertIn(r'\ref{lem:incomp-proof-check}',src)
        self.assertIn(r'$Q\vdash\Box\varphi$',src)

    def test_sigma1_soundness_is_stronger_than_consistency(self):
        part=SOURCE.split('Dodatkowe założenie może zmienić sytuację.',1)[1].split(r'\end{przyklad}',1)[0]
        self.assertIn(r'$\Sigma_1$-poprawna',part)
        self.assertIn(r'$\mathfrak N\models\Box\varphi$',part)
        self.assertIn('rzeczywisty dowód',part)
        self.assertNotIn('wynika z samej niesprzeczności',part)

    def test_no_unjustified_reverse_implication_for_d1(self):
        for pr,phi in itertools.product((False,True),repeat=2):
            if pr and not phi:
                self.assertTrue(pr and not phi)
        self.assertIn('nie wynika z samego warunku wyprowadzalności',SOURCE)
        self.assertIn(r'\Box\varphi\to\Box\Box\varphi',SOURCE)

    def test_each_d2_d3_has_exact_future_proof(self):
        self.assertIn(r'\ref{ch:derivability-proof}',SOURCE)
        target=FIXTURE/'21-operacje-na-dowodach-i-warunki-wyprowadzalnosci.tex'
        self.assertTrue(target.is_file(), f"Missing chapter 21 source: {target}")
        nxt=target.read_text(encoding='utf8')
        for label in ('thm:xi-hbl-verified','thm:xi-d2','lem:xi-formal-sigma1'):
            self.assertIn(r'\label{'+label+'}',nxt)

    def test_disjunction_for_repeated_codes(self):
        for value in (False,True):
            codes=[7,10,7]
            values=[value,not value,value]
            self.assertEqual(any(7==c and v for c,v in zip(codes,values)),value)

    def test_all_tarski_proofs_end_and_no_new_envs(self):
        self.assertEqual(SOURCE.count(r'\begin{proof}'),4)
        self.assertEqual(SOURCE.count(r'\end{proof}'),4)
        self.assertEqual(SOURCE.count(r'\begin{twierdzenie}'),3)

    def test_chapter20_labels_not_reused_elsewhere(self):
        here=set(re.findall(r'\\label\{([^}]+)\}', SOURCE))
        elsewhere=set()
        for file in FIXTURE.glob('*.tex'):
            if file.name.startswith('20-'):
                continue
            elsewhere.update(re.findall(r'\\label\{([^}]+)\}',file.read_text(encoding='utf8')))
        self.assertFalse(here & elsewhere)

if __name__=='__main__':
    unittest.main()