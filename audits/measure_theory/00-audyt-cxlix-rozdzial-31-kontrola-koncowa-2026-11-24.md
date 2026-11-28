# Audyt CXLIX (149) — kontrola końcowa rozdziału 31
Data 2026-11-24; gałąź biblioteka-matematyczna-iteracja-6.

Poprzedni przebieg 45379767192: wszystkie trzy zadania success. Zweryfikowano dowód lem:lusin-whitney-28: rozdział 28 używa własnego lematu lem:whitney-c1-28, nie późniejszego rozdziału 31; brak zależności kołowej z omawianym twierdzeniem.

## Korekty
Commit f52e0ecd7e8b8d79bc60dadfb92e45eac9aea416; blob 244cf333eab3822272dcbbc217bd7e42418c8fb9; 1594 → 1667 wierszy, 30 etykiet zachowanych.
- Relacja na kiełkach i dżetach: jawne hipotezy, reguła łańcuchowa wyższych rzędów oraz równoważność.
- Granica przybliżona: jawny mianownik, równoważność normalizacji; dżety zgodnych prawie wszędzie przedstawicieli wymagają również przynależności punktu do zbioru równości, nie tylko jego gęstości.
- Przykład zbioru przedziałów diadycznych: oszacowanie szeregu geometrycznego i gęstości; kontrprzykład |x|: uzasadnienie równości funkcji ciągłych równych p.w.
- Dżety holomorficzne: korekta sugestii globalnych ograniczeń dla dowolnych danych skończonych, dowód realizacji przez wielomian z chińskiego twierdzenia o resztach; ograniczenia na zbiorach z punktami skupienia lub dla klasy funkcji z dodatkowymi warunkami.
- Ujednolicenie terminologii wzorów pola i koobszaru; odróżnienie wyników wcześniejszych rozdziałów od jawnie przyjętych wyników zewnętrznych o Sobolewie i BV.

## Regresje
MT31-015–016: commit ead4f1fb6f41bec7f99ccc99768efdb7bc037b02; 16 trwałych testów. Niezależne kontrole JS: 625 przypadków interpolacji Hermite'a, 6 warunków źródłowych, zaliczone. Nowe testy Python nie uruchomione lokalnie. Aktualne statusy: [].

## Następny krok
Końcowa kontrola składu nowej wersji i potwierdzenie CI; nie zamykamy rozdziału na podstawie poprzedniego PDF. Stan 30/31. Następnie audyt przekrojowy książki.
