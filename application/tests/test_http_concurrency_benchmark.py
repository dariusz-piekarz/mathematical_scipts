import unittest
from scripts.benchmark_http_concurrency import benchmark

class HTTPConcurrencyBenchmarkTests(unittest.TestCase):
    def test_two_parallel_requests(self):
        result=benchmark(levels=(2,),requests_per_level=2)
        self.assertEqual(result['results'][0]['successes'],2)
        self.assertTrue(all(r['bytes']>0 for r in result['results'][0]['requests']))

    def test_invalid_parameters(self):
        for levels,requests in [((),2),((0,),2),((17,),2),((1,),0),((1,),65)]:
            with self.subTest(levels=levels,requests=requests), self.assertRaises(ValueError):
                benchmark(levels=levels,requests_per_level=requests)