# Lean Formalization — plan wdrożenia do Atlasu matematycznego

**Data przyjęcia:** 2026-11-22  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź robocza:** `biblioteka-matematyczna-iteracja-6`  
**Stan:** zatwierdzony plan; wdrożenie iteracyjne.  
**Zasada:** Lean to niezależna warstwa formalizacji, a nie zastępstwo audytu matematycznego i językowego. Kanoniczne źródła `.tex` są tylko do odczytu.

## Cel końcowy
W czytniku aplikacji użytkownik wybiera twierdzenie/lemat/dowód albo zaznacza dowolny zakres pełnych wierszy źródłowego LaTeX-a. Może otworzyć panel **Lean 4** z:
- dokładnym źródłem LaTeX, etykietą i lokalizacją,
- odpowiadającym mu kodem Lean 4, o ile formalizacja istnieje,
- statusem zgodności treści, statusem kompilacji/dowodu, logiem diagnostycznym,
- zależnościami Mathlib i lokalnymi lematami oraz odciskiem wersji źródła,
- przyciskiem **Uruchom Lean** dla zatwierdzonej formalizacji.
Brak istniejącego pliku Lean nie jest udawany przez generację szablonu jako dowód. Wybrany dowolny fragment nie jest traktowany jako wykonywalny kod.

## Rozdzielenie stanów (nie łączyć w jeden bool!)
1. **Wierność treści** (`statement_status`): `unreviewed`, `needs_review`, `approved`; kontrola zgodności formalnego stwierdzenia z polskim LaTeX, zakresami kwantyfikatorów, założeniami, definicjami i typami.
2. **Stan formalizacji** (`formalization_status`): `missing`, `draft`, `ready`, `stale`; powiązanie z `module_id`, `entity_id`, `label` i SHA256 źródła.
3. **Stan uruchomienia** (`proof_status`): `not_run`, `verified`, `failed`, `timeout`, `toolchain_unavailable`, `blocked`; wynika wyłącznie z rzeczywistego wykonania Lean.
Do wyświetlenia certyfikatu **Zweryfikowane matematycznie** wymagane są jednocześnie: zatwierdzona wierność stwierdzenia, aktualne SHA źródła, rzeczywisty pozytywny wynik Lean, kontrola niepożądanych aksjomatów, brak `sorry`/`admit` i brak pozornie dowolnych założeń. Kompilacja kodu nie certyfikuje poprawności przekładu oryginalnego twierdzenia.

## Architektura
- **Istniejące wejście:** `application/backend/latex_parser.py`, SQLite `documents`/`entities`/`labels` (read-only); wybór zakresu w `application/frontend/app.js`.
- **Nowy backend:** `application/backend/lean_formalization.py`: odczyt rejestru, sprawdzenie integralności SHA, uruchomienie Lean w procesie podrzędnym, diagnostyka.
- **Rejestr:** `application/lean/manifest.json`, elementy z `source_module`, `source_entity` lub dokładną etykietą, `source_sha256`, `lean_file`, `lean_theorem`, statusem recenzji treści. Pliki `.lean` w `application/lean/src/`; rygorystyczna kontrola ścieżek bez traversalu.
- **Backend API:** `GET /api/lean/status` (dostępność `lake`/Lean), `GET /api/lean/fragment?entity_id=...` lub `?module_id=...&start_line=...&end_line=...` (źródło + kod + status), `POST /api/lean/run` (identyfikator zatwierdzonej formalizacji, bez dowolnego kodu z przeglądarki).
- **Frontend:** panel/zakładka Lean otwierana z Czytnika; przejście z obiektu i z istniejącego zaznaczenia wierszy; tylko `textContent` dla nieufnego LaTeX/Lean/logów. Widoczne statusy osobno.
- **Uruchomienie:** wyłącznie lokalny `lake env lean` lub `lean`, ustalony katalog, izolowany katalog tymczasowy, limit czasu i wyjścia, biała lista zarejestrowanych plików; żadnej możliwości uruchamiania arbitralnych komend powłoki. W środowisku współdzielonym konieczny sandbox na poziomie systemu operacyjnego (sam timeout subprocess nie jest pełnym sandboxem).
- **Wersjonowanie:** stabilny Lean 4 + przypięty commit Mathlib/`lake-manifest.json`; rejestrować wersję przy każdym sprawdzeniu.
- **CI:** statyczne testy API/JS zawsze; kompilacja małej bazy próbnej tylko w środowisku z zainstalowanym Lean/Mathlib. Nie zaliczać „verified” bez takiego uruchomienia.

## Etapy

### Etap 1 — działający minimalny moduł (priorytet)
1. Zidentyfikować obiekt ze źródła `entities` (lemat, twierdzenie, dowód) albo dokładne wiersze.
2. Wyświetlić panel Lean wraz z dokładnym źródłem LaTeX, kodem formalizacji, statusami i komunikatami.
3. Dodać czytelny status `missing` dla fragmentów bez formalizacji (nie generować fałszywych odpowiedników).
4. Odczytać konkretne, ręcznie przygotowane przykłady z `manifest.json`, zabezpieczyć integralność źródła.
5. Dodać przycisk uruchomienia wyłącznie znanego pliku z rejestru, z limitem zasobów, logiem i poprawnym `toolchain_unavailable`, gdy Lean nie jest zainstalowany.
6. Dodać testy jednostkowe/API/UX: obiekt, wybór wierszy, brak kodu, uszkodzony manifest, przestarzały SHA, brak narzędzia, awaria/timeout, pomyślne wykonanie przez atrapę procesu.
**Kryterium akceptacji:** użycie UI i API dla 1 poprawnie powiązanego obiektu; testy regresji; realne uruchomienie Lean, jeśli środowisko je udostępnia. W przeciwnym razie jawnie status `toolchain_unavailable`, etap 1 nie ma dowodu rzeczywistego uruchomienia.

### Etap 2 — pilotaż 20–30 formalizacji
- Najpierw `LST-01`, `LST-02` oraz `LA-01`, zaczynając od prostych praw logicznych i podstaw algebry liniowej.
- Każda formalizacja powiązana z **konkretnym** `\label`/obiektem i wersją źródła; oddzielać nieformalną semantykę wartościowań od `Prop` w Lean. Zmiana siły stwierdzenia wymaga przeglądu.
- Przykłady pilotażowe: prawa de Morgana, rozwinięcie implikacji, negacja implikacji, prawa kwantyfikatorów, przemienność dwóch kwantyfikatorów tego samego typu, podstawowe własności przestrzeni wektorowych.
- Raport liczbowy: przygotowane, skompilowane, zatwierdzone semantycznie, bez `sorry`, błędy i ograniczenia.

### Etap 3 — biblioteka zależności i automatyczna transkrypcja (eksperyment)
- Zintegrować mapowanie `label ↔ theorem`, graf zależności i wyszukiwanie Mathlib.
- Opcjonalnie przetestować PaperFormalizer/LeanAide/Aristotle; wymagana walidacja licencji, wersji i kosztów. Kandydaci nie mogą bezpośrednio nadpisywać źródeł `.tex`.
- Generacja transkrypcji trafia zawsze do stanu `draft`/`needs_review`; niezależne sprawdzenie semantyki i Lean.

### Etap 4 — skala i CI
- Cache kluczowany `source_sha + lean_sha + toolchain_version`; powtórna kontrola tylko zmienionych zależności.
- Publiczne raporty JSON dla rozdziału; opcjonalne oznaczenie w PDF tylko po spełnieniu kryteriów certyfikatu.
- Stopniowe rozszerzanie na inne dziedziny, bez automatycznego przypisywania wysokiego statusu przy braku Mathlib.

## Podział prac automatycznych
**Strumień A — implementacja aplikacji:** pracuje tylko w `application/backend/`, `application/frontend/`, `application/tests/` i dokumentacji Lean; wykonuje jedną mierzalną iterację oraz testy, commit na istniejącej gałęzi, wpis do dziennika. Unika zmian `.tex` i innych audytów.
**Strumień B — formalizacje i ich audyt:** pracuje wyłącznie w `application/lean/` i własnych raportach, dodaje po jednym lub kilku niepowielanych przykładach oraz uruchamia Lean, jeśli dostępny; nie dotyka plików backend/frontend/kanonicznych `.tex`. Przy braku działającego interfejsu programu kontynuuje tworzenie i testowanie korpusu niezależnie.
**Zasada współbieżności:** przed zapisem zawsze odczytać aktualny HEAD gałęzi; nie robić force-push, nie nadpisywać zmian innych audytów; przy konflikcie zaniechać zapisu i zaraportować. Każda iteracja odczytuje ten plan i ostatni status; brak nowej pracy = raport, bez fikcyjnych commitów.

## Dziennik iteracji Lean
- 2026-11-22 — użytkownik zatwierdził uruchamianie Lean z aplikacji, podgląd kodu i statusu dla wybranego fragmentu. Przyjęto cztery etapy i dwa rozdzielone strumienie automatyczne. Etap 1 traktować jako pierwszy cel implementacji. Rzeczywiste wykonanie Lean nie jest jeszcze potwierdzone.


### Stan implementacji po pierwszej ręcznej iteracji (22.11.2026)
- Utworzono `application/backend/lean_formalization.py` oraz API `/api/lean/status`, `/api/lean/fragment`, `/api/lean/run`.
- Utworzono w aplikacji zakładkę **Lean 4**, przyciski dla obiektu i zaznaczenia w Czytniku, pokaz źródła LaTeX, kodu Lean, statusów i diagnostyki. Dla `proof` bez własnej etykiety dopuszczono wyłącznie powiązanie z bezpośrednio poprzedzającym twierdzeniem oraz wyraźny komunikat o ograniczeniu.
- Dodano pilot `LST-01:thm:de-morgan-logic`, w rejestrze jako `needs_review` i `draft`, bez certyfikatu. Lean `v4.26.0` + Mathlib `v4.26.0` zadeklarowane, ale **nie uruchomiono realnej kompilacji Lean** z powodu braku `lake` w środowisku implementacji; `lake-manifest.json` jeszcze do wygenerowania.
- Dodano `application/tests/test_lean_formalization.py`, `test_lean_http.py` i `application/lean/README.md`. Test jednostkowy podstawowej implementacji przeszedł w GitHub Actions run 45008510683; nowo dodane testy HTTP i powiązania dowodów czekają na wynik najnowszego CI (nie należy ekstrapolować poprzedniego sukcesu).
- Utworzono dwie aktywne automatyzacje: rozwój modułu o :15 i pilotaż formalizacji o :45 każdej godziny (Europe/Warsaw); zakresy zapisu są rozłączne.
- **Pozostało do zamknięcia etapu 1:** sprawdzenie nowego CI, rzeczywisty test `lake env lean`, przypięcie SHA źródła oraz zależności Mathlib, audyt semantyczny, pełny test przeglądarkowy ścieżki Lean, a także kontrola izolacji wykonania. `compiled` nie jest równoznaczne z `certificate=true`.

### Iteracja ręczna — trwała historia Lean (22.11.2026)
- Dodano `backend/lean_results.py` i podłączono zapis/odczyt do `backend/lean_formalization.py`: JSON ostatniej rzeczywistej próby kompilacji, atomowy zapis, SHA256 źródła w indeksie, SHA256 kodu Lean, SHA256 konfiguracji narzędzi + deklarowana wersja Lean. Wyniki unieważniają się automatycznie przy zmianie zależności.
- Panel Lean w `frontend/app.js` po ponownym otwarciu pokazuje rzeczywisty ostatni status, czas i log, a w przypadku rozbieżności komunikat o nieaktualnym wyniku. `certificate=false` pozostaje niezależnie od kodu zakończenia procesu; nie jest to jeszcze certyfikacja semantyczna ani audyt aksjomatów.
- Dodano `tests/test_lean_results.py` (8 testów mechanizmu zaliczonych lokalnie), rozszerzono `tests/test_lean_formalization.py` o testy zapisu z mockiem i unieważniania, dodano `data/.gitignore`. Szczegółowy raport: `docs/LEAN_RUN_HISTORY_2026-11-22.md`.
- **Do weryfikacji:** pełny CI po pushu i rzeczywista kompilacja `lake env lean` po skonfigurowaniu Lean/Mathlib. Następne zadanie dla strumienia A: test przeglądarkowy historii oraz wymuszanie ponownego sprawdzenia po zmianie SHA.

### Kontrola Lean przez GitHub Actions — iteracja 22.11.2026
- Dodano osobny workflow `.github/workflows/lean-formalization.yml` uruchamiający rzeczywisty Lean dla plików w `application/lean/manifest.json`, z przypiętymi wersjami Lean v4.26.0 oraz Mathlib commit `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`.
- Dodano `application/scripts/lean_ci_audit.py` oraz `application/tests/test_lean_ci_audit.py`: bezwarunkowe wymaganie `#print axioms` i jego rzeczywistego logu dla każdego deklarowanego twierdzenia; niedozwolone aksjomaty oraz brak logu to błąd. **10/10 testów CI audit zaliczone w GitHub Actions** po poprawieniu parsera cytowanych nazw.
- Oficjalna akcja Lean wymaga `lake-manifest.json`; workflow inicjalizuje go przez `lake update` przed pobraniem cache. Najnowszy workflow z inicjalizacją: `https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010519869`.
- **Status:** nie deklarować kompilacji/prawdziwej weryfikacji, dopóki krok `Compile registered Lean files and check axioms` w tym workflow rzeczywiście nie przejdzie. Oddzielnie zachować `statement_status=needs_review` dla LST-01; `certificate=false` niezależnie od sukcesu CI. Raport: `application/docs/LEAN_CI_KERNEL_2026-11-22.md`.

### Etap 2 — pilotaż LST-01: prawa implikacji (22.11.2026)
- Potwierdzono rzeczywiste, zakończone sukcesem CI [45010519869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010519869): Lean 4.26.0, Mathlib z commit `2df2f015…`, kompilacja `LST01_DeMorgan.lean`, **2 deklaracje** i dozwolone aksjomaty.
- Dodano `application/lean/src/LST01_ImplicationLaws.lean` (obie równoważności + modus ponens, **3 deklaracje**) i `application/lean/src/LST01_NegatedImplication.lean` (jedna równoważność, **1 deklaracja**) oraz dwa wpisy rejestru. Razem obecnie **3 etykiety LaTeX / 6 deklaracji Lean**.
- Analiza przekładu w `application/docs/LEAN_PILOT_LST01_2026-11-22.md`; wszystkie wpisy mają `statement_status=needs_review`, bo `Prop` reprezentuje wartości zdań, a nie indukcyjną składnię formuł i funkcję wartościowania. Nie przypisano certyfikatów.
- Nowe pliki są testowane przez [CI 45011246156](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011246156). **Nie wpisywać nowym twierdzeniom statusu skompilowane, dopóki przebieg nie przejdzie.**
- Następnie: pełna semantyka formuł/wartościowań albo kolejne mapowania LST-02; zachować odrębność audytu semantycznego i kompilacji.

### Strumień A — integralność indeksu przed runnerem (22.11.2026)
- `backend/lean_formalization.py::run` sprawdza teraz, czy SHA256 rzeczywistych bajtów `documents.content` odpowiada `documents.sha256`; niezgodność lub brak tekstu daje `blocked` i `certificate=false` bez uruchamiania Lean.
- Dodano dwie regresje `test_runner_blocks_inconsistent_index_before_subprocess` i `test_runner_rejects_nontext_index_content` z asercją braku uruchomienia subprocess.
- Raport: `application/docs/LEAN_RUNNER_INDEX_INTEGRITY_2026-11-22.md`. Pełny test CI: [45011756997](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011756997) (wynik do sprawdzenia). Wcześniejszy pełny CI [45011702386](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011702386) miał błąd w niezależnym teście `test_lean_ci_audit`, nie w runnerze.
- Następny krok: zweryfikować końcowy CI i poprawić limity zasobów i wyjścia runnera. Sukces procesu nadal oznacza `compiled`, nigdy automatycznie `verified`.

### Etap 2 — indukcyjna składnia i wszystkie wartościowania, LST-01 (22.11.2026)
- Dodatkowy moduł `application/lean/src/LST01_SyntaxValuations.lean`: `inductive Formula` dokładnie z konstruktorami `atom`, `neg`, `conj`, `disj`, `imp`, `iff`; `Valuation := Nat → Bool`, `eval`, `equivalent` jako równość wartości przy każdym wartościowaniu i `tautology`. Łącznie 8 nowych twierdzeń, w tym 6 odpowiadających wszystkim członom trzech etykiet z LST-01, dodatkowe prawo dla `iff` oraz powtórzona litera.
- `application/lean/manifest.json`: 3 istniejące etykiety wskazują nowy plik (każda własne `lean_theorem`). Trzy wcześniejsze pliki `Prop` pozostają jako pomocnicze; `lean_ci_audit.py` weryfikuje wszystkie 4 pliki `.lean` (łącznie 14 deklaracji), także niezarejestrowane jako główna reprezentacja UI.
- Rozszerzono `test_lean_ci_audit.py` o wykrywanie pomocniczych plików oraz `test_lean_http.py` o 3 etykiety rzeczywistego indeksu. Raport porównania: `application/docs/LEAN_FORMULA_VALUATIONS_2026-11-22.md`.
- **Status ostrożności:** nowy CI [45011738363](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011738363) rozpoczął testy; 11 testów kontrolera zaliczonych, właściwa kompilacja nowego modułu musi jeszcze zostać potwierdzona. `statement_status=needs_review`, `certificate=false` pozostają bez zmian. Kanonicznych plików `.tex` nie modyfikowano.
