# Audyt 221 — drukowany rozdział 24, zamknięcie etapu A

Data: 2026-11-25. Kontynuacja 220 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Commit źródłowy 6c9722cee627b211ac5b4a5aa35df48560ce1a73, blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830 potwierdzony trzykrotnie. Bez dalszych zmian źródła.

## Weryfikacja rysunków
W oczekiwaniu na artefakt pełnego tomu lokalnie skompilowano oba bloki TikZ ze stylami, rozmiarem czcionki i marginesami z books/pl/graph_and_knot_theory.tex. pdfLaTeX zakończony pomyślnie; render pdftoppm 200 dpi obejrzano. Oba rysunki czytelne.
Następnie pobrano artefakt 15010186951 dla dokładnego SHA. Rozpakowano i otwarto PDF w PyMuPDF: 354 strony, rozdział 24 na stronach fizycznych 200–206 (druk 190–196), rozdział 25 zaczyna się na 207. Pięć adnotacji odsyłaczy, plik ostrzeżeń 0 bajtów. Wyrenderowano siedem stron w skali 1.6 i obejrzano trzy arkusze kontaktowe oraz pełne strony 201 i 204.
- GKT-24-FIG-CAYLEY-01 PASS: wierzchołki prostej rozdzielone, etykiety liczb nie przecinają obwodów, cykl sześciowierzchołkowy czytelny, przerywane przedłużenia łączą się z węzłami.
- GKT-24-FIG-GROUP-01 PASS: podpisy amalgamacji i HNN nie przecinają etykiet grup, pętla i krawędź widoczne.
Nie stwierdzono istotnych kolizji lub obcięć w pozostałych miejscach rozdziału. Ostatnia strona w dużej części pusta, nie zmieniano kosmetycznie łamania stron.

## Regresje i struktura
Ponownie pobrano z repozytorium i wykonano trzy skrypty: CAYLEY-01 PASS (380 modeli, 4308 słów, 31892 przejścia); COSET-01 PASS (585 prób, 1755 odwróceń, 15795 kontroli reprezentantów, 5265 translacji, 4094 kontrole dziecko–rodzic); FREE-PRODUCT-01 PASS (218 słów, 219 wierzchołków, 218 krawędzi, 1090 kontroli incydencji, 654 translacje).
5 etykiet, 30 poprawnie zagnieżdżonych par środowisk, pięć wystąpień ref, cele sprawdzone w 219. Skrypty wykonane w izolacie JS; nie potwierdzono integracji z CI ani uruchomienia w procesie Node, nie formalizacja Lean. Kontrola matematyczna 219 pozostaje aktualna, od tego czasu zmieniono tylko dwa rysunki. Fundamentalne twierdzenie Bassa–Serre'a jest jawnie przyjęte z literatury.

## CI i decyzja
Wszystkie cztery przebiegi dla 6c9722ce SUCCESS: terminologia 45589293161, algorytmy 45589292932, pełny audyt 45589292978, aplikacja 45589292943.
Etap A zamknięty. Rozdział 24 pozostaje otwarty do niezależnego etapu B. Następny audyt 222: niezależna kontrola działania, nakryć nieskończonych, prezentacji HNN i modelu klas bocznych. Bez niezatwierdzonych rozszerzeń. Postęp 23/44.
