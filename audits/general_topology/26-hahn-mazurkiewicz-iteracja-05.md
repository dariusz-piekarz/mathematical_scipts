# Topologia ogólna — rozdział 26, audyt 05 (drugi czysty)

**Data:** 2026-11-22.
**Badany bez zmian blob:** `9f1ea17248b4df5805c025ba7bb47219c1dd4562`.
**Status:** CZYSTY 2/2, drugi niezależny audyt
na identycznym pliku jak w audycie 04.

## Dowód konieczności: analiza wszystkich przejść

**A. Zwartość i spójność.**
Niepusty odcinek [0,1] jest zwarty
i spójny. Ciągła surjekcja
przenosi te własności na X;
współdziedzina X z założenia
jest Hausdorffa. Nie pojawia się
nieuprawniona teza, że dowolny
ciągły obraz przestrzeni Hausdorffa
jest Hausdorffa.

**B. Drugi aksjomat przeliczalności.**
Nie jest on dziedziczony przez
arbitralne surjekcje ciągłe.
Tu istotne jest, że f ma dziedzinę
**zwartą**, a X jest Hausdorffa.
Dla skończonej sumy V
elementów przeliczalnej bazy
odcinka zbiór
W_V=X\f([0,1]\V) jest otwarty.
Jego otwartość korzysta
z domkniętości obrazu
zwartych podzbiorów przy f
w przestrzeni Hausdorffa.
Dla x∈O otwartego
zwarty przeciwobraz f^{-1}({x})
daje skończoną rodzinę bazową V
taką, że f^{-1}({x})⊂V⊂f^{-1}(O).
Stąd x∈W_V⊂O.
Liczba wszystkich skończonych
sum zbiorów z bazy przeliczalnej
pozostaje przeliczalna.
To jest rzeczywisty dowód
przeliczalności bazy X.

**C. Lokalna spójność.**
Dla x∈O każdemu punktowi włókna
F=f^{-1}({x}) przypisujemy
przedział domknięty w [0,1]
ze względnym otwartym wnętrzem
zawartym w f^{-1}(O).
Zwartość F daje skończoną
podrodzinę przedziałów,
których wnętrza pokrywają F.
Każdy obraz przedziału
jest spójny i zawiera ten sam
punkt x, więc ich suma K
jest spójna i leży w O.
Dla V będącego sumą wnętrz
W=X\f([0,1]\V) jest otwarty,
zawiera x i leży w K.
W konsekwencji cała
składowa spójna O jest
otwarta: rozumowanie
powtarzamy dla każdego jej punktu.
Zgodność z definicją lokalnej
spójności wynika z istniejącej
w rozdziale 08 charakteryzacji.

**D. Metryzowalność.**
Wynik B daje drugi aksjomat
przeliczalności; zwartość
i Hausdorffowość dają
regularność i T1.
Twierdzenie Urysohna
z rozdziału 10 działa więc
bez żadnej brakującej hipotezy.

## Testy niezależnych przesłanek

- Dwupunktowy zbiór dyskretny
  spełnia wszystkie wymagania
  poza spójnością.
- Solenoid dyadyczny jest
  zwartym spójnym continuum metrycznym,
  ale brak mu lokalnej spójności.
- Cantor nie jest lokalnie spójny,
  bo każde **niepuste** spójny
  podzbiór jest singletonem,
  a singletony nie są otwarte.
  Nie został wykorzystany jako
  fałszywy przykład lokalnej spójności.
- Dwupunktowa przestrzeń Sierpińskiego
  jest surjektywnym ciągłym obrazem
  odcinka, lecz nie jest Hausdorffa
  i nie jest metryzowalna.
  Zatem nie można bez komentarza
  wykreślać aksjomatu Hausdorffa.

## Redakcja i odsyłacze

Sprawdzono odsyłacze
do rozdziału 08 (spójność lokalna),
10 (Urysohn) i 25 (continua Peana),
z zachowaniem odrębności skryptów.
Środowiska, etykiety i zakazana
terminologia nie wykazują nowych usterek.
Bloba źródła nie zmieniono.

**Wynik: czysty 2/2.** Pozostaje
audyt dodatkowy 3/2 i
potwierdzenie z nowego PDF,
że korekta wydawnicza
usunęła niemal pustą
stronę końcową.
