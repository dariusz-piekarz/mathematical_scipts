# Algebra abstrakcyjna — AA-28, audyt II (stabilizacyjny)

**Data:** 2026-11-22  
**Rozdział:** „Ciała cyklotomiczne i wielomiany cyklotomiczne”  
**Źródło:** `AA-28-audyt-II-zrodlo.tex` (327 wierszy)  
**Status:** **stabilny — audyt II bez zmian źródła; opublikowany w GitHub**.

## 1. Ponowny niezależny audyt matematyczny

- Istnienie pierwotnego `n`-tego pierwiastka z jedynki w `\overline{\mathbb Q}`: rozdzielczość `X^n-1` oraz cykliczność skończonych podgrup `F^\times`; przypadek `n=1` uwzględniony.
- Niezależność `\Phi_n` od wyboru `\zeta_n` oraz rozkład `X^n-1=\prod_{d\mid n}\Phi_d` przy jednoznacznym podziale według rzędów.
- Całkowitość współczynników przez dzielenie wielomianów przez moniczny czynnik w `\mathbb Z[X]`, indukcję i jednoznaczność dzielenia nad ciałem.
- Lemat o pierwotnym pierwiastku podniesionym do potęgi `\ell`, gdzie `\ell` jest pierwsza i `\ell\nmid n`: podzielność `f\mid g(X^\ell)`, lemat Gaussa, redukcja modulo `\ell`, czynnik nierozkładalny `h` oraz niemożność `h^2\mid X^n-1` w `\mathbb F_\ell[X]`.
- Nierozkładalność `\Phi_n` nad `\mathbb Q` na podstawie kolejnych potęg pierwszych; każdy etap zachowuje rząd pierwiastka i jego wielomian minimalny.
- Grupa Galois `\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)\simeq(\mathbb Z/n\mathbb Z)^\times`: iniektywność, surjektywność, zgodność mnożenia i szczególny przypadek `n=1`.
- Przykłady: `\Phi_5`, ciało elementów stałych podgrupy rzędu `2`, `\Phi_8` i grupa Kleina, redukcja `\Phi_3\bmod 3` z podwójnym pierwiastkiem, rozróżnienie nierozkładalności od rozdzielczości w dodatniej charakterystyce.

**Nowe usterki:** 0. **Zmiany matematyczne, językowe i techniczne podczas audytu II:** 0.

## 2. Testy niezależne i regresyjne

- Powtórzone testy audytu I, wersja przenośna do `tools/tests`: **22/22 PASS**.
- Nowy, niezależnie napisany zestaw testów II: **22/22 PASS**.
- Zakres: stopnie, moniczność, współczynniki całkowite, tożsamość iloczynowa, nierozkładalność, działanie jednostek modulo `n`, tożsamość `\Phi_n(X^\ell)\equiv0\bmod\Phi_n(X)` przy `\gcd(\ell,n)=1`, rozdzielczość i nierozdzielczość po redukcji, konkretne przykłady `n=5,8`, a także struktura etykiet i odsyłaczy.
- Środowisko testowe: Python, SymPy 1.14.0; oba zestawy uruchomione lokalnie po adaptacji ścieżek do repozytorium.

## 3. Kompilacja i kontrola wizualna

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error AA-28-audyt-II-kompilacja.tex`: **PASS**, dwukrotne przebiegi LaTeX.
- PDF pomocniczy: **5 stron**, z czego strona 1 zawiera etykiety zastępcze dwóch zewnętrznych rozdziałów; właściwy AA-28 zajmuje strony 2–5.
- Brak `LaTeX Warning`, `Overfull`, `Underfull` i niezdefiniowanych odsyłaczy.
- Wyrenderowano wszystkie strony i zweryfikowano czytelność rysunku `aa:fig:cyclotomic-five`, tekstu oraz podpisów.
- **10 unikatowych etykiet**, **6 odsyłaczy**; dwa zewnętrzne cele `aa:ch:fields-fractions`, `aa:ch:kummer` zweryfikowane w aktualnych rozdziałach AA-19 i AA-26.

## 4. Publikacja

- Opublikowano `chapters/pl/abstract_algebra/28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex` na gałęzi `biblioteka-matematyczna-iteracja-6`.
- Plik `books/pl/abstract_algebra.tex` zawiera `\input` AA-28, a `catalog/books.json` rejestruje 28 rozdziałów algebry abstrakcyjnej.
- Dodano `tools/tests/test_abstract_algebra_ch28.py` i `tools/tests/test_abstract_algebra_ch28_independent.py` (razem 44 testy).
- Zaktualizowano `.github/workflows/abstract-algebra-chapter.yml`, rozszerzając zakres na AA-01–AA-28.
- Zdalny Git blob rozdziału jest bajtowo zgodny z audytowanym źródłem.

**SHA-256 źródła:** `33318101c1a2f11920cc63757cd4572a7f18b8cba07855d705a0a17fcfe78d85`  
**Git blob SHA-1 źródła:** `2e24a69608aeab7856acf40f882480a97eb455bc`.

**Ograniczenia:** Lokalna kompilacja pomocnicza nie zastępuje pełnej kompilacji książki AA-01–AA-28. Zdalny wynik GitHub Actions CI nie został potwierdzony jako PASS.

## 5. Wniosek i następny etap

**AA-28: STABILNY po audycie II.** Pierwszy audyt wprowadził pięć korekt redakcyjnych i notacyjnych; drugi nie wymagał żadnej zmiany. Kolejny rozdział do audytu: **AA-29 — struktura ciał skończonych, audyt I**.
