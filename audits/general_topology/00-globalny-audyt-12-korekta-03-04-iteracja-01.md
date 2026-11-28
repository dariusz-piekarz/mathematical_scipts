# Topologia ogólna — audyt globalny 12: rewalidacja 03–04, kontrola czysta 1/2

**Data:** 2026-11-22.
**Bloby sprawdzane bez edycji:**
- rozdział 03: `021f4f843b26e90dca57b3e38b33e95cd0c03a5b`,
- rozdział 04: `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081`.

**Wynik:** pierwsza czysta kontrola matematyczno-strukturalna
na nowych blobach. Samo CI i ostatni render
są wymagane osobno.

## Kontrola różnic względem wersji zatwierdzonych

Porównano bieżące pliki z wersjami
`0c0395aebcf21a1ec253c21499049642dd710798`
i `ba468b3413b37bf6cd7776761eb67195951ccd20`.

- Wszystkie **39 etykiet** rozdziału 03
  i wszystkie **40 etykiet** rozdziału 04 zachowano,
  w identycznej kolejności.
- Liczby środowisk `twierdzenie`, `lemat`,
  `stwierdzenie`, `wniosek`,
  `definicja`, `przyklad`,
  `proof` i `figure` nie zmieniły się
  w żadnym z dwóch rozdziałów.
- Nadal występują **15 dowodów** w rozdziale 03
  i **17 dowodów** w rozdziale 04.
- Rozdział 03 zachowuje standardową komendę
  `\section{Podsumowanie i zależności}`
  i etykietę sekcji. Nie stosujemy
  niestandardowego ręcznego licznika
  zakłócającego analizę sekcji przez aplikację.
- Rozdział 04 zachowuje standardową sekcję
  `Zestawienie własności uniwersalnych`
  i jej etykietę.
- Odsyłacz do powtórzonego przykładu w 03
  wskazuje istniejącą etykietę
  `ex:topog-bijekcja-niehomeomorfizm`
  w tym samym rozdziale.

## Ponowna kontrola zmienionego dowodu w 03

Dla homeomorfizmu `f:X→Y` i `A⊂X`:
1. Otwartość `f` daje
   `f(int_X A)⊂int_Y f(A)`,
   a zastosowanie tego samego
   do `f^{-1}` daje odwrotną inkluzję.
2. Ciągłość `f` i `f^{-1}`
   daje dwie inkluzje
   dla domknięć, a więc równość.
3. Bijekcja zachowuje dopełnienie
   i przecięcia; wzór na brzeg
   przez przecięcie dwóch domknięć
   daje równość dla brzegu.
4. Punkty zbioru pochodnego
   są określone przez każde
   otwarte otoczenie spotykające
   `A\setminus\{x\}`. Homeomorfizm
   daje odpowiedniość otoczeń,
   a jawna równość obrazów
   przecięć z usuniętym punktem
   dowodzi równości zbiorów pochodnych.
5. Stąd wynikają także
   zachowanie gęstości,
   otwartości, domkniętości
   i izolowania punktów.

Nie usunięto żadnego z
pięciu kroków argumentacji,
a jedynie ograniczono powtórzenia
w ich opisie. Definicja zanurzenia
i kryterium zanurzenia są niezmienione.

## Ponowna kontrola zakończenia 04

Topologia początkowa jest najmniejszą
topologią wymuszającą ciągłość
rodziny odwzorowań wychodzących
z danej przestrzeni. Topologia końcowa
jest największą topologią wymuszającą
ciągłość rodziny odwzorowań
do niej wchodzących.
W tekście poprawnie przyporządkowano
podprzestrzeń i iloczyn
pierwszej konstrukcji,
a sumę rozłączną i iloraz — drugiej.
Scalenie uwagi z podsumowaniem
zachowało rozróżnienie kierunku
sprawdzania ciągłości.

## Kontrola składu

Źródło 03 wykorzystuje lokalnie
`\enlargethispage{4\baselineskip}`
przed ostatnim przykładem,
aby uniknąć osierocenia
standardowej sekcji 3.7.
Jest to zabieg typograficzny,
nie wpływający na matematyczne
twierdzenia; wymaga kontroli,
czy nie zbliży tekstu
nadmiernie do stopki.
Rozdział 04 został już
wydany bez pustej strony końcowej
w [CI 45066436226](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066436226),
które zakończyło się pomyślnie.
Ostateczny wynik dla 03
zależy od renderingu
nowego bloba.

**Status:** czysty matematycznie i strukturalnie 1/2;
skład 03 w rewalidacji.
