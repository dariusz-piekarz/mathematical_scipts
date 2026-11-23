# Atlas / Lean — L1.4.1: diagnostyczny raport rozdziałowy

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Stan: testing / stabilizacja 0/3**.

## Zakres pierwszej zmiany L1.4

- Odczytowy `GET /api/lean/chapter-report?module_id=LST-01` pokazuje wersjonowany raport (schemat 1) dla istniejącego rozdziału indeksu, listę zarejestrowanych formalizacji i rozdzielne liczniki `ready/draft/stale` oraz `statement_approved`.
- Sprawdzane są bajty tekstu z indeksu wobec zapisanego SHA256. Powiązania, etykiety i kanoniczny plik TeX są weryfikowane przez istniejący `lean_catalog`. Uszkodzony indeks zeruje pozytywne deklaracje. Nieznany rozdział to HTTP 404, błędne ID to HTTP 400.
- Raport nie odczytuje plików historii uruchomień, nie uruchamia Lean, nie oblicza kosztownego fingerprintu i nie aktywuje nowego cache. `run_history_checked=false`, `dependency_fingerprint_checked=false`, `proof_status_included=false`, `certificate=false`. Stan `ready` nie oznacza `compiled` ani równoważności Lean–LaTeX.
- Moduł agregujący jest ograniczony wcześniejszym limitem katalogu (250 wpisów). Nie jest atomowym snapshotem równoczesnych zmian plików/katalogu i indeksu SQLite. Nie służy do poświadczania pochodzenia wyników wykonania Lean.

## Kryteria akceptacji i stabilizacja

1. Testy jednostkowe: gotowe i puste rozdziały, błędne identyfikatory, uszkodzony SHA i zastąpiony TeX, niedostępność historii/fingerprintu oraz brak fałszywych pozytywnych statusów.
2. Test HTTP dla rzeczywistego LST-01; brak `proof_status` i dowolnych certyfikatów.
3. Po zmianie: natywne Linux/Windows, pełne CI aplikacji z Chromium, przypięty Lean 4.26.0/Mathlib i osobny sceptyczny audyt, a następnie 2+1 na dokładnie jednym SHA. Zmiana kodu resetuje licznik.
4. Dopiero po stabilizacji tej jednostki rozważyć następny fragment: strategię cache zależności i miarodajny pomiar narzutu pełnego fingerprintu na rzeczywistym Mathlib — bez ograniczania istniejących kontroli `before/locked/after`.

**Granice:** kompilacja i kontrola aksjomatów to diagnostyka wykonania Lean. Nawet poprawne SHA, `statement_status=approved` i `compiled` nie stanowią automatycznego poświadczenia zgodności twierdzeń z LaTeX-em. Zachować `certificate=false`.

**Uwaga do planu:** w dokumentacji historycznej oznaczenie L1.3 użyto także dla pilotażu 20–30 formalizacji. Zamknięty techniczny L1.3 dotyczył odczytu lokalnych rekordów; przejście do tego podetapu architektury nie jest deklaracją ukończenia całego pilotażu.

## Wewnętrzny przegląd sceptyczny przed stabilizacją

Przegląd odkrył potencjalny wyciek przyszłych pól historii: naiwny raport przekazywał całą strukturę z katalogu, a więc przyszłe rozszerzenie katalogu mogłoby wprowadzić do raportu `proof_status` mimo `proof_status_included=false`. Zastosowano ścisłą projekcję pól i regresję z podrobionym `compiled`, logiem i `certificate=true`. Wynik 2+1 trzeba liczyć od **nowego** commita, bez zaliczania wcześniejszego CI.
