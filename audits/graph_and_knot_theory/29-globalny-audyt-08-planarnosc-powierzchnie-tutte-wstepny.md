# Teoria grafów i węzłów — globalny audyt 08: historyczne rozdziały 10–12, iteracja 01

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: audyt w toku; pełny przebieg CI oraz wizualny przegląd PDF wymagają potwierdzenia przed lokalną stabilizacją.**

## Audyt matematyczny

### Rozdział 10 — planarność i kolorowania

Skontrolowano definicje subdywizji, podgrafu topologicznego, minora i zewnętrznej planarności, dowody zachowania planarności przez subdywizję i operacje minorowe, ograniczenie \`m<=2n-3\` dla prostych grafów zewnętrznie planarnych oraz dowód twierdzenia o pięciu kolorach oparty na łańcuchach Kempego i twierdzeniu Jordana.

**Istotne zastrzeżenie:** w rozdziale Kuratowski ma tylko samodzielny dowód kierunku „planarny ⇒ nie zawiera odpowiednich subdywizji”. Kierunek odwrotny jest **jawnie cytowanym wynikiem zewnętrznym**, nie pełnym udowodnionym twierdzeniem w tym skrypcie. Twierdzenie Wagnera jest uzyskane pod warunkiem przyjęcia pełnego Kuratowskiego. Audyt globalny nie może przypisać brakującego dowodu do rezultatów „sprawdzonych od początku do końca”; ewentualne pełne rozwinięcie jest odrębnym zadaniem.

**Rozwinięcie:** wprowadzono szczegółowo udowodniony lemat o istnieniu wierzchołka stopnia co najwyżej dwa w każdym prostym grafie zewnętrznie planarnym. W dowodzie wykorzystano triangulację wielokąta i drzewo jej trójkątów. Wyprowadzono stąd pełne elementarne twierdzenie, że każdy skończony prosty graf zewnętrznie planarny jest **trzykolorowalny**. Dla grafu pustego podano przypadek brzegowy. Nowe stwierdzenia umieszczono po definicji poprawnego kolorowania.

### Rozdział 11 — grafy komórkowo zanurzone w powierzchniach

Skontrolowano konieczność komórkowości przy liczeniu \`n-m+f\`, konstrukcję orientowalnej powierzchni z układu rotacji, model półkrawędzi i ścian jako cykli permutacji \`sigma alpha\`, a także rachunek rodzaju powierzchni. Zweryfikowano oba schematy układów rotacji multigrafu theta: 3 ściany na sferze i 1 na torusie.

Weryfikowano związek między mostami grafu płaskiego a pętlami w dualu, konstrukcję dualnego drzewa rozpinającego i rozkład komórkowy \`C_2 -> C_1 -> C_0\`. Zwrócono uwagę na orientację łańcuchów brzegowych i możliwość występowania pętli grafu dualnego. Argument o jądrze \`partial_2\` opiera się na spójności grafu dualnego i przeciwnych orientacjach dwóch stron każdej krawędzi, prowadząc do wymiarów homologii \`(1,2g,1)\`.

### Rozdział 12 — wielomian Tutte'a

Sprawdzono definicję \`T_G(x,y)\` przez sumę po wszystkich zbiorach krawędzi (również dla pętli, krawędzi równoległych i grafu bez krawędzi). Kontrolowano trzy gałęzie rekurencji usuwania/kontrakcji, specjalizacje \`T_G(1,1)\` i \`T_G(2,1)\`, inkluzję i ekskluzję wielomianu chromatycznego oraz wzór \`P_G(q)=(-1)^{n-c}q^c T_G(1-q,0)\`. Sprawdzono algebraiczne przejście w dualności \`T_{G*}(x,y)=T_G(y,x)\` oraz bijekcję między przepływami modulo \`q\` i kolorowaniami ścian, z czynnikiem \`q\`.

Symbol \`tau(G)\` pozostaje liczbą drzew rozpinających, odróżnioną w poprzedniej iteracji od \`tau_V(G)\` dla pokrycia wierzchołkowego. Nie zmieniono dotychczasowych dowodów Tutte'a.

## Nowy niezależny zestaw modeli skończonych

Utworzono \`tools/tests/test_graph_and_knot_planar_surface_tutte.py\`. Weryfikuje:
1. Całkowite wartości wielomianu Tutte'a obliczane **dwoma niezależnymi sposobami**: przez wszystkie podzbiory krawędzi oraz rekurencję usuwania/kontrakcji z jawnym rozpoznawaniem pętli i mostów.
2. Wielomian chromatyczny w trzech ujęciach: bezpośrednia enumeracja kolorowań, włączenia i wyłączenia i specjalizacja Tutte'a. Dodatkowo policzone są maksymalne lasy rozpinające.
3. Macierze brzegowe \`partial_1\`, \`partial_2\` z cykli permutacji półkrawędzi układów rotacji; ich złożenie, rzędy nad \`Q\` i wymiar \`H_1=2g\` dla powierzchni orientowalnej.
4. Planarną dualność Tutte'a, dopełnienie drzewa rozpinającego dualnym drzewem oraz równość \`P_{G*}(q)=q F_G(q)\` porównaną z bezpośrednią enumeracją przepływów modulo 2 i 3.
5. Rozpoznawanie zewnętrznie planarnych osadzeń przez występowanie ściany incydentnej ze wszystkimi wierzchołkami, ograniczenie liczby krawędzi oraz trzykolorowalność, z niezależnym sprawdzeniem \`K_4\` i \`K_{2,3}\`.
6. Kontrast \`K_5\`, \`K_{3,3}\`, \`K_5-e\`, grafów cyklicznych i grafu kołowego na sześciu wierzchołkach.

Testy są wyłącznie skończonymi modelami i kontrolą poszukiwania kontrprzykładów. Nie poświadczają trudnego kierunku Kuratowskiego ani twierdzeń dla dowolnie dużych grafów.

## Plan do stabilizacji

1. Wykonać CI pełnej książki i wszystkie regresje historyczne 01–12.
2. Zanalizować bezpośrednio liczby przypadków i ewentualne niepowodzenia niezależnych modeli, poprawić kod lub argumenty źródłowe.
3. Potwierdzić trzy kompilacje całej książki, brak ostrzeżeń i kolizji w rysunkach rozdziałów 10–12.
4. Zweryfikować redakcyjne odniesienia między planarnymi kryteriami, homologią powierzchni i dualnością Tutte'a.
5. Opisać jawnie ograniczony status dowodu Kuratowskiego; nie ogłaszać pełnego udowodnienia odwrotnej implikacji.

Status całego skryptu: **globalny audyt nadal w toku**.
