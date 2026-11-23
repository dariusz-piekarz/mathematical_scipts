# Lean Formalization — lokalny pilotaż

Pierwszy etap rozwijany niezależnie od audytów LaTeX. Źródła matematyczne są tylko do odczytu; kod Lean ma odrębny rejestr w `manifest.json`.

## Zakres pilotażu

Manifest zawiera obecnie **9 powiązań** (5 z `LST-01` i 4 z `LST-02`). Pierwotne trzy mapowania logiczne mają źródło w `LST-01`. Głównym plikiem Lean dla LST-01 pokazywanym w panelu jest `src/LST01_SyntaxValuations.lean`: definiuje **indukcyjną składnię formuł** (litera, negacja, koniunkcja, alternatywa, implikacja, równoważność), funkcję `eval` dla wartościowania `Nat → Bool`, równoważność formuł przez wszystkie wartościowania oraz tautologię.

- `thm:de-morgan-logic` — oba prawa de Morgana dla formuł.
- `thm:implication-laws` — rozwinięcie implikacji, przeciwstawienie i modus ponens.
- `thm:negated-implication-xli` — negacja implikacji.
- Ponadto w tym pliku: formalna tablica prawdy dla równoważności oraz poprawne traktowanie dwóch wystąpień tej samej litery.

Pliki `LST01_DeMorgan.lean`, `LST01_ImplicationLaws.lean` i `LST01_NegatedImplication.lean` pozostają jako krótkie opracowania na poziomie `Prop`. Nowy CI kompiluje **każdy** plik `.lean` z `src/` i kontroluje raporty `#print axioms` dla wszystkich ich twierdzeń, także gdy dany plik nie jest głównym mapowaniem w panelu.

Mapowanie `Prop` to tylko semantyka pojedynczego wartościowania, natomiast nowe mapowanie `Formula` oddaje budowę formuły i kwantyfikację po wszystkich wartościowaniach. **Historycznie pierwsze trzy powiązania `LST-01` uzyskały `statement_status=approved` po osobnym audycie sześciu tez.** Później rejestr rozszerzono do pięciu mapowań LST-01 obejmujących łącznie **10 deklaracji** zapisanych w grupach `lean_theorems`. Wszystkie pięć mapowań jest w rejestrze oznaczonych `approved` względem dokładnego SHA256 źródła `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`; kontrole digestu nie stanowią automatycznego poświadczenia niezależnej recenzji ani równoważności semantycznej. Zmiana źródła unieważnia zatwierdzenie; sama kompilacja nie jest certyfikatem zgodności. Pełna analiza: [audyt semantyczny](../docs/LEAN_SEMANTIC_AUDIT_LST01_2026-11-22.md).

## Co jest dostępne w aplikacji
1. Otwórz obiekt matematyczny w Explorerze; w Czytniku kliknij **Zobacz w Lean**.
2. Alternatywnie zaznacz wiersze źródłowego LaTeX i kliknij **Zaznaczenie → Lean**, albo wpisz zakres wierszy. Kod Lean jest widoczny wyłącznie, jeśli w rejestrze istnieje formalizacja powiązana z odpowiednią etykietą.
3. Odczytaj osobne statusy zgodności tłumaczenia, obecności/synchronizacji źródła i wykonania Lean. Powiązania `LST-01` są zatwierdzone semantycznie wyłącznie dla przypiętej wersji dokumentu; sprawdzenie wykonania Lean pozostaje odrębnym statusem.
4. Lokalny przycisk **Uruchom Lean** jest domyślnie zablokowany. Nie uruchamia dowolnego kodu wpisanego w przeglądarce.

## Instalacja Lean/Mathlib (lokalne środowisko zaufane)
Zainstaluj elan/Lean 4 i upewnij się, że `lake` jest dostępne w PATH. Następnie w terminalu:

```powershell
cd application/lean
lake update
lake exe cache get
lake env lean src/LST01_SyntaxValuations.lean
cd ..
$env:MATLIB_LEAN_RUN = "1"
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
```

`lean-toolchain` wskazuje Lean 4 `v4.26.0`, a `lakefile.toml` przypina Mathlib do commitu `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` (tag `v4.26.0`). `lake update` tworzy lokalny `lake-manifest.json`; workflow CI wykonuje je również na czystym repozytorium. **Historyczny** [CI #45011738363](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011738363) kompilował cztery pliki i kontrolował 14 deklaracji. **Aktualny** [CI Lean #45206502490](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206502490) `completed/success` na `163c8f64` kompilował pięć plików (w tym LST-02), **25 twierdzeń**, `axiom_check=passed`, Lean 4.26.0 i przypięty Mathlib; weryfikacja semantyczna pozostaje odrębną procedurą.

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

## LST-02: pierwsza partia pilotażu (2026-11-23)

Nowy plik `src/LST02_Quantifiers.lean` formalizuje cztery tezy z kanonicznego
rozdziału **LST-02** w siedmiu deklaracjach (w tym pomocniczy
kontrprzykład dla pustych dziedzin): negacje kwantyfikatorów,
zamiany kolejności kwantyfikatorów jednego typu, tylko właściwy
kierunek implikacji dla kwantyfikatorów różnych typów oraz rozwinięcie
`∃!`. Rejestr `manifest.json` zawiera teraz **9 wpisów** (5 LST-01,
4 LST-02). Wszystkie cztery nowe wpisy mają
`statement_status=needs_review`, nie mają zatwierdzonego
SHA256 źródła i pozostają `draft`. Pełna zgodność semantyczna
wymaga odrębnej recenzji; `certificate=false`.

- [Raport mapowań LST-02](../docs/LEAN_L13_LST02_PILOT_2026-11-23.md)
- [Issue #11 — niezamknięty pilotaż 20–30](https://github.com/dariusz-piekarz/mathematical_scipts/issues/11)
- [CI aplikacji #45206502457](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206502457) — `completed/success`, 736 testów, 10 sklasyfikowanych pominięć i 0 nierozliczonych, Chromium PASS na 509 rozdziałach.
- [Rzeczywisty Lean #45206502490](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206502490) — **`completed/success`** na poprawionym SHA `163c8f6415d9d390fc1a737f6954b2865eff6c6e`: **5 plików, 25 twierdzeń, kontrola aksjomatów PASS**, w tym 7 nowych deklaracji LST-02. Pozostaje obowiązek niezależnej recenzji semantycznej. [Przebieg technicznej stabilizacji 2+1 #45208224201](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201) został uruchomiony na tym SHA; wynik każdej pełnej rundy wymaga osobnego zakończenia.

Pierwszy CI dla `2deca7ba` zakończył się błędem testu
odczytującego dosłowną etykietę TeX z podwójnym ukośnikiem.
Commit `163c8f64` poprawił ten test; błędne CI nie jest
zaliczoną rundą stabilizacji.
