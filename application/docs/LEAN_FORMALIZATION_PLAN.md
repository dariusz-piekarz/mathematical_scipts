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

### Strumień A — integralność podglądu Lean (22.11.2026)
- `backend/lean_formalization.py::fragment` weryfikuje SHA256 rzeczywistej treści `documents.content` względem `documents.sha256` przed udostępnieniem mapowania i kodu Lean. Uszkodzony indeks zwraca HTTP 409 zamiast pokazywać potencjalnie nieaktualne powiązanie jako gotowe.
- Dodano regresję HTTP `test_corrupt_index_blocks_fragment_preview` w `tests/test_lean_http.py`, wymuszając błędny skrót w odpowiedzi warstwy indeksu.
- Commity: `114a5537`, `2e7d8173`. Testy GitHub Actions uruchamiane przez push; **wynik tej iteracji niepotwierdzony w chwili zapisu**, nie deklarować zaliczenia bez sprawdzenia workflow. Poprzedni CI `45011821712` zakończył się sukcesem.
- Bez zmian w źródłach `.tex` i rejestrze Lean. `certificate=false` pozostaje zasadą; brak toolchaina to `toolchain_unavailable`, nie `verified`.
- Następny krok: sprawdzić CI nowego commitu; następnie ograniczyć zasoby i wielkość wyjścia procesu Lean, z testami timeout i przerwania procesu potomnego.

### Strumień A — regresja diagnostyki runnera (22.11.2026)
- Dodano `test_runner_truncates_large_output_and_never_certifies_failure` w `application/tests/test_lean_formalization.py`: symulowany nieudany proces emituje 100000 znaków stdout i końcową diagnostykę stderr; test wymaga statusu `failed`, `certificate=false`, logu o długości najwyżej 16000 znaków i poprawnego odczytu historii uruchomienia.
- Commit testu: `6e8b6cda`. Test nie jest dowodem ograniczenia pamięci subprocess: `capture_output=True` nadal buforuje pełne stdout/stderr przed przycięciem. Nie deklarować ochrony przed nadmiernym wyjściem procesu.
- W chwili zapisu nie ma potwierdzonego wyniku CI tego commitu. Następny krok: sprawdzić GitHub Actions, następnie zaimplementować ograniczone strumieniowanie wyjścia i niezawodne zakończenie grupy procesów przy timeout, z testami procesów potomnych, bez uruchamiania kodu z klienta.

### Audyt semantyczny i przypięcie SHA: LST-01 (22.11.2026)
- W rzeczywistym [GitHub Actions #45011738363](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011738363) zakończono sukcesem kompilację **4 plików / 14 deklaracji Lean** i kontrolę ich aksjomatów (Lean 4.26.0, Mathlib commit `2df2f015...`). W 8 deklaracjach `Formula` Lean raportuje najwyżej `propext`; żaden dowód nie używa `sorryAx`.
- W oddzielnym audycie porównano `Formula`, pięć spójników, `Valuation`, `eval`, `equivalent`, `tautology` oraz wszystkie sześć członów `thm:de-morgan-logic`, `thm:implication-laws` i `thm:negated-implication-xli` z literalną treścią `LST-01`. Sprawdzono także 32 przypadki tablic prawdy dla ośmiu tożsamości. Raport: `application/docs/LEAN_SEMANTIC_AUDIT_LST01_2026-11-22.md`.
- `manifest.json`: 3 powiązania mają teraz `statement_status=approved` **wyłącznie dla** kanonicznego źródła `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`, SHA256 `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`. `lean_theorems` wymienia wszystkich 6 członów źródłowych twierdzeń.
- W backendzie zmiana SHA w spójnym indeksie oraz zmiana fizycznego pliku `.tex` **bez przebudowania indeksu** unieważniają zatwierdzenie (`stale`, efektywne `needs_review`) i blokują lokalną kompilację. Uszkodzony indeks daje HTTP 409. W CI sprawdzana jest pełna lista grup, rzeczywisty SHA kanonicznego pliku, ścieżka źródła i wszystkie wyniki `#print axioms`. Dodano testy jednostkowe, API i antyregresyjne.
- **Nadal `certificate=false`:** recenzja semantyczna tej iteracji jest oddzielna od udowodnienia formalnego w Lean i nie stanowi podpisu niezależnego recenzenta. Włączenie certyfikatów wymaga osobnej zaufanej polityki. Następny zakres: `thm:valuation-well-defined-xli`, `thm:equiv-test`, a potem `LST-02`.

### Strumień A — brak tekstu źródła w podglądzie (22.11.2026)
- W `_find_source` sprawdzana jest tekstowa treść `documents.content` przed wycinaniem zakresu obiektu i przed `splitlines` dla wyboru wierszy. W przypadku `NULL`/nietekstowej wartości API zgłasza HTTP 409 zamiast nieobsłużonego wyjątku.
- Dodano `test_nontext_source_is_rejected_for_entity_and_line_selection` z obiema ścieżkami wyboru. Commity `a40f3f0a`, `9c28c3f1`.
- Wynik CI nowych zmian wymaga osobnego potwierdzenia; nie deklarować sukcesu przed zakończeniem workflow. Nie modyfikowano kanonicznych `.tex` ani rejestru Lean.
- Nadal otwarte: limit pamięci przechwytywanego stdout/stderr i poprawne zamykanie procesów potomnych przy timeout.

### Strumień A — ograniczone wyjście i sprzątanie procesów Lean (22.11.2026)
- Dodano `backend/lean_process.py::execute_registered`: osobny lokalny proces `lake env lean`, wspólny strumień stdout/stderr odczytywany porcjami 8192 bajtów, przechowywany w pamięci ogon najwyżej 16000 bajtów. Zastąpiono `subprocess.run(capture_output=True)` w `backend/lean_formalization.py::run`, tak aby wielkość RAM bufora logu nie zależała od liczby komunikatów kompilatora.
- Na POSIX: osobna sesja procesu i `killpg(..., SIGKILL)` przy timeout; Windows: próba `taskkill /T /F` i awaryjne `process.kill`. W razie odziedziczonego otwartego stdout po zakończeniu rodzica nie zapisuje się sukcesu — wynik `failed` i `certificate=false`. Nadal nie jest to sandbox ani gwarancja usunięcia wszystkich procesów odłączonych od grupy.
- Zaktualizowano jednostkowe mocki runnera i dodano `test_lean_process.py` z trzema rzeczywistymi testami: 3 MB wyjścia, timeout rodzica z potomkiem i wczesny koniec rodzica z żywym potomkiem. Wszystkie trzy przeprowadzono lokalnie na Linuksie i zaliczono. Dodatkowy test `test_incomplete_descendant_cleanup_never_reports_compiled` sprawdza kontrakt API.
- Commity: `a938ccaf` (moduł), `5751e92a` (klasyfikacja błędów), `e702be92` (integracja), `16571103` (mocki), `166ff211` (brak fałszywego sukcesu), `d9de679d` (rzeczywiste procesy), `2b91e99e` (kontrakt API). CI po ostatnim commicie: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013555013 — **oczekuje na końcowy wynik**.
- Poprzedni przebieg `45013419540` zakończył się błędem czterech starych testów mockujących `subprocess.run` podczas przejściowego commitu; dostosowano je w `16571103`. Nie przedstawiać tego przebiegu jako zaliczonego.
- **Pozostałe ryzyko:** maksymalny rozmiar logu w RAM jest ograniczony, ale zużycie pamięci samych procesów Lean/Lake nie podlega jeszcze limitowi OS/cgroup/Job Object. Kolejna iteracja: bezpieczny, konfigurowalny limit pamięci zależny od systemu, z testami odmowy uruchomienia, jeśli limitu nie da się wyegzekwować. Nie uruchamiać Lean z kodu dostarczonego przez klienta.

### Strumień A — limit pamięci procesu Lean (22.11.2026)
- Dodano opcjonalną konfigurację `MATLIB_LEAN_MEMORY_MB` (liczba całkowita 512–65536 MiB). W Linuksie `backend/lean_process.py` uruchamia dedykowany program `backend/lean_memory_exec.py`, który **przed** `execvp(lake)` wywołuje `resource.setrlimit(RLIMIT_AS, (limit, limit))`. Potomkowie dziedziczą limit przestrzeni adresowej; celowo uniknięto `preexec_fn` w wielowątkowym procesie serwera.
- Brak zmiennej oznacza zgodność wsteczną: **nie ma limitu pamięci systemowej** (pozostałe limity czasu i logu nadal obowiązują). Zalecana konfiguracja na Linuksie: `MATLIB_LEAN_RUN=1 MATLIB_LEAN_MEMORY_MB=8192`; limit należy dobrać do lokalnego toolchaina. Na Windows oraz innych niezweryfikowanych systemach żądanie limitu **blokuje** uruchomienie, zamiast wykonywać je bez ograniczeń. Nie oznacza to obsługi Windows Job Objects.
- `run` zwraca `blocked` i `certificate=false` przy błędnej konfiguracji lub braku wsparcia systemowego; `availability` ujawnia `memory_limit_mb`, `memory_limit_supported`, `memory_limit_enforced`, `memory_limit_error`. W razie błędu ustawienia RLIMIT w pomocniczym procesie program nie uruchamia Lean i kończy się niezerowym kodem.
- Testy `test_lean_process.py` sprawdzają walidację konfiguracji, odmowę uruchomienia przy nieobsługiwanej platformie, faktyczne odziedziczenie RLIMIT_AS oraz nieudaną próbę alokacji 1,2 GiB przy limicie 512 MiB. `test_lean_formalization.py` dodaje trzy regresje API. Uruchomione lokalnie próby limitu Linuksa przeszły; całościowy CI wymaga potwierdzenia.
- Przejściowy CI `45014071222` zakończył się **niepowodzeniem jednej asercji testu**, która szukała słowa `allocated` także w tracebacku zawierającym kod źródłowy. Zastąpiono ją wymaganiem `MemoryError` w commicie `2bbaf552`; nowy CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014145355 (wynik do potwierdzenia).
- **Granice ochrony:** Linux RLIMIT_AS ogranicza wirtualną przestrzeń adresową **każdego procesu osobno**, a nie sumę RSS całego drzewa procesów. Nie jest to sandbox ani zamiennik cgroup v2/Windows Job Object. W przyszłości wdrożyć agregowany limit w cgroup v2 oraz Job Objects; zachować odmowę uruchomienia tam, gdzie zażądany limit nie może zostać wyegzekwowany. Kanonicznych `.tex` i rejestru Lean nie zmieniano; `certificate=false` bez wyjątku.

- Uzupełniono regresję o rzeczywisty proces potomny (`test_linux_memory_ceiling_is_inherited_by_descendants`), który odczytuje własny `RLIMIT_AS` po uruchomieniu przez proces nadrzędny. Próba lokalna Linux przeszła; commit `2da1ef7f`, CI https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014252809 — wynik niepotwierdzony w chwili zapisu.

### Strumień A — agregowany limit pamięci cgroup v2 (22.11.2026)
- Dodano opcjonalny `MATLIB_LEAN_TOTAL_MEMORY_MB` (512–65536 MiB) **niezależnie** od `MATLIB_LEAN_MEMORY_MB`. Linux cgroup v2 wymaga, by bieżący proces miał już delegowany kontroler `memory` i uprawnienia do utworzenia dziecka w swoim poddrzewie. Brak wartości zachowuje kompatybilność wsteczną, ale nie ustanawia limitu agregowanego.
- `backend/lean_cgroup.py` tworzy osobną losową cgroup na kompilację, ustawia `memory.max`, `memory.oom.group=1`, `memory.swap.max=0` i wymaga `cgroup.kill`. `backend/lean_cgroup_exec.py` najpierw zapisuje swój PID do `cgroup.procs`, a dopiero potem wykonuje zaufany program `lake`. Nie zmieniamy uprawnień ani `cgroup.subtree_control` rodzica.
- `lean_process.execute_registered` sprząta grupę w bloku `finally` (także przy błędach i timeout), nie pokazuje sukcesu, gdy pozostały uruchomione procesy, i blokuje wynik przy niemożności egzekwowania limitu. `lean_formalization.run` zwraca `blocked` i `certificate=false` dla niewłaściwej konfiguracji, braku delegacji lub błędów cgroup. `availability` raportuje `total_memory_limit_mb`, `total_memory_limit_supported` oraz `total_memory_limit_error`. Zgłoszona dostępność oznacza tylko wstępne rozpoznanie; rzeczywiste uprawnienia weryfikuje utworzenie grupy.
- Dodano `application/tests/test_lean_cgroup.py`: testy walidacji, odmowy uruchomienia bez delegacji, błędu przygotowania grupy, kolejności dołączenia przed `exec`, nieuruchamiania kodu po nieudanym dołączeniu oraz sprzątania. Test z rzeczywistą cgroup działa tylko tam, gdzie jest przyznana delegacja; na typowym CI może zostać jawnie pominięty. Rozszerzono `test_lean_formalization.py` o regresje API.
- Commity: `56f2e5c0`, `0577c1a1`, `f65361fc`, `ea2106ac`, `fab7f984`, `1968bdd5`. CI ostatniego commitu: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45015672942 — **nie potwierdzono jeszcze wyniku** w chwili zapisu.
- **Granice:** cgroup ogranicza łączną pamięć procesów, które pozostały w grupie. Nie jest sandboxem ani zabezpieczeniem przed złośliwym lokalnym plikiem Lean mogącym opuścić delegowaną cgroup; brak obsługi Windows Job Objects jest osobnym otwartym zadaniem. Zatwierdzenie semantyczne pozostaje oddzielone od wyniku kompilacji; `certificate=false` bez wyjątków. Nie zmieniano kanonicznych `.tex` ani źródeł `application/lean`.
