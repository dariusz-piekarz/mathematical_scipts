# Atlas / Lean — L1.2: ścisła walidacja zapisanych wyników uruchomień

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Jednostka:** L1.2 — osobna od ustabilizowanej optymalizacji L1.1.
**Stan:** implementacja i testy złożone; wyniki nowego CI do weryfikacji.

## Problem i ograniczony zakres

`application/backend/lean_results.py::last_run` dotąd sprawdzał podstawowe pola
rekordu, jego wersję i zgodność wartości z podanym fingerprintem, ale nie
wymagał pełnego, dokładnego schematu JSON. Nie odrzucał jawnie
`certificate=true`, nie sprawdzał duplikatów kluczy, a odczyt poprzez
`Path.read_text` po osobnym `stat` nie miał **limitu rzeczywistych bajtów
odczytanych** w razie wzrostu pliku pomiędzy operacjami. Odczyt mógł też
podążyć za dowiązaniem symbolicznym pliku rekordu.

Nie oznaczało to automatycznego uznania `certificate=true` w API, ponieważ
zwracana wartość `certificate` jest na sztywno `false`. Mimo to
niekompletny rekord nie powinien w ogóle być dopuszczany jako poprawny cache.

## Zmiana produkcyjna

Commit `23cf4183`:

- wymaga dokładnego zestawu pól bieżącego schematu 5, włącznie z **ośmioma
  SHA256**, `source_binding_sha256`, wersją toolchainu i `certificate=false`;
- odrzuca duplikaty kluczy JSON niezależnie od ich wartości, dzięki
  `object_pairs_hook`;
- rozróżnia rekord **nieprawidłowy** (`run_record_invalid`) od strukturalnie
  poprawnego rekordu ze **starym SHA** (`previous_run_outdated`);
- odrzuca dowiązania symboliczne pliku zapisu, błędny/bezstrefowy
  `finished_at`, nieprawidłowy `proof_status` oraz przekroczony limit pól
  `detail` i `log`;
- ogranicza rzeczywisty odczyt pliku do `MAX_RECORD_BYTES+1`, odrzucając
  rekord większy niż `MAX_RECORD_BYTES=30000` bajtów;
- używa jednego walidatora fingerprintu przy odczycie i zapisie.
  Nie zmienia `SCHEMA_VERSION=5` ani formatu poprawnie zapisanych rekordów.

**Uczciwa granica zaufania:** lokalny edytowalny plik JSON nie jest
kryptograficznym potwierdzeniem przeprowadzenia kompilacji Lean. Kontrola
formatu zmniejsza ryzyko przyjęcia uszkodzonych lub błędnie przygotowanych
danych, ale nie eliminuje dowolnej modyfikacji procesu/plików przez podmiot
mający prawa zapisu. Sprawdzenie `Path.is_symlink()` nie stanowi pełnej
ochrony przed wyścigiem zmian ścieżki przez inny proces. Testy i komunikaty
nie mogą podnosić semantycznego statusu dowodu.

## Testy

Commit `db5c2a70`, `application/tests/test_lean_results.py`:

- podstawowy zapis/odczyt prawdziwie utworzonego rekordu;
- `certificate=true` i `"false"`, dodatkowe i brakujące pola;
- niepoprawny SHA, `proof_status`, timestamp i wersja schematu;
- za długie `detail`, `log` i `declared_toolchain`;
- duplikat `proof_status` w JSON oraz nadmierny fizyczny rozmiar rekordu;
- prawidłowy, ale nieaktualny fingerprint nadal daje `previous_run_outdated`;
- brakujący/rozszerzony fingerprint oczekiwany i symlink rekordu.

Commity `752ea793` i `550bb1ea` podłączają ten test do szybkiego
Linux/Windows i osobnego przypiętego workflow Lean 4 / Mathlib. Kontrakt
API i runner Lean pozostają bez zmian.

## Bramka stabilizacji

- [ ] Udane regresje Linux i natywny Windows dla L1.2
- [ ] Pełne CI aplikacji na commicie obejmującym implementację i testy
- [ ] Rzeczywisty Lean 4.26.0 / przypięty Mathlib oraz kontrola aksjomatów
- [ ] Odrębny sceptyczny przegląd semantyki `run_record_invalid` i
      `previous_run_outdated`
- [ ] Powtarzalna walidacja 2+1 na tym samym SHA

Do zamknięcia tych bramek oznaczać L1.2 jako **W TOKU**.
L1.1 pozostaje niezależnie **ZAMKNIĘTY** dla SHA `95508306`.
