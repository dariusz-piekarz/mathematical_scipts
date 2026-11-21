# Algebra liniowa — rozdział 19, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/linear_algebra/19-postac-frobeniusa-i-czynniki-niezmiennicze.tex`  
**Blob rozdziału:** `64ca6fc464c80d76a4adc002668366b6720b6dd6`  
**Poprzedni etap:** rozdziały 01–18 stabilne, raport `ch18_iteration_03.md`.

## Weryfikacja matematyczna

1. **Działanie modułu (V_T).** Sprawdzono liniowość i zgodność mnożenia wielomianów z `p(T)q(T)=(pq)(T)`. Izomorfizm (K[t])-modułów jest równoważny (K)-liniowemu izomorfizmowi przeplatającemu operatory. Nie zakładamy algebraicznej domkniętości (K).
2. **Prezentacja (V_T).** Mapowanie `ε(Σt^kv_k)=ΣA^kv_k` jest surjektywne i liniowe nad (K[t]). Zweryfikowano teleskopową tożsamość `t^kI-A^k=(tI-A)Σ_(j<k)t^(k-1-j)A^j`, która dowodzi równości jądra z `(tI-A)K[t]^n`. Przypadek (n=0) jest poprawny.
3. **Postać Smitha.** W pierścieniu euklidesowym (K[t]) elementarne operacje wierszy i kolumn są odwracalne. Redukcja przez dzielenie z resztą obniża stopień wyróżnionego elementu, jeśli nie dzieli on jednego z wpisów; po wyzerowaniu pierwszej kolumny/wiersza redukcja jest powtarzana, jeśli element wyróżniony nie dzieli reszty macierzy. Indukcja daje `d_1|...|d_n` i macierze unimodularne `U,W`.
4. **Jednoznaczność czynników Smitha.** Ideały generowane przez minory ustalonego stopnia są zachowywane przez odwracalne operacje elementarne. Dla macierzy diagonalnej o łańcuchu podzielności `Δ_k=d_1...d_k`; zatem `d_k=Δ_k/Δ_(k-1)` jest niezależne od operacji i od wyboru bazy. Założenie `det M≠0` zapewnia niezerowość `Δ_k`.
5. **Macierz towarzysząca.** Klasy `1,t,...,t^(d-1)` są bazą `K[t]/(f)`, a mnożenie przez (t) ma macierz (C(f)). Z warunku `p(T)·[1]=[p]` wynika, że wielomian minimalny bloku to (f); twierdzenie Cayleya–Hamiltona i porównanie stopni daje `χ_(C(f))=f`.
6. **Postać Frobeniusa.** Prezentacja (V_T), postać Smitha macierzy (tI-A) i usunięcie czynników jednostkowych `d_j=1` dają sumę bloków (C(f_j)). Wzory `χ_T=∏f_j` oraz `m_T=f_r) wynikają odpowiednio z wyznacznika i z przecięcia ideałów annihilatorów. Jednoznaczność opiera się na czynnikach Smitha, które nie zależą od bazy.
7. **Kryteria i przykłady.** Równość `m_T=χ_T` jest równoważna jednemu blokowi dla (n≥1), a ten warunek istnieniu wektora cyklicznego. Sprawdzono przykłady (J_2(0)⊕J_1(0)), diagonalnej `diag(1,1,2)` nad (mathbb Q) oraz obrotu nad (mathbb R), gdzie `t²+1` nie rozkłada się na czynniki liniowe.
8. **Terminologia.** W całym nowym rozdziale zachowano regułę „wielomian rozkłada się nad ciałem na czynniki”; ani razu nie zastosowano innego czasownika dla tego pojęcia. Nie zmieniono etykiet wcześniejszych rozdziałów.

## Testy, integracja i status

- Rozdział dodano do `books/pl/linear_algebra.tex`, `catalog/books.json`, `README.md` oraz `.github/workflows/linear-algebra-chapter.yml`.
- Dodano `tools/test_linear_algebra_frobenius.py`: obliczenie monicznych wyznacznikowych dzielników `Δ_k`, czynników Smitha i wielomianów minimalnych dla wszystkich `2×2` nad `F2,F3`, wszystkich `3×3` nad `F2` i 500 deterministycznie wybranych `3×3` nad `F3`, oraz sprawdzenie niezmienniczości względem sprzężenia i odtworzonej postaci Frobeniusa.
- Pierwszy przebieg CI po integracji, [44940345350](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44940345350), wykrył **techniczną usterkę testu**, polegającą na dodaniu listy do krotki w Pythonie. Poprawiono `list(coeffs)+(1,)` na `list(coeffs)+[1]` (commit `ee1ce17b741e18a255806d0afd5da107f581f1ef`).
- Regresja w [44940416454](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44940416454) po tej poprawce zakończyła się sukcesem. Wynik pełnej kompilacji i PDF należy potwierdzić po zakończeniu przebiegu.
- Źródło rozdziału ma **20 unikatowych etykiet**, **13 poprawnych odsyłaczy**, **7 par środowiska `proof`** i około 664 linie.

## Decyzja

**Audyt I nowego rozdziału 19 — wyniki matematyczne po pierwszej kontroli bez znalezionych kontrprzykładów.** Wykryto i naprawiono błąd techniczny nowego testu, dlatego do czasu niezależnego audytu II i ostatecznej kontroli PDF rozdział pozostaje `w audycie`. Nie dodawać nowych twierdzeń podczas jego kolejnych iteracji.
