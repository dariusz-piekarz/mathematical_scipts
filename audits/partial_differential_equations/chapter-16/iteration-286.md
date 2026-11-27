# RRC 16 — iteracja 286: trzecia lektura 033–042

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano definicję przestrzeni Höldera oraz pełne dowody lem:pde16-newton-holder, thm:pde16-schauder-poisson, thm:pde16-scalar-schauder. Zweryfikowano hipotezy thm:pde3-analytic i prop:pde3-gradient.

| Kryterium | Wynik kontroli |
|---|---|
| 033 | Normy i półnormy, rozszerzenie pochodnych na domknięcie, zgodność supremów dzięki gęstości, definicja lokalna na zwartych zbiorach oraz równoważność z lokalnym warunkiem na kulach przez liczbę Lebesgue'a pokrycia. Poprawne. |
| 034 | Reguła iloczynu: rozkład różnicy na dwa składniki; po dodaniu normy supremum pełna norma iloczynu jest ograniczona iloczynem norm. Poprawne. |
| 035 | Reprezentacja Hessianu dla gładkich danych: korekta punktowa -delta_ij f/d, znoszenie na pierścieniach, całka r^{alpha-1} dająca 1/alpha, część daleka kontrolowana przez L¹, a L¹ przez objętość nośnika i supremum. Poprawne. |
| 036 | D=B_L(x), L=R+M+2 zawiera nośnik i oba punkty. Przesunięcie środka: B_{L-h}(x') w D, D w B_{L+h}(x'); zerowa wartość główna na wewnętrznej kuli i J ograniczone przez C h/L. Bliskie całki na B_{2h}(x) oraz B_{3h}(x') ograniczone przez C h^alpha. Poprawne. |
| 037 | Dla |x-y|>=2h cały odcinek argumentów jądra ma moduł >=|x-y|/2. Gradient jądra daje h|x-y|^{-d-1}; po uwzględnieniu różnicy danych i miary radialnej całka h int_{2h}^L r^{alpha-2} dr <= C h^alpha/(1-alpha). Poprawne. |
| 038 | Wspólny pierścień 3h<|y-x'|<L-h leży w E, gdzie nie ma osobliwości. Jego całka znika; pozostałe fragmenty ograniczone przez log 3 i log((L+h)/(L-h)). Nie pojawia się niekontrolowany czynnik log(1/h). Człon f(x')J i korekta punktowa także rzędu h^alpha; dla h>=1/4 wystarcza supremum. Poprawne. |
| 039 | Gamma oraz jej klasyczny gradient lokalnie całkowalne; przy całkowaniu przez części na małej sferze wyraz brzegowy zanika jak epsilon lub epsilon |log epsilon|. Kontrola funkcji i gradientu przez całki modułów jądra na B_{M+R}. Wygładzenia danych zachowują ograniczenia normy i półnormy, zbieżność supremum z błędem n^{-alpha}[f]_alpha i wspólnym zwartym nośnikiem. Poprawne. |
| 040 | Arzelà–Ascoli na zwartych kulach i wybór przekątniowy dla skończonej liczby składowych Hessianu. Jawne tożsamości całkowe na odcinkach identyfikują g_i i H_ij z pochodnymi klasycznymi, dla obu znaków h. Norma Höldera przechodzi do granicy bez założenia zbieżności w tej normie; równanie -Delta u=f wynika z lokalnie jednostajnej zbieżności Hessianów. Poprawne. |
| 041 | Odcięcie danych, kontrola par z obu stron brzegu i potencjału Newtona, harmoniczność reszty. Hipotezy oszacowania gradientu RRC 03 spełnione na domknięciach wszystkich kul o promieniu sigma=(rho-r)/4 użytych w trzech iteracjach. Kontrola pochodnych do rzędu trzy, półnorma Hessianu przez całkowanie na odcinku i pełna norma rozwiązania. Poprawne. |
| 042 | Dodatni współczynnik skalarny: norma odwrotności przez lambda^{-1}, półnorma przez lambda^{-2}[a]_alpha, poprawny znak -Delta u=-f/a. Jednolity promień ell, kontrola par bliskich i dalekich, także na niespójnych zbiorach. Poprawne. |

Nie wykryto nowych błędów ani luk wymagających zmiany źródła. Siódma kolejna czysta iteracja (280–286). Trzecia lektura 42/64. PDF i CI nadal niepotwierdzone. Następna iteracja 287: 043–052 — oszacowanie Schaudera a priori i metoda norm ważonych.
