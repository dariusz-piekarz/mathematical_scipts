# Weryfikacja rzeczywistej kompilacji międzytomowej — tomy I–IV

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Przebieg GitHub Actions:** [44746470218](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44746470218)  
**Status:** **SUCCESS**, zakończony, potwierdzony w logu i artefaktach.

## Zakres

Test uruchomiono na prawdziwych plikach:
- `books/pl/probability_volume_i.tex`,
- `books/pl/probability_volume_ii.tex`,
- `books/pl/probability_volume_iii.tex`,
- `books/pl/probability_volume_iv.tex`.

Workflow `.github/workflows/probability-xr-hyper.yml` wykonuje:

1. Instalację zależności TeX (w tym `lmodern`, wymagane do pełnej kompilacji).
2. Kompilację wszystkich czterech tomów za pomocą `latexmk -pdf`, generując prawdziwe pliki `.aux` i `.pdf`.
3. Ponowną kompilację tomów po wytworzeniu `.aux` innych tomów, aby `xr-hyper` zaimportował prefiksowane etykiety.
4. Dodatkową kompilację dla stabilizacji odsyłaczy.
5. Walidację `application/scripts/verify_probability_aux.py`: istnienie czterech PDF, AUX i LOG, importy prefiksowe, obecność oryginalnych celów w źródłowych AUX, brak nieznanych prefiksowanych cytowań.
6. Publikację artefaktu `probability-xr-hyper-logs-aux` (ID `14634000776`) z logami, czterema plikami `.aux` i raportem.

## Wynik liczbowy

| Tom | Oryginalne etykiety w jego AUX | Zweryfikowane cytowania prefiksowane |
|---|---:|---:|
| I | 32 | 13 |
| II | 46 | 10 |
| III | 257 | 10 |
| IV | 357 | 39 |
| **Razem** | **692** | **72** |

Wynik walidatora: `passed = true`, `failures = []`.

## Ważne ograniczenia

- Test dotyczy **czterech tomów prawdopodobieństwa**, nie wszystkich 355 rozdziałów Biblioteki.
- Prawidłowość kompilacji i rozstrzygania etykiet **nie oznacza audytu matematycznego dowodów**, typografii każdej strony ani braku wszystkich ostrzeżeń innych niż sprawdzone błędy odsyłaczy.
- Pełne PDF nie zostały dołączone do artefaktu GitHub; artefakt zawiera AUX, LOG, FLS i podsumowanie. Ich istnienie podczas testów zostało zweryfikowane.
- Poprzedni przebieg `44745766244` nie przeszedł przez brak `lmodern.sty` w runnerze; poprawkę środowiska zastosowano i powtórny przebieg **zakończył się sukcesem**.
- W plikach kanonicznych nie zmieniono `\label`, `\ref`, `\eqref`, nie scalano treści i nie zmieniano gałęzi `main`.

## Pozostałe zadania

Osobny raport `AUDYT_19_PO_REJESTRZE_2026-11-20.md` obejmuje 19 pozostałych pozycji statycznego indeksu (2 cele w `shared/pl`, 12 celów poza importem, 1 możliwa niezgodność lokalna, 1 niezweryfikowane powiązanie między skryptami i 3 odsyłacze do matematycznie niewłaściwego wariantu twierdzenia). Te 19 pozycji nie należą do sprawdzonych tutaj 72 odsyłaczy prefiksowanych czterech tomów.

Następny etap po audytach pozostałych 16 rozdziałów geometrii różniczkowej: ponowne zbudowanie indeksu i aktualizacja statusów; niezależnie rozszerzenie indeksowania o źródłowe etykiety plików `shared/pl` w `\input`.