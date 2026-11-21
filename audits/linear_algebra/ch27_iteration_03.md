# Algebra liniowa — rozdział 27, audyt III (poprawka kompilacji)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`.  
**Blob po korekcie:** `53f829322b3a921b52a766c08363b298a4c31293`.

## Rozpoznanie

Pełny przebieg [44951715486](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44951715486) zaliczył wszystkie regresje rozdziałów 01–27 (w tym test 6561 trójek 2×2 nad F3), ale **FAILURE** wystąpił w kompilacji LaTeX:

```text
.../27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex:756:
Undefined control sequence.
l.756 \mathscr H_{r,s}=
```

Preambuła książki nie dostarcza makra `\mathscr`; nie chcemy z tego powodu dokładać pakietu `mathrsfs` do całego repozytorium.

## Korekta

Wszystkie osiem wystąpień `\mathscr` dla macierzy Hankela zostało zastąpionych przez dostępne w dotychczasowej preambule `\mathcal`: używamy teraz oznaczenia `\mathcal H_{r,s}`. Definicja, rangowe kryterium minimalności, dokładny przykład, dowody i wyniki pozostają bez zmian. Zachowano wszystkie etykiety i odsyłacze.

## Decyzja

**Audyt III wykrył i naprawił usterkę kompilacji.** Nie jest czystym audytem; do stabilizacji potrzeba dwóch kolejnych czystych kontroli, zielonego CI i zweryfikowanego samodzielnego PDF.
