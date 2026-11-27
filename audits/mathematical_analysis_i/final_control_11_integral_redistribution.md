# AM I 36–43 — zbiorcza kontrola integracyjna po redystrybucji IT

27.11.2026, gałąź biblioteka-matematyczna-iteracja-6.

## Stan źródeł
Wszystkie 43 pliki rozdziałów AM I są wymienione kolejno w książce; każdy z rozdziałów 36–43 występuje dokładnie raz. Bloby aktualne i identyczne z wersją c5898591c0866f9e27a3535711e6917246771a72:

| Rozdział | Blob | Wiersze | Etykiety |
|---|---|---:|---:|
| 36 | 6865bcb0bb03ceaec0553de08856947ba55b6350 | 257 | 32 |
| 37 | 37eca0440a4b7291506be5db7db6677ceca4aaa7 | 646 | 22 |
| 38 | 9c937e050a86ab61fb8d02040df76cc5ade3400f | 508 | 31 |
| 39 | e57710509f1f4fbff8423aa4b7668d6f61d3598e | 304 | 10 |
| 40 | 5a4d78fdaaf9e0e42dbdf4ee5263b5b9a6e14e2c | 482 | 17 |
| 41 | a35641825fe19704e55c205b233f625954a189e0 | 1025 | 30 |
| 42 | a6346e25541a568a0c63720efc5b1bc7de62a7f7 | 1418 | 45 |
| 43 | 127c0b1b50a1ebfd2c3c7435a41c2e303ca6b5eb | 452 | 18 |

Plik książki: 0bb2051ae7390edb335447daa93378e77c5dc55b, również zgodny z c589859. Łącznie 5092 wiersze według split("\n"), 205 unikalnych etykiet. 114 różnych odsyłaczy wewnętrznych (cztery poza blokiem, w AM I 29 i 32), wszystkie rozwiązane. 33 różne odsyłacze Atlasu zweryfikowane bezpośrednio w plikach ME 04, 07, 08, 13, 14, 16, 17, 18, 20, 21, 23, 25, 32, FA 12 i PDE 09. Brak duplikatów etykiet w bloku.

## Zachowanie materiału źródłowego
Sprawdzono każdą etykietę aktualnych IT 03–09: odpowiednio 18, 43, 9, 41, 15, 32, 28 wystąpień; 186/186 ma cel w AM I 36–43. Wszystkie 29 par etykiet z ch36_source_map.md występują dokładnie raz każda. Nie jest to dowód pełnego pokrycia semantycznego wszystkich rozdziałów IT. Pliki źródłowe IT nadal istnieją, natomiast książki IT nie ma w bieżącym katalogu books/pl. Nie usuwano źródeł IT w tej iteracji.

Porównanie z wcześniejszymi audytowanymi blobami AM I 38 i 40 wykazało zmianę odsyłaczy na opisowe odwołania do późniejszych rozdziałów; matematyki w tych zmianach nie zmieniono. Nie przywracano odsyłaczy wbrew równoległym zmianom. Raporty indywidualne 37–39 nie są w tym katalogu osobnymi plikami ch37–39_stable.md; nie należy przypisywać im nieistniejącej dokumentacji.

## CI i PDF
c589859: AM I 46022724890 i 46022717401, AM II 46022724954, terminologia 46022717326, aplikacja 46022717478 — wszystkie success. Artefakt AM I 15211365492, 2454284 bajtów archiwum, nieprzeterminowany przy kontroli. Nie wykonano kontroli wizualnej PDF ani ponownego pełnego audytu matematycznego wszystkich 5092 wierszy w tej iteracji.

Wynik: integracja strukturalna i kontrola zachowania etykiet IT 03–09 zaliczone; odbiór wizualny PDF i pełne usunięcie/rozliczenie pozostałych materiałów IT pozostają osobnymi zadaniami. Następnie AM II — odbiór rozdziału 16 przed dalszą rozbudową.
