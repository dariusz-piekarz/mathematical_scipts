# Algebra liniowa — audyt globalny 33: LA-32 i naprawa zakładek PDF

**Data:** 23 listopada 2026; **gałąź:** `biblioteka-matematyczna-iteracja-6`. Zakres: cały rozdział LA-32 (917 wierszy), dziesięć dowodów, rysunki i bieżąca książka PDF. Źródło przed zmianą: `8aea8bd8db02ca8677fb0547f770c9166fdaef88`. Po korekcie nagłówków: `9ed35f18a5300f6e9ee70e8654ef0092e260af2f`. Powiązany LA-13: stary blob `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af`, nowy `ddf705004f13f4df7289036d82c13ff64fe89f56`.

## Kontrola 10/10 dowodów — zakres i wyniki

Oddzielny [rejestr wszystkich dziesięciu dowodów](iteration_33_proof_review_32.csv) dokumentuje sprawdzane wnioski. Przeprowadzono sceptyczny reread całych 917 wierszy źródła (nie tylko testy):
1. Forma spolaryzowanego wyznacznika jest niezdegenerowana; jądro działania `SL₂×SL₂` jest dokładnie `{(I,I),(-I,-I)}`.
2. Odwrotność osadzenia Segrego na czterech otwartych mapach istnieje, a rząd 1 macierzy determinuje parę czynników rzutowych.
3. Wzór `det(uαᵀ+λvβᵀ)=λdet[u,v]det[αᵀ;βᵀ]` daje dokładnie dwie rodziny maksymalnych podprzestrzeni izotropowych; z niezdegenerowania formy wynika granica wymiaru 2.
4. Dwie proste twistorowe przecinają się dokładnie wtedy, gdy `det(X−Y)=0`; przy `X≠Y` jądro ma wymiar 1.
5. `X↦Xπ` jest surjekcją dla `π≠0`, płaszczyzna incydencji ma wymiar 2 i jedno wspólne jądro.
6. Lokalna transformata Penrose'a: sprawdzono założenia holomorficzności w otoczeniu konturu, jednorodność `−2`, niezmienniczość pod skalowaniem `π`, prawidłowe pochodne `∂ij F(Xπ,π)` oraz `□_C Φ=0`. Przykład `F=1/(ω₁ω₂)` daje residuum `−1/det X`; nie utożsamia się tego lokalnego wzoru z pełnym kohomologicznym izomorfizmem Penrose'a.
7. Minory wykresu `W_X` dają `[det X:-b:a:-d:c:1]`, spełniają równanie Plückera, a `p₃₄≠0` pozwala jednoznacznie odzyskać `X`.
8. W korespondencji flag włóknami są `CP¹` i `CP²`; incydencja `ω=Xπ` dotyczy otwartej mapy `π≠0`.
9. `J²=-I` i antyliniowość wykluczają rzutowe punkty stałe `[z]=[Jz]`; określone jest prawidłowe działanie na zespolonych prostych.
10. Jawna trywializacja kwaternionowa `(q,[v])↦[(v,qv)]` ma gładką odwrotność; `HP¹≃S⁴` uzyskuje się przez stereografię także w drugiej mapie.

W zakresie tych dziesięciu dowodów nie znaleziono błędu matematycznego.

## Nowe niezależne testy dokładne

Odrębny skrypt `/mnt/data/la_audit/la32_independent_checks.py` (Python/SymPy/Fraction, seed 202611230033): **7019/7019 PASS**, w tym:
- 4 kontrole polaryzacji, 600 działania `SL₂×SL₂`;
- 900 testów Segrego i 900 wspólnego wiersza, 487×2 kontrole incydencji i izotropowości;
- 700×2 kontroli minorów Plückera;
- 1 symboliczny test równania `□_C(det X)^{-1}=0`, 640 dokładnych reszt;
- 600 kontroli wzoru mnożenia kwaternionowego bez błędów zaokrąglenia, 1000 tożsamości stereograficznych.

Początkowa implementacja samego *test harness* użyła konwersji SymPy do typu `complex`; porównanie dokładnej wartości 0 z zaokrąglonym `−1.08⋅10^{-19}` powodowało fałszywą porażkę. Zastąpiono tę konwersję obliczeniami dokładnymi, po czym wszystkie 7019 testów przeszły. **Nie oznacza to usterki w rozdziale.**

## Rzeczywisty PDF — wykryty problem redakcyjny G33-01

Pobrano oryginalny artefakt [CI 45085147540](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45085147540), zakończony SUCCESS dla poprzedniego, niezmienionego matematycznie bloba. Obejrzano **9/9 stron LA-32, PDF 312–320**, w tym rysunki incydencji, konturu Penrose'a i fibracji. Nie znaleziono widocznych kolizji. W całej książce 320 stron i 7844 bloki tekstowe: **0 bloków poza stronami**. Brak pustych stron, przepełnień i nierozwiązanych odsyłaczy.

Jednak niezależna analiza `linear_algebra.log` ujawniła **8 ostrzeżeń `Package hyperref Warning`**, pomimo sukcesu CI (bramka CI ich dotąd nie wykrywała):
- LA-13, linia 36: 2 ostrzeżenia dla matematycznych symboli `R,C` w tytule sekcji;
- LA-32, linia 13: 3 ostrzeżenia dla `2×2`;
- LA-32, linia 666: 3 ostrzeżenia dla `C⁴`.

Naprawiono **wyłącznie trzy nagłówki** przez `\\texorpdfstring{zapis matematyczny}{zwykły tekst zakładki PDF}`. Nie zmieniano dowodów, definicji, wzorów, etykiet, przykładów ani rysunków. Commity: [LA-13 `b89cf878`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/b89cf8784fb27dcdd6831f815f971edb7a0ce21e), [LA-32 `fdf0ceee`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/fdf0ceee2b112174687235794c11d58395143ff6).

## Decyzja

**Globalny audyt 33 jest korekcyjny, nie bezusterkowy.** Merytorycznie LA-32: **10/10 dowodów skontrolowanych**; postęp rejestru **382/382**. **Nie zamykać całego skryptu** na podstawie starego PDF ani starego CI: trzeba wykonać nowy CI i obejrzeć PDF po poprawkach, przeprowadzić dwie czyste kontrole poprawionych blobów oraz dodatkowy sceptyczny audyt przekrojowy i potwierdzający. Zostawić źródła matematyczne bez dalszych zmian, jeśli nie pojawi się faktyczna usterka.
