# Algebra liniowa — ponowna sekwencja audytów rozdziałów 12–32

**Utworzono:** 22 listopada 2026
**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Automatyzacja:** `6b02b88391748191bc804355ba103bf6` (cogodzinna, Europe/Warsaw)
**Zakres:** 12–32; wszystkie rozdziały muszą przejść nową sekwencję, również jeśli miały historyczny status stabilny.
**Zasada stabilności:** dwie następujące po sobie czyste kontrole tego samego bloba po ostatniej zmianie oraz zielona walidacja CI.

## Stan wykonania

- Bieżący rozdział: **30**.
- Ostatni zamknięty blob (rozdział 29): **55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd**.
- Liczba czystych audytów bieżącego rozdziału 30: **0/2**; oddzielny końcowy audyt: **niewykonany**. Rozdział 29 zakończony: 2/2 oraz dodatkowy czysty audyt końcowy 03.
- Kolejne działanie: **rozdział 30 — audyt 01**. Rozdział 29 zamknięto po dwóch czystych audytach 01–02, osobnym sceptycznym audycie końcowym 03, zielonym CI 45023597804 dla tego samego bloba oraz rzeczywistej kontroli 8-stronicowego PDF wyodrębnionego z książki. Rozdział 28 pozostaje zamknięty. Rozszerzenie LA-32 o transformatę Penrose’a pozostaje w planie.
- Historyczne audyty, w tym ręczne audyty rozdziałów 13–15 z 22 listopada, pozostają ważnymi źródłami, ale **nie są automatycznie liczone** jako wykonanie nowego przebiegu.

## Tabela statusów

| Rozdział | Stan nowej sekwencji | Czyste kontrole po ostatniej zmianie | Ostatni SHA |
|---|---|---:|---|
| 12 | STABILNY; iteracje 01 i 02 czyste, CI success | 2 | `ded0c69dc298d00842d4009073e2444e1037952a` |
| 13 | STABILNY; iteracje 02 i 03 czyste, CI success | 2 | `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af` |
| 14 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `8216c60505324854e2339928bb9be562724e1db2` |
| 15 | STABILNY; audyty 02 i 03 czyste po poprawce, dedykowane CI success | 2 | `5a17f877bf3639cebc33ca95c202aca4498bd6c9` |
| 16 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a` |
| 17 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `05b93309d0e444f1c3fcbe3489cfd98a0f02846f` |
| 18 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `ef815633cf3a1f795d912c510fbc8575f21e464d` |
| 19 | STABILNY; audyty 03 i 04 czyste, CI success | 2 | `dd289d5c86452910a89d60ddfbcc558ef6d5be85` |
| 20 | STABILNY; audyty 01 i 02 czyste, CI success | 2 | `8d585c7f4c208990ad5f82222cc47f586144c138` |
| 21 | STABILNY; audyty 01 i 02 czyste, CI success | 2 | `6527ae1a6daca48717e6a5f5e83958271abb16f5` |
| 22 | STABILNY; audyty 03 i 04 czyste po poprawce, CI success | 2 | `dfa3d790bfed4c92c66642ea626a6213bc06ad3f` |
| 23 | STABILNY; audyty 01 i 02 czyste, CI success | 2 | `bbd199baed1ee2c1a88843aad9fbfd0eac665d22` |
| 24 | STABILNY; audyty 01 i 02 czyste, CI success | 2 | `92106feafce495e11f051279733cb34e9d9bed64` |
| 25 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `6b57fc1b64ef560b98e17f89322c688160376ccf` |
| 26 | STABILNY; audyty 02 i 03 czyste po poprawce, CI success | 2 | `80032eef1e0e5de817821d97de96aaf86c960e03` |
| 27 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success | 2 | `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a` |
| 28 | STABILNY po dodatkowym audycie; 04 korekta, 05–06 czyste, CI success | 2 | `b9507aa2db7eda554446248996e7c0ae241d4e73` |
| 29 | STABILNY; audyty 01 i 02 czyste oraz dodatkowy końcowy 03 czysty, CI success i PDF obejrzany | 3 (2+1) | `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd` |
| 30 | OTWARTY; audyt 01 do wykonania | 0 | — |
| 31 | W kolejce | 0 | — |
| 32 | W kolejce | 0 | — |

## Instrukcja dla każdej iteracji

Przed pracą odczytaj aktualne źródło, raporty, AGENTS.md i globalne standardy. Przeprowadź **jedną rzeczywistą kontrolę jednego rozdziału**; zapisz osobny raport w `audits/linear_algebra/re_audit_from_ch12/`, podaj SHA i sprawdzony wynik CI. W razie poprawki źródła wyzeruj licznik czystych audytów; po dwóch kolejnych czystych i zielonym CI zamknij rozdział i przejdź do następnego. Po zamknięciu 32 zapisz raport końcowy i nie wracaj do 12.

## Poprzednia iteracja — 2026-11-22

- Rozdział: **12**; status: **OTWARTY**, czyste kontrole po ostatniej zmianie: **1/2**.
- SHA źródła: `ded0c69dc298d00842d4009073e2444e1037952a`; plik .tex niezmieniony.
- Raport: [12_iteration_01_2026-11-22.md](re_audit_from_ch12/12_iteration_01_2026-11-22.md), commit [55422dab](https://github.com/dariusz-piekarz/mathematical_scipts/commit/55422dab3f2eca2a38371a782128b7927d26f4a7).
- Wynik: matematyka, dowody, przykłady, terminologia, struktura LaTeX — **czyste**; 1332 niezależne przypadki obliczeniowe PASS; [CI 45013564279](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013564279) — **success**, dla gałęzi z identycznym blobem źródła.
- **Uzasadnienie braku zamknięcia:** dopiero jedna nowa czysta kontrola. Następny etap: drugi audyt rozdziału 12, bez automatycznego zaliczania audytów historycznych.

## Ostatnia rzeczywista iteracja — 2026-11-22 (02)

- Rozdział **12**: **STABILNY**, 2/2 czyste audyty tego samego bloba `ded0c69dc298d00842d4009073e2444e1037952a`.
- Raport: [12_iteration_02_2026-11-22.md](re_audit_from_ch12/12_iteration_02_2026-11-22.md); commit [9a45a6c](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9a45a6c36bd20e8d69544313ad91bc26d7e6543a).
- Uzasadnienie zamknięcia: dwa kolejne niezależne czyste audyty bez modyfikacji źródła oraz [CI 45013564279](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013564279) completed/success dla commitu z tym samym blobem rozdziału.
- Nie wykonano nowej kompilacji PDF ani nowych testów Python w iteracji 02.
- Następny etap: **rozdział 13**, iteracja 01. Ostatni sprawdzony SHA w nagłówku dotyczy zamkniętego rozdziału 12; SHA rozdziału 13 zostanie zapisany podczas jego pierwszego audytu.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 13, audyt 01)

- Źródło wejściowe `6a14ebe0879846b12c48b2c172b940cc8314388c`, po poprawce `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af`.
- Poprawiono niegramatyczne objaśnienie sprzężonej transpozycji; matematyka nie wymagała zmian.
- Raport: [13_iteration_01_2026-11-22.md](re_audit_from_ch12/13_iteration_01_2026-11-22.md), commit [19e13dc3](https://github.com/dariusz-piekarz/mathematical_scipts/commit/19e13dc3c19e5a8ebedfb5cb021ff8def1bf7a9f).
- **Stan 13: otwarty, 0/2** czystych kontroli po ostatniej zmianie. Zielony wcześniejszy CI nie potwierdza nowego bloba. Następny: audyt 02 rozdziału 13.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 13, audyt 02)

- Rozdział 13: czysta kontrola **1/2** bloba `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af`, bez zmiany źródła.
- Raport: [13_iteration_02_2026-11-22.md](re_audit_from_ch12/13_iteration_02_2026-11-22.md), commit [53a273aa](https://github.com/dariusz-piekarz/mathematical_scipts/commit/53a273aa3fdae171de0e8e435bb4909a9208cc95).
- [CI 45015993405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45015993405): success dla commitu `b709ed3b18b9add604ddfbe404d4ca6379088224`, zawierającego ten sam blob.
- Następny krok: audyt 03 rozdziału 13. Nie deklarowano nowej kompilacji PDF ani testów numerycznych.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 13, audyt 03)

- Rozdział 13: **STABILNY, 2/2**, ten sam blob `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af` co w audycie 02, bez zmian źródła.
- Raport: [13_iteration_03_2026-11-22.md](re_audit_from_ch12/13_iteration_03_2026-11-22.md), commit [4a254b69](https://github.com/dariusz-piekarz/mathematical_scipts/commit/4a254b6960b70dee1e02c3681d42950bd9f76b16).
- [CI 45015993405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45015993405): completed/success dla commitu z tym samym blobem.
- Bez nowej kompilacji PDF i testów numerycznych w audycie 03. Następny: rozdział **14**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 14, audyt 01)

- Rozdział 14: czysty audyt **1/2** źródła `8216c60505324854e2339928bb9be562724e1db2`, bez edycji.
- Raport: [14_iteration_01_2026-11-22.md](re_audit_from_ch12/14_iteration_01_2026-11-22.md), commit [79498221](https://github.com/dariusz-piekarz/mathematical_scipts/commit/794982212afbb41af6004ff34eae0271c5fc71ec).
- Na gałęzi widoczne są przebiegi CI o różnych wynikach; pełnego wymaganego zielonego CI dla bloba jeszcze nie potwierdzono.
- Następny: rozdział 14, audyt 02.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 14, audyt 02)

- Rozdział **14: STABILNY (2/2)**; blob `8216c60505324854e2339928bb9be562724e1db2` niezmieniony względem audytu 01.
- Raport: [14_iteration_02_2026-11-22.md](re_audit_from_ch12/14_iteration_02_2026-11-22.md), commit [d686d9b0](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d686d9b0a8950873cf2ea7abc341db90a017bdbf).
- [Linear algebra chapter validation 45016577027](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45016577027): completed/success, commit `4045ae10c6093a34c2d5ad5b4d9001af041fb6bd`, ten sam blob rozdziału 14.
- Następny: rozdział **15**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 15, audyt 01)

- Poprawiono błędne sformułowanie „sprzężenie transpozycję” na „transpozycję ze sprzężeniem zespolonym”. Commit [f1e95b7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/f1e95b7f32a8691d7e10d3c87e9420ca7a7a563c).
- Raport: [15_iteration_01_2026-11-22.md](re_audit_from_ch12/15_iteration_01_2026-11-22.md), commit [0f7742a](https://github.com/dariusz-piekarz/mathematical_scipts/commit/0f7742ae6cac062bed4a3faad8e204c3249dfcc5).
- Źródło po edycji: `5a17f877bf3639cebc33ca95c202aca4498bd6c9`. Czyste kontrole: **0/2**. CI dla nowego bloba jeszcze nie potwierdzono.
- Następny: rozdział 15, audyt 02.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 15, audyt 02)

- Rozdział 15: czysta kontrola **1/2** na blobie `5a17f877bf3639cebc33ca95c202aca4498bd6c9`, bez edycji.
- Raport: [15_iteration_02_2026-11-22.md](re_audit_from_ch12/15_iteration_02_2026-11-22.md), commit [278ecee4](https://github.com/dariusz-piekarz/mathematical_scipts/commit/278ecee4268f6de2255e8319f61b353cf23952c4).
- Dedykowane CI: [run 45017069172](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017069172), completed/success dla commitu z tym samym blobem.
- Następny: rozdział 15, audyt 03.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 15, audyt 03)

- Rozdział **15: STABILNY (2/2)**; audyty 02 i 03 czyste na niezmienionym blobie `5a17f877bf3639cebc33ca95c202aca4498bd6c9`.
- Raport: [15_iteration_03_2026-11-22.md](re_audit_from_ch12/15_iteration_03_2026-11-22.md), commit [95653ba3](https://github.com/dariusz-piekarz/mathematical_scipts/commit/95653ba327ee8e3b8e250f6f38086fa334b40baf).
- Dedykowane CI [run 45017069172](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017069172): completed/success, commit `f1e95b7f32a8691d7e10d3c87e9420ca7a7a563c`, potwierdzony ten sam blob rozdziału 15.
- Następny: rozdział **16**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 16, audyt 01)

- Rozdział **16: OTWARTY (1/2)**; czysty audyt na blobie `4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a`; źródła nie edytowano.
- Raport: [16_iteration_01_2026-11-22.md](re_audit_from_ch12/16_iteration_01_2026-11-22.md), commit [a203852d](https://github.com/dariusz-piekarz/mathematical_scipts/commit/a203852d354ea15bf82f4abe49d54de6a039228f).
- Dedykowane CI: [run 45017945078](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017945078), completed/success, commit `786d00d9ea55799c17a27107144facb8cc40c2ca` zawierający ten sam blob rozdziału 16.
- Następny: rozdział **16**, audyt 02.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 16, audyt 02)

- Rozdział **16: STABILNY (2/2)**, niezmieniony blob `4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a`.
- Raport: [16_iteration_02_2026-11-22.md](re_audit_from_ch12/16_iteration_02_2026-11-22.md), commit [23c959e7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/23c959e7b1892409475d4530e996bc18e21e76cf).
- CI: [run 45017945078](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017945078), completed/success na commicie zawierającym ten sam blob.
- Następny etap: rozdział **17**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 17, audyt 01)

- Rozdział **17: OTWARTY (1/2)**; czysty audyt na blobie `05b93309d0e444f1c3fcbe3489cfd98a0f02846f`; źródła nie zmieniono.
- Raport: [17_iteration_01_2026-11-22.md](re_audit_from_ch12/17_iteration_01_2026-11-22.md), commit [65ef8c8](https://github.com/dariusz-piekarz/mathematical_scipts/commit/65ef8c8607f71c43adc0e916e9bafd6ec4a2d1a3).
- Dedykowana walidacja CI: [run 45018486327](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45018486327), completed/success na commicie `3a5f271108ef508fb261356b56a46cc528e15332` z tym samym blobem rozdziału 17.
- Następny: rozdział **17**, audyt 02.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 17, audyt 02)

- Rozdział **17: STABILNY (2/2)**; audyty 01 i 02 czyste na niezmienionym blobie `05b93309d0e444f1c3fcbe3489cfd98a0f02846f`.
- Raport: [17_iteration_02_2026-11-22.md](re_audit_from_ch12/17_iteration_02_2026-11-22.md), commit [25177a3](https://github.com/dariusz-piekarz/mathematical_scipts/commit/25177a3e6d597ca37d2b59b6fbf31f6414c3d16f).
- Dedykowane CI: [run 45018486327](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45018486327), completed/success, commit `3a5f271108ef508fb261356b56a46cc528e15332` zawiera ten sam blob rozdziału 17.
- Następny: rozdział **18**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 18, audyt 01)

- Rozdział **18: OTWARTY (1/2)**; czysty audyt na blobie `ef815633cf3a1f795d912c510fbc8575f21e464d`, źródła nie edytowano.
- Raport: [18_iteration_01_2026-11-22.md](re_audit_from_ch12/18_iteration_01_2026-11-22.md), commit [bb36660](https://github.com/dariusz-piekarz/mathematical_scipts/commit/bb36660e18968bd062649c65a4c5e9dbdccf3036).
- Dedykowane CI [run 45018755189](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45018755189): completed/success na commicie `6d859ac49fbdcff1389888e6109337ffb22934e2` z tym samym blobem rozdziału 18.
- Następny: rozdział **18**, audyt 02.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 18, audyt 02)

- Rozdział **18: STABILNY (2/2)**; audyty 01 i 02 czyste na niezmienionym blobie `ef815633cf3a1f795d912c510fbc8575f21e464d`.
- Raport: [18_iteration_02_2026-11-22.md](re_audit_from_ch12/18_iteration_02_2026-11-22.md), commit [4cc28c0](https://github.com/dariusz-piekarz/mathematical_scipts/commit/4cc28c00819826a84fdbbf0a72356622936e7df5).
- Dedykowane CI: [run 45018755189](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45018755189), completed/success dla commitu `6d859ac49fbdcff1389888e6109337ffb22934e2` z tym samym blobem.
- Następny: rozdział **19**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 19, audyt 01)

- **Wynik: korekta**, nie czysty audyt. Niespójny zakres twierdzenia o postaci Frobeniusa dla n=0 został poprawiony, [commit 9276ae7](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9276ae75687489d7ef591df87ad2142c60a5795b).
- Aktualny blob źródła: `ac826f20aa3462f01e0a051cef72631407fbc0dd`. Licznik kolejnych czystych kontroli po zmianie: **0/2**.
- Raport: [19_iteration_01_2026-11-22.md](re_audit_from_ch12/19_iteration_01_2026-11-22.md), [commit d2deb1d](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d2deb1d05894278e5145392e369fc157e8c32478).
- Dotychczasowe dedykowane CI success [run 45019153860](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45019153860) dotyczy poprzedniego bloba, **nie zalicza** poprawionej wersji. Po poprawce uruchomiono [run 45020142844](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020142844); w chwili audytu był w toku.
- Następny: rozdział **19**, audyt 02 oraz kontrola CI na poprawionym blobie.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 19, audyt 02)

- Raport [19_iteration_02_2026-11-22.md](re_audit_from_ch12/19_iteration_02_2026-11-22.md); skorygowano błędne indeksy bloku Smitha i fleksję `oba wielomiany`, commit [b52330c](https://github.com/dariusz-piekarz/mathematical_scipts/commit/b52330c2ca5497b4612cf320f49f1898e527729b).
- Blob po poprawkach: `dd289d5c86452910a89d60ddfbcc558ef6d5be85`. Audyt nieczysty, licznik **0/2** po ostatniej edycji. 1484 niezależne testy numeryczne PASS; 20 etykiet unikalnych, 14 odsyłaczy poprawnych.
- [Dedykowane CI 45020307205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020307205): completed/success na commicie `b52330c2ca5497b4612cf320f49f1898e527729b` z tym samym blobem.
- Następny: audyt 03 rozdziału 19.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 19, audyt 03)

- Rozdział **19: OTWARTY (1/2)**, niezależny czysty audyt po poprawkach audytu 02 na blobie `dd289d5c86452910a89d60ddfbcc558ef6d5be85`, bez zmiany źródła.
- Raport: [19_iteration_03_2026-11-22.md](re_audit_from_ch12/19_iteration_03_2026-11-22.md), [commit c6b1450](https://github.com/dariusz-piekarz/mathematical_scipts/commit/c6b1450433a735a79b4d0516a7f599cc830ba39d).
- Dedykowane CI: [run 45020307205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020307205), completed/success na commicie `b52330c2ca5497b4612cf320f49f1898e527729b` z identycznym blobem.
- Następny: rozdział **19**, audyt 04; jeśli czysty na niezmienionym blobie, zamknąć jako stabilny i przejść do 20.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 19, audyt 04)

- Rozdział **19: STABILNY (2/2)**, niezmieniony blob `dd289d5c86452910a89d60ddfbcc558ef6d5be85`. Audyty 03 i 04 czyste na tym samym źródle po ostatniej poprawce.
- Raport: [19_iteration_04_2026-11-22.md](re_audit_from_ch12/19_iteration_04_2026-11-22.md); 1730 lokalnych przypadków PASS, w tym niezależne operacje unimodularne i bloki stopnia 4; 20 etykiet bez duplikatów, 14 poprawnych odsyłaczy. Nie edytowano źródła w audytach 03–04.
- Dedykowane [CI 45020307205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020307205) completed/success dla commitu `b52330c2ca5497b4612cf320f49f1898e527729b`, ten sam blob rozdziału 19; 43 kroki joba, dwa warunkowo pominięte.
- Następny: rozdział **20**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 20, audyty 01 i 02)

- Rozdział **20: STABILNY (2/2)**, niezmieniony blob `8d585c7f4c208990ad5f82222cc47f586144c138`. Oba nowe audyty czyste na tym samym źródle, bez jego modyfikacji.
- Raporty: [20_iteration_01_2026-11-22.md](re_audit_from_ch12/20_iteration_01_2026-11-22.md), [20_iteration_02_2026-11-22.md](re_audit_from_ch12/20_iteration_02_2026-11-22.md); 1385 przypadków PASS w audycie 01 oraz 1628 PASS w audycie 02, wszystkie zgodne. 22 unikalne etykiety, 23 poprawne odsyłacze.
- [Dedykowane CI 45020307205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020307205): completed/success na commicie zawierającym identyczny blob rozdziału 20.
- Następny: rozdział **21**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 21, audyty 01 i 02)

- Rozdział **21: STABILNY (2/2)**. Dwa nowe, samodzielne czyste audyty na tym samym blobie `6527ae1a6daca48717e6a5f5e83958271abb16f5`, bez zmiany źródła.
- Raporty: [21_iteration_01_2026-11-22.md](re_audit_from_ch12/21_iteration_01_2026-11-22.md), [21_iteration_02_2026-11-22.md](re_audit_from_ch12/21_iteration_02_2026-11-22.md). Audyt 01: 1368 PASS; audyt 02: 1708 PASS, w tym 340 innych próbek. Testy rozwiązywały AX=XA i niezależnie sprawdzały wzory z dwóch klasyfikacji.
- Dedykowane [CI 45020307205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020307205): completed/success na commicie z identycznym źródłem.
- Następny: rozdział **22**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 22, audyty 01–04)

- Audyt 01 równolegle sprawdzał stary blob `1e38cbc7e7fc2613a2914a8c92c4e9bf92005920`; po nim wykryto błąd zakresu deklaracji we wstępie i w [audycie 02](re_audit_from_ch12/22_iteration_02_2026-11-22.md) wykonano korektę, commit [b6d3687](https://github.com/dariusz-piekarz/mathematical_scipts/commit/b6d3687237d6a08b31ad4da5b18f00370d6577b5). Licznik po zmianie wyzerowano.
- [Audyt 03](re_audit_from_ch12/22_iteration_03_2026-11-22.md) oraz [audyt 04](re_audit_from_ch12/22_iteration_04_2026-11-22.md) są czyste (2/2) na niezmienionym blobie `dfa3d790bfed4c92c66642ea626a6213bc06ad3f`. Sprawdzono m.in. 887 kontroli Sylvestera i przykładów, 48 zespolonych przypadków Lapunowa, 4 kontrole całkowe i 342 testy bloków Jordana; brak niezgodności. Źródło 936 wierszy, 25 etykiet i 25 poprawnych odsyłaczy.
- [CI 45021237405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021237405) completed/success dla commitu `b6d3687237d6a08b31ad4da5b18f00370d6577b5`, potwierdzono identyczny blob źródła rozdziału 22. Rozdział **STABILNY**; następny 23.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 23, audyty 01 i 02)

- Rozdział **23: STABILNY (2/2)**, źródło `bbd199baed1ee2c1a88843aad9fbfd0eac665d22` niezmienione między czystymi audytami 01 i 02.
- Raporty: [23_iteration_01_2026-11-22.md](re_audit_from_ch12/23_iteration_01_2026-11-22.md) oraz [23_iteration_02_2026-11-22.md](re_audit_from_ch12/23_iteration_02_2026-11-22.md). Weryfikacja niezależna: 1494 testy widma i odwracalności operatora Steina nad ciałami skończonymi, 64 zespolone przypadki równania Steina, 64 tożsamości energii; wszystkie PASS. Struktura źródła: 965 wierszy, 25 unikalnych etykiet, 12 istniejących odsyłaczy.
- [CI 45021237405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021237405) completed/success dla commitu zawierającego identyczny blob. Następny: rozdział 24.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 24, audyty 01 i 02)

- Rozdział **24: STABILNY (2/2)**, niezmieniony blob `92106feafce495e11f051279733cb34e9d9bed64` po dwóch kolejnych samodzielnych czystych kontrolach.
- Raporty [24_iteration_01_2026-11-22.md](re_audit_from_ch12/24_iteration_01_2026-11-22.md) i [24_iteration_02_2026-11-22.md](re_audit_from_ch12/24_iteration_02_2026-11-22.md). Wykonano 80 zespolonych przypadków DARE/CARE, 112 niezależnych skończenohoryzontowych LQR, 96 nowych porównań DARE/CARE z równaniami Lapunowa; wszystkie PASS. Źródło 1452 wiersze, 26 unikalnych etykiet, 31 poprawnych odsyłaczy.
- [CI 45021237405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021237405) completed/success dla commitu zawierającego identyczny blob. Następny: rozdział **25**, audyt 01.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 25, audyt 01)

- Raport [25_iteration_01_2026-11-22.md](re_audit_from_ch12/25_iteration_01_2026-11-22.md). Rozdział **25: OTWARTY (1/2 czystych audytów)**. Źródło `6b57fc1b64ef560b98e17f89322c688160376ccf` niezmienione; kontrola założeń, Kalmana, PBH, graminów, rozkładu Kalmana, stabilizowalności, wykrywalności i energii nie wykazała błędów.
- Nowe, lokalnie wykonane niezależne testy `/mnt/data/la25_reaudit_independent.py`: **793** pełne układy wymiaru 2 nad F2/F3 (Kalman, PBH, obserwowalność), **400** dokładnych przypadków rozmieszczenia biegunów, **37** losowych testów graminów i minimalnej energii, razem **1230 PASS, 0 FAIL**. 47 unikalnych etykiet, 30 poprawnych odsyłaczy, 108 domkniętych środowisk.
- [CI 45021237405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021237405): completed/success dla commitu o identycznym blobie. Nowszy run 45021828182 był in_progress w czasie sprawdzenia.
- Następny: rozdział **25**, audyt **02** na tym samym blobie. Nie przechodzić jeszcze do 26.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 25, audyt 02)

- Rozdział **25: STABILNY (2/2)** na źródle `6b57fc1b64ef560b98e17f89322c688160376ccf`, niezmienionym od audytu 01. Raport [25_iteration_02_2026-11-22.md](re_audit_from_ch12/25_iteration_02_2026-11-22.md).
- Nowy lokalny test `/mnt/data/la25_reaudit_02_tests.py`: **889** kontroli Kalman/PBH/obserwowalność, **39** porównań graminu ciągłego i energii, **120** przykładów wymiernych sprzężenia zwrotnego, **1048 PASS**. LaTeX: 47 unikalnych etykiet, 30 poprawnych odsyłaczy, 108 par środowisk. Bez zmian źródła.
- Dedykowane CI [45021237405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021237405) i [45021828182](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021828182) completed/success z identycznym blobem. Następny: rozdział 26.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 26, audyty 01–03)

- W nowym [audycie 01](re_audit_from_ch12/26_iteration_01_2026-11-22.md) wykryto i poprawiono usterkę językową „w współczynnikach” → „we współczynnikach”, commit [5a7317df](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5a7317df50f2ddd986d424a9ed3b0f9ea8592b4f). Audyt 01 **nieczysty, 0/2** po zmianie.
- [Audyt 02](re_audit_from_ch12/26_iteration_02_2026-11-22.md) i [audyt 03](re_audit_from_ch12/26_iteration_03_2026-11-22.md) to dwa kolejne **czyste** przeglądy poprawionego bloba `80032eef1e0e5de817821d97de96aaf86c960e03` (2/2). Testy niezależne: 254 przypadki DARE/CARE/półokreślony koszt przed korektą, 196 testów porównań z Lapunowem po korekcie, 143 dodatkowe kontrole trójstanowe i monotoniczność rekurencji — wszystkie PASS. Weryfikacja LaTeX: 38 etykiet, 45 odsyłaczy, 56 par środowisk. Nie wykonano nowej wizualnej inspekcji PDF.
- Dedykowane [CI 45022565397](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022565397) dla commitu zawierającego dokładnie ten nowy blob było **in_progress** w chwili odczytu (kompilacja PDF). **Nie zamykać rozdziału ani nie przechodzić do 27 przed potwierdzeniem completed/success dla właściwego bloba**.

## Uzupełnienie końcowe — 2026-11-22 (zamknięcie rozdziału 26)

- [GitHub Actions 45022565397](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022565397) i [45022589412](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022589412) są już **completed/success**. Sprawdzono, że commit `5a7317df50f2ddd986d424a9ed3b0f9ea8592b4f` zawiera dokładnie aktualny blob rozdziału 26 `80032eef1e0e5de817821d97de96aaf86c960e03`.
- Po spełnieniu 2/2 czystych audytów i CI rozdział **26: STABILNY**; aktywny jest **27**. Nie dodano nowego materiału, jedyna edycja to językowa korekta w dowodzie DRE.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 27, audyty 01 i 02)

- Rozdział **27: STABILNY (2/2)**. Źródło `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a` niezmienione między dwiema kolejnymi niezależnymi czystymi kontrolami.
- Raporty: [27_iteration_01_2026-11-22.md](re_audit_from_ch12/27_iteration_01_2026-11-22.md), [27_iteration_02_2026-11-22.md](re_audit_from_ch12/27_iteration_02_2026-11-22.md). Nowe testy: 720 przypadków Hankela nad F2/F3/F5, 65 dyskretnych zrównoważeń, 85 przypadków najmniejszych kwadratów, 135 sprawdzeń parametrów Markowa i podobieństwa, 135 rang Hankela, 77 ciągłych zrównoważeń — **1217 PASS**. LaTeX: 32 unikalne etykiety, 32 poprawne odsyłacze i 57 domkniętych środowisk.
- [CI 45022565397](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022565397) completed/success dla identycznego bloba. Następny rozdział w nowej sekwencji: **28**.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 28, audyty 01–03)

- Audyt 01 rozdziału **28** ujawnił i skorygował warunek zerowego stanu początkowego w przykładzie nieminimalnej realizacji z ukrytym niestabilnym stanem. Commit [e1d6e803](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e1d6e803b410e77ed3ddc519d482863e2db83159), nowy blob `a2afdd2b20b2694d70bdbee6ad6a0f8c42b9aea8`; audyt 01 nieczysty, reset do 0/2. [Raport](re_audit_from_ch12/28_iteration_01_2026-11-22.md).
- [Audyt 02](re_audit_from_ch12/28_iteration_02_2026-11-22.md) i [audyt 03](re_audit_from_ch12/28_iteration_03_2026-11-22.md) to dwie kolejne czyste kontrole po korekcie. Wykonano **1205+520+450=2175** niezależnych testów w trzech oddzielnych skryptach Python, wszystkie PASS. Kontrola strukturalna: 664 linie, 36 unikalnych etykiet, 31 poprawnych odsyłaczy i 38 par środowisk LaTeX.
- [CI 45023213569](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023213569) **completed/success** dla commitu zawierającego identyczny blob rozdziału 28. **Rozdział 28: STABILNY (2/2)**; aktywny rozdział **29**.
- **Zatwierdzony dodatek Penrose’a do LA-32**: [la32_penrose_extension_plan.md](la32_penrose_extension_plan.md). Dopisać przy audycie i opracowaniu 32: lokalną skalarną transformatę Penrose’a, konturową formułę z jednorodnością `−2`, sprawdzenie operatora falowego, przykład rezydualny i precyzyjne granice twierdzenia kohomologicznego. Nie dublować już istniejącej incydencji, kwadryki i fibracji.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 29, audyt 01)

- **Stan: OTWARTY, 1/2**, następnie obowiązkowy dodatkowy audyt końcowy. Przeczytano pełne 743 wiersze źródła i sprawdzono atlas, rzutowania, styczne, wiązki, orientację, przestrzenie ilorazowe, osadzenie Plückera, równanie dla Gr₂(R⁴), odwzorowanie Gaussa, przykłady i warunki brzegowe. Nie znaleziono usterek wymagających korekty źródła.
- SHA źródła: `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd` (bez edycji). Raport: [29_iteration_01_2026-11-22.md](re_audit_from_ch12/29_iteration_01_2026-11-22.md); [commit 993e4e1](https://github.com/dariusz-piekarz/mathematical_scipts/commit/993e4e1238bbdd21297bfc00d254e3729a38f0e1).
- [CI 45023597804](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023597804): **completed/success**, SHA commit `edcd2f934d724636816d14b15aa8280e3273cdaf`, zweryfikowany identyczny blob LA-29. Nie przeprowadzono osobnego renderingu PDF LA-29: dostępny artefakt „current chapter” dotyczył LA-32. Nie wykonano nowych testów obliczeniowych.
- Następny krok: **LA-29 audyt 02**, bez przechodzenia do LA-30. Zasada z 22.11.2026 wymaga po spełnieniu 2/2 i CI jeszcze osobnego czystego audytu kontrolnego tego samego etapu.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 29, audyt 02)

- Bieżący rozdział: **29**, status **OTWARTY**, czyste kontrole od ostatniej poprawki: **2/2**, oddzielny audyt końcowy: **NIE**.
- Sprawdzony blob: `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd` (743 wiersze), bez zmiany źródła.
- Raport: [29_iteration_02_2026-11-22.md](re_audit_from_ch12/29_iteration_02_2026-11-22.md), commit [6f9e36f](https://github.com/dariusz-piekarz/mathematical_scipts/commit/6f9e36f623b2e6465f81634f53c7ecbb8fdcc473).
- Rzeczywiście wykonano **6561** kontroli tożsamości Plückera w deterministycznym modelu całkowitoliczbowym: **0 naruszeń**; 19 etykiet, 20 poprawnie rozpoznanych odsyłaczy, brak błędów struktury środowisk i delimiterów.
- [CI 45023597804](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023597804) **completed/success**, bezpośrednio zweryfikowano identyczny blob rozdziału w commicie CI `edcd2f934d724636816d14b15aa8280e3273cdaf`.
- Nie wykonano nowego renderingu PDF 29; układ rysunków nie ma niezależnej walidacji wizualnej.
- **Uzasadnienie braku zamknięcia:** nadrzędny wymóg oddzielnego pełnego audytu końcowego po osiągnięciu 2/2. **Następny etap: rozdział 29, audyt 03 końcowy**, a nie 30.

## Ostatnia rzeczywista iteracja — 2026-11-22 (rozdział 29, końcowy audyt 03)

- **LA-29 STABILNY I ZAMKNIĘTY**: 2/2 wcześniejsze czyste audyty oraz oddzielny pełny audyt końcowy 03, także czysty, bez zmiany bloba `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd`.
- Raport: [29_iteration_03_2026-11-22.md](re_audit_from_ch12/29_iteration_03_2026-11-22.md), [commit 35ecbd5](https://github.com/dariusz-piekarz/mathematical_scipts/commit/35ecbd522a28a16845a5c61a92185b8e905f6266).
- Matematyka, terminologia, etykiety i LaTeX: bez nowych usterek. Wykonano 14641 przypadków regresji Plückera, 0 błędów.
- [CI 45023597804](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023597804) completed/success, potwierdzono identyczny blob. Pobierano rzeczywisty artefakt pełnej książki i wizualnie przejrzano wszystkie **8 stron** rozdziału 29 (strony fizyczne 285–292) z dwoma rysunkami, bez zauważonych kolizji. To wcześniejszy CI, nie nowy run.
- **Uzasadnienie zamknięcia:** dwa czyste audyty po ostatniej zmianie + dodatkowy niezależny czysty audyt końcowy + zielony CI zgodny z SHA + kontrola PDF. **Następny etap:** LA-30 audyt 01, 0/2. Nie rozpoczynać LA-29 ponownie bez konkretnej nowej przyczyny.

## Audyt kontrolny dla pewności — 2026-11-22 (rozdział 28, audyty 04–06)

- Na wyraźną prośbę użytkownika ponownie szczegółowo zweryfikowano **LA-28**, niezależnie od trwającej kolejki, której bieżącym rozdziałem pozostaje ten sam rozdział wskazany w nagłówku powyżej.
- [Audyt 04](re_audit_from_ch12/28_iteration_04_2026-11-22.md) wykrył dwie usterki redakcyjne: nieprecyzyjną hipotezę skończonego nośnika pojedynczego `u_k` (zamiast ciągu `(u_k)_{k≥0}`) i brak przecinka przed „podstawiając”. Poprawiono źródło w [commicie 9c4229fa](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9c4229fa1cf7f686654345ee9140d7b8e9bbee7a), nowy blob `b9507aa2db7eda554446248996e7c0ae241d4e73`. **Audyt 04 nieczysty, reset 0/2**.
- [Audyt 05](re_audit_from_ch12/28_iteration_05_2026-11-22.md) i [audyt 06](re_audit_from_ch12/28_iteration_06_2026-11-22.md): **dwie kolejne czyste kontrole bloba `b9507aa2db7eda554446248996e7c0ae241d4e73` (2/2)**. Wykonano dodatkowo **783 + 690 = 1473** rzeczywiste kontrole obliczeniowe w dwóch zestawach Python, wszystkie PASS, 0 FAIL. Źródło: 664 wiersze, 36 etykiet, 31 poprawnych odsyłaczy, 38 par środowisk. Nie wykonywano osobnej inspekcji graficznej PDF.
- [Dedykowane CI 45038348657](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45038348657) **completed/success**, commit `9c4229fa1cf7f686654345ee9140d7b8e9bbee7a` zawiera dokładnie finalny blob. **Rozdział 28 ponownie STABILNY**, wcześniejsza korekta nie zmienia matematyki. Rozdział 29 i aktualna kolejka nie zostały cofnięte.
