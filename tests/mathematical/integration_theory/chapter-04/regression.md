# IT-04 — regresje KH (rozszerzenie MA1-36)
| ID | Kryterium | Metoda |
|---|---|---|
| IT-04-001 | Jednoznaczność: minimum cechowań i Cousin | semantyczna |
| IT-04-002 | Funkcja Dirichleta: grupowanie komórek z powtórzonym znacznikiem | semantyczna + Python |
| IT-04-003 | Ciągłość pierwotnej z jednej komórki częściowej, obie orientacje | semantyczna |
| IT-04-004 | Hake dla funkcji dyadycznej: kontrola ostatniej niepełnej komórki | semantyczna + Python |
| IT-04-005 | Jednostajna całkowalność: wspólne cechowanie, Cauchy i przejście do granicy na ustalonym podziale | semantyczna + Python |
| IT-04-006 | Hake: lokalne cechowania przy wspólnym końcu, rozcięcie i suma błędów | semantyczna + Python |
| IT-04-007 | Kryterium Cauchy'ego: malejące cechowania, wspólny podział dopełnienia i lokalność | semantyczna + Python |
| IT-04-008 | Zmiana na zbiorze zerowym: cechowanie także dla punktów o wartości zero, sumowalny budżet | semantyczna + Python |
| IT-04-009 | Różniczkowanie pierwotnej: dwa znaki przyrostu, mierzalne ilorazy, zupełność miary | semantyczna |
| IT-04-010 | Pochodna x^2 cos(pi/x^2): poprawne podstawienie, dolne oszacowania okresów i rozbieżność modułu | semantyczna |
| IT-04-011 | Dolne oszacowania półokresów przy beta>=0 oraz -1<=beta<0 i próg zbieżności modułu | semantyczna + Python |
| IT-04-012 | Newton–Leibniz dla pochodnej we wnętrzu: ciągłość F wystarcza na końcach; dowolne skończone wartości f(a), f(b); osobny budżet błędów | semantyczna + Python |
| IT-04-013 | Oscylacyjna całka dla beta<0: całkowanie przez części, oszacowanie ogona 2A^beta, kryterium Cauchy'ego | semantyczna + Python |
| IT-04-014 | Zbieżność zmajoryzowana: wspólny zbiór wyjątkowy, mierzalność granicy przez zupełność, zgodność z HK | semantyczna |
| IT-04-015 | Podstawienie: obrazy rozłącznych wnętrz, bi-lipschitzowskość, charakterystyka ACG_* i pochodna p.w.; mnożniki BV i AC | semantyczna |
| IT-04-016 | Pokrycie 5r również dla domkniętych komórek ze znacznikiem na końcu; co najwyżej przeliczalna podrodzina i suma po skończonych podrodzinach | semantyczna |

Audyt po migracji: commit 8ef0ada28df587a817668d19ea315b10b394b374, blob c13d123ecc187dd6ef8c951950b7ce8fd248d120, 36/36 etykiet zachowanych. Zmieniono dowód całkowalności pochodnych na końcach, rozpisano konieczność Hake'a i oszacowanie oscylacyjne, doprecyzowano mierzalność i zależności. Sprawdzono m.in. Cousina, kryterium Cauchy'ego, lokalność, Saks–Henstock, pokrycie 5r, podstawienie i mnożniki oraz jednostajną całkowalność. Nowe testy w febe58bba89cb991b61f4e38bbc28e3793bdebbc; nie potwierdzono jeszcze ich wykonania. Poprzedni CI 45621624236: 27/27, 130 stron; nie dotyczy nowych poprawek. Kontrola PDF i Lean nieprzeprowadzone.

Kontrola II (2026-11-25): CI 45622315897, job 139233411193, zakończony sukcesem, 29/29 testów (IT-04 9/9), dwa przebiegi LaTeX, 131 stron w drugim. Ostrzeżenia Overfull 3.89328pt, 0.59775pt oraz Underfull 1194; bez kontroli wizualnej. Ponownie sprawdzono wszystkie dowody IT-04 oraz rzeczywiste zależności IT-08 (ACG_*, pochodna p.w.) i IT-11 (McShane=Lebesgue, bezwzględna całkowalność, DCT, AC, Alexiewicz, lemat 5r), IT-07 (liniowość). Uzupełniono przejście od kul otwartych do domkniętych komórek w dowodzie różniczkowania pierwotnej i jawne użycie liniowości przy modyfikacji na zbiorze zerowym; dodano odsyłacz do dowodu niezupełności w IT-11. Commit 68b7836c91811c7f5b7e5f80945669fb7c5132f1, blob 05687dca689e3354e0f3d840a388f5bcbbadb700, etykiety 36/36, trzy nowe odsyłacze mają cele. Nie zmieniono twierdzeń. Nowa wersja wymaga potwierdzenia CI; nie przenosić sukcesu starszego przebiegu. Lean i PDF wizualnie niekontrolowane.
