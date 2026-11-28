# Teoria grafów i węzłów — audyt wstępny rozdziału 41

Data: 2026-11-23.
Gałąź: biblioteka-matematyczna-iteracja-6.
**Status: WSTĘPNY — jeszcze nie ustabilizowano.**

## Zakres i brak dublowania

Sprawdzono rozdział 01 (definicje grafów prostych, klik, stopni, dwudzielności), spójność pliku głównego oraz katalogu Atlasu. Dotychczasowy skrypt nie ma osobnego opracowania twierdzenia Turána i liczb Ramseya. Dla zachowania rytmu pracy utworzono tylko jeden rozdział **ekstremalny**; modele grafów losowych i expandery pozostają na później.

Źródło: \`chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex\` (po historycznych 00–05 i czterech nowych modułach algorytmicznych, przed historycznym 06).

## Zawartość matematyczna

- \`ex(n,H)\`, rozróżnienie podgrafu od podgrafu indukowanego, definicja grafu Turána również dla \`n<r\`.
- Mantel: pełny dowód przez liczenie stopni i nierówność Cauchy'ego–Schwarza.
- Zykov: symetryzacja klas bliźniaków z dowodem zachowania zakazu kliki, bilansu liczby krawędzi i relacji bliźniaków.
- Turán: maksymalizacja liczby krawędzi, następnie sumy kwadratów klas bliźniaków i wyrównanie liczności części; przykład \`T_3(10)\` z 33 krawędziami.
- Ramsey: pełne twierdzenie skończone, indukcja i nierówność rekurencyjna, szacowanie dwumianowe, równoważna wersja dla kliki i zbioru niezależnego.
- Dokładne \`R(3,3)=6\`: dolne ograniczenie przez pięciocykl, górne przez rekurencję.
- Ramsey wielobarwny: konstrukcja indukcyjna przez grupowanie kolorów.
- Dwa rysunki TikZ: \`K_{3,3}\` oraz dwukolorowanie \`K_5\` oparte na \`C_5\`.

## Plan niezależnych kontroli

\`tools/tests/test_graph_and_knot_extremal.py\`:
1. Wyczerpująca enumeracja wszystkich grafów prostych na 0–6 wierzchołkach, pomiar \`ex(n,K_{r+1})\` dla \`r=1..5\` i porównanie z bezpośrednio skonstruowanym grafem Turána;
2. niezależna kontrola symetryzacji Zykowa na grafach na 2–5 wierzchołkach;
3. sprawdzenie wszystkich dwukolorowań \`K_5\` i \`K_6\` oraz dokładności \`R(3,3)\`;
4. testy brzegowe \`n=0\`, \`r>n\`, liczności części, duplikaty etykiet, struktura LaTeX i zgodność 42 plików źródłowych Atlasu.

Dotychczasowe regresje BFS/DFS, A*, CH, MST/DSU oraz przepływów nadal są uruchamiane. Workflow ma wykonać trzy przebiegi LaTeX, sprawdzić etykiety i wymusić brak przepełnień.

## Przed stabilizacją

Wymagane rzeczywiste wyniki CI, kontrola dowodów, wizualna inspekcja PDF (zwłaszcza pięciocyklu i grafu dwudzielnego), ewentualne poprawki i ponowne testy.
