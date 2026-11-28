# PDE-06 — iteracja 83: audyt kontrolny i zamknięcie stabilizacji

Data: 2026-11-25. Kandydat: commit 4647cf25e044a36438f81cc9add2b3165900740b, blob źródła ed1b662b3f324d0efca35e7a77e9729217b125f1. Rejestr 6293e2798c2b66b9a7fd126670bea0988b76ba00; testy ccbb8b39902904365b1403df5eefa10ff40d2134; workflow 80e96a751f7cbc8418bd364888e2c17037b080b0.

## Audyt kontrolny

Porównano aktualne źródło z kandydatem e9c45024f3ccfc565f94ef6e713ddbb7d771eb99: wszystkie sekcje dowodowe 6.1–6.8 są identyczne. Ponownie sprawdzono korektę 6.9 w kontekście założeń 6.5 (gładkie dane początkowe o zwartym nośniku oraz wspólny zwarty nośnik wymuszenia). Nie rozszerzano zakresu. Skontrolowano spójność matematyczną przejść między sekcjami: normy na torusie i odcinku, czynnik 2/L w bazie nieunormowanej wobec współczynników ortonormalnych, dodatnie wartości własne i wykładniki zaniku, energia modów, zgodność wzorów Duhamela, ważony operator Greena i odwrotność jego wartości własnych, baza iloczynowa i krotności, odwrotny operator cieplny na jego właściwej dziedzinie. Nie wykryto nowego istotnego błędu. Kontrola końcowa nie jest trzecią pełną lekturą wszystkich dowodów od zera: opiera się na dwóch lekturach, sprawdzeniu ich pokrycia oraz kontroli spójności i ostatniej zmiany.

Raporty 79–82 zawierają dokładnie 42 różne ID PASS (w tym jedno PASS po korekcie), bez luk i powtórzeń względem rejestru. Wszystkie 42 kotwice istnieją. Źródło ma 9 sekcji, 14 środowisk dowodowych, 38 unikatowych etykiet i 52 odsyłacze; środowiska poprawnie zagnieżdżone. Cztery cele zewnętrzne chap:pde-heat, chap:pde-wave, chap:pde-distributions, chap:pde-fourier-Rd występują po jednym razie w aktualnych rozdziałach 04,05,07,08.

## Wykonane kontrole

CI 45573770161, job 139066525718: completed/success, wszystkie kroki zaliczone. Log potwierdza Ran 10 tests in 0.293s, OK; 42 kotwice, 38 etykiet, 52 odsyłacze; 16 stron. Terminologia 45573770164 i aplikacja 45573770314: completed/success dla tego samego commitu. Testy są skończonymi kontrolami rachunkowymi; nie dowodami ogólnych twierdzeń.

Pobrano artefakt 15002772779, 5164259 bajtów; lokalny SHA256 zgodny z GitHub: 6d1ddd133aaad267343f2d8b4c1231d390f7525de9df1ba4de22ab2e6b1bc0b0. Rozpakowano 19 plików; pdfinfo potwierdza 16 stron A4. Końcowy log nie zawiera ostrzeżeń objętych bramką diagnostyczną (Overfull, Missing character, Undefined control sequence, niezdefiniowane odsyłacze). Porównano wszystkie 16 PNG piksel po pikselu z artefaktem 15002486925 oglądanym w iteracji 78: strony 1–15 identyczne, zmiana wyłącznie na stronie 16. Obejrzano aktualny render strony 16: poprawione założenia widoczne, brak dostrzeżonych obcięć lub nakładania elementów. Kontrola wizualna aktualnej wersji zaliczona poprzez porównanie i oględziny zmienionej strony.

## Decyzja

Rozdział 06 USTABILIZOWANY dla wskazanego bloba. Dwie pełne lektury 9/9, 42/42 kryteriów semantycznych, końcowa kontrola spójności, testy 10/10, CI i kompilacja izolowanego rozdziału, kontrola wizualna — zaliczone. Brak otwartych istotnych błędów w ustalonym zakresie. Nie wykonano formalizacji Lean ani kompilacji całego tomu; nie oznaczamy ich jako zaliczone. W izolowanym PDF zewnętrzne odsyłacze mają numery, nie aktywne cele w nieobecnych rozdziałach. Każda przyszła zmiana źródła wymaga adekwatnej ponownej kontroli.

Postęp: 6/33 rozdziałów ustabilizowanych. Kolejny rozdział 07 — Dystrybucje i słabe pochodne, pierwszy szczegółowy audyt od początku, zgodnie z ustalonym cyklem.
