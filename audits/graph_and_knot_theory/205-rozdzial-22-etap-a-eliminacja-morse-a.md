# Audyt 205 — drukowany rozdział 22, pierwszy etap A

Data: 2026-11-25. Rozdział 21 zamknięty w 204.
Źródło: chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex.
Blob wejściowy 3d038550d45f94141b9671ce79feedb8900d74ed.
Korekta 939dc824b24c0239a226e104ded804048f66f850, blob 3e5793221d991bfef83d7c23b604c49a4209a11e.

## Usterki i poprawki
- GKT-22-FUNCTION-01: uzupełniono brakujący kierunek równoważności dyskretnej funkcji Morse'a i acyklicznego parowania. Argument rombu w zbiorze ścian wyklucza parowanie tej samej komórki jednocześnie w górę i w dół; wzdłuż strzałek Hassego F jest niemalejąca, na niesparowanych ściśle rośnie. Doprecyzowano numerację topologiczną, definicję pola gradientowego, zapis V-ścieżki i konwencję niepustych sympleksów. Usunięto potoczne „poset”.
- GKT-22-GRAPH-01: odróżniono incydencje w multigrafie od regularnego kompleksu; pętle nie są parowane. Podział każdej krawędzi na trzy daje graf prosty także przy pętlach i równoległych krawędziach, zachowuje m-n+1. W przykładzie trójkąta wykazano acykliczność również po dodaniu pary wymiarów 1,2.
- GKT-22-COLLAPSE-01: wykazano domknięcie podkompleksu po usunięciu wolnej pary, opis przecięcia przez nośniki barycentryczne oraz ciągłość sklejonej homotopii na iloczynach z przedziałem.
- GKT-22-CANCEL-01: jawna formuła aktualizacji Schura, rachunek współczynnika przy a' w brzegu brzegu, włączenie/rzut i homotopia łańcuchowa. Przy porządku topologicznym macierz par jest dolnotrójkątna; eliminowanie od pierwszej pary nie zmienia pozostałego bloku par. Rozpisano wpływ zmian baz na sąsiednie różniczki: usunięcie kolumny w stopniu p i wiersza w stopniu p+2, bez zmiany pozostałych współczynników. Jednostki ±1 pozostają jednostkami również nad Z.
- GKT-22-TREE-COTREE-01: spójność szkieletu z rozkładu na składowe; argument liścia w lesie złożonym z nośnika niezerowego cyklu, z jawnym współczynnikiem 1 nad F2.
- Poprawiono indeks najwyższej zerowej różniczki w nierównościach Morse'a (r_{d+1}, nie r_d), w tym pusty kompleks, termin „element główny” zamiast pivot i „gładka” funkcja Morse'a. Dodano bibliograficzny odsyłacz do przyjmowanego twierdzenia Formana (A User's Guide to Discrete Morse Theory, SLC 48, B48c, 2002). Nie przedstawiano twierdzenia topologicznego jako udowodnionego w rozdziale.
13 etykiet bez zmian, 35 poprawnie zagnieżdżonych par środowisk.

## Regresja
GKT-22-CANCEL-01, test_gkt22_cancel.js, commit be601ec29abb2002efb59ecd114f94f257435456.
PASS: 240 deterministycznie generowanych skończonych kompleksów symplicjalnych, 152 z parami w sąsiednich wymiarach, 3652 eliminacje w dwóch porządkach wymiarów, 6433 zmiany współczynników Schura, 1920 porównań homologii nad F2,F3,F5,F7. Sprawdzano jednostki, zachowanie pozostałych elementów głównych, brzeg brzegu po każdej eliminacji, bazę krytyczną i liczby Bettiego. Obliczenia całkowitoliczbowe w JS Number na małych przypadkach; nie test Smitha ani dowód zachowania torsji. Wykonano przed zapisem i po odczycie z repozytorium w izolacie JS, nie w procesie Node; integracja z CI niepotwierdzona, nie Lean.

## Dalsza stabilizacja
Sprawdzić dokładniej konstrukcję drzewo–drzewo dualne (w tym nieorientowalne powierzchnie), jawny model okresowej triangulacji torusa 3x3, przykład RP2 i torsję, kompletność nierówności, terminologię i PDF. Trwała regresja dla konstrukcji drzewo–drzewo dualne i funkcji Morse'a pozostaje do rozważenia jako kontrola istniejącego materiału.

## Propozycje po pierwszym audycie
Opcjonalnie: wzór na różniczkę Morse'a przez ważone ścieżki gradientowe i przykład, w którym niezerowy współczynnik powstaje dopiero po eliminacji; schemat graficzny drzewo–drzewo dualne na małej triangulacji. Nie dodano bez zgody; w stabilizacji nie rozszerzać zakresu.

## Bramka
Dla 939dc824: algorytmy 45576561918, terminologia 45576562013, pełny audyt 45576562063 queued; aplikacja 45576562157 w toku. PDF nie sprawdzono. Etap A otwarty. Następny audyt 206: stabilizacja istniejących dowodów, przykładów i regresji oraz CI/PDF. Postęp 21/44.
