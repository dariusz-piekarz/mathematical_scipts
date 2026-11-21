# Audyt GitHub / CI — odsyłacze i przyszłe rozdziały

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Zweryfikowany commit funkcjonalny:** `4a2d84da3b8938171e1067c794b1edb1abffe871`  
**Workflow:** [GitHub Actions 44919311372](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44919311372) — **SUCCESS**, wszystkie kroki, w tym testy przeglądarkowe Chromium.

## Naprawa

Wdrożono mechanizm rygorystycznego rozdzielenia **znanych, nadal nierozwiązanych** odsyłaczy od nowych błędów indeksu. Zmiany:

1. `application/config/pending_reference_baseline.json` — dokładna lista `(rozdział źródłowy, etykieta docelowa)`, bez domniemania istnienia celu;
2. `application/scripts/triage_unresolved_refs.py` — audyt pochodzenia i jawne liczniki `documented_pending_occurrences`, `unclassified_unresolved_occurrences`; pole `known_pending`, powód braku i opcja `--fail-on-unclassified`;
3. `application/tests/test_triage_unresolved_refs.py` — testy regresyjne źródło+cel, cel o tej samej nazwie w innym rozdziale, niedozwolona niejednoznaczność, przyszła kompletność DG i kod wyjścia CLI;
4. `.github/workflows/mathematical-library-app.yml` — po testach przeglądarkowych obowiązkowy krok odrzucający nowe nieudokumentowane braki.

## Rzeczywiste wyniki na zbudowanym indeksie

| Pozycja | Liczba |
|---|---:|
| Zaindeksowane rozdziały | 378 |
| Nierozwiązane wystąpienia odsyłaczy | 21 |
| Celowo udokumentowane odsyłacze do przyszłych rozdziałów AA/LST | 8 |
| Odsyłacze DG oczekujące kontroli przy niepełnym imporcie | 13 |
| **Nowe lub nieklasyfikowane braki / niejednoznaczności** | **0** |
| Nazwy etykiet mające wielu właścicieli | 306 |
| Niejednoznaczne odwołania w indeksie | 0 |
| Rozdziały DG obecne / planowane | 20 / 36 |

Wszystkie 21 wystąpień nadal mają status `missing` i `requires_mathematical_review=true`. Nie zostały przemianowane, usunięte ani uznane za rozwiązane przez sam wpis na listę. Dla DG istnieje 16 brakujących rozdziałów; dopóki nie zostaną zaimportowane, nie należy domniemywać właściwych etykiet. Kiedy import DG-01–DG-36 będzie kompletny, dotychczasowe wyjątki DG tracą ważność automatycznie: nadal brakujące odsyłacze zaczną powodować błąd CI.

Liczba 306 kolizji nazw jest globalna (między skryptami), ale w tym przebiegu żaden konkretny odsyłacz nie był niejednoznacznie rozwiązany. To zadanie porządkowania przestrzeni nazw, **nie** dowód 306 błędów matematycznych. Nie zmieniano arbitralnie etykiet bez porównania ich treści i pochodzenia.

## Wyniki testów

GitHub Actions 44919311372 potwierdził `success` dla: budowania bazy SQLite, audytu pochodzenia etykiet, triage, kontroli importu DG, pełnych testów jednostkowych, testów Chromium (Explorer, reader, graf, workspace), końcowego rygorystycznego audytu nowych odsyłaczy oraz archiwizacji raportów.

**Decyzja:** mechanizm zabezpieczenia jest stabilny. Nie należy scalać `main` ani masowo zmieniać etykiet podczas równoległych audytów. Dalsze etapy: uzupełnianie rzeczywistych przyszłych rozdziałów, audyt 306 potencjalnie kolidujących nazw według pochodzenia oraz osobne kompilacje stabilizowanych tomów.
