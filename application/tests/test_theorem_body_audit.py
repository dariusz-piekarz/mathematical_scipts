import unittest
from backend.generator import theorem_environment_audit

class BodyTheoremAuditTests(unittest.TestCase):
    def test_body_definition_prevents_duplicate_import(self):
        result=theorem_environment_audit({'A':'', 'B':r'\newtheorem{lemma}{Lemat}[chapter]'},['A','B'],
            {'A':r'\newtheorem{lemma}{Lemat}[chapter]\begin{lemma}X\end{lemma}', 'B':''})
        self.assertEqual(result['additions'],[])
        self.assertEqual(len(result['body_declarations']),1)
        self.assertEqual(result['unresolved'][0]['reason'],'repeated_declaration_across_sources')

    def test_body_preamble_conflict_is_reported(self):
        result=theorem_environment_audit({'A':'', 'B':r'\newtheorem{lemma}{Lemat}[chapter]'},['A','B'],
            {'A':r'\newtheorem{lemma}{Twierdzenie}[section]\begin{lemma}X\end{lemma}', 'B':''})
        self.assertEqual(result['additions'],[])
        self.assertEqual(result['conflicts'][0]['reason'],'body_preamble_definition_mismatch')

    def test_comments_and_verbatim_ignored(self):
        result=theorem_environment_audit({'A':''},['A'],{'A':r'% \newtheorem{foo}{Foo}'+'\n'+r'\begin{verbatim}\newtheorem{bar}{Bar}\end{verbatim}'})
        self.assertEqual(result['body_declarations'],[])

if __name__=='__main__':unittest.main()