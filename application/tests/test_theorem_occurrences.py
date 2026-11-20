import unittest
from backend.generator import theorem_environment_audit, theorem_declaration_occurrences

class OccurrenceTests(unittest.TestCase):
    def test_duplicate_in_single_body(self):
        body='\\newtheorem{lemma}{Lemma}\\n\\newtheorem{lemma}{Lemma}'
        result=theorem_environment_audit({'A':''}, ['A'], {'A':body})
        self.assertTrue(any(x['reason']=='repeated_declaration_within_source' for x in result['unresolved']))

    def test_grouped_declaration_warning(self):
        body='{\\newtheorem{lemma}{Lemma}}'
        result=theorem_environment_audit({'A':''}, ['A'], {'A':body})
        self.assertTrue(any(x['reason']=='declaration_inside_brace_group' for x in result['unresolved']))

    def test_comments_not_counted(self):
        source='% \\newtheorem{lemma}{Lemma}\n\\newtheorem{lemma}{Lemma}'
        self.assertEqual(len(theorem_declaration_occurrences(source)),1)