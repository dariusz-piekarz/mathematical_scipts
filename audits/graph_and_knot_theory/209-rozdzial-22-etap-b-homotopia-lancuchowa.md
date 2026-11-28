# Audyt 209 — drukowany rozdział 22, niezależny etap B

Data: 2026-11-25. Etap A zamknięto w 208.
Źródło: chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex.
Blob wejściowy 2ad61fc865659e0e80951f78b53e415e82ecee9d.
Korekta 05684b16437814f248588cefa27e626bc4bdd056, blob a7be1b39417ef4da80481afd2cfba70bbdac8008.

## Niezależna kontrola i poprawki
- GKT-22-B-BASIS-01: jawne odwrotne podstawienia w obu zmienianych bazach, w tym nad Z przy elemencie głównym ±1. Uzasadnienie, że oba składniki sumy prostej są podkompleksami, a nie tylko podprzestrzeniami.
- GKT-22-CONTRACTION-01: rachunek homotopii na obu usuwanych generatorach, uzasadnienie łańcuchowości włączenia i rzutu; jawne formuły w pierwotnych bazach, w tym pi(a)=-lambda^{-1}sum B_y bar y, i(bar x)=x-mu_x lambda^{-1}b, h(a)=lambda^{-1}b. Tożsamości pi i=id i id-i pi=dh+hd. Wniosek o redukcji nad Z uzupełniono o całkowite odwrotne zmiany baz i składanie równoważności.
- GKT-22-B-CRITICAL-01: rozróżniono generatory indeksowane przez krytyczne sympleksy od pierwotnych łańcuchów; redukcja nie musi odpowiadać podkompleksowi symplicjalnemu. Uzasadniono składanie homotopii przez odwzorowania łańcuchowe.
- GKT-22-B-REF-01: zweryfikowano wzór Eulera–Poincarégo w źródle 13; dodano odsyłacz do wcześniej sprawdzonego twierdzenia thm:tg-wedge dla doskonałości parowania na grafie nad dowolnym ciałem, z przypomnieniem o podziale pętli. Nie rozszerzano zakresu. Twierdzenie topologiczne Formana pozostaje przyjmowane z literatury.
- Ponownie przejrzano równoważność parowania z funkcją Morse'a, wolne kolapsy, torsję RP2, nierówności, drzewo–drzewo dualne i triangulację okresową. Zachowano 13 etykiet, 37 poprawnie zagnieżdżonych par środowisk (nowe aligned).

## Regresje
Nowy GKT-22-CONTRACTION-01, test_gkt22_contraction.js, commit e26deaf219435c95738e401b8162297ea3b33da7.
PASS: 240 deterministycznie wygenerowanych kompleksów wolnych grup abelowych z pięcioma stopniami i unimodularnymi zmianami baz; 136 przypadków z dostępnym jednostkowym elementem głównym w zadanej różniczce, 104 pominięto z braku takiego elementu (nie błędy), 76 elementów głównych -1, 136 nietrywialnych włączeń lub rzutów, 680 kontroli stopni. 960 bloków o współczynnikach torsyjnych w kompleksach wejściowych przed zmianami baz. Dokładna arytmetyka BigInt, sprawdzenie d^2=0, pi i=id, id-i pi=dh+hd, obu warunków odwzorowań łańcuchowych, Schura i ograniczeń sąsiednich różniczek. Nie jest to ogólny algorytm postaci Smitha ani bezpośredni pomiar torsji w każdym przypadku.
Poprzednie regresje PASS: CANCEL-01 (240 kompleksów, 3652 eliminacje, 1920 porównań nad ciałami), TREE-COTREE-01 (120 konstrukcji, 3936 eliminacji, 24 RP2 z d2=±2), FUNCTION-COLLAPSE-01 (16384 przypisania, 42 parowania, 12005 kontroli homotopii). Wszystkie cztery pobrano i wykonano w izolacie JS, nowy także przed zapisem. Nie potwierdzono integracji z CI ani wykonania w procesie Node. Nie Lean.

## Bramka
Dla 05684b16: terminologia 45584509261 SUCCESS, algorytmy 45584509040, pełny audyt 45584509070 i aplikacja 45584509113 w toku. PDF najnowszej wersji nie oglądano; nie przeniesiono wyników poprzedniego SHA. Etap B otwarty. Następny audyt 210: kontrola poprawek, CI i PDF, stabilizacja bez niezatwierdzonych rozszerzeń. Postęp 21/44.
