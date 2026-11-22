# Algebra liniowa — ponowna sekwencja audytów rozdziałów 12–32

**Utworzono:** 22 listopada 2026
**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Automatyzacja:** `6b02b88391748191bc804355ba103bf6` (cogodzinna, Europe/Warsaw)
**Zakres:** 12–32; wszystkie rozdziały muszą przejść nową sekwencję, również jeśli miały historyczny status stabilny.
**Zasada stabilności:** dwie następujące po sobie czyste kontrole tego samego bloba po ostatniej zmianie oraz zielona walidacja CI.

## Stan wykonania

- Bieżący rozdział: **13**.
- Ostatni sprawdzony blob (rozdział 13, po poprawce): **cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af**.
- Liczba kolejnych czystych audytów od ostatniej poprawki (bieżący rozdział 13): **1**.
- Kolejne działanie: **wykonać audyt 03 rozdziału 13 na tym samym blobie**. Iteracja 02 była czysta; licznik wynosi 1/2.
- Historyczne audyty, w tym ręczne audyty rozdziałów 13–15 z 22 listopada, pozostają ważnymi źródłami, ale **nie są automatycznie liczone** jako wykonanie nowego przebiegu.

## Tabela statusów

| Rozdział | Stan nowej sekwencji | Czyste kontrole po ostatniej zmianie | Ostatni SHA |
|---|---|---:|---|
| 12 | STABILNY; iteracje 01 i 02 czyste, CI success | 2 | `ded0c69dc298d00842d4009073e2444e1037952a` |
| 13 | OTWARTY; iteracja 02 czysta, CI success dla bloba; wymagany audyt 03 | 1 | `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af` |
| 14 | W kolejce | 0 | — |
| 15 | W kolejce | 0 | — |
| 16 | W kolejce | 0 | — |
| 17 | W kolejce | 0 | — |
| 18 | W kolejce | 0 | — |
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
