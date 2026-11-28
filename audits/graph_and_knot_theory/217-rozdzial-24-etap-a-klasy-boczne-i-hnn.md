# Audyt 217 — drukowany rozdział 24, stabilizacja A: klasy boczne i HNN

Data: 2026-11-25. Kontynuacja 216 bez niezatwierdzonych rozszerzeń.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Blob wejściowy b041226a6aea62eedb4be28a8e5ec25ea95dc5bd.
Korekta 74c5971f06d86a2d071028fece6da6fa0cd837bf, blob 2e1000789fce40b7e9098e6bd9a8ac71037e89f6.

## Poprawki
- GKT-24-CAYLEY-02: jawne założenie, że wybrane a_i tworzą wolną bazę, nie tylko układ generatorów.
- GKT-24-ACTION-02: zorientowane krawędzie ilorazu jako orbity z inwolucją odwracania bez punktów stałych przy braku inwersji; zgodna orientacja i liniowe przedłużenie działania na realizację CW. Jednoznaczność przekształcenia pokładowego przez jednoznaczność podniesień dróg. Rozpisano argument Zorna dla drzewa rozpinającego dowolnego spójnego grafu.
- GKT-24-HNN-02: jawne deformacje kołnierzy podwójnego cylindra oraz ciągłość homotopii przez topologię ilorazową i iloczyn z przedziałem (lem:tg-collapse-CW). Homotopia relacji sprzężenia jako kwadrat (r,s)->[(c(r),s)]. Zmiana ścieżek bazowych: iota'±*=u± iota±* u±^{-1}, t'=u+ t u-^{-1}; odwracalne podstawienia. Homomorfizm HNN na Z zerujący grupę bazową i wysyłający t na 1 uzasadnia konieczność dodatkowej litery.
- GKT-24-COSET-01: przy konwencji t_e iota_- t_e^{-1}=iota_+ półkrawędź typu e reprezentowana przez g iota_-(G_e) ma początek gG_o i koniec g t_e^{-1}G_t. Wykazano niezależność od reprezentanta, wzór na odwróconą półkrawędź, inwolucyjność i zgodność z lewymi translacjami. Typy pozostają osobną częścią danych. Fakt, że graf klas bocznych jest drzewem, nadal przyjmujemy z fundamentalnego twierdzenia Bassa–Serre'a. W BS(1,2) jawnie przypisano identyczność do iota_-, mnożenie przez dwa do iota_+.
Zachowano 5 etykiet i 29 poprawnie zagnieżdżonych par środowisk. Cztery odsyłacze, wszystkie cele występują w sprawdzonym w 216 źródle 07.

## Regresje
GKT-24-CAYLEY-01 ponownie PASS: 380 modeli cyklicznych, 4486 wierzchołków, 12724 krawędzi, 41 niespójnych; 4308 słów zredukowanych, 31892 przejścia.
Nowy GKT-24-COSET-01, test_gkt24_coset.js, commit 76dd9aeab43ac32bb0af7ef8a27a8af6012b1105. PASS: dokładna arytmetyka BigInt w afinicznym modelu x->2^k x+b/256, 585 prób reprezentantów wierzchołków, 1755 incydencji i odwróceń, 15795 kontroli zmiany reprezentanta, 5265 kontroli zgodności z lewymi translacjami, 2047 wierzchołków modelu reszt dwójkowych w ograniczonych poziomach, 4094 kontrole powrotu dziecka do rodzica. Sprawdzono relację HNN, nieprzemienność, stopień trzy i jeden niższy sąsiad. Nie udowodniono wierności reprezentacji afinicznej ani ogólnego twierdzenia o drzewie; model ilorazowy, ograniczona siatka, nie enumeracja wszystkich klas bocznych.
Oba skrypty wykonano po odczycie z repozytorium w izolacie JS; nowy również przed zapisem. Nie potwierdzono integracji z CI ani uruchomienia w procesie Node; nie Lean.

## Bramka
Dla f3f6fc82 terminologia 45587950648, algorytmy 45587950969, pełny audyt 45587950996 SUCCESS, aplikacja 45587950778 w toku przy ostatnim odczycie.
Dla 74c5971f algorytmy 45588270912, terminologia 45588271030, aplikacja 45588270992 i pełny audyt 45588270968 queued. PDF najnowszego SHA nie oglądano.
Etap A otwarty. Następny audyt 218: stabilizacja konstrukcji grafu grup z działania, przykładu C2*C3 i torusa, kontrola odsyłaczy, CI i PDF. Postęp 23/44.
