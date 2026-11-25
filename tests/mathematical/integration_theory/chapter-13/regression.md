# IT-13 — całka Radona: kryteria audytu

## Blok A — regularność i jednoznaczność

| ID | Kryterium | Metoda |
|---|---|---|
| IT-13-001 | Lokalna skończoność i borelowskość zwartych zbiorów, zakres Hausdorffa | semantyczna |
| IT-13-002 | Konwencje regularności, regularność na zbiorach skończonej i sigma-skończonej miary | semantyczna + Python |
| IT-13-003 | Aproksymacja domkniętymi i otwartymi w dowolnej przestrzeni metrycznej, jawny budżet błędu | semantyczna + Python |
| IT-13-004 | Lokalnie zwarta ośrodkowa przestrzeń metryczna: przeliczalne pokrycie, lokalizacja miary, regularność zewnętrzna | semantyczna + Python |
| IT-13-005 | Regularność wewnętrzna, ślad sigma-algebry, przypadek nieskończonej miary | semantyczna |
| IT-13-006 | Funkcja odcinająca na ogólnej lokalnie zwartej przestrzeni Hausdorffa, normalność zwartego otoczenia i lemat Urysohna, alternatywny wzór metryczny | semantyczna + Python |
| IT-13-007 | Jednoznaczność miary Radona na ogólnej lokalnie zwartej przestrzeni Hausdorffa przez całki funkcji C_c | semantyczna + Python |

Audyt I, blok A, 2026-11-25. Commit 58b90bc4a5b222e773b4a0c6c81f47a5f3080ee3, blob 86cdcc6a4be8900d2e104779b90c41213ca45459. Przeczytano część od początku do twierdzenia reprezentacyjnego (14981 -> 17723 znaków); pozostałe 17948 znaków bez zmian. Poprawiono nieuprawnione użycie miary na dowolnym zwartym zbiorze bez założenia borelowskości; rozpisano przejścia w regularności i budżet błędów, poprawiono twierdzenie o konieczności rozłącznego pokrycia (nie jest konieczne), przywrócono ogólny lemat odcinający i jednoznaczność Radona dla LCH z wykorzystaniem normalności zwartych przestrzeni Hausdorffa i lematu Urysohna. Zachowano 29/29 etykiet, 7/7 różnych odsyłaczy w bloku, środowiska sparowane. Pięć regresji skończonych, commit c4098a4ae66c52ccf6fd370a8e9732c2060490da. CI nowych zmian w toku; kontrola PDF i Lean niepotwierdzone. Następny blok B: reprezentacja Riesza–Markowa–Kakutaniego, w tym konstrukcja i sklejanie miar oraz możliwość ogólnej wersji LCH. Raport IT-12 zapisano osobno w commicie 426cc654a0b71537c993b4c8e0b2dff66ec8e7c2.
