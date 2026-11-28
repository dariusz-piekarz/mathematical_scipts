# Audyt 200 — drukowany rozdział 21, etap A: kontrola PDF i stabilizacja

Data: 2026-11-25. Kontynuacja 199, bez rozszerzania zakresu.
Źródło chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Commit źródła 287db8a3bd6d71e5bf8f6e2fdafcebd8d70ea215, blob e64756b6a0f5b37035f376dc55b098bb2937cd57 potwierdzony na gałęzi. Bez zmian źródła.

## Kontrola semantyczna
Ponownie odczytano cały rozdział. Sprawdzono przepływ na regularnych przedziałach (funkcja odcięcia, zupełność, odwrotność), hipotezy twierdzenia o uchwytach, rachunek charakterystyki Eulera pasa siodłowego, konstrukcję cylindra regularnej składowej poziomu krytycznego i dowód spójności włókna w W. Zgodność trywializacji i sklejania grafów, stopnie 1/3 oraz wzór Bettiego mają jawne uzasadnienia. Sprawdzono przykłady sfery, torusa i RP2. Nie zidentyfikowano nowej istotnej usterki. Przyjmowane klasyczne wyniki teorii Morse'a i klasyfikacji powierzchni pozostają jawnie wskazane. 7 etykiet, 29 poprawnie zagnieżdżonych par środowisk.

## PDF
Pobrano i rozpakowano dwa artefakty:
- 15003034819 dla 83fc634 (audyt 198): 345 stron, rozdział 21 na fizycznych stronach 179–184, 7 adnotacji odsyłaczy, plik ostrzeżeń 0 bajtów.
- 15003816651 dla 287db8a (audyt 199): 345 stron, rozdział 21 na fizycznych stronach 179–184 (druk 169–174), 10 adnotacji odsyłaczy, plik ostrzeżeń 0 bajtów.
W obu wersjach wyrenderowano wszystkie sześć stron w skali 1.5 i obejrzano dwa arkusze kontaktowe. Schematy sfery, torusa i obu siodeł czytelne; siodła mają trzy ramiona. Najnowszy PDF ma pełniej wykorzystaną ostatnią stronę. Dowód twierdzenia 21.2.2 zaczyna się na następnej stronie po jego wypowiedzi, a przykład RP2 przechodzi przez granicę stron po wyświetlonym wzorze. Układ czytelny, bez zauważalnych kolizji ani obcięć. Nie wprowadzano kolejnego cyklu zmian kosmetycznych.

## Regresje
GKT-21-REEB-01 PASS: 460 sekwencji, 161 spójnych modeli, 150 cykli łącznie w modelach spójnych, 182 modele z krawędziami równoległymi, 3572 zdarzenia, 2994 podziały krawędzi.
GKT-21-EXAMPLES-01 PASS: 120 par promieni, 480 indeksów, 3 indeksy RP2, 9120 numerycznych punktów elips.
Oba skrypty ponownie pobrano i wykonano w izolacie JS. Nie potwierdzono wykonania w procesie Node ani wywołania przez CI; nie są formalizacją Lean.

## Bramka
Dla 287db8a: terminologia 45575134707 SUCCESS, algorytmy 45575134818 SUCCESS, pełny audyt 45575134635 SUCCESS, aplikacja 45575134761 w toku przy ostatniej kontroli. PDF najnowszego SHA zweryfikowany. Etap A pozostaje otwarty jedynie do potwierdzenia ostatniego przebiegu CI, pod warunkiem niezmienionego źródła.
Następny audyt 201: potwierdzić ostatnią bramkę, zamknąć A bez nowych zmian jeśli brak usterek; następnie osobna iteracja B. Postęp 20/44. Nie dodano niezatwierdzonych rozszerzeń.
