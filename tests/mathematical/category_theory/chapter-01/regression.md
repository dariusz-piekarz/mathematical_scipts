# CAT-01 — audyt I, rozszerzenie i kryteria regresyjne

Źródło: chapters/pl/category_theory/01-kategorie-i-ich-pierwsze-przyklady.tex
Commit 99348d9accf9e6a0b99ba10e588b28b707b96200, blob 10d01e7f6c3e95c65fd802e4230eaf4bd0e60a54.

## Wykonane zmiany
- Rozróżniono kolekcję obiektów, zbiory morfizmów, kategorie małe, lokalnie małe i duże; jawna relatywizacja do uniwersum Grothendiecka, bez zakładania istnienia dowolnie dużych uniwersów w ZFC.
- Dodano kategorie modułów lewostronnych nad dowolnym pierścieniem z jedynką i gładkich rozmaitości bez brzegu, z uzasadnieniami składania; kategorię konkretną i grupoid (jedyność odwrotności, grupoid par).
- Uzupełniono dowód łączności i identyczności w Rel, składanie ścieżek oraz aksjomaty kategorii przeciwnej.
- Zachowano wszystkie dotychczasowe etykiety. Nie kopiowano całych rozdziałów z innych skryptów.

## Mapa źródeł
- AA-16, blob 319cbac9af83a819e0d375fc282284c62638c3ac: definicja modułu i homomorfizmu; przykład wykorzystuje te pojęcia. Istnieje raport stabilizacji AA-16 III.
- DG-01, blob 8636e1a7477d6130b0387d71ec24bd1ec290e5ab: rozmaitości i gładkie odwzorowania; zaadaptowano przykład. Nie potwierdzono w tej iteracji CI DG.
- AT-04, blob 076025b2e3909cb03fa6b45221d69465e7eee775: drogi i homotopia; wskazano grupoid podstawowy, pełna konstrukcja w dalszej części. Nie przypisano źródłu dowodu ogólnego grupoidu.
- ALG-04, blob ab1344ed93a02bb757e5a78cb3833d6c4a18079c: schematy afiniczne; materiał odłożony do funktorów i zastosowań, bez przedwczesnego importu.

## Trwałe kryteria
| ID | Źródło | Metoda i kryterium |
|---|---|---|
| CAT-01-001 | Rel | Python + semantyczna: łączność i dwustronne jednostki |
| CAT-01-002 | cat:def:grupoid, cat:ex:grupoid | Python + semantyczna: typy, łączność, odwrotności i jednostki |
| CAT-01-003 | def:op | Python + semantyczna: odwrotna kolejność składania w nieprzemiennym modelu |
| CAT-01-004 | cat:ex:moduly-rozmaitosci | Python + semantyczna: lewa liniowość złożeń także dla pierścienia nieprzemiennego |
| CAT-01-005 | cały rozdział | Python: zachowanie etykiet, zagnieżdżenie środowisk |
| CAT-01-006 | cat:def:uniwersum, cat:rem:uniwersa | semantyczna: relatywizacja małości, domknięcia, brak nieuzasadnionego założenia ZFC |
| CAT-01-007 | cat:def:konkretna | semantyczna: zachowanie składania i identyczności, wierność na ustalonych hom-zbiorach |

Testy: tools/tests/test_category_theory_ch01.py (commit 5415eb5a99ea36b743c15eb67a692481bb3257ad). CI rozszerzone na wszystkie testy CAT (a50ae6debdcd14296241e6d9d8a6fa0e03bd8289). W tej iteracji sprawdzono zagnieżdżenie środowisk przy zapisie; wynik nowych testów Python i kompilacji niepotwierdzony. Nie wykonano formalizacji Lean.
Status: otwarty audyt stabilizacyjny; kolejna iteracja bez rozszerzeń.
