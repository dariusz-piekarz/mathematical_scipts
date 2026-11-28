# RRC 22 — iteracja 345

Drugi pełny audyt stabilizacyjny wszystkich 8 sekcji (odczyt 1649 wierszy). Commit 7dc5720fc689233af00ef32a919599113765f98a, blob 5ade6594686e5dd7edbe3f16d55fa6750e915651.

- Ustalono parowanie półtoraliniowe H^{-2} × H² przez transformatę Fouriera, oszacowanie ważone i rozdzielanie punktów. Rozpisano identyfikację równania dystrybucyjnego w czasie z wartościami w H^{-2}. Ponownie sprawdzono obcięcie częstotliwości, ciągłość i jednoznaczność Duhamela oraz zastosowanie do potencjału zależnego od czasu.
- Zamiast nieprecyzyjnego stwierdzenia o operatorze na C_c^infty podano konkretny kontrprzykład samosprzężoności na przedziale. Sprawdzono znaki sprzężenia, normy grafowe, bilans prawdopodobieństwa oraz wspólną ciągłość ewolucji dwuparametrowej.
- Doprecyzowano argument całki gaussowskiej i wariancji, terminologię w dowodzie braku skończonej prędkości propagacji. Sprawdzono stałe, gałąź potęgi i interpolację.
- W metodzie TT* uzasadniono wspólnie mierzalnego reprezentanta Tφ przez Bochnera i Fubiniego na skończonych przedziałach. Sprawdzono operator maksymalny, zanurzenie H²→L⁴, dualność i przedłużenie całki opóźnionej.
- Uściślono miarę spektralną w przeszkodzie dyspersji. W konstrukcji z formy określono pełne założenia hermitowskiej formy półtoraliniowej, iloczyn skalarny dziedziny, ograniczoność funkcjonału, liniowość R i oszacowanie w normie formy. Rozpisano samosprzężoność R, injektywność i tożsamość dla R^{-1}-I. Ustalono normę Sobolewa na obszarze ograniczonym, odrębną od normy Fouriera na całej przestrzeni.
- Nie znaleziono nowego błędu rachunkowego w zasadniczych dowodach. Uzupełnienia są merytoryczne i redakcyjne; wymagają kontroli różnic.

Kontrola źródła: 1722 wiersze, 17 zachowanych unikatowych etykiet, 26 odsyłaczy, siedem różnych zewnętrznych celów (8,18,20,21), wszystkie jednoznaczne; brak błędów zagnieżdżenia środowisk i delimiterów. CI 46017673118 przy odczycie queued; nowe CI 46017984350 queued. Poprzedni PASS 46014868939 dotyczy wersji przed stabilizacją. Aktualna kompilacja, wizualny odbiór i globalne CI niepotwierdzone.

Następny etap: kontrola zmian 345, w szczególności parowania i reprezentacji form. Jeżeli nie pojawią się nowe usterki, przejść do pełnego audytu końcowego.
