# Audyt CXXVIII (128) — granica półprzestrzenna De Giorgiego
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 76512ae932c39e4e7efacb7a45b877161a55cfeb, blob 5b1a2b091869a4de2dd5cac0aef140cf513f5b4f. Commit źródłowy ecba558bed0d61235acf18d8ee4e56036dd24715, blob 4bbbf3ed6b90d0a296ebc01ca311deb48682a185.
## Wyniki
Zastąpiono cały dowód lematu dg-blowup pełnym pięcioetapowym argumentem. 2680 -> 2879 wierszy, zachowano wszystkie 37 etykiet.
- Jawne hipotezy, dystrybucyjne skalowanie z czynnikiem r^(1-n), transformacja wariacji i pola polarnego.
- Lokalne ograniczenia masy, reguła iloczynu dla odciętych funkcji BV, pełna kontrola norm i zastosowanie wcześniejszego argumentu średnich na kostkach do funkcji o wartościach w [0,1]. Przekątna na wyczerpaniu, zgodność granic, dwuwartościowość granicy.
- Lokalna zwartość miar dodatnich przez ośrodkowość testów C_c, argument przekątniowy i reprezentację dodatniego funkcjonału. Precyzyjna zbieżność względem C_c zamiast niejednoznacznej zbieżności na zbiorach zwartych.
- Oszacowanie błędu normalnej przez Cauchy'ego–Schwarza i wcześniejszą kontrolę kwadratową. Identyfikacja dystrybucji granicznej D chi_F = -nu sigma.
- Zastąpiono lukę w przejściu od zerowych pochodnych stycznych do zależności od jednej zmiennej bezpośrednim dowodem przez splot: gładkie funkcje zależne od ostatniej współrzędnej i nierosnące; średnie na kostce jednostkowej identyfikują jednowymiarową granicę. Uzasadniono monotoniczność na zbiorze pełnej miary i postać funkcji charakterystycznej półprostej.
- Dolne oszacowania objętości w każdej kuli wykluczają zarówno granice stałe, jak i przesunięcie hiperpłaszczyzny. Nie potrzeba dodatkowego argumentu z masą zwartej kuli.
- Obliczenie pochodnej półprzestrzeni, identyfikacja sigma, pełna zbieżność dla dowolnego ciągu promieni; przejście do masy kuli przez ciągłe funkcje odcinające i granicę delta -> 0.
## Otwarte
Następny audyt: prostowalność brzegu zredukowanego i identyfikacja miary Hausdorffa, w szczególności stałe w argumencie stożkowym i precyzyjne hipotezy różniczkowania miar. Nie potwierdzono kompilacji ani PDF. Stan 28/31.
