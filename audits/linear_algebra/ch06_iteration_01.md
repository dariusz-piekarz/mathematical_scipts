# Algebra liniowa — rozdział 06, audyt 1

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/06-wyznaczniki-macierzy.tex`

## Cel i zakres

Utworzono nowy rozdział „Wyznaczniki macierzy”, rozwijający ukończone rozdziały 04–05. Materiał obejmuje znaki permutacji i ich multiplikatywność, definicję wyznacznika przez permutacje, wieloliniowość i naprzemienność wierszy, jednoznaczność znormalizowanej funkcji, wpływ operacji elementarnych, macierze trójkątne, transpozycję, multiplikatywność wyznacznika, kryterium odwracalności, niezmienniczość przy zmianie bazy, rozwinięcie Laplace'a, macierz dołączoną, wzory Cramera i interpretację geometryczną na `R^2` z samodzielnym rysunkiem TikZ.

## Kontrola pierwsza

- Podano wszystkie zmienne, ciała i zakresy wymiarów; przypadek `n=0` traktowany jest jawnie, a rozwinięcie Laplace'a, macierz dołączoną i wzory Cramera sformułowano dla `n>=1`.
- Dowód naprzemienności bezpieczny w charakterystyce `2`: parowanie permutacji o przeciwnych znakach, zamiast nieuprawnionego wniosku z `det A=-det A`.
- Dowód multiplikatywności opiera się na jednoznaczności naprzemiennej funkcji wieloliniowej i pozostaje poprawny dla `n=0`.
- Odwracalność wyprowadzono z reguł wyznacznika i z wcześniejszego algorytmu Gaussa bez zakładania istnienia wyznaczników mniejszych niż zero.
- Rozwinięcie Laplace'a wykorzystuje znak `(-1)^(i+j)` po przeniesieniu indeksów, a tożsamość macierzy dołączonej uwzględnia zarówno iloczyn lewo-, jak i prawostronny.
- Dla wzorów Cramera uzasadniono jednoznaczność rozwiązania i zanikanie wyznaczników z dwiema identycznymi kolumnami.
- Sprawdzono numerycznie przykład `3×3` z wyznacznikiem `13`, jego zachowanie w charakterystyce `13` i przykład Cramera `2×2` z rozwiązaniem `(2,1)`.
- Niezależny test enumeracyjny znaków permutacji sprawdził multiplikatywność dla wszystkich par permutacji zbiorów rozmiarów `0..5` — zero rozbieżności.

## Status

Pierwszy audyt matematyczny wykonano podczas tworzenia. Rozdział **pozostaje otwarty**, do kolejnego niezależnego audytu istniejącej treści oraz weryfikacji wyniku CI. Nie deklarujemy zakończonej kompilacji przed sprawdzeniem workflow.
