# Topologia ogólna — globalny audyt 10: rysunki i skład PDF

**Data:** 2026-11-22.
**Źródło PDF do kontroli:** artefakt `general-topology-ch01-ch26`
nr **14771125631** z [udanego CI 45064706272](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064706272).
**Zakres:** ręczny przegląd ilustracji i kontrola
danych o stronach, podpisach oraz logów LaTeX.
To audyt **wydawniczy**, a nie dowód poprawności
wszystkich twierdzeń matematycznych.

## Zakres rzeczywiście sprawdzony

Pobrano i wypakowano ZIP z pełną książką
(190 stron, wersja 1.26)
oraz osobnymi PDF rozdziałów 02–26.
Archiwum **nie zawiera samodzielnego PDF rozdziału 01**,
ale dwa jego rysunki znaleziono
na stronach 9 i 15 pełnej książki
i obejrzano w powiększeniu.

Rzeczywisty spis rysunków:
- 01: 2 rysunki (książka: s. 9, 15);
- 02: 1; 04: 2; 05: 5;
- 06: 2; 07: 2; 08: 2; 09: 2;
- 10: 1; 11: 1; 12: 1;
- 21: 1; 22: 1; 23: 1; 24: 1;
- 25: 1; 26: 1.

**Razem: 27 rysunków w 17 rozdziałach.**
Pozostałe 9 rozdziałów nie mają
środowisk `figure` w tym wydaniu.

Dla wszystkich rysunków 02–26
wyrenderowano strony z podpisami
i obejrzano cztery plansze zbiorcze;
dla dwóch ilustracji rozdziału 01
sprawdzono osobne powiększenia.
Widoczne rysunki, osie, oznaczenia
i podpisy nie mają oczywistych
kolizji, przecięć z marginesem
ani uciętych elementów.
W szczególności diagramy 12
(relacja bliskości metrycznej),
23 (pokrycie prostej),
24 (iloraz prostej) i
25 (namiot) zachowują czytelny
opis wraz z podpisem.
Nie poświadczamy jednak
automatycznego sprawdzenia
każdej odległości między
dwoma glifami w kodzie TikZ:
to ograniczenie przeglądu wizualnego.

Sprawdzono strukturę wszystkich
25 samodzielnych PDF-ów
rozdziałów 02–26 i pełnego wydania.
Pełna książka ma 190 stron,
w jej analizie nie stwierdzono
pustej strony zawierającej
wyłącznie numer strony.
Z poziomu tekstu PDF
i logów nie stwierdzono
błędów `Overfull`, `Underfull`,
`Missing character`, `LaTeX Warning`
ani `Undefined control sequence`.

## Błąd inwentaryzacji — wykryty i skorygowany

Pierwszy odczyt rysunków
wykonany wyłącznie na
samodzielnych PDF-ach wskazywał
**25 rysunków w 16 rozdziałach**.
To było niepełne, ponieważ
zabrakło pliku samodzielnego
rozdziału 01. Rysunki 1.1 i 1.2
w pełnym PDF istnieją i są poprawnie
podpisane; po doliczeniu ich
prawidłowy stan to **27 w 17**.

Dodano test
`tools/tests/test_general_topology_figure_sources.py`,
który wymaga dla każdego rysunku
jednego podpisu, jednej unikatowej
etykiety po podpisie i obecności
środowiska TikZ. Dodatkowo sprawdza
stałą liczbę 27 rysunków w 17 rozdziałach.
Test włączono do workflow
`.github/workflows/general-topology-chapter.yml`.
Po pierwszym błędzie CI spowodowanym
niepełną inwentaryzacją poprawiono
oczekiwane liczności.

## Wykryte rzeczywiste usterki składu

Dodatkowo wyrenderowano ostatnie strony
wybranych rozdziałów, w szczególności
03, 04, 06, 07, 17 i 21.
**W rozdziałach 03 i 04 wystąpiły
nadmiernie puste strony końcowe:**
- rozdział 03: ostatnia strona
  zawierała jedynie podsumowanie
  i zapowiedź kolejnego rozdziału;
- rozdział 04: ostatnia strona
  zawierała jedynie krótką uwagę
  o kierunku sprawdzania ciągłości.

Obie rzeczywiste usterki
zostały zgłoszone do poprawy,
a nie przemilczane z powodu
braku ostrzeżeń kompilatora.

**Korekta rozdziału 03:** usunięto
powielenie przykładu o identyczności
z dyskretnej przestrzeni dwupunktowej
do antydyskretnej: zapisano odsyłacz
do wcześniejszego szczegółowego przykładu.
Zredagowano podsumowanie tak,
aby zachowało wszystkie wątki:
kryteria ciągłości, sklejanie,
homeomorfizm, zanurzenie
i zapowiedź kolejnego rozdziału.
Nowy blob:
`a5606bc0c213dbd1fb5224e7440f66a7cf66dbb0`.

**Korekta rozdziału 04:** uwagę
o kierunku sprawdzania ciągłości
scalono z podsumowaniem
własności uniwersalnych,
bez utraty rozróżnienia
topologii początkowej i końcowej.
Nowy blob:
`adbd56a91e5b5f3857ce16ec5c3b1241dd0d102e`.

## Stan i dalsza walidacja

Powyższe błędy zidentyfikowano
w PDF z poprzednich blobów 03 i 04.
Nowe wersje źródeł
wymagają jeszcze:
1. zielonego CI z aktualnym
   testem inwentaryzacji;
2. pobrania i ręcznej inspekcji
   świeżych PDF-ów 03, 04,
   a także pełnej książki;
3. dwukrotnego czystego
   audytu redakcyjno-matematycznego
   obu nowych blobów i
   dodatkowej kontroli potwierdzającej.

**Status:** audyt rysunków 27/27 — wykonany;
poprawki składu 03/04 — w rewalidacji.
Globalny audyt wszystkich dowodów
01–26 nadal pozostaje otwarty.
