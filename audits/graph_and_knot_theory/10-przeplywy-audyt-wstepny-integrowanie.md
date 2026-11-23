# Audyt wstępny — algorytmy przepływowe, iteracja 01

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: NOWY / DO STABILIZACJI**.

## Kontrola zależności

Przejrzano \`04-spojnosc-przekroje-i-twierdzenie-mengera.tex\`:
- definicję sieci, przepływu i przekroju, a także dopuszczenie łuków przeciwnych;
- lemat wartości przepływu przez przekrój \`lem:tg-cutbound\`;
- sieć resztową z rozróżnianiem identyfikatorów przejść, w tym równoległych;
- twierdzenie \`thm:tg-maxflow\` dla całkowitych przepustowości i wynikowe twierdzenie Mengera.
Nie powielono tych podstaw. Nowy rozdział rozwija je algorytmicznie i daje uogólnienie na przepustowości rzeczywiste.

## Zakres nowego rozdziału

Plik \`chapters/pl/graph_and_knot_theory/40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex\`:
- niezmiennik powiększenia przepływu i certyfikat optymalności;
- uogólnienie maksymalny przepływ / minimalny przekrój na pojemności rzeczywiste przez zwartość zbioru przepływów;
- Ford--Fulkerson: poprawność i ograniczenie pseudowielomianowe dla pojemności całkowitych, ograniczenie przy niewymiernych;
- przykład pokazujący konieczność przejść wstecznych;
- Edmonds--Karp: BFS i dowód wielomianowości dla wszystkich pojemności rzeczywistych;
- Dinic: sieci warstwowe, przepływ blokujący, wzrost odległości i oszacowanie \`O(n^2(m+1))\`;
- odzyskanie minimalnego przekroju i arytmetyka dokładna;
- dwa rysunki TikZ, przykłady i analiza złożoności.

## Testy

Dodano niezależny test \`tools/tests/test_graph_and_knot_flow.py\`:
- weryfikacja maksymalnego przepływu przez wyczerpujące wyliczanie wszystkich przekrojów \`s,t\` (nie przez porównywanie wyłącznie algorytmów);
- trzy algorytmy: Ford--Fulkerson, Edmonds--Karp i Dinic;
- całkowitoliczbowe oraz wymierne pojemności (\`fractions.Fraction\`), łuki przeciwne i równoległe, przypadki zerowe, niespójne, przypadki wymagające anulowania wcześniejszego przepływu;
- automatyczna kontrola ograniczeń przepustowości, bilansów każdego wierzchołka, certyfikatu przekroju i niemalejących odległości resztowych w Edmondsie--Karpie;
- zgodność \`catalog/books.json\` z kolejnością 41 źródeł książki.

Rozszerzono dotychczasowy workflow grafowy o testy oraz dwuprzebiegowy skład PDF fragmentu książki 00–05+37+38+39+40 z weryfikacją odsyłaczy, poprawności kompilacji i zakazem przepełnień.

## Do wykonania

Pierwszy rzeczywisty przebieg CI, inspekcja obu rysunków w PDF,
niezależna kontrola dowodów i ich przypadków brzegowych,
poprawki, ponowny przebieg, a dopiero po sukcesie stabilizacja.
Nie oznaczać obecnej wersji jako stabilnej.
