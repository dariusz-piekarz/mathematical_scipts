# Algebra liniowa — rozdział 09, audyt I (konstrukcja i wstępna kontrola)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**SHA kontrolowanej treści:** `6639b04df4de851feeb6e29e4e6afa39fdaf3764`

## Zakres

Utworzono rozdział „Iloczyny tensorowe”: konstrukcja z wolnej przestrzeni `K^(V×W)` i ilorazu przez warunki dwuliniowości, własność uniwersalna, jednoznaczność realizacji, tensory proste i ich zerowanie, bazy i wymiar, rząd tensora, iloczyn odwzorowań, macierze Kroneckera i ich rząd, zamiana i łączność, czynnik jednostkowy, wiele czynników i linearyzacja, odwzorowania o skończonym rzędzie, duale, sumy proste i ilorazy, kontrakcja oraz ślad. Diagram własności uniwersalnej przygotowano bez użycia zewnętrznych grafik.

## Wstępna kontrola dowodów

1. Własność uniwersalna podaje kwantyfikatory: dla każdej przestrzeni `Z` i każdego dwuliniowego `b` istnieje dokładnie jedno liniowe przedłużenie. Konstrukcja posługuje się funkcjami o skończonym nośniku i czterema rodzinami generatorów podprzestrzeni `N`.
2. Jednoznaczność dwóch realizacji udowodniono przez zastosowanie obu własności uniwersalnych, bez narzucania skończonego wymiaru.
3. Wektor `v⊗w` jest niezerowy, gdy oba czynniki są niezerowe: dowód korzysta z funkcjonałów rozdzielających i jawnie odwołuje się do istnienia baz Hamela w wymiarze nieskończonym.
4. Baza `v_i⊗w_j` została zweryfikowana przez funkcjonały współrzędnych indukowane przez własność uniwersalną; wynik obejmuje przestrzenie zerowe.
5. Minimalną liczbę tensorów prostych przedstawiających `t` porównano z rzędem macierzy współczynników w obu kierunkach. Jako kontrprzykład prostoty podano tensor o macierzy `I_2`.
6. Macierz `S⊗T` ma współczynniki `a_{pi}b_{qj}` przy określonym leksykograficznym porządku par; rząd iloczynu Kroneckera wyprowadzono z baz dostosowanych do jąder i obrazów.
7. Łączność i zamiana czynników są określone jako kanoniczne izomorfizmy, nie dosłowne równości dwóch odmiennych konstrukcji ilorazowych.
8. Odwzorowanie `W⊗V*→Hom(V,W)` ma dokładnie obraz skończonego rzędu; dowód iniektywności wykorzystuje liniowo niezależne wektory z `W`.
9. Iloczyn tensorowy sumy prostej oraz ilorazu udowodniono za pomocą rozkładu algebraicznego. Wzór na ślad jako kontrakcję jest niezależny od wyboru bazy.

## Weryfikacja techniczna

Weryfikacja lokalna na pobranej treści: `41` unikalnych etykiet, `14` odsyłaczy, domknięte środowiska LaTeX, brak niepożądanych form terminologicznych. W tym commicie dodano rejestrację rozdziału do książki i katalogu oraz rozbudowano dedykowaną kontrolę CI. Kompilacja PDF, sprawdzenie wszystkich odsyłaczy i niezależne testy obliczeniowe następują w kolejnej iteracji.

**Status:** rozdział 09 otwarty po audycie I; nie zamykać do uzyskania czystego kolejnego audytu i potwierdzenia CI.
