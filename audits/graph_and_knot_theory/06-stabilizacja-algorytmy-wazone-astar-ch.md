# Teoria grafów i węzłów — stabilizacja rozdziału o algorytmach ważonych (A*, CH)

Data: 2026-11-23.
Zakres: \`chapters/pl/graph_and_knot_theory/38-najkrotsze-drogi-wazone-i-algorytmy-wyszukiwania-tras.tex\`, rozdział 7 w składzie książki.
Status: **STABILNY PO AUDYTACH 01–02**, na poziomie tego rozdziału i jego zależności. Nie oznacza stabilizacji całego tomu.

## Stan wersji poddanej pełnym kontrolom

Commit źródeł: [33d8d1056b8d5211a7f9eb88a6766b769f98bcfc](https://github.com/dariusz-piekarz/mathematical_scipts/commit/33d8d1056b8d5211a7f9eb88a6766b769f98bcfc).

[GitHub Actions — kontrola algorytmów i PDF](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45140774379):
- \`finite-models\`: success;
- \`chapter-pdf\`: success.

[GitHub Actions — kontrola aplikacji Atlas](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45140774315): success.
[GitHub Actions — terminologia polska](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45140774507): success.

## Wyniki kontroli niezależnej

Test \`tools/tests/test_graph_and_knot_weighted.py\` sprawdził:
- 4113 wyczerpująco generowanych małych grafów skierowanych o wagach nieujemnych, z kontrolą Dijkstry, Bellmana--Forda, Floyda--Warshalla, A* i dwukierunkowej Dijkstry;
- 1750 deterministycznie generowanych grafów o wagach także ujemnych, w tym z osiągalnymi cyklami ujemnymi;
- 1190 deterministycznie generowanych grafów dla A* z dopuszczalnymi, potencjalnie niespójnymi heurystykami oraz jawny kontrprzykład konieczności ponownego otwierania;
- 760 grafów nieskierowanych z wagami dodatnimi w kontroli dokładności CH dla wszystkich kolejności rang.
Równocześnie przeszły stare testy BFS/DFS: 1099 grafów prostych nieskierowanych i 4165 grafów skierowanych bez pętli.

## Kontrola tekstu i składu

- Podano pełne dowody Dijkstry, Bellmana--Forda, Floyda--Warshalla, A*, wersji A* z ponownym otwieraniem, poprawnego warunku zatrzymania Dijkstry dwukierunkowej oraz dokładności CH w modelu nieskierowanym z dodatnimi wagami.
- Uściślono warunki stosowalności: wagi nieujemne, cykle ujemne, dopuszczalność i spójność heurystyki; CH z preprocessingiem nie jest uniwersalnie najszybszym algorytmem.
- Podłączono nowy rozdział 38 po BFS/DFS w książce i \`catalog/books.json\` (39 plików źródłowych).
- Dwuprzebiegowa kompilacja fragmentu 00–05+37+38: PDF ma **46 stron**; sprawdzono log: brak \`Overfull\` i ostrzeżeń \`LaTeX Warning\`.
- Obejrzano wizualnie ostatnie strony zawierające cały nowy rozdział (rysunek, formuły, dowody, spis metod). Po zastąpieniu ciasnej tabeli listą i doprecyzowaniu dowodów układ jest czytelny, bez kolizji.
- PDF pochodzi z artefaktu \`graph-and-knot-weighted-algorithms-pdf\` przebiegu 45140774379.

## Ograniczenia statusu

To **stabilizacja modułu** po iteracjach niezależnych audytów, a nie matematyczna formalizacja w Lean ani dowód wolny od wszelkiej możliwości błędu.
Skład potwierdzono dla fragmentu 00–05+37+38, nie dla pełnego tomu 36 wcześniejszych rozdziałów.

## Następny krok

Dopiero teraz przejść do osobnego modułu **minimalnych drzew rozpinających: Prim, Kruskal, DSU oraz dowody własności przekroju i cyklu**, następnie wielokrotne audyty i testy; kolejny moduł dopiero po stabilizacji.
