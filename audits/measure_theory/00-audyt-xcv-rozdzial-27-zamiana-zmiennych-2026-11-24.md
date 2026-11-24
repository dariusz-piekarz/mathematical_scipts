# Audyt XCV (95) — rozdział 27: Miary na rozmaitościach
Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Punkt startowy
HEAD 2ce393c30501632e4e3076cf279c4391d2c00937; odczyt historii i pełnego raportu XCIV potwierdza zapisane zamknięcie rozdziału 26 (CI i oględziny 11 stron według raportu). Odczytano AGENTS.md, standardy terminologiczne, oba pliki główne książek oraz pełny rozdział 27. Nie zmieniano innych rozdziałów.

## Ustalenia i korekty
- Regularność: dodatnia ciągła gęstość na zwartej kuli współrzędnych daje lokalną skończoność; przeliczalne pokrycie i regularność miar Radona uzasadniają tezę.
- Zbiory zerowe: dodatnie minima na wyczerpaniu zwartym uzasadniają równoważność; lokalna postać immersji i przeliczalne podpokrycie dają zerową miarę zewnętrzną. Borelowskość obrazu pozostaje jawną hipotezą.
- Radon–Nikodym: twierdzenie stosowane na borelowskiej sigma-algebrze daje od razu funkcję borelowską, nie tylko mierzalną względem uzupełnienia. Lokalna całkowalność wynika ze skończoności na zwartych. Doprecyzowano jednoznaczność gęstości rozkładu Lebesgue'a prawie wszędzie.
- Zamiana zmiennych: wcześniejsze wymaganie nośnika zawartego w mapie nie uzasadniało zastosowania do funkcji charakterystycznych części podziału (domknięcie części może wyjść poza mapę). Zastąpiono je znikaniem poza otwartym zbiorem i skonstruowano przeliczalne pokrycie jednocześnie podporządkowane mapom źródła i celu. Sumowanie uzasadniono zbieżnością monotoniczną. Poprawiono argument miary obrazowej: dla A borelowskiego w N funkcją na M jest chi_{F^{-1}(A)}, a nie chi_A. Odwrotny jakobian daje prawidłową gęstość.
- Jakobian i przykład konforemny: iloraz pierwiastków wyznaczników i czynnik e^{n phi} są zgodne z definicją.
- Produkt: uzupełniono brakujące uzasadnienie równości borelowskiej sigma-algebry produktu i produktowej sigma-algebry; blokowy wyznacznik i Tonelli są właściwe.
- Terminologia: drugi aksjomat przeliczalności, bezwzględna ciągłość; zachowano chi_A i wszystkie etykiety.
- Skrypt całkowy ma odmienną historyczną makrodefinicję funkcji charakterystycznej; nie zmieniano go w tym audycie. Nie scalano treści.

## Weryfikacja
10 celowanych zamian tekstu; 323 wiersze po korekcie. Ponowny odczyt źródła potwierdził blob f7b75fcadafd303b45355af0b72d3e00e4439832. Commit 20a74f961d635426c1b911af4d4353981dfb6000 odczytany przez API: wyłącznie rozdział 27. Wszystkie 11 etykiet zachowane, bez duplikatów; 8 wystąpień odsyłaczy (4 lokalne, 4 zewnętrzne); sparowanie środowisk poprawne, 7 dowodów, brak środowisk figure/tikzpicture. Nie uruchomiono kompilacji ani testów repozytorium; nie oglądano PDF. Zewnętrzne cele odsyłaczy wymagają jeszcze weryfikacji w źródłach.

## Status
NIESTABILNY — po korektach konieczny pełny niezależny audyt tego samego rozdziału, w tym samodzielność hipotez, dowody lokalnego kryterium w uzupełnieniu, wzór jakobianu, kontrola odsyłaczy, CI i PDF. Nie przechodzić do 28. Brak nowych treści wymagających zatwierdzenia.
