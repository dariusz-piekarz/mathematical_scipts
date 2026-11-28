# AA-40 — audyt II (stabilizacyjny)

**Rozdział:** „Całkowitość i twierdzenia o ideałach pierwszych”.
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.
**Status merytoryczny:** stabilny po audycie II; **zero zmian w źródle** względem audytu I.

## Kontrola matematyczna

1. Kryterium wyznacznikowe całkowitości: poprawna równoważność z istnieniem skończenie generowanego modułu zawierającego jednostkę i stabilnego na mnożenie przez dany element; nie wymaga dziedzin całkowitości.
2. Domknięcie elementów całkowitych na działania i przechodniość całkowitości: poprawne wykorzystanie skończonych podalgebr generowanych przez współczynniki jednego równania monicznego.
3. Skończoność modułowa rozszerzenia: jeśli algebra jest generowana przez skończenie wiele elementów całkowitych, istnieje jawna skończona rodzina jednomianów generująca ją jako moduł; implikacja odwrotna korzysta z lematu wyznacznikowego.
4. Twierdzenie *lying over*: prawidłowa lokalizacja przy ustalonym ideale pierwszym i użycie lematu o przeciwobrazach ideałów maksymalnych. Niezerowość lokalizowanego pierścienia sprawdzona.
5. Twierdzenie *going up*: powtarzane zastosowanie *lying over* do rozszerzenia ilorazowego; ścisłość łańcucha wynika z różnych kontrakcji.
6. Nieporównywalność: skrócenie przez niezerowy element w dziedzinie ilorazowej i minimalność stopnia równania monicznego.
7. Skończone włókna: dla `B` generowanego przez `m` elementów nad `A`, algebra włókna `B⊗_A κ(p)` ma wymiar co najwyżej `m`; wszystkie jej ideały pierwsze są maksymalne. Chińskie twierdzenie o resztach ogranicza liczbę ideałów do `m`, a *lying over* zapewnia ich istnienie. Przypadki niezerowego nilradikału nie zmieniają dowodu.
8. Wymiar w rozszerzeniu całkowitym: nierówności przez *going up* oraz kontrakcję i nieporównywalność, także dla wymiaru nieskończonego.
9. `dim K[X_1,…,X_n]=n`: dolne oszacowanie przez łańcuch ideałów współrzędnych; górne przez trójkątną monizację niezerowego `f∈p_1`, całkowitość ilorazu i indukcję po `n`. Bez używania tego twierdzenia jako założenia we wcześniejszych dowodach.
10. Przykłady `Z[i]`: dla `p=2`, `T²+1=(T+1)²` i `(2)=(1+i)²`; `p=3` jest nierozkładalne, `p=5` rozszczepia się na dwa różne ideały. Sprawdzono rozróżnienie liczby ideałów od ich krotności.
11. Krzywa ostrzowa `K[t²,t³]⊂K[t]`: poprawne równanie moniczne, rozkład modułu, obliczenie jądra homomorfizmu, ideału maksymalnego i wymiaru.

## Kontrole automatyczne

- **Regresja z audytu I:** 126/126 PASS.
- **Nowy, niezależnie przygotowany zestaw:** 248/248 PASS.
- **Łącznie:** **374/374 PASS**. Powtórzono obie grupy testów jako moduły `tools.tests.*` w układzie katalogów zgodnym z repozytorium: **374/374 PASS**.
- Niezależny zestaw bada współczynniki i faktoryzację wielomianów nad `F_p`, włókna algebr monogenicznych z wielokrotnymi czynnikami, idempotenty i ideały w iloczynach pierścieni, semigrupę wykładników `K[t²,t³]`, stosowalność twierdzeń oraz zagnieżdżenie środowisk LaTeX.
- Kontrola struktury źródła: **23/23 etykiet unikatowych, 11 dowodów, 9 przykładów**.
- Wszystkie sześć zewnętrznych celów odsyłaczy istnieje w aktualnych rozdziałach AA-38 i AA-39.
- Źródło po audycie I i II: **identyczne bajtowo**, SHA-256 `7bcde5700095674872ff8cf1a77c62f6252432a386e557267aed70ba6a3c288f`.

## Kompilacja i kontrola wizualna

- Ponownie wykonano `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error` na samodzielnym pliku głównym.
- **PDF: 7 stron A4**; **0 ostrzeżeń, 0 przepełnień, 0 nierozwiązanych odsyłaczy** w kompilacji kontrolnej.
- Renderowano komplet stron i skontrolowano wizualnie — brak kolizji i ucięć.
- Plik kompilacyjny posiada kontrolne definicje sześciu odsyłaczy do zweryfikowanych rozdziałów; w ramach pełnej kompilacji książki muszą być sprawdzone rzeczywiste odsyłacze.

## Zależności

- AA-38: `aa:ch:noether-normalization`, `aa:lem:noether-monic`, `aa:tw:noether-normalization`, `aa:wn:noether-dimension` — wszystkie znalezione.
- AA-39: `aa:tw:krull-localization-primes`, `aa:tw:krull-pid` — oba znalezione.

## Zdalny CI — diagnostyka i naprawa

- Pierwszy workflow AA-01–AA-40 (run `45066102397`) zakończył się błędem w ogólnym kroku `Run repository tool tests`. Log pokazał pięć błędów `FileNotFoundError`: niezależny test AA-40 wskazywał lokalną ścieżkę `/mnt/data/AA-40-audyt-II-zrodlo.tex`, niedostępną w środowisku GitHub. Pozostałe kontrole testowe nie wskazały błędu matematycznego w AA-40.
- Poprawiono wyłącznie `tools/tests/test_abstract_algebra_ch40_independent.py`: domyślne źródło jest odszukiwane relatywnie względem katalogu repozytorium; lokalny wariant pozostaje możliwy. Skrót rozdziału LaTeX nie uległ zmianie.
- Ponowiono lokalnie cały zestaw 374 testów w układzie `tools.tests.*` **bez** `AA40_SOURCE`: **374/374 PASS**.
- Poprawkę testu opublikowano w commicie `0ed9eaea3dd947c83e6ab076c7eece2e855428a5`.
- **Ponowny zdalny przebieg CI:** [AA-01–AA-40 / run 45066500032](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066500032) — **completed / success**. Oddzielnie potwierdzono sukces ogólnych testów repozytorium, dedykowanych 374 testów AA-40, kompilacji pełnej książki AA-01–AA-40 oraz kroku `Verify PDF and references (no undefined refs)`.

## Zapis i publikacja

- Źródło i pełny pakiet archiwalny znajdują się w `/Biblioteka matematyczna/iteracje/`.
- AA-40 nadaje się do dołączenia do `chapters/pl/abstract_algebra/`, `books/pl/abstract_algebra.tex`, `catalog/books.json` oraz workflow `abstract-algebra-chapter.yml`.
- **GitHub Actions:** status rzeczywistych testów i pełnej kompilacji książki należy odnotować osobno po odczycie przebiegu CI; lokalna kompilacja rozdziału nie stanowi dowodu sukcesu CI pełnej książki.

**Wynik: AA-40 STABILNY po audycie II; bez zmian źródła; pełny zdalny CI AA-01–AA-40 zakończony sukcesem.**
