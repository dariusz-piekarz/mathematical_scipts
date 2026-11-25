# Audyt 207 — drukowany rozdział 22, stabilizacja A: funkcje Morse'a i kolapsy

Data: 2026-11-25. Kontynuacja 206 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex.
Blob wejściowy 4cb9468e2963e47cd5ea516667f2c99c65fdad2a.
Korekta 0a436d68f580b252c1e68ec33501f37d301b7867, blob 2ad61fc865659e0e80951f78b53e415e82ecee9d.

## Poprawki i kontrola
- GKT-22-FUNCTION-02: jawna dziedzina i przeciwdziedzina funkcji, zakres p>=0, konstrukcja numeracji topologicznej przez kolejne usuwanie źródeł wraz z dowodem istnienia źródła. Doprecyzowano kierunek nierówności względem relacji ścian, charakterystykę komórek krytycznych i fakt, że konstrukcja odtwarza parowanie, a nie konkretne wartości funkcji. Sprawdzono argument rombu oraz obie implikacje równoważności acykliczności z brakiem cyklu Hassego. Poprawiono tytuł definicji porządku częściowego.
- GKT-22-COLLAPSE-02: rozpisano nieujemność i sumę współrzędnych barycentrycznych dla całej homotopii, opis przecięcia |beta| z |K'| przez nośniki i jawny wzór na sumę ścian. Uwzględniono p=0; właściwe ściany usuwanej ściany pozostają w podkompleksie. Odsyłacz do konwencji realizacji w rozdziale 20.
- Bez nowych zagadnień ani rysunków. Zachowano 13 etykiet i 36 poprawnie zagnieżdżonych par środowisk. Kontrola zależności szersza niż wskazany rozdział nadal otwarta.

## Regresje
GKT-22-CANCEL-01 PASS: 240 kompleksów, 152 z parami w sąsiednich wymiarach, 3652 eliminacje, 6433 aktualizacje Schura, 1920 porównań nad ciałami.
GKT-22-TREE-COTREE-01 PASS: 120 prób konstrukcji, 3936 eliminacji, 24 redukcje RP2 z d2=±2, 96 z zerową różniczką, 60 kontroli ogniw.
Nowy GKT-22-FUNCTION-COLLAPSE-01, test_gkt22_function_collapse.js, commit 4ea85812f2647cb760a9eaabb601529761db304f. PASS: wszystkie 16384 przypisania wartości 0,1,2,3 do siedmiu niepustych sympleksów pełnego trójkąta, 232 spełniające warunki Morse'a, w tym 201 z równością wartości w co najmniej jednej parze. Wszystkie 42 parowania pełnego trójkąta (40 acyklicznych, 2 cykliczne), niezależne wykrywanie zamkniętych V-ścieżek i cykli przez sortowanie topologiczne, odtworzenie każdego acyklicznego parowania przez funkcję. 1715 punktów siatki barycentrycznej o mianowniku 6 dla p=0,...,5, 12005 kontroli homotopii w siedmiu chwilach: nieujemność, suma, nieruchomość na celu i osiągnięcie celu dla u=1. Rachunek na całkowitych licznikach, bez błędów zaokrągleń dla tych prób. Skończona regresja nie zastępuje dowodu ciągłości. Wszystkie skrypty wykonano po odczycie z repozytorium w izolacie JS, nowy także przed zapisem. Nie Node, nie Lean, nie potwierdzono integracji z CI.

## CI i PDF
Dla 64b55ae9: terminologia 45576859890, pełny audyt 45576860020, algorytmy 45576859915 SUCCESS; aplikacja 45576859940 w toku przy ostatniej kontroli.
Dla 0a436d68: terminologia 45577187370 SUCCESS; aplikacja 45577187356, pełny audyt 45577187416, algorytmy 45577187736 w toku. Nie przeniesiono PASS poprzedniego SHA. Nie wykonano oględzin PDF: artefakt najnowszego SHA jeszcze niepotwierdzony; poprawki zmieniły skład.
Etap A pozostaje otwarty. Następny audyt 208: CI, rzeczywiste oględziny PDF najnowszego SHA, kontrola odsyłaczy i pozostałych zależności, stabilizacja bez rozszerzania zakresu. Postęp 21/44.
