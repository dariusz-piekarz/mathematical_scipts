# GT — pełna kontrola par rozdziałów pod kątem powtórzeń tekstowych

Snapshot: 47b3c7816cf814308f1437494a818bf57321a3e4. Potwierdzono brak zmian wszystkich 42 plików GT do commitu e96868542d3c25802682b73907d342ec0350e50c.

Metoda jak w raporcie 309: usunięcie komentarzy, TikZ, listingów i komend TeX, normalizacja wielkości liter, porównanie zbiorów okien 18 słów. Próg kandydata: 6 wspólnych różnych okien. Kontrola 41 numerowanych rozdziałów, bez wstępu.

Bloki źródłowe: A = 01–08, 37–43 (15); B = 09–22 (14); C = 23–34 (12).

| Pary | Liczba | Kandydaci |
|---|---:|---:|
| A–A | 105 | 0 |
| B–B | 91 | 0 |
| C–C | 66 | 0 |
| A–B | 210 | 0 |
| A–C | 180 | 0 |
| B–C | 168 | 0 |
| Razem | 820 | 0 |

W tej iteracji wykonano 558 porównań między blokami (wszystkie z maksymalnie 0 wspólnych okien), oraz powtórzono 196 porównań wewnątrz A i B po zmianach źródeł 04, 06, 11 (również maksymalnie 0). Dla 66 par C–C zachowano wynik raportu 309, ponieważ SHA wszystkich plików C są identyczne. Łącznie 820/820 par na zgodnych wersjach, 0 kandydatów. Nie zmieniano treści rozdziałów.

Wynik dotyczy powtórzeń dosłownych według przyjętej metody, nie wyklucza parafraz, powtórzeń krótszych ani dublowania pojęć. Kontrola matematycznych zależności i terminologii pozostaje otwarta. CI pełnego skryptu 45977560152 nadal queued; nie wykonano odbioru PDF.
