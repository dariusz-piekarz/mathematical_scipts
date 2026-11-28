# RRC 17 — iteracja 296: założenia, obcięcia i iteracja De Giorgiego

Rozdział 16: niezależne potwierdzenie istniejącego odbioru 295. Run 45976114789, dedykowany CI PASS, 20 stron PDF; przegląd wszystkich stron na czterech arkuszach kontaktowych, brak widocznych przepełnień. Końcowy log: brak niezdefiniowanych odsyłaczy i makr, brak Overfull hbox i Missing character; 28 ostrzeżeń o pustych celach linków w izolowanym PDF. Globalne CI pozostaje w kolejce.

## Rozdział 17 — pierwsza lektura szczegółowa sekcji 17.1–17.3

Commit źródła: be2751896a74d8d97f3fe314c9d5c64e9a6145a8. Zmieniono cztery bloki:
1. Uzasadniono dopuszczalność testów Sobolewa o zwartym nośniku, w tym zachowanie nieujemności przy aproksymacji i przejście do granicy. Usunięto zapis H^1(K) dla zbioru zwartego i niepoprawną terminologię zbieżności.
2. Rozpisano skalowanie słabej formy (R^(2-d)), zachowanie znaku i normalizację przez dolną stałą eliptyczności.
3. Dla nadrozwiązania zastosowano oszacowanie Caccioppolego do podrozwiązania -u oraz poziomu -k; usunięto niejednoznaczny opis ujemnego testu.
4. W iteracji De Giorgiego wyodrębniono przypadek zerowej normy, uzasadniono próg małości, przejście od Y_n do znikania obcięcia na B_1 i dokładne przeskalowanie normy na średnią całkową.

Sprawdzono ponownie źródło zapisanego commitu: 689 wierszy (przed zmianą 647), 36 etykiet zachowanych w tej samej kolejności, 30 wystąpień ref/eqref/cref. To kontrola strukturalna, nie walidacja rozwiązywalności wszystkich odsyłaczy. Nie wykonano kompilacji rozdziału 17 ani pełnego CI; przy pierwszym odczycie API brak przebiegów dla commitu. Nie oznaczać rozdziału jako ustabilizowany.

Następny etap: sekcja 17.4, energia dodatnich i ujemnych potęg, iteracja Mosera (hipotezy, znaki, stałe, małe wykładniki, granice). Następnie sekcje 17.5–17.8, stabilizacja i niezależny odbiór.
