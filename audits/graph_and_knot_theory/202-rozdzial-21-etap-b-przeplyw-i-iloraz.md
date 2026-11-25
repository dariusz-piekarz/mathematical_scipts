# Audyt 202 — drukowany rozdział 21, niezależny etap B

Data: 2026-11-25. Etap A zamknięto w 201.
Źródło: chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Blob wejściowy e64756b6a0f5b37035f376dc55b098bb2937cd57.
Korekta c8d7ec0bf37a7498ace7ed66943eb84b161e2b0d, blob c5f5cd82fc80e9480801b8565c356d509eeab503.

## Kontrola niezależna i poprawki
- GKT-21-B-HESS-01: pełna reguła transformacji hesjanu w punkcie krytycznym, znikanie składników zawierających pierwsze pochodne, prawo bezwładności Sylvestera; izolowanie punktów przez twierdzenie o funkcji odwrotnej.
- GKT-21-B-FLOW-01: argument pierwszego wyjścia z regularnego pasa dla czasów dodatnich i ujemnych, także na końcach przedziału. Uzasadniono wybór małego dysku w lokalnym modelu siodła, zawartego w W, oraz wartości a<s<c<t<b.
- GKT-21-B-GLUE-01: relacja utożsamiania końców skończonej sumy odcinków jest domknięta, więc iloraz jest Hausdorffa; jawnie sprawdzono klasy włókien po sklejeniu pasów, bez identyfikacji różnych wysokości i różnych okręgów wspólnego brzegu.
- GKT-21-B-RP2-01: różniczka formy kwadratowej na sferze, warunek wektora własnego i lokalny dyfeomorfizm ilorazu antypodycznego. Uzasadniono niezerowość współrzędnych w mapach afinicznych i niepustość/spójność poziomic w przedziale [0,2].
- GKT-21-B-HANDLE-01: poprawiono niedostateczne założenie przykładu (wcześniej wykluczało tylko inne punkty indeksu 1); teraz dokładnie jeden punkt krytyczny w przeciwobrazie przedziału, indeks 1, funkcja prosta i jawne założenia o powierzchni. Rozróżniono sam abstrakcyjny graf i graf z wysokością.
Nie rozszerzano zakresu ani nie zmieniano rysunków. Zachowano 7 etykiet i 29 poprawnie zagnieżdżonych par środowisk. Klasyczne twierdzenie o uchwytach pozostaje przyjmowane.

## Regresje
Nowy GKT-21-GLUE-01, test_gkt21_glue.js, commit 5d2820ec91afcdfe4e496039c5d21cfbeb200d8a.
PASS: 105 modeli zdarzeń z maksymalnie 7 wierzchołkami (nie tylko wybór FIFO; różne aktywne końce), 42 spójne, 28 z krawędziami równoległymi, 340 wstawionych regularnych wierzchołków, 98 modeli z krawędzią przechodzącą przez wysokość innego punktu krytycznego. Sprawdzono stopnie, wzór Eulera, monotoniczność przy usuwaniu wierzchołków pomocniczych, zachowanie liczby cykli i dokładne odtworzenie multizbioru krawędzi. Test kombinatoryczny, nie dowód topologiczny ani enumeracja klas izomorfizmu.
REEB-01 PASS: 460 sekwencji, 161 modeli spójnych, 182 z krawędziami równoległymi.
EXAMPLES-01 PASS: 120 par promieni, 480 indeksów torusa, 3 indeksy RP2, 9120 punktów elips.
Wszystkie trzy skrypty pobrano z repozytorium i wykonano w izolacie JS; nowy skrypt także przed zapisem. Nie potwierdzono uruchomienia w procesie Node ani integracji z CI; nie formalizacja Lean.

## Bramka
Dla c8d7ec0: terminologia 45575850030, algorytmy 45575849967, pełny audyt 45575849896, aplikacja 45575849954 — wszystkie w toku przy kontroli. Nowego PDF nie oglądano. Etap B otwarty do stabilizacji. Następna iteracja 203: kontrola poprawek, CI i PDF dokładnego SHA, bez rozszerzania zakresu.
