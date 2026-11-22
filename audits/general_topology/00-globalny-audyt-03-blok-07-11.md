# Topologia ogólna — globalny audyt 03, blok 07–11

**Data:** 2026-11-22.
**Przedmiot:** matematyczny przegląd wybranych kluczowych
twierdzeń rozdziałów 07–11, bez dodatkowej edycji ich źródeł.
**Status:** kontrola tematyczna czysta;
nie oznacza audytu wszystkich dowodów tego bloku.

## Przejrzane twierdzenia i uzasadnienia

### Rozdział 07: twierdzenie Tychonoffa

Dla dowolnego zbioru indeksów I autor wyodrębnił
pusty produkt (przestrzeń jednopunktowa) oraz produkt
z pustym czynnikiem (przestrzeń pusta).
Dla rodziny wszystkich czynników niepustych jawnie
użyto aksjomatu wyboru, zarówno do istnienia elementu
produktu, jak i do jednoczesnego wyboru granic
ultrafiltrów rzutowanych. Przeciwobrazy pod rzutowaniem
zachowują dopełnienia i przecięcia skończone;
zbieżność wszystkich rzutowań implikuje zbieżność
ultrafiltru na produkcie, ponieważ otoczenia bazowe
ograniczają jedynie skończenie wiele współrzędnych.
Warunki przy zastosowaniu kryterium ultrafiltrów
zostały zachowane.

### Rozdział 08: składowe spójne

Składowa spójna C(x) jest sumą wszystkich spójnych
podzbiorów zawierających x, a zatem jest spójna
ze względu na wspólny punkt. Jej domknięcie
jest nadal spójne; maksymalność wymusza
domkniętość C(x). Składowe przecinające się
są równe, co daje rozkład X. Tekst nie
twierdzi, że składowe muszą być otwarte;
podaje \(\mathbb Q\) jako przeciwny przykład.
W przykładzie Cantora każda skończona informacja
o cyfrach wyznacza podzbiór otwarto-domknięty,
co rozdziela dowolne dwa punkty;
nie jest to twierdzenie o dyskretności zbioru Cantora.

### Rozdział 09: przeliczalność i metryzowalność

Przejrzano równoważność ośrodkowości,
drugiego aksjomatu przeliczalności i własności
Lindelöfa dla *przestrzeni metrycznych*:
- baza kul o środkach z przeliczalnego D i wymiernych
  dodatnich promieniach daje ośrodkowość -> drugi aksjomat;
- dla Lindelöfa pokrycia kulami promienia 1/n
  dają co najwyżej przeliczalne zbiory ich środków D_n,
  których suma jest gęsta;
- przypadek przestrzeni pustej został jawnie
  oddzielony od dowodu dla niepustej.
Rozdział nie przedstawia żadnej z tych równoważności
jako twierdzenia dla dowolnych przestrzeni topologicznych.

### Rozdział 10: metryzowalność Urysohna

Sprawdzono konstrukcję przeliczalnych par
\((B,C)\) z \(\overline B\subseteq C\),
zawężanie otoczeń z regularności
i uzyskanie funkcji Urysohna rozdzielających punkty.
Metryka \(\sum2^{-n}|f_n(x)-f_n(y)|\)
ma nieujemność, symetrię, dodatnią określoność
i nierówność trójkąta. Obie inkluzje topologii
są udowodnione osobno: ciągłość każdej f_n
daje otwartość kul, a oddzielenie
\(x\in O\) od dopełnienia O przez pewną f_n
daje otwartość O w metryce.
Przypadki przestrzeni pustej i jednoelementowej
są rozważone przed konstrukcją.

### Rozdział 11: twierdzenie Baire'a

Dowód przez zstępujące domknięte kule
o promieniach mniejszych niż 2^{-n}
ma prawidłowy schemat: gęstość kolejnego G_n
pozwala wybrać środek i domkniętą kulę
wewnątrz przecięcia poprzedniej otwartej kuli z G_n.
Środki tworzą ciąg Cauchy'ego;
granica należy do każdej domkniętej kuli.
Poprawnie rozróżniono zupełność metryki
i samą metryzowalność (przykład \(\mathbb Q\)).
Dowód, że \(\mathbb Q\) nie jest typu G_delta
w \(\mathbb R\), używa niepustości przecięcia
dwóch przeliczalnych rodzin zbiorów
otwartych i gęstych na zupełnej prostej.

## Zależności i zakres rozdziałów

Tychonoff (07) używa filtrów/ultrafiltrów
i iloczynów z 04–06. Składowe spójne (08)
korzystają ze spójności ich sumy/domknięcia.
Drugi aksjomat przeliczalności (09)
wraz z T3 jest hipotezą metryzowalności (10).
Metryzowalność sama nie daje Baire'a (11):
potrzebna jest zupełność zgodnej metryki
albo inna odpowiednia hipoteza, np. lokalna zwartość
Hausdorffa, omówiona dopiero w 14.
Nie znalazłem logicznego użycia lokalnej zwartości
przed jej zdefiniowaniem w 14.

**Wynik:** przejrzane dowody są spójne i bez
wskazanych nieuzasadnionych kroków.
Pozostałe dowody i przykłady 07–11 nadal
wymagają indywidualnego audytu.
Kolejne bloki: 12–17 i 18–22;
następnie pełna wizualna inspekcja rysunków
i kontrola nakładek między skryptami.
