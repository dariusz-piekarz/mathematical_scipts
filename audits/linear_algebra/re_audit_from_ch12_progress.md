# Algebra liniowa — ponowna sekwencja audytów rozdziałów 12–32

**Utworzono:** 22 listopada 2026
**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Automatyzacja:** `6b02b88391748191bc804355ba103bf6` (cogodzinna, Europe/Warsaw)
**Zakres:** 12–32; wszystkie rozdziały muszą przejść nową sekwencję, również jeśli miały historyczny status stabilny.
**Zasada stabilności:** dwie następujące po sobie czyste kontrole tego samego bloba po ostatniej zmianie oraz zielona walidacja CI.

## Stan wykonania

- Bieżący rozdział: **18**.
- Ostatni zamknięty blob (rozdział 17): **05b93309d0e444f1c3fcbe3489cfd98a0f02846f**.
- Liczba kolejnych czystych audytów (bieżący rozdział 18): **1**.
- Kolejne działanie: **wykonać audyt 02 rozdziału 18** na niezmienionym blobie `ef815633cf3a1f795d912c510fbc8575f21e464d`. Audyt 01 czysty, dedykowane CI success.
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
| 18 | OTWARTY; audyt 01 czysty, dedykowane CI success | 1 | `ef815633cf3a1f795d912c510fbc8575f21e464d` |
| 19 | W kolejce | 0 | — |
| 20 | W kolejce | 0 | — |
| 21 | W kolejce | 0 | — |
| 22 | W kolejce | 0 | — |
| 23 | W kolejce | 0 | — |
| 24 | W kolejce | 0 | — |
| 25 | W kolejce | 0 | — |
| 26 | W kolejce | 0 | — |
| 27 | W kolejce | 0 | — |
| 28 | W kolejce | 0 | — |
| 29 | W kolejce | 0 | — |
| 30 | W kolejce | 0 | — |
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
