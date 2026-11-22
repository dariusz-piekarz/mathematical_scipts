# Algebra abstrakcyjna — AA-34, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Rezolwenta sześcienna i grupy Galois wielomianów czwartego stopnia”.  
**Wersja wejściowa:** `/Biblioteka matematyczna/iteracje/AA-34-audyt-I-zrodlo.tex`.  
**Wynik:** **AA-34 STABILNY po audycie II** — zero zmian w treści źródłowej, źródło opublikowane na GitHub.

## Matematyka: druga niezależna kontrola

1. **Działanie na podziałach.** Niezależnie wyliczono wszystkie 24 permutacje zbioru czteroelementowego i ich działanie na trzech podziałach na pary. Jądro homomorfizmu `rho: S_4 -> S_3` jest równe `V_4`, a obraz jest całym `S_3`.
2. **Pełna klasyfikacja grup przechodnich.** Algorytm wyznaczył wszystkie 30 podgrup `S_4`, z czego 9 jest przechodnich na czterech punktach. Dla każdej z dziewięciu sprawdzono parę `(rząd grupy, rząd obrazu rho)`; możliwe są wyłącznie `(4,1), (4,2), (8,2), (12,3), (24,6)`. Ich obrazy działają na trzech podziałach z orbitami odpowiednio `1+1+1`, `1+2`, `1+2`, `3`, `3`. Potwierdza to poprawność wniosku o typach rozkładu rezolwenty.
3. **Wzór rezolwenty.** Sprawdzono symbolicznie, że dla `f=X^4+aX^3+bX^2+cX+d` zachodzi `r_f(Y)=Y^3-bY^2+(ac-4d)Y-(a^2d+c^2-4bd)`. Bezpośrednie rozwinięcie przy czterech niezależnych symbolicznych pierwiastkach potwierdza formułę i wszystkie tożsamości różnic pierwiastków.
4. **Równość wyróżników.** Niezależne porównanie `disc_X(f)` i `disc_Y(r_f)` dla czterech ogólnych parametrów daje wielomian zerowy o współczynnikach całkowitych. Zbadano również specjalizacje nad `F_2` (16 zestawów współczynników) i `F_3` (81 zestawów) oraz przypadki pierwiastków wielokrotnych.
5. **Przykłady.** Niezależnie potwierdzono typy Galois: `C_4` dla `Phi_5(X)`, `V_4` dla `X^4-10X^2+1`, `D_4` dla `X^4-2` i `S_4` dla `X^4-X-1`. Dodatkowo przetestowano przykład **`A_4`**: `X^4-3X^3+3X^2+2X+1` (nierozkładalny, rezolwenta `Y^3-3Y^2-10Y-1` nierozkładalna, wyróżnik `4225=65^2`, grupa Galois rzędu 12). Nie jest konieczne dopisywanie go do rozdziału w tym audycie.
6. **Dowody grupowe.** Ponownie sprawdzono przejście `G/(G∩V_4) ≅ rho(G)`, klasyfikację przechodnich podgrup `S_4`, wykorzystanie kryterium wyróżnika przy `char K != 2` i poprawność uwagi o `char K = 2`.

## Testy i struktura

- Ponownie uruchomione testy audytu I: **82/82 PASS**.
- Nowe testy niezależne audytu II: **24/24 PASS**; obejmują pełną enumerację podgrup, tożsamości symboliczne, charakterystyki dodatnie i dodatkowy przykład `A_4`.
- Testy w układzie katalogów repozytorium (`python -m unittest tools.tests.test_abstract_algebra_ch34 tools.tests.test_abstract_algebra_ch34_independent -v`): **106/106 PASS**.
- Etykiety: **14/14 unikatowych**, wszystkie 11 pierwotnych zachowane.
- **14 wystąpień `\\ref`**. Pięć zewnętrznych celów jest obecnych w opublikowanych rozdziałach AA-28, AA-31, AA-32 i AA-33; wszystkie wewnętrzne odsyłacze pozostają rozwiązywalne.
- SHA-256 źródła po audycie I i II, identyczny: `4657ca96aa6dea11541c47441e045ed66383d5dc50cea40dd475b7be37369ecf`.
- Git blob SHA źródła opublikowanego na GitHub: `a7202801c7e5ae9d4ad202a5deceabd631512a85` (zgodność bajtowa zweryfikowana przez ponowny odczyt). Testy także zweryfikowano bajtowo.

## Kompilacja i wygląd

- Świeża kompilacja pomocnicza `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS**, **5 stron A4**.
- Brak ostrzeżeń kompilatora, nierozwiązanych odsyłaczy i komunikatów `Overfull`/`Underfull`.
- PDF wyrenderowano do pięciu obrazów i przejrzano; rysunek trzech podziałów `P_1,P_2,P_3`, wzory i tekst są czytelne, bez kolizji lub ucięcia.
- Kompilacja pomocnicza podaje wcześniejsze pięć etykiet zewnętrznych w nagłówku testowym; **nie należy jej utożsamiać z pełną kompilacją książki**.

## Publikacja i zakres potwierdzenia

Repozytorium: `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.

Opublikowano i sprawdzono przez ponowny odczyt:

- `chapters/pl/abstract_algebra/34-rezolwenta-szescienna-i-grupy-galois-stopnia-czwartego.tex`;
- `tools/tests/test_abstract_algebra_ch34.py` oraz `tools/tests/test_abstract_algebra_ch34_independent.py`;
- `books/pl/abstract_algebra.tex` (obejmuje AA-01–AA-34);
- `catalog/books.json` (34 rozdziały algebry abstrakcyjnej);
- `.github/workflows/abstract-algebra-chapter.yml` (oba zestawy testów AA-34 i kompilacja AA-01–AA-34).

W chwili ostatniego sprawdzenia przebieg GitHub Actions [45039812764](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45039812764) **trwał**, a zdalne testy AA-34 i kompilacja pełnej książki nie miały jeszcze potwierdzonego wyniku. Lokalna walidacja i publikacja źródeł są potwierdzone, sukces całego zdalnego CI — **nie**.

## Decyzja

**AA-34 STABILNY po audycie II.** Rozdział zintegrowano z katalogiem oraz plikiem głównym książki. **Następny etap:** AA-35 („Redukcja modulo p i cykle Frobeniusa”), audyt I. Należy kontrolować wynik GitHub Actions dla AA-34, nie przedstawiając procesu w toku jako sukcesu.
