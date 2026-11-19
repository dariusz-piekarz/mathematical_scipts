# Teoria miary (PL) — pełna wersja modularna

Moduł `books/pl/measure_theory.tex` składa przez `\input` 31 rozdziałów w `chapters/pl/measure_theory/`.
Rozdziały 1–30 pochodzą z wersji zredagowanej i audytowanej skryptu „Teoria miary” (19.11.2026).
Rozdział 31 to audytowany moduł „Dżety: od geometrii różniczkowej do teorii miary”
z zachowanym ujęciem geometrycznym i miarowym. Rozdział 28 zawiera odsyłacz do rozdziału 31.
Indeks i spis oznaczeń znajdują się w `chapters/pl/measure_theory/supplements/`.

**Oddzielny skrypt:** `books/pl/integration_theory.tex` z rozdziałami w `chapters/pl/integration_theory/`.
Obie książki pozostają odrębne: „Teoria całki” porównuje konstrukcje całek, a „Teoria miary”
rozwija aksjomaty i konstrukcje miar, przestrzenie Lp, miary Radona, miary Hausdorffa, area/coarea, BV i dżety.

Kompilacja z katalogu głównego repozytorium: `cd books/pl; pdflatex -interaction=nonstopmode -halt-on-error measure_theory.tex`
(uruchom trzykrotnie dla poprawnego spisu treści i odsyłaczy).