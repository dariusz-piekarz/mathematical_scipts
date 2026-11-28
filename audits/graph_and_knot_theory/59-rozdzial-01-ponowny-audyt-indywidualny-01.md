# Rozdział 01 — ponowny audyt indywidualny 01

2026-11-24. Zgodnie z nową decyzją autora, po zachowaniu dotychczasowych poprawek przechodzimy ponownie przez rozdziały pojedynczo aż do ich stabilizacji; dopiero potem wracamy do audytów przekrojowych. Nie rozpoczynać 02 przed zamknięciem 01. Audyt przekrojowy 37 pozostaje odrębnym otwartym zadaniem.

Źródło: `chapters/pl/graph_and_knot_theory/01-podstawy-teorii-grafow.tex`. Commit poprawek `4b17aa515f61ccfcaac96c4f7ff8af0f1ec2bfa1`.

## Pierwsze przejście

- Usunięto sprzeczność dotyczącą grafu zerowego; podgraf indukowany przez zbiór pusty istnieje. Realizacja CW ma wymiar co najwyżej jeden (przy grafie bez krawędzi nie musi mieć wymiaru jeden).
- Multigraf ma jawne odwzorowanie końców. Spacer w multigrafie wymaga podania krawędzi, a cykl jest zamkniętym szlakiem z różnymi wierzchołkami poza końcami; unikamy uznania dwukrotnego przejścia tej samej krawędzi za cykl długości dwa.
- W dowodzie metryki osobno rozpatrzono u=w; lemat usuwania powtórzeń zakłada różne końce.
- Zastąpiono argument o drzewie najkrótszych dróg w dowodzie dwudzielności argumentem o nieparzystym spacerze zamkniętym. Minimalny taki spacer nie ma powtarzających się wierzchołków poza końcami, bo podział dałby krótszy nieparzysty spacer zamknięty; brak pętli wymusza długość co najmniej trzy. W rozdziale 01 nie jest zatem konieczne użycie teorii drzew z rozdziału 02.
- Przeniesiono przykład graniastosłupa trójkątnego i K_{3,3} po definicjach stopni i cykli oraz kryterium dwudzielności. Dodano uzasadnienie niezmienniczości stopni i cykli.
- Dodano przykład podgrafu K_4 na trzech wierzchołkach, w którym pominięta krawędź odróżnia podgraf od indukowanego.
- Jawnie rozstrzygnięto ujemne wyrazy w kryterium Havla–Hakimiego.

## Propozycje do rozważenia (nie dodano jeszcze)

1. Rysunek porównawczy podgrafu i podgrafu indukowanego oraz rysunek dwóch nieizomorficznych grafów 3-regularnych.
2. Wyodrębnienie lematu o nieparzystym spacerze zamkniętym; wersja z cyklem zawartym w spacerze wymaga minimalizacji w podgrafie krawędzi tego spaceru.
3. Kryterium Erdősa–Gallaia z pełnym dowodem jako opcjonalne uzupełnienie kryterium Havla–Hakimiego; sprawdzić najpierw brak powtórzeń w całym tomie.
4. Przykład wykorzystujący macierz sąsiedztwa do liczenia trójkątów: tr(A^3)/6, z dowodem.
5. Sprawdzić jawne definicje P_n i C_n, konwencje oznaczeń, wprowadzenie drzew i kompletną konstrukcję grafu z przykładu Havla–Hakimiego. Sprawdzić wszystkie istniejące rysunki i łamanie stron.

## Bramki stabilizacji

Status OTWARTY. Zapis źródła potwierdzony przez GitHub. Przy pierwszym zapytaniu o workflow dla SHA poprawek nie zwrócono jeszcze przebiegów. Nie potwierdzono CI ani składu. Niezależnie przejrzeć całe źródło po zmianach, zweryfikować testy, pełny PDF i zmienione strony. Nie przechodzić do rozdziału 02 do spełnienia bramek.
