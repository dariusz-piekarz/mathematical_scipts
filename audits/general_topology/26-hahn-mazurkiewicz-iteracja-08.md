# Topologia ogólna — rozdział 26, audyt 08 (drugi czysty)

**Data:** 2026-11-22.
**Niezmieniony blob z audytu 07:** `161d04d779ae86554f81c11bb24daa842c8dd363`.
**Wynik:** CZYSTY 2/2 — drugi, niezależny audyt
dotyczący hipotez, wyniku konieczności,
kontrprzykładów i odsyłaczy.

## Kierunek konieczny — analiza przyczynowa

1. Niepustość, zwartość i spójność
   wynikają z istnienia ciągłej
   surjekcji odcinka bez dodatkowego
   warunku metrycznego.
   Aksjomat Hausdorffa dla X
   jest hipotezą twierdzenia.
2. Drugiego aksjomatu przeliczalności
   nie przenosi automatycznie
   dowolna surjekcja ciągła.
   Dowód używa domkniętości
   zwartego obrazu w X Hausdorffa,
   czyli kluczowo dwóch hipotez:
   zwartego odcinka i Hausdorffowości X.
3. Dla każdej skończonej sumy
   V elementów przeliczalnej
   bazy odcinka W_V=X\f([0,1]\V)
   jest otwarty. Jeżeli x∈O,
   kompaktowe włókno f^{-1}(x)
   mieści się w skończonej sumie V
   bazowych otwartych zbiorów,
   z V⊂f^{-1}(O).
   Wtedy x∈W_V⊂O, a
   rodzina wszystkich takich W_V
   jest przeliczalna.
4. Lokalna spójność wynika
   ze spójności obrazów
   domkniętych przedziałów.
   Każdy wybrany przedział
   zawiera punkt włókna x,
   więc jego obraz zawiera x.
   Suma skończenie wielu
   spójnych zbiorów o
   niepustej części wspólnej
   jest spójna. Z otwartego
   W_V⊂K⊂O wynika,
   że składowa spójna
   O zawierająca x
   jest otwartym otoczeniem x;
   powtarzamy dla jej punktów.
5. Regularność T1 wynika
   ze zwartości Hausdorffa.
   Drugi aksjomat przeliczalności
   pozwala zastosować
   wcześniejsze twierdzenie
   Urysohna o metryzowalności
   z rozdziału 10.
6. Przy sformułowaniu
   głównego twierdzenia
   wszystkie cztery
   własności z warunku (ii)
   są jawnie wymienione:
   zwartość, spójność,
   lokalna spójność
   i metryzowalność.
   Brak przemilczanych
   dodatkowych założeń.

## Sprawdzenie przykładów granicznych

- Jednoelementowe X jest
  Peanowskie, a surjekcja
  [0,1]→X jest stała.
- Dwupunktowa przestrzeń
  dyskretna jest lokalnie
  spójna i metryzowalna,
  ale niespójna, więc
  nie może być ciągłym
  obrazem odcinka.
- Solenoid dyadyczny
  jest zwartym spójnym
  continuum metrycznym,
  ale nie jest lokalnie spójny;
  nie jest obrazem odcinka.
- Zbiór Cantora nie jest
  spójny i nie jest
  lokalnie spójny:
  jego każdy **niepusty**
  spójny podzbiór
  jest singletonem.
- Sierpiński Y={0,1} z
  topologią {∅,{1},Y}
  jest surjektywnym
  ciągłym obrazem [0,1]
  przez f(0)=0, f(t)=1
  dla t>0, ale nie jest
  Hausdorffa. Zatem
  warunek T2 w twierdzeniu
  nie może zostać
  pominięty bez zmiany tezy.

## Redakcja i granice audytu

Sprawdzono referencje do
rozdziałów 08, 10 i 25,
ciągłość rozumowania
i zgodność terminologii.
Rozdział nie powtarza już
wcześniejszego przykładu
grafów i sześcianów.
Wszystkie 9 środowisk
dowodu, 22 etykiety i
19 odsyłaczy pozostają
spójne oraz poprawnie
zamknięte w źródle.

**Status: czysty 2/2 na identycznym blobie.**
Pozostaje dodatkowy audyt 3/2
wraz z obejrzeniem rzeczywistego
końcowego PDF i CI.
