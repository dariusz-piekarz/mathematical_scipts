# RRC 16 — iteracja 288: trzecia lektura 053–058

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano pełne dowody lem:pde16-commutator i thm:pde16-schauder-variable.

| Kryterium | Wynik kontroli |
|---|---|
| 053 | Komutator z a ograniczoną Hölderowską i g istotnie ograniczoną: oba sploty istnieją w każdym punkcie, są niezależne od reprezentanta g. Różnica a(x)-a(y) na nośniku jądra daje dokładne ograniczenie supremum epsilon^alpha [a]_alpha ||g||_infty. Poprawne. |
| 054 | Dla h>=epsilon wystarcza dwukrotna norma supremum; dla h<epsilon rozpisanie różnicy komutatorów ma poprawne znaki, różnica jąder znika poza B_{2epsilon}(x'). Całkowanie gradientu jądra po odcinku i Tonelli dają h epsilon^{-1}||grad rho||_1. Po przemnożeniu przez (2epsilon)^alpha otrzymuje się czynnik h^alpha(h/epsilon)^{1-alpha}<=h^alpha. Stała pełnej normy niezależna od epsilon<=1. Poprawne. |
| 055 | Trzy współśrodkowe kule i odcięcie równe 1 na otoczeniu domknięcia B_R. Zerowe przedłużenia w=chi u klasy C_c² oraz tilde a, tilde f klasy C_c^{0,alpha}; oszacowanie par po przeciwnych stronach sfery i lokalnych półnorm na domknięciu B_S. Wygładzanie w zbiega jednostajnie wraz z pochodnymi do drugiego rzędu dzięki ich jednostajnej ciągłości. Poprawne. |
| 056 | Dodatni odstęp domknięcia B_R od dopełnienia N zapewnia lokalność wszystkich splotów. Dokładna tożsamość dla a(x)D^beta u_epsilon ma znak plus przed komutatorem. Sumowanie po składowych i członach niższego rzędu daje tilde f*rho_epsilon oraz komutatory, bez wygładzania współczynników po lewej. Wszystkie drugie argumenty komutatorów są ograniczone; wygładzenie f nie zwiększa normy Höldera. Poprawne. |
| 057 | Gładkie u_epsilon spełniają hipotezę lematu a priori, ze stałą niezależną od epsilon. Uzyskana jednostajna kontrola normy C^{2,alpha} na B_r może zależeć od normy C² w; przejście do granicy w nierównościach dwupunktowych Hessianu dzięki zbieżności jednostajnej daje regularność lokalną u bez błędnego koła. Poprawne. |
| 058 | Po uzyskaniu regularności ponowne zastosowanie lematu a priori bezpośrednio do u usuwa zależność od jego normy C². Wspólny dodatni promień ell, domknięcia kul B_{2ell}(x) zawarte w V, stałe kontrolowane przez dane na domknięciu V. Dla par bliskich oszacowanie na jednej kuli, dla dalekich dwukrotne supremum razy ell^{-alpha}; pełna norma także dla niespójnego U. Poprawne. |

Nie wykryto nowych błędów ani luk wymagających zmiany źródła. Dziewiąta kolejna czysta iteracja (280–288). Trzecia lektura 58/64. PDF i CI nadal niepotwierdzone. Następna iteracja 289: 059–064 i zamknięcie trzeciej lektury.
