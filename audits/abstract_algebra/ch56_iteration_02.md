# AA-56 — audyt II: kompletność klasyfikacji, modele korzeni i niezależność bazy

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit źródłowy 78aad66a51ad2e4399df2621b8dafb81c3fd7f9c, blob b75d8fac66195d710df141cdae3e3081b137d687.

## Kontrola matematyczna i korekty
Przejrzano dowody istnienia bazy, redukcji wysokości korzenia, przechodniości na komorach, klasyfikacji dodatnio określonych macierzy oraz modele realizacji. Istotna luka w sformułowaniu klasyfikacji z dokładnością do podobieństwa: poprzednio wykazano jednoznaczność dla ustalonej macierzy, ale nie udowodniono niezależności typu od wyboru bazy. Uzupełniono twierdzenie o przechodniości na bazach jako zbiorach: element grupy Weyla przeprowadzający komorę na drugą zachowuje znaki odpowiednich korzeni, a nierozkładalne dodatnie korzenie to dokładnie korzenie proste. Stąd podobieństwo dwóch układów wymusza równość macierzy z dokładnością do jednoczesnej permutacji indeksów; uwzględniono B2=C2. Uzasadniono też nierozkładalność realizacji ze spójności diagramu.

Pozostałe korekty: interpretacja symetryzatora przez kwadraty długości; dokładna konstrukcja ścieżki zawierającej dwie podwójne krawędzie; wybór dwóch sąsiadów spoza ścieżki przy rozgałęzieniu; jawny blok pozadiagonalny przy jednej podwójnej krawędzi; pełne uzupełnienie kwadratu i obie implikacje kryterium dopełnienia Schura; wypisanie sześciu dodatnich korzeni G2 we współrzędnych standardowych. Nie zmieniono zakresu rozdziału ani innych rozdziałów. Po zmianie 871 wierszy LaTeX, 18 etykiet, 26 wystąpień odsyłaczy do 16 różnych celów, wszystkie cele jednoznaczne w AA-55–56; środowiska zrównoważone.

## Wykonana niezależna kontrola modeli F4 i G2
W JavaScript wygenerowano całe zbiory korzeni z podanych modeli (F4 w skali 2, G2 bez skalowania), obliczono całkowite iloczyny skalarne i dla każdej uporządkowanej pary sprawdzono podzielność 2(a,b) przez (a,a) oraz przynależność odbitego wektora do zbioru. F4: 48 korzeni, 2304/2304 par; G2: 12 korzeni, 144/144 par. Razem 2448/2448. Ponadto eliminacja współrzędnych względem podanych baz dała całkowite współrzędne o jednolitym znaku we wszystkich przypadkach, dokładnie 24 i 6 dodatnich korzeni. Macierze Cartana F4: [[2,-1,0,0],[-1,2,-1,0],[0,-2,2,-1],[0,0,-1,2]], G2: [[2,-3],[-1,2]]. Nie stwierdzono błędów w tych modelach.

## CI
Pierwszy run 45359549483: w toku, 7 kroków success, wspólny zestaw testów w toku. Nowy run 45359728972 po korekcie źródła: queued. Nie oglądano PDF.

## Werdykt
AA-56 W AUDYCIE, czyste niezależne audyty po II: 0/2. Następna iteracja: niezależna enumeracja ważonych drzew typu skończonego i kontrola realizacji ADE. AA-57 nieotwarty.
