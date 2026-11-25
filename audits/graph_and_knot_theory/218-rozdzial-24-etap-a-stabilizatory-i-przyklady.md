# Audyt 218 — drukowany rozdział 24, stabilizacja A: graf grup z działania

Data: 2026-11-25. Kontynuacja 217 bez niezatwierdzonych rozszerzeń.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Blob wejściowy 2e1000789fce40b7e9098e6bd9a8ac71037e89f6.
Korekta 7dd1dbfaf127259219f733a2c53bb6626599cbf2, blob a6830b28deff06af43d16bb8bec3de449fc6b3a7.

## Poprawki
- GKT-24-ACTION-03: jawne automorfizmy Cayleya przez lewe translacje, z zachowaniem etykiet. Izomorfizm grupy fundamentalnej ilorazu z G przez końce podniesionych pętli; homomorficzność dla konkatenacji od lewej do prawej, niezmienniczość homotopijna, injektywność i surjektywność.
- GKT-24-ACTION-DATA-01: dla działania bez inwersji na niepustym drzewie wybrano kopię drzewa rozpinającego ilorazu przez podnoszenie krawędzi według odległości od korzenia. Wybór podniesienia e o początku w reprezentancie o(e), element h_e przenoszący jego koniec na reprezentanta t(e), h_e=1 na drzewie. Monomorfizmy iota_-(c)=c, iota_+(c)=h_e c h_e^{-1}; jawne uzasadnienie docelowych stabilizatorów i injektywności. Prezentacja wyznacza homomorfizm na stabilizatorach przez inkluzje i t_e->h_e. Jego izomorficzność nadal przyjęta z fundamentalnego twierdzenia Bassa–Serre'a, nie przedstawiana jako samodzielnie dowiedziona. Dla orientacji odwrotnej zamiana monomorfizmów i odwrotna litera.
- GKT-24-EXAMPLES-01: iloczyn wolny Z*Z wynika z prezentacji bez relacji między generatorami; jawne wzajemnie odwrotne homomorfizmy prezentacji torusa i Z², model podwójnego cylindra z identycznościami i ciągła bijekcja zwartego ilorazu na S¹×S¹. Przykład C2*C3: krawędzie indeksowane elementami iloczynu, końce gC2 i gC3, liczba incydencji równa rzędowi odpowiedniej grupy.
- Zachowano 5 etykiet; 30 poprawnie zagnieżdżonych par środowisk. Pięć wystąpień ref, cele w źródle 07 zweryfikowanym wcześniej. Zakres nie rozszerzony o proponowane rysunki, postać normalną amalgamacji ani lemat Brittona.

## Regresje
Nowy GKT-24-FREE-PRODUCT-01, test_gkt24_free_product.js, commit 8cb9666f6fb226dee0a720ef09050f7a6dc7a296. PASS: 218 słów zredukowanych C2*C3 o długości sylabowej 0–10, 219 wierzchołków i 218 krawędzi skończonego podgrafu, spójność i acykliczność podgrafu, 1090 kontroli incydencji (stopnie pełnych gwiazd 2 i 3, niezależność reprezentantów), 654 kontroli lewych translacji przez nietrywialne elementy czynników. Algorytm korzysta z redukowanych naprzemiennych sylab; nie jest dowodem ogólnej postaci normalnej ani acykliczności całego nieskończonego drzewa.
Ponownie PASS: CAYLEY-01 (380 modeli cyklicznych, 4308 słów, 31892 przejścia); COSET-01 (585 prób reprezentantów, 1755 odwróceń, 15795 zmian reprezentanta, 5265 translacji, 4094 relacje rodzic–dziecko w ograniczonym modelu afinicznym).
Wszystkie trzy skrypty wykonano po odczycie z repozytorium w izolacie JS; nowy także przed zapisem. Nie potwierdzono integracji z CI ani wykonania w procesie Node. Nie formalizacja Lean.

## Bramka
Dla 74c5971f terminologia 45588271030 i pełny audyt 45588270968 SUCCESS, algorytmy 45588270912 i aplikacja 45588270992 w toku przy końcowym odczycie.
Dla 7dd1dbfa pełny audyt 45588642579, aplikacja 45588642607, algorytmy 45588642566, terminologia 45588642803 w toku. PDF najnowszej wersji nie oglądano. Nie przeniesiono wyników ze starszego SHA.
Etap A otwarty. Następny audyt 219: kontrola stabilizacyjna, zgodność konstrukcji z działaniem, odsyłacze, CI oraz rzeczywiste oględziny PDF. Postęp 23/44.
