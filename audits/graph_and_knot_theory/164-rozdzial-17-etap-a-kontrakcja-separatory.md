# Audyt 164 — drukowany rozdział 17, etap A (kontynuacja)

2026-11-24. Plan 118, poprzedni raport 163.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commity źródłowe: deb0e0abf51e82b5ffb6a604f84451f786595eff, 0acaf3eb89a36e4a64771d97da8472d0f3730ec3.
Commity regresji: 55e0bc24e04c3f5f87d1e2cfe33e733e05d7c138, 7d2b656d560b3ce294e588cc73ef281835d2f597.

## Zmiany
- Pełne kryterium kontrakcji krawędzi xy: graf po kontrakcji jest trójspójny wtedy i tylko wtedy, gdy każde usunięcie x,y,z pozostawia graf spójny. Rozpatrzono wszystkie zbiory usuwane w grafie po kontrakcji.
- Jawna rodzina trójek (xy,z,C) i minimalizacja po wszystkich składowych, nie tylko po separatorach.
- Rozdzielenie przypadków t=x, t=y oraz t różnego od x,y; uzasadnienie istnienia D oraz ścisłej inkluzji D w C.
- Dodatkowy wniosek: t należy do C lub {x,y}, ponieważ jako element drugiego separatora ma sąsiada w D.
- Ponowny odczyt zmian, 22 etykiety i poprawne zagnieżdżenie 57 par środowisk.

## Regresja
GKT-17-CONTRACT-02: test_gkt17_contraction_descent.js. Rzeczywiste wykonanie funkcji w JS: PASS; 3902 wystąpienia grafów trójspójnych, 48996 kontrakcji (34169 zachowujących, 14827 niezachowujących trójspójności), 37975 trójek z wyborem składowej, 15449 ścisłych zejść (13261 z t=x lub y, 2188 z t w C, 0 z t poza C i pierwszym separatorem). Wszystkie grafy etykietowane o 5 lub 6 wierzchołkach oraz 20000 deterministycznych próbek grafów o 7 wierzchołkach, z możliwymi powtórzeniami, filtrowanych według trójspójności. Pierwsza próba obejmująca wyłącznie n<=6 ujawniła niewystarczające pokrycie przypadków; zakres rozszerzono. Po wykonaniu dodano asercję outside===0 zgodną z odczytanym wynikiem; nie uruchomiono ponownie końcowego pliku po tej zmianie. Test nie jest dowodem formalnym.
Wcześniejszy test GKT-17-KUR-01 odczytano i porównano zakres; nie uruchamiano ponownie wcześniejszych regresji w tej iteracji.

## Stabilizacja
CI: zapytania dla ostatniego commitu źródłowego zwracają puste listy statusów i workflow. Brak pełnej kompilacji książki i oględzin PDF; nie potwierdzono usunięcia wcześniejszej blokady DNS. Etap A OTWARTY.
Wznowienie: kontrola odsyłaczy do rozdziału o grafach planarnych, lokalnego prostowania i obchodów ścianowych; pełny skład oraz CI/PDF przed zamknięciem A i niezależnym B.
