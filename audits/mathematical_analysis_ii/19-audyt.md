# AM II 19 — Twierdzenie o funkcji uwikłanej

27.11.2026. Pierwsza wersja rozdziału: twierdzenie i redukcja do FA-15, równania z parametrami i prawą stroną, druga pochodna i oszacowanie normy, przypadek skalarny, sfera, dwa kontrprzykłady i równanie operatorowe. Dodano listing Plotly, definicję repozytoryjną oraz rejestrację AM2-19 w podglądzie. Włączono rozdział do książki i katalogu. Kontrola podczas tworzenia: 8 unikalnych etykiet, stos środowisk bez błędów, katalog poprawny składniowo. Nie uruchomiono kompilacji, testu przeglądarkowego ani audytów stabilizacyjnych. Rozdział pozostaje otwarty do szczegółowego audytu.

## Pierwszy audyt szczegółowy — 27.11.2026

Wprowadzono 18 korekt źródłowych w czterech sekcjach, w tym: ograniczoność i obie kompozycje operatora blokowego; jawne otwartości i odwracalność pochodnej częściowej w równaniu z prawą stroną; oszacowanie normy drugiej pochodnej; odsyłacz do twierdzenia Schwarza; gładkość i lokalne zastosowania twierdzenia na całym dysku, płaszczyzna styczna i rachunek drugiej pochodnej sfery; uzasadnienie kontrprzykładu; ograniczoność, różniczkowalność operatorowa, reguła iloczynu i przypadek przestrzeni zerowej. Poprawiono zarówno listing, jak i repozytoryjną definicję Plotly, aby powierzchnia wyróżnionego wykresu nie była nałożona na tę samą część sfery. Zachowano wszystkie 8 etykiet; stos środowisk bez błędów. Stabilizacja 0/2. Nie uruchomiono kompilacji PDF ani przeglądarki.

## Drugi audyt szczegółowy — 27.11.2026

Wprowadzono 9 korekt: jawna norma produktu, korekta gramatyczna, ciągłość operatorów częściowych z oszacowania normy, wyprowadzenie pierwszej pochodnej, pełna równoważność i dobór otwartych otoczeń w wersji z prawą stroną, poprawienie nieokreślonej zmiennej q w przykładzie sfery, ścisły dowód braku lokalnego wykresu nad równikiem wraz z doborem alternatywnej współrzędnej, uzasadnienie ograniczoności ewaluacji operatorowej i jawne podstawienie t=0. Odczytano deklaracje wyników AM II dotyczących reguły dwuliniowej, twierdzenia Schwarza, drugiej pochodnej złożenia, Taylora, odwracalności perturbacyjnej i funkcji odwrotnej. Hipotezy zastosowań zgodne. Wszystkie 8 etykiet zachowane, stos środowisk poprawny. Stabilizacja 0/2. Bez zmian w Plotly i bez uruchomienia PDF lub testów przeglądarkowych.

## Pierwszy audyt stabilizacyjny — 27.11.2026

Pełny ponowny odczyt rozdziału (blob 96f4abb83541005740f3b9d1f2275dbaa238c5d5). Zweryfikowano zupełność produktu, ciągłość operatorów częściowych, oba złożenia blokowe i oszacowanie ograniczoności odwrotności, zgodność twierdzenia oraz szczegółów doboru otoczeń z rzeczywistym dowodem FA-15. Sprawdzono znaki i dziedziny pierwszej i drugiej pochodnej, normę dwuliniową, regularność wyższych rzędów, obie implikacje dla równania z prawą stroną, przypadek skalarny i twierdzenie Schwarza. W przykładzie sfery sprawdzono dodatnią gałąź, wzory pochodnych, płaszczyznę styczną, współczynnik Taylora, ciągi punktów nad równikiem i zmianę współrzędnej. W kontrprzykładach sprawdzono ścisłe nierówności i równoważności, w przykładzie operatorowym resztę Frécheta, pochodną drugiego rzędu, regułę dwuliniową, przypadek zerowy i zastosowanie szeregu Neumanna. Nie znaleziono nowych usterek wymagających zmian.

Kontrola źródłowa: 9/9 różnych lokalnych celów odsyłaczy oraz 2/2 celów FA-15 występuje dokładnie raz w sprawdzonych rozdziałach; 8 unikalnych etykiet, stos środowisk bez błędów, pojedynczy wpis w książce i katalogu, rejestracja AM2-19 obecna. Dodatkowa kontrola numeryczna przez odtworzenie wzorów i rozdzielczości siatek z definicji JS: maksymalna odchyłka równania sfery na 7381 punktach 4.441e-16, na 4961 punktach lokalnego wykresu 2.220e-16, rozbieżność wspólnego brzegu 0.000e+0. Nie jest to test wykonania całego modułu ani renderowania.

Stabilizacja merytoryczna 1/2. CI dla 5d0cf5f: AM II 46038430372, terminologia 46038430325, aplikacja 46038430552 — wszystkie queued przy odczycie. Brak potwierdzenia aktualnej kompilacji PDF i renderowania w przeglądarce.

## Drugi audyt stabilizacyjny — 27.11.2026

Ponowny przegląd pełnego źródła, blob 96f4abb83541005740f3b9d1f2275dbaa238c5d5. Bez nowych usterek wymagających zmian. Sprawdzono cztery sekcje, w tym: typy operatorów A:Y→Z, B:X→Z, L:X×Z→X×Y i obie kompozycje; ważność oszacowań także dla przestrzeni zerowych; zastosowanie twierdzenia o funkcji odwrotnej na zupełnym produkcie; istnienie i jednoznaczność rozwiązania z FA-15; znak pochodnej względem prawej strony oraz obie implikacje równoważności. Sprawdzono ponownie regułę drugiej pochodnej złożenia, oszacowanie w normie maksimum i współczynnik 2 w przypadku skalarnym. W przykładzie sfery: dodatniość mianowników, współczynnik 1/2 we wzorze Taylora, obraz pochodnej parametryzacji, obie gałęzie przy równiku i dobór współrzędnej. W przykładach zdegenerowanych i operatorowym: dobór parametrów, resztę Frécheta, symetrię drugiej pochodnej, współczynnik 2 przy K²b, przypadki K=0 i E={0} oraz zbieżność szeregu w normie operatorowej.

Ponowna kontrola pobranych źródeł: 8 unikalnych etykiet, 9/9 lokalnych i 2/2 zewnętrznych różnych celów odsyłaczy występują dokładnie raz w sprawdzonych rozdziałach, poprawny stos środowisk, po jednym wpisie w książce i katalogu. Rejestracja i definicja Plotly AM2-19 obecne. CI dla 5d0cf5f: trzy przebiegi nadal queued. Nie wykonano kompilacji PDF ani testu przeglądarkowego.

Stabilizacja merytoryczna 2/2. Kolejny etap: audyt kontrolny.

## Audyt kontrolny — 27.11.2026

Ponowny odczyt całego rozdziału (blob 96f4abb83541005740f3b9d1f2275dbaa238c5d5). Kontrola od definicji po ostatni przykład: zupełność produktu i rozkład pochodnej na operatory częściowe, odwracalność operatora blokowego i ograniczoność odwrotności, zgodność odesłania do pełnego dowodu FA-15, jednoznaczność rozwiązania lokalnego, znaki i dziedziny pierwszej i drugiej pochodnej, regularność wyższych rzędów, równanie z prawą stroną, współczynnik mieszany w przypadku skalarnym, płaszczyzna styczna i brak lokalnego wykresu wzdłuż ustalonej projekcji nad równikiem, przykłady zdegenerowane oraz równanie operatorowe i jego szereg Neumanna. Nie stwierdzono nowych usterek wymagających zmian.

Kontrola pobranych źródeł: 8 unikalnych etykiet, 9/9 lokalnych i 2/2 zewnętrznych różnych celów odsyłaczy występują dokładnie raz w sprawdzonych rozdziałach; poprawny stos środowisk; pojedynczy wpis w książce i katalogu; definicja oraz rejestracja Plotly obecne. Dodatkowo porównano trzy niezależne składowe macierzy Hessego dodatniej gałęzi sfery w punkcie (0.21,-0.32) z centralnymi różnicami skończonymi o kroku 10^-4; maksymalna różnica 6.361e-9. Jest to pomocnicza kontrola numeryczna, nie dowód.

Stabilizacja merytoryczna 2/2 + audyt kontrolny zaliczony. Odbiór techniczny pozostaje otwarty: przebiegi AM II 46038430372, terminologia 46038430325 i aplikacja 46038430552 nadal queued; nie potwierdzono aktualnej kompilacji PDF ani renderowania przeglądarkowego. Kolejny etap merytoryczny: AM II 20.
