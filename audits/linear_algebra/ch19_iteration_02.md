# Algebra liniowa — rozdział 19, audyt II (niezależny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/19-postac-frobeniusa-i-czynniki-niezmiennicze.tex`  
**Wersja po korekcie:** `230cea2d0c9e7bd616bd7f1ed9f24e0953609a7e`  
**Poprzedni audyt:** `ch19_iteration_01.md`.

## Audyt matematyczny

1. **Zakres i przypadki brzegowe.** Twierdzenia wymagają tylko ciała `K` i skończonego wymiaru. W zerowym wymiarze macierz, lista czynników i suma blokowa są puste, a oba wielomiany przyjęte jako `1`. W definicji towarzyszącej uwzględniono `d=1`; nie wymaga się algebraicznego domknięcia.
2. **Moduł operatora.** Podstawienie `p -> p(T)` jest homomorfizmem pierścieni: równość `(pq)(T)=p(T)q(T)` wynika z pomnożenia sum potęg `T`. Izomorfizm modułów jest dokładnie odwracalnym operatorem liniowym przeplatającym oba `T`.
3. **Prezentacja macierzą `tI-A`.** Homomorfizm `ε(f)=ΣA^kv_k` jest surjekcją i jest `K[t]`-liniowy; teleskopowa tożsamość `t^kI-A^k=(tI-A)Σ t^(k-1-j)A^j` daje także odwrotne zawieranie `ker ε ⊆ (tI-A)K[t]^n`. Nie korzysta się tu z twierdzenia Smitha ani z przyjęcia baz pośrednich.
4. **Algorytm Smitha.** Każda nieudana próba podzielności daje niezerową resztę o mniejszym stopniu; kolejne zerowania wiersza i kolumny są skończone. Gdy pozostały blok nie jest podzielny przez wyróżniony element, dodanie wiersza i operacja kolumnowa ponownie obniżają stopień. Operacje mają odwrotności nad `K[t]`; wyznacznik nie znika i indukcja działa.
5. **Dzielniki wyznacznikowe.** Każda operacja elementarna zachowuje ideał generowany przez minory stopnia `k` (w obie strony). W trakcie audytu uzupełniono *jawny* argument: przy obu wybranych wierszach dodatkowy wyznacznik ma wiersze jednakowe, a przy jednym wybranym wierszu liniowość daje kombinację dwóch minorów; analogicznie na kolumnach. Dla diagonali z łańcuchem podzielności `Δ_k=d_1...d_k`; stąd jednoznaczne `d_k=Δ_k/Δ_(k-1)`.
6. **Macierz towarzysząca.** Dzielenie przez moniczny `f` wyznacza bazę klas `1,t,...,t^(d-1)`. Mnożenie przez `t` daje wskazaną macierz; jej wielomian minimalny to dokładnie `f`, a charakterystyczny również `f` dzięki Cayleyowi–Hamiltonowi i porównaniu stopni.
7. **Postać Frobeniusa.** Smith macierzy `tI-A` daje rozkład `V_T ≅ ⊕K[t]/(d_i)`, usunięcie `d_i=1` jest legalne. `χ_T=∏f_j` wynika z wyznacznika po normalizacji, a `m_T=f_r` ze wspólnego anihilatora sumy cyklicznych modułów. Przy zmianie bazy ekwiwalencja wielomianowa zachowuje czynniki Smitha.
8. **Kryteria.** Dla `n≥1` cykliczność oznacza jeden blok i równoważnie `χ_T=m_T`; dowód używa wcześniejszego wyniku o minimalnym wielomianie wektora. Dla `n=0` wyjątek jest jawnie omówiony.

## Przykłady — rachunek niezależny

Wyznaczniki i NWD wszystkich minorów ponownie policzono w SymPy, niezależnie od testu repozytorium:

| Macierz | `Δ_1, Δ_2, Δ_3` (stosowne wymiary) | Czynniki Smitha |
| --- | --- | --- |
| `J_2(0)⊕J_1(0)` | `1,t,t^3` | `1,t,t^2` |
| `diag(1,1,2)` | `1,t-1,(t-1)^2(t-2)` | `1,t-1,(t-1)(t-2)` |
| `[[0,-1],[1,0]]` | `1,t^2+1` | `1,t^2+1` |

## Struktura i redakcja

- Zgodność definicji i treści z rozdziałami 16–18; brak dublowania twierdzeń.
- Zachowano wszystkie istniejące etykiety i odsyłacze.
- Poprawiono błąd fleksyjny „kombinację liniową minory” oraz dopisano krótkie wyjaśnienie podstawy używanej niezmienniczości minorów. **Nie dodano nowych twierdzeń ani lematów.**
- W aktualnym źródle jest 20 etykiet, 13 odsyłaczy oraz 7 dowodów.
- CI po korekcie: [uruchomienie 44941540440](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44941540440); status należy sprawdzić po zakończeniu uruchomienia.

## Decyzja

Audyt II **bez kontrprzykładów i luk w tezie**, z jedną poprawką uzasadnienia w dowodzie Smitha. Rozdział pozostaje w audycie do następnych niezależnych czystych kontroli oraz pozytywnego CI i PDF.
