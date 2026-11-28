# Algebra liniowa — rozdział 01: audyt, iteracja 1

Data: 2026-11-21  
Gałąź: `algebra-liniowa`  
Plik: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`

## Zakres audytu

1. Język i terminologia: ciało skalarów, przestrzeń wektorowa, podprzestrzeń, przestrzeń rozpięta, niezależność liniowa, baza Hamela.
2. Matematyka: kompletność założeń i kwantyfikatorów, dowody własności aksjomatów, kryterium podprzestrzeni, własności rozpinania, kryteria niezależności, lemat Steinitza, istnienie i jednoznaczność współrzędnych, bazy w nieskończonym wymiarze.
3. Przykłady: \(K^n\), \(K[X]\), \(K^S\), \(\mathbb C\) nad \(\mathbb R\), \(\mathbb F_2^2\), przestrzeń ciągów o skończonym nośniku, przestrzeń ciągów rekurencyjnych.
4. Rysunki i technika: brak zależności od plików obrazów, oznaczenia i podpisy, parowanie środowisk LaTeX, etykiety i odsyłacze.

## Wykryte nieprawidłowości i poprawki

- **Błąd merytoryczny — dołączanie wektora do zbioru:** pierwotne kryterium sugerowało, że \(S\cup\{v\}\) jest niezależny wtedy i tylko wtedy, gdy \(v\notin\operatorname{span}(S)\) również dla \(v\in S\). W tym przypadku unia zbiorów nie zmienia \(S\), więc twierdzenie było fałszywe. Dodano jawne założenie \(v\notin S\), zmieniono dowód oraz wydzielono uwagę o rodzinach indeksowanych.
- **Luka argumentacyjna — lemat o wymianie Steinitza:** doprecyzowano sprzeczność w przypadku \(r>m\): po \(m\) wymianach pozostałyby wyłącznie \(v_1,\ldots,v_m\), co wymuszałoby zależność \(v_{m+1}\).
- **Tytuł o podprzestrzeniach:** zastąpiono nieprecyzyjne określenie „suma zbiorów” terminem „unia podprzestrzeni”.
- **Redakcja:** skorygowano formy gramatyczne i utrzymano rozróżnienie zbioru od rodziny indeksowanej.

## Wyniki kontroli statycznej po poprawkach

- Etykiety \(\backslash label\): **55**, wszystkie unikalne w rozdziale.
- Odsyłacze lokalne \(\backslash ref\), \(\backslash eqref\): bez brakujących celów.
- Środowiska \(\backslash begin\), \(\backslash end\): zgodne i domknięte.
- Rysunek: kod TikZ w samym pliku; brak zależności od zewnętrznego obrazu.
- Książka \(books/pl/linear_algebra.tex\) i wpis w \(catalog/books.json\) dodane; parser aplikacji posiada identyfikator \(LA\).

## Ograniczenia obecnej iteracji

Pełna kompilacja aktualnego rozdziału przez `latexmk` i sprawdzenie wizualnego składu nie zostały jeszcze potwierdzone. Weryfikacja statyczna nie zastępuje kompilacji ani ponownego audytu matematycznego. W środowisku lokalnym sprawdzono działanie preambuły testowej ze środowiskiem twierdzenia, pakietem `babel` i rysunkiem TikZ, ale **nie całego rozdziału**.

## Status

**Iteracja 1: przygotowanie rozdziału + pierwszy audyt z poprawkami wykonane.**
Nie oznaczać rozdziału jako ostatecznie zamkniętego. W następnej iteracji ponownie audytować wyłącznie rozdział 01; dopiero po audycie bez nowych merytorycznych i redakcyjnych braków przejść do rozdziału 02.
