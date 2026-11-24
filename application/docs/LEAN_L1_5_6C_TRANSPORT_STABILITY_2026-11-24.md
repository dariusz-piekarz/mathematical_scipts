# L1.5.6c — stabilizacja transportu lokalnego i rzeczywisty preflight rootless (24.11.2026)

## Dowody z CI

- Poprzedni kandydat `1ec25612d4058077b6d5c733504c2c29fd6f45b0`: [45406330037](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45406330037), dwa pełne przebiegi pomyślne; licznik unieważniony przez zmianę kodu.
- Poprawka `fcf2bede2e70f4e27b00c4990723ef8a62eb95b3` zabija lokalną grupę procesów CLI przed zebraniem lidera w ścieżce błędu. Dwie trwałe regresje w `application/tests/test_lean_draft_transport.py` od `e78110c30b240e439048796d48afe69197160f01` sprawdzają żywego lidera oraz osieroconego potomka utrzymującego potok; oba testy rzeczywistych procesów Linux zakończyły się ok.
- [Pełny CI aplikacji 45422911731](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45422911731), SHA `e78110c30b240e439048796d48afe69197160f01`, próba 1: 861 testów (10 uzasadnionych pominięć, 0 niezaklasyfikowanych); Chromium passed, 529 indeksowanych rozdziałów, javascript_errors=[].
- [Pierwszy realny preflight 45422902836](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45422902836) odmówił pracy z powodu CpuCfsQuota. Poprawka CI `759fbd17dcbcb77b4361b8de62e6ffead34f54d4` deleguje kontrolery cgroup v2 przez systemd, bez osłabiania polityki aplikacji.
- [Realny preflight 45423273067](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45423273067), SHA `759fbd17dcbcb77b4361b8de62e6ffead34f54d4`, próba 1: ukończony z sukcesem. Rzeczywisty Docker rootless utworzył, skontrolował i usunął kontener bez jego uruchomienia. Log ATLAS_ROOTLESS_PREFLIGHT: status=configuration_checked, cleanup_status=removed, execution_allowed=false, proof_status=not_run, certificate=false.
- Sprawdzono zgodność blobów transportu, polityki runnera, regresji, skryptu probe i workflow aplikacji pomiędzy obydwoma kandydatami i bieżącą gałęzią. Workflow rootless jest identyczny z tym z kandydata 759fbd17, a nie z wcześniejszym e78110c3.
- Zlecono ponowne wykonanie obydwu jobów na ich niezmienionych SHA; w momencie zapisu **1/3 potwierdzonych przebiegów każdego rodzaju**. Nie liczyć samej akceptacji zlecenia jako zaliczenia.

## Granice i dalsza kolejność

Preflight nie dowodzi skuteczności izolacji podczas wykonywania kodu. Zakończenie lokalnej grupy CLI nie gwarantuje zakończenia daemonu, kontenera ani procesów, które celowo opuściły grupę. Nie włączać wykonywania kandydatów na podstawie tych wyników. Najpierw potwierdzić 2+1 dla każdego kandydata i niezależny sceptyczny audyt, następnie osobno zaplanować rzeczywisty test ograniczeń z ustalonym nieszkodliwym payloadem. Bez zmian kanonicznych TeX, Lean, manifestu i bez przejścia do L1.5.7.

## Druga kontrola stabilizacyjna (24.11.2026)

- Próba 2 obydwu wskazanych workflow zakończona sukcesem na niezmienionych SHA. Pełne CI: 861 testów, 10 sklasyfikowanych pominięć, 0 błędów JavaScript, 529 rozdziałów; obydwie regresje rzeczywistych procesów Linux: ok. Realny preflight: configuration_checked, cleanup_status=removed, execution_allowed=false, proof_status=not_run, certificate=false.
- Ponownie sprawdzono sześć blobów: transport, polityka runnera, test transportu, skrypt probe i dwa workflow. Ich treść nie zmieniła się względem raportu poprzedniej iteracji. Zlecono trzeci przebieg obydwu jobów (138549550505, 138549585636); wynik niepotwierdzony w chwili zapisu.
- Przegląd granic kontraktu: prepare regeneruje kandydat z oczekiwanymi trzema digestami i wymaga osobnej zgody; nie wykonuje kodu. Preflight sprawdza lokalny silnik i konfigurację nieuruchomionego kontenera. Nie jest to dowód egzekwowania ograniczeń w trakcie działania, bezpieczeństwa zawartości obrazu ani izolacji od procesów, które opuszczają grupę CLI. Nie wolno odblokować wykonania na tej podstawie. Następny krok po zaliczeniu 2+1: osobny kontrolowany test działającego kontenera na stałym nieszkodliwym payloadzie, nadal bez uruchamiania kandydatów Lean. Nie zmieniać kanonicznych źródeł ani manifestu.

## Trzeci przebieg i niestabilność przygotowania hosta (24.11.2026)

- Pełne CI [45422911731](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45422911731), SHA e78110c30b240e439048796d48afe69197160f01, próby 1–3: success. Trzecia: 861 testów, 10 uzasadnionych pominięć, 529 rozdziałów, Chromium passed, 0 błędów JS, oba rzeczywiste testy potomków ok. Kryterium powtórzeń 2+1 aplikacji spełnione dla tego SHA.
- Rootless preflight [45423273067](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45423273067), SHA 759fbd17dcbcb77b4361b8de62e6ffead34f54d4: próby 1–2 success; próba 3 failure w przygotowaniu hosta, przed uruchomieniem daemonu i przed Python probe. Log: Job for user@1001.service failed because the control process exited with error code. Szczegółowa przyczyna systemd nie została zarejestrowana. Nie interpretować jako niezaliczenia właściwego testu izolacji ani uznawać za trzeci zaliczony przebieg.
- Commit 3720e055f4ac415b67c269b10ae3854d15731ba4: najpierw linger i runtime-dir, restart aktywnego user managera tylko gdy brak wymaganych kontrolerów, zachowana kontrola cgroup bieżącego procesu, kontrola socketu bus i diagnostyka status/journal na błędzie. To poprawka hipotezy dotyczącej cyklu życia sesji, nie potwierdzona diagnoza pierwotnego błędu. Nie osłabiono sprawdzania limitów ani polityki aplikacji.
- Rootless 2+1 reset do 0/3 na nowym SHA. Bez zmian kodu produkcyjnego, testów aplikacji, kanonicznych TeX/Lean i manifestu. execution_allowed=false, certificate=false. Nie przechodzić do prób wykonania kandydatów.

## Pierwsza kontrola po poprawce cyklu życia sesji (24.11.2026)

- [Rzeczywisty rootless preflight 45424815794](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45424815794), SHA 3720e055f4ac415b67c269b10ae3854d15731ba4, próba 1: success. Wszystkie kroki przeszły, w tym przygotowanie hosta, uruchomienie daemonu, rzeczywista inspekcja i usunięcie kontenera. Docker 28.0.4, Delegate=yes, ControlGroup=/user.slice/user-1001.slice/user@1001.service. Raport: configuration_checked, cleanup_status=removed, execution_allowed=false, proof_status=not_run, certificate=false.
- Cztery bloby (workflow rootless, transport, polityka runnera i skrypt probe) identyczne z bieżącą gałęzią. Pierwszy sukces nowego workflow potwierdza działanie na tym hoście, ale nie rozstrzyga przyczyny poprzedniej awarii ani powtarzalności.
- Zlecono drugą próbę joba 138553794864 na niezmienionym SHA. Stan rootless 1/3, aplikacja 3/3 na wcześniej wskazanym niezmienionym kandydacie. Nie uznawać samego zlecenia za zaliczenie. Bez zmian implementacji i bez uruchamiania kodu Lean.

## Kryteria odbioru następnego testu runtime (projekt, nie wykonanie)

Audyt projektu: preflight przed startem nie wystarcza do potwierdzenia egzekwowania ograniczeń. Poniższe wymagania są bramką odbioru następnego podetapu, a nie wynikami testów. Implementację rozpocząć dopiero po stabilizacji obecnego workflow.

| ID regresji | Warunek i obserwowalny dowód |
|---|---|
| L156C-RT-01 | Wyłącznie stały, lokalny obraz testowy i znany nieszkodliwy entrypoint, przypięty ID. Walidacja silnika, obrazu i kontenera przed startem, brak danych użytkownika i sieci podczas testu. |
| L156C-RT-02 | W działającym kontenerze odczytać rzeczywiste cgroup v2: memory.max = 2147483648, memory.swap.max = 0, pids.max = 64, cpu.max z dodatnią kwotą i stosunkiem kwota/okres = 1. Brak odczytu lub rozbieżność blokuje odbiór; same metadane Docker inspect nie wystarczą. Nie prowokować alokacji 2 GiB na współdzielonym runnerze. |
| L156C-RT-03 | Potwierdzić UID/GID 65534, CapEff=0, NoNewPrivs=1, Seccomp=2. Odczytać rzeczywiste mountinfo: root ro, /tmp rw/noexec/nosuid/nodev; próba zapisu w katalogu przygotowanym z prawami dla UID 65534 na rootfs musi zawieść z EROFS, zapis do /tmp musi się udać. |
| L156C-RT-04 | Brak interfejsu sieciowego poza loopback i brak domyślnej trasy; bez rzeczywistego odpytywania zewnętrznych serwisów. Zweryfikować brak bind mountów i brak socketu daemonu wewnątrz kontenera. |
| L156C-RT-05 | Stały fixture emitujący ograniczone wyjście, kończący się błędem i przekraczający krótki limit czasu: osobne przypadki. Wymagać dowodu zatrzymania kontenera w daemonie oraz usunięcia po ID, nie tylko zakończenia lokalnego CLI. Przy niepotwierdzonej identyfikacji lub sprzątaniu status blocked i jawny raport; bez awaryjnego uruchomienia na hoście. |
| L156C-RT-06 | Raport odrębny od statusu dowodu i manifestu, zawiera SHA checkoutu, ID obrazu, wersję silnika, faktyczne obserwacje i status każdego przypadku. Brak danych = niezaliczone, bez automatycznego podnoszenia certificate. |

To nie jest pełna specyfikacja sandboxa ani test odporności na dowolny złośliwy obraz. Nie uruchamiać niezaufanego Lean. Nadal execution_allowed=false, proof_status=not_run i certificate=false. W tej iteracji nie zmieniono implementacji ani workflow, więc istniejący licznik 2+1 nie ulega resetowi z powodu tego wpisu.

## Zamknięcie preflight 2+1 i pierwszy test runtime (24.11.2026)

- Rootless [45424815794](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45424815794), SHA 3720e055f4ac415b67c269b10ae3854d15731ba4: próby 1–3 success, ostatni log configuration_checked, cleanup_status=removed, execution_allowed=false, proof_status=not_run, certificate=false. Wraz z wcześniejszym 3/3 pełnego CI aplikacji spełniono powtarzalność dotychczasowego preflight, nie wykonania kodu. Pliki transportu, polityki, skryptu i workflow przed zmianą zgodne z kandydatem.
- Commit e423dae440a5fb4e0dd359b3d3b3b14c662c7133: pierwsza część RT-01/02, wyłącznie CI. Lokalny obraz z ustalonym skryptem BusyBox odczytuje cztery rzeczywiste pliki cgroup v2 po inspekcji kontenera i starcie. Walidacja dokładnych wartości RAM, swap, PID i proporcji CPU; odrzucenie brakujących/obcych/niejednoznacznych danych. Kontrola stanu exited, kodu 0, braku OOM i usunięcie po ID również przy błędzie. Brak Lean, danych użytkownika i nowych uprawnień aplikacji. Nie jest to jeszcze test obciążeniowy ani kompletne RT-03–06.
- Commit 900e8ac6ff58d39b9fb608519f6a702714549f82: trzy trwałe testy parsera obserwacji, w tym brak, duplikat i wartości niespełniające polityki. To testy walidatora, nie dowód rzeczywistej izolacji. CI nowego podetapu jeszcze niepotwierdzone w chwili zapisu; nowa stabilizacja 0/3. Nie przechodzić do wykonywania kandydatów Lean. Kod backendu, manifest, kanoniczne TeX/Lean bez zmian.

## Pierwsza kontrola stabilizacyjna obserwacji cgroup runtime (24.11.2026)

- Kandydat 900e8ac6ff58d39b9fb608519f6a702714549f82: [pełne CI aplikacji 45425911822](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45425911822) i [rzeczywisty Docker 45425911930](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45425911930), obydwa próba 1 completed/success. Wcześniejszy e423dae4 również przeszedł oba workflow, lecz nie liczy się jako powtórzenie identycznego SHA.
- Aplikacja: 864 testy ogółem, 854 zaliczone, 10 sklasyfikowanych pominięć, brak niesklasyfikowanych; trzy nowe testy walidatora runtime ok. Rzeczywisty Chromium passed, 532 rozdziały, javascript_errors=[].
- Rzeczywisty kontener: ATLAS_ROOTLESS_RUNTIME status=runtime_limits_checked, memory.max=2147483648, memory.swap.max=0, pids.max=64, cpu.max=100000 100000, cleanup_status=removed, execution_allowed=false, proof_status=not_run, certificate=false. Odczyt czterech wartości wewnątrz działającego kontenera, nie tylko Docker inspect.
- Sześć blobów (skrypt, test, transport, polityka runnera, dwa workflow) bieżącej gałęzi identycznych z kandydatem. Zlecono próbę 2 obu jobów na tym samym SHA (138557724129 i 138559141699). Licznik 1/3 każdego rodzaju, do czasu rzeczywistego potwierdzenia wyniku.
- Sceptyczna kontrola zakresu: obserwacje potwierdzają wartości cgroup w tym konkretnym uruchomieniu, ale nie testują obciążeniowo OOM, throttling ani wyczerpania PID. Fixture nie uruchamia Lean, nie sprawdza jeszcze RT-03–06, a poprawne sprzątnięcie przy normalnym wyjściu nie dowodzi sprzątnięcia po timeout. Nie zmieniono implementacji ani polityki wykonawczej; następny krok to druga kontrola stabilizacyjna, bez rozszerzania zakresu.
