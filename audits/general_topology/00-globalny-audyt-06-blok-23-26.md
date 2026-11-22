# Topologia ogólna — globalny audyt 06, blok 23–26

**Data:** 2026-11-22.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres:** szczegółowa kontrola zależności rozdziałów 23–26
i niezależne sprawdzenie wybranych trudniejszych dowodów
matematycznych. Raport nie twierdzi, że każdy z 64 dowodów
przeszedł dodatkowy pełny audyt po wcześniejszych
audytach indywidualnych.

## Stan źródła

| Rozdział | Blob Git | Środowiska proof | Etykiety | Odsyłacze |
| --- | --- | ---: | ---: | ---: |
| 23 | `9dc1ed4784d929b405d00a3216865418f240a37c` | 20 | 40 | 23 |
| 24 | `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6` | 21 | 41 | 14 |
| 25 | `7b772123870296af95d3ce951ccddb65685af7aa` | 14 | 35 | 15 |
| 26 | `161d04d779ae86554f81c11bb24daa842c8dd363` | 9 | 22 | 19 |

Łącznie: 4 233 wiersze LaTeX, 64 dowody,
138 etykiet i 71 odsyłaczy.
Dotychczasowe audyty indywidualne zakończyły się
2/2 + 1, a końcowe CI dla wersji 1.26 przeszło
([45063338871](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45063338871)).

## Logiczna kolejność wyników

Sprawdzono występowanie każdego odsyłacza
w rozdziałach 23–26. Żaden z nich nie powołuje
się na rozdział późniejszy:

- Rozdział 23 korzysta z twierdzenia Tychonoffa
  i normalności zwartych przestrzeni Hausdorffa
  z rozdziału 07.
- Rozdział 25 wykorzystuje kodowanie zbioru
  Cantora z rozdziału 23, a także podstawowe
  twierdzenia o spójności z 08
  i twierdzenie Tietzego z 05.
- Rozdział 26 korzysta z lokalnej spójności
  z rozdziału 08, twierdzenia Urysohna
  z rozdziału 10 oraz konkretnych
  continuów i wyników Peana z 25.
- Rozdział 24 w głównych tezach
  o grupach topologicznych działa niezależnie
  od rozdziałów 25–26.
- W szczególności nie ma kołowej
  zależności „Hahn–Mazurkiewicz ↔ Peano”:
  rozdział 25 pokazuje surjekcje na
  konkretne grafy i sześciany,
  podczas gdy rozdział 26 daje
  ogólną charakteryzację.

## Audyt 23 — wymiar topologiczny

Niezależnie przeanalizowano trudny dowód
\(\dim [0,1]^n=n\).
Górne oszacowanie opiera się na drobnej
triangulacji siatki i otwartych gwiazdach
o rzędzie ≤n+1. Dla zwartego K
lokalna skończoność daje skończone
rozdrobnienie pokrycia.
W dolnym oszacowaniu:
1. Z założenia dim Q≤n−1 wybieramy
   rozdrobnienie rzędu ≤n.
2. Otwarte ortanty pozwalają wybrać
   rodzinę wektorów v_j, z której
   dowolna podrodzina o liczności ≤n
   jest liniowo niezależna.
   Wybór poza skończoną sumą
   właściwych podprzestrzeni liniowych
   jest uzasadniony.
3. Rozkład jedności podległy
   rozdrobnieniu daje niezerowe
   f(x)=Σφ_j(x)v_j, ponieważ
   w każdym punkcie aktywnych
   jest ≤n liniowo niezależnych
   wektorów z nieujemnymi
   współczynnikami sumującymi się do 1.
4. Warunki na przeciwległych
   ścianach sześcianu mają
   przeciwne znaki, więc lemat
   Poincarégo–Mirandy wymusza
   punkt zerowy: sprzeczność.

Sprawdzono również, że lemat
Poincarégo–Mirandy powołuje się
na twierdzenie Brouwera
o punkcie stałym.
To ostatnie rzeczywiście występuje
jako udowodniony wniosek
z twierdzenia Lefschetza w
`chapters/pl/algebraic_topology/19-stopien-indeks-punktu-stalego-i-twierdzenie-lefschetza.tex`.
Nie ma tu potrzeby powielania
tego dowodu; natomiast pełny
audyt podstaw twierdzenia Lefschetza
jest osobnym zadaniem dla topologii
algebraicznej.

## Audyt 24 — grupy i ilorazy

Prześledzono rozdzielenie:
- H domknięta ⇒ G/H Hausdorffa;
- H normalna ⇒ istnieje
  zgodna algebraiczna grupa ilorazowa;
- w pierwszym twierdzeniu o
  izomorfizmie topologicznym
  dodatkowa otwartość homomorfizmu
  jest konieczna i jawnie założona.

W dowodzie Birkhoffa–Kakutaniego
metryka jest skonstruowana przez
infimum długości łańcuchów.
Dodatnia określoność wymaga
osobnego dyadycznego lematu
o małych sumach wag, który
faktycznie znajduje się w źródle.
Nie wyprowadzono metryki
z samej pseudometryki bez
uzasadnienia jej rozdzielania.
Wciąż ważne są wcześniejsze
indywidualne audyty rozdziału 24.

## Audyt 25–26 — związki Peana i Hahna–Mazurkiewicza

Rozdział 25:
- istnienie minimalnego
  podcontinuum między punktami
  stosuje Zorna dopiero po
  udowodnieniu zachowania
  spójności przecięcia łańcucha;
- nierozkładalność Knastera
  jest otrzymana z pełnych
  gałęzi iteracji namiotu
  i kontroli rzutowań C na poziomach;
- solenoid dyadyczny jest
  ciągłą granicą odwrotną
  okręgów i ma lokalny
  model łuk × Cantor;
- istnienie surjekcji
  [0,1]→[0,1]^n
  wynika z przeplatania
  cyfr kodowania Cantora
  i przedłużania Tietzego.

Rozdział 26:
- lokalna spójność i zwartość
  dają małe spójne otoczenia,
  a następnie małe drogi
  przez konstruowanie łańcuchów;
- krótkie pętle pozwalają
  zagęszczać obraz krzywej
  przy sumowalnych kosztach;
- jednostajna granica
  jest surjektywna dzięki
  drobnym sieciom i domkniętości obrazu;
- konieczność lokalnej
  spójności uzasadniono
  zwartością włókien odwzorowania
  [0,1]→X, a metryzowalności
  — bazą złożoną z W_V
  i twierdzeniem Urysohna.

Nie wykryto nowych luk w
wybranych sprawdzonych przejściach.
Dwa rozdziały mają osobne
kompletne audyty matematyczne
oraz oględziny samodzielnych PDF.

## Ciąg dalszy i granice oceny

W tym przebiegu **nie wprowadzano zmian**
w stabilnych plikach 23–26.
Dopisano niezależny regresyjny
`tools/tests/test_general_topology_cross_dependencies.py`:
sprawdza pełną globalną
rozwiązywalność etykiet i brak
odwołań z nowych rozdziałów
do wyników jeszcze niewprowadzonych.
Weryfikuje także występowanie
twierdzenia Brouwera w
topologii algebraicznej.
Test włączono do CI.

**Status:** rozszerzenie przekrojowego
audytu na 23–26 — wykonane.
**Nie oznacza zakończenia
pełnego audytu matematycznego
wszystkich rozdziałów 01–26.**
Kolejną kontrolę skierować na
minimalizację filtrów Cauchy'ego
i zupełność konstrukcji w
rozdziale 13, gdzie raport
globalny 04 wyraźnie pozostawił
część argumentacji technicznej
do ponownej niezależnej weryfikacji.
