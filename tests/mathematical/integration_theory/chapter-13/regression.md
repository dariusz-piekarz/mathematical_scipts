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

## Blok B — reprezentacja Riesza–Markowa–Kakutaniego
| ID | Kryterium | Metoda |
|---|---|---|
| IT-13-008 | Zupełność C0, lokalne ograniczenie dodatniego funkcjonału bez miary | semantyczna |
| IT-13-009 | Zawartość otwartych: monotoniczność, skończoność na relatywnie zwartych, addytywność na rozłącznych | semantyczna + Python |
| IT-13-010 | Skończone rozcięcie funkcji przez funkcje odcinające, ciągłość przy zerowym mianowniku, grupowanie indeksów | semantyczna + Python |
| IT-13-011 | Konstrukcja miary zewnętrznej oraz zwarta aproksymacja otwartych przed wykazaniem mierzalności | semantyczna |
| IT-13-012 | Kryterium Carathéodory'ego bez metryki i bez sigma-skończoności, przypadek nieskończonego kosztu | semantyczna + Python |
| IT-13-013 | Identyfikacja całki przez sumy progowe i lokalną funkcję odcinającą, przypadki graniczne | semantyczna + Python |
| IT-13-014 | Alternatywny dowód metryczny, puste zbiory w metrycznej addytywności, wcześniejsze etykiety i zależności | semantyczna |

Audyt B: commit 82d88614f684d719717bba8d44ad7c4b0c3f4a35, blob d92de4d374c395367d04ad51f0c0903c2e1dfa6b. Udowodniono ogólne twierdzenie dla LCH bez metryczności, ośrodkowości i sigma-skończoności; zachowano dowody metryczne i sklejanie. Rozdział 35671 -> 43935 znaków, 29/29 zachowanych etykiet i cztery nowe, 24 różnych odsyłaczy, brakujące w sprawdzonych plikach: brak. Zaktualizowano IT-16. Sześć nowych skończonych regresji, commit 93583e881736bb14661b781b6de16a44323c3a3f. CI A 45653824339: 113/113 testów, 143 strony PDF. CI B niepotwierdzony, kontrola wizualna i Lean oczekują. Następny blok C: lokalizacja, sklejanie, związek z Daniellem i przykłady.

## Blok C — lokalizacja, sklejanie i przykłady
| ID | Kryterium | Metoda |
|---|---|---|
| IT-13-015 | Wyczerpanie dla sigma-zwartej LCH, przypadek pusty, funkcje odcinające | semantyczna |
| IT-13-016 | Przedłużenie funkcji i miary zerem, zgodność całek i regularność ograniczeń | semantyczna |
| IT-13-017 | Sklejanie zgodnych lokalnych miar, jawna addytywność i równość na wyczerpaniu | semantyczna + Python |
| IT-13-018 | Zupełność C(K) dla zwartej Hausdorffa, Dini i lokalna ciągłość porządkowa | semantyczna |
| IT-13-019 | Rozróżnienie sigma-algebry Baire'a i borelowskiej, zgodność reprezentacji Daniella i Radona | semantyczna |
| IT-13-020 | Miara z gęstością i atomem, miara obrazowa okręgu, skończone sumy mas Diraca i regularność | semantyczna + Python |

Audyt C: commit 9f6652bbdbaef153952c829e6771b9ffdb89ea0b, blob ea447fcd7e750cc8c86015f4afdc9331035a7a8a. Równoległa zmiana prefiksu rozdziału (blob 34f0ebba6a0a62aab719937b4074995db9487fc9) zachowana; potwierdzono identyczność bloku C z poprzednim źródłem przed modyfikacją. Blok 6968 -> 11060 znaków, całe źródło 47856 znaków, 33 etykiety zachowane, 25 różnych odsyłaczy, 0 brakujących. Rozpisano wyczerpanie w LCH sigma-zwartej, lokalne przedłużenia, zgodność i sklejanie, dowód zupełności C(K), precyzyjny związek z sigma-algebrą Baire'a oraz rachunki przykładów. Zachowano alternatywny dowód metryczny. Pięć regresji skończonych 1b2909f8adc107092c36f05ae037b0b1b17721da. CI B 45658210952, job 139360557742: 119/119 testów i 145 stron PDF. CI C i kontrola wizualna oczekują. Lean nieuruchamiany. Następny etap: stabilizacja całego IT-13 i niezależny audyt kontrolny; szczególnie sprawdzić hipotezy ogólnej reprezentacji i równoległe zmiany prefiksu.
