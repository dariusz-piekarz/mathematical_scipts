"""Prevent browser smoke tests from depending on historical index counts."""
import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent

class BrowserSmokeContractTests(unittest.TestCase):
    def test_module_count_is_dynamic(self):
        source = (ROOT / 'browser_e2e.py').read_text(encoding='utf-8')
        ast.parse(source)
        self.assertIn("re.compile(r'^\\d+ rozdziałów$')", source)
        self.assertNotIn("233 rozdziałów", source)

if __name__ == '__main__':
    unittest.main()
