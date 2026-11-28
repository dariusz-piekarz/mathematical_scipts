# Audyt 195 — drukowany rozdział 20, niezależny etap B

Data: 2026-11-25. Etap A zamknięto w 194.
Źródło: chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Blob wejściowy 52e28adc146a90688df02e04f1b225efcde82c59.
Korekta eb987ce92073a01273a166e2a0c4d121306e14e5, blob 71b95c62b6094e4607f0c868a89522a8b4c92858.

## Niezależna kontrola B
- GKT-20-B-REAL-01 (semantyczna): określono realizacje poszczególnych sympleksów, ich przecięcia przez nośniki, identyfikację wierzchołka z wektorem bazowym; poprawiono v in K na v in V.
- GKT-20-B-LOCAL-01 (semantyczna): uzasadniono stopień dwa w grafie homeomorficznym z okręgiem, lokalny model k półdysków przez kulę w realizacji barycentrycznej i rozłączność poza średnicą. Rozpisano homologiczny rachunek k-1 przez macierz brzegu grafu k równoległych łuków.
- GKT-20-B-EXCISION-01 (semantyczna): odróżniono przekrój stożka zawarty w przebitym otoczeniu od samego ogniwa leżącego poza nim; jawny warunek wycięcia, fragment ciągu dokładnego i jądro augmentacji H0. Kontrolować także niepuste ogniwo, czystość i przypadek niespójnego ogniwa.
- GKT-20-B-CHAIN-01 (semantyczna): jawnie wskazano jeden generator na sympleks abstrakcyjny, pozostałe orientacje określone przez znak. Sprawdzono wzór brzegu, zgodność ze zmianą orientacji i obliczenie H0/H1 trójkąta.
- GKT-20-B-GLUE-01 (semantyczna): opisano złożenie map do wspólnego wypukłego modelu oraz przecięcie dysku z pozostałym podkompleksem dokładnie w brzegu w każdym ruchu; użyto lematu o sklejaniu na zbiorach domkniętych także dla odwrotności. Rozróżniono kierunki ruchów.
- Bez rozszerzania zakresu, bez zmiany rysunków. Zachowano 7 etykiet i 48 poprawnie zagnieżdżonych par środowisk. Nie dodano kryterium powierzchni z brzegiem ani orientowalności. Pachner pozostaje jawnie przyjmowanym klasycznym twierdzeniem.

## Trwałe regresje
Nowy GKT-20-LOCAL-01: test_gkt20_local.js, commit e62ce8f696410a588e19afebec16e75ea1382f09.
Niezależna konstrukcja względnego kompleksu łańcuchów stożek/podstawa, macierze brzegu i eliminacja nad F2,F3,F5,F7. PASS: 1100 grafów na 0–5 etykietach, 16 modeli k półdysków przez stożek nad K_{2,k}, 8 sum rozłącznych cykli, 4496 kontroli nad ciałami. Obejmuje pustą podstawę (względne H0), przypadki k=1,2,3 i więcej, niespójne ogniwo. Nie jest dowodem wycięcia ani formalizacją Lean.
LINK-MOVES-01 PASS: 1044 przypadki, 17 spełniających kryterium powierzchni, 92 ruchy 1->3, 42 dopuszczalne i 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi.
CHAIN-01 PASS: 873 uporządkowania, 873 kontrole brzegu brzegu, 4166 transpozycji, 2197 trójek całkowitych, 503 nad ciałami.
Wszystkie trzy skrypty wykonane po odczycie repozytorium w izolacie JS; nowy test wykonany dwukrotnie. Nie w procesie Node, nie potwierdzono automatycznego wywołania przez CI. Kryteria semantyczne pozostają odrębnymi kontrolami.

## Bramka
Dla eb987ce: terminologia 45573421919 SUCCESS; algorytmy 45573421951, aplikacja 45573421989 i pełny audyt 45573421948 w toku. Nowy PDF nie był oglądany. Etap B otwarty do stabilizacji. Następny audyt 196: ponowny przegląd poprawek, CI i PDF. Nie przechodzić jeszcze do rozdziału 21.
