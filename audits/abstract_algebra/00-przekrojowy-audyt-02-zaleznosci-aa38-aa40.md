# Algebra abstrakcyjna — audyt przekrojowy 02: zależności AA-38–AA-40

Data: 2026-11-23. Rodzaj: pojedyncza nowa kontrola przekrojowa (nie pełny audyt 42 rozdziałów).
Gałąź: `biblioteka-matematyczna-iteracja-6`. HEAD bezpośrednio przed publikacją: `fd750d583d071b4ac053135ae5a88892bd0cdaac`.

## Zakres i wersje
- AA-38, `38-lemat-normalizacyjny-noether.tex`: Git blob `2edea1072ab0b052f492e88f9dd508ba5c938d3a`.
- AA-39, `39-wymiar-krulla-i-lancuchy-idealow-pierwszych.tex`: Git blob `1b8990241d26cbf461a0e7b4a07546a3ef77fa9e`.
- AA-40, `40-calokowitosc-i-twierdzenia-o-idealach-pierwszych.tex`: Git blob `101cd301f88c9e1cc84e89d2ce3cb57bc7c8fe2b`.
- Weryfikacja dodatkowa: AA-37, Git blob `b710ae2447d41aef8681de6d55f4c6d3709616c1`.

## Rzeczywiście wykonane kontrole
1. Pobrano i porównano trzy pełne źródła AA-38–AA-40. Skan statyczny wykrył **52 definicje etykiet** i **39 użyć poleceń** `\\ref`, `\\eqref`, `\\autoref`, `\\cref`, `\\Cref`. **0 powtórzeń etykiet** w tych trzech źródłach; **6 odwołań między nimi** zostało rozwiązanych.
2. Spośród 39 użyć trzy wskazują poza analizowany zestaw: `aa:tw:transcendence-degree` (AA-38), `aa:ch:pierscienie` i `aa:ch:lokalizacja` (AA-39). Pierwszą etykietę potwierdzono w AA-37. Dwie pozostałe wymagają weryfikacji w wcześniejszych rozdziałach; nie uznano ich za błędy.
3. Niezależnie prześledzono łańcuch logiczny w AA-40: lying-over + going-up zapewniają `dim A <= dim B`; nieporównywalność ideałów daje `dim B <= dim A`. Argument używa właściwych założeń całkowitości i nie wymaga skończoności modułowej.
4. Sprawdzono dowód `dim K[X_1,...,X_n]=n` w AA-40: dolne oszacowanie przez jawny łańcuch ideałów pierwszych, górne przez element niezerowy w drugim ideale łańcucha, trójkątną zmianę zmiennych, moniczność, skończoność modułową ilorazu, całkowitość i indukcję. Dla `n=0,1` podano osobne przypadki. Nie znaleziono luki w skontrolowanym łańcuchu.
5. Sprawdzono dowód nieporównywalności: minimalny stopień monicznego równania dla niezerowego elementu ideału oraz skrócenie przez ten element w dziedzinie dają sprzeczność. Warunek dziedziny jest spełniony przez iloraz względem ideału pierwszego.

## Wyniki i ograniczenia
- Kontrola logiczna wymienionych argumentów: **bez nowej potwierdzonej usterki**; nie jest to deklaracja pełnej stabilności całych rozdziałów.
- Test statyczny etykiet: **52 definicje, 39 użyć, 0 duplikatów wewnątrz AA-38–AA-40**; 2 odwołania zewnętrzne pozostają do sprawdzenia.
- Kompilacja LaTeX: **nieuruchomiona**. Inspekcja PDF: **niewykonana**. GitHub Actions: **niezweryfikowane**.
- Źródła rozdziałów, katalog, README i workflow: **bez zmian**. Brak podstaw do resetowania licznika stabilizacji AA-38–AA-40, ale ten audyt nie jest dodatkowym pełnym audytem stabilizacyjnym.
- Nie dopisywano twierdzeń ani lematów.

## Następny odrębny zakres
Po ponownym sprawdzeniu HEAD i ewentualnego AA-43 zweryfikować globalnie dwie pozostałe etykiety i rozszerzyć test integralności odsyłaczy na inne rozdziały, bez ponownego liczenia AA-38–AA-40 jako nowego audytu.
