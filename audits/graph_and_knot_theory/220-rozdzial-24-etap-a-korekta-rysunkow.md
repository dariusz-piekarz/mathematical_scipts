# Audyt 220 — drukowany rozdział 24, kontrola PDF i korekta rysunków

Data: 2026-11-25. Kontynuacja 219, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Wersja wejściowa 7dd1dbfaf127259219f733a2c53bb6626599cbf2, blob a6830b28deff06af43d16bb8bec3de449fc6b3a7.

## CI i oględziny
Dla wejściowego SHA wszystkie cztery przebiegi SUCCESS: terminologia 45588642803, algorytmy 45588642566, aplikacja 45588642607, pełny audyt 45588642579.
Pobrano artefakt 15009852868 dokładnie dla tego SHA. Rozpakowano PDF w środowisku wykonawczym. PyMuPDF: 354 strony, rozdział 24 na stronach fizycznych 200–206 (druk 190–196), następny rozdział na 207. Pięć adnotacji odsyłaczy; plik ostrzeżeń ma 0 bajtów. Wyrenderowano wszystkie siedem stron w skali 1.6 i obejrzano trzy arkusze kontaktowe oraz osobno pełne strony 201 i 204.
Stwierdzono dwie istotne usterki graficzne:
- GKT-24-FIG-CAYLEY-01 (strona fizyczna 201): wierzchołki prostej stykają się lub zachodzą na siebie, etykiety są przy samych obwodach wierzchołków zarówno prostej, jak i cyklu.
- GKT-24-FIG-GROUP-01 (strona fizyczna 204): podpisy amalgamacja i rozszerzenie HNN nakładają się na etykiety grup wierzchołkowych.
Tekst i wzory mieszczą się w polu składu; ostatnia strona jest w znacznej części pusta, co nie jest błędem merytorycznym.

## Korekta
Commit 6c9722cee627b211ac5b4a5aa35df48560ce1a73, blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830, potwierdzony po zapisie.
W pierwszym rysunku zmniejszono węzły do 4 mm, usunięto wewnętrzny odstęp, zwiększono krok prostej z 0.58 do 0.82, odsunięto etykiety, poprawiono przerywane przedłużenia do kotwic węzłów, zwiększono odległość między rysunkami i odsunięto podpis cyklu. W drugim rysunku obniżono podpisy z -0.80 do -1.35, podniesiono opis pętli. Nie zmieniono treści matematycznej ani nie dodano ilustracji.
5 etykiet, 30 poprawnie zagnieżdżonych par środowisk, 5 wystąpień odsyłaczy bez zmian. Kryterium trwałej kontroli wizualnej: na nowym PDF węzły prostej są rozdzielone, oznaczenia liczb nie przecinają węzłów, podpisy obu modeli grafu grup nie przecinają etykiet G_v. Metoda: render obu stron i oględziny w pełnej rozdzielczości. Kryteria zapisane w tym raporcie, nie wykonano jeszcze kontroli dla zmienionego SHA.

## Regresje
Ponownie wykonano z repozytorium: CAYLEY-01 PASS (380 modeli, 4308 słów, 31892 przejścia), COSET-01 PASS (1755 odwróceń, 15795 zmian reprezentantów, 5265 translacji), FREE-PRODUCT-01 PASS (218 słów, 219 wierzchołków, 218 krawędzi, 1090 kontroli incydencji). Izolat JS, nie Lean; nie potwierdzono integracji z CI ani uruchomienia w procesie Node.

## Bramka
Dla 6c9722ce wszystkie przebiegi in_progress przy ostatnim odczycie: terminologia 45589293161, aplikacja 45589292943, pełny audyt 45589292978, algorytmy 45589292932. Nowego PDF jeszcze nie oglądano. Nie przeniesiono PASS poprzedniego SHA.
Etap A pozostaje otwarty ze względu na ponowną kompilację i kontrolę dwóch poprawionych rysunków. Następny audyt 221: końcowa kontrola nowego SHA, PDF i regresji, zamknięcie A przy spełnieniu bramki. Postęp 23/44.
