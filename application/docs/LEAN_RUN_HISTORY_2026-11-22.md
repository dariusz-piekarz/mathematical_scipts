# Lean 4 — historia wyników uruchomień (iteracja 22.11.2026)

## Zmiana aplikacji
- `application/backend/lean_results.py` zapisuje **ostatni wynik rzeczywistej próby wykonania procesu Lean** do osobnego, lokalnego JSON.
- `application/backend/lean_formalization.py` zapisuje wyniki `compiled`, `failed` i `timeout` oraz odczytuje wynik dla wybranego twierdzenia przez istniejący `GET /api/lean/fragment`.
- `application/frontend/app.js` pokazuje ostatni czas wykonania, log, status lub komunikat unieważnienia po ponownym otwarciu źródła.
- `application/data/.gitignore` chroni historię lokalną przed przypadkowym dołączeniem do Git.
- `application/tests/test_lean_results.py` weryfikuje zapis/odczyt, automatyczne unieważnianie po zmianie LaTeX SHA, pliku Lean, wersji Lean/Mathlib, uszkodzone JSON, niebezpieczne ID, rotację ostatniego wyniku oraz limity logów.
- `application/tests/test_lean_formalization.py` sprawdza także integrację mechanizmu przez `run()` oraz ponowny odczyt `fragment()` po symulowanym procesie. Zmiana kodu Lean odbiera status poprzedniej kompilacji.

## Wersjonowanie i bezpieczeństwo
Domyślna lokalizacja to `application/data/lean_runs/<formalization_id>.json`; można ją lokalnie zmienić przez `MATLIB_LEAN_RESULTS_DIR`. Plik jest zapisywany atomowo przy użyciu pliku tymczasowego i `os.replace`. Źródłowa baza SQLite i `.tex` pozostają tylko do odczytu.

Każdy zapis zawiera:
1. SHA256 całego źródłowego dokumentu w indeksie SQLite,
2. SHA256 bajtów rzeczywiście wskazanego pliku `.lean`,
3. SHA256 deklarowanej konfiguracji narzędzi: `lean-toolchain`, `lakefile.toml`, opcjonalnie `lake-manifest.json`,
4. deklarowaną wersję narzędzi (z `lean-toolchain`), czas UTC, ostatni wynik procesu, szczegóły i ograniczony log.

**Unieważnianie:** jeśli jakikolwiek odcisk przestaje pasować, `GET /api/lean/fragment` zwraca `proof_status=not_run` i `previous_run_outdated=true`, nigdy starego `compiled`. Ostatni historyczny plik pozostaje na dysku. Uszkodzony zapis również nie staje się pozytywnym wynikiem.

**Interpretacja:** `compiled` oznacza wyłącznie kod zakończenia procesu `lake env lean` = 0. Nie oznacza potwierdzonej zgodności semantycznej LaTeX ↔ Lean i nie jest certyfikatem wolności od `sorry`, dodatkowych aksjomatów lub luk formalizacyjnych. `certificate=false` pozostaje bezwarunkowe.

Nie zapisujemy do historii sztucznych wyników `blocked` i `toolchain_unavailable`. Zapis lokalny nie jest kryptograficznie podpisany ani zaufanym audytem wykonania; serwer musi działać na kontrolowanym komputerze.

## Wyniki sprawdzania
- Lokalnie wykonano **8/8** testów jednostkowych modułu historii, z pozytywnym wynikiem i osobnym sprawdzeniem składni Python.
- Dodano regresje integracji backendowej; dopóki pełny CI nie skończy się poprawnie, nie oznaczać ich jako zaliczone.
- Brak wykonanego tutaj rzeczywistego `lake env lean`; wynik `compiled` w testach jest uzyskany przez atrapę procesu, co jest jawnie odróżniane od realnej weryfikacji.

## Następna iteracja
Przeprowadzić test interfejsu w rzeczywistej przeglądarce (weryfikacja ponownego otwarcia), a po zainstalowaniu Lean/Mathlib dodać oddzielny workflow sprawdzający faktyczne kompilacje i rejestrowanie standardowych aksjomatów. Rozważyć cache wielu wersji i historię prób zamiast przechowywania tylko ostatniego wyniku.
