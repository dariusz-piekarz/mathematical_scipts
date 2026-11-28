# Audyt 203 — drukowany rozdział 21, stabilizacja etapu B

Data: 2026-11-25. Kontynuacja 202.
Źródło: chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Commit źródłowy c8d7ec0bf37a7498ace7ed66943eb84b161e2b0d; blob c5f5cd82fc80e9480801b8565c356d509eeab503 potwierdzony dwukrotnie. Bez zmian źródła.

## Stabilizacja semantyczna
Ponownie odczytano cały rozdział i sprawdzono poprawki B:
- B-HESS-01: reguła łańcuchowa drugiego rzędu w punkcie krytycznym, znikanie wyrazów z pierwszymi pochodnymi, kongruencja przez odwracalną macierz i prawo bezwładności; izolowanie zer pierwszych pochodnych.
- B-FLOW-01: funkcja odcięcia na otoczeniu zwartego pasa, zupełność, argument pierwszego wyjścia dla czasów dodatnich i ujemnych, także z brzegu; wzajemna odwrotność map produktowych. Mały spójny dysk Morse'a wokół siodła w pasie i przepływ do obu regularnych brzegów.
- B-GLUE-01: lokalny cylinder regularnej składowej krytycznego poziomu, poprzeczność, zwartość i otwartość; konstrukcja gwiazdy ilorazowej, domknięta relacja na skończonej sumie odcinków, zgodność włókien na wspólnych poziomach. Usuwanie wierzchołków pomocniczych nie zmienia wysokości ani stopni krytycznych. Odsyłacz do bukietu okręgów uwzględnia krawędzie równoległe.
- B-RP2-01: warunek Aw równoległy do w, lokalny dyfeomorfizm ilorazu antypodycznego, indeksy 0/1/2, równania obu rodzin elips, przecięcie prostych rzutowych i niepustość poziomic w [0,2].
- B-HANDLE-01: dokładnie jeden punkt krytyczny w przeciwobrazie przedziału, orientowalność, rozdzielenie/połączenie; odróżnienie grafu z wysokością od abstrakcyjnego grafu. Rachunek Eulera i Bettiego zgodny z poprzednimi rozdziałami.
Nie zidentyfikowano nowej istotnej usterki. Klasyczne twierdzenie o uchwytach i klasyfikacja powierzchni pozostają jawnymi przesłankami. Zachowano 7 etykiet i 29 poprawnie zagnieżdżonych par środowisk.

## Regresje
Ponownie pobrano i wykonano trzy skrypty:
- GKT-21-REEB-01 PASS: 460 sekwencji, 161 spójnych modeli, 150 cykli łącznie w modelach spójnych, 182 modele z krawędziami równoległymi, 3572 zdarzenia, 2994 podziały.
- GKT-21-EXAMPLES-01 PASS: 120 par promieni, 480 indeksów, 3 indeksy RP2, 9120 punktów elips.
- GKT-21-GLUE-01 PASS: 105 modeli, 42 spójne, 340 wstawionych wierzchołków, 28 z krawędziami równoległymi, 98 modeli z krawędzią przechodzącą przez inną wysokość krytyczną.
Wykonano w izolacie JS, nie w procesie Node; nie potwierdzono integracji z CI. Nie formalizacja Lean.

## CI i PDF
Dla c8d7ec0: terminologia 45575850030 SUCCESS, algorytmy 45575849967 SUCCESS, pełny audyt 45575849896 w toku (structural-audit SUCCESS, full-book-pdf w toku), aplikacja 45575849954 w toku. Dostępny tylko artefakt strukturalny 15003727822, brak artefaktu pełnej kompilacji na chwilę ostatniej kontroli. Nie oglądano nowego PDF. Kontrola PDF w 200 dotyczy poprzedniego SHA i nie zamyka obecnej bramki.

## Decyzja
Etap B pozostaje otwarty wyłącznie do sprawdzenia pozostałych CI i PDF, pod warunkiem niezmienionego źródła. Następny audyt 204: potwierdzić bramkę, obejrzeć PDF dokładnego SHA, zamknąć B tylko w razie braku usterek. Postęp 20/44. Bez rozszerzania zakresu.
