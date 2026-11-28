# Algebra abstrakcyjna — AA-32, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026.  
**Rozdział:** „Wyróżnik wielomianu i grupa Galois”.  
**Gałąź publikacji:** `biblioteka-matematyczna-iteracja-6`, repozytorium `dariusz-piekarz/mathematical_scipts`.  
**Decyzja:** **AA-32 STABILNY po audycie II (0 zmian źródła).**

## 1. Powtórny audyt matematyczny

Przeczytano całość aktualnej wersji po audycie I, bez korzystania z wcześniejszego raportu jako dowodu poprawności. Niezależnie zweryfikowano:

1. Przynależność wyróżnika do ciała współczynników z podstawowego twierdzenia o wielomianach symetrycznych i wzorów Viète'a; przypadek stopnia 1 i charakterystyki 2.
2. Kryterium `disc(f) ≠ 0` równoważne rozdzielczości dla każdego monicznego wielomianu dodatniego stopnia.
3. Zależność znaku permutacji i iloczynu Vandermonde’a, z wyraźnym wykorzystaniem `char K ≠ 2` w twierdzeniu `Gal(f) ⊆ A_n` wtedy i tylko wtedy, gdy `disc(f)` jest kwadratem w `K`.
4. Tożsamość `disc(X^3+pX+q)=-4p^3-27q^2`, w tym w charakterystykach 2 i 3: wszystkie przejścia są całkowitoliczbowe, bez dzielenia przez 2 lub 3.
5. Klasyfikację grup Galois nierozkładalnych, rozdzielczych sześcianów w charakterystyce różnej od 2; przykłady `X^3-2` (grupa `S_3`, wyróżnik `-108`) i `X^3-3X+1` (grupa `A_3`, wyróżnik `81`).
6. Pełny kontrprzykład nad `F_2(t)`: `h(X)=X^3+X+t` jest nierozkładalny (biegun w nieskończoności), rozdzielczy (`h'(X)=(X+1)^2`, `h(1)=t≠0`), a nad `K(α)=F_2(α)` czynnik kwadratowy jest nierozkładalny na mocy równania Artina–Schreiera `z^2+z=1+α^{-2}` i obliczenia części głównej w punkcie `α=0`. Stąd grupa Galois `S_3`, chociaż `disc(h)=t^2` jest kwadratem.
7. Poprawione w audycie I zapisy `\\ne` oraz ich poprawną składnię w LaTeX.

**Wynik:** brak luk, błędów i niedopowiedzeń wymagających kolejnej zmiany treści. Nie zmieniono żadnego wiersza źródła w audycie II.

## 2. Testy algebraiczne

- Ponowne uruchomienie zestawu z audytu I: **26/26 PASS**.
- Nowy niezależny zestaw: **29/29 PASS**; obejmuje wielomian Vandermonde’a pod wszystkimi permutacjami czterech indeksów, wyróżniki symboliczne i w małych charakterystykach, zgodność z wypadkową, działania na wielomianach nad ciałami skończonymi, faktoryzację sześcianu nad `F_2(α)` oraz skończone wyszukiwanie ewentualnych rozwiązań równań wymiernych.
- Oba zestawy przygotowane z odczytem pliku z `chapters/pl/abstract_algebra/32-wyroznik-i-grupa-galois.tex`, uruchomione w symulacji układu katalogów GitHub przez `python -m unittest ...`: **55/55 PASS**.
- Ograniczone wyliczanie przykładów nie zastępuje dowodu nad nieskończonym ciałem `F_2(t)`; niezależny audyt matematyczny obejmował argument dla wszystkich funkcji wymiernych.

## 3. LaTeX i odsyłacze

- Oryginalne **9 etykiet pozostaje unikatowych**; 5 odsyłaczy poprawnych, w tym 3 zewnętrzne do etykiet `aa:tw:fundamental-symmetric`, `aa:tw:vieta-general` w AA-31 i `aa:tw:orbita-stabilizator` w AA-03.
- Kompilacja pomocnicza `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS, 4 strony**, bez ostrzeżeń LaTeX, przepełnień oraz nierozstrzygniętych odsyłaczy. Wszystkie strony wyrenderowano i sprawdzono wizualnie.
- **Ograniczenie:** kompilacja pomocnicza (3 stubs zewnętrznych etykiet) nie jest pełną kompilacją książki 32-rozdziałowej.

## 4. Integralność publikacji

- SHA-256 poprawionego źródła, identyczny w audytach I i II: `0603f1b8d344c73785cc8ba163fb36e617daba871630e812880a6a3dbecca80a`.
- Git blob SHA źródła `f8c525aff1093478dcd8b1083387a42a37078086`.
- Opublikowano źródło i dwa zestawy testów, zweryfikowano dokładną zgodność bajtową za pomocą Git blob SHA (wszystkie 3 pliki).
- Zaktualizowano `books/pl/abstract_algebra.tex` do AA-32, `catalog/books.json` do 32 rozdziałów i `.github/workflows/abstract-algebra-chapter.yml` o testy AA-32 i kompilację AA-01–AA-32.
- Raport zapisano także w Bibliotece matematycznej.

## 5. Status GitHub Actions

Po aktualizacji workflow widoczny był starszy nieudany przebieg [45022125583](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022125583): zatrzymał się na walidacji zależności przed uruchomieniem testów AA-32. Późniejszy przebieg [45022143302](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022143302) przeszedł walidację zależności, a pozostałe zadania były nadal uruchamiane w momencie sprawdzenia.

**Nie deklaruje się sukcesu zdalnego CI bez jego końcowego wyniku.** Stabilność oznacza niezależny audyt II bez zmian oraz pomyślne lokalne testy i kompilację rozdziału.

## 6. Następny etap

**AA-33 — „Wypadkowa wielomianów i macierz Sylvestera”, audyt I.**
