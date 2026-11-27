"""Regression checks for the actual figure-audit PNG validator."""
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from audit_graph_figure_previews import verify_png


class PngAuditTests(unittest.TestCase):
    def test_decode_and_reject_invalid_images(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "figure.png"
            Image.new("RGB", (16, 12), "red").save(path)
            verify_png(path)
            valid = path.read_bytes()
            for name, data in (
                ("signature only", valid[:8]),
                ("truncated", valid[:len(valid) // 2]),
                ("bad CRC", valid[:29] + bytes([valid[29] ^ 1]) + valid[30:]),
            ):
                with self.subTest(name=name):
                    path.write_bytes(data)
                    with self.assertRaises((OSError, ValueError, SyntaxError)):
                        verify_png(path)
            Image.new("RGB", (16, 12)).save(path, format="JPEG")
            with self.assertRaises(ValueError):
                verify_png(path)


if __name__ == "__main__":
    unittest.main()
