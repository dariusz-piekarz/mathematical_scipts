# Audyt 198 — drukowany rozdział 21, stabilizacja A: przykłady i charakterystyka Eulera

Data: 2026-11-25. Kontynuacja 197, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Blob wejściowy dcb909fe03e7d7236b4d2789076b572407526df7.
Korekta 83fc634fd90a746424dd00d372e24510918e0786, blob aafe399a3ee907106c23a10977e721ad758088fd.

## Poprawki
- GKT-21-BAND-02: lemat pasa krytycznego dla dowolnych a<c<b, zgodnie z jego rzeczywistym użyciem, nie tylko symetrycznych granic. Jawny wybór regularnych cięć przed pierwszą i po ostatniej wartości krytycznej.
- GKT-21-CYL-01: skończoność liczby okręgów regularnej poziomicy przez zwartość i otwartość składowych; dla składowej pasa bez p pole z funkcją odcięcia na jej otoczeniu, pozostawanie przepływu w tej samej składowej, produkt i spójność dolnej poziomicy.
- GKT-21-EULER-01: wyprowadzenie chi=c0-c1+c2 przez sklejanie pasów wzdłuż okręgów o chi=0; dyski +1, pary spodni -1, cylindry 0. Nie trzeba ponownie zakładać globalnej formuły Morse'a.
- GKT-21-EXAMPLES-01: na sferze obliczono hesjany w mapach biegunowych. Na torusie R>r>0 obliczono pochodne, diagonalny hesjan i cztery różne uporządkowane wartości krytyczne, uzasadniono kolejność rozdzielenia i połączenia. Na RP2 podano funkcję (y^2+2z^2)/(x^2+y^2+z^2), obliczono indeksy z różnic wartości własnych i wykazano spójność poziomic przez równania elips w mapach x=1 i z=1 oraz sumę dwóch przecinających się prostych rzutowych na poziomie 1. Zwartość i ciągła bijekcja dają iloraz homeomorficzny z odcinkiem. Usunięto nieuzasadnione powołanie na sam rozkład komórkowy jako konstrukcję funkcji Morse'a.
- GKT-21-HANDLE-01: uzasadniono liczbę składowych po przyczepieniu uchwytu przez lemat o pasie krytycznym. Doprecyzowano zakres końcowej uwagi o rodzaju powierzchni. Nie dodano nowych zagadnień ani rysunków.
7 etykiet i 29 poprawnie zagnieżdżonych par środowisk zachowanych.

## Regresje
GKT-21-REEB-01 PASS: 460 sekwencji, 161 modeli spójnych, 150 cykli łącznie w modelach spójnych, 182 modele z równoległymi krawędziami, 3572 zdarzenia, 2994 podziały krawędzi.
Nowy GKT-21-EXAMPLES-01, test_gkt21_examples.js, commit 3d4dfef0b1b457c2faddbdc5ca0e05eb282c4667: PASS 120 par całkowitych promieni R>r>0, 480 kontroli indeksu hesjanu i porządkowania wartości, 3 indeksy RP2, 9120 numerycznych punktów elips (tolerancja 1e-12). Próby skończone nie zastępują dowodów. Wykonano oba skrypty po pobraniu z repozytorium w izolacie JS, nowy dwukrotnie. Nie w procesie Node, nie Lean; nie potwierdzono uruchamiania przez CI.

## CI i bramka
Dla d2e2224: terminologia 45574398809, algorytmy 45574398634, pełny audyt 45574398923, aplikacja 45574398914 — wszystkie SUCCESS.
Dla 83fc634: terminologia 45574885598 SUCCESS; aplikacja 45574885603, algorytmy 45574885651, pełny audyt 45574885799 w toku. Nie oglądano PDF w tej iteracji. Nie przenosimy statusu CI poprzedniego SHA na nowy.
Etap A otwarty. Następny audyt 199: kontrola PDF najnowszego SHA, semantyczna kontrola spójności włókien i zależności, stabilizacja. Nie dodano proponowanych rozszerzeń dotyczących drzewa konturowego ani nowego rysunku torusa.
