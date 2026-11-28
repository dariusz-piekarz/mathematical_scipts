# Audyt 231 — drukowany rozdział 25, etap A: Jones i nawias Kauffmana

Data: 2026-11-25. Kontynuacja 230.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex.
Blob wejściowy a0441e5c2b1f96954ccb61d40cfecf834f8f21f1.

## Kontrola i poprawki
Przeczytano sekcję Jonesa i wcześniejszą definicję znaku skrzyżowania. Zachowano konwencje diagramu i wielomianu trójlistnika. Uzasadniono dobrze określoną sumę stanów oraz zgodność dodatniego znaku z wygładzeniem A zachowującym orientację; rozpisano oba mnożniki RI i obie kolejności RII. W RIII dopisano redukcję do lokalnego warkocza z trzema pasmami o ścisłym porządku wysokości. Porównania par (1,2),(1,3),(2,3) dają sześć dopuszczalnych trójek znaków; dwie cykliczne są wykluczone. Mieszane relacje wynikają z podstawowej relacji warkoczowej przez mnożenie i odwracanie. Wyprowadzono relację skein z dwoma lokalnymi wygładzeniami i czynnikiem normalizacji; obliczono resztę wykładników modulo cztery dla wszystkich stanów, zależną wyłącznie od parzystości liczby składowych.
Commit ac2999266413645513c4bafbfa07cdc325fcdc05, blob 9923272820507d4e46fdc9570aa62c0534499f94. Kontrola struktury: 169 par środowisk, 21 unikatowych etykiet, 8 odsyłaczy.

## Regresja
GKT-25-JONES-01: samodzielny model Python wykonany w środowisku wykonawczym. PASS: sześć porządków wysokości w algebrze Temperleya–Lieba, 25 wartości skrętu poza dyskiem od -12 do 12 (dla każdej sprawdzono oba współczynniki skein). Kod zintegrowano z istniejącymi funkcjami tl_mul, poly_mul i poly_add w tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py. Commit 6b65a203d53df7045965bb436801fc52402dd8db, blob 79ac5d477268fde20d1009d43764a74c93b8f8f6. Potwierdzono wywołanie w __main__. Lokalnie nie uruchomiono całego pliku repozytorium. Test skończony, nie formalizacja Lean.

## CI i dalszy zakres
Poprzedni run 45595479850: full-book-pdf success, structural-audit queued przy odczycie. Nowy run 45596077674 dla 6b65a203 queued. Nie wykonano nowych oględzin PDF. Nie deklaruje się wyniku całego CI.
Następny audyt 232: warkocze, twierdzenia Alexandra i Markowa, suma spójna i rodzaj, węzły torusowe oraz ostatnia część rozdziału. Następnie stabilizacja etapu A i kontrola rysunków. Postęp 24/44.
