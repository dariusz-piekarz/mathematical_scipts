# AA-59 — audyt II: dowody i niezależne modele po zmianie bazy

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Źródło przed korektą 1b9a680247f2d1781bee225871485b3466e099e8, po korekcie 96d034d117a7f96f9928e92761d4bf113d9e896f (commit 48c68517b217baf2748f45707787cc834c5e3ab0).

## Kontrola matematyczna i redakcyjna

Sprawdzono indukcję dwumianową w lemacie o uogólnionych przestrzeniach własnych, konstrukcję części S i N, przejście do derywacji wewnętrznych i użycie zerowego centrum. Rozpisano brakującą inkluzję w dowodzie jednoznaczności poprzez rozkład wektora v na przestrzenie własne S'. Uzupełniono założenia i definicję centralizatora. W dowodzie maksymalnej podalgebry toralnej rozdzielono zastosowanie kryterium Cartana do całej półprostej g od niezdegenerowania ograniczenia formy do centralizatora; nie utożsamia się go z formą Killinga centralizatora. Sprawdzono zachowywanie centralizatora przez składowe Jordana, użycie Engela, rozwiązalność przez lemat AA-57, reprezentację ograniczoną do centralizatora i ślad iloczynu górnotrójkątnego. Sprawdzono normalizator, rozpiętość korzeni, przeciwległe wagi, normalizację t_alpha oraz argument śladowy na przestrzeniach własnych ad(t_alpha). W przykładzie sl3 zweryfikowano układ znaków i rysunek: suma alpha12+alpha23=alpha13. Poprawiono składnię i doprecyzowano tytuł twierdzenia. Nie znaleziono fałszywej tezy, lecz audyt zawiera korekty, więc nie jest czysty.

## Niezależne regresje

Uruchomiono jednorazową funkcję JavaScript z arytmetyką BigInt, niezależną od SymPy. Wynik PASS: 12 modeli sl_n (n=2,...,5, trzy dokładne zmiany bazy), 1752 par korzeni dla nawiasów, 1752 par dla śladu reprezentacji dołączonej i parowania, 120 trójek sl2, 141 sprawdzeń nilpotentności i komutowania składowych Jordana. Ranga obliczana eliminacją całkowitą z redukcją przez NWD. Dla każdego modelu sprawdzono wymiar centralizatora regularnego elementu i inkluzję podalgebry diagonalnej po sprzężeniu. Ślad ad_X ad_Y obliczony bezpośrednio na bazie gl_n, gdzie centralny składnik nie wnosi śladu. Pierwsza próba atomowego zapisu testu i workflow została odrzucona podczas równoległego ruchu gałęzi. Trwały zapis drugiego zestawu testów oraz włączenie do CI pozostają do wykonania; nie deklaruje się ich jako zrealizowanych. Testy nie zastępują dowodów.

## CI i werdykt

Run 45375398497 był w toku w momencie kontroli i nie dotyczy niniejszych poprawek. Nie sprawdzono nowego PDF. AA-59 W AUDYCIE, licznik czystych audytów po korektach 0/2. AA-60 nieotwarty. Zakres niezmieniony.
