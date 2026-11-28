# Algebra abstrakcyjna — AA-04, audyt II

Data: 21 listopada 2026. Rozdział „Twierdzenie Cauchy'ego i trzy twierdzenia Sylowa”. Ponowny audyt wszystkich sformułowań, dowodów, przykładów, założeń oraz odsyłaczy; bez rozszerzania materiału.

## Wynik

Nie znaleziono nowych błędów ani luk. Źródło AA-04 jest identyczne bajtowo z audytem I (SHA-256: `fe458301fa9779854027153b5690bb28754db4231cdafc4238a1dec938a0232e`). Zachowano 18 unikatowych etykiet, 12 dowodów i wszystkie istniejące twierdzenia, lematy, przykłady oraz definicje.

Kontrolowano dokładnie dowód Cauchy'ego także dla grup nieprzemiennych; kongruencję dwumianową; swobodne działanie stabilizatora z pierwszego twierdzenia Sylowa; zawieranie i sprzężoność w drugim twierdzeniu; argument z normalizatorem i punktem stałym w trzecim; przykład trzech różnych stabilizatorów S4; przykłady S3, A4 i nieprzemiennej grupy rzędu 21; grupy rzędu pq, rzędu 30 oraz normalność podgrup indeksu najmniejszego dzielnika pierwszego.

## Testy i kompilacja lokalna

- 20/20 PASS: testy poprzedniej iteracji plus przypadki brzegowe dla p niedzielącego rzędu grupy, grup p-potęgowych, nierozkładalności orbit i normalności podgrup małego indeksu.
- 20/20 PASS: testy zapisane w formacie repozytorium `tools/tests/test_abstract_algebra_ch04.py`.
- `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error audit_ch04.tex`: PASS, AA-01–AA-04, 35 stron, brak ostrzeżeń.
- `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error abstract_algebra.tex`: PASS, 74 rozdziały, 463 strony, bez brakujących odsyłaczy. Pozostały cztery ostrzeżenia hyperref i jedno Underfull hbox spoza AA-04.
- Kontrola wizualna ośmiu stron AA-04: PASS, bez kolizji i uciętych wzorów.

## Integracja

Dodano AA-04 do `catalog/books.json` oraz `books/pl/abstract_algebra.tex`, testy do `tools/tests` i etap testowy do GitHub Actions. Globalny walidator repozytorium raportuje wcześniejsze problemy spoza AA-04 i pozostaje diagnostyczny. Ostateczny wynik CI trzeba sprawdzić na commicie po pushu.
