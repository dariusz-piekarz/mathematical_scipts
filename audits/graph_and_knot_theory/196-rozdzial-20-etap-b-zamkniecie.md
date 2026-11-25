# Audyt 196 — drukowany rozdział 20, zamknięcie etapu B

Data: 2026-11-25. Kontynuacja 195 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Commit źródłowy eb987ce92073a01273a166e2a0c4d121306e14e5, blob 71b95c62b6094e4607f0c868a89522a8b4c92858 potwierdzony na gałęzi. Bez zmian źródła.

## Stabilizacja semantyczna
- B-REAL-01 PASS: nośnik punktu wyznacza najmniejszy sympleks, przecięcie realizacji odpowiada przecięciu nośników; wierzchołki jako wektory bazowe.
- B-LOCAL-01 PASS: skończoność daje dodatni dystans do sympleksów niezawierających krawędzi; w każdym incydentnym trójkącie przekrój ma postać półdysku. Retrakcja radialna zgodna na średnicach. Homologia grafu k łuków jest jądrem sumy współczynników, o bazie różnic względem pierwszego łuku. Sprawdzono warunek k>=1 oraz wymuszenie k=2.
- B-EXCISION-01 PASS: dopełnienie otwartego otoczenia jest domknięte i nie zawiera badanego punktu; spełnia warunek wycięcia dla pary (|K|, |K| minus punkt). Przekrój t_v=1-epsilon/2 należy do przebitego otoczenia; deformacja zachowuje zakres parametru. H1 pary odpowiada jądru sumowania H0, a więc zredukowanemu H0 niepustego ogniwa. Dla powierzchni lokalne H1=0, stąd ogniwo spójne.
- B-CHAIN-01 PASS: po jednym generatorze na sympleks, znaki transpozycji i znoszenie par składników brzegu brzegu, rząd-jądro i teleskopowanie w charakterystyce Eulera. Rachunek trójkąta poprawny.
- B-GLUE-01 PASS: nowe wierzchołki/krawędzie/trójkąty spełniają warunki dopuszczalności; pozostały podkompleks przecina dysk w brzegu. Afiniczne mapy do wspólnego modelu wypukłego zgadzają się na brzegu, złożenie z odwrotnością i lemat o sklejaniu dają homeomorfizm z ciągłą odwrotnością. Podział krawędzi przez dwa ruchy zachowuje cztery wymagane trójkąty. Twierdzenie Pachnera pozostaje jawnym wynikiem przyjmowanym, nie dowiedzionym w tym rozdziale.
Nie zidentyfikowano nowych istotnych usterek. Zachowano 7 etykiet i 48 poprawnie zagnieżdżonych par środowisk. Kontrola zależności 30 dalszych plików została zakończona w 194; brak zmian konwencji względem tej wersji.

## CI i PDF
Dla eb987ce92073a01273a166e2a0c4d121306e14e5: pełny audyt 45573421948, algorytmy 45573421951, terminologia 45573421919, aplikacja 45573421989 — wszystkie SUCCESS.
Pobrano artefakt 15003626651 i rozpakowano. PDF 343 strony, plik ostrzeżeń 0 bajtów. Rozdział 20: fizyczne strony 172–178, druk 162–168; rozdział 21 zaczyna się na 179. Jedna adnotacja odsyłacza. Wyrenderowano wszystkie siedem stron w skali 1.5 i obejrzano dwa arkusze kontaktowe. Wszystkie cztery schematy czytelne, bez zauważalnych kolizji i obcięć; stwierdzenie o podziale krawędzi i dowód mieszczą się na ostatniej stronie. Przykład trójkąta i fragmenty dłuższych dowodów przechodzą przez granice stron, ale układ pozostaje czytelny. Nie wprowadzano kosmetycznych poprawek.

## Regresje
Ponownie pobrano i wykonano trzy zapisane skrypty:
- GKT-20-LINK-MOVES-01 PASS: 1044 przypadki, 17 spełniających warunek spójnej powierzchni, 92 ruchy 1->3, 42 dopuszczalne i 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi, 1 przypadek niespójnego ogniwa.
- GKT-20-CHAIN-01 PASS: 873 orientacje, 873 kontrole brzegu brzegu, 4166 transpozycji, 2197 trójek całkowitych, 503 nad ciałami skończonymi.
- GKT-20-LOCAL-01 PASS: 1100 grafów, 16 modeli k półdysków, 8 sum cykli, 4496 kontroli nad F2,F3,F5,F7.
Skrypty wykonane w izolacie JS, nie w procesie Node; nie potwierdzono wywoływania ich przez CI. Skończone próby nie zastępują dowodów ani formalizacji Lean.

## Decyzja
Etap B zamknięty dla wskazanego blobu; rozdział 20 zakończony po etapach A i B. Postęp 20/44. Nie dodano niezatwierdzonych propozycji dotyczących powierzchni z brzegiem i orientowalności. Następny audyt 197: pierwszy audyt A drukowanego rozdziału 21, Grafy Reeba i funkcje Morse'a na powierzchniach.
