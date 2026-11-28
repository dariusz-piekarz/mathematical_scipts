# RRC 12 — iteracja 202: kontrola przekrojowa i CI

Źródło przed a9f10e9609fbc124c7a6d85b9616378f4a862b41, po c673beaec26ce80dc4af0d4cf1b7bbef9819d43a (commit c7629cded8fc9e179981555b1cd6d31386b96fed).
Kontrola przekrojowa dziewięciu sekcji: usunięto niejednoznaczne wskazanie zwartości K, ujednolicono pozostałe różniczki miary Lebesgue'a z argumentem, usunięto nieaktualny komentarz o rozdziale 13. Zachowano kolejność 33 etykiet. Nie deklarujemy zakończenia czwartej pełnej lektury merytorycznej 68 kryteriów.

Dodano 10 wykonywalnych metod regresyjnych (struktura, cele odsyłaczy, rezolwenta, minmax, generator i wygładzanie, Duhamel, nośniki kontrprzykładu, energia, unitarność, krotności) w tests/mathematical/partial_differential_equations/chapter-12/test_spectral.py, commit f7e274c6229dbb939b9c4764d3e67709abb945b9. Kontrole skończone nie dowodzą twierdzeń nieskończeniewymiarowych.

Dedykowane CI .github/workflows/partial-differential-equations-ch12.yml, commit 1787dabc9ca2898e7c1628fb72728a6da261a103. Przebieg 45685098403: krok testów regresyjnych SUCCESS, krok kontroli odsyłaczy i przygotowania samodzielnego rozdziału SUCCESS. W chwili odczytu kompilacja trwała; końcowy wynik, diagnostyka i kontrola wizualna niepotwierdzone. Numeracja zewnętrznych odsyłaczy w samodzielnym PDF odpowiada numeracji książki, bez linków do nieobecnych rozdziałów. Nie potwierdzono jeszcze pełnego CI Atlasu, indeksu atlasref, PDF całej książki ani Lean.

Następnie: odczytać wynik przebiegu, naprawić ewentualne diagnostyki, pobrać PDF i przeprowadzić kontrolę wizualną; domknąć czwarty przebieg merytoryczny 001–068 bez zbędnych rozszerzeń i wykonać niezależny audyt kontrolny po stabilizacji.
