# Algebra liniowa — rozdział 05: audyt stabilizacyjny III (pierwszy czysty po korekcie)

**Data:** 22 listopada 2026.
**Źródło:** \`chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex\`.
**SHA źródła:** \`c238cb3232b69fb19d0dfe1062af05a2a0d8ddb8\`, bez zmian w tej iteracji.

## Niezależna weryfikacja wszystkich głównych argumentów
- **Elementarne działania:** każdy z trzech rodzajów działań na wierszach ma poprawną operację odwrotną, a działanie na macierzy rozszerzonej zachowuje cały zbiór rozwiązań. Warunek \(\lambda\ne0_K\) jest wyraźny przy normalizacji, a przy \(i\ne j\) dodatkowo nie zmienia się wiersz użyty do eliminacji.
- **Skończoność algorytmu:** indeksy \`j=1,...,n\` są przeglądane tylko raz, liczba wybranych pivotów wynosi najwyżej \(\min(m,n)\); pominięte kolumny pozostają zerowe w rozpatrywanych niższych wierszach. Operacje wsteczne od ostatniego pivotu nie psują kolumn bazowych wcześniej wyzerowanych.
- **Rząd:** w postaci schodkowej rzut z jądra na \`n-r\` współrzędnych swobodnych jest bijektywny, bo każdy zestaw wartości pozwala jednoznacznie obliczyć współrzędne pivotowe. Wyprowadzono \(\dim\ker A=n-r\) i \(\operatorname{rk}A=r\), z oddzielną interpretacją pustej rodziny.
- **Zgodność:** sprawdzono każdą implikację w teście \(\operatorname{rk}A=\operatorname{rk}[A|b]\) i nieistnieniu sprzecznego wiersza. **Nowe uzasadnienie** jest ścisłe: jeśli \(b\ne0\), zbiór rozwiązań zgodnego układu nie zawiera \(0_{K^n}\), a zatem nie jest podprzestrzenią. W szczególności dotyczy to także zerowego wymiaru dziedziny.
- **Bazy:** wektory jądra konstruowane z \(-R_{if}\) są niezależne i rozpinające ze względu na współrzędne swobodne. Bazę obrazu tworzą indeksowane przez pivoty kolumny **A, nie R**. Dowód z \(R=PA\) i odwracalnością \(P\) ma oba wymagane kierunki.
- **Jednoznaczność RREF:** niezmienniczość przestrzeni wierszy ustala zbiór pivotów jako możliwe pierwsze niezerowe indeksy wektorów tej przestrzeni; to ustala niezależnie współczynniki wierszy przez wartości w kolumnach pivotowych. Argument jest poprawny także dla przestrzeni wierszy zerowej.
- **Gauss–Jordan:** macierz rozszerzona \([A|I_n]\) zmienia się na \([PA|P]\); z \(\operatorname{rk}A=n\) wynika RREF lewego bloku \`I_n\`. Bezpośrednio sprawdzono przykład \(\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\) i jego odwrotność.

## Testy
1. Trwały test \`tools/test_linear_algebra_ch05.py\`: **1553** macierze nad \(\mathbb F_2,\mathbb F_3\), **12558** układów ze wszystkimi prawymi stronami, dwa niezależne wybory pivotu, bazy jądra i obrazu, Gauss–Jordan i przypadki 0-wymiarowe — **PASS**.
2. Dodatkowa niezależna weryfikacja nad \(\mathbb Q\) z arytmetyką dokładną (\`fractions.Fraction\`) w zestawieniu z \`sympy.Matrix.rref\`: **800** losowych macierzy rozmiarów od \(1\times1\) do \(4\times5\), z ustalonym ziarnem 20261122; wszystkie dały identyczne RREF i indeksy pivotów. Sprawdzono oddzielnie opublikowany przykład \((3\times4)\), obie prawe strony, przestrzeń zerową, jądro, kolumny obrazu i odwrotność \(2\times2\). **PASS**.

## Redakcja i integralność
- Źródło po korekcie: **752 wiersze**, **10 twierdzeń/stwierdzeń/wniosków z następującymi dowodami**, cztery przykłady, 27 etykiet i 16 poprawnych odsyłaczy.
- W rozdziałach 01–05: **226 unikatowych etykiet**, brak zderzeń. Środowiska \`begin/end\` są poprawnie sparowane i zagnieżdżone.
- Brak wykrytych odstępstw od polskiej terminologii. Nie dodawano nowych tematów ani twierdzeń.

**Decyzja:** audyt III **czysty** na SHA \`c238cb3...\`. Potrzebny jeszcze kolejny czysty audyt na tym samym źródle oraz potwierdzenie finalnej kompilacji PDF z tego SHA. W chwili raportu nowe workflow wykonywały jeszcze kompilację.
