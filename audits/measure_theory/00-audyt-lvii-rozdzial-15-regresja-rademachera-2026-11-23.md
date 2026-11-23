# Audyt LVII (57) — rozdział 15: regresja Rademachera i stan bramki CI

Data: 2026-11-23.
Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Gałąź: `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowej).
Rozdział źródłowy: `chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex`, blob `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab` — bez zmian.

## Niezależnie wykryty problem testu

W przypadku `test_rademacher_cancellation_on_dyadic_blocks` sprawdzano zerowanie sumy znaków tylko na **pierwszym** przedziale diadycznym danego rzędu i na całym odcinku. Nie wykrywało to wszystkich możliwych błędów rozkładu znaków na innych podprzedziałach. Tymczasem argument matematyczny opiera się na anulowaniu całki funkcji Rademachera na **każdym** ustalonym przedziale diadycznym, gdy rząd funkcji jest dostatecznie duży.

## Wykonana poprawka

Commit: `c6a10a16debe0db589fcce450ef1dc0297cf2b59`.
Zmieniono tylko plik `tools/tests/test_measure_theory_ch15_li_gate.py` (blob po zmianie `0c4030893db1da52b6a60321c73b3d0d254322bf`).
Test sprawdza wszystkie podprzedziały każdego rzędu `m=0,...,n` dla `n=1,...,9`, a nie wyłącznie pierwszy. Dodano celowo uszkodzone dane (odwrócony znak w końcowym przedziale), na których kontrola musi wykryć niezerową sumę.

Zachowano dokładnie osiem metod testowych w pakiecie. Zmiana dotyczy testu, **nie** dowodu ani źródła matematycznego.

## Rzeczywiste wykonanie

Przeprowadzono w lokalnym Pythonie `unittest` dla nowej metody w tym samym brzmieniu: **1/1 PASS**; łączna liczba sprawdzonych bloków diadycznych: **2035**. Dla dziewięciu poziomów wykonano po jednej skutecznej kontroli negatywnej. Jest to test własności skończonych funkcji schodkowych reprezentujących znaki, nie dowód ogólnej zbieżności słabej.

Po zapisaniu plik testowy ponownie odczytano z GitHub: `sha=0c4030893db1da52b6a60321c73b3d0d254322bf`, liczba metod `test_*=8`, pętla po wszystkich blokach i kontrola negatywna obecne. Zweryfikowano, że nazwa zmienionego testu znajduje się w `paths` istniejącego workflow `.github/workflows/measure-theory-ch15-lii-gate.yml` (blob `4c3884d9ca0773e28239ca61f84a5dd8b4b8aead`).

## Wynik CI i ograniczenia

Odczyt z GitHub connector dla commitu `c6a10a16debe0db589fcce450ef1dc0297cf2b59`: `get_commit_combined_status` zwrócił pustą listę statusów legacy, a `fetch_commit_workflow_runs` zwrócił pustą listę przebiegów filtrowanych przez konektor (API ogranicza odczyt do przebiegów określonej klasy pull requestów). Nie jest to dowód sukcesu ani porażki workflow na `push`. Publiczny widok akcji oraz GitHub API nie były dostępne w używanym narzędziu web, a lokalne `git ls-remote` nadal kończyło się błędem rozwiązywania nazwy `github.com`.

**Werdykt LVII:**
- Zidentyfikowana luka w regresji Rademachera — **naprawiona**.
- Nowa metoda testowa — **PASS (1/1, 2035 bloków)**.
- Stan matematyczny niezmienionego rozdziału 15 — dotychczasowy **PASS**.
- Pełne 8/8 w repozytorium, dwa joby GitHub CI i realna kompilacja PDF — **NIEPOTWIERDZONE**.
- Stabilizacja rozdziału 15 — **OTWARTA TECHNICZNIE**; audyt rozdziału 16 wstrzymany do potwierdzenia tej bramki.

## Następna iteracja

Przez narzędzie z dostępem do listy uruchomień GitHub Actions odczytać najnowszy run `Measure theory chapter 15 LII stabilization` na gałęzi `biblioteka-matematyczna-iteracja-6`. Sprawdzić jego identyfikator, SHA commitu, wyniki jobów `tests` i `pdf`, pełne 8/8 `unittest`, końcowe logi LaTeX, oba PDF-y i podglądy stron. Nie zamykać stabilizacji bez poświadczenia tych elementów. W przypadku rzeczywistego błędu naprawić jego przyczynę, a nie kolejną hipotetyczną.
