# Lean Formalization — lokalny pilotaż

Pierwszy etap rozwijany niezależnie od audytów LaTeX. Źródła matematyczne są tylko do odczytu; kod Lean ma odrębny rejestr w \`manifest.json\`.

## Co jest dostępne w aplikacji
1. Otwórz obiekt matematyczny w Explorerze; w Czytniku kliknij **Zobacz w Lean**.
2. Alternatywnie zaznacz wiersze źródłowego LaTeX i kliknij **Zaznaczenie → Lean**, albo wpisz zakres wierszy. Kod Lean jest widoczny wyłącznie, jeśli w rejestrze istnieje formalizacja powiązana z odpowiednią etykietą.
3. Odczytaj osobne statusy zgodności tłumaczenia, obecności/synchronizacji źródła i wykonania Lean. Przykładowy pilot \`LST-01/thm:de-morgan-logic\` pozostaje niezatwierdzonym szkicem.
4. Lokalny przycisk **Uruchom Lean** jest domyślnie zablokowany. Nie uruchamia dowolnego kodu wpisanego w przeglądarce.

## Instalacja Lean/Mathlib (lokalne środowisko zaufane)
Zainstaluj elan/Lean 4 i upewnij się, że \`lake\` jest dostępne w PATH. Następnie w terminalu:

\`\`\`powershell
cd application/lean
lake update
lake exe cache get
lake env lean src/LST01_DeMorgan.lean
cd ..
$env:MATLIB_LEAN_RUN = "1"
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
\`\`\`

\`lean-toolchain\` i \`lakefile.toml\` wskazują kompatybilną parę Lean/Mathlib \`v4.26.0\`. Po pierwszym udanym \`lake update\` należy dodać i wersjonować wygenerowany \`lake-manifest.json\` dla pełnej powtarzalności. Środowisko wykonawcze bieżącej iteracji **nie ma zainstalowanego** \`lake\`; prawdziwa kompilacja pliku demonstracyjnego nie została jeszcze potwierdzona.

**Bezpieczeństwo:** endpoint wykonania jest dla serwera uruchomionego lokalnie i pod kontrolą właściciela. Nie należy wystawiać go publicznie: Lean to program i zarejestrowany plik może wykonywać operacje IO. Timeout jest ograniczeniem operacyjnym, a nie sandboxem systemowym. Zdalny tryb wykonawczy wymaga odrębnego, izolowanego kontenera z ograniczonymi uprawnieniami, pamięcią, czasem i dostępem do sieci.

## API
- \`GET /api/lean/status\`
- \`GET /api/lean/fragment?entity_id=LST-01%2Ftheorem%2F0001\` (identyfikator zależy od faktycznego indeksu)
- \`GET /api/lean/fragment?module_id=LST-01&start_line=433&end_line=438\`
- \`POST /api/lean/run\` z body \`{"formalization_id":"lst01-de-morgan"}\`

Udana kompilacja daje status \`compiled\`, **nigdy automatycznie certyfikat zgodności oryginalnego twierdzenia**. Brak Lean, timeout, błędy lub nieznana formalizacja są jawnie raportowane. Oryginalny skrypt pozostaje kanoniczny.

## Testowanie
\`\`\`powershell
cd application
python -m unittest tests.test_lean_formalization -v
\`\`\`
Testy obejmują wybór obiektu i zakresu, brak formalizacji, źródło stale, ścieżki, blokadę uruchamiania i symulację subprocess. Test z atrapą procesu NIE jest prawdziwą weryfikacją twierdzenia w Lean. CI aplikacji uruchamia te testy przez zwykłe unittest discover.
