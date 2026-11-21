# Algebra liniowa — rozdział 29, audyt VII (czysty matematycznie)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/29-grassmanniany.tex`, blob `8dc9a0ed6ae1868e2b95acae77d96a9dae989077` — niezmieniony w tej iteracji.

## Niezależne sprawdzenie

1. **Atlas wykresowy:** dla V=P⊕Q wykazano obustronną jednoznaczność pomiędzy wykresami podprzestrzeni i Hom(P,Q); formuła przejścia `A'=π_Q' T_A(π_P' T_A)^{-1}` ma jasno podaną otwartą dziedzinę. Przy k=0,n wykresy mają zerowymiarowe parametry i obejmują pojedynczą podprzestrzeń.
2. **Topologia:** osadzenie w przestrzeni macierzy rzutu ortogonalnego uzasadnia Hausdorff i przeliczalną bazę, a domkniętość i ograniczoność podzbioru idempotentów samosprzężonych ze śladem k — zwartość. Jawnie pokazano zgodność atlasu z topologią macierzy.
3. **Przestrzeń styczna:** konstrukcja z pochodnej krzywej `v(t)∈L(t)` jest niezależna od reprezentantów modulo L, a współrzędnie jest `A'(0)`. Z niej wynika kanoniczny izomorfizm `T_L Gr_k(V) ≅ Hom(L,V/L)`.
4. **Wiązki:** po audycie III wszystkie potrzebne pojęcia (rząd, lokalna trywializacja, cofnięcie, dualna wiązka, normalna) są jawnie zdefiniowane. Dokładność ciągu `0→γ→B×V→Q→0` wynika z jądra i surjektywności map na każdym włóknie.
5. **Osadzenie Plückera:** po audycie VI treść precyzyjnie rozróżnia immersję i gładkie osadzenie. Dowód odzyskuje podprzestrzeń jako `{w:w∧ξ=0}`, różniczka ma lewą odwrotność w mapie wykresowej, a zwartość i Hausdorff dają globalne osadzenie.
6. **Odwzorowanie Gaussa:** w lokalnej parametryzacji `F` macierze `D_PF` i `D_QF` prowadzą do mapy wykresowej; poprawnie zdefiniowane `νM` jest izomorficzne z ilorazem `R^N/T_pM`.

## Niezależne testy

- **250** dokładnych przypadków Gr(2,4): jądro odwzorowania `w ↦ w∧ξ` odzyskuje dokładnie pierwotną płaszczyznę — PASS.
- **175** analogicznych przypadków Gr(3,5), z minorami stopnia 3 i liniowymi warunkami stopnia 4 — PASS.
- W poprzednich przebiegach zweryfikowano 500 przypadków chart/Plücker i 175 przypadków rzutów/zmian map. Nie znaleziono kontrprzykładu do żadnego wzoru.

## Decyzja

**Audyt VII matematycznie i redakcyjnie czysty**, bez zmiany źródła.
Pozostaje ostateczna kontrola aktualnego artefaktu PDF i drugi czysty audyt VIII przed stabilizacją.
