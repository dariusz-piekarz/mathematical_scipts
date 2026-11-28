# Audyt bezpieczeństwa lokalnego runnera Lean — strumień A

Data: 22.11.2026. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Zakres

Sprawdzono `application/backend/{lean_formalization,lean_results,lean_process,lean_memory_exec,lean_cgroup,lean_cgroup_exec,lean_windows_job,lean_windows_exec,lean_run_lock}.py`, testy obu platform i workflow Windows. Zakres obejmuje kontrolę źródła LaTeX/Lean, procesy potomne, zapis historii, timeout, wyjście procesu, pamięć, współbieżność i ograniczenia środowisk wykonawczych.

## Zrealizowane kontrole

| Kontrola | Mechanizm | Dowód testowy |
| --- | --- | --- |
| Wybór kodu | Wyłącznie ścieżki `.lean` z lokalnego rejestru; nie wykonywać kodu ani dowolnej ścieżki wskazanej przez klienta | `test_lean_formalization.py`, `test_lean_http.py` |
| Zgodność źródła | SHA256 tekstu w SQLite i kanonicznego `.tex` jest weryfikowane przed uruchomieniem; fingerprint Lean i zadeklarowanego toolchaina sprawdzany ponownie po wykonaniu | testy starych i uszkodzonych indeksów |
| Statusy | `compiled`, `failed`, `timeout` są stanami procesu, nie certyfikatami matematycznymi; zawsze `certificate=false` | testy API oraz `lean_results.py` |
| Diagnostyka | Odczyt po 8192 bajtów, ogon do 16000 bajtów; brak gromadzenia nieograniczonego logu w RAM | `test_lean_process.py` |
| POSIX | Limit czasu, osobna sesja, próba zabicia grupy procesów po timeout | test z rzeczywistym potomkiem |
| Linux | Opcjonalny per-process `RLIMIT_AS`; opcjonalna delegowana cgroup v2 `memory.max` / `memory.swap.max` / `memory.oom.group` i `cgroup.kill` | Linux CI; test z rzeczywistą cgroup może być pominięty bez delegacji |
| Windows | Opcjonalny Job Object z `JOB_OBJECT_LIMIT_JOB_MEMORY` i `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`; program pomocniczy uruchamia Lean dopiero po przypisaniu do Job Object | natywny Windows CI [45017259828](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017259828), 12 testów |
| Współbieżność | OS-owa wyłączna blokada `application/data/lean_runs/.runner.lock`, bez czekania; obejmuje start i zapis historii; przy zajętej blokadzie `blocked` bez nowego procesu. Plik pozostaje na dysku, by nie rozdzielić właścicieli blokady. | `test_lean_run_lock.py`: dwa procesy, nieudana próba, awaryjne zwolnienie, niezależność błędów; natywny Windows [45017923364](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017923364) |
| Łącze symboliczne blokady (POSIX) | `os.open(O_NOFOLLOW)` i kontrola `fstat` odmawiają otwarcia dowiązania symbolicznego lub obiektu niebędącego zwykłym plikiem | `test_symlinked_lock_file_fails_closed` |

Dotychczasowe przebiegi potwierdzone: aplikacja Linux [45017338869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017338869) — SUCCESS; natywny Windows Job Object [45017259828](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017259828) — SUCCESS. Natywny Windows z nową blokadą [45017923364](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017923364) — SUCCESS (4/4 testy blokady). Dla nowych commitów uruchamianych podczas audytu wymagana jest odrębna kontrola wyników; nie przedstawiać oczekujących zadań jako zaliczonych.

## Ryzyka pozostające otwarte

1. **Brak sandboxu dla nieufnego Lean (wysoki wpływ).** Kod wybrany z lokalnego rejestru nadal działa z uprawnieniami użytkownika. Limity pamięci, czasu i blokady nie chronią przed celowym dostępem do plików, sieci ani przed kodem opuszczającym mechanizm kontroli zasobów. Aplikacja nie może przyjmować i wykonywać dowolnych fragmentów Lean od klienta.
2. **Niedomknięte zależności fingerprintu (średni wpływ).** Wynik historyczny jest związany z SHA256 wskazanego pliku Lean, tekstem źródłowym i plikami deklaracji toolchaina, ale nie z całym przechodnim domknięciem importów Lean/Mathlib i binarnym stanem środowiska. Wcześniejszego `compiled` nie przedstawiać jako dowodu aktualnej kompilacji tych zależności.
3. **TOCTOU w źródłach (średni wpływ).** SHA jest sprawdzany przed i po kompilacji, ale nie blokuje innych lokalnych procesów przed zmianą plików pomiędzy kontrolą a wykorzystaniem (w szczególności po końcowym porównaniu i przed atomowym zapisem wyniku). Do ścisłego poświadczenia budowy potrzebne byłyby niezmienne wejścia, pełny manifest i izolowane środowisko.
4. **Blokada dotyczy jednego checkoutu i jego lokalnego systemu plików (średni wpływ).** Chroni kilka procesów działających w tym samym drzewie `application/` przy standardowych lokalnych blokadach OS; nie jest blokadą rozproszoną między niezależnymi checkoutami ani gwarancją poprawności na wszystkich sieciowych FS. Limit całkowitego obciążenia systemu przez inne aplikacje nie istnieje.
5. **Ograniczenia pamięci są opcjonalne (średni wpływ).** Bez `MATLIB_LEAN_MEMORY_MB` i/lub `MATLIB_LEAN_TOTAL_MEMORY_MB` nie ma odpowiedniego systemowego limitu RAM. Cgroup v2 wymaga faktycznej delegacji kontrolera, a Windows Job Objects sprawdzono na `windows-latest`, nie na każdej konfiguracji Windows 11.
6. **Cleanup przy nieprzewidzianej awarii systemu (niskie/średnie).** Zamknięcie uchwytu Job Object przy `KILL_ON_JOB_CLOSE` i zamknięcie plikowej blokady OS jest odporne na typowe awarie procesu, natomiast zewnętrzne zabijanie serwera w połowie kompilacji i pozostające artefakty cgroup wymagają osobnego testowania oraz procedury operatora.

## Wnioski operacyjne

Uruchamianie lokalne nadal wymaga `MATLIB_LEAN_RUN=1`; rekomendować limity i tryb jednego kompilatora na checkout. `blocked` z powodu zajętej blokady, braku kontrolera lub błędu inicjalizacji nie jest porażką matematyczną. Dopiero rzeczywisty `compiled` na zatwierdzonych źródłach oznacza sukces procesu, nigdy certyfikat zgodności semantycznej. Najbliższy kierunek rozwoju: manifest pełnych zależności i odporność na TOCTOU, a nie rozszerzanie zakresu wykonywalnego kodu.
