# Algebra liniowa — globalny audyt, iteracja 11 (krytyczna kontrola dowodów LA06–11)

**Data:** 2026-11-22. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`; gałąź `biblioteka-matematyczna-iteracja-6`.
**Stan wejściowy:** iteracja globalna 10 potwierdziła 32 moduły, 1083 etykiety, 659 odsyłaczy, kompletność kompilacji i inspekcję 318-stronicowego PDF. Ta iteracja **nie** wznawia zakończonej sekwencji LA12–32.
**Wynik:** **ITERACJA 11 NIE-CZYSTA ze względu na rzeczywistą usterkę w dowodzie LA08, poprawioną i następnie ustabilizowaną w 2+1 niezależnych audytach**. W pozostałych zbadanych fragmentach LA06, LA07, LA09, LA10 i LA11 nie wykryto koniecznej korekty.

## Zakres faktycznej lektury i SHA

Przeczytano pełny rozdział 06 oraz pełny rozdział 08 (w tym wszystkie kroki czternastu środowisk `proof`), a w rozdziałach 07, 09, 10, 11 szczegółowo przeczytano wybrane najistotniejsze twierdzenia i dowody, ze szczególną uwagą na zależności między nimi. **Razem rozdziały 06–11 zawierają 98 środowisk `proof`; nie twierdzimy, że w tej iteracji ponownie z równą głębokością oceniono wszystkie 98 dowodów.** Pozostałe szczegółowe przypadki są przedmiotem wcześniejszych audytów lokalnych i przyszłych iteracji globalnych.

| Rozdział | Aktualny blob | Faktycznie zbadane w tym przebiegu twierdzenia i powiązania |
|---|---|---|
| 06 | `ca2041609035de1bbe8ce390ccc23c0369d726fb` | 11 dowodów: znak złożenia permutacji, wyznacznik nad dowolnym ciałem, naprzemienność w char. 2, wyznacznik iloczynu, transpozycji, kryterium odwracalności, Laplace, `adj A`, Cramer; `n=0` |
| 07 | `5e320759f55012f807be790214d6ad76119ab544` | zmiana bazy dualnej, anihilator i podwójny anihilator, anihilator przecięcia, `ker T^*` i `im T^*`, rząd transpozycji, wzajemność iniektywności i surjektywności, naturalna bidualność |
| 08 | wejściowy `72533f5383fb1e981d82d0a3f582ef45355c536b`; finalny `0cd0e91a194700b38862f2f1478a693dcd2e5dd3` | cały rozdział, w tym wzory współrzędnych, kongruencja form, radykały, symetrie, dim `Sym^k` / `Alt^k`, alternowanie w char. 2 i polaryzacja |
| 09 | `979ce687c677125aeb8304e9d13cb8e7af842602` | diagonalizacja przez kongruencję, prawo bezwładności Sylvestera, kryterium dodatniej określoności, postać kanoniczna form naprzemiennych, rzut i Grama–Schmidta |
| 10 | `9c397a15f5f668e84cb68681e00bf0305cf73adf` | budowa `V⊗W` przez przestrzeń swobodną i iloraz, jednoznaczność, dowód bazy, iniekcja `W⊗V^*→Hom(V,W)`, przestrzeń dualna iloczynu tensorowego, dokładność ciągu dla `U⊂V` |
| 11 | `17f1bae2db46ac6790f1fc562660393f2f616076` | własność uniwersalna `Λ(V)` w dowolnej char., konstrukcja potęgi zewnętrznej, wzór z przetasowaniami, Cauchy–Binet oraz symetryzatory/antysymetryzatory i ich rzutowanie przy `k!` odwracalnym |

## Usterka LA-08 — wykrycie, kontrprzykład, poprawka

W dowodzie `thm:lin8-operatory-wlasnosci` źle sparowano permutacje przy dowodzeniu, że nieznormalizowane alternowanie `AF` jest naprzemienne. **Stara wersja:** `σ↦σ∘(p q)`, co zamienia *pozycje* argumentów w permutowanej krotce i **nie zapewnia** równości odpowiednich składników nawet przy `v_p=v_q`.

**Kontrprzykład do starego kroku:** `k=3`, `v_1=v_2=e_1`, `v_3=e_2` w `K²`; `F(x,y,z)=x_1y_2z_1`; dla `σ=(2,3,1)` wartości wynoszą `F(v_{σ(1)},v_{σ(2)},v_{σ(3)})=1`, lecz dla `σ∘(1 2)=(3,2,1)` wynoszą `0`. Historyczne raporty LA08 określały to parowanie jako poprawne, lecz błędu nie wychwyciły; to potwierdza potrzebę sceptycznego przeglądu z niezależnym kontrprzykładem.

**Nowy, prawidłowy krok:** `σ↦(p q)∘σ`. Dla każdego `j`, `v_{((p q)∘σ)(j)}=v_{σ(j)}`, bo `v_p=v_q`. Jest to inwolucja bez punktów stałych, a znaki są przeciwne, więc pary sumują się do zera także w `char K=2`. Poprawiono wyłącznie ten dowód, bez dodania treści opcjonalnych ani zmiany etykiet.

[Commit źródła 06c2e0b5](https://github.com/dariusz-piekarz/mathematical_scipts/commit/06c2e0b5eb6dd3c50d15989fcbbbcd141782d55f). Kontrola po poprawce:
- [LA08 audyt 04](../ch08_iteration_04_2026-11-22.md) — **nieczysty, korekcyjny**;
- [LA08 audyt 05](../ch08_iteration_05_2026-11-22.md) — **czysty, 1/2**;
- [LA08 audyt 06](../ch08_iteration_06_2026-11-22.md) — **czysty, 2/2**;
- [LA08 audyt 07](../ch08_iteration_07_2026-11-22.md) — **dodatkowy sceptyczny czysty**.

**LA08 jest ponownie STABILNY** na `0cd0e91a194700b38862f2f1478a693dcd2e5dd3`. W dwóch czystych audytach i dodatkowym audycie źródło nie zmieniało się.

## Nowe niezależne regresje rzeczywiście wykonane

1. `/mnt/data/la_global11_alt_pairing.py` — **118 695 PASS**, w tym 118 004 skontrolowane lewostronne pary permutacji `S_k`, `2≤k≤7`, oraz jawny kontrprzykład dla starego parowania; ponownie uruchomiono w audycie 07.
2. `/mnt/data/la08_after_fix_independent.py` — **15 209 PASS**, w tym **12 288** wyczerpujących testów wszystkich form trójliniowych nad `F₂²`, polaryzacji, kongruencji i wymiarów `Sym^k`, `Alt^k`.
3. `/mnt/data/la08_after_fix_skeptical.py` — **1 130 221 PASS**, z tego **1 128 960** wszystkich parowań przy `k=8` i 1260 kontroli kasowania składników nad `F₂,F₃`.
4. `/mnt/data/la_global11_crosscheck.py` — **18 304 PASS** niezależnych regresji dla LA06–11: wyznaczniki, macierze dołączone i Cramera w `F₂,F₃,F₅`; bazy dualne i rząd macierzy transponowanej; przykłady dodatnio określonych form w kryterium Sylvestera; rząd Kroneckera; algebra zewnętrzna; wzór Cauchy’ego–Bineta.

Skrypt z pkt 1 i skrypt z pkt 4 uruchomiono dodatkowo ponownie w końcowym audycie LA08. Liczb testów z ponownych przebiegów **nie należy dodawać jako nowych różnych przypadków**. Poszczególne duże liczby oznaczają kontrole rachunkowe (wiele strukturalnie podobnych przypadków), nie liczbę twierdzeń.

## LaTeX, CI, PDF i śledzenie zmian

Źródło LA08 po poprawce: **1367 wierszy, 43 etykiety, 14 standardowych `ref/eqref`, 14 środowisk `proof`, poprawne domknięcie/zagnieżdżenie środowisk**. Pozostałe rozdziały 06, 07, 09, 10 i 11 mają niezmienione SHA; porównanie aktualnego drzewa z 32 źródłami inwentarza globalnego 10 wykazało **jedną jedyną zmianę źródła: LA08**.

[GitHub Actions 45046473869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45046473869) — **completed/success** dla commitu poprawki `06c2e0b5eb6dd3c50d15989fcbbbcd141782d55f`, który zawiera dokładnie nowy blob LA08. Wszystkie rygorystyczne kroki walidacji skryptu i dwukrotnej kompilacji PDF przeszły. Pobrano **nowy pełny PDF 319 stron** z artefaktu workflow `linear-algebra-ch01-ch32` (ID 14763458526), a po poprawce **wyrenderowano i obejrzano stronę 87** z dowodem. Nie wykryto kolizji ani błędów łamania. Poprzedni globalny przegląd montażu wszystkich 318 stron z iteracji 10 pozostaje kontrolą wcześniejszej wersji; nie deklaruje się powtórzenia 319 osobnych oględzin po zmianie.

## Decyzja i następna iteracja

**ITERACJA 11 WYKONANA, WYKRYTO I POPRAWIONO RZECZYWISTY BŁĄD W DOWODZIE LA08.** Rozdział LA08 ponownie ustabilizowany po dwóch czystych audytach i dodatkowym sceptycznym oraz zielonym CI na identycznym źródle. LA06, LA07, LA09, LA10, LA11 bez koniecznych korekt w analizowanych fragmentach. Nie modyfikować ani nie resetować stabilnych LA12–32 bez nowego konkretnego błędu.

**Globalna niezależna weryfikacja wszystkich 382 dowodów nadal NIE jest zakończona**. Zalecany następny blok: szczegółowy matematyczny przegląd pozostałych, niezbadanych jeszcze w tej iteracji dowodów LA07 i LA09–11; następnie struktura spektralna LA14–20 i zależności sterowania LA22–28.
