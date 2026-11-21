# Algebra liniowa — rozdział 17, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/17-postac-jordana.tex`  
**Zweryfikowany blob źródła:** `d116dc8fc69bd8c016ba1ccc536702b33f516ef1`  
**Poprzedni audyt:** `audits/linear_algebra/ch17_iteration_01.md`.

## Ponowny niezależny audyt matematyczny

1. **Nilpotentność i filtracja jąder:** z `ker N^k ⊆ ker N^(k+1)` i równości dwóch kolejnych jąder wynika ich dalsza stabilizacja; na `V ≠ 0` indeks nilpotentności nie przekracza `dim V`. Ujęto `V=0` oraz konwencję `N^0=I_V`.
2. **Łańcuchy Jordana:** dowód niezależności wektorów `v_1,...,v_s` poprzez kolejne zastosowania `N^(s-1),N^(s-2),...` jest poprawny i zgodny z nadprzekątną przyjętej definicji bloku.
3. **Indukcja dla nilpotentnego operatora:** zweryfikowano `W=im N`, działanie ograniczenia `N|_W`, niezależność wektorów końcowych `w_(i,l_i)` modulo `N(W)`, istnienie preobrazów `v_i`, niezależność modulo `W`, równości `U=W⊕span(v_i)`, `N(U)=W`, `dim(U ∩ kerN)=r` i uzupełnienie do `V` przez wektory z `kerN`. Nie stwierdzono luki, także przy `N=0`.
4. **Wzór na rozmiary bloków:** dla `d_k=dim ker(N^k)` rachunek `d_k=Σ min(k,s_i)`, liczba bloków o rozmiarze co najmniej `k` równa `d_k-d_(k-1)`, a o rozmiarze dokładnie `k` równa `2d_k-d_(k-1)-d_(k+1)` jest poprawny.
5. **Istnienie postaci Jordana:** rozkład z rozdziału 16 na uogólnione przestrzenie własne jest bezpośredni; na każdym składniku `N_λ=(T-λI)|W_λ` jest nilpotentny. Baza dla operatora nilpotentnego daje bloki `J_s(λ)`. Wykazano równoważność rozszczepienia `m_T` i `χ_T` nad `K`.
6. **Jednoznaczność:** na bloku o `μ ≠ λ` operator `T-λI` jest odwracalny przez skończony szereg geometryczny. Każde `d_(λ,k)` zależy wyłącznie od bloków `λ`, więc wzór różnicowy wyznacza ich rozmiary niezależnie od bazy.
7. **Wielomian charakterystyczny i minimalny:** prawidłowo użyto iloczynu i monicznej NWW odpowiednich czynników. Stwierdzenie o diagonalizowalności i blokach rozmiaru `1` wynika z udowodnionego w rozdziale 16 kryterium. Uwzględniono `V=0` przez puste iloczyny i NWW.
8. **Przykłady:** w niezależnym rachunku SymPy potwierdzono `(d_0,...,d_4)=(0,3,5,7,7)` dla `J_3(0)⊕J_3(0)⊕J_1(0)` oraz ciągi `(0,2,3,4)` i `(0,1,2,2)` dla wartości własnych `1` i `3` w przykładzie sześciowymiarowym. Macierze `J_3(2)` oraz `J_2(2)⊕J_1(2)` mają ten sam wielomian charakterystyczny, ale różne wielomiany minimalne.

## Wykryte i usunięte problemy

- W twierdzeniu o bazie Jordana nilpotentnego endomorfizmu zastąpiono niejednoznaczne `[N] ~ ...` jawnym `[N]_B=...` wraz z określeniem bazy `B`.
- W twierdzeniu ogólnym określono `A=[T]` w dowolnej ustalonej bazie oraz `P ∈ GL_n(K)`, `n=dim V`, w równaniu `P^(-1)AP=J`.
- W przykładzie z ciągami `d_(1,k)` i `d_(3,k)` dodano argument stabilizacji na podstawie `d_(1,3)+d_(3,3)=6=dim V` oraz bezpośredniego rozkładu na uogólnione przestrzenie własne. Uzasadnia on brak dłuższych bloków poza podanymi wymiarami.
- Jedna aktualizacja źródła: commit `fccbe60841e9958f55d64966c148f41ce56ae462`. Nie dodano żadnego nowego twierdzenia ani przykładu.

## Struktura, regresje i PDF

- Rozdział ma **21 różnych etykiet**, **8 odsyłaczy**, wszystkie do etykiet istniejących w rozdziałach 16 i 17, oraz **7 poprawnie zamkniętych dowodów**. Zachowano wszystkie nazwy i etykiety.
- [GitHub Actions 44935907983](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935907983) zakończył się **success** dla commitu poprawiającego tekst. Testy Jordana, walidacja katalogu i terminologii, dwukrotna kompilacja LaTeX, odsyłacze i eksport bieżącego rozdziału przeszły bez błędów.
- Pobierany z powyższego workflow artefakt `linear-algebra-current-chapter` zawiera **6-stronicowy PDF** rozdziału 17. Wszystkie strony są niepuste; kontrola tekstowych bloków z PyMuPDF wykazała **0 bloków wychodzących poza granice stron**. Po renderowaniu i przeglądzie wizualnym nie stwierdzono nachodzenia napisów na wzory ani przycięć.

## Decyzja

**Audyt II wykazał i usunął trzy niedoprecyzowania.** Po korektach nie znaleziono dalszych błędów merytorycznych. Ponieważ źródło zostało zmienione, zgodnie z rytmem wielokrotnego audytu rozdział 17 pozostaje **w audycie** do wykonania niezależnego audytu III. Rozdziały 01–16 pozostają stabilne. Nie dodawać nowych twierdzeń w kolejnych audytach 17; sprawdzić wyłącznie aktualny tekst, PDF i CI.
