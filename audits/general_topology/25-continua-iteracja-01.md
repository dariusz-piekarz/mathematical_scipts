# Topologia ogólna — rozdział 25, audyt 01 (korekcyjny)

**Data:** 2026-11-22.
**Rozdział:** `chapters/pl/general_topology/25-continua-i-ich-struktura.tex`.
**Blob źródła po korektach:** `7b772123870296af95d3ce951ccddb65685af7aa`.
**Status:** 0/2; konieczne kolejne czyste audyty i dodatkowa
kontrola po rzeczywistym CI/PDF. Rozdziały 01–24 pozostają stabilne.

## Zakres, oryginalność i zależności

- Rozdział 08 topologii ogólnej ma już definicje,
  charakterystyki i podstawy spójności, spójności drogowej,
  lokalnej oraz krzywej sinusowej topologa.
  W 25 dołączono tylko treści specyficzne dla continuów.
- Rozdział 23 obejmuje kodowanie zbioru Cantora.
  Rozdział 05 zawiera pełny dowód twierdzenia Tietzego.
  Nie kopiujemy tych dowodów, lecz wykorzystujemy je
  w dowodzie istnienia surjekcji Peana \([0,1]\to[0,1]^n\).
- Rozdział 24 bada grupy topologiczne.
  Solenoid dyadyczny wykorzystuje tę strukturę
  tylko jako własność dodatkową, bez powtarzania
  teorii grup i bez wprowadzania miary Haara.
- Ogólne twierdzenie Hahna–Mazurkiewicza
  jest precyzyjnie *zaznaczone jako jeszcze
  nieudowodnione w tym rozdziale*.
  W przeciwieństwie do niego surjekcje na
  skończone spójne grafy i sześciany
  mają pełne samodzielne dowody.

## Kontrola matematyczna

1. Continuum definiujemy jako niepustą zwartą
   spójną przestrzeń Hausdorffa; podcontinua
   są zwartymi, a więc domkniętymi podzbiorami.
   Dopuszcza się continuum jednoelementowe
   i wyraźnie oznacza przypadki nietrywialne.
2. Ciągły obraz continuum w przestrzeni Hausdorffa
   jest continuum; dowód nie myli obrazu
   z przeciwobrazem spójnego zbioru.
3. Przecięcie zstępujących niepustych continuów
   jest niepuste przez zwartość i spójne:
   rozdzielenie granicy dałoby
   rozdzielenie pewnego późniejszego K_n.
4. Wersja dla łańcucha dowolnej długości
   jest oparta na skończonym podpokryciu
   rodziny \((X\setminus C)\cup\{U,V\}\).
   To zapewnia przecięcie pewnej
   skończonej podrodziny łańcucha
   zawarte w U∪V, a więc sprzeczność
   ze spójnością jednego z jego elementów.
5. Zorn zastosowany do niepustej rodziny
   podcontinuów zawierających punkty a,b,
   uporządkowanej odwrotną inkluzją,
   daje minimalne continuum między punktami.
   Łańcuch pusty ma górne ograniczenie X.
6. Jeśli continuum rozkłada się jako
   suma dwóch właściwych podcontinuów A,B,
   to A ma niepuste wnętrze, bo
   \(X\setminus B\subseteq A\)
   jest niepuste i otwarte.
   Stąd warunek pustego wnętrza
   wszystkich właściwych podcontinuów
   wystarcza do nierozkładalności.
7. Granica odwrotna ciągu zwartych Hausdorffa
   jest domkniętym podzbiorem zwartego produktu;
   przy surjektywnych odwzorowaniach
   wiążących wszystkie projekcje są surjektywne.
   Spójność granicy wynika z faktu,
   że dwie rozłączne zwarte składowe
   rozdzielenia miałyby rozłączne obrazy
   przy jakimś skończonym rzutowaniu,
   co przeczyłoby spójności X_n.
   Metryzowalność wynika z przeliczalnej
   sumy ograniczonych metryk.
8. Odwzorowanie namiotowe T ma 2^r
   gałęzi bijektywnych na [0,1].
   Jeśli właściwe podcontinuum C granicy
   odwrotnej miałoby wnętrze,
   zawierałoby cylinder p_k^-1(U).
   Dla wysokich poziomów m
   przedział p_m(C) zawiera
   \([1/4,3/4]\), a T² mapuje
   ten przedział na całe [0,1].
   Wszystkie rzuty p_j(C) byłyby więc
   pełne, co przy domkniętości C
   wymuszałoby C=X: sprzeczność.
   Ten argument dowodzi dokładnie
   nierozkładalności continuum Knastera.
9. Dla solenoidu dyadycznego
   lokalne rozwinięcie kolejnych
   pierwiastków kwadratowych z z_0
   daje model \(J\times\{0,1\}^{\mathbb N}\).
   Każdy spójny podzbiór produktu
   ma stałą współrzędną Cantora,
   która nie jest izolowana,
   więc model nie ma niepustych
   spójnych otwartych otoczeń.
   Zatem solenoid nie jest lokalnie spójny.
10. Dla skończonego spójnego grafu
    konstrukcja drogi obejmującej
    kolejno każdą krawędź (wracając
    do wspólnego wierzchołka)
    daje ciągłą surjekcję [0,1]→P.
    Ścisła lokalna spójność realizacji
    wynika z małych gwiazd wierzchołków.
11. Surjekcja Peana na n-sześcian:
    cyfry binarne przeplatają się
    między n współrzędnymi obrazu
    domkniętego zbioru Cantora.
    Każda współrzędna jest ciągła,
    bo ogony szeregu są jednostajnie
    ograniczone przez 2^-m;
    każdy punkt sześcianu ma
    rozwinięcia binarne.
    Rozszerzenia z twierdzenia Tietzego
    są ciągłe i mają wartości w [0,1];
    obraz całego przedziału zawiera
    obraz C, czyli cały sześcian.

## Korekty audytu 01

- Naprawiono angielsko-polski tytuł
  „Granice odwrotne compactów” na
  „Granice odwrotne przestrzeni zwartych”.
- Usunięto z zapowiedzi obietnicę
  dowodu braku spójności drogowej,
  którego w tym rozdziale nie ma.
- Skorygowano niespójność wielkości
  liter w teście integracji.
- Rozszerzono zewnętrzne odsyłacze
  samodzielnego punktu wejścia
  o rozdziały 05, 08 i 23.
- Zapis `\\(` w podsumowaniu zastąpiono
  poprawnymi ogranicznikami matematycznymi.
- Umieszczono podpis przy wykresie
  odwzorowania namiotowego poza jego
  linią, aby nie nakładał się na wykres.
- Dodano dowód surjekcji
  przedziału na sześcian z użyciem
  kodowania Cantora i Tietzego.

## CI i zakres nieukończonego audytu

Wersje przejściowe CI miały błędy
związane z niespójnością testów/integracji;
przedwczesnych przebiegów nie należy
interpretować jako wyniku końcowego źródła.
Aktualny etap wymaga:
1) pomyślnego CI z pełną kompilacją
   całej książki i rozdziału 25;
2) pobrania i wizualnej inspekcji PDF,
   w tym rysunku odwzorowania namiotowego;
3) dwóch kolejnych czystych audytów
   i dodatkowego audytu, bez modyfikacji
   źródła w tym okresie.

**Wynik audytu 01: korekcyjny — 0/2.**
