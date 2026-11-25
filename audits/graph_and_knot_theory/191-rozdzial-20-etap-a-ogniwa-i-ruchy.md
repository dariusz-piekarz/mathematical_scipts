# Audyt 191 — drukowany rozdział 20, etap A: kryterium ogniwa, dualność i ruchy Pachnera

Data: 2026-11-25. Rozdział 19 zamknięto w 190.
Źródło: chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Blob wejściowy 940db3f266fce4546dc519fec35b471583652162.
Korekta 5a5186dad08b55b9740ad84a3cfbe6ee594cb762, blob d8ee6fbd913f936d93aabab730abde06c92fc33b.

## Usterki i poprawki
- GKT-20-LINK-01: spójna konwencja niepustych sympleksów (także w ogniwie), właściwy zbiór wierzchołków ogniwa, przypadek izolowanego wierzchołka i grafu zerowego. Jawne współrzędne stożka oraz baza otoczeń. W źródłach kolejnych rozdziałów 14 i 15 nie znaleziono użycia ogniwa ani pustego sympleksu; pełna kontrola dalszych zależności pozostaje do wykonania.
- GKT-20-PURITY-01: dowód czystości dowolnej skończonej triangulacji powierzchni bez brzegu przez lokalne homologie w punktach wnętrz maksymalnych sympleksów, także p=0. Jawnie wskazano użyte klasyczne twierdzenia homologii singularnej.
- GKT-20-LOCAL-01: usunięto nieuprawnione wnioskowanie o spójności dowolnego przebitego otoczenia. Wycięcie i ciąg dokładny pary dają H_2 lokalne dla k półdysków i H_1 lokalne równe zredukowanemu H_0 ogniwa; stąd dwa trójkąty przy krawędzi i jedno spójne ogniwo. Sprawdzić założenia i dokładność izomorfizmów.
- GKT-20-DUAL-01: zastąpiono nieuzasadnioną poprzeczną ścieżkę argumentem kombinatorycznym przez cykle ogniw i rozbicie realizacji na domknięte sumy trójkątów. Graf dualny abstrakcyjnej triangulacji jest prosty i trójregularny; wykluczono pętle i równoległe krawędzie. Rozróżniono kompleksy typu Delta i podano rachunek wierzchołków/krawędzi modelu torusa z kwadratu.
- GKT-20-MOVE-01: warunki odwrotnego ruchu 3->1 (trójkąt nie może już istnieć), ruchu 2->2 (brak nowej przekątnej, cztery różne wierzchołki), konstrukcja homeomorfizmu względnie do brzegu przez wspólny model wypukły, sprawdzenie dopuszczalności dwuruchowego podziału krawędzi. Pachner jawnie jako przyjmowany wynik z bibliografią, a nie udowodniony globalnie.
- Drobne korekty definicji realizacji, zwartości, homologii niezredukowanej i d_0 d_1=0. Rysunek czworościanu: kolor i podpis zewnętrznej ściany; wcześniej zewnętrzna ściana była zasłonięta trzema wypełnieniami. Nowy PDF wymaga oględzin.

## Trwała regresja
GKT-20-LINK-MOVES-01: test_gkt20_link_moves.js, commit 4a5e5538482e627b4b8edaea7d9fbfe44e2a5dcb.
PASS: 1044 przypadki (wszystkie podzbiory trójkątów na 3–5 etykietach plus dwie konstrukcje specjalne), 17 przypadków spełniających warunek powierzchni spójnej, 92 ruchy 1->3 z odwróceniem, 42 dopuszczalne 2->2, 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi, jeden jawny przypadek dwóch sfer sklejonych w wierzchołku z niespójnym ogniwem. Nie są to liczby klas izomorfizmu. Kontrole kombinatoryczne, nie dowód topologiczny i nie Lean.
Wykonano dwukrotnie w izolacie JS, w tym po pobraniu zapisanego pliku. Nie w procesie Node i nie podłączono nowego skryptu do CI.
7 etykiet zachowanych, 48 poprawnie zagnieżdżonych par środowisk.

## Bramka i propozycja zakresu
Terminologia 45571962580 SUCCESS; algorytmy 45571962406, aplikacja 45571962572, pełny audyt 45571962481 w toku przy kontroli. Nie oglądano PDF po korekcie.
Opcjonalne rozszerzenie po pierwszym audycie: kryterium ogniwa dla powierzchni z brzegiem (okrąg albo odcinek, wraz z odpowiednim stopniem krawędzi) oraz orientowalność triangulacji przez zgodne orientacje trójkątów. Nie dodano bez decyzji użytkownika. W kolejnych iteracjach nie rozszerzać zakresu samodzielnie.
Etap A otwarty; audyt 192: stabilizacja, kontrola zależności, pełnego CI i PDF. Nie przechodzić do następnego rozdziału.
