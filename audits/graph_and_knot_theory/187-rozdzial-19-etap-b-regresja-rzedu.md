# Audyt 187 — drukowany rozdział 19, stabilizacja etapu B

Data: 2026-11-25. Kontynuacja 186, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Commit źródłowy bdd1587f6b5465ce720ccd8f2bb2ed89a96f7e96, blob 1902a533a76e3e5d1110908ba74789303e064dde potwierdzony na gałęzi roboczej. Źródło bez zmian.

## Ponowna kontrola semantyczna
- GKT-19-B-FOREST-01: usunięcie pętli i zastąpienie kopii jedną krawędzią zachowuje podział na składowe; las prosty po wyborze reprezentantów jest lasem multigrafu, także dla n=0. Wybór kopii nie zmienia incydencji. Dla cykli długości 1 i 2 dodatkowa krawędź zamyka cykl, więc argument o zerowym wymiarze jest poprawny. Kryterium spełnione.
- GKT-19-B-REC-01: kontrakcja krawędzi obecnej w podgrafie nie łączy różnych składowych; most łączy różne składowe każdego podgrafu, który go nie zawiera, więc k-c-1>=0. Pętle zwiększają jedynie nullity. Kryterium spełnione.
- GKT-19-B-CHROM-01: różnica dwóch wielomianów zgodnych na dodatnich liczbach całkowitych jest zerowa; znak specjalizacji redukuje się modulo 2 do |A|. Dla grafu zerowego oba wielomiany mają wartość 1. Kryterium spełnione.
- GKT-19-B-CELL-01: spójne regularne otoczenie w S^2 ma dysk po zewnętrznej stronie każdego okręgu brzegowego; dołączenie półotwartego kołnierza daje otwartą ścianę dyskową. W przypadku jednego wierzchołka otoczenie jest dyskiem i dopełnienie także. Zatem założenia dualności komórkowej i komplementarnych drzew są spełnione. Kryterium spełnione.
- Sprawdzono konwencję D=-d2, całkowitość q i utożsamienie q kolorów z Z/qZ. Działa także dla złożonych q, bez dzielenia. Brak nowych zidentyfikowanych istotnych usterek. 12 etykiet, 32 poprawnie zagnieżdżone pary środowisk.

## Wykonane regresje
REC-01 PASS: 3528 grafów, 15855 rekurencji, 14112 porównań kolorowań.
DUAL-01 PASS: 453 sferyczne układy, 3533 par podzbiorów, 1812 porównań.
KIRCH-01 PASS: 3532 dokładne minory.
LIFT-01 PASS: 8791 kolumn, 216466 rekonstrukcji, 178826 dla złożonych q.
Nowy GKT-19-RANK-01: audits/graph_and_knot_theory/test_gkt19_rank.js, commit d1312f678162952a7efc6a6c6ab31f65c5824321. Niezależna eliminacja bitowa nad F2, składowe liczone przez przeszukiwanie sąsiedztwa, bezpośrednie liczenie elementów jądra przez XOR, test cyklu przez alternatywną drogę po usunięciu krawędzi oraz jawny test pętli i kopii równoległych. PASS: 3528 grafów, 89217 podzbiorów, 21778 lasów, 270062 elementów jąder łącznie (z krotnością prób), 3002 grafy z pętlami i 2816 z powtórzonymi parami końców. Test wykonano dwukrotnie, także po odczycie zapisanego pliku.
Wszystkie testy wykonane w izolacie JS, nie w procesie Node. Próby częściowo pokrywają się. Nie jest to formalizacja Lean. Nowego skryptu nie podłączono do workflow CI.

## Bramka
Dla właściwego źródłowego SHA: Mathematical library application checks 45570370627 in_progress; Polish mathematical terminology 45570370783 success; Graph and knot theory - algorithms audit 45570370580 success; Graph and knot theory - full book global audit 45570370695 success.
Stan zadań pełnego audytu: [{"name":"structural-audit","status":"completed","conclusion":"success","steps":[]},{"name":"full-book-pdf","status":"completed","conclusion":"success","steps":[]}].
Artefakty dostępne przy końcowej kontroli: graph-and-knot-global-structure 15002006455; graph-and-knot-complete-book-audit 15001254231.
Nie przeprowadzono oględzin PDF najnowszej wersji. Nie przenosimy wcześniejszego PASS PDF. Etap B pozostaje otwarty do potwierdzenia CI i PDF. Następny audyt 188: zamknięcie B po pozytywnej kontroli, bez przechodzenia wcześniej do rozdziału 20.
