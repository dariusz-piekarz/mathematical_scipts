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
