# PDE-06 — iteracja 76: testy wykonywalne i CI

Data: 2026-11-25. Źródło po pierwszej lekturze: blob 7bfc61b06a70474a4426a51bb473647b3f7e269a; rejestr 42 kryteriów semantycznych: blob 5b5ed2020e6819adda63d3002306ba30c68ed40e. Nie zmieniano treści rozdziału.

## Testy wykonywalne

Dodano tests/mathematical/partial_differential_equations/chapter-06/test_fourier.py, commit 7798ffdd3ae24a3f052df1152929544548388183, blob ccbb8b39902904365b1403df5eefa10ff40d2134. Dziesięć metod unittest obejmuje skończone przykłady jądra Fejéra, nieparzyste przedłużenie zespolone, nierówność Poincarégo, normalizację periodyzowanego Gaussa, zanik ciepła, energię zespolonego oscylatora, Duhamela dla wymuszenia liniowego w czasie, funkcję Greena dla p=1,q=0,w=2, arytmetykę krotności prostokąta i skończone obcięcia odwróconej ewolucji cieplnej. ID powiązanych kryteriów w komentarzach metod.

Wykonano lokalnie python3 /tmp/pde06/test_fourier.py -v: Ran 10 tests in 0.247s, OK. Git hash-object lokalnego pliku oraz blob odczytany z repozytorium są identyczne: ccbb8b39902904365b1403df5eefa10ff40d2134. Testy stanowią skończone rachunki i przykłady (częściowo kwadratura numeryczna), nie dowody ogólne, nie analizują bezpośrednio twierdzeń w TeX i nie zastępują 42 kontroli semantycznych.

## Workflow

Dodano .github/workflows/partial-differential-equations-ch06.yml, commit 2ddae7a2476ebf76a639b1b84e415d31923a4796, blob 80e96a751f7cbc8418bd364888e2c17037b080b0. Adaptacja workflow rozdziału 05: testy, kontrola etykiet, odsyłaczy, kotwic kryteriów, struktury, manifestu i kanonicznych listingów; izolowana kompilacja z preambułą księgi, zewnętrzne odsyłacze rozdziałowe jako numery ustalone z kolejności księgi; diagnostyka, render stron i artefakt PDF/log/tekst/PNG.

Dwa zapytania o przebiegi (według SHA kandydata i gałęzi) nie zwróciły jeszcze przebiegu PDE-06; zapytanie o przebiegi przez nazwę pliku workflow zostało odrzucone przez konektor. Nie potwierdzono uruchomienia ani wyniku CI, kompilacji, kontroli wizualnej lub formalizacji Lean. Następny etap: odczytać rzeczywisty przebieg dla kandydata, rozliczyć kroki i diagnostykę, obejrzeć PDF, naprawić wykryte usterki i przeprowadzić niezależną lekturę 9 sekcji. Stabilizacja pozostaje otwarta.
