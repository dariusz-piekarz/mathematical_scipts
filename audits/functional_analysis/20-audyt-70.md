# Rozdział 20 — audyt 70 (2/5, pierwszy przegląd, 0/3 stabilizacji)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Zakres
Podsekcje 1–2: definicja pochodnej i ciągłość w topologiach dualnych; skoki, funkcja Heaviside'a i osobliwości punktowe.

## Poprawki
Doprecyzowano ciągłość funkcjonałów, wielowskaźniki, ciało skalarów i kwantyfikatory. W dowodzie ciągłości różniczkowania funkcji testowych rozpisano niepowiększanie nośnika, włożenia etapów, własność uniwersalną i zachowanie ograniczoności. Jawnie sprawdzono przemienność pochodnych dystrybucyjnych i znaki, zgodność przedłużania zerem z różniczkowaniem oraz inkluzję nośników. W dowodzie zgodności z pochodną klasyczną na dowolnym zbiorze otwartym wykorzystano funkcję odcięcia, przedłużenie zerem i Fubiniego, zapisano całkowanie przez części i jednoznaczność słabej pochodnej. Rozpisano obliczenia dla funkcji Heaviside'a, znaku i modułu. W twierdzeniu o skoku wyprowadzono obie całki brzegowe z poprawnymi znakami i uzasadniono oba przejścia graniczne. Sprawdzono założenia przykładu częściowo gładkiego, zmieniono oznaczenia funkcji charakterystycznych na chi, dodano konkretną funkcję testową rozróżniającą deltę od jej pochodnej i odsyłacz do dokładnego rzędu. Nie zmieniono zakresu tematycznego.

## Kontrole
Źródło e780a7f367bf961c82ae15a9b73b8f19c1fb5088, blob 0bd5eb3391b37ffc4863f9cd4b4615a23fef8fe6. 678 wierszy, 24/24 unikatowych etykiet, 15/15 odsyłaczy ref i hyperref rozwiązanych w 17–20, zbilansowane środowiska, 15/15 warunków tekstowych. Dodano trzy metody testowe (1087317611db5ec73b7bdc2d617e9b0d4b61539f), w tym dokładne rachunki wielomianowe znaków skoku na przedziale. Dodano workflow pełnego kontekstu 01–20 (9bb1dfe1a85dec24f946694ad61f704e736d60a0), bieg 45406443951 oczekiwał przy kontroli. Nie potwierdzono jeszcze wykonania pełnych testów i kompilacji rozdziału 20. Kontrola wizualna rysunku po kompilacji pozostaje do wykonania. Globalny CI stylu kodu 45405481160 zakończył się sukcesem: synchronizacja preambuł, kompilacja Python i Julia, diagnostyka oraz upload. Brak kodu źródłowego w audytowanych podsekcjach rozdziału 20; nie wymagają dodawania przykładów programistycznych. Nie wykonywano formalizacji Lean.

## Następna iteracja
Audyt 71: podsekcje 3–4 (mnożenie, Leibniz, transpozycja), kontrola CI. Następnie podsekcja 5, a po pełnym pierwszym przeglądzie trzy osobne pełne stabilizacje.
