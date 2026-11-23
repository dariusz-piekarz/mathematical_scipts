# Lean L1.1 — profil CPU prawdziwego skanowania .olean (2026-11-23)

**Strumień:** A — architektura aplikacji Atlas. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Stan wejściowy

- Poprzednia zmiana benchmarku `51e67723` otrzymała poprawne szybkie testy Linux/Windows [#45143635852](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635852), pełne testy aplikacji [#45143635752](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635752), a przypięty Lean+Mathlib i audyt aksjomatów [#45143635766](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635766) zakończyły się `completed/success`.
- Rzeczywisty pomiar po filtrze nazw (SHA `fd58593c`, [#45143070388](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143070388)): 85 022 nazw, 7 732 kandydatów .olean, 77 290 odrzuconych nazw (90,9%); brak wiarygodnego sparowanego porównania czasu przed/po na tym samym runnerze.
- Podstawowy benchmark `benchmark_lean_fingerprint.py` mierzy trzy faktyczne pełne fingerprinty. Każde odczytanie pliku pozostaje limitowane pierwotnymi zabezpieczeniami produkcyjnymi.

## Implementacja

Dodano `application/scripts/profile_lean_olean_cpu.py`:

- `profile_olean_cpu(lean_root, limit=12)` używa istniejącej walidacji wejścia benchmarku, a następnie uruchamia **dokładnie jeden** prawdziwy `compiled_artifacts_sha256(lean_root)` pod kontrolą `cProfile`.
- Zapisuje wynik SHA256, listę maksymalnie 20 funkcji posortowaną według łącznego czasu wykonywania, liczniki wywołań i wartość `certificate=false`.
- Nie korzysta z imitacji haszowania; wyjątki rzeczywistej kontroli integralności są propagowane. Nie wykonuje drugiego przejścia po katalogach ani nie zapisuje stanu formalizacji.
- Wyniki `cProfile` służą do znajdowania hotspotów, nie do porównania z bezprofilowanym `perf_counter`. Sam profiler dodaje narzut.

Uruchomienie w zaufanej kopii repozytorium:

```bash
cd application
python scripts/profile_lean_olean_cpu.py --top 12 --output lean/ci_olean_cpu_profile.json
```

## Testy i CI

- `application/tests/test_lean_olean_cpu_profile.py` porównuje prawdziwy digest przed i po profilowaniu; zapewnia dokładnie jedno produkcyjne wywołanie, brak zmian w plikach, walidację parametrów, odmowę przy błędnym źródle i przy symlinku .olean.
- Szybki workflow uruchamia testy na natywnych Linux i Windows. [#45144394316](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45144394316) zakończył się `completed/success`.
- Przypięty workflow Lean 4.26.0/Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` wywołuje profiler po rzeczywistym benchmarku, zapisując `application/lean/ci_olean_cpu_profile.json` do artefaktów workflow.
- W chwili dopisania dokumentacji nie odnotowano jeszcze zakończonego pozytywnie CI całego nowego przebiegu profilera; nie nazywać L1.1 zamkniętym do czasu sprawdzenia.

## Kolejny punkt kontrolny

1. Zweryfikować pełny nowy przebieg CI Lean/Mathlib, opublikowany JSON i kompletną listę hotspotów.
2. Sprawdzić regresje Windows i realną kompilację; zachować odniesienie do konkretnego SHA.
3. Dalsze optymalizacje podejmować na podstawie hotspotów i równoważności fingerprintu, a nie wyłącznie czasu.
4. Bez zmian dla `certificate=false` bez rzeczywistej, aktualnej kompilacji i niezależnej kontroli semantycznej przekładu LaTeX.
