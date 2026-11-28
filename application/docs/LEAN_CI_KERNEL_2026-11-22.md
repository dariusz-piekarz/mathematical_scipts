# Lean 4 — niezależny workflow formalnej kompilacji (22 listopada 2026)

## Co zaimplementowano

**Repo:** `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.

Nowy workflow `.github/workflows/lean-formalization.yml` uruchamia się po zmianach plików `application/lean/**`, kontrolera i testów kontroli lub przy ręcznym `workflow_dispatch`; nie podłącza się do audytów rozdziałów. Projekt używa `lean-toolchain: leanprover/lean4:v4.26.0` oraz Mathlib dokładnie z commitu `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` (tag v4.26.0).

Zabezpieczenia procesu:
1. `python -m unittest tests.test_lean_ci_audit -v` — offline, nie jest to sprawdzenie Lean.
2. Instalacja `elan`, `lake update` do przygotowania brakującego `lake-manifest.json` na czystej kopii Git, następnie oficjalna `leanprover/lean-action` przypięta do commitu v1.7.1.
3. Weryfikacja `lake env lean --version`, zgodności wersji i rzeczywistego commitu checkout Mathlib.
4. `lake env lean <plik>` dla wszystkich pozycji z `application/lean/manifest.json` z kontrolą kodu powrotu, zapisem rzeczywistego logu dla każdego pliku.
5. `application/scripts/lean_ci_audit.py` wymaga dla **każdego** wykrytego twierdzenia w źródle obecności `#print axioms` i odpowiadającego mu komunikatu Lean w realnym logu; odrzuca wszystko spoza `propext`, `Classical.choice`, `Quot.sound`. `sorryAx` i nieznane aksjomaty powodują błąd. Brak logu lub brak twierdzenia nie może dać zielonego wyniku.
6. Workflow publikuje `ci_lean_logs/*.log`, `ci_lean_files.txt` i `ci_lean_report.json` jako artefakt `lean-kernel-axiom-evidence`.

Do testów narzędzia służy `application/tests/test_lean_ci_audit.py`. Nie zakłada ono zainstalowanego Lean. Lokalna baza dowodów w `application/lean/src` nie została zmieniona poza przypięciem repozytorium Mathlib w `lakefile.toml`.

## Stan walidacji na koniec ręcznej iteracji

- Pierwsze CI: parser niepoprawnie interpretował cytowane apostrofami nazwy twierdzeń. Poprawiono alternatywy nazw cytowanych i bez cudzysłowów.
- W kolejnym CI: **10/10 testów kontrolera zakończonych sukcesem**; oficjalna akcja wymagała `lake-manifest.json` przed pobraniem cache. Dodano krok `lake update` przed akcją.
- CI po tej poprawce: `https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010519869`. W momencie zapisu raportu trwa inicjalizacja projektu. **Nie potwierdzono jeszcze kompilacji Lean w tym przebiegu ani kontroli aksjomatów z prawdziwego logu**; stan należy odczytać z GitHub Actions, nie domyślać się.

## Granica certyfikacji

Wynik `compiled`/poprawne `#print axioms` dowodzi poprawnej kontroli formalnego kodu przez zadeklarowany Lean oraz braków niedopuszczalnych aksjomatów w sprawdzanych twierdzeniach, lecz **nie dowodzi tożsamości formalnego stwierdzenia z polskim LaTeX**. Semantyka `LST-01/thm:de-morgan-logic` pozostaje `needs_review`, a `certificate` ma pozostać `false` do niezależnego przeglądu.

## Kolejny krok

Po rzeczywistym przejściu CI zarchiwizować wynik jako raport pilota, rozwinąć mapowania stwierdzeń `LST-01`/`LST-02`/`LA-01` i niezależną kontrolę wierności semantycznej; nie zaznaczać raportów wygenerowanych z atrap procesu jako wyników produkcyjnych.
