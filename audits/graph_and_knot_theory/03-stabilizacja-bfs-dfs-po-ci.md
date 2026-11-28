# Teoria grafów i węzłów — BFS/DFS: status stabilny po audycie 03

Data kontroli: 2026-11-23.

## Werdykt i zakres

**STABILNY W ZAKRESIE NOWEGO ROZDZIAŁU ALGORYTMICZNEGO**: \`chapters/pl/graph_and_knot_theory/37-algorytmiczne-przeszukiwanie-grafow-bfs-dfs.tex\`, jako szóstego rozdziału w złożonej książce. Ten status nie oznacza zakończenia matematycznego audytu pozostałych 36 dawnych rozdziałów ani kompilacji kompletnego tomu.

Stan kodu objętego testem: commit [171bf8806865d0d0a0c9372b9c506ebad5c8ca46](https://github.com/dariusz-piekarz/mathematical_scipts/commit/171bf8806865d0d0a0c9372b9c506ebad5c8ca46).

## Dowody wykonanych kontroli

- [GitHub Actions — przebieg końcowy 45138277758](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45138277758): **finite-models — success; chapter-pdf — success**.
- Testy niezależnych modeli: **1099 wszystkich grafów prostych nieskierowanych na 1–5 wierzchołkach** oraz **4165 wszystkich grafów skierowanych bez pętli na 1–4 wierzchołkach**. Kontrolowano BFS przez relaksację odległości, mosty przez usuwanie krawędzi, wykrywanie cykli nieskierowanych przez wzór \`m>n-c\`, dwudzielność przez wszystkie kolorowania, wykrywanie skierowanych cykli przez algorytm Kahna oraz topologiczny porządek według czasów kończenia DFS.
- Katalog Atlasu \`catalog/books.json\` zgadza się dokładnie z kolejnością \`\\input\` książki: 38 plików źródłowych (rozdziały 00–36 i nowy plik 37).
- Dwuprzebiegowa kompilacja \`pdflatex\` izolowanego fragmentu **00–05 + 37** zakończona sukcesem: 40-stronicowy PDF, zarejestrowane etykiety \`ch:tg-bfs-dfs\`, \`thm:tg-bfs-correct\`, \`thm:tg-dfs-bridge\`, \`fig:tg-bfs-layers\`.
- Log końcowego PDF: **brak ostrzeżeń LaTeX, brak \`Overfull \\hbox\`, brak \`Overfull \\vbox\`**. Wstępny przebieg ujawnił przepełnienie 8,82693 pt we wzorze \`low\`; poprawiono je, a workflow odtąd nie dopuszcza takich przepełnień.
- Pobrano ZIP z końcowego CI i ponownie wyrenderowano stronę ze wzorem \`low\`; kontrola wizualna: wzór mieści się w łamie, numeracja, treść i układ są czytelne. Wcześniej sprawdzono wizualnie stronę z rysunkiem BFS i jego podpisem — bez kolizji.

## Weryfikacja zakresu matematycznego

Sprawdzono dowody niezmiennika kolejki BFS, poprawności obliczonych odległości i drzewa rodziców, wykrywania składowych i dwudzielności, lasu i przedziałów czasowych DFS, kryterium mostu przez \`low\`, wykrywania cyklu oraz sortowania topologicznego. Doprecyzowano przodka i poprawiono dowód kryterium DAG.

## Co dalej

Teraz można bezpiecznie przejść do **osobnego rozdziału o najkrótszych drogach ważonych (Dijkstra, Bellman–Ford, Floyd–Warshall)**, prowadząc go zgodnie z zasadą: stworzenie rozdziału, wielokrotne audyty, kompilacja PDF, testy i dopiero po stabilizacji kolejny moduł.

Nie usuwać historycznych raportów audytów 00–02; dokumentują wykryte wady i proces ich usunięcia.
