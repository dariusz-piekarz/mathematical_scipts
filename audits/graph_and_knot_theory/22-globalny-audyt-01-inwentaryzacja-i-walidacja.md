# Teoria grafów i węzłów — audyt globalny 01: inwentaryzacja i walidacja korpusu

Data rozpoczęcia: 2026-11-23.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
Status: **AUDYT GLOBALNY W TOKU** — nie jest to raport stabilizacji całości.

## Punkt startowy

Główna książka: \`books/pl/graph_and_knot_theory.tex\`.
Katalog Atlasu: \`catalog/books.json\`, wpis \`graph_and_knot_theory\`.
Zidentyfikowano **44 pliki rozdziałów** \`00–43\`. Rzeczywisty porządek \`\\input\` ma postać \`00–05, 37–43, 06–36\` — nowe moduły teoretyczno-algorytmiczne wstawiono w obręb historycznej sekwencji źródeł. Wymaga to osobnej oceny redakcyjnej (numer pliku źródłowego nie jest numerem drukowanego rozdziału); nie należy teraz naruszać zatwierdzonego porządku przez automatyczne sortowanie.

Moduły 37–43 mają osobne raporty stabilizacji i testy. **Nie stanowi to jednak audytu całości**: moduły historyczne 00–36 obejmują w szczególności podstawy teorii grafów, macierze incydencji i Laplasjan, planarne grafy i kolorowania, zagadnienia topologiczne, teorię węzłów, 3- i 4-rozmaitości, chirurgię oraz teorię Seiberga–Wittena.

## Zadania tego etapu

1. Utworzyć nowy niezależny test \`tools/tests/test_graph_and_knot_global.py\`, który przegląda **wszystkie** pliki \`\\input\`, porównuje katalog Atlasu i rzeczywiste pliki na dysku, kontroluje unikalność etykiet, brak nierozwiązanych odsyłaczy, strukturę środowisk LaTeX, terminologię i potencjalnie dublowane 18-wyrazowe fragmenty.
2. Dla każdego rozdziału zliczyć definicje, twierdzenia/lematy, dowody, ilustracje, etykiety, referencje i sekcje; wynik zachować jako JSON, aby kolejne iteracje audytu miały mierzalny stan.
3. Uruchomić **rzeczywistą kompilację całej 44-rozdziałowej książki**, a nie wybranych 13 rozdziałów: \`pdflatex\` trzy razy, kontrola ostrzeżeń, odsyłaczy, przepełnień, stron i tekstu PDF. Zachować również artefakty niepowodzeń.
4. Porównać nowe zagadnienia Laplasjanu i widma w rozdziale 43 z historycznym rozdziałem 08: są matematycznie związane, ale rozdział 08 wprowadza ważony Laplasjan kombinatoryczny \`BWB^T\`, a rozdział 43 normalizację \`I-A/d\` dla grafu \`d\`-regularnego. Przy dalszej redakcji należy dodać jawny most między konwencjami i eliminować powtórzenia bez utraty dowodów.
5. Rozpocząć audyty matematyczne starszych rozdziałów w sposób systematyczny, jeden blok naraz, i nie nadawać globalnego statusu stabilności przed szczegółowym przejściem przez wszystkie dowody i diagramy.

## Pierwsza poprawka

Strona tytułowa książki przed audytem twierdziła, że jest to „wersja po audycie globalnym”, mimo braku raportu i pełnego testu wszystkich rozdziałów. Zmieniono na „globalny audyt w toku”, aby status nie wyprzedzał rzeczywistej kontroli.

## Warunek zakończenia iteracji

Wyniki świeżego GitHub Actions dla obu zadań: \`structural-audit\` i \`full-book-pdf\`, a następnie kolejny raport z wykrytymi problemami, ich klasyfikacją i rzeczywistymi poprawkami. Zielony build pełnego PDF nie zastępuje merytorycznej kontroli wszystkich historycznych dowodów.
