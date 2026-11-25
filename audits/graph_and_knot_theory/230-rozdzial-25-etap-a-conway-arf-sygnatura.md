# Audyt 230 — drukowany rozdział 25, etap A: Conway, Arf, sygnatura

Data: 2026-11-25. Kontynuacja 229.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex.
Blob wejściowy b634aa684ddf601ad570feadfaebfd4c50bf5195.

## Kontrola i poprawki
Odczytano obie sekcje w całości. Dla Conwaya jawnie oddzielono przyjmowane twierdzenie o istnieniu i normalizacji dla splotów od dowodu jednoznaczności oraz wykazano injektywność podstawienia z=u-u^-1, parzystość i wyraz stały. Dla formy Arfa podano niezależność od całkowitego podniesienia klasy modulo dwa i polaryzację macierzy V.
Zastąpiono przyjmowane wcześniej algebraiczne kryterium modulo osiem pełnym dowodem: w całkowitej bazie symplektycznej M=V+V^T ma modulo dwa bloki 2x2; pierwszy blok D o parzystej przekątnej i nieparzystych elementach poza nią ma wyznacznik nieparzysty. Eliminacja Schura nad Z/8Z zmienia przekątną pozostałego bloku o wielokrotności ośmiu i inne elementy o wielokrotności czterech. Indukcja daje det M = (-1)^g(1-4 Arf) mod 8; normalizacja symetryczna daje Delta_sym(-1)=1-4 Arf mod 8. Następnie z kongruencji Conwaya wynika Arf=a_2 mod 2. Twierdzenie topologiczne o metabolizerze węzła typu slice pozostaje wynikiem zewnętrznym.
Dla sygnatury rozpisano rzeczywistą zmianę współrzędnych w obu elementarnych powiększeniach, dającą sumę z płaszczyzną hiperboliczną, oraz znak przy odbiciu lustrzanym. Twierdzenie Murasugiego i S-równoważność pozostają przyjmowane z literatury.
Commit 88145da89421166678900e1542b64133bf5485dd, blob a0441e5c2b1f96954ccb61d40cfecf834f8f21f1. Kontrola struktury: 168 poprawnie zagnieżdżonych par środowisk, 21 unikatowych etykiet, 8 odsyłaczy.

## Rzeczywiście wykonane regresje Python
GKT-25-ARF-MOD8-01: 16384 dokładne przypadki 4x4 (przekątne 0,2; pary 1,3; pozostałe pozycje 0,2,4,6) oraz 128 deterministycznych przypadków 6x6 (seed 230). PASS, 16512 macierzy; wyznacznik liczony wzorem Leibniza, niezależnie od dowodu eliminacyjnego. Test zapisano w tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py, commit dea15eee9f417477fef4e6fb222b693f12ac67d7, blob b1f6cb1de2db519b535175357b41471eb9395dd3. Potwierdzono wywołanie w __main__.
Ponownie rzeczywiście uruchomiono samodzielne kopie modeli z 227–229: LINK 13392, FOX 18495, PREFIX 30948 redukcji, 1365 tożsamości oraz 1 trójlistnik. Wszystkie PASS. Testy skończone, nie formalizacja Lean. Nie wykonano całego pliku testowego lokalnie.

## CI i decyzja
Run 45594206845: full-book-pdf success, structural-audit queued przy ostatnim odczycie. Nowy run 45595479850 dla dea15eee queued. Brak nowych oględzin PDF i potwierdzenia nowych regresji w CI. Etap A otwarty. Postęp 24/44.
Następny audyt 231: Jones, nawias Kauffmana, kompletność dowodu ruchów Reidemeistera i relacji skein; potem warkocze i końcowe sekcje. Sprawdzić CI i rysunki po zakończeniu pierwszego przejścia, nie zamykać przed stabilizacją.
