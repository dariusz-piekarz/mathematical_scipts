# Audyt 193 — drukowany rozdział 20, etap A: PDF i rysunki

Data: 2026-11-25. Kontynuacja 192 bez rozszerzania zakresu.
Źródło chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Wejściowy commit 73f6d907d40e49a6cfd2f0cac3dd2872c9ec61e4, blob 686c99ef9827ca8a323b3cf7dc3277ccdd2f647e.
Korekta 0991cb332182507dee3db82b357f048324b44969, blob 52e28adc146a90688df02e04f1b225efcde82c59.

## CI i PDF
Dla wejściowego SHA: terminologia 45572212154, aplikacja 45572212144, pełny audyt 45572212254, algorytmy 45572212307 — wszystkie SUCCESS.
Pobrano artefakt 15002447757. PDF 343 strony, plik ostrzeżeń 0 bajtów. Rozdział 20: strony fizyczne 172–178, drukowane 162–168; 7 stron, 1 adnotacja odsyłacza. Wyrenderowano każdą stronę w skali 1.6 i obejrzano oba arkusze kontaktowe. Stwierdzono kolizję oznaczeń a,b z podpisem liczbowym oraz c z etykietą ściany zewnętrznej na rysunku czworościanu. Poprawiono odstępy, położenia oznaczeń i tła. Na rysunku ruchu 2->2 brakowało oznaczeń wierzchołków mimo podpisów przekątnych ac,bd; dodano wszystkie cztery po obu stronach. Dodano preferowany podział strony przed stwierdzeniem o subdywizji, aby ograniczyć rozdzielenie twierdzenia i dowodu. Nie zmieniono treści matematycznej. Skuteczność korekt wymaga nowego PDF.

## Zależności i regresje
Odczytano rozdziały źródłowe 17–22; nie znaleziono wystąpień ogniw, operatorname{Lk}, pustego sympleksu ani dwóch etykiet rozdziału w zastosowanym przeszukaniu tekstowym. Wcześniej sprawdzono 14–16. Pozostają źródła 23–43; nie uznajemy całego przeszukania za zakończone. Nie dodano proponowanych rozszerzeń.
GKT-20-LINK-MOVES-01 PASS: 1044 przypadki, 17 powierzchni w próbach, 92 ruchy 1->3, 42 dopuszczalne i 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi.
GKT-20-CHAIN-01 PASS: 873 uporządkowania, 873 kontrole brzegu brzegu, 4166 transpozycji, 2197 trójek całkowitych, 503 nad ciałami skończonymi.
Oba zapisane skrypty wykonano przed i po korekcie w izolacie JS. Nie w procesie Node, nie Lean; nie potwierdzono wywołania przez CI. 7 etykiet i 48 poprawnie zagnieżdżonych par środowisk zachowanych. Nie zidentyfikowano nowych istotnych błędów matematycznych podczas kontroli PDF.

## Bramka
Dla 0991cb3: pełny audyt 45572737213 w toku, algorytmy 45572737294 oczekują, aplikacja 45572737085 i terminologia 45572737114 w toku przy kontroli. Nie oglądano PDF po korekcie. Etap A otwarty; audyt 194: kontynuacja zależności, potwierdzenie CI/PDF i stabilizacja. Nie przechodzić do etapu B przed bramką.
