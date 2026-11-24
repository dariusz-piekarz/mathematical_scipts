# Audyt CLII (152) — zależności między rozdziałami
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.

## Potwierdzone wykonanie
Globalne CI 45384538250 (7970d8afb965586a86caf135492a807019616722): 153 testy, OK. Starszy stan 45384610240 miał jedną porażkę terminologiczną indeksu (drugoprzeliczalnych), poprawioną w CLI; nie jest to aktualny błąd.
CI 45384737785 (0b0b6a24316701267c019f47cf897d676bd4ad6b): 155 testów, OK. Inwentaryzacja: 721 etykiet rozdziałowych, 81 różnych skierowanych par rozdziałów połączonych bezpośrednimi odsyłaczami, 18 wystąpień odsyłaczy do późniejszych rozdziałów. Brak nierozwiązanych bezpośrednich odsyłaczy. Nie znaleziono identycznych jednowierszowych tytułów tego samego typu środowiska w różnych rozdziałach; nie jest to dowód braku semantycznych powtórzeń.

## Klasyfikacja odsyłaczy wyprzedzających
- 1→2 (2), 3→4 (1), 7→8 (2), 10→12 (1), 11→12 (1), 17→18 (1), 20→23 (1), 21→22 i 23 (po 1), 26→28 i 29 (po 1), 27→28 (1), 28→30 i 31 (po 1), 29→30 (2).
- 17 odsyłaczy poza środowiskiem proof: zapowiedzi, omówienia i odniesienia do szerszego kontekstu. Jedyny wewnątrz proof: 7→8, twierdzenie thm:integrability-criterion. Sprawdzono tekst dowodu: jawnie rezygnuje z późniejszego twierdzenia o addytywności i wykorzystuje twierdzenia o funkcjach prostych i nierówność Markowa z bieżącego rozdziału. Nie stanowi zależności logicznej.
- 28→31: późniejsze rozwinięcie teorii dżetów; rozdział 28 ma własny lemat przedłużania C^1 niezbędny dla wzorów pola i koobszaru. Zachowanie obu ujęć służy niezależności wcześniejszego dowodu; nie scalać kosztem wprowadzenia cyklu.
- Nie wykryto dowodowej zależności wyprzedzającej w analizowanych bezpośrednich odsyłaczach. Nie utożsamiać tego z formalną kontrolą wszystkich niejawnych zależności.

## Trwałe zmiany
MTG-004–005 (0b0b6a24316701267c019f47cf897d676bd4ad6b), klasyfikacja jedynego wyjątku dowodowego utrwalona w 64331eaa0b0d0255467e4bd4b967ac068dcaf777. Testy raportują kandydatów na zależności i kolizje tytułów; nowe odsyłacze wyprzedzające w proof wymagają kontroli.
Workflow globalny poprawiony w 8500c16e93e92ea2e5ca1b0be9386941e5197e08: dodano uruchamianie samodzielnych skryptów tools/test_measure_theory*.py, wcześniej nieobjętych unittest discover w tools/tests. Test PDF layout wymaga wejściowego pliku bbox i pozostaje w osobnej bramce PDF. Najnowszy run 45384874133 w chwili zapisu pending; nie ogłaszać jego zaliczenia przed sprawdzeniem.
Bez zmian merytorycznych w rozdziałach; stan 31/31. Kolejny audyt CLIII: kompletność indeksu i zgodność tytułów z rzeczywistymi środowiskami, potem globalny PDF i ostrzeżenia.
