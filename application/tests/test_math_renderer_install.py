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
        chapter = Path(__file__).resolve().parents[2] / "chapters/pl/mathematical_analysis_i/36-calka-kurzweila-henstocka.tex"
        target = self.root.parent / "chapters/pl/mathematical_analysis_i" / chapter.name
        target.parent.mkdir(parents=True)
        shutil.copyfile(chapter, target)
        # Later declarations must not be visible in a header profile.
        (target.parent / "99-test.tex").write_text(
            r"\chapter{Fixture}" + "\n" + r"\providecommand{\R}{WRONG}" + "\n"
            + r"\providecommand{\localtest}[1]{\mathcal{#1}}" + "\n"
            + "Body text\n" + r"\newcommand{\late}{WRONG}", encoding="utf-8")
        self.addCleanup(patch.stopall)
        patch.object(renderer, "DEST", self.dest).start()

    def profiles(self):
        source = (self.dest.parent / "math-macro-profiles.js").read_text(encoding="utf-8")
        self.assertTrue(source.startswith("window.atlasMathMacroProfiles = "))
        return json.loads(source.removeprefix("window.atlasMathMacroProfiles = ").removesuffix(";\n"))

    def test_actual_preambles_and_conflicting_macros(self):
        renderer.write_macro_profiles()
        profiles = self.profiles()
        self.assertEqual({key for key in profiles if "-" not in key},
                         {p.stem for p in (self.root / "config/preambles").glob("*.tex")})
        self.assertEqual(profiles["DG"][r"\Q"], r"\mathbb{Q}")
        self.assertEqual(profiles["MOD"][r"\Q"], r"\mathrm Q")
        self.assertEqual(profiles["KAT"][r"\cat"], r"\mathsf{#1}")
        self.assertEqual(profiles["KAT"][r"\Hom"], r"\operatorname{Hom}")
        self.assertEqual(profiles["KAT"][r"\End"], r"\operatorname{End}")
        self.assertNotIn(r"\proofname", profiles["DG"])

    def test_chapter_header_macros_and_isolation(self):
        renderer.write_macro_profiles()
        profiles = self.profiles()
        for letter in "RCK":
            self.assertEqual(profiles["AM1"]["\\" + letter], r"\mathbb " + letter)
        chapter = profiles["AM1-36"]
        self.assertEqual(chapter[r"\HK"], r"\mathrm{KH}")
        self.assertEqual(chapter[r"\Var"], r"\operatorname{Var}")
        self.assertEqual(chapter[r"\ind"], r"\chi_{#1}")
        self.assertNotIn(r"\HK", profiles["AM1"])
        self.assertNotIn(r"\R", profiles["AM1-99"])
        self.assertNotIn(r"\late", profiles["AM1-99"])
        self.assertEqual(profiles["AM1-99"][r"\localtest"], r"\mathcal{#1}")

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
