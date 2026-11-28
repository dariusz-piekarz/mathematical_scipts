# Lean 4 — katalog formalizacji (22.11.2026)

**Zakres:** strumień A — wyłącznie aplikacja. Nie zmieniano kanonicznych plików `.tex`, `application/lean/src` ani manifestu formalizacji.

## Wdrożenie

- Nowy moduł `backend/lean_catalog.py` i punkt `GET /api/lean/catalog`: aktualny spis zarejestrowanych formalizacji (limit 250), rozwiązywanie etykiet względem wskazanego rozdziału, weryfikacja rzeczywistej treści indeksu względem jego SHA256, przypiętego SHA w manifeście i bieżącego pliku źródłowego na dysku.
- `index_status` rozróżnia `ok`, `missing_document`, `corrupt_document`, `unlinked_label` i `ambiguous_label`. W każdym niepoprawnym przypadku wpis nie ma aktywnego odsyłacza i ma `formalization_status=stale`, `statement_status=needs_review`.
- Zakładka Lean ma wyszukiwarkę modułów, etykiet, identyfikatorów i twierdzeń, filtr `ready/draft/stale`, ręczne odświeżanie, licznik powiązań i możliwość otwarcia istniejącego podglądu fragmentu.
- Katalog **nie zwraca stanu kompilacji** i nie wywołuje runnera. Pełny fingerprint i historia kompilacji są sprawdzane dopiero dla konkretnego fragmentu. `ready` to wyłącznie aktualne, przypięte źródło, nie skompilowany dowód. `certificate=false`.

## Regresje

- `tests/test_lean_catalog.py`: roboczy wpis, przejście do obiektu, brak pozornego `proof_status`, zmiana treści w bazie i na dysku, uszkodzony dokument, powielona lub brakująca etykieta, brak dokumentu, limit rejestru.
- `tests/test_lean_http.py`: katalog API na rzeczywistym indeksie LST-01.
- `tests/test_lean_formalization.py`: kontrakt elementów interfejsu i odwołania do API.

**Ograniczenia:** lista pokazuje status źródła, nie odtwarzalność środowiska Lean, przebieg kompilacji, wynik `#print axioms` ani semantyczne zatwierdzenie przez niezależnego recenzenta. Test przeglądarkowy interakcji katalogu i rzeczywisty CI wymagają odrębnego sprawdzenia; nie należy przypisywać im sukcesu tylko na podstawie commitu.
