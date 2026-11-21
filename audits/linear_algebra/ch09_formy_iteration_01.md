# Algebra liniowa — migracja kolejności rozdziałów i audyt I nowego 09

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`

## Decyzja redakcyjna i wykorzystane źródła

Na życzenie użytkownika teorię form dwuliniowych i kwadratowych umieszczono po rozdziale 08 o odwzorowaniach wieloliniowych i przed teorią iloczynów tensorowych. Jest to zgodne z logiką wykładu: wprowadzenie form, ich podstawowych własności i klasyfikacji poprzedza abstrakcyjną linearyzację wieloliniowości. Zachowano i przemianowano oba stabilne rozdziały tensorowe z wcześniejszych audytów.

Nowy rozdział 09 wykorzystuje:

- `chapters/pl/linear_algebra/08-odwzorowania-wieloliniowe.tex` — udowodnione wcześniej definicje form dwuliniowych, kongruencję macierzy, podstawy radykału i polaryzacji; nie powielono dowodów tych wyników;
- `chapters/pl/differential_geometry_and_topology/11-tensor-metryczny-dlugosc-i-miara.tex` — konstrukcję dodatnio określonej metryki, opis okręgu i elipsy jednostkowej w różnych bazach, ramkę ortonormalną, argumenty dotyczące bazy dualnej i rzutowania; odpowiednie fragmenty zaadaptowano do algebry liniowej bez odwoływania się do rozmaitości;
- `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` — zgodność abstrakcyjnej konstrukcji tensorowej i kontrakcji; nie przenoszono do nowego rozdziału 09 wyników wymagających znajomości iloczynu tensorowego.

## Zakres rozdziału 09

Ortogonalność, radykał i dopełnienie ortogonalne; wzór na wymiar dopełnienia; ortogonalna suma prosta; aksjomatyczna forma kwadratowa nad dowolnym ciałem i jej polaryzacja; współrzędne formy kwadratowej także w charakterystyce 2; ortogonalna diagonalizacja form symetrycznych w charakterystyce różnej od 2; prawo bezwładności Sylvestera nad liczbami rzeczywistymi; kryterium Sylvestera; nierówność Cauchy'ego--Schwarza; ortogonalizacja Grama--Schmidta i rzutowanie; postać blokowa form naprzemiennych, także w charakterystyce 2; przykłady, kontrprzykłady i rysunek TikZ zaadaptowany z DG.

## Bezstratna migracja rozdziałów

- Poprzedni `09-iloczyny-tensorowe.tex` przeniesiono do `10-iloczyny-tensorowe.tex`, zamieniając przestrzeń nazw etykiet i wewnętrznych odsyłaczy `lin9-` na `lin10-`.
- Poprzedni `10-algebry-tensorowa-symetryczna-i-zewnetrzna.tex` przeniesiono do `11-algebry-tensorowa-symetryczna-i-zewnetrzna.tex`, zamieniając `lin10-` na `lin11-` i odsyłacze do dawnego rozdziału 09 z `lin9-` na `lin10-`.
- W obu plikach **nie usuwano treści matematycznej**; poza techniczną zmianą przestrzeni nazw oraz numeracją plików i `\\input` zachowano ich wszystkie dowody, przykłady, rysunki i sekcje.
- Poprawiono importy w `books/pl/linear_algebra.tex`, rejestrację w `catalog/books.json` i listę sprawdzaną w dedykowanym workflow. Historyczne raporty `ch09_iteration_01–06` i `ch10_iteration_01–03` dotyczą starych numerów, dlatego pozostawiono je nienaruszone jako dokumentację pierwotnych audytów tensorowych. Bieżący raport dotyczy nowego rozdziału 09.

## Stan pierwszej kontroli

Skontrolowano ręcznie konstrukcję formy kwadratowej, diagonalizację, przypadki zerowego wymiaru i dodatniej charakterystyki, dowód prawa bezwładności przez maksymalne podprzestrzenie dodatnie i ujemne, kryterium Sylvestera przez dopełnienie Schura oraz klasyfikację form naprzemiennych przez bloki `J`. Nie dostrzeżono błędnego przejścia wymagającego dzielenia przez 2 w charakterystyce 2.

**Status:** nowy rozdział 09 otwarty do niezależnego audytu II, kontroli wszystkich etykiet i kompilacji książki po migracji. Stare rozdziały tensorowe 10–11 zachowują wyniki dotychczasowych audytów, ale również muszą przejść CI po zmianie odsyłaczy.
