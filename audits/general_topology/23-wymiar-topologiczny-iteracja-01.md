# Topologia ogólna — rozdział 23, audyt 01

**Data:** 2026-11-22. **Branża źródła:** biblioteka-matematyczna-iteracja-6.
**Plik:** chapters/pl/general_topology/23-wymiar-topologiczny.tex.
**Wynik:** audyt korekcyjny (**0/2** czystych audytów po zmianie).
**Blob po korekcie:** 26d9348431988f5e221404b647cd7a343f457a26.

## Zakres i założenia

Definicja wymiaru pokryciowego jest świadomie ograniczona do
zwartych przestrzeni Hausdorffa; zapewnia to równoważność
warunku dla pokryć skończonych i dowolnych pokryć otwartych.
Nie używamy bez uzasadnienia twierdzeń o dowolnych
niezwartych przestrzeniach ani nie utożsamiamy wymiaru
pokryciowego z wymiarem Hausdorffa w metryce.

Definicje małego wymiaru ind i dużego Ind są rekurencyjne,
z wyraźną wartością -1 dla pustej przestrzeni
oraz ze sformułowaniem warunków dla punktów lub par
złożonych z domkniętego F i otwartego U.
Nie twierdzimy, że wszystkie trzy wymiary są zawsze równe:
udowodniono wyłącznie ich zgodność w wymiarze 0
dla zwartych przestrzeni Hausdorffa.

## Kontrola matematyczna

1. Rozdrobnienia traktowane są jako rodziny indeksowane,
   więc rząd zlicza także różne indeksy o tych samych zbiorach.
2. Niezmienniczość homeomorficzna wynika ze zgodności
   przeciwobrazów/obrazów pokryć i z zachowania liczby elementów
   zawierających punkt.
3. Zamknięte zmniejszenie skończonego pokrycia:
   zwarte Hausdorffa implikuje normalność; najpierw
   wybieramy otoczenia o domknięciu w odpowiednim U_i,
   a później skończone podpokrycie i łączymy domknięcia.
4. Monotoniczność wymiaru względem domkniętych podzbiorów
   korzysta z pokrycia X dodanego zbiorem X\F i
   ograniczenia końcowego rozdrobnienia do F.
5. Charakterystyka wymiaru zero: przy pokryciu
   {U, X\{x}} rozdrobnienie rzędu 1 zawiera dokładnie
   jeden element z x, który jest otwarto-domknięty.
   W przeciwną stronę skończona suma otwarto-domkniętych
   otoczeń, po odjęciu poprzedników, daje rozłączne
   rozdrobnienie.
6. Iloczyny wymiaru zero: z twierdzenia Tychonoffa
   mamy zwartość, z podstawowych cylindrów clopen
   bazę otwarto-domkniętą, co zapewnia dim=0.
7. Cantor: pierwsza odmienna cyfra na miejscu m
   oddziela dwie liczby trójkowe o co najmniej 3^{-m};
   kodowanie product-space jest homeomorfizmem.
8. Dla zwartej spójnej X o co najmniej 2 punktach
   pokrycie X\{a}, X\{b} uniemożliwia wymiar zero.
9. Wymiary ind i Ind: gdy n=0 granica otwartego V jest
   pusta, więc V clopen; kompaktowość F zapewnia
   skończone pokrycie F clopen otoczeniami w U.
10. Liczba Lebesgue'a: użyto pokrycia kulami
    B(x,epsilon_x), których podwojone promienie
    pozostają w wybranym U_i; minimum skończonej
    rodziny epsilon_x działa dla wszystkich zbiorów
    o średnicy <delta.
11. Dla zwartego K subset R: przedziały (kh-h,kh+h)
    mają krotność <=2, średnicę <=2h<delta,
    a K przecina tylko skończenie wiele;
    zatem dim K<=1. Spójność odcinka daje dim=1.
12. Konstrukcja mapy do nerwu używa ciągłych funkcji
    psi_i=d(x,X\U_i), z osobnym przypadkiem U_i=X;
    suma psi_i>0 dzięki pokryciu.
13. Triangulacja Freudenthala siatki R^n:
    simplex odpowiada porządkowi nierosnących współrzędnych;
    otwarte gwiazdy mają rząd <=n+1 i średnicę <=2h sqrt(n).
    Dla zwartego K jedynie skończenie wiele gwiazd je przecina.
14. Dim K<=n dla K zwartego w R^n wynika z liczby
    Lebesgue'a i rozdrobnienia otwartymi gwiazdami.
    Uwaga w tekście wyraźnie oddziela brakujący dowód
    dim([0,1]^n)>=n dla n>1.
15. Ciągły obraz zbioru Cantora o wymiarze 0 może być [0,1]
    o wymiarze 1: funkcja od cyfr ternarnych 0/2
    do binarnych 0/1 jest ciągła i surjektywna.

## Znaleziona usterka i korekta

Pierwotna definicja nerwu opisywała wszystkie indeksy
pokrycia jako wierzchołki, nawet gdy U_i jest puste.
Tymczasem przy U_i=empty singleton {i} nie jest sympleksem,
więc takie indeksy nie mogą być wierzchołkami.
Skorygowano definicję: wierzchołki odpowiadają tylko
indeksom niepustych elementów pokrycia.
Współrzędne kanonicznej mapy dla pustych U_i są równe 0;
dowód mapy nie wymaga innych zmian.
Commit: 0f59c10a8fddba249718ea3f61fc7744b7cae1eb.
Nowy blob: 26d9348431988f5e221404b647cd7a343f457a26.

## Testy, biblioteka i rysunek

Dodano wpis w catalog/books.json, import do książki,
samodzielny punkt wejścia books/pl/general_topology_ch23.tex,
test tools/tests/test_general_topology_ch23.py oraz kroki CI.
Testy modelowe obejmują skończone dyskretne pokrycia,
cylindry Cantora, współrzędne triangulacji i rząd
rozdrabniających przedziałów; nie są matematycznym
dowodem twierdzeń ogólnych.

Rysunek przedziałów wymaga kontroli po kompilacji.
Status kompilacji najnowszego bloba ma być potwierdzony
osobnym zakończonym przebiegiem GitHub Actions
oraz przeglądem rzeczywiście wyrenderowanego PDF.

**Status: OTWARTY (0/2)** — kolejne czyste audyty muszą
odnosić się do niezmienionego bloba 26d93484... .


## Dodane następnie: pełny wymiar sześcianu

Po pierwszym audycie użytkownikowy zatwierdzony zakres
teorii wymiaru rozszerzono o pełne dolne oszacowanie
\(\dim[0,1]^n\ge n\), a więc o równość
\(\dim[0,1]^n=n\) dla każdego \(n\ge1\).

- Z twierdzenia Brouwera (dowód istnieje w AT-19)
  wyprowadzono wprost własność Poincarégo--Mirandy,
  konstruując odwzorowanie \(T(x)=P_Q(x-f(x))\)
  i analizując każdy przypadek graniczny.
- Udowodniono lemat wyboru skończenie wielu
  wektorów w zadanych otwartych ortantach
  w położeniu liniowo ogólnym:
  każda podrodzina co najwyżej n wektorów
  jest liniowo niezależna.
- Gdyby \(\dim Q\le n-1\), rozdrobnienie
  skończonego pokrycia przez \(2^n\) otwartych
  obszarów znakowych dostarczyłoby
  (za pomocą funkcji barycentrycznych)
  ciągłego odwzorowania \(f:Q\to\mathbb R^n\)
  bez zera, którego składowe mają przeciwne
  znaki na przeciwległych ścianach.
  Jest to sprzeczne z własnością Poincarégo--Mirandy.
- Przez jawny radialny homeomorfizm
  \([-1,1]^n\simeq D^n\) uzasadniono
  przejście od twierdzenia Brouwera
  w wersji dla domkniętej kuli do sześcianu.
- Dodano testy modelu brzegowego Poincarégo--Mirandy
  i radialnego homeomorfizmu kostka--kula.

Późniejszy blob źródła: `c666640268a1a14b813b4e0a1e7744e342cf9fe8`.
Zmiany unieważniają licznik kontroli wcześniejszego bloba:
**aktualny stan pozostaje 0/2** do czasu audytów
na tym konkretnym, niezmienionym źródle.

Odnotowano, że wcześniejszy CI na pierwszym dodaniu
twierdzenia o sześcianie nie przeszedł testu regresyjnego
zawierającego stary warunek „brak dowodu dolnego oszacowania”.
Test uaktualniono wraz z dodaniem nowego dowodu.
