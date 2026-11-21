"""Smoke test for repeatable, read-only generation measurements."""
import unittest
from pathlib import Path
from scripts.benchmark_generation import benchmark, ROOT

class BenchmarkGenerationTests(unittest.TestCase):
    def test_single_module_run(self):
        result = benchmark(ROOT/'data'/'biblioteka.db', sizes=(1,), repetitions=1)
        self.assertEqual(len(result['results']), 1)
        row = result['results'][0]
        self.assertEqual(row['modules'], 1)
        self.assertGreater(row['runs'][0]['zip_bytes'], 0)
        self.assertGreaterEqual(row['runs'][0]['total_s'], 0)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            benchmark(ROOT/'data'/'biblioteka.db', sizes=(0,), repetitions=1)
        with self.assertRaises(ValueError):
            benchmark(ROOT/'data'/'biblioteka.db', sizes=(1,), repetitions=0)

    def test_without_memory_tracing(self):
        result = benchmark(ROOT/'data'/'biblioteka.db', sizes=(1,), repetitions=1, measure_memory=False)
        self.assertFalse(result['memory_tracing'])
        self.assertIsNone(result['results'][0]['max_peak_bytes'])
        self.assertIsNone(result['results'][0]['runs'][0]['tracemalloc_peak_bytes'])
        self.assertGreater(result['results'][0]['runs'][0]['zip_bytes'], 0)