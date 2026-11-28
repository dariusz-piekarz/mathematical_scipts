# Analiza funkcjonalna — rozdział 07 — audyt 05 (niezależne potwierdzenie stabilizacji)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex`.  
**Blob SHA źródła:** `3802015b41891911fe852e6a2600547d894fab8c` (bez zmian względem audytów 07/03 i 07/04).  
**Werdykt:** **CZYSTY, 2/2 — ROZDZIAŁ 07 STABILNY**. W tej iteracji nie zmieniano źródła ani testów.

## Weryfikacja stanu przed pracą

Odczytano raporty `07-audyt-3.md` i `07-audyt-4.md`, aktualne źródło 07, testy `tools/tests/test_functional_analysis_ch07.py`, plik główny książki oraz źródło 06 dla odsyłacza. Audyt 07/03 zawierał dwie poprawki i reset do 0/2. Audyt 07/04 był pierwszym czystym przeglądem na tym samym blob SHA (1/2). Raport `07-audyt-5.md` nie istniał przed tą iteracją.

## Niezależna kontrola matematyczna: 11/11 dowodów

1. **Rekonstrukcja zespolonego funkcjonału:** `F(x)=ell(x)-i ell(ix)`; liniowość, jednoznaczność i ciągłość wynikają z ciągłości mnożenia przez `i`. PASS.
2. **Minkowski:** dla otwartego wypukłego otoczenia 0 dowiedziono pochłaniania, dodatniej jednorodności, podaddytywności i ciągłości bez założenia symetrii; `V={p_V<1}`. PASS.
3. **Punkt poza otwartym zbiorem wypukłym:** `-a∉V`, więc `p_V(-a)≥1`; przedłużenie funkcjonału na prostej przez Hahn–Banacha daje `ell(d)<0` dla `d∈D`. PASS.
4. **Dwa zbiory wypukłe, jeden otwarty:** `A-B` jest otwarty i wypukły, nie zawiera 0; punktowa ścisłość nie została pomylona z jednolitą luką. PASS.
5. **Otoczenie zbioru zwartego:** skończone podpokrycie otoczeniami `k+W_k`, `W_k+W_k⊂V_k`, wspólne `U` wystarczają bez metryzowalności. PASS.
6. **Silna separacja:** otwarty wypukły `A+U` nie przecina `B`; z `ell(u_0)>0` otrzymuje się dodatnią jednolitą lukę. PASS.
7. **Separacja punktu od domkniętego wypukłego:** singleton jest zwarty, więc zastosowanie poprzedniego twierdzenia ma wszystkie hipotezy. PASS.
8. **Hiperpłaszczyzna podpierająca:** `(1-t)x+tg_0∈int(C)` dla `0<t≤1`, a przejście graniczne jest uprawnione. PASS.
9. **Polary:** antymonotoniczność, absolutna wypukłość, `A°=(aco A)°`, `A⊂A°°` oraz domkniętość jako przecięcie przeciwobrazów domkniętych przedziałów/kul. PASS.
10. **Bipolar:** `C=cl(aco A)` jest niepusty także dla `A=∅`; silna separacja i obrót fazy dają `sup_C |F|=sup_C Re F`; przypadki `m=0` i `m>0` rozdzielono. PASS.
11. **Domknięcie słabe zbioru wypukłego:** oddzielany jest `D=cl C`, nie niekoniecznie domknięty `C`; separator jest słabo ciągły. PASS.

## Przykłady: 4/4

- `(-1,0)` i `{0}`: ścisła separacja punktowa bez jednolitej luki. PASS.
- Polara kuli `l^1` w `R²` to kula `l^∞`; dodatkowo niezależnie sprawdzono formułę maksimum na czterech wierzchołkach rombu dla trzech par współczynników. PASS.
- `K^N` w topologii produktowej: polara wektorów bazowych ma skończony nośnik i ograniczone współczynniki; bipolar opisuje kula `l^1`, a obcięcia dowodzą domknięcia. PASS.
- `L^p[0,1]`, `0<p<1`: `X'={0}` daje kontrprzykład do twierdzenia bipolarnego bez lokalnej wypukłości. PASS.

## Sprawdzenia techniczne wykonane w tej iteracji

- Parsowanie aktualnego źródła: **11/11** otwarć/zamknięć `proof`, **4/4** `przyklad`, **17/17** etykiet unikatowych, **12** wystąpień odsyłaczy. Jedyny cel spoza rozdziału 07, `sec:hahn-banach` (trzy wystąpienia), znaleziony w rzeczywistym źródle 06: **12/12 celów istnieje**.
- Dwa niezależne proste sprawdzenia rachunkowe: funkcjonał Minkowskiego `p(x)=max(x,0)` dla `V=(-∞,1)` w pięciu punktach oraz formuła `sup_{||x||_1≤1}|a·x|=||a||_∞` na trzech zestawach współczynników — zgodne z teorią.
- **Nie uruchamiano ponownie pełnych 22 testów**, nie kompilowano LaTeX lokalnie i nie oglądano ponownie PDF w tej iteracji. Nie przedstawia się powyższych kontroli jako pełnego nowego CI.

## CI i PDF — niezależnie zweryfikowane poświadczenie wcześniejszego przebiegu

Odczytano GitHub API dla [run 45186232281](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45186232281): **status `completed`, conclusion `success`**, commit `13a76c54983740847a915ee9fc67ec7c5d7033e0`, aktualizacja 2026-11-23 13:42:29 UTC. Raport 07/04 dokumentuje na tym samym blob SHA źródła **22/22 testy PASS**, kompilację 43-stronicowego PDF i wizualny przegląd stron 39–43. Zweryfikowano również run 45185870226 (`completed/success`), z którego pochodzi opisany artefakt. Nie jest to nowe wykonanie CI dla niniejszego raportu.

## Decyzja i następny krok

Audyt 07/05 jest drugim kolejnym czystym przeglądem **tego samego źródła** po audycie 07/04; dodatkowo ma niezależną kontrolę matematyczną i potwierdzone wcześniejsze CI/PDF. **Rozdział 07: STABILNY (2/2)**. Rozdziały 01–07 pozostają stabilne. Następna iteracja może rozpocząć **rozdział 08**, po ponownym odczytaniu aktualnego stanu repozytorium. Bez zmian źródła i testów, bez resetu licznika; nie wykonywano force-push ani tworzenia gałęzi.
