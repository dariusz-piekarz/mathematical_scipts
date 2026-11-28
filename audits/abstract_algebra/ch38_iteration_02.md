# AA-38 — Lemat normalizacyjny Noether: audyt II (stabilizacyjny)

**Data:** 2026-11-22  
**Projekt:** Biblioteka matematyczna — Algebra abstrakcyjna  
**Status matematyczny:** **AA-38 stabilny po audycie II, 0 zmian źródła**.  
**Status publikacji:** rozdział, dwa zestawy testów, książka, katalog i workflow zostały opublikowane i ponownie odczytane z GitHub; pełny wynik CI był jeszcze w toku podczas tej aktualizacji.

## Niezależna kontrola matematyczna

1. **Moniczność i brak założenia nieskończoności ciała.** Dla stopnia całkowitego `d` i bazy `M>d+1` wagi `w(α)=α_n+∑_{i<n} α_i M^i` jednoznacznie rozróżniają jednomiany z nośnika relacji. Po podstawieniu `X_i=Y_i+Y_n^{M^i}` wyraz o największej wadze ma stały współczynnik różny od zera; ponieważ relacja jest niestała, wykładnik jest dodatni. Tożsamości obowiązują w dowolnej charakterystyce.
2. **Indukcja po liczbie generatorów.** Początek `n=0`, przypadek wolnych zmiennych, relacja przy `n=1`, indukcyjne przejście od `A=B[a_n]` przy `a_n` całkowitym nad `B` do skończoności `A` nad pierścieniem wielomianów `C`. Brak potrzeby zakładania, że `A` jest zredukowana albo jest dziedziną całkowitości.
3. **Wniosek o stopniu transcendencji.** Przy założeniu, że `A` jest dziedziną, macierz dołączona i skończoność modułowa dają równanie moniczne dla każdego `a∈A`; po przejściu do ciał ułamków parametry normalizujące są bazą transcendencji, więc `r=trdeg_K Frac(A)`.
4. **Przykład w `F₂`.** Sprawdzono równość `V⁸+V⁵+UV+U²+V=0`, moniczność i jednoznaczność klasy reszty stopnia `<8`; parametr `u` jest transcendentalny nad `F₂` przez porównanie stopni w `V`.
5. **Kontrprzykłady.** W `K[t]⊂K(t)` dowód oparty na `D` i `h=1+tD` poprawnie pokazuje zarówno brak skończoności modułowej, jak i brak skończonego generowania `K(t)` jako `K`-algebry. Zweryfikowano przykłady z hiperbolą, parabolą półsześcienną, nilpotentami i dzielnikami zera.

## Testy

- **94/94 PASS**: testy z audytu I, przystosowane do ścieżek repozytorium; zachowano wszystkie przypadki symboliczne, modularne i strukturalne.
- **115/115 PASS**: nowy zestaw niezależny, w tym 50 przypadków moniczności po podstawieniu w `GF(p)`, 21 przypadków redukcji wyższych potęg modułem monicznej relacji nad `GF(2)(u)`, 24 niezależne przypadki przeszkody mianownikowej `gcd(D,1+tD)=1`, a także kontrole strukturalne i przykładów.
- **209/209 PASS**: łącznie, w dwóch uruchomieniach, w tym w katalogach odpowiadających `tools/tests` oraz `chapters/pl/abstract_algebra`.
- W pierwszym uruchomieniu nowego zestawu wystąpiło 24 niepowodzeń technicznych z powodu mnożenia obiektu `Poly(...,GF(p))` przez symbol reprezentowany w `ZZ`; poprawiono **wyłącznie test**, zgodnie z domeną `GF(p)`. Ostateczne pełne uruchomienie bez błędów.

Testy skończenie wielu przypadków nie zastępują dowodu ogólnego; oceniono także niezależnie cały tekst argumentów matematycznych.

## LaTeX, skład i odsyłacze

- **5 stron A4**, `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error`: **PASS**.
- W logu: brak `LaTeX Warning`, `Overfull/Underfull \hbox`, niezdefiniowanych poleceń oraz nierozwiązanych odsyłaczy.
- Wizualnie zweryfikowano wszystkie strony (montaż pięciu stron).
- **9 unikatowych etykiet**: 8 historycznych i 1 z audytu I. **3 historyczne dowody** zachowane.
- Jedyny odsyłacz zewnętrzny `aa:tw:transcendence-degree` zweryfikowano w opublikowanym AA-37 na gałęzi `biblioteka-matematyczna-iteracja-6`.
- Kompilacja rozdziału używa lokalnej deklaracji etykiety zewnętrznej; wynik pełnego tomu zależy osobno od GitHub Actions.

## Kryterium stabilizacji

Po niezależnej kontroli **nie trzeba było zmieniać źródła**. Plik jest identyczny bajtowo z wynikiem audytu I; SHA-256 obu plików:

`f494054979b230729e307a82c9400ae2b9ebd796da17681fd51ebe23ea6a78ff`

**Wniosek:** `AA-38 STABILNY po audycie II`, kwalifikuje się do włączenia do książki oraz regresji CI. Osobno raportować wynik uruchomienia zdalnego CI.

## Integracja z GitHub

- Gałąź: `biblioteka-matematyczna-iteracja-6`, repozytorium `dariusz-piekarz/mathematical_scipts`.
- Rozdział: `chapters/pl/abstract_algebra/38-lemat-normalizacyjny-noether.tex`. Git blob: `2edea1072ab0b052f492e88f9dd508ba5c938d3a`; zgodność z lokalnym plikiem zweryfikowana.
- Testy: `tools/tests/test_abstract_algebra_ch38.py` (`38468a259f54fd2c13f550011cf57cb89ef926a6`) oraz `tools/tests/test_abstract_algebra_ch38_independent.py` (`17f786e775754214b265766d2f2321052ecae260`).
- Książka `books/pl/abstract_algebra.tex` zawiera `\input` rozdziału 38. `catalog/books.json`: 38 rozdziałów, AA-38 na końcu. Workflow `.github/workflows/abstract-algebra-chapter.yml` uruchamia oba zestawy testów AA-38 i kompilację 38 rozdziałów. Wszystkie sześć plików ponownie odczytano i zweryfikowano.
- [GitHub Actions — walidacja AA-01–AA-38](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45054158202). **W chwili tego zapisu przebieg pozostawał `in_progress`**; nie należy interpretować opublikowania workflow jako potwierdzenia wykonania kompilacji całej książki.
