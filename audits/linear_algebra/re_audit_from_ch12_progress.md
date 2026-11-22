# Algebra liniowa — ponowna sekwencja audytów rozdziałów 12–32

**Utworzono:** 22 listopada 2026
**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Automatyzacja:** `6b02b88391748191bc804355ba103bf6` (cogodzinna, Europe/Warsaw)
**Zakres:** 12–32; wszystkie rozdziały muszą przejść nową sekwencję, również jeśli miały historyczny status stabilny.
**Zasada stabilności:** dwie następujące po sobie czyste kontrole tego samego bloba po ostatniej zmianie oraz zielona walidacja CI.

## Stan wykonania

- Bieżący rozdział: **12**.
- Ostatni sprawdzony blob: **ded0c69dc298d00842d4009073e2444e1037952a**.
- Liczba kolejnych czystych audytów od ostatniej poprawki: **1**.
- Kolejne działanie: **wykonać drugi niezależny audyt aktualnego bloba rozdziału 12**, zweryfikować CI i zamknąć tylko jeśli audyt będzie czysty; potem przejść do 13.
- Historyczne audyty, w tym ręczne audyty rozdziałów 13–15 z 22 listopada, pozostają ważnymi źródłami, ale **nie są automatycznie liczone** jako wykonanie nowego przebiegu.

## Tabela statusów

| Rozdział | Stan nowej sekwencji | Czyste kontrole po ostatniej zmianie | Ostatni SHA |
|---|---|---:|---|
| 12 | Otwarty; nowa iteracja 01 czysta, wymagany audyt 02 i zielone CI | 1 | `ded0c69dc298d00842d4009073e2444e1037952a` |
| 13 | W kolejce | 0 | — |
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

## Ostatnia rzeczywista iteracja — 2026-11-22

- Rozdział: **12**; status: **OTWARTY**, czyste kontrole po ostatniej zmianie: **1/2**.
- SHA źródła: `ded0c69dc298d00842d4009073e2444e1037952a`; plik .tex niezmieniony.
- Raport: [12_iteration_01_2026-11-22.md](re_audit_from_ch12/12_iteration_01_2026-11-22.md), commit [55422dab](https://github.com/dariusz-piekarz/mathematical_scipts/commit/55422dab3f2eca2a38371a782128b7927d26f4a7).
- Wynik: matematyka, dowody, przykłady, terminologia, struktura LaTeX — **czyste**; 1332 niezależne przypadki obliczeniowe PASS; [CI 45013564279](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013564279) — **success**, dla gałęzi z identycznym blobem źródła.
- **Uzasadnienie braku zamknięcia:** dopiero jedna nowa czysta kontrola. Następny etap: drugi audyt rozdziału 12, bez automatycznego zaliczania audytów historycznych.
