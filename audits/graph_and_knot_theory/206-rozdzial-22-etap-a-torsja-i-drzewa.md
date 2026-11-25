# Audyt 206 — drukowany rozdział 22, stabilizacja A: torsja i drzewo–drzewo dualne

Data: 2026-11-25. Kontynuacja 205, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex.
Blob wejściowy 3e5793221d991bfef83d7c23b604c49a4209a11e.
Korekta 64b55ae951bfdd45bb6ecf71de60beb0a9427b2b, blob 4cb9468e2963e47cd5ea516667f2c99c65fdad2a.

## Poprawki
- GKT-22-TORSION-01: izomorfizmy homologii całkowitych zachowują podgrupy torsyjne. Uzasadniono stopień 2 mapy przyklejającej dwukomórkę w RP2 przez iloraz antypodyczny brzegu dysku; rozpisano H0,H1,H2 nad Z i H1 nad R. Wyraźnie odróżniono nieregularny model CW od regularnego kompleksu, do którego stosujemy parowanie Formana.
- GKT-22-INEQ-01: jawna suma teleskopowa różnic c_j-b_j, współczynniki wewnętrzne i pozostający r_{p+1}.
- GKT-22-TREE-COTREE-02: konstrukcja nie wymaga orientowalności; dowód nad F2 dotyczy wszystkich zamkniętych spójnych powierzchni. Dla orientowalnej powierzchni uzasadniono b2=1 nad dowolnym ciałem przez zgodne orientacje i spójność grafu dualnego, następnie b1=2g z Eulera. Sprawdzono treść odsyłacza thm:tg-surface-homology (sformułowany nad R; tutaj jawnie rozszerzono jego argument na dowolne ciało).
- GKT-22-TORUS-01: jawne trójkąty A_ij,B_ij na (Z/3Z)^2, trzy rozłączne typy krawędzi, niepowtarzalność trójkątów, realizacja przez okresową triangulację, rachunek (9,27,18).
- Doprecyzowano współczynniki homologii w przykładzie sfery. Zachowano 13 etykiet, 36 poprawnie zagnieżdżonych par środowisk (jedno dodatkowe split). Bez nowych zagadnień i rysunków.

## Regresje
GKT-22-CANCEL-01 ponownie PASS: 240 kompleksów, 152 z parami sąsiednich wymiarów, 3652 eliminacje, 6433 zmiany Schura, 1920 porównań nad ciałami.
Nowy GKT-22-TREE-COTREE-01, test_gkt22_tree_cotree.js, commit cd171305a35a3b71fde5b77e734a46d865736d40.
PASS: pięć modeli triangulacji (brzeg czworościanu, sześciowierzchołkowa RP2, torusy okresowe 3x3,4x4,5x5), 60 sprawdzeń ogniw wierzchołków, 120 konstrukcji drzew z 24 deterministycznymi próbami wyboru korzeni i kolejności na model, 3936 eliminacji par, 96 wyników orientowalnych z zerowymi różniczkami, 24 wyniki RP2 z d1=0, d2=±2. Liczby prób nie oznaczają liczby różnych klas izomorfizmu ani unikatowych drzew. W modelu RP2 każdy brzeg należy do dwóch trójkątów, ogniwa są spójne stopnia dwa, a chi=1; identyfikacja z RP2 przez klasyfikację powierzchni. Eliminacja nad Z na małych macierzach JS Number z jednostkowymi elementami głównymi, nie ogólny algorytm postaci Smitha. Oba skrypty wykonano po odczycie z repozytorium w izolacie JS, nowy także przed zapisem. Nie potwierdzono integracji z CI, nie Node ani Lean.

## Bramka
Dla 939dc824: terminologia 45576562013, algorytmy 45576561918, aplikacja 45576562157 SUCCESS; pełny audyt 45576562063 w toku.
Dla 64b55ae9: terminologia 45576859890 SUCCESS; algorytmy 45576859915 i pełny audyt 45576860020 w toku, aplikacja 45576859940 queued. Najnowszy PDF nie był oglądany. Nie przeniesiono PASS z poprzedniego SHA.
Etap A otwarty. Następny audyt 207: kontrola równoważności dyskretnej funkcji Morse'a i parowania, kolapsów, zależności i PDF. Nie dodano niezatwierdzonych rozszerzeń. Postęp 21/44.
