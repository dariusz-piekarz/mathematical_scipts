# Lean Formalization — lokalny pilotaż

Pierwszy etap rozwijany niezależnie od audytów LaTeX. Źródła matematyczne są tylko do odczytu; kod Lean ma odrębny rejestr w `manifest.json`.

## Zakres pilotażu
Do ręcznego mapowania źródła `LST-01` służą trzy wpisy w `manifest.json`:
- `thm:de-morgan-logic` — dwa prawa de Morgana (`LST01_DeMorgan.lean`), skompilowane w rzeczywistym CI.
- `thm:implication-laws` — obie równoważności implikacji oraz modus ponens (`LST01_ImplicationLaws.lean`).
- `thm:negated-implication-xli` — równoważność negacji implikacji (`LST01_NegatedImplication.lean`).

Dwa ostatnie pliki wymagają osobnego przebiegu CI po dodaniu. Wszystkie trzy powiązania mają status `needs_review`: `Prop` formalizuje wartości logiczne, a nie wprost składnię formuł i wszystkie funkcje wartościujące; nie wolno mylić tych dwóch poziomów.

## Co jest dostępne w aplikacji
1. Otwórz obiekt matematyczny w Explorerze; w Czytniku kliknij **Zobacz w Lean**.
2. Alternatywnie zaznacz wiersze źródłowego LaTeX i kliknij **Zaznaczenie → Lean**, albo wpisz zakres wierszy. Kod Lean jest widoczny wyłącznie, jeśli w rejestrze istnieje formalizacja powiązana z odpowiednią etykietą.
3. Odczytaj osobne statusy zgodności tłumaczenia, obecności/synchronizacji źródła i wykonania Lean. Przykładowy pilot `LST-01/thm:de-morgan-logic` pozostaje niezatwierdzonym szkicem.
4. Lokalny przycisk **Uruchom Lean** jest domyślnie zablokowany. Nie uruchamia dowolnego kodu wpisanego w przeglądarce.

## Instalacja Lean/Mathlib (lokalne środowisko zaufane)
Zainstaluj elan/Lean 4 i upewnij się, że `lake` jest dostępne w PATH. Następnie w terminalu:

```powershell
cd application/lean
lake update
lake exe cache get
lake env lean src/LST01_DeMorgan.lean
cd ..
$env:MATLIB_LEAN_RUN = "1"
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
```

`lean-toolchain` wskazuje Lean 4 `v4.26.0`, a `lakefile.toml` przypina Mathlib do commitu `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` (tag `v4.26.0`). `lake update` tworzy lokalny `lake-manifest.json`; workflow CI wykonuje je również na czystym repozytorium. **Rzeczywista kompilacja i kontrola aksjomatów pierwszego pliku `LST01_DeMorgan.lean` zakończyła się powodzeniem** w [przebiegu CI 45010519869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010519869). Nie oznacza to zatwierdzenia zgodności ze źródłem LaTeX.

**Bezpieczeństwo:** endpoint wykonania jest dla serwera uruchomionego lokalnie i pod kontrolą właściciela. Nie należy wystawiać go publicznie: Lean to program i zarejestrowany plik może wykonywać operacje IO. Timeout jest ograniczeniem operacyjnym, a nie sandboxem systemowym. Zdalny tryb wykonawczy wymaga odrębnego, izolowanego kontenera z ograniczonymi uprawnieniami, pamięcią, czasem i dostępem do sieci.

## API
- `GET /api/lean/status`
- `GET /api/lean/fragment?entity_id=LST-01%2Ftheorem%2F0001` (identyfikator zależy od faktycznego indeksu)
- `GET /api/lean/fragment?module_id=LST-01&start_line=433&end_line=438`
- `POST /api/lean/run` z body `{"formalization_id":"lst01-de-morgan"}`

Udana kompilacja daje status `compiled`, **nigdy automatycznie certyfikat zgodności oryginalnego twierdzenia**. Brak Lean, timeout, błędy lub nieznana formalizacja są jawnie raportowane. Oryginalny skrypt pozostaje kanoniczny.

## Testowanie
```powershell
cd application
python -m unittest tests.test_lean_formalization -v
```
Testy obejmują wybór obiektu i zakresu, brak formalizacji, źródło stale, ścieżki, blokadę uruchamiania i symulację subprocess. Test z atrapą procesu NIE jest prawdziwą weryfikacją twierdzenia w Lean. CI aplikacji uruchamia te testy przez zwykłe unittest discover.
