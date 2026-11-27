"""Check compiled measure-theory PDF; visual review remains separate."""
import argparse
import re
import sys
from pathlib import Path

INDEX_SOURCE = (Path(__file__).resolve().parents[1] /
                "chapters/pl/measure_theory/supplements/indeks_definicji_i_twierdzen.tex")


def expected_destinations(index_text, aux_text):
    """Match every source index label to its genuine hyperref destination."""
    labels = re.findall(r"(?m)^\s*\\hyperref\[([^\]\n]+)\]", index_text)
    if not labels or len(set(labels)) != len(labels):
        raise ValueError("Empty index or duplicate source index labels")
    wanted = set(labels)
    destinations = {}
    for line in aux_text.splitlines():
        match = re.match(r"^\\newlabel\{([^{}]+)\}", line)
        if not match or match[1] not in wanted:
            continue
        label = match[1]
        # Hyperref's five-field \newlabel record ends with the anchor and
        # external-document field. Titles can contain nested TeX groups.
        dest = re.search(r"\}\{(twierdzenie\.\d+\.\d+)\}\{[^{}]*\}\}\s*$", line)
        if not dest or label in destinations:
            raise ValueError(f"Invalid or duplicate AUX index label: {label}")
        destinations[label] = dest[1]
    missing = wanted - destinations.keys()
    if missing:
        raise ValueError(f"Missing AUX index labels: {sorted(missing)}")
    if len(set(destinations.values())) != len(wanted):
        raise ValueError("Distinct index labels share a PDF destination")
    return set(destinations.values())


def audit(filename, index_source=INDEX_SOURCE):
    import fitz

    try:
        expected_index = expected_destinations(
            Path(index_source).read_text(encoding="utf-8-sig"),
            Path(filename).with_suffix(".aux").read_text(encoding="utf-8-sig"),
        )
    except (OSError, ValueError) as exc:
        return [f"Cannot validate source/AUX index: {exc}"]
    errors = []
    with fitz.open(filename) as doc:
        outline = doc.get_toc()
        index_pages = [page for _, title, page in outline
                       if title == "Indeks definicji i twierdzeń"]
        if len(index_pages) != 1:
            return [f"Expected one index outline entry, got {index_pages}"]
        index_start = index_pages[0] - 1
        names = doc.resolve_names()
        seen_index = set()
        links = words_count = 0
        for i, page in enumerate(doc):
            words = page.get_text("words")
            words_count += len(words)
            for word in words:
                if (word[0] < -.1 or word[1] < -.1 or
                        word[2] > page.rect.width+.1 or word[3] > page.rect.height+.1):
                    errors.append(f"Page {i+1}: word outside page: {word[:5]}")
            grouped = {}
            for link in page.get_links():
                links += 1
                dest = link.get("nameddest")
                if dest and (dest not in names or not 0 <= names[dest]["page"] < len(doc)):
                    errors.append(f"Page {i+1}: unresolved named destination {dest}")
                if link["kind"] == fitz.LINK_GOTO and not 0 <= link.get("page", -1) < len(doc):
                    errors.append(f"Page {i+1}: invalid direct link {link}")
                if i >= index_start:
                    grouped.setdefault(dest, []).append(link)
            for dest, annotations in grouped.items():
                if not dest or not re.fullmatch(r"twierdzenie\.\d+\.\d+", dest):
                    errors.append(f"Page {i+1}: non-statement index destination {dest}")
                    continue
                if dest in seen_index:
                    errors.append(f"Page {i+1}: repeated index destination {dest}")
                seen_index.add(dest)
                link = min(annotations, key=lambda l: l["from"].y0)
                y = (link["from"].y0 + link["from"].y1)/2
                row = sorted((w for w in words if w[0] > .65*page.rect.width
                              and abs((w[1]+w[3])/2-y) < 3), key=lambda w:w[0])
                actual = [w[4] for w in row[-2:]]
                target_page = names.get(dest, {}).get("page", -1)
                if not 0 <= target_page < len(doc):
                    continue
                expected = [dest.split(".", 1)[1], doc[target_page].get_label()]
                if actual != expected:
                    errors.append(f"Page {i+1}: {dest}, printed {actual}, expected {expected}")
        for _, title, page in outline:
            if not 1 <= page <= len(doc):
                errors.append(f"Invalid bookmark target: {title} -> {page}")
        missing = expected_index - seen_index
        unexpected = seen_index - expected_index
        if missing:
            errors.append(f"Missing index destinations: {sorted(missing)}")
        if unexpected:
            errors.append(f"Unexpected index destinations: {sorted(unexpected)}")
        print(f"Pages: {len(doc)}; words: {words_count}; links: {links}; bookmarks: {len(outline)}; index destinations: {len(seen_index)}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    errors = audit(parser.parse_args().pdf)
    for error in errors:
        print("ERROR:", error)
    print(f"Preflight errors: {len(errors)}")
    sys.exit(bool(errors))
