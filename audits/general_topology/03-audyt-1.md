# Topologia ogólna — rozdział 03 „Odwzorowania ciągłe”

- Data: 2026-11-21.
- Wersja: 0.1 po audycie 1.
- Status: roboczy, 0/2 kolejnych czystych audytów; bez pushu do GitHuba.
- Zweryfikowana gałąź repozytorium: `biblioteka-matematyczna-iteracja-6`; rozdziały 01 i 02 były już na gałęzi, 03 jeszcze nie.

## Zakres

1. Ciągłość przez przeciwobrazy otwartych i domkniętych podzbiorów.
2. Charakteryzacje ciągłości przez domknięcie i otoczenia.
3. Ciągłość w punkcie; równoważność z warunkiem epsilon–delta w przestrzeniach metrycznych.
4. Sprawdzanie ciągłości na bazie i podbazie przeciwdziedziny.
5. Składanie, ograniczanie dziedziny, przeciwdziedzina podprzestrzenna oraz sklejanie na otwartych i skończonych domkniętych pokryciach.
6. Odwzorowania otwarte i domknięte; kryteria za pomocą wnętrza i domknięcia.
7. Homeomorfizmy, zachowanie operacji topologicznych, zanurzenia topologiczne.

## Audyt matematyczny

- Zweryfikowano kierunki inkluzji w warunkach ciągłości, otwartości i domkniętości.
- Przeanalizowano przypadki pustej dziedziny, pustej przeciwdziedziny, pustej podbazy i pustych rodzin.
- Zweryfikowano kontrprzykłady: dyskretna → antydyskretna oraz kierunek odwrotny; nieciągłość funkcji skokowej; brak sklejania na dowolnych zamkniętych pokryciach.
- W dowodzie lematu o sklejaniu dopisano jawny argument uzasadniający, że podzbiór domknięty w podprzestrzeni $F_j$ ma postać $F_j\cap E_j$ dla pewnego zbioru $E_j$ domkniętego w $X$.
- W uwadze o przeciwobrazach uporządkowano skład długich wzorów, eliminując ostrzeżenie składu.
- Nie dodawano nowych tematów po zamknięciu zakresu rozdziału.

## Testy

- `tools/tests/test_general_topology_ch03.py`: PASS; 24 907 par odwzorowanie/przestrzenie (liczone ze wszystkimi topologiami na zbiorach od 0 do 3 punktów); 11 345 ciągłych przypadków; 184 homeomorfizmy.
- Sprawdzono równoważności: preobrazy otwartych, preobrazy domkniętych, warunek domknięcia obrazu, preobrazy domknięć, warunek lokalny; odwzorowania otwarte i domknięte; homeomorfizmy i zachowanie wnętrza/domknięcia/brzegu/zbioru pochodnego; sklejanie na pokryciach dwuelementowych; klasyfikację otwartych przez przestrzeń Sierpińskiego.
- Testy regresyjne rozdziałów 01 i 02: PASS.
- Kompilacja `general_topology_ch03.tex`: PASS, 8 stron, bez ostrzeżeń.
- Kompilacja `general_topology.tex` (rozdziały 01–03): PASS, 27 stron, bez ostrzeżeń.
- Etykiety i `\ref`: 124 unikatowe etykiety dla trzech rozdziałów, 7 wykorzystanych odsyłaczy, bez odsyłaczy nierozwiązanych.
- Kontrola wizualna: obejrzano podgląd wszystkich stron PDF rozdziału.
- Pełne GitHub Actions/CI: NIEURUCHOMIONE dla rozdziału 03 — rozdział nie jest jeszcze w repozytorium.

## Decyzja

Audyt 1 zakończony z dwiema zmianami precyzującymi/redakcyjnymi. Licznik czystych audytów: **0/2**. Następna iteracja: audyt 2 tego samego pliku, bez nowych twierdzeń. Rozdział 03 pozostaje poza GitHubem do zakończenia stabilizacji.
