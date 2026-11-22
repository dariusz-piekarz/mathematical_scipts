# AA-39 — audyt II (stabilizacyjny)

**Data:** 2026-11-22  
**Rozdział:** „Wymiar Krulla i łańcuchy ideałów pierwszych”  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; gałąź `biblioteka-matematyczna-iteracja-6`.  
**Ocena matematyczna:** stabilny po audycie II; nie znaleziono potrzeby dalszych zmian źródła.

## Powtórny niezależny audyt dowodów

1. **Wymiar płaszczyzny afinicznej:** zweryfikowano `aa:lem:krull-plane-dimension`, w tym rozkład elementów w pierścieniu z jednoznacznością rozkładu `K[U,V]`, względną pierwszość dwóch niestowarzyszonych nierozkładalnych wielomianów nad `K(U)[V]` i `K(V)[U]`, eliminację do niezerowych `h(U)` i `k(V)`, skończony wymiar `K[U,V]/(f,g)` nad `K` i klasyfikację niezerowych ideałów pierwszych jako maksymalnych albo głównych nierozkładalnych. Dolne ograniczenie jest otrzymywane z łańcucha `(0) ⊊ (U) ⊊ (U,V)`; nie stosuje się przyszłego twierdzenia dla `n≥3`.
2. **Definicje:** długość łańcucha, wysokość ideału, przypadek pierścienia niezerowego i kryterium wymiaru zero `aa:cor:krull-dim-zero` są spójne.
3. **Zmiana pierścienia:** dowody korespondencji ideałów pierwszych dla ilorazu i lokalizacji, nierówności wymiaru, niezmienniczości po redukcji nilradykału i równości `ht(p)=dim A_p` zostały sprawdzone wraz z warunkami dotyczącymi zbiorów multiplikatywnych.
4. **Przykłady:** zweryfikowano pierścienie `Z`, `Z/(6)`, `K[T]/(T^2)`, iloczyn `K[T]×K[U,V]` z ideałami maksymalnymi różnych wysokości, krzyżujące się proste `K[X,Y]/(XY)`, pierścień wielomianów w przeliczalnie wielu zmiennych oraz obie lokalizacje `Z`.
5. **Ograniczenia zakresu:** twierdzenie `dim K[X_1,...,X_n]=n` dla dowolnego `n≥3` nadal pozostaje odłożone do dalszej części materiału. Nie przypisano mu fałszywego odsyłacza ani statusu udowodnionego.

## Testy niezależne

- **136/136 PASS** — pełne testy regresyjne z audytu I.
- **89/89 PASS** — nowy plik `test_abstract_algebra_ch39_independent.py`, niezależnie weryfikujący strukturę źródła, eliminację przez wypadkowe w charakterystykach `0,2,3,5,7`, przykłady łańcuchów w `K[U,V]`, skończone algebry lokalne z nilpotentami i iloczyny ciał.
- **225/225 PASS** — oba zestawy uruchomione razem w układzie katalogów repozytorium `tools/tests/` i `chapters/pl/abstract_algebra/`.
- Testy skończonych instancji są **kontrolami regresyjnymi**, a nie formalnym dowodem twierdzeń dla wszystkich ciał i pierścieni.
- Pierwsza wersja testu niezależnego sprawdzała dosłowną obecność notacji `K(V)[U]` w źródle, chociaż źródło poprawnie stosuje zdanie „Zamieniając role U i V”. Zmieniono wyłącznie błędne kryterium testowe, nie źródło rozdziału.

## LaTeX i źródła

- **Źródło:** dokładnie niezmienione względem audytu I. SHA-256: `2d0f5684877a8acc8807d51527957108f7f122045ccf5ea09198856ca36a6aea`.
- **Etykiety:** 18/18 historycznych zachowanych; 20/20 unikatowych łącznie.
- **Dowody:** 10; **przykłady:** 7; rysunek krzyżujących się prostych zachowany.
- **Odsyłacze zewnętrzne:** 2/2 do rozdziałów AA-09 i AA-12 potwierdzone bezpośrednio na GitHub.
- **Kompilacja:** `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error` — PASS, A4, **6 stron**. Brak ostrzeżeń LaTeX, przepełnień i nierozwiązanych odsyłaczy w pomocniczej kompilacji. Wrapper deklaruje etykiety zastępcze dla dwóch odsyłaczy do rozdziałów wcześniejszych.
- **PDF:** sześć stron wyrenderowano i obejrzano. Brak uciętych formuł i kolizji elementów.

## Publikacja i CI

Źródło, testy, raport, książka, katalog i workflow CI publikuje się na wskazanej gałęzi. Wydanie AA-39 opublikowano na gałęzi `biblioteka-matematyczna-iteracja-6`; książka i katalog obejmują obecnie 39 rozdziałów. Zdalna walidacja: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45061986098. W chwili publikacji raportu workflow trwa; sukces testów zdalnych i pełnej kompilacji książki wymaga osobnego potwierdzenia.
