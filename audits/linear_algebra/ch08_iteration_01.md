# Algebra liniowa — rozdział 08, audyt 1 (opracowanie i weryfikacja)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/08-odwzorowania-wieloliniowe.tex`

## Zakres

Opracowano rozdział „Odwzorowania wieloliniowe”: definicja i podstawowe przykłady, współrzędne na krotkach wektorów bazowych i wzór na wymiar przestrzeni odwzorowań, zmiana baz, formy dwuliniowe i ich macierze, kongruencja i podprzestrzenie radykalne, symetria oraz naprzemienność (z pułapką charakterystyki `2`), wymiary i bazy form symetrycznych oraz naprzemiennych, determinanty form najwyższego stopnia, operatory symetryzacji i alternowania, diagonalizacja argumentów i wzór polaryzacyjny. Rozdział nie korzysta z iloczynów tensorowych, przewidzianych osobno dalej.

## Kontrola matematyczna pierwsza

- Wszystkie twierdzenia wymiarowe zakładają skończoną wymiarowość. Wyodrębniono przypadek `k=0` i uwzględniono zerowe wymiary przestrzeni.
- Udowodniono istnienie oraz jednoznaczność odwzorowania określonego przez wartości na krotkach bazowych, bez zakładania z góry istnienia abstrakcyjnego iloczynu tensorowego.
- W prawie transformacji współczynników każde wejście przekształca się macierzą `P_r`, a wyjście macierzą `Q^{-1}`; dla formy dwuliniowej daje to kongruencję `P^T A P`, nie podobieństwo.
- Lewy radykał ma współrzędne `ker A^T`, prawy `ker A`; dzięki twierdzeniu `rank A=rank A^T` ich zerowanie jest równoważne odwracalności macierzy.
- Rozróżniono naprzemienność od antysymetrii w charakterystyce `2`, gdzie przeciwne wartości mogą być równe. Wzór na wymiar form symetrycznych nie wymaga dzielenia przez współczynniki wielomianowe.
- Basis form naprzemiennych zbudowano przez wyznaczniki macierzy wartości elementów bazy dualnej, z kontrolą każdego przypadku `k>n`, `k=0`, `n=0`.
- Alternowanie wykazano przez parowanie przeciwnych składników nawet w charakterystyce `2`; normalizację operatorów podano wyłącznie przy `k!1_K\ne0_K`.
- Wzór polaryzacyjny oparto na sumie po wszystkich podzbiorach `S\subset\{1,...,k\}`, z kasowaniem krotek, które nie zawierają wszystkich indeksów. Nie wnioskowano o jednoznaczności, jeśli `k!1_K=0_K`.

## Integracja

Rozdział 08 zarejestrowano w pliku głównym, katalogu i osobnym workflow; dodano niniejszy raport. Wstępnie sprawdzono pary `\\begin/\\end`, unikalność `\\label` i zakazane formy terminologiczne. Niezależny audyt istniejącego tekstu i wynik GitHub Actions przeprowadzimy w następnej iteracji.

**Status:** rozdział 08 otwarty po pierwszym audycie; bez zgody na zamknięcie przed czystą kolejną iteracją i przejściem CI.
