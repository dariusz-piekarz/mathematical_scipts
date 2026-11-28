# PDE I — rozdział 08: kontrola techniczna po drugiej lekturze

Data: 2026-11-25. Iteracja 122. **Aktualizacja w audycie 126: łączna kontrola techniczna PASS. Rozdział oczekuje na ostatnie 7 kryteriów lektury kontrolnej.**

- Źródło po drugiej lekturze: 7e35b139c158ab1a6230fa1c2a7778d14a2743c2. Rejestr: b26d3381fe6c3f1752b44ce2090650aa8d577939. Commit rejestru: 5864e953691a5cef7da3034a1254cef88ecc4603.
- Przebieg docelowy [45595506552](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45595506552), head 5864e953691a5cef7da3034a1254cef88ecc4603: status queued w chwili kontroli.
- Porównano drzewa aktualnej gałęzi i head przebiegu: 12/12 identycznych blobów wejściowych (rozdziały 04–08, rejestr i test 08, workflow, książka, manifest, listingi i preambuła Atlasu).
- Ponowiono niezależne sprawdzenie struktury na treści z head przebiegu: 39 unikatowych etykiet; 92 wystąpienia odsyłaczy, każdy cel lokalny lub jednoznacznie odnaleziony w rozdziałach 04–07; 10 różnych celów zewnętrznych, każdy występuje raz. 92/92 ID kryteriów w kolejności 001–092, bez duplikatów, z istniejącymi kotwicami. Stos środowisk pusty, uproszczona kontrola niezacytowanych nawiasów klamrowych (bez komentarzy) daje końcową i minimalną głębokość 0. 12 sekcji, w tym podsumowanie. Kolejność input zgodna z manifestem, pozycja rozdziału 8. Wspólna konfiguracja listingów występuje po jednym razie w książce i preambule Atlasu.
- Zweryfikowano logi poprzedniego zaliczonego przebiegu [45592899920](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45592899920), head 34012c11133261c8b5d75a3a73bb4a0eb96f3056 (po audycie 116), job 139131418748: 12/12 OK w 0,097 s, 92 kotwice, 39 etykiet, 84 odsyłacze, kompilacja i diagnostyka PASS, 27 stron PDF. Plik testowy niezmieniony od pierwszego CI (blob a70c18b1384563d26c1a7ac8894ebd52fec27164). Wynik poprzedniego CI nie potwierdza kompilacji po audycie 121.
- Kolejne sprawdzone przebiegi dla audytów 117–120 oczekiwały w kolejce. Nie uruchamiano duplikatu workflow, nie zmieniano źródła ani testów, nie anulowano żadnych przebiegów.

Blokada: oczekujący przebieg końcowy. Nie ma jeszcze końcowego PDF ani jego diagnostyki i kontroli wizualnej. Nie wykonywano formalizacji Lean. Następna iteracja: sprawdzić przebieg docelowy i aktualność jego wejść; w razie błędu poprawić przyczynę, w razie PASS sprawdzić PDF i przeprowadzić niezależną lekturę kontrolną. Bez nowych tematów.


## Domknięcie łącznej kontroli technicznej — audyt 126

- Przebieg 45595506552, job 139140395511, head 5864e953691a5cef7da3034a1254cef88ecc4603: completed/success. Aktualne 12/12 blobów wejściowych identyczne z head tego przebiegu. Kontrola struktury z audytu 122 pozostaje aktualna, a końcowy CI potwierdził 92 kotwice, 39 etykiet i 92 rozwiązane wystąpienia odsyłaczy.
- Log wykonania: 12 testów w 0,052 s, OK. Są to testy wykonywalne wybranych przykładów, nie formalne dowody.
- Artefakt 15014325429: ZIP 8446965 B, zweryfikowany SHA256 bac2fb6a255deecbbfd6aa52a812dd881d6c0043076590c0d05858e75ceeca57. PDF 30 stron A4, 503296 B, SHA256 455ef0f51648459583d7e4cbee9653597d123bf27cf478f206939d2ae7c50b3f.
- Z finalnego pliku log: brak niezdefiniowanych odsyłaczy, brak Overfull/Underfull, brak Missing character i Undefined control sequence. Pozostało 21 ostrzeżeń hyperref o pustym celu odsyłacza: w izolowanej kompilacji odsyłacze do innych rozdziałów mają numery, ale nie mają docelowych stron w tym PDF. Nie jest to weryfikacja klikalności w całym tomie. Wcześniejsze ostrzeżenie Underfull nie występuje.
- Obejrzano wszystkie 30 renderów stron z artefaktu na pięciu planszach po sześć stron. Nie widać obcięć, nachodzenia treści ani pustych stron; podsumowanie na ostatniej stronie celowo zajmuje tylko jej górną część. Jest to kontrola układu w skali plansz, nie ponowne odczytanie każdego symbolu w powiększeniu. Brak zmian źródła po kompilacji.
- Kontrola techniczna (struktura, CI/testy, wizualna kontrola PDF) zakończona wspólnie w audycie 126. Nie kompilowano całego tomu ani nie wykonywano Lean. Pozostałe kryteria lektury kontrolnej 086–092; dopiero po ich zaliczeniu i sprawdzeniu tożsamości wejść można oznaczyć rozdział 08 jako stabilny.
