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
