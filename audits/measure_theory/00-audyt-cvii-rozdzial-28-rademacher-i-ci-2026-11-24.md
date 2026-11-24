# Audyt CVII (107) — kontrola CI, PDF i mierzalności pochodnych
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy c5ec84b77c25b751026b79f8c9fb899e918f9763, rozdział bez zmian od CVI.

## Weryfikacja CI i PDF wersji CVI
Przebieg 45350605640 dla a143b2c727bb5553d87566373c8de2dd2952ab48: zadania testów i PDF zakończone sukcesem; 7/7 regresji i 4/4 integralności. Zadanie publikacji statusów było jeszcze w kolejce w chwili pierwszego odczytu.
Artefakt 14899339686 (7780970 bajtów), SHA-256 zweryfikowany: 0c2ce2980edee8e1df955e83ceffb0ab216213926df375a105591deca1764e4d.
Tom 275 stron (2006445 bajtów), rozdział 20 stron, 28 lokalnych i 9 zaimportowanych etykiet. Log izolowany: 0 Overfull i 0 Underfull; pełny tom: 0 Overfull, 13 Underfull. W tekście izolowanego PDF brak ??.
Wyrenderowano i obejrzano 20 stron izolowanego PDF w pięciu arkuszach po cztery strony. Nie zauważono ucięć, nakładania elementów ani brakujących glifów. Strony 17–18 z poprawionym rachunkiem blokowym i całką są czytelne; ostrzeżenie CVI usunięte. Nie przeprowadzano oględzin wszystkich stron tomu.

## Kontrola matematyczna
Trzy celowane zmiany w commicie fcbbc9fc4c7c053d20753513a5171ac726bd59d6 (blob 40848d314c735bf5626c1d93e591d556c6229f70).
- W twierdzeniu o wykresie jawnie uzasadniono sigma-skończoność obu miar i bezwzględną ciągłość przez przeliczalne pokrycie kulami, przed zastosowaniem Radona–Nikodyma.
- W lemacie o słabych pochodnych uzupełniono borelowskość zbioru istnienia pochodnej przez przeliczalny warunek Cauchy'ego dla wymiernych przyrostów, równoważność z pełną granicą przez ciągłość w parametrze, zastosowanie Tonellego do zbioru braku pochodnej oraz jawny borelowski reprezentant. Uwzględniono wymiar jeden.
- W dowodzie Rademachera rozpisano obie implikacje kryterium borelowskiego, oszacowanie normy różnicy macierzy, zbieżność macierzy i resztę po przejściu do granicy oraz jawny przeliczalny opis zbioru różniczkowalności.
Wszystkie 28 etykiet zachowano.

## Otwarte
Ponowny CI po poprawkach CVII, kontrola PDF i kolejna niezależna iteracja bez pomijania kroków dowodowych. Wyniki techniczne CVI nie stanowią weryfikacji CVII. Rozdział 28 nadal otwarty, stan 27/31. Nie przechodzić do 29.
