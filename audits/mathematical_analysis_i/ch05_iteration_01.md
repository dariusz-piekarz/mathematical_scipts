# MA1-05 — iteracja rozwojowo-stabilizacyjna 01
Po certyfikacji MA1-04 (7450dc3) utworzono MA1-05 i dodano do tomu i katalogu. Aktualna treść 037712d, blob 9f2d721a3dec17a88da101b31abab75abbb9c64b, 292 wiersze.
## Przegląd semantyczny
001–003: sprawdzono łączność i rozdzielność po współrzędnych, odwrotność, zanurzenie R, sprzeczność porządku zgodnego z działaniami i własności sprzężenia; rachunek przykładu ilorazu poprawny. Opis ilorazu wielomianów z jądrem ewaluacji.
004–005: multiplikatywność przez sprzężenie, nierówność trójkąta przez część rzeczywistą, nierówność odwrotna, dokładna charakterystyka równości. Doprecyzowano użycie monotoniczności kwadratu, moduł przeciwności.
006–007: macierz mnożenia, iloczyn z transpozycją, wyznacznik i składanie; dwa rysunki TikZ (odbicie i obrót jednostkowy). Sprawdzono współrzędne i zgodność geometryczną kodu, nie oglądano jeszcze skompilowanych rysunków.
008–009: wyprowadzono konieczne wzory, zweryfikowano istnienie bez dzielenia przez zero dla v != 0, pozostałe przypadki jawnie; faktoryzacja różnicy kwadratów i jednoznaczność do znaku. Dopisano tożsamość dopełnienia kwadratu. Trzy przykłady pierwiastków oraz równanie kwadratowe.
010: podgrupa, bijekcja rozkładu, homomorfizm grup. Nie wprowadzano przedwcześnie argumentu liczbowego ani funkcji trygonometrycznych.
## Kontrole
17 etykiet, brak kolizji i nierozwiązanych ref, poprawne zagnieżdżenie środowisk; preambuła Atlasu i tomu identyczne; rozdział w pliku głównym i katalogu. 10 kryteriów, 7 nowych testów arytmetyki dokładnej (30 testów łącznie). CI najnowszej treści: 45410512293, Atlas 45410512356, terminologia 45410512584 — w kolejce. Wcześniejszy przebieg testów 45410471142 w toku. Nie deklarujemy zaliczenia nowych testów, pełnej kompilacji, wizualnego audytu rysunków ani Lean. Status: w stabilizacji; następna iteracja potwierdzająca.
