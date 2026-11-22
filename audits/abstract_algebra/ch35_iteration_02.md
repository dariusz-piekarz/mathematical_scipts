# Algebra abstrakcyjna — AA-35, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026  
**Rozdział:** *Redukcja modulo liczb pierwszych i cykle Frobeniusa*  
**Wynik:** **AA-35 STABILNY po audycie II**; brak poprawek tekstu między audytami I i II.

## Źródło i integralność

- Wejście: `AA-35-audyt-I-zrodlo.tex`, 438 wierszy, SHA-256 `b55d002d23958debfe7dc2c0b4c5e37fd6492426945e872d39c4d105a1af3cbc`.
- Wyjście: `AA-35-audyt-II-zrodlo.tex`, **identyczny SHA-256**, **zero zmian**.
- GitHub: `chapters/pl/abstract_algebra/35-redukcja-modulo-p-i-cykle-frobeniusa.tex`, gałąź `biblioteka-matematyczna-iteracja-6`, blob SHA `28ea95ff258683a4ee9a89864f03b142ad6e8688`.

## Audyt matematyczny

1. **Dobra redukcja.** Potwierdzono równość `disc(f) mod p = disc(f mod p)` przez uniwersalny całkowitoliczbowy wielomian symetryczny we współczynnikach. Jest to poprawne również po spadku stopnia pochodnej i przy `f' = 0` w charakterystyce dodatniej. Kryterium `gcd(f mod p, (f mod p)')=1` zostało osobno udowodnione.
2. **Frobenius dla ciał skończonych.** Udowodniono zgodność długości orbit potęgowania `x↦x^q` z stopniami nierozkładalnych czynników. Wykorzystanie unikatowości `F_(q^d)` w domknięciu algebraicznym i twierdzenia o stopniach wieży jest poprawne.
3. **Pierścień generowany przez pierwiastki.** Sprawdzono skończoność jako modułu nad `Z` (ograniczenie potęg generatorów), całkowitość przez Cayleya–Hamiltona, równości `B∩Q=Z` i `B^G=Z`.
4. **Przechodniość działania Galois na ideałach nad p.** Zweryfikowano użycie chińskiego twierdzenia o resztach i normy `N=∏_{σ∈G}σ(b)`. Wybór elementu o zadanych resztach jest uprawniony, bo skończona rodzina różnych ideałów maksymalnych jest parami współmaksymalna. Sprzeczność `N∈q` i `N∉q` nie wymaga normalności pierścienia `B`.
5. **Podniesienie Frobeniusa.** Wielomian `P(T)=∏_{σ∈G}(T−σ(b))` ma współczynniki w `B^G=Z`. Jeśli klasa `c∈B/𝔭` jest pierwiastkiem redukcji `P`, to także `c^p`; wybrana klasa `b` wykrywająca tylko jeden ideał nad `p` wymusza `σ(𝔭)=𝔭`. Ponieważ `c` generuje multiplikatywną grupę ciała reszt, uzyskany automorfizm jest Frobeniusem na całym ciele reszt.
6. **Twierdzenie o typach cykli.** Dobra redukcja sprawia, że pierwiastki zachowują różność modulo ideał maksymalny; działanie skonstruowanego automorfizmu jest sprzężone z Frobeniusem. Twierdzenie nie wymaga nierozkładalności `f` nad `Q`.
7. **Parzystość i wyróżnik.** Sprawdzono znak `(-1)^(n-s)` i prawidłowe użycie kryterium `G⊆A_n` nad `Q`.
8. **Przykłady.** Sprawdzono rozkłady `X³-X-1` modulo `2`, `5`, `23`, `59`, ostrzeżenie o złych liczbach pierwszych oraz przykład rozkładalny `(X²−2)(X−3)`, `disc=392`, `p=5`.

## Testy

- Pierwszy zestaw, regresyjny: **192/192 PASS** (`test_abstract_algebra_ch35.py`). Obejmuje wyróżniki i dobre redukcje, faktoryzacje, orbity Frobeniusa, typy cykli, charakterystyki dodatnie oraz arytmetykę w `F_16` dla `q=4`.
- Drugi, niezależny: **82/82 PASS** (`test_abstract_algebra_ch35_independent.py`). Wykorzystuje własne dzielenie wielomianów nad `F_p`, NWD euklidesowy, faktoryzację przez przegląd monicznych dzielników i potęgowanie w pierścieniach ilorazowych; sprawdza przykłady i strukturę LaTeX.
- **Razem 274/274 PASS**, również przy wywołaniu w strukturze `tools/tests` i `chapters/pl/abstract_algebra`, równoważnej strukturze repozytorium.
- W nowym zestawie początkowo wykryto błąd samej asercji (sprawdzała rozwinięcie wyrażenia zamiast rozkładalności); poprawiono wyłącznie test, nie rozdział.
- Testy skończonej liczby przypadków **nie zastępują** dowodów ogólnych.

## LaTeX, grafika, odsyłacze

- **Kompilacja izolowana PASS**, pięć stron A4; brak ostrzeżeń, niedopasowanych pudeł i nierozwiązanych odsyłaczy.
- Zwizualizowano i obejrzano wszystkie pięć stron. Nie stwierdzono kolizji tekstu, uciętych wzorów ani problemów z formatowaniem.
- **12/12 unikatowych etykiet**; 14 użyć `\ref`, w tym **5 zewnętrznych**: `aa:tw:fundamental-symmetric` (AA-31), `aa:tw:disc-separable`, `aa:tw:disc-alternating`, `aa:tw:cubic-disc` (AA-32) oraz `aa:tw:finite-frobenius-roots` (AA-29). Wszystkie cele potwierdzono odczytem GitHub.
- W kompilacji izolowanej użyto pomocniczych deklaracji istniejących etykiet zewnętrznych. To nie jest kompilacja całej książki.

## Publikacja

- Rozdział i dwa zestawy testów opublikowano na gałęzi `biblioteka-matematyczna-iteracja-6`; porównanie Git blob SHA potwierdziło zgodność bajtową z wersjami po audycie.
- Zaktualizowano `books/pl/abstract_algebra.tex` i `catalog/books.json`; w katalogu jest 35 rozdziałów.
- Zaktualizowano `.github/workflows/abstract-algebra-chapter.yml` o testy AA-35 i kompilację książki AA-01–AA-35.
- Zdalny workflow GitHub Actions: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041272951 — krok **„Run AA-35 Frobenius and reduction regression tests” zakończył się sukcesem**. Podczas ostatniego sprawdzenia kompilacja całej książki AA-01–AA-35 nadal trwała; końcowa kontrola PDF i odsyłaczy pozostawała oczekująca. Nie ogłaszamy pełnego CI jako zaliczonego bez potwierdzenia.

## Werdykt

**AA-35 STABILNY po audycie II.** Rozdział nie wymagał dalszych korekt i został włączony do książki. Następny rozdział do audytu: **AA-36 — „Wielomiany ogólne i grupy symetryczne”**.
