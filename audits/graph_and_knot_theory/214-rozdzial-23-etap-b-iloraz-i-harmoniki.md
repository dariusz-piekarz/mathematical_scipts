# Audyt 214 — drukowany rozdział 23, niezależny etap B

Data: 2026-11-25. Etap A zamknięto w 213.
Źródło: chapters/pl/graph_and_knot_theory/16-od-triangulacji-do-topologii-i-geometrii-rozmaitosci.tex.
Blob wejściowy 3c9c08a9577bfbf20f7d2e173d5d9a8684a38c2f.
Korekta 5bef53311b40dcb53ab4e733cb35c0c91feaa954, blob 176cf68b3634dd1a36f1290e51221929d664cf17.

## Niezależna kontrola i poprawki
- GKT-23-B-QUOTIENT-01: wypowiedziano jawnie założenie braku dodatkowych utożsamień wierzchołków. Z domkniętości relacji wykazano domkniętość mapy ilorazowej przez rzut zwartego zbioru (F x X) przecinającego relację; nie zakładano wcześniej własności Hausdorffa ilorazu. Rozłączne zwarte włókna mają rozłączne otwarte otoczenia U,V w X; Y\q(X\U) i Y\q(X\V) rozdzielają ich obrazy. Następnie drugi aksjomat przeliczalności jak wcześniej.
- GKT-23-B-RADIAL-01: sklejanie homeomorfizmów boków i odwrotności, homeomorfizm stożka nad brzegiem z trójkątem przez promienie od środka ciężkości, jawna ciągłość przedłużenia i odwrotności przez topologię ilorazową.
- GKT-23-B-EDGE-01: otwarte nasycone paski przy dwóch wystąpieniach boku, z jednakowym parametrem wzdłuż sklejonego odcinka i przeciwnymi parametrami poprzecznymi; lokalny model otwartego prostokąta. Uwzględniono dwa boki tego samego trójkąta.
- GKT-23-HARMONIC-MIN-01: nazwano elementy jądra laplasjanu kołańcuchami harmonicznymi; jawna jednoznaczność reprezentanta z injektywności oraz tożsamość Pitagorasa dla wszystkich reprezentantów tej samej klasy (konsekwencja udowodnionego rozkładu, nie nowy zakres). Doprecyzowano orientację dwusympleksu w przykładzie.
- Ponownie przejrzano pełny rozdział, w tym automatyczną spójność ogniw, model stożkowy, składowe dualne, ważone sprzężenia i kohomologię. Zachowano 5 etykiet, 13 poprawnie zagnieżdżonych par środowisk. Pierwszy zapis napotkał konflikt 409 na gałęzi; ponowny odczyt potwierdził niezmieniony blob i zapisano korektę, nie nadpisując innych plików.

## Regresje
Nowy GKT-23-HARMONIC-MIN-01, test_gkt23_harmonic_min.js, commit 6be1d21de836057ed2c9540dba402e1393f86d39. PASS: 196 dodatnio określonych macierzy Grama, 24500 par metryka–reprezentant na cyklu C3, w tym 24260 ścisłych nierówności norm i 240 przypadków równości. Dokładna arytmetyka BigInt po przeskalowaniu wspólnym dodatnim mianownikiem; sprawdzono harmoniczność, przynależność do tej samej klasy przez jawny kobrzeg, ortogonalność i tożsamość Pitagorasa. Nie test ogólnych kompleksów ani dowód formalny.
Ponownie wykonano GLUE-01 (120 modeli, 222 ogniwa), HODGE-01 (196 metryk), LINK-COMPONENTS-01 (480 modeli, 1836 ogniw, 116 niespójnych, 399 dodatkowych identyfikacji). Wszystkie cztery PASS po odczycie z repozytorium w izolacie JS, nowy także przed zapisem. Nie potwierdzono wykonania w procesie Node ani integracji regresji z CI; nie Lean.

## Bramka
Dla 5bef5331: terminologia 45587309705 SUCCESS; pełny audyt 45587309687, aplikacja 45587309694, algorytmy 45587309887 w toku. Nie oglądano PDF najnowszego SHA. Etap B otwarty. Następny audyt 215: kontrola poprawek B, CI i rzeczywiste oględziny PDF. Bez niezatwierdzonych rozszerzeń. Postęp 22/44.
