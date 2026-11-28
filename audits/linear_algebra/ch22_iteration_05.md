# Algebra liniowa — rozdział 22, audyt V (pierwszy czysty po korekcie składu)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Blob po audycie IV:** `11aafed28081c5db85005cf235f51b6795710705`  
**Poprzedni etap:** audyt IV wykrył i poprawił jedno przepełnienie wiersza (bez zmian matematycznych).

## Powtórne sprawdzenie

1. Założenia wszystkich twierdzeń określają ciało, rozmiary macierzy i dziedziny; brak przemilczanej algebraicznej domkniętości w części Sylvestera. Odróżniono `n,m≥1` od wcześniejszych konwencji w wymiarze zerowym.
2. Przestrzeń jądra `S_(A,B)` odpowiada operatorom przeplatającym `W_B→V_A`, a jej wymiar jest sumą stopni NWD odpowiednich czynników niezmienniczych. Różne kierunki mapowania nie zmieniają symetrycznej sumy stopni.
3. Kryterium Sylvestera korzysta z twierdzenia o wymiarze obrazu i jądra na przestrzeni `Mat_{n×m}(K)`; stwierdza rozwiązanie dla **każdego** `C`, a nie dla arbitralnego już ustalonego `C`.
4. Wzór teleskopowy działa przy `k=1` (suma jednoelementowa) oraz dowolnym `k≥1`; uzyskany wzór zamknięty na `X` zachowuje właściwą kolejność mnożenia. Nowy test wykonawczy nad `F2,F3` sprawdza go niezależnie przez podstawienie.
5. W przypadku `J_a(λ),J_b(μ)` uzasadniono nilpotentność operatora `X↦NX-XM` o indeksie co najwyżej `a+b-1`. Gdy `λ≠μ`, skończona seria rozwiązuje równanie, także w charakterystyce dodatniej; dla `λ=μ` wymiar jądra to `min(a,b)`.
6. W twierdzeniu Lapunowa istnienie, zbieżność i hermitowska dodatnia określoność są wykazane odrębnie. Jednoznaczność obowiązuje bez początkowego założenia hermitowskości nieznanego rozwiązania. Kierunek odwrotny wynika z rachunku wektora własnego, a nie z intuicji dynamicznej.
7. Przykład niediagonalny ma sprawdzoną macierz `P`, a formuła `z*Pz=1/2|x+y/3|²+5/18|y|²` pozostaje poprawna nad `C` bez dodatkowych założeń.

## Integracja

Źródło ma 25 unikatowych etykiet, 25 odsyłaczy oraz 10 poprawnych par środowisk dowodów. Odsyłacze do rozdziałów 16–21 po poprawie są prawidłowe. Skrócone założenia w twierdzeniu o wzorze wykonawczym zachowują tę samą tezę i nie wprowadzają nowych oznaczeń.

**Decyzja:** audyt V matematycznie i redakcyjnie czysty; stan techniczny końcowego PDF będzie ostatecznie potwierdzony po zrealizowaniu pełnego workflow. Pierwszy czysty przebieg po ostatniej korekcie tekstu.
