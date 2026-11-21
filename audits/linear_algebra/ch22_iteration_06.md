# Algebra liniowa — rozdział 22, audyt VI (ostateczny, stabilizacyjny)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Zatwierdzony blob:** `11aafed28081c5db85005cf235f51b6795710705`  
**Poprzednie audyty:** I–V; ostatnia korekta w IV dotyczyła jedynie łamania wiersza.

## Powtórna kontrola matematyczna

1. Równanie przeplatania `AX=XB` zinterpretowano jako `K[t]`-homomorfizm `W_B→V_A` z zachowaniem zgodności wszystkich rozmiarów.
2. Kryterium `gcd(χ_A,χ_B)=1` jest równoważne jądru zerowemu `S_(A,B)`, a więc jej odwracalności i jednoznacznej rozwiązywalności dla każdej prawej strony. Dowód działa nad dowolnym ciałem.
3. Tożsamość teleskopowa daje znak minus w jawnej formule i nakazuje mnożyć przez `χ_A(B)^{-1}` z prawej strony. Odwracalność `χ_A(B)` została uzasadniona przez Bézout i Cayleya–Hamiltona. Test nad `F2,F3` sprawdza formułę niezależnie przez podstawienie.
4. Skończony wzór dla bloków Jordana `λ≠μ` opiera się na nilpotentności `L_N-R_M`. Jego dowód jest poprawny w każdej charakterystyce; dla `λ=μ` wymiar przestrzeni przeplatającej to `min(a,b)`.
5. Stabilność spektralna i równanie Lapunowa: oszacowanie wykładniczej daje całkowalność, całkowanie pochodnej wyprowadza równanie, z dodatniej określoności integrandu wynika dodatnia określoność wyniku, a z zaniku wykładniczej jednoznaczność. Implikuje odwrotną stabilność podstawienie wektora własnego. Nie wymagano diagonalizowalności macierzy.
6. Wniosek o malejącej energii jest uzasadniony pochodną iloczynu i invertowalnością `e^{tA}`.
7. Przykłady: nad `Q` rozwiązanie `X=(-2,-2)^T`; nad `C` nie-normalna stabilna macierz i dodatnie `P=[[1/2,1/6],[1/6,1/3]]`; przypadki braku rozwiązań lub niejednoznaczności. Obliczenia zgodne z niezależną kontrolą algebraiczną.

## Skład, regresje i artefakty

- Źródło ma 25 unikatowych etykiet, 25 odsyłaczy i 10 poprawnie sparowanych dowodów.
- Terminologia zachowuje globalne zasady i odsyła do rzeczywistych etykiet rozdziałów 16–21.
- [GitHub Actions 44944927262](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944927262) — **SUCCESS**, obejmuje cały zestaw regresji, ponowną kompilację, walidację odsyłaczy i kontrolę ostrzeżeń LaTeX.
- [GitHub Actions 44944950886](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944950886) — **SUCCESS** również po zapisaniu raportu audytu IV; zapewnia aktualny samodzielny PDF.
- PDF eksportowany z pomyślnego workflow: **8 stron, 8 niepustych**, wszystkie bloki tekstu w granicach stron (**0 naruszeń** w PyMuPDF). Wyrenderowano i obejrzano układ wszystkich ośmiu stron. Brak uciętych wzorów, kolizji i błędów paginacji.
- Audyt VI nie spowodował dalszych zmian w źródle.

## Decyzja

**Audyt VI czysty**, drugi kolejny czysty przegląd po ostatniej korekcie z audytu IV. Rozdział 22 jest **STABILNY** po sześciu audytach. Rozdziały 01–22 są stabilne; kolejny rozdział powinien być opracowywany jako osobny etap. Zgodnie z procedurą nie dokładamy nowych twierdzeń do już zamkniętych rozdziałów.

**Propozycja do osobnej decyzji użytkownika:** równanie dyskretne Lapunowa `A*PA-P=-Q` i stabilność Schura (wartości własne wewnątrz koła jednostkowego) jako naturalny następny zakres. Nie dopisano go do rozdziału 22.
