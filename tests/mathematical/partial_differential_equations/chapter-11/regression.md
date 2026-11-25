# Rozdział 11 — trwały rejestr kryteriów regresyjnych

Kryteria semantyczne są punktami ręcznego audytu matematycznego, a nie formalnymi dowodami wykonywanymi przez CI. Pierwsza lektura, następnie druga stabilizacyjna i niezależna trzecia, testy wykonywalne tam, gdzie mają sens, kontrola strukturalna oraz kompilacja i kontrola PDF.

| ID | Kotwica | Kryterium | Typ |
| --- | --- | --- | --- |
| PDE-11-001 | sec:pde11-weak | Rzeczywiste przestrzenie, ograniczony obszar Lipschitzowski, V=H_0^1, jawna stała Poincarégo, dodatnia określoność iloczynu energetycznego. | semantyczna |
| PDE-11-002 | sec:pde11-weak | Równoważność norm i zupełność przez domkniętość H_0^1 w H^1; zależności z rozdziałów 09 i 10. | semantyczna |
| PDE-11-003 | def:pde11-dual | Ograniczoność a ciągłość funkcjonału, norma supremum, dodatnia określoność, jednorodność i nierówność trójkąta. | semantyczna |
| PDE-11-004 | def:pde11-dual | Słabe rozwiązanie i norma H^{-1} względem normy energetycznej; poprawny kierunek obu nierówności porównania norm funkcjonału. | semantyczna |
| PDE-11-005 | def:pde11-dual | Iniektywne ograniczenie funkcjonałów H^{-1} do dystrybucji, oszacowanie na testach o wspólnym zwartym nośniku, gęstość. | semantyczna |
| PDE-11-006 | ex:pde11-poisson-weak | C² na otoczeniu domknięcia, H¹ i zerowy ślad przez gładkie odcięcie, splot, zbieżność jednostajną i ciągłość śladu. | semantyczna |
| PDE-11-007 | ex:pde11-poisson-weak | Całkowanie przez części dla testów, oba oszacowania ciągłości, aproksymacja w V i przejście do granicy. | semantyczna |
| PDE-11-008 | ex:pde11-poisson-weak | Równość dystrybucyjna -Delta u=f z poprawnym znakiem, interpretacja ogólnego F, zerowy ślad oraz rozróżnienie istnienia i regularności. | semantyczna |
| PDE-11-009 | lem:pde11-projection | Skończone infimum, ciąg minimalizujący, wypukłość, tożsamość równoległoboku, Cauchy, domkniętość i jednoznaczność. | semantyczna |
| PDE-11-010 | lem:pde11-projection | Charakterystyka rzutu nierównością wariacyjną w obie strony; ortogonalność przy podprzestrzeni. | semantyczna |
| PDE-11-011 | thm:pde11-riesz | F=0, domknięte właściwe jądro F niezerowego, rzut x na jądro i niezerowy wektor prostopadły, F(e) != 0. | semantyczna |
| PDE-11-012 | thm:pde11-riesz | Konstrukcja reprezentanta przez odjęcie składowej e; jednoznaczność przez podstawienie różnicy, równość norm, liniowość i surjektywność izometrii. | semantyczna |

| PDE-11-013 | def:pde11-coercivity | Definicje ograniczoności i koercywności; jawny niesymetryczny przykład i jego stałe. | semantyczna |
| PDE-11-014 | thm:pde11-LM | Przestrzeń zerowa osobno; dla niezerowej przestrzeni 0<alpha<=M. | semantyczna |
| PDE-11-015 | thm:pde11-LM | Reprezentacja formy przez Riesza, liniowość T, norma operatora, równoważność równania Tu=f. | semantyczna |
| PDE-11-016 | thm:pde11-LM | Rozwinięcie kwadratu, zakres t, nieujemność podpierwiastkowa i minimum oszacowania q. | semantyczna |
| PDE-11-017 | thm:pde11-LM | Przypadek q=0, indukcja dla kolejnych różnic i suma geometryczna. | semantyczna |
| PDE-11-018 | thm:pde11-LM | Zupełność, ciągłość S_t, punkt stały, oszacowanie błędu iteracji. | semantyczna |
| PDE-11-019 | thm:pde11-LM | Jednoznaczność z koercywności, oszacowanie rozwiązania, bijekcja T i ograniczoność odwrotności. | semantyczna |
| PDE-11-020 | cor:pde11-stability | Stabilność różnicy rozwiązań względem funkcjonału; poprawność Hadamarda dla ustalonej formy. | semantyczna |
| PDE-11-021 | thm:pde11-elliptic | Normy macierzy i wektorów, mierzalność i całkowalność składników, dwuliniowość. | semantyczna |
| PDE-11-022 | thm:pde11-elliptic | Ograniczoność i koercywność z eliptyczności, c>=0, bez symetrii; oszacowanie rozwiązania. | semantyczna |
| PDE-11-023 | thm:pde11-elliptic | Tożsamość dystrybucyjna i jej odwrotność przez gęstość testów; ogólny F. | semantyczna |
| PDE-11-024 | ex:pde11-1d | Jawne rozwiązanie, pochodne, zerowy ślad, gęstość i jednoznaczność. | semantyczna |
| PDE-11-025 | thm:pde11-lower-order | Wspólny zbiór pełnej miary przez wymierne wektory, ograniczoność wszystkich trzech składników, stała koercywności. | semantyczna |
| PDE-11-026 | ex:pde11-divfree-drift | Zanik składnika dryftu przez test u², jawne oszacowanie różnicy przy aproksymacji, brak warunku małości. | semantyczna |

| PDE-11-027 | thm:pde11-lifting | Rozszerzenie formy na H¹ razy V, równoważność warunku brzegowego z zadanym śladem i redukcja do równania dla w. | semantyczna |
| PDE-11-028 | thm:pde11-lifting | Ciągłość funkcjonału G, jawna stała K+C_c C_P, oszacowanie normy pełnej rozwiązania. | semantyczna |
| PDE-11-029 | thm:pde11-lifting | Istnienie i jednoznaczność oraz niezależność od wyboru podniesienia o tym samym śladzie. | semantyczna |
| PDE-11-030 | thm:pde11-lifting | Dopuszczalność danych w przestrzeni śladów; przypadek d=1, w którym wszystkie dane L² są dopuszczalne. | semantyczna |
| PDE-11-031 | thm:pde11-lifting | Izometryczne podnoszenie śladu z rozdziału 10, oszacowanie przez normę śladową, brak zależności kołowej od rozdziału 13. | semantyczna |
| PDE-11-032 | sec:pde11-neumann | Pierwszy wzór Greena dla gładkiego przypadku i znaki danych przy normalnej zewnętrznej; brak założenia klasycznej pochodnej normalnej rozwiązania słabego. | semantyczna |
| PDE-11-033 | thm:pde11-neumann | Konieczność warunku zgodności przez test stały i skończoność całek. | semantyczna |
| PDE-11-034 | thm:pde11-neumann | Domkniętość przestrzeni średniej zero, osobna stała Poincarégo, iloczyn skalarny i zupełność. | semantyczna |
| PDE-11-035 | thm:pde11-neumann | Ograniczoność i koercywność ze stałą 1, ciągłość funkcjonału z danymi brzegowymi, jawne oszacowanie H¹. | semantyczna |
| PDE-11-036 | thm:pde11-neumann | Rozszerzenie tożsamości na wszystkie testy H¹ przez odjęcie średniej, interpretacja dystrybucyjna. | semantyczna |
| PDE-11-037 | thm:pde11-neumann | Jednoznaczność z dokładnością do stałych przez nierówność Poincarégo; spójność, normalizacja. | semantyczna |

## Iteracja 167 — pierwsza lektura 001–012
Odczytano aktualny rozdział 11 (966 wierszy przed zmianami), potwierdzono włączenie do książki na pozycji 11. Nie znaleziono dotychczasowego rejestru chapter-11/regression.md (404). Źródło przed b06d7b5554c8b06dc80c53dea0050681bc971f61, po f0e5cde93e447288a38ec2d86bc32a12968138cd, commit c9f1a3afb35242d756013126e8d7734e2cc86126. Czternaście dokładnych zmian w pierwszych dwóch sekcjach: norma energetyczna i jej zupełność, norma funkcjonału oraz konwencja H^{-1}, dystrybucje, przynależność klasycznego rozwiązania do H_0^1, przejście przez gęstość, znak dystrybucyjnego laplasjanu, pełna charakterystyka rzutu i dowód Riesza. Zachowano 36 etykiet (unikatowe) w tej samej kolejności, 24 wystąpienia odsyłaczy rozwiązane w 09, 10, 11, 13; odsyłacz thm:pde13-nonhom rzeczywiście istnieje, jego użycie merytoryczne będzie kontrolowane we właściwej sekcji. Stos środowisk poprawny, treść od sekcji Laxa–Milgrama bez zmian. Nie uruchamiano testów wykonywalnych, CI, kompilacji ani Lean. Następna iteracja: twierdzenie Laxa–Milgrama, przypadek H={0}, konstrukcja kontrakcji i oszacowanie stabilności, następnie formy eliptyczne. Rejestr 12 kryteriów pierwszej lektury; ostateczna liczba kryteriów rozdziału jeszcze nieustalona.

## Iteracja 168 — pierwsza lektura 013–026
Źródło przed f0e5cde93e447288a38ec2d86bc32a12968138cd, po eb0769dc945074810666048384195fb6e1228451, commit dd15f2bf1d3cfe791a20b372f89c5780752e93b8. Odczytano sekcje Laxa–Milgrama i równań eliptycznych. Czternaście zmian źródłowych: przypadek przestrzeni zerowej, niesymetryczna forma, liniowość i odwracalność T, zakres kroku i q=0, szczegóły iteracji i błędu, stabilność, mierzalność i normy współczynników, równoważność dystrybucyjna, przykład jednowymiarowy i zanik dryftu. Zachowano 36 unikatowych etykiet w tej samej kolejności; 28/28 wystąpień odsyłaczy rozwiązanych w 09,10,11,13; stos środowisk poprawny; wcześniejszy i późniejszy materiał bez zmian. Rejestr pierwszej lektury 26 kryteriów. Nie wykonywano testów, CI, kompilacji ani Lean. Następna iteracja: niezerowe dane Dirichleta i zagadnienie Neumanna (podnoszenie, warunek zgodności, jednoznaczność modulo stałe).

## Iteracja 169 — pierwsza lektura 027–037
Źródło przed eb0769dc945074810666048384195fb6e1228451, po 4bee504fbd7056892092c6096d0a5460a4fea8b9, commit 91dae75b8a1ceba53434a851cd284fd66620f1aa. Odczytano sekcje podnoszenia i Neumanna oraz właściwe twierdzenia rozdziałów 10 i 13. Dziesięć zmian źródłowych: jawna dziedzina formy mieszanej, stałe oszacowań i niezależność od podniesienia, dopuszczalność danych także d=1, oszacowanie normą ilorazową, znaki wzoru Greena, konieczność zgodności, zupełność przestrzeni średniej zero, osobna stała Poincarégo, oszacowanie znormalizowanego rozwiązania oraz rozszerzenie testów i jednoznaczność. Zachowano 36 unikatowych etykiet w tej samej kolejności; 35/35 wystąpień odsyłaczy rozwiązanych w 09,10,11,13; stos środowisk poprawny; materiał przed i po sekcjach bez zmian. Rejestr pierwszej lektury 37 kryteriów. Nie wykonywano testów, CI, kompilacji ani Lean. Następna iteracja: metoda bezpośrednia rachunku wariacyjnego, słaba zbieżność, słaba zwartość ciągowa i dolna półciągłość.
