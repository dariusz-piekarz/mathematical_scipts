"""Inspect rendered R04 PDF text boxes and the Cantor drawing's caption.

Usage: python3 test_measure_theory_ch04_pdf_layout.py ch04_bbox.html
The parser validates *text* bounds and the axis-caption separation; it is
not a substitute for visually reviewing the TikZ fills or all pages.
"""
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

NAMESPACE = "{http://www.w3.org/1999/xhtml}"


def inspect_bbox(filename):
    root = ET.parse(filename).getroot()
    pages = root.findall(f".//{NAMESPACE}page")
    assert pages, "PDF has no pages"
    word_count = 0
    captions = []
    for number, page in enumerate(pages, 1):
        width = float(page.get("width"))
        height = float(page.get("height"))
        words = []
        for word in page.iter(f"{NAMESPACE}word"):
            xmin, ymin = float(word.get("xMin")), float(word.get("yMin"))
            xmax, ymax = float(word.get("xMax")), float(word.get("yMax"))
            assert 0 <= xmin <= xmax <= width, (number, word.text, "x")
            assert 0 <= ymin <= ymax <= height, (number, word.text, "y")
            words.append((word.text or "", xmin, ymin, xmax, ymax))
        word_count += len(words)
        for idx in range(len(words)-3):
            if [w[0] for w in words[idx:idx+4]] != [
                "Pierwsze", "cztery", "etapy", "konstrukcji"
            ]:
                continue
            caption_y = words[idx][2]
            ones = [w for w in words if w[0] == "1"
                    and w[1] > width * .6
                    and caption_y - 75 < w[2] < caption_y]
            zeros = [w for w in words if w[0] == "0"
                     and width * .1 < w[1] < width * .5
                     and caption_y - 75 < w[2] < caption_y]
            axis_pairs = [(o, one) for o in zeros for one in ones
                          if one[1] > o[3] + 40
                          and abs(o[2] - one[2]) < 3
                          and caption_y - max(o[4], one[4]) > 5]
            assert axis_pairs, (
                f"Cantor caption not separated from both axis labels "
                f"on page {number}"
            )
            captions.append(number)
    assert len(captions) == 1, f"expected one Cantor caption: {captions}"
    print(f"PASS {len(pages)} pages, {word_count} bounded words; "
          f"Cantor caption separated on page {captions[0]}")


if __name__ == "__main__":
    assert len(sys.argv) == 2, "provide pdftotext -bbox XHTML path"
    inspect_bbox(Path(sys.argv[1]))
