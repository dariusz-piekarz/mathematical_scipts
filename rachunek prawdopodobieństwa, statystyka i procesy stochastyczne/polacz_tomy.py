#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Łączy cztery tomy w jeden PDF i zastępuje GoToR zwykłymi linkami wewnętrznymi.

Wymagania: python -m pip install pymupdf
Użycie: python polacz_tomy.py
W katalogu wejściowym muszą leżeć rachunek_prawdopodobienstwa_tom_I.pdf, ..._II.pdf, ..._III.pdf, ..._IV.pdf.
"""
from __future__ import annotations
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
KEYS = ('I', 'II', 'III', 'IV')
INPUTS = {k: ROOT / f'rachunek_prawdopodobienstwa_tom_{k}.pdf' for k in KEYS}
OUTPUT = ROOT / 'Cztery_tomy_polaczone_aktywne_linki.pdf'
REMOTE_RE = re.compile(r'^rachunek_prawdopodobienstwa_tom_(I|II|III|IV)\.pdf#nameddest=(.+)$')


def main() -> None:
    for path in INPUTS.values():
        if not path.is_file():
            raise FileNotFoundError(path)
    sources = {k: fitz.open(str(path)) for k, path in INPUTS.items()}
    offsets: dict[str, int] = {}
    destinations = {k: src.resolve_names() for k, src in sources.items()}
    out = fitz.open()
    toc = []
    page_offset = 0
    titles = {'I': 'Rachunek prawdopodobieństwa',
              'II': 'Procesy stochastyczne',
              'III': 'Analiza stochastyczna',
              'IV': 'Statystyka matematyczna'}
    for key in KEYS:
        src = sources[key]
        offsets[key] = page_offset
        # Przenosimy strony bez linków, żeby wykluczyć nieobsługiwane przez część
        # przeglądarek akcje GoToR. Wszystkie linki utworzymy ponownie.
        out.insert_pdf(src, links=False, annots=False)
        toc.append([1, f'Tom {key} — {titles[key]}', page_offset + 1])
        for level, caption, pno in src.get_toc():
            toc.append([level + 1, caption, page_offset + pno])
        page_offset += len(src)
    counts = {'local': 0, 'cross_volume': 0, 'web': 0}
    for key in KEYS:
        src = sources[key]
        for page_index, page in enumerate(src):
            target_page = out[offsets[key] + page_index]
            for link in page.get_links():
                kind = link['kind']
                if kind == fitz.LINK_URI:
                    target_page.insert_link({'kind': fitz.LINK_URI, 'from': link['from'], 'uri': link['uri']})
                    counts['web'] += 1
                    continue
                if kind == fitz.LINK_NAMED:
                    dst_key = key
                    name = link.get('nameddest')
                    if name not in destinations[key]:
                        raise ValueError(f'Nie znaleziono lokalnego celu: {key}: {name}')
                    dest = destinations[key][name]
                elif kind in (fitz.LINK_GOTOR, fitz.LINK_LAUNCH):
                    remote = REMOTE_RE.fullmatch(link.get('file', ''))
                    if remote is None:
                        raise ValueError(f'Nieznana postać linku do zewnętrznego pliku PDF: {link}')
                    dst_key, name = remote.groups()
                    if name not in destinations[dst_key]:
                        raise ValueError(f'Nie znaleziono celu: {dst_key}: {name}')
                    dest = destinations[dst_key][name]
                elif kind == fitz.LINK_GOTO:
                    dst_key = key
                    dest = {'page': link['page'], 'to': (link.get('to') or fitz.Point(0, 0))}
                    # LINK_GOTO ma już współrzędne po transformacji do osi pionowej strony.
                    dst_index = offsets[dst_key] + dest['page']
                    target_page.insert_link({'kind': fitz.LINK_GOTO,
                                             'from': link['from'], 'page': dst_index,
                                             'to': fitz.Point(*dest['to'])})
                    counts['local'] += 1
                    continue
                else:
                    raise ValueError(f'Nieobsługiwany rodzaj odsyłacza {kind}: {link}')
                # resolve_names() zwraca pozycję w układzie PDF: zero jest na dole.
                original_target_page = sources[dst_key][dest['page']]
                x, y_bottom_up = dest['to']
                destination = fitz.Point(x, original_target_page.rect.height - y_bottom_up)
                target_page.insert_link({
                    'kind': fitz.LINK_GOTO,
                    'from': link['from'],
                    'page': offsets[dst_key] + dest['page'],
                    'to': destination,
                    'zoom': 0,
                })
                counts['cross_volume' if dst_key != key else 'local'] += 1
    out.set_toc(toc)
    out.set_metadata({'title': 'Podstawy teorii prawdopodobieństwa i statystyki — Tomy I–IV',
                      'subject': 'Cztery tomy z odsyłaczami wewnętrznymi'})
    out.save(OUTPUT, garbage=4, deflate=True)
    out.close()
    with fitz.open(OUTPUT) as final:
        actual = {'local': 0, 'web': 0}
        for i, page in enumerate(final):
            for link in page.get_links():
                if link['kind'] == fitz.LINK_GOTO:
                    assert 0 <= link['page'] < len(final), (i, link)
                    actual['local'] += 1
                elif link['kind'] == fitz.LINK_URI:
                    actual['web'] += 1
                else:
                    raise AssertionError(f'W wydaniu łączonym pozostał niedziałający rodzaj linku: {i+1}, {link}')
        assert actual['local'] == counts['local'] + counts['cross_volume'], (actual, counts)
        assert actual['web'] == counts['web'], (actual, counts)
        print('Zbudowano:', OUTPUT)
        print('Strony:', len(final), 'odsyłacze:', actual, 'w tym międzytomowe:', counts['cross_volume'])


if __name__ == '__main__':
    main()
