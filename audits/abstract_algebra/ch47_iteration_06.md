# AA-47 — audyt VI: podłączenie dodatkowych regresji do GitHub Actions

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Status:** NIE STABILNY — oczekiwanie na rzeczywiste zakończenie CI oraz przegląd PDF.

## Zweryfikowany stan przed zmianą

Odczytano istniejący workflow `.github/workflows/abstract-algebra-chapter.yml` i stwierdzono, że **dwa pierwotne zestawy AA-47 były już uruchamiane**:
- `python -m unittest tools.tests.test_abstract_algebra_ch47 -v`;
- `python -m unittest tools.tests.test_abstract_algebra_ch47_independent -v`.

Workflow zawiera również kompilację całej książki `abstract_algebra.tex`, kontrolę logu i archiwizację PDF. Nie wolno zatem twierdzić, że te zestawy nie były podłączone.

## Zmiana produkcyjna

Zmodyfikowano workflow, dodając:
1. `audits/abstract_algebra/test_aa47_audit05.py` do filtra ścieżek wyzwalających `push`;
2. osobny krok `python audits/abstract_algebra/test_aa47_audit05.py` bezpośrednio przed kompilacją LaTeX.

**Commit zmiany workflow:** `3ce83e8ab852a02ca1ccd2a1b2940e034673523a`.

Po zapisie ponownie odczytano workflow z gałęzi i zweryfikowano pięć warunków statycznych: filtr ścieżki, nowy krok, zachowanie dwóch dotychczasowych zestawów AA-47 oraz zachowanie kompilacji PDF — **5/5 PASS (kontrola tekstu workflow, nie wykonania CI)**.

## Pozostałe bramki

- Potwierdzić faktyczny wynik GitHub Actions dla commita z nowym krokiem.
- Odczytać log kompilacji i obejrzeć każdą nową stronę AA-47 w wygenerowanym PDF.
- Dopiero po tych kontrolach przeprowadzić niezależny audyt stabilizacyjny.

**Werdykt:** nowy zestaw testów jest w konfiguracji CI; wykonanie workflow i jego wynik nie zostały poświadczone. AA-47 pozostaje NIE STABILNY; AA-48 nieotwarty.
