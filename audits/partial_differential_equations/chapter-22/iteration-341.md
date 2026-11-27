# RRC 22 — iteracja 341

Pierwszy audyt szczegółowy sekcji 22.5 (postęp 5/8). Commit 8012fdf3e8d8ea880d1b0c7b4d15948215523975, blob b6577b2c838ff42459cfb2bcea87246b010234e4.

- Wyprowadzono całkę gaussowską przez równanie zwyczajne dla transformaty, całkowanie przez części i Fubiniego; uzasadniono holomorficzność względem parametru w prawej półpłaszczyźnie i wybór gałęzi logarytmu oraz granicę dla obu znaków czasu.
- Uzasadniono normalizację splotu, przedłużenie tożsamości regularizowanej na L², majorantę niezależną od epsilon dla ustalonego t != 0, zbieżność w L² i punktowo oraz identyfikację ciągłego reprezentanta. Rozszerzono wzór na L¹ ∩ L² oraz jądrowe przedłużenie na L¹.
- Rozpisano zgodność operatorów na przecięciu L¹ i L², operator na sumie, interpolację Riesza–Thorina z jawną stałą oraz gęstość i jednoznaczność przedłużenia.
- Wyprowadzono ewolucję pakietu gaussowskiego, jego gęstość, zachowanie całki i wariancję jednowymiarowej znormalizowanej gęstości. Dodano rysunek TikZ dla t=0, 1/2, 1. Skopiowany kod samego rysunku skompilowano lokalnie w klasie standalone z tikz i arrows.meta (pdflatex, 1 strona), zrasteryzowano i obejrzano: wszystkie trzy krzywe, osie i legenda czytelne. Jest to test izolowanego rysunku, nie kompilacja rozdziału w kanonicznej preambule.
- Oddzielono przykład Gaussa od właściwego twierdzenia o propagacji. Dla dowolnych niezerowych danych L² o zwartym nośniku wykazano, że dla t != 0 nośnik rozwiązania jest równy całej R^d. Rozpisano dokładny czynnik Fouriera, całkowalność danych i argument identyczności dla funkcji holomorficznej jednej zmiennej na prostych. Nie utożsamiano pełnego nośnika z brakiem pojedynczych zer.

Kontrola źródła: 1163 wiersze (949 wcześniej), 17 zachowanych unikatowych etykiet, 21 odsyłaczy, sześć różnych celów zewnętrznych w rozdziałach 8,18,20,21, wszystkie jednoznaczne; brak błędów zagnieżdżenia środowisk i delimiterów. Wszystkie pozostałe sekcje identyczne. Kompilacja całego rozdziału 22 niepotwierdzona. Runy 46001463968 (20) i 46001463740 (21) przy odczycie queued.

Następny etap: sekcja 22.6 — oszacowania Strichartza w d=2, nierówność ułamkowego całkowania w czasie, argument TT* i człon niejednorodny.
