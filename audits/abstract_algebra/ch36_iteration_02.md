# Algebra abstrakcyjna — AA-36, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026  
**Rozdział:** Wielomian ogólny i jego grupa Galois  
**Status:** **AA-36 STABILNY po audycie II** — bez zmian matematycznego ani redakcyjnego źródła względem audytu I. Opublikowano na gałęzi `biblioteka-matematyczna-iteracja-6`.

## Źródło i tożsamość

- Audytowana wersja: `AA-36-audyt-I-zrodlo.tex`.
- Opublikowany plik: `chapters/pl/abstract_algebra/36-wielomian-ogolny-i-grupy-symetryczne.tex`.
- **SHA-256 źródła:** `0f7ec0c3daf03e90e3689d78a9a24a6f7d6c64da439c32df3db44da85d82a964` — niezmieniony od audytu I.
- **Git blob źródła:** `4c7f5c055172ff88331978592b89d4c44d5584dc` — po publikacji porównany z plikiem lokalnym.

## Druga kontrola matematyczna

1. **Niezależność funkcji symetrycznych:** dowód korzysta z jednoznaczności reprezentacji w generatorach `e_1,...,e_n` dla dowolnego ciała, w tym w dodatniej charakterystyce. Zastosowanie podstawowego twierdzenia jest poprawne.
2. **Rozszerzenie i grupa Galois:** `L=k(x_1,...,x_n)` jest ciałem rozkładu `\prod(X-x_i)` nad `K=k(e_1,...,e_n)`. Każda permutacja zmiennych daje automorfizm `L/K`, a każdy taki automorfizm permutuje `n` różnych pierwiastków. Uzyskujemy dokładnie `S_n`.
3. **Nierozkładalność:** gdyby wielomian dzielił się na dwa czynniki dodatniego stopnia, nietrywialny właściwy zbiór pierwiastków jednego czynnika byłby niezmienniczy względem przechodniego działania `S_n`, co jest niemożliwe.
4. **Niemożliwość rozwiązania przez pierwiastniki:** dla `n>=5` osadzamy grupę `A_5` w `S_n`. Nierozwiązalność `A_5` jest już udowodniona w AA-05 (`aa:wn:a5-not-solvable`); argument nie zakłada nieudowodnionej w skrypcie prostoty `A_n` dla wszystkich `n`.
5. **Ciało funkcji wymiernych symetrycznych:** z korespondencji Galois dostajemy `L^{S_n}=K` oraz `[L:K]=n!` dla każdego ciała `k`.
6. **Podrozszerzenie stopnia 2:** dla `n=3` i `char k != 2`, `\Delta` zmienia znak przy nieparzystych permutacjach i `L^{A_3}=K(\Delta)`, przy `[K(\Delta):K]=2`.
7. **Specjalizacje:** przypadki `X^3-2`, `X^3-3X+1`, `X^4-2` są zgodne z klasyfikacją grup Galois; `X^p-t` ma jeden pierwiastek w ciele rozkładu mimo nierozkładalności i ilustruje, dlaczego niezależność formalnych współczynników jest kluczowa.

Nie wykryto błędów wymagających zmiany źródła.

## Testy

- Ponownie uruchomiony zestaw z audytu I: **84/84 PASS**.
- Niezależny zestaw audytu II: **42/42 PASS**.
- Testy wykonane wspólnie w strukturze repozytorium (`tools/tests`, `chapters/pl/abstract_algebra`): **126/126 PASS**.
- Kontrolowano tożsamości symetryczne, formuły Viète'a, permutacje, charakterystyki `2,3,5,7,11,13`, wyróżniki, osadzenia `A_5`, specjalizacje i integralność TeX.
- Testy skończonych przypadków wspierają, lecz nie zastępują dowodów ogólnych.

## Odsyłacze i LaTeX

- **12/12 etykiet unikatowych.**
- **Pięć zewnętrznych celów odsyłaczy** potwierdzonych w aktualnych plikach GitHub: `aa:wn:a5-not-solvable` (AA-05), `aa:tw:fundamental-galois` (AA-22), `aa:ch:radicals` (AA-24), `aa:tw:fundamental-symmetric` (AA-31), `aa:prz:quartic-v4` (AA-34).
- Świeża **izolowana kompilacja LaTeX PASS**, 4 strony; zero ostrzeżeń, niezdefiniowanych odsyłaczy, `Overfull` i `Underfull`. W tej pomocniczej kompilacji odsyłacze zewnętrzne mają wpisy zastępcze po rzeczywistym zweryfikowaniu istnienia etykiet.
- Wszystkie cztery strony obejrzane wizualnie; brak ucięć i nakładania tekstu.

## Publikacja i integracja

Gałąź: `biblioteka-matematyczna-iteracja-6` w `dariusz-piekarz/mathematical_scipts`.

- Rozdział: `chapters/pl/abstract_algebra/36-wielomian-ogolny-i-grupy-symetryczne.tex`.
- Regresja: `tools/tests/test_abstract_algebra_ch36.py` (**84 testy**).
- Kontrola niezależna: `tools/tests/test_abstract_algebra_ch36_independent.py` (**42 testy**).
- Plik główny: `books/pl/abstract_algebra.tex` — dodano wejście AA-36.
- Katalog: `catalog/books.json` — 36 rozdziałów.
- Workflow: `.github/workflows/abstract-algebra-chapter.yml` — oba zestawy testów i kompilacja książki AA-01–AA-36.
- Raport: `audits/abstract_algebra/ch36_iteration_02.md`.

Przeprowadzono ponowny odczyt i weryfikację wszystkich trzech plików źródło/testy (zgodność bajtowa) oraz zmian książki, katalogu i workflow.

## Zdalne GitHub Actions

- Przebieg: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45046681799
- **Status przy pierwszej kontroli:** `in_progress`. Nie przedstawiamy uruchomienia workflow jako ukończonej kompilacji całej książki, dopóki rzeczywisty przebieg nie zwróci sukcesu.

## Decyzja

**AA-36 STABILNY po audycie II.** Druga kontrola nie wymagała zmian źródła. Opublikowano go i włączono do katalogu, książki i workflow. Następny rozdział do audytu: **AA-37 — Algebraiczna niezależność i bazy transcendencji**.
