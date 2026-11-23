# AA-49 — kwadratowy przypadek algorytmu Kovacica: zakres

**Data:** 23 listopada 2026 r.
**Poprzedni etap:** AA-48 STABILNY.
**Rozdział:** chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex.
**Status:** W AUDYCIE — NIE STABILNY.

## Zakres matematyczny

1. Rozwiązania Riccatiego stopnia dokładnie 2 nad C(x); automorfizm sprzężenia i zachowanie derywacji; ślad φ=r+rbar, wyróżnik Δ=(r−rbar)^2 i wniosek Δ'=−2φΔ.
2. Równanie śladu φ''+3φφ'+φ³−4qφ−2q'=0 i dokładna równoważność z istnieniem algebraicznych pierwiastków r±=(φ±√Δ)/2. Test niekwadratowości Δ odróżnia ścisły stopień 2 od gałęzi racjonalnej AA-48.
3. Symetryczny kwadrat: jeśli z1''=qz1, z2''=qz2, to v=z1z2 spełnia v'''−4qv'−2q'v=0. Podstawienie φ=θ+P'/P daje liniowy trzeciorzędowy operator na P; obie strony równoważności mają pełne dowody.
4. Wyczerpujące, skończone listy lokalne E_a,E_∞ oraz wzór n=(e∞−Σe_a)/2 i θ=Σ e_a/(2(x−a)) **są wyraźnie cytowanymi klasycznymi wynikami Kovacica**, nie własnymi dowodami pełnej lokalnej klasyfikacji. Źródło: J. Kovacic, J. Symbolic Computation 2 (1986), 3–43.
5. Przy cytowanych listach: skończona enumeracja, liniowe układy na P ustalonego stopnia, konieczna kontrola Δ≠0 i nierówności względem kwadratów; ogólny przypadek parametrów można rozstrzygnąć eliminacją algebraiczną (nie deklarować wydajnej implementacji).
6. Przykłady z bezpośrednim rachunkiem: q=x+5/(16x²) i n=0; q=(4x+5)/(16x²) i n=1 z P=x−1; q=1/x−3/(16x²), n=0; negatywny przypadek Airy'ego.
7. Regresje: 11 testów SymPy oraz 10 niezależnych testów Fraction; pełne zdalne CI, kontrola 49 rozdziałów i każdego nowego arkusza PDF; audyty I–III przed stabilizacją.

## Granice

To **drugi** przypadek Kovacica; przypadek trzeci (skończone prymitywne grupy algebraiczne i stopnie 4, 6, 12) jest poza zakresem. Wnioski o zupełności wynikają warunkowo z cytowanej klasyfikacji lokalnej; sprawdzenie kilku modeli nie stanowi dowodu tej klasyfikacji.

**AA-50 nieotwarty.**
