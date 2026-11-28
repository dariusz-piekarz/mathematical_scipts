# Audyt 173 — drukowany rozdział 18, etap A

Data: 2026-11-24. Plan 118; kontynuacja raportu 172.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit źródłowy 2c580a45663502771ecca2e19f379bedb3a2cb5a; blob 0835abd0853b0ae168da35dc590c252959263199.
Commit regresji bea661df270d79ba6e44887613b071258426cd5f.

## Zmiany
- Uogólniono definicję grafu dualnego na zamknięte zorientowane powierzchnie, skonstruowano go za pomocą pasów i promieni w dyskach ścianowych. Uzasadniono komórkowość i spójność, przypadek pętli i grafu bez krawędzi; opisano dualność przez sigma*=sigma alpha, podwójny dual i zależność równoważności osadzeń od rotacji.
- Zachowano sferyczne kryterium mostu, a jawnie wskazano jego ograniczenie dla dodatniego rodzaju (jednościanowy torus).
- Twierdzenie o rozkładzie na drzewo pierwotne T, drzewo dualne T* i pozostałe 2g krawędzi L, dowód spójności przez przekrój dualny i parzystość stopni w lesie.
- Twierdzenie o homologii nad Z: jawna baza cykli fundamentalnych dla L. Dowód całkowitego izomorfizmu współrzędnych cykli poza T, rozwiązywania równań różnicowych na T*, usuwania współrzędnych B przez brzegi i niezależności pozostałych klas. Wyprowadzono H0 i H2, brak torsji H1, wskazano użycie twierdzenia o homologii komórkowej.
- Sprawdzono sąsiednie tematy w rozdziałach 06,13,16; wykorzystano istniejący materiał o cyklach fundamentalnych, bez dodawania odrębnej teorii triangulacji.
- 14 unikalnych etykiet, 43 prawidłowo zagnieżdżone środowiska, 7 odsyłaczy z odnalezionymi celami.

## Rzeczywiste regresje 3/3
GKT-18-TC-01: test_gkt18_tree_cotree.js, blob b927588e0f1ebdccb39fd9135c46bede1060c607. Wykonano JS przed zapisem i po pobraniu z gałęzi, zmieniając wyłącznie końcowy log na return.
PASS total=2546, connected=2221, positiveGenus=1408, loops=1858, parallel=1896, oneFace=329, decomps=4442, basis=8996, relations=12354.
Wszystkie permutacje na 2,4,6 półkrawędziach, ustalone parowanie alpha(d)=d xor 1, oraz 1800 deterministycznych prób na 8–18 półkrawędziach. Próby mogą się powtarzać; liczby nie oznaczają klas izomorfizmu. Dla spójnych modeli sprawdzono podwójny dual, warunek łańcuchowy, dwa porządki wyboru drzew, całkowite współrzędne i redukcję, jednostkową bazę ilorazu oraz zerowanie brzegów. Test nie obejmuje przypadku pustego zbioru półkrawędzi, który uzasadniono osobno w tekście.
Ponowiono ROT-01: PASS 7776+64 rotacji; BRIDGE-01: PASS 1067 mostów. W BRIDGE-01 zastąpiono import Node równoważną asercją i log zwracaniem wyniku. Testy skończone, nie formalizacja Lean.

## CI/PDF
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45491866148 — pełny audyt i skład dla commitu źródłowego w toku, bez końcowego wyniku. Terminologia polska SUCCESS (45491866120). Nie pobrano nowego PDF.
Etap A otwarty. Uzupełnienia wskazane w raporcie 172 wykonano; nie rozszerzać dalej zakresu bez istotnej luki. Następnie stabilizacja: w szczególności kontrola geometrycznej konstrukcji dualu i konwencji rotacji, dowodu całkowitej homologii, istniejących rysunków i rzeczywistego PDF, ponowienie regresji. Dopiero po bramce CI/PDF etap B.
