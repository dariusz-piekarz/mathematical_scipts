"""Run unchanged mathematical assertions for FA 17–25 against DT sources."""
import os
from pathlib import Path
import subprocess
import sys
import unittest

from distribution_migration_sources import DT_MODE, MAP, SPLIT

HERE = Path(__file__).resolve().parent


class DistributionFoundationsRegression(unittest.TestCase):
    def test_inherited_chapter_regressions(self):
        env = dict(os.environ, **{DT_MODE: "1"})
        for chapter in (*MAP, *SPLIT):
            with self.subTest(historical_chapter=chapter):
                script = HERE / f"test_functional_analysis_ch{chapter:02d}.py"
                result = subprocess.run([sys.executable, str(script)], env=env,
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0,
                                 result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
