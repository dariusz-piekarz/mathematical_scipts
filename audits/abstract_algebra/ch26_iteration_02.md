# Algebra abstrakcyjna — AA-26, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Rozszerzenia cykliczne, pierwiastki z jedynki i teoria Kummera”.  
**Status:** ustabilizowany po drugiej, niezależnej kontroli; brak zmian matematycznych i redakcyjnych w audycie II.

## 1. Źródło i zakres

- Ponownie przeanalizowano cały 506-wierszowy plik po audycie I, bez zmian w treści.
- Tożsamy SHA-256 po obu audytach: `e4cab2ec70541603deba96490920fd9c2fae441e5adee50767fb85767cc2bf78`.
- Rozdział: 1 definicja, 1 lemat, 1 wniosek, 3 twierdzenia, 6 przykładów, 2 uwagi, 5 dowodów oraz 1 rysunek TikZ.
- Zmienione w audycie I fragmenty dotyczące założeń stopnia `p`, działania automorfizmów i przykładu nad `Q(i)` sprawdzono ponownie.

## 2. Kontrola matematyczna

1. Skończona podgrupa grupy multiplikatywnej ciała jest cykliczna: konstrukcja elementu o rzędzie NWW rzędów, liczba pierwiastków wielomianu `X^m-1`.
2. Dla `char(F)∤n` i `|μ_n(F)|=n` rozszerzenie `F(α)/F`, `α^n=a≠0`, jest Galois z grupą cykliczną wstrzykiwaną do `μ_n(F)`. Sprawdzono normalność, rozdzielczość i własność homomorfizmu.
3. Odwrotne twierdzenie Kummera: operator sumacyjny `P(x)=Σ ζ^{-j}σ^j(x)` jest niezerowy na mocy niezależności różnych automorfizmów; `σ(P(x))=ζP(x)`; orbitę niezerowego wektora tworzy dokładnie `n` różnych elementów, stąd stopień minimalnego wielomianu to `n`.
4. Rozszerzenia nie-Galois bez pierwiastków z jedynki (`Q(∛2)/Q`), nierozdzielczość w charakterystyce `p` i niepełny stopień przy `n=4`, `a=4` nad `Q(i)` rozpatrzono z podanymi założeniami.
5. Klasyfikacja dla liczby pierwszej `p`: `F(√[p]a)=F(√[p]b)` wtedy i tylko wtedy, gdy `b=c^p a^j`, `1≤j≤p−1`, przy `char(F)≠p` i `μ_p⊂F`. Sprawdzono oba kierunki, elementy stałe Galois i niezerowość generatorów.
6. Opis jednowymiarowych podprzestrzeni `F×/(F×)^p` oraz przykłady trzech pól kwadratowych i dwóch klas `2,4` dających to samo rozszerzenie — zgodne z klasyfikacją.

## 3. Regresja i LaTeX

- **26/26 niezależnych testów PASS**; uruchomiono także w strukturze katalogów `tools/tests` i `chapters/pl/abstract_algebra`, z której korzysta CI.
- Kontrole algebraiczne obejmowały pełne `343×343` par mnożenia w `F_7[α]/(α³−2)`, rząd automorfizmu, ciało elementów stałych, operator własny z odwrotnego twierdzenia Kummera, sześciany i wielomiany minimalne; dodatkowo `Q(i)`, `Q(ω)`, klasy kwadratowe i charakterystyki 2,3,5,7.
- Pierwsza wersja **testu** zawierała niedopasowany wzorzec tekstowy; zmieniono wyłącznie test, nie źródło rozdziału.
- **12/12 unikatowych etykiet**, **6 odwołań**: jedynym zewnętrznym celem jest `aa:lem:dedekind-independent`, obecny w AA-25 na aktualnej gałęzi.
- Izolowana kompilacja `latexmk -pdf`: **PASS**; 7 stron (pierwsza wyłącznie na etykietę pomocniczą, właściwy rozdział zajmuje 6 stron). `LaTeX Warning`, `Overfull/Underfull` oraz `Undefined control sequence`: **0**.
- Render wszystkich 7 stron skontrolowany wizualnie; strzałki i podpis w rysunku grupy Galois nie nachodzą na siebie.

## 4. Publikacja i ograniczenia

- Publikacja na dotychczasowej gałęzi `biblioteka-matematyczna-iteracja-6` w `dariusz-piekarz/mathematical_scipts`.
- Nowy plik: `chapters/pl/abstract_algebra/26-rozszerzenia-cykliczne-i-teoria-kummera.tex`.
- Książka `books/pl/abstract_algebra.tex` i katalog `catalog/books.json` zawierają pozycję AA-26 (łącznie 26 rozdziałów).
- Testy z audytu II przygotowano do rejestrowania w `tools/tests/test_abstract_algebra_ch26_independent.py`.
- **Nie przeprowadzono pełnej kompilacji AA-01–AA-26 ani nie potwierdzono sukcesu zdalnego GitHub Actions**. Izolowany podgląd nie jest równoważny pełnemu buildowi.

**Wniosek:** AA-26 spełnia kryterium stabilizacji: drugi audyt przeprowadzony na kompletnym źródle nie wykazał żadnej usterki wymagającej poprawki. Następny: AA-27, audyt I.

## 5. Integralność publikacji

Podczas końcowego porównania źródła z kopią na GitHub zauważono techniczny błąd przeniesienia: w pojedynczym miejscu kopia utraciła zamykający znak `$` przy `$X^2-2=0$`. Błąd powstał **podczas przesyłania treści, nie w źródle poddanym audytowi**. Kopię na GitHub skorygowano na podstawie pełnego lokalnego pliku i sprawdzono jej SHA Git: `5bee95fdfedeaaf4fc697dce636e5d82afcd249b`, identyczne z wynikiem `git hash-object` lokalnego źródła po audycie. Zmiany w matematycznej treści rozdziału podczas audytu II: nadal **0**.