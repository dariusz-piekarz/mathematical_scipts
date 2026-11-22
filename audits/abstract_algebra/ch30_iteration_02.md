# Algebra abstrakcyjna — AA-30, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026  
**Rozdział:** Konstrukcje cyrklem i linijką oraz wielokąty foremne  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` repozytorium `dariusz-piekarz/mathematical_scipts`  
**Wynik:** **STABILNY**. Drugi audyt nie wymagał zmian w źródle (0 korekt).

## Zbadane zagadnienia

1. Definicja konstrukcji za pomocą skończonej liczby izolowanych przecięć prostych i okręgów. Wykluczono arbitralny wybór punktu z pokrywających się obiektów.
2. Lemat o dodawaniu, odejmowaniu, mnożeniu, dzieleniu wyłącznie przez liczbę niezerową i pierwiastkowaniu liczb nieujemnych. Sprawdzono geometryczne równania prostych i okręgu o średnicy `[0,1+a]`, także dla ujemnych argumentów działań arytmetycznych, gdy to dozwolone.
3. Równoważność konstruowalności z przynależnością obu współrzędnych do skończonej rzeczywistej wieży rozszerzeń stopnia co najwyżej dwa. Osobno sprawdzono przecięcia dwóch prostych, prostej z okręgiem i dwóch okręgów, jak też indukcję odwrotną.
4. Lemat o domknięciu normalnym wieży kwadratowej: indukcyjne dołączanie pierwiastków kwadratowych wszystkich sprzężeń i przejście do grupy Galois będącej `2`-grupą.
5. Kontrprzykład `f(X)=X^4-X-1`: nierozkładalność nad `Q` i modulo `2`, bezkwadratowość, rezolwenta sześcienna `Y^3+4Y-1`, działanie grupy na podziałach pierwiastków, wyróżniki `-283`, rozkład modulo `7`, dwa pierwiastki rzeczywiste, sprzężenie zespolone jako transpozycja, grupa `S_4`, brak konstruowalności rzeczywistego pierwiastka stopnia cztery.
6. Niemożliwość podwojenia sześcianu i ogólnej trysekcji kąta.
7. Kryterium Gaussa–Wantzela: obie implikacje, rzeczywiste ciało elementów stałych sprzężenia zespolonego, łańcuch podgrup indeksu dwa, konstrukcja sinusa z pierwiastka kwadratowego oraz postać liczb pierwszych Fermata. Sprawdzono wzory dla pięciokąta.

## Testy i kompilacja

- **31/31 PASS:** ponownie uruchomiono kompletny zestaw z audytu I; wersja dostosowana do GitHub w `tools/tests/test_abstract_algebra_ch30.py`.
- **27/27 PASS:** dodatkowe, niezależne kontrole w `tools/tests/test_abstract_algebra_ch30_independent.py`. Sprawdzono m.in. rząd grup Galois dla `X^4-X-1` (`24`, `S_4`) i `X^4-2` (`8`), tożsamości rezolwenty, nierozkładalność, liczbę pierwiastków rzeczywistych, kryterium Gaussa–Wantzela dla `3 ≤ n ≤ 2000` oraz wzory trygonometryczne pięciokąta.
- Przy pierwszym uruchomieniu nowych testów naprawiono wyłącznie **błąd testu**: użycie liczby zmiennoprzecinkowej zamiast dokładnego typu `Integer` z SymPy w próbie równania geometrycznego. Wersja końcowa: 27/27 PASS, **bez zmiany tekstu**.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS**; PDF zawiera **6 stron**. Brak ostrzeżeń LaTeX, niezdefiniowanych odsyłaczy, przepełnień `Overfull/Underfull` i błędów.
- Wyrenderowano i obejrzano wszystkie strony PDF. Rysunek pięciokąta i jego podpisy są czytelne, bez widocznych kolizji.
- W pomocniczej kompilacji wstrzyknięto wyłącznie zastępcze numery dwóch zewnętrznych odsyłaczy, których **rzeczywiste etykiety osobno sprawdzono na GitHub**. Kompilacja nie jest równoważna kompilacji całej książki.

## Kontrola integralności

- SHA-256 źródła: `4b8d1785dfbe63ac39aacfd86d5b24d689d5fd3f0ad2f8e08ab8b4631f76e747`, bez zmian względem audytu I.
- Git blob SHA źródła: `f9d6e4e96d41e3faba57f9c9f895c99611c12998`.
- **12 unikatowych etykiet**, **7 wystąpień odsyłaczy**. Dwa cele zewnętrzne: `aa:tw:orbita-stabilizator` (AA-03), `aa:tw:cyclotomic-galois` (AA-28); oba potwierdzone w GitHub. Brak przedwczesnego odsyłacza do AA-31.
- Publikacja na GitHub: `chapters/pl/abstract_algebra/30-konstrukcje-cyrklem-i-linijka-oraz-wielokaty-foremne.tex`, `tools/tests/test_abstract_algebra_ch30.py`, `tools/tests/test_abstract_algebra_ch30_independent.py`, `books/pl/abstract_algebra.tex`, `catalog/books.json`, `.github/workflows/abstract-algebra-chapter.yml`.
- Ponowny odczyt po publikacji potwierdził zgodność bajtową źródła i obu zestawów testów; w katalogu **30 rozdziałów**, w książce `\input` AA-30, w workflow testy i kompilacja AA-01–AA-30.

**Ograniczenie:** nie uruchomiono ani nie potwierdzono wyniku zdalnego GitHub Actions ani pełnej kompilacji całej książki. PASS dotyczy lokalnej kompilacji izolowanej oraz testów matematycznych wykonanych w bieżącej iteracji.

## Status

**AA-30 STABILNY po audycie II i opublikowany w GitHub.** Następny etap: **AA-31, audyt I**.
