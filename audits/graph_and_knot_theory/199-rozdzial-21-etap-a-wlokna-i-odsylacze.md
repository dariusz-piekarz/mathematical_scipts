# Audyt 199 — drukowany rozdział 21, stabilizacja A: włókna i zależności

Data: 2026-11-25. Kontynuacja 198, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Blob wejściowy aafe399a3ee907106c23a10977e721ad758088fd.
Korekta 287db8a3bd6d71e5bf8f6e2fdafcebd8d70ea215, blob e64756b6a0f5b37035f376dc55b098bb2937cd57.

## Kontrola semantyczna
- GKT-21-FIBER-02: rozpisano konstrukcję cylindra wokół regularnej składowej krytycznego poziomu. Jednolity lokalny czas przepływu na zwartym okręgu, przedłużenia po regularnych przedziałach zgodne przez jednoznaczność, różnowartościowość przez cofnięcie przepływu, otwartość względna przez twierdzenie o funkcji odwrotnej i poprzeczność, domkniętość przez zwartość. Cylinder stanowi składową pasa niezawierającą p. Każda składowa poziomicy przecinająca W leży w W, zatem krytyczne włókno w W jest spójne.
- GKT-21-GLUE-02: wspólne pole na obu regularnych stronach c zapewnia zgodność trywializacji i pozostawanie w W. Jawnie zdefiniowano b_a,b_b dla wszystkich typów punktów. Wyjaśniono usuwanie pomocniczych wierzchołków stopnia dwa także na regularnych składowych poziomów krytycznych oraz ścisłą monotoniczność wysokości na krawędziach, wykluczającą pętle i okręgi bez wierzchołków krytycznych.
- GKT-21-REF-01: sprawdzono pełną treść thm:tg-wedge w źródle 07; twierdzenie obejmuje grafy z pętlami i krawędziami równoległymi. Dodano jawny odsyłacz i rachunek homologii komórkowej bukietu. Sprawdzono wzór Eulera dla powierzchni w źródle 11 (thm:tg-surface-euler i poprzedzający wywód dla powierzchni z brzegiem); dodano odsyłacze bez stosowania twierdzenia o zanurzeniu komórkowym do samego grafu Reeba. Przejrzano odpowiednie wystąpienia w źródłach 13,15,16; nie znaleziono konfliktu. To kontrola celowana, nie pełny audyt dalszych rozdziałów.
- 7 etykiet i 29 poprawnie zagnieżdżonych par środowisk zachowanych. Bez zmian rysunków, bez dodawania niezatwierdzonych zagadnień.

## Regresje
GKT-21-REEB-01 PASS: 460 sekwencji, 161 modeli spójnych, 150 cykli łącznie w modelach spójnych, 182 modele z równoległymi krawędziami, 3572 zdarzenia, 2994 podziały krawędzi.
GKT-21-EXAMPLES-01 PASS: 120 par promieni, 480 kontroli indeksów, 3 indeksy RP2, 9120 punktów elips. Oba zapisane skrypty wykonano po pobraniu z repozytorium w izolacie JS, nie w procesie Node, nie Lean; nie potwierdzono uruchomienia przez CI. Testy kombinatoryczne i numeryczne nie zastępują dowodu topologicznego.

## CI i bramka
Dla 83fc634: terminologia 45574885598, algorytmy 45574885651 i pełny audyt 45574885799 SUCCESS, aplikacja 45574885603 w toku przy ostatnim sprawdzeniu.
Dla 287db8a: pełny audyt 45575134635, algorytmy 45575134818, aplikacja 45575134761, terminologia 45575134707 — queued przy kontroli.
Nie oglądano PDF w tej iteracji; artefakt pełnej kompilacji nie był dostępny podczas pierwszego zapytania, a następnie zmieniono źródło. Nie przenosimy PASS z poprzedniego SHA. Etap A otwarty. Audyt 200: CI i rzeczywiste oględziny PDF właściwego SHA, dalsza stabilizacja tylko jeśli wykryto usterkę. Nie przechodzić do B przed bramką.
