# Audyt LIX (59) — rozdział 15, weryfikowalne statusy obu zadań GitHub Actions

Data: 2026-11-23.
Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Istniejąca gałąź: `biblioteka-matematyczna-iteracja-6` — bez tworzenia nowej.
Źródło rozdziału: `chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex`, blob `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab` (niezmieniony).
Punkt wyjścia: audyt LVIII (58), 8 regresji rozdziału 15 oraz 4 testy integralności całej 31-rozdziałowej książki.

## Diagnoza problemu obserwowalności

Dotychczasowe zapytania do `get_commit_combined_status` zwracały pustą listę. **To nie oznacza pozytywnego ani negatywnego przebiegu GitHub Actions**, ponieważ GitHub Actions zwykle publikuje wyniki przede wszystkim jako `check runs`, natomiast używany interfejs konektora odczytuje klasyczne commit statuses. Alternatywny interfejs `fetch_commit_workflow_runs` filtruje wyniki do określonych uruchomień powiązanych z pull requestami i nie zapewnia pełnej listy przebiegów `push`. Publiczny podgląd strony Actions i punktu końcowego API nie był dostępny w narzędziu sieciowym; lokalny kontener nadal nie ma DNS dla github.com.

## Rzeczywista zmiana

Commit `d4bd9b94a3dc02ae10d2c085e71a649d679e0559` dodaje do **istniejącego** workflow `.github/workflows/measure-theory-ch15-lii-gate.yml` końcowe zadanie `report-statuses`, pozostawiając bez zmian dwa główne zadania `tests` i `pdf`.

- `report-statuses` ma zależność `needs: [tests, pdf]` i `if: always()`; jego jedyną rolą jest publikowanie wyniku po zakończeniu obu jobów.
- Job uzyskuje wyłącznie wymaganą dodatkową możliwość `statuses: write`. Token dostarczany jest z wbudowanego `github.token`, bez wpisywania poświadczeń do repozytorium.
- Dwa odrębne konteksty klasycznych statusów GitHub: `measure-theory/ch15-regressions` (8 testów rozdziału + 4 integralności) i `measure-theory/ch15-pdf` (książka + izolowany rozdział, kontrola odsyłaczy, podglądy).
- Status `success` jest publikowany **wyłącznie**, gdy odpowiedni job GitHub Actions ma zakończenie `success`. Zakończenie `failure` przekłada się na `failure`, a `cancelled`, `skipped` i stan nieznany na `error`. W każdym statusie umieszczany jest URL konkretnego przebiegu `actions/runs/<run_id>`.
- Publikacja odbywa się przez standardowy GitHub REST `POST /repos/{owner}/{repo}/statuses/{sha}` z poprawnym nagłówkiem autoryzacji; nieudane zapisy są zgłaszane błędem zadania, a nie ignorowane.

Po zapisaniu pobrano workflow ponownie przez konektor i potwierdzono SHA bloba `19d71922d8126698b972b93e477c9aa57ee8b090`, obecność obydwu kontekstów i ustawienia `statuses: write`. W lokalnym Pythonie niezależnie sprawdzono mapowanie pięciu wariantów zakończenia (5/5 PASS). To sprawdza mechanikę mapowania, **nie potwierdza wywołania API ani rezultatu workflow**.

## Stan bramki

Dla commitu `d4bd9b94a3dc02ae10d2c085e71a649d679e0559` bezpośrednio po zapisaniu nadal uzyskano `statuses: []`, `workflow_runs: []` w ograniczonym interfejsie; brak danych nie jest sukcesem ani porażką.

**Rozdział 15: matematyka — wcześniejszy PASS, bez zmian w źródle.**
**Testy integralności całego tomu — przygotowane i podłączone do workflow; pełne wykonanie 12/12 niepotwierdzone.**
**Kompilacje obu PDF i inspekcja wizualna — niepotwierdzone.**
**Bramka stabilizacji — OTWARTA TECHNICZNIE.**

Następna iteracja: odczytać oba nowe konteksty dla commitu zawierającego tę zmianę lub późniejszego commitu z przebiegiem tej bramki. Gdy obydwa będą `success`, sprawdzić ich `target_url`, logi i artefakty. Jeżeli statusy nie pojawią się, nie raportować zaliczenia; przeanalizować rzeczywistą przyczynę na podstawie dostępnego identyfikatora przebiegu lub bieżących logów. Do rozdziału 16 przejść wyłącznie po pełnej stabilizacji.
