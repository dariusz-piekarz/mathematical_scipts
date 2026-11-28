# AA-08 — audyt V, 21 listopada 2026

**Wynik:** piąta niezależna iteracja, bez nowych błędów matematycznych, językowych, odsyłaczy ani problemów wizualnych. Rozdział "Grupy abelowe, torsja i iloczyn tensorowy" jest stabilny po audycie V. Źródło pozostało identyczne bajtowo z audytem IV, SHA-256: `3d7cbbb8b0d615ed6ce674a874061c0149e2c4681bde7cc69dbd89db40fe83ff`.

## Zakres
Sprawdzono 12 istniejących dowodów, wszystkie definicje, twierdzenia i przykłady; dopuszczalny brak zależności od nieudowodnionej w tym rozdziale klasyfikacji skończonych grup abelowych; rozkład torsji na p-składniki, grupę Prüfera, własność uniwersalną i naturalność iloczynu tensorowego. 31 unikatowych etykiet, 12 dowodów, brak nowych twierdzeń i lematów. Brak zmian źródłowych w audycie V.

## Lokalna walidacja
- 38/38 niezależnych testów audytowych PASS.
- 38/38 testów przygotowanych do struktury repozytorium PASS.
- Kompilacja pierwszych 8 rozdziałów: PASS, 64 strony. Pozostaje tylko znany wyprzedzający odsyłacz `aa:ch:module-tensor-product` do AA-18.
- Kompilacja 74 rozdziałów: PASS, 463 strony, 1411 unikatowych etykiet, 954 odsyłacze i brak brakujących celów.
- Wizualna kontrola 7 stron AA-08: PASS (bez uciętych wzorów i nieczytelnych rysunków).
- Starsze ostrzeżenia hyperref i Underfull w pozostałych rozdziałach poza AA-08 nadal występują.

## Integracja GitHub
AA-08 dołączono jako ósmy stabilny rozdział do `catalog/books.json` i `books/pl/abstract_algebra.tex`. Zaktualizowano workflow i dodano testy do `tools/tests/test_abstract_algebra_ch08.py`. Dwa poprzednio dopuszczane odsyłacze wyprzedzające do AA-08 są teraz rozwiązywane bez wyjątków; pozostawiono wyłącznie jeden jawny wyjątek do AA-18. Historyczne uwagi globalnego walidatora innych modułów nadal pozostają odrębnym zagadnieniem. Wynik GitHub Actions należy zweryfikować po commicie.

## Zbiorczy status

| Rozdział | Liczba audytów | Status | GitHub/CI |
|---|---:|---|---|
| AA-01 — Grupy i podgrupy | 5 | Stabilny | PASS |
| AA-02 — Warstwy i grupy ilorazowe | 3 | Stabilny | PASS |
| AA-03 — Działania grup | 3 | Stabilny | PASS |
| AA-04 — Cauchy i Sylow | 2 | Stabilny | PASS |
| AA-05 — Szeregi i nilpotentność | 3 | Stabilny | PASS |
| AA-06 — Rozszerzenia grup | 2 | Stabilny | PASS |
| AA-07 — Grupy wolne | 2 | Stabilny | PASS |
| AA-08 — Grupy abelowe | 5 | Stabilny, po bezusterkowym audycie V | CI do sprawdzenia |

**Łącznie:** 8/74 rozdziały stabilne, 25 audytów.
