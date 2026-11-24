# Audyt 172 — drukowany rozdział 18, etap A

Data: 2026-11-24. Plan 118. Uwzględniono równoległy raport 171; jego zmian nie cofano.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit źródłowy d3d45f44b5598a6528fcfafc7ecfaec3f310969e, blob 38e1d199b3c79187dbc768d25e4782f708fc6add.
Commit regresji ed5052ea57758838e61365fa94bdb555292d8fbe.

## Zmiany
- Rozpisano wykluczenie obchodów długości 1 i 2 dla prostego spójnego grafu o n>=3 przez cykliczny następnik półkrawędzi; przypadek dwudzielny i algebra obu oszacowań rodzaju.
- Rozwinięto istniejącą poprawkę równoległą dotyczącą komórkowości konstrukcji wstęgowej: sektory, półwstęgi, kołnierz, doklejenie dysku i przypadek jednego promienia. Nie utożsamiano ściany z samym wnętrzem dysku.
- Dodano jawne układy rotacji K5 oraz K3,3, pełne obchody wszystkich półkrawędzi i obliczenie rodzaju. Dolne ograniczenie dla K3,3 wyprowadzono z nierówności dwudzielnej. Wcześniejsze twierdzenie o istnieniu zanurzeń nie pozostaje nieuzasadnione.
- Sprawdzono zakres sąsiednich rozdziałów 12,13,16; nie stwierdzono powielenia tego uzupełnienia.
- 11 unikalnych etykiet, 36 poprawnie zagnieżdżonych par środowisk; 3 odsyłacze, wszystkie cele istnieją. Ponowny odczyt potwierdził blob.

## Rzeczywiste regresje
GKT-18-ROT-01, test_gkt18_torus_rotations.js, blob 19ed1be956e08fbc97e5c9ef70d49bbbf320163b. Wykonano funkcję run w JS, a po zapisie pobrano plik i ponowiono wykonanie, zastępując jedynie końcowe console.log przez return.
- K5: PASS 20 półkrawędzi, dokładnie 5 wypisanych obchodów; wszystkie 7776 układów rotacji przy ustalonych pierwszych półkrawędziach, minimalny rodzaj 1, 462 rotacje rodzaju 1.
- K3,3: PASS 18 półkrawędzi, dokładnie 3 wypisane obchody; wszystkie 64 układy rotacji, minimalny rodzaj 1, 40 rotacji rodzaju 1.
- Weryfikacja minimalnej długości ścian i parzystości w przypadku dwudzielnym. Liczby rotacji nie są liczbami klas izomorfizmu zanurzeń.
- Ponowiono GKT18-BRIDGE-01 z pobranego pliku (blob b7ecafa70dfed28916c2443c35164c647e329b73), w JS zastępując import Node równoważną asercją równości, a końcowy log zwracaniem wyniku: PASS 1067 mostów.
To testy skończone, nie dowody topologiczne ani formalizacja Lean.

## Stabilizacja
Pełny CI dla commitu źródłowego: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45491222926 — in_progress, brak końcowego wyniku. Nie pobrano jeszcze nowego PDF.
Etap A otwarty. Wznowienie: szczegółowy audyt konstrukcji dualnej (w tym podwójnego dualu), homologii komórkowej i ocena uzupełnienia o rozkład drzewo–drzewo dualne oraz homologię nad Z, zgodnie z raportem 171. Następnie stabilizacja i pełne CI/PDF; nie przechodzić do B przed spełnieniem bramki.
