# Algebra liniowa — rozdział 09, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**SHA sprawdzonego rozdziału:** `6639b04df4de851feeb6e29e4e6afa39fdaf3764`

## Ponowna kontrola niezależna

Rozdział został przejrzany po audycie II bez dodawania materiału. Weryfikacja dotyczyła kompletności kwantyfikatorów, zgodności założeń z tezami, istnienia, jednoznaczności oraz poprawności kolejnych przejść w dowodach, przypadków wymiaru zero i odmiennych charakterystyk ciała.

- **Własność uniwersalna:** konstrukcja ilorazu `K^(V×W)/N` jest poprawna dla dowolnych przestrzeni wektorowych, a formalne symbole `[v,w]` rzeczywiście tworzą bazę wolnej przestrzeni. Złożenia z kanonicznym odwzorowaniem jednoznacznie wyznaczają mapy wyjściowe.
- **Tensor prosty:** zerowanie przy zerowym czynniku oraz rozdzielanie dwóch niezerowych wektorów funkcjonałami z baz Hamela są udowodnione. Wybrano tylko potrzebne założenia teoriomnogościowe, zgodne z wcześniej użytym twierdzeniem o bazach.
- **Współrzędne:** skończone rozwinięcia z baz czynników zapewniają rozpiętość, a formy `v^p(v)w^q(w)` zapewniają niezależność współczynników, także w przypadkach `n=0` i `m=0`.
- **Rząd tensora:** obie nierówności `rank C_t≤r` oraz `r_min≤rank C_t` są udowodnione i nie zależą od charakterystyki. Przykład z macierzą `I_2` nie jest prosty.
- **Odwzorowania:** `S⊗T` jest poprawnie zdefiniowane przez odwzorowanie dwuliniowe, a nie przez nieuprawnione wartości na dowolnych przedstawieniach sum. Macierz Kroneckera korzysta z zadanej kolejności współrzędnych; wzór na rząd działa również dla odwzorowań nieodwracalnych i zerowych.
- **Kanoniczność:** zamiana, łączność, jednostka i linearyzacja wielu argumentów są udowodnione przez własność uniwersalną, w tym oddzielną kontrolę liniowości pomocniczych funkcji. Odróżniono izomorfizmy od dosłownych równości nawiasowanych konstrukcji.
- **Dual i Hom:** identyfikacja `W⊗V*≅FinRank(V,W)` działa w dowolnych wymiarach; surjektywność na całe `Hom(V,W)` została ograniczona do `dim V<∞`. Także `V*⊗W*≅(V⊗W)*` podano tylko dla skończonych wymiarów, a szerszą formułę `(V⊗W)*≅Hom(V,W*)` udowodniono bez tego ograniczenia.
- **Ilorazy i kontrakcja:** dopełnienie `H` jest pomocnicze, a izomorfizm quotientu jest indukowany przez kanoniczne `q⊗id`. Ślad wynika z `c_V(Σ T(v_i)⊗v^i)` i nie wymaga identyfikacji `V` z `V*`.

**Wynik matematyczny:** czysty audyt III, bez nowych usterek, rozdział 09 pozostaje bez zmian.

## Weryfikacja automatyczna

Wszystkie **9 rozdziałów** mają **387 unikalnych etykiet** i **154 istniejące cele odsyłaczy**; brak błędów środowisk LaTeX i naruszeń terminologii. Przeprowadzono pełny CI [44913108990](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44913108990) — **success**. Plik PDF ma **95 stron**, końcowy log kompilacji nie zawiera ostrzeżeń typu `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence` ani nierozwiązanych odsyłaczy.

Dedykowany test `tools/test_linear_algebra_tensors.py`, uruchamiany automatycznie w workflow, zaliczył: **4** przypadki wymiaru ilorazu wolnej przestrzeni przez warunki dwuliniowości, **6817** par macierzy dla rzędu i transpozycji Kroneckera, **6817** testów składania oraz **97** przypadków prostoty tensorów nad `F_2` i `F_3`. Weryfikacja testowa nie zastępuje dowodów, lecz nie wykazała żadnej rozbieżności.

## Decyzja

**Rozdział 09 stabilny i zamknięty po trzech audytach.** Niniejszy commit aktualizuje wyłącznie status książki i raport końcowy, nie zmienia tekstu matematycznego. Nowy CI po zmianie statusu należy sprawdzić osobno.
