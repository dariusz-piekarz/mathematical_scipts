# Audyt 192 — drukowany rozdział 20, stabilizacja A (łańcuchy symplicjalne)

Data: 2026-11-25. Kontynuacja 191 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Blob wejściowy d8ee6fbd913f936d93aabab730abde06c92fc33b.
Korekta 73f6d907d40e49a6cfd2f0cac3dd2872c9ec61e4, blob 686c99ef9827ca8a323b3cf7dc3277ccdd2f647e.

## Poprawki
- GKT-20-CHAIN-01: uzasadniono zgodność wzoru operatora brzegu z relacją orientacji przez transpozycje sąsiednie. Rozpisano rachunek jądra i obrazu w przykładzie trójkąta, także H0.
- Uzupełniono warunek przeliczalnej bazy topologii w dowodzie kryterium powierzchni.
- Brzeg czworościanu: uzasadniono homeomorfizm ze sferą przez rzut radialny, oznaczono wierzchołki na rysunku.
- Poprawiono określenia symplicjalne, afiniczne oraz podpis ruchu 1->3 (brzeg dysku, nie powierzchni zamkniętej).
- Zachowano 7 etykiet i 48 poprawnie zagnieżdżonych par środowisk.
- Kontrola dalszych zależności: rozdziały źródłowe 14 i 15 sprawdzone w 191; w 16 znaleziono użycia geometrycznego ogniwa, bez odwołania do pustego sympleksu. Pełne przeszukanie 14–43 napotkało limit wywołań narzędzi; nie uznajemy kontroli całego tomu za zakończoną.

## Trwałe regresje
GKT-20-LINK-MOVES-01 PASS: 1044 przypadki, 17 spełniających warunki spójnej powierzchni, 92 ruchy 1->3, 42 dopuszczalne i 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi.
Nowy GKT-20-CHAIN-01, test_gkt20_chains.js, commit 1f1e6321ec38c3e8951b368690ca438a48063c54: PASS 873 uporządkowania sympleksów (do 6 wierzchołków), 873 kontrole brzegu brzegu, 4166 transpozycji sąsiednich, 2197 trójek całkowitych w przykładzie trójkąta, 503 trójki nad 4 ciałami F2,F3,F5,F7. Test skończony, nie formalizacja Lean. Nowy test wykonano dwukrotnie, drugi raz po odczytaniu z repozytorium. Oba skrypty wykonano w izolacie JS, nie w procesie Node; nie potwierdzono ich wywołania przez CI.

## CI i bramka
Dla 5a5186d: algorytmy 45571962406, terminologia 45571962580, pełny audyt 45571962481, aplikacja 45571962572 — wszystkie SUCCESS.
Dla 73f6d90: pełny audyt 45572212254, aplikacja 45572212144, terminologia 45572212154, algorytmy 45572212307 — queued przy kontroli. Nie oglądano PDF dla żadnej z tych dwóch wersji w tej iteracji. Nie przenosimy PASS na nowy blob.
Etap A otwarty. Następny audyt 193: kontrola PDF i CI właściwego SHA, weryfikacja pozostałych zależności oraz stabilizacja. Nie dodano proponowanego kryterium powierzchni z brzegiem ani orientowalności.
