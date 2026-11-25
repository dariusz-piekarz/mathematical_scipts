"""Offline regression of per-book math profiles and cached renderer installation."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from scripts import install_math_renderer as renderer


class MathRendererInstallTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "application"
        self.dest = self.root / "frontend/vendor/katex"
        preambles = Path(__file__).resolve().parents[1] / "config/preambles"
        shutil.copytree(preambles, self.root / "config/preambles")
        self.addCleanup(patch.stopall)
        patch.object(renderer, "DEST", self.dest).start()

    def profiles(self):
        source = (self.dest.parent / "math-macro-profiles.js").read_text(encoding="utf-8")
        self.assertTrue(source.startswith("window.atlasMathMacroProfiles = "))
        return json.loads(source.removeprefix("window.atlasMathMacroProfiles = ").removesuffix(";\n"))

    def test_actual_preambles_and_conflicting_macros(self):
        renderer.write_macro_profiles()
        profiles = self.profiles()
        self.assertEqual(set(profiles), {p.stem for p in (self.root / "config/preambles").glob("*.tex")})
        self.assertEqual(profiles["DG"][r"\Q"], r"\mathbb{Q}")
        self.assertEqual(profiles["MOD"][r"\Q"], r"\mathrm Q")
        self.assertEqual(profiles["KAT"][r"\cat"], r"\mathsf{#1}")
        self.assertEqual(profiles["KAT"][r"\Hom"], r"\operatorname{Hom}")
        self.assertEqual(profiles["KAT"][r"\End"], r"\operatorname{End}")
        self.assertNotIn(r"\proofname", profiles["DG"])

    def test_cached_install_refreshes_profiles_without_network(self):
        for name in renderer.REQUIRED + ("fonts/test.woff2",):
            target = self.dest / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"fixture")
        (self.dest / ".version").write_text(renderer.VERSION)
        with patch.object(renderer, "urlopen", side_effect=AssertionError("unexpected network")) as network:
            renderer.install()
            network.assert_not_called()
        self.assertIn("KAT", self.profiles())


if __name__ == "__main__":
    unittest.main()
