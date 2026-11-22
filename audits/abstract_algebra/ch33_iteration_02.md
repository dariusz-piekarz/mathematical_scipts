# Algebra abstrakcyjna — AA-33, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026.  
**Rozdział:** „Wypadkowa wielomianów i macierz Sylvestera”.  
**Gałąź GitHub:** `biblioteka-matematyczna-iteracja-6`, repozytorium `dariusz-piekarz/mathematical_scipts`.  
**Decyzja:** **AA-33 STABILNY po audycie II**; **0 zmian źródła** w tej iteracji, rozdział opublikowany i zintegrowany z książką.

## 1. Ponowne sprawdzenie matematyczne

1. **Definicja i konwencja znaku.** Weryfikacja macierzy `S_{m,n}(f,g)` operatora `(u,v)↦uf+vg` w bazach rosnących potęg; standardowa wypadkowa `R_{m,n}=(-1)^{mn}det S_{m,n}`. Przypadki liniowe i z formalnymi zerowymi współczynnikami wiodącymi sprawdzone odrębnie.
2. **Wspólny czynnik.** Dla niezerowych `f,g` nad ciałem i rzeczywistych dodatnich stopni dowód równoważności `R(f,g)=0`, `deg gcd(f,g)>0` i istnienia wspólnego pierwiastka w domknięciu algebraicznym: bezlukowe przejście przez jądro macierzy i lemat Euklidesa.
3. **Wzór przez pierwiastki.** Niezależna kontrola faktora `a_m^n`, zamiany bloków, wyznacznika zmiany bazy, trójkątnej postaci mnożenia przez `X` w bazie dzielników `P_k` oraz poprawności w obecności pierwiastków wielokrotnych.
4. **Wyróżnik.** Sprawdzono znak `(-1)^{n(n-1)/2}` i zgodność z formalnym stopniem `n-1` pochodnej, także gdy pochodna ma mniejszy stopień rzeczywisty albo jest zerowa w charakterystyce dodatniej.
5. **Przykłady i pierścienie.** Sprawdzono eliminację `X²-s, X-t` i specjalizację do dowolnego ciała; parę `(X-1)², X+2`; kontrprzykład w `Z/4Z` z odwracalnym `1+2X`.

Żaden z tych punktów nie wymagał zmiany tekstu względem audytu I. Testy skończonych przypadków uzupełniają, ale nie zastępują przytoczonych dowodów.

## 2. Kontrola integralności

- Źródło: **255 wierszy**, SHA-256 `06e4275e10bb916164f51005c4405f69551d502a6a2bf235308b08634d3a5e79` — zgodne bajtowo z audytem I.
- Git blob źródła: `40f339a13b5890418869a12ef27881d29233ffe7`; porównano bajtowo z wersją opublikowaną.
- **10/10 etykiet unikatowych**, **5/5 odsyłaczy rozstrzygniętych wewnętrznie**; **4 dowody**, **3 przykłady**; zagnieżdżenia `begin/end` poprawne.
- Niezmienione wcześniejsze rozdziały AA-01–AA-32; do pliku książki dołączono dokładnie jeden `\input` AA-33.

## 3. Niezależna walidacja

- Zestaw I powtórzony: **56/56 PASS** (`test_abstract_algebra_ch33.py`).
- Zestaw II nowy: **44/44 PASS** (`test_abstract_algebra_ch33_independent.py`). Jest odrębną implementacją budowy macierzy z kolumn współczynników; wykorzystuje również własny algorytm Euklidesa modulo liczby pierwsze i niezależne porównania symboliczne, krotności, pochodne, specjalizację, prawo mnożenia wypadkowej i stopnie formalne.
- Oba zestawy uruchomiono łącznie jako pakiety `tools.tests...` w układzie zgodnym z repozytorium: **100/100 PASS**.
- Pierwotnie w dodatkowym zestawie testów był błąd wywołania API `sympy.det`; poprawiono wyłącznie test przed końcowym pomiarem. Nie była to wada tekstu matematycznego.

## 4. Kompilacja i kontrola wizualna

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error` na pomocniczej kompilacji pojedynczego rozdziału: **PASS**.
- **4 strony**, brak błędów, ostrzeżeń LaTeX, niezdefiniowanych etykiet, `Overfull` i `Underfull`.
- Wszystkie 4 strony wyrenderowano i sprawdzono wizualnie; bez obciętych wzorów i kolizji.
- **Granica:** w tej iteracji nie wykonano lokalnej kompilacji całego tomu AA-01–AA-33.

## 5. Publikacja i stan CI

- Opublikowano `chapters/pl/abstract_algebra/33-wypadkowa-wielomianow-i-macierz-sylvestera.tex` — blob `40f339a13b5890418869a12ef27881d29233ffe7`.
- Opublikowano testy `tools/tests/test_abstract_algebra_ch33.py` (blob `b63a55734f3a09c5772d96b694b9450a9691b017`) i `tools/tests/test_abstract_algebra_ch33_independent.py` (blob `c92a516259049fb1ed5025fa257bc268bc46c9f2`). Zgodność bajtową obu testów potwierdzono ponownym odczytem GitHub.
- `books/pl/abstract_algebra.tex` zawiera `\input` AA-33; `catalog/books.json` zawiera **33 rozdziały** w odpowiedniej kolejności.
- Workflow `.github/workflows/abstract-algebra-chapter.yml` ma wyzwalacze dla nowych testów, krok z **100 testami AA-33** oraz krok `Compile AA-01 to AA-33 book with latexmk`.
- Rzeczywisty przebieg [GitHub Actions #45023153837](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023153837) był **w toku w chwili weryfikacji**: walidacja zależności zakończyła się powodzeniem, testy narzędzi trwały, a testy AA-33 i pełna kompilacja książki oczekiwały na wykonanie. **Nie przedstawiamy pełnego CI jako zaliczonego**.

## 6. Następny etap

**AA-34 — „Rezolwenta sześcienna i grupy Galois stopnia czwartego”, audyt I.**
