# Moduł 15B — iteracja 15 (zatwierdzone rozszerzenie)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: audyt 14, 8c71e33845f2fa4a1c86aa8239d605c42554a90c, źródło 641dd59fc065281f00dda099123dac99533213cc, testy 5b744df89381f90529f84effdddfdba6a28ac40c. Drugi przegląd matematyczny poprzedniej wersji nie wykazał koniecznych korekt. Powtórne CI 45348555144: success.
Przed zamknięciem stabilizacji użytkownik zaakceptował propozycję z audytu 14, dotyczącą miary generowanej przez całkę Pettisa o nieskończonej wariacji.

## Rozszerzenie
Po twierdzeniu o mierze generowanej przez całkę Bochnera, przed definicją RNP, wstawiono przykład ex:pettis-infinite-variation15b z odsyłaczem do ex:pettis-strong-not-bochner15b. Zdefiniowano m(A)=(chi_A(n)/n) w l2. Pełne uzasadnienie przeliczalnej addytywności: kwadrat normy reszty jest szeregiem po malejącym ogonie zbiorów, zdominowanym przez sumowalny 1/n^2. Bezwzględna ciągłość względem miary atomowej. Dokładny wzór |m|(A)=sum_{n in A}1/n: górne oszacowanie normą l1 dla każdej partycji, dolne przez singletony do N i resztę. W szczególności wariacja całkowita nieskończona mimo jednostajnego ograniczenia norm wartości m. Związek z całką Bochnera wyjaśniono. Bez dalszych opcjonalnych rozszerzeń.

## Technika
Źródło commit 749d07658ced0f35579ca9f5e5f1135154698191, blob cefc9bdb7724e7bd12cc54ab3b7704ed5fa3a9c6. 76 dodatkowych wierszy, 938 łącznie, 25 unikalnych etykiet (24 poprzednie zachowane w kolejności), 6 przykładów, 11 dowodów. Ponowny odczyt potwierdza poprawne zagnieżdżenie środowisk.
Testy commit bba3a79627c6f674389b5b36b4f931a43ef6e0dc, blob abacd77424e1fdde379d42b0a8a5327d682afd22. Dodano trzynasty test: kontrakty źródłowe, skończone zbiory atomów, rozkłady na początek i ogon, bloki diadyczne. Kontrakty sprawdzono podczas zapisu. Nie potwierdzono wykonania nowego unittest ani kompilacji i oględzin nowego PDF w tej iteracji. Odczyt przebiegów: [{"id":45348881459,"sha":"bba3a79627c6f674389b5b36b4f931a43ef6e0dc","status":"in_progress","conclusion":null},{"id":45348858230,"sha":"749d07658ced0f35579ca9f5e5f1135154698191","status":"in_progress","conclusion":null}].

## Decyzja
Zatwierdzone rozszerzenie zmieniło źródło, więc stan stabilizacji 0/2. Następny niezależny audyt 16 modułu 15B, w tym kontrola matematyczna nowego przykładu, CI i PDF. Nie przechodzić jeszcze do rozdziału 16.
