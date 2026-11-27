# RRC 19 — iteracja 316: pierwsza lektura stabilizacyjna

Commit źródła 8517d3ee557cd4bc60695773e56ee804ed487c52, blob 19db478d42898f0089787ef0e3dece8d09e5c834.

Ponownie odczytano wszystkie 9 sekcji. Uściślono porównanie pojemności z infimum kwadratu pełnej normy H^1, stałą Poincarégo, wzory gradientów minimum i maksimum oraz argument podaddytywności. W dowodzie pojemności punktu jawnie ograniczono użycie twierdzenia Morreya do d>=2, wskazano jednowymiarową charakterystykę Sobolewa. Wyodrębniono izometryczność i surjektywność ograniczenia H^1 po usunięciu zwartego zbioru zerowej pojemności, niezależną od równania. Uzupełniono argument przeliczalnych zbiorów wyjątkowych i przynależność modułu do H_0^1 w dowodzie quasi-ciągłości. Poprawiono język i sklejenie w dowodzie Fourierowskim.
Dodano źródła dla twierdzenia o barierach Perrona (Axler, Bourdon, Ramey, Harmonic Function Theory, wyd. 2, 2001, 11.7 i 11.11) i pierścieniowej postaci kryterium Wienera (Prats, Tolsa, Harmonic measure in Euclidean spaces, rozdz. 6, https://mat.uab.cat/~xtolsa/mesuraharmonica.pdf). Równoważność pojemności Newtonowskiej określonej energią miar i wariacyjnej pozostaje wynikiem przywołanym; wymaga dokładnego odsyłacza. Pełnego kryterium Wienera nie dowodzono.

Kontrola źródła: 1245 wierszy (1202 przed zmianami), 37 zachowanych unikatowych etykiet, 44 wystąpienia odsyłaczy, 13 różnych celów zewnętrznych. Wszystkie cele istnieją jednoznacznie w rozdziałach 7,9,10,14,18 i źródle. Brak niezgodności begin/end. Dedykowane CI 45988751946 queued, poprzedni run 45988455742 przy pierwszym odczycie queued. Końcowy run rozdziału 18 (45985977450) przy pierwszym odczycie nadal queued. Brak odbioru PDF obu aktualnych wersji i globalnego CI.

Następny etap: drugi audyt stabilizacyjny, dokładny odsyłacz dla równoważności pojemności, odbiór aktualnego CI i PDF. Nie deklaruje się stabilizacji.
