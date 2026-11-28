# Algebra liniowa — rozdział 17, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/17-postac-jordana.tex`  
**Blob rozdziału po poprawkach:** `a7bfa2bbefe1e2eb3c8f3a27d4e0035d77b35a32`.

## Kontrola matematyczna

1. **Nilpotentność.** Dla nilpotentnego `N` wykazano rosnącą filtrację jąder `ker N^k`. Stabilizacja jednego kroku wymusza stabilizację dalszych; na `V≠0` indeks nilpotentności nie przekracza `dim V`. Definicja i dowód uwzględniają `V=0`.
2. **Łańcuchy Jordana.** Wektor początkowy jest niezerowy, a zastosowania `N^{s-1},N^{s-2},...` do zależności liniowej dowodzą niezależności całego łańcucha. Z przyjętej kolejności wektorów wynikają jedynki na nadprzekątnej, a nie podprzekątnej.
3. **Istnienie bazy dla nilpotentnego operatora.** Szczegółowo sprawdzono indukcję na `W=im N`: łańcuchy w `W`, ich końcowe wektory niezależne modulo `N(W)`, wybór preobrazów `v_i`, dowód niezależności modulo `W`, równość `N(U)=W`, uzupełnienie `ker N∩U` do bazy `ker N` i bilans wymiarów. Wariant `W=0` jest jawny. Nie ma założenia algebraicznego domknięcia ciała.
4. **Jednoznaczność dla nilpotentnego operatora.** Dla bloku rozmiaru `s`, wymiar jądra potęgi jest `min(k,s)`. Różnicowanie `d_k` daje liczbę bloków rozmiaru co najmniej `k`; drugie różnicowanie daje dokładnie `2d_k-d_{k-1}-d_{k+1}`.
5. **Postać Jordana operatora ogólnego.** Rozkład pierwotny z rozdziału 16 oraz nilpotentność `(T-λI)|E_gen` dostarczają bazę Jordana. Przebieg dowodu poprawnie odróżnia ciała, nad którymi wielomian charakterystyczny rozszczepia się, od ogólnego przypadku. Równoważność rozszczepienia `m_T` i `χ_T` jest uzasadniona bez koła logicznego.
6. **Jednoznaczność bloków o ustalonej wartości własnej.** Na blokach o wartości własnej `μ≠λ` operator `T-λI` jest odwracalny; podano i sprawdzono skończony szereg odwrotności. Zatem w `d_{λ,k}` uczestniczą tylko bloki `λ), a różnice wymiarów wyznaczają jednoznacznie ich rozmiary.
7. **Wielomiany i diagonalizacja.** Wielomian minimalny sumy blokowej to moniczna NWW ich wielomianów minimalnych; charakterystyczny to iloczyn. Związek diagonalizowalności z blokami rozmiaru `1` wynika z kryterium rozdziału 16. W audycie I dodano jawne konwencje pustego iloczynu i NWW przy `V=0` (commit `585d97f551ba1bb5cce2c3c5c48eb8b79e6759f9`).
8. **Przykłady.** Skontrolowano bloki `N_3`, `N_2⊕N_1`, rozmiary bloków `3,3,1` odczytywane z `d=(0,3,5,7,7)` oraz przykład wymiaru `6`, w którym bloki mają rozmiary `3,1` dla `λ=1` i `2` dla `λ=3`.

## Integracja, testy i PDF

- Dodano plik rozdziału 17 do `books/pl/linear_algebra.tex`, `catalog/books.json` i listy kontrolnej workflow; README wskazuje rozdziały 01–16 jako stabilne, rozdział 17 jako „w audycie”.
- Wprowadzono `tools/test_linear_algebra_jordan.py` i krok workflow testujący bloki rozmiarów 1–4 nad `F2,F3`, losowe odwracalne podobieństwa, wymiary jąder potęg i jednoznaczność rozmiarów bloków.
- Nowy test Jordana przeszedł w [GitHub Actions 44935451202](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935451202). Cały przebieg zakończył się sukcesem, w tym ponowna kompilacja całego tomu, kontrola ostrzeżeń i odsyłaczy oraz eksport PDF rozdziału 17.
- Zweryfikowano zarówno wstępny 6-stronicowy PDF z [44935307611](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935307611), jak i ostateczny PDF z przebiegu 44935451202 po ostatniej poprawce. Wszystkie sześć stron zostało wyrenderowanych i sprawdzonych wizualnie; żadna strona nie jest pusta, nie wykryto elementów poza obszarem strony ani kolizji tekstu. Porównano oba renderowania i potwierdzono, że zmiana dotyczy jedynie jawnej konwencji dla wymiaru zero.
- Rozdział ma 21 różnych etykiet, 8 odsyłaczy i 7 zakończonych środowisk dowodu.

## Decyzja

**Audyt I wykrył jedynie brak jawnej konwencji dla przestrzeni zerowej, który poprawiono.** Z tego powodu rozdział 17 pozostaje **w audycie**, a jego stabilność wymaga co najmniej jednej niezależnej iteracji po zakończeniu aktualnego CI i kontroli ostatecznego PDF. Nie dodawać nowych twierdzeń podczas kolejnych audytów.
