import sys
import unittest
from pathlib import Path
from scripts.benchmark_process_resources import benchmark, ROOT

@unittest.skipUnless(sys.platform == 'linux', 'Linux resource metrics')
class ProcessResourceBenchmarkTests(unittest.TestCase):
    def test_isolated_child(self):
        result = benchmark(ROOT/'data'/'biblioteka.db', sizes=(1,), timeout=30)
        row = result['results'][0]
        self.assertEqual(row['exit_code'], 0, row)
        self.assertGreater(row['maxrss_kib_linux'], 0)
        self.assertGreater(row['zip_bytes'], 0)
        self.assertGreaterEqual(row['cpu_user_s'], 0)

    def test_invalid_arguments(self):
        for sizes, timeout in [((), 10), ((0,), 10), ((76,), 10), ((True,), 10), ((1,), 0), ((1,), 301)]:
            with self.subTest(sizes=sizes, timeout=timeout), self.assertRaises(ValueError):
                benchmark(ROOT/'data'/'biblioteka.db', sizes=sizes, timeout=timeout)