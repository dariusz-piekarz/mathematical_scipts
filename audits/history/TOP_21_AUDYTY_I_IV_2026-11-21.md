# Topologia algebraiczna — TOP-21, audyty I–IV

**Data:** 21 listopada 2026.  
**Repozytorium i gałąź:** `dariusz-piekarz/mathematical_scipts`, `biblioteka-matematyczna-iteracja-6`; gałąź `main` bez zmian.  
**Rozdział:** `chapters/pl/algebraic_topology/21-indeks-pol-wektorowych-i-twierdzenie-poincarego-hopfa-z-brzegi.tex`.  
**Końcowy blob:** `70099ac735f1da25abc97313586b3752f78743ff`, **526 wierszy**.  
**Standard:** powtarzany pełny audyt istniejącego materiału (poprawność matematyczna, samodzielność sformułowań, uzasadnienie każdego istotnego przejścia, terminologia, przykłady, rysunki, odsyłacze, TeX/CI), **bez nowych twierdzeń ani lematów**. Punktem wyjścia był raport `TOP_21_22_ITERACJA_21_2026-11-21.md`.

## Audyt I — lokalny stopień i porównanie indeksów

Ponownie zweryfikowano wszystkie sekcje TOP-21: lokalne przejście od zera pola do punktu stałego, wersję Poincarégo–Hopfa z brzegiem, pole skierowane do wnętrza, pierścień, nieorientowalną wstęgę Möbiusa, stopień brzegowy i zmianę indeksu podczas wejścia zera do dysku.

W lemacie o lokalnym porównaniu indeksów wykryto niepoprawną dziedzinę stopnia: pojawiało się `deg(id−F_t,U,0)` dla `U⊂M`, podczas gdy stopień Brouwera powinien być obliczany w obszarze współrzędnych `φ(U)⊂R^n`. Poprawiono formułę na `deg(id−F_t,φ(U),0)=deg(V,φ(U),0)`. Jawnie określono mapę `φ:W→R^n`, `φ(p)=0`, warunek `cl U⊂W∩int M`, izolowanie zera w `cl U`, warunek `f_t(cl U)⊂W` i ścisłą definicję pola współrzędnościowego `V`.

Doprecyzowano definicję pola skierowanego na zewnątrz, używając `X∈𝔛(M)`, oraz usunięto dwa nieaktualne komentarze robocze.

**Commit źródła:** `47c33bef0770bb7276e86ddc9fe33e86ba5fe0f4`.

Dodano dwa testy ochronne: poprawność dziedziny stopnia Brouwera oraz rachunek przechodzenia zera przez brzeg dysku dla `X_s(x)=(1−s)e_1+sx`. **Commit testów:** `2654b8eeda27bbae0d79c334361085953efd7843`.

## Audyt II — dowód przez podwojenie rozmaitości

Niezależnie sprawdzono etap przejścia od `f_t:M→M` do `F=j f_t r:DM→DM`, gdzie `DM` jest podwojeniem, `j` włożeniem, a `r` odwzorowaniem składającym. `F` jest ciągłe i gładkie w otoczeniach jego izolowanych punktów stałych, jednak wzdłuż szwu podwojenia nie musi być gładkie.

W poprzednim dowodzie brakowało explicite argumentu, że wygładzenie nie zmienia **liczby Lefschetza**, a nie tylko zbioru punktów stałych. Dodano dokładnie ten krok: względna gładka aproksymacja `\widetilde F` jest homotopijna z `F`, identyczna z nim w małych otoczeniach punktów stałych i jednostajnie bliska poza nimi, więc nie wprowadza nowych punktów stałych, zachowuje lokalne indeksy i spełnia `L(\widetilde F)=L(F)`. Dopiero do `\widetilde F` stosuje się gładką formułę Lefschetza–Hopfa. Zależność od względnego twierdzenia aproksymacyjnego jest jawna.

**Commit źródła:** `fd896b56bb9f408040d0a8e6402a95208bdd8a50`.

Do testów dodano regresję dotyczącą zachowania punktów stałych i liczby Lefschetza podczas wygładzania oraz kontrolę **kolejności zagnieżdżania** wszystkich środowisk i domknięcia odsyłaczy w TOP-21/22. **Commit testów:** `92d6b213f52cf2084d4865362eb89864e24a8ce1`.

## Audyt III — samodzielne przykłady i rachunek indeksów

W przykładzie z gradientem funkcji Morse'a dopisano jawnie metrykę riemannowską `g` i oznaczenie `X=grad_g f`. Trzy przykłady na dysku uzupełniono o wymiar `n≥1` lub `n≥2`, zależnie od używanego twierdzenia.

Niezależnie sprawdzono:
- dla pola `X(x)=x` na dysku indeks `+1`, a dla `X(x)=−x` indeks `(−1)^n`; sprawdzono osobno parzystość wymiaru;
- na pierścieniu `X=(r−r_0)e_r+e_θ` nie ma zer, a na **obu** składowych brzegu jego składowa normalna jest dodatnia; stopnie na dodatnio geometrycznie parametryzowanych okręgach są równe `+1`, ale indukowana orientacja wewnętrznego brzegu daje `−1`, więc suma to zero;
- pole na wstędze Möbiusa jest zgodne z identyfikacją `g(θ,t)=(θ+2π,−t)`, bezzerowe i skierowane na zewnątrz;
- dla interpolacji `X_s(x)=(1−s)e_1+sx` zero jest poza dyskiem przy `s<1/2`, na brzegu dla `s=1/2` i wewnątrz przy `s>1/2`; zmiana indeksu nie przeczy niezmienniczości przy warunku brzegowym.

**Commit źródła:** `9e1f3a55f6f3ba4a3a2bd70ac7a5e8a8b7b99ef9`.

## Audyt IV — ponowna walidacja matematyczna, strukturalna i wizualna

Źródło po trzech poprawkach ponownie pobrano z GitHuba. Stwierdzono:
- **14 różnych etykiet**, **13 poprawnie domkniętych odsyłaczy**;
- wszystkie środowiska prawidłowo domknięte i zagnieżdżone, zachowany diagram TikZ pierścienia;
- brak niedozwolonej terminologii i starych komentarzy iteracyjnych;
- brak nowych zastrzeżeń matematycznych wymagających korekty.

Wykorzystano rzeczywisty artefakt GitHub Actions wygenerowany z końcowego commita źródła `9e1f3a55`. Dokument kontrolny TOP-01–23 liczy **259 stron**; TOP-21 jest na stronach **237–242**, a osobny PDF ma **6 stron**. Obejrzano render wszystkich stron rozdziału i powiększony rysunek pierścienia. Brak widocznych kolizji podpisów, przepełnień i obcięć. Drugi przebieg `pdflatex`: **0 błędów**, **0 niezdefiniowanych odsyłaczy**, **0 Overfull hbox**. Trzy ostrzeżenia `Underfull hbox` pochodzą z wcześniejszych rozdziałów TOP-11, TOP-12 i TOP-15.

## Potwierdzenie GitHub Actions

Po końcowym commicie źródła `9e1f3a55`:
1. [Kompilacja TOP-01–23, poprawność odsyłaczy i Overfull](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938562863) — **completed / success**.
2. [Aplikacja, indeksowanie, testy regresyjne, testy przeglądarkowe](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938562822) — **completed / success**.
3. [Kontrola AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938562994) — **completed / success**.
4. [TOP-21 ↔ DG-17, względna klasa Eulera i Poincaré–Hopf](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938562893) — **completed / success**, oba zadania kompilacyjne, w tym pełny bieżący DG-01–20.

Po ostatniej zmianie **samych testów** `92d6b213`:
- [Aplikacja i rozszerzone regresje](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938500794) — **completed / success**.
- [Kompilacja TOP-21–22 z pełnym kontekstem](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938500762) — **completed / success**.
Ostatnia zmiana testów poprzedzała finalny commit źródła; pełne testy na końcowym źródle również przeszły.

**Decyzja:** TOP-21 **STABILNY PO AUDYCIE IV**, z zachowanymi wynikami i wszystkimi historycznymi etykietami. Nie dodano nowych twierdzeń ani lematów. Następny rozdział do ponownej stabilizacji: **TOP-22**. Nie uruchomiono automatyzacji.