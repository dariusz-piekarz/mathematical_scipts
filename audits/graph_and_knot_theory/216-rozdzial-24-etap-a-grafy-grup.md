# Audyt 216 — drukowany rozdział 24, pierwszy etap A

Data: 2026-11-25. Rozdział 23 zamknięto w 215.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Blob wejściowy 8836c0f6b368eab2fd5fc72a14f5af04d68c74f5.
Korekta f3f6fc821fbe61993fc2f0930c24e3452f174ba8, blob b041226a6aea62eedb4be28a8e5ec25ea95dc5bd.

## Usterki i poprawki
- GKT-24-CAYLEY-01: każdą krawędź nieskierowaną liczymy raz, także przy generatorach rzędu dwa; brak pętli, stopień |S|. Doprecyzowano, że relacje odczytujemy z etykietowanych spacerów, a cykl prosty ma długość co najmniej trzy. Odsyłacz do definicji grupy wolnej.
- GKT-24-ACTION-01: jawna swoboda na wierzchołkach; dla działania bez inwersji stabilizator krawędzi jest przecięciem stabilizatorów końców. Realizacja CW również przy nieskończonych stopniach. Dowód równomiernego nakrywania gwiazd z topologii słabej CW, a nie z metryki długości. Prosta spójność nieskończonego drzewa oraz wolność grupy fundamentalnej nieskończonego grafu przez zwartość obrazów pętli i homotopii, skończone podkompleksy, drzewo rozpinające i wcześniejsze twierdzenie o skończonym grafie. Użyto standardowego faktu o zwartych podzbiorach CW i lematu Zorna.
- GKT-24-GROUP-GRAPH-01: brakującą definicję grupy fundamentalnej grafu grup uzupełniono prezentacją względem drzewa rozpinającego, relacjami t_bar e=t_e^{-1}, t_e=1 na drzewie i relacjami sprzężenia. Wyjaśniono zachowanie relacji grup wierzchołkowych. Niezależność od drzewa i injektywność naturalnych homomorfizmów jawnie przyjmowane z teorii Bassa–Serre'a, nie wyprowadzane z samej prezentacji.
- GKT-24-HNN-01: jawne otwarte pokrycie podwójnego cylindra odwzorowań, dwie składowe przecięcia, wybór ścieżek bazowych i t=[p_+ gamma^{-1} p_-^{-1}] dla konkatenacji od lewej do prawej. Kierunek relacji sprawdzony homotopią w cylindrze. Grupoidową wersję van Kampena stosujemy jako znane twierdzenie, nie dowodzimy jej ogólnie.
- GKT-24-INDEX-01: jawny opis półkrawędzi danego typu przy wierzchołku przez lewe klasy boczne i stabilizatory sprzężone, w tym indeksy nieskończone. Klasy boczne to zbiór, nie grupa ilorazowa.
- GKT-24-BS-01: jawny rachunek afiniczny TAT^{-1}=A², TA≠AT. Podstawowe twierdzenie Bassa–Serre'a pozostaje wynikiem przyjętym z literatury Serre'a. 
Zachowano pięć etykiet, 29 poprawnie zagnieżdżonych par środowisk, dodano trzy odsyłacze do wcześniejszego rozdziału o grafie jako przestrzeni topologicznej. Bez zmian innych źródeł.

## Regresja
GKT-24-CAYLEY-01, test_gkt24_cayley.js, commit 9c891237073fd6f5b17c386e472ac603541ef482. PASS: wszystkie symetryczne podzbiory niezerowych elementów Z/nZ dla 2<=n<=14, 380 modeli (41 niespójnych), 4486 wystąpień wierzchołków, 12724 krawędzi. Kontrole stopnia, liczby krawędzi, składowej jedności przez gcd oraz translacji. Dla F_r, r=1,...,4, słowa zredukowane długości 0,...,4: 4308 wierzchołków, 31892 przejścia, kontrola liczby słów w każdej sferze, unikatowego poprzednika, stopnia i odwracalności przejścia. Nie dowód ogólnego twierdzenia ani test nieskończonego drzewa w całości.
Wykonano przed zapisem i po odczycie z repozytorium w izolacie JS. Nie potwierdzono wykonania w procesie Node ani integracji z CI; nie Lean.

## Dalsza stabilizacja
Sprawdzić szczegółowo zgodność relacji prezentacji grafu grup z orientacją krawędzi w modelu klas bocznych, dowód nakrycia i grupę przekształceń pokładowych, przypadek HNN (w tym deformacja kołnierzy), przykłady iloczynu wolnego i BS(1,2), oraz rysunki i odsyłacze. Dodać regresje właściwe dla istniejących przykładów i poprawianych tożsamości.

## Propozycje po pierwszym audycie
Opcjonalnie: rysunek fragmentu drzewa Bassa–Serre'a dla C2*C3 i BS(1,2), osobne omówienie postaci normalnej dla amalgamacji i lematu Brittona dla HNN. Nie dodano bez zatwierdzenia; dalsza stabilizacja bez rozszerzania zakresu.

## Bramka
Dla f3f6fc82: algorytmy 45587950969, terminologia 45587950648, aplikacja 45587950778, pełny audyt 45587950996 — queued przy ostatnim odczycie. PDF nie oglądano. Etap A otwarty. Następny audyt 217: stabilizacja istniejącej treści, CI/PDF. Postęp 23/44.
