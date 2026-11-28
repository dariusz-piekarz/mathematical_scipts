# Audyt CLI (151) — terminologia i oznaczenia
Data 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6. Stan rozdziałów 31/31, książka jeszcze niezamknięta.

## Kontrola
Pobrano wszystkie 31 rozdziałów (26 735 wierszy według split na newline) i oba dodatki. Przeszukano widoczną treść pod kątem notacji funkcji charakterystycznej i niedozwolonych terminów (sekwencja, zwartościowanie, pierwszo-/drugoprzeliczalność, samodzielne dual, tensorowanie, zbieżność zwarta, seskwiliniowy). Nie stwierdzono trafień w treści rozdziałów; 11 trafień dual to wyłącznie stabilne identyfikatory etykiet w rozdziałach 15–16, których nie zmieniano. Dodatki: jedno trafienie w indeksie (drugoprzeliczalnych), poprawione na „spełniających drugi aksjomat przeliczalności”, commit 7970d8afb965586a86caf135492a807019616722. Jest to kontrola wzorców, nie pełny semantyczny przegląd każdego zdania.

## Poprawki
Spis oznaczeń, commit 306f0b0f1152db0d28a914cd1c86f06cc3c0b5b8: miara zewnętrzna określona na całej potędze zbioru, ograniczenie Carathéodory'ego; rozróżnienie zewnętrznej miary Hausdorffa o ograniczonej średnicy i jej granicy, będącej miarą na zbiorach borelowskich; półwariacja jako funkcja zbioru zgodnie z rozdziałem 30. Weryfikacja źródłowa w rozdziałach 26 i 30.

## Trwałe regresje
MTG-001–003: commit 82b4443803dbeb6c5e4272db73788bec1316904c; test 33 importowanych źródeł, negatywne/pozytywne przykłady regex, poprawiony spis oznaczeń. Zachowano istniejące identyfikatory. Globalny workflow ffc26343773715a8520ea9d1c1b39ce14a12186a uruchamia wszystkie test_measure_theory*.py przy zmianach książki, rozdziałów, dodatków i testów. Nie potwierdzono jeszcze wykonania nowej bramki Python ani nie kompilowano nowej wersji PDF w tej iteracji.

## Następny krok
Audyt CLII: zależności między rozdziałami, odsyłacze wyprzedzające, potencjalne koła i powtórzenia (odróżnić przypomnienia od duplikatów), zgodność indeksu. Następnie ostrzeżenia LaTeX i kontrola globalnego PDF. Bez nowych tematów.
