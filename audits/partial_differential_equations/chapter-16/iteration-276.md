# RRC 16 — iteracja 276: druga lektura 001–012

Źródło przed 930b0be4cfa0f0eea0b5e73b327ab8d8e180caf0 (1821 wierszy), po 979ec37ab74b0e0c366eac2f6d43711e19967a67 (1823 wiersze), commit 741807b8279e1cf4efd1a46bf3736fec1dbb2512.

| Kryterium | Wynik kontroli |
|---|---|
| 001 | Wstęp i konwencja Fouriera zgodne z RRC 08; wzór i znak rozwiązania fundamentalnego zgodne z thm:pde7-laplace, odmienny indeks omega nie zmienia definicji pola sfery. |
| 002 | Różniczkowanie obu wzorów Gamma daje -x_i/(omega |x|^d), a następnie poprawne K_ij. Uściślono oznaczenie delty Kroneckera i sformułowanie językowe. |
| 003 | Jednorodność jądra i gradientu, symetrie sfery i zerowa średnia — poprawne. |
| 004 | Niezerowość na otwartym fragmencie sfery dla wszystkich i,j, d>=2, radialna rozbieżność int_0^1 dr/r, dolne ograniczenie |f(x-z)| przy f(x) != 0 — poprawne. |
| 005 | Główna wartość na testach C_c^1: podstawienie, odejmowanie stałej dzięki zerowej całce po pierścieniu, obie całki bezwzględnie zbieżne i ograniczenie supremum — poprawne. |
| 006 | Definicja p.v. K na C_c^infty, liniowość, kontrola półnorm na każdym zwartym nośniku — poprawne. |
| 007 | Dwukrotne całkowanie przez części na pierścieniu, zgodność kolejności pochodnych, znaki obu wyrazów brzegowych — poprawne. |
| 008 | Normalna -theta na wewnętrznej sferze, skala miary, granica -delta_ij/d razy phi(0), zanikanie pozostałego wyrazu także d=2 — poprawne. |
| 009 | Splot z testem i przemienność pochodnych zgodne z lem:pde7-convolution-derivatives, delta_0*f=f — poprawne. |
| 010 | Ograniczoność T_ij f i zanik poza 2R dają L² niezależnie od oszacowania docelowego; H_ij należy do L². |
| 011 | Równanie dla H_ij i rachunek Fouriera w S', lokalna całkowalność obu stron, jednoznaczność dystrybucji regularnych, dzielenie poza zerem i brak składnika punktowego. Dodano dokładny odsyłacz do udowodnionej gęstości C_c^infty w przestrzeni Schwartza (thm:pde8-density). |
| 012 | Rzeczywisty ograniczony mnożnik, normalizacja Plancherela, jednoznaczne przedłużenie przez zupełność i gęstość. Dodano odsyłacz do tego samego twierdzenia o gęstości w L². |

Nie stwierdzono nowych błędów merytorycznych w sprawdzonym zakresie. Wprowadzono doprecyzowanie notacji i dwa odsyłacze zgodnie z zasadą jawnego uzasadniania. Wszystkie 30 etykiet zachowane; 73/73 odsyłaczy do 41 celów w RRC 03,07,08,09,15,16,17, bez brakujących i wieloznacznych w sprawdzonych plikach. Stos środowisk poprawny przed zapisem. PDF i CI nadal niepotwierdzone. Druga lektura 12/64 z drobnymi poprawkami. Następna iteracja 277: 013–024.
