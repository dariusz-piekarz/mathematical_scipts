# Topologia ogólna — rozdział 18: audyt iteracja 02

Data: 2026-11-22. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: chapters/pl/general_topology/18-przestrzenie-odwzorowan-i-topologia-zwarto-otwarta.tex.

## Zakres ponownej kontroli

Ponownie zweryfikowano całą treść rozdziału 18, niezależnie od wniosków audytu 01, ze szczególnym uwzględnieniem twierdzenia o zgodności topologii, prawa wykładniczego i zupełności. Sprawdzono kwantyfikatory, konstrukcje otoczeń, przypadki zbioru pustego, przestrzenie nie-Hausdorffa i niezliczalne dziedziny, a także odsyłacze do rozdziałów 12 i 14.

## Wyniki matematyczne

1. **Topologia zwarto-otwarta**. Zbiory [K,U] są podbazą i dla K pustego dają pełne C(X,Y). Zwartość singletonu {x}, bez warunków T1, zapewnia zawieranie topologii zbieżności punktowej. Jeśli Y jest Hausdorffa, to dwie różne funkcje można rozdzielić odpowiednimi otoczeniami wyznaczonymi przez {x}.
2. **Ciągłość składania**. Dla u:X'→X i v:Y→Z ciągłych bezpośrednio obliczamy przeciwobrazy [K',U] przez prekompozycję jako [u(K'),U], a przez postkompozycję jako [K,v^{-1}(V)]. Nie założono milcząco zwartości lokalnej dziedzin.
3. **Baza topologii zbieżności jednostajnej na zbiorach zwartych**. Dla K niepustego funkcja d(f,g)|K osiąga maksimum m<ε, więc B_K(g,ε−m) mieści się w B_K(f,ε). Dla K pustego otoczenia są całym zbiorem odwzorowań. Rodzina spełnia aksjomaty otoczeń.
4. **Zgodność z topologią zwarto-otwartą**. Kierunek od [K,U] do B_K(f,η/2) wykorzystuje ciągłość odległości od domkniętego D=Y\U i dodatnie minimum tej odległości na f(K). Kierunek od B_K(f,ε) do otoczenia zwarto-otwartego wykorzystuje δ=ε−max_K d(f,g)>0, skończone pokrycie g(K) kulami o promieniu δ/4 i zwarte K_j=K∩g^{-1}(closed ball(y_j,δ/4)). Otoczenie W=∩_j[K_j,B(y_j,δ/2)] zawiera g, bo na każdym K_j odległość do y_j jest ≤δ/4<δ/2. Dla h∈W mamy d(f(x),h(x))<m+3δ/4<ε na każdym K_j, więc W⊂B_K(f,ε). Właśnie tę ostatnią własność „g∈W” wyjaśniono bez przeskoku w audycie 02. Nie trzeba lokalnej zwartości ani Hausdorffowości X.
5. **Zbieżność sieci**. Po równości dwóch topologii definicja zbieżności sieci w bazie B_K(f,ε) jest dokładnie jednostajną zbieżnością na każdym zwartym K, bez wymogu przeliczalności zbioru indeksów.
6. **Ciągłość ewaluacji**. Lokalna zwartość i Hausdorffowość X dają W otwarty i K zwarty z x∈W⊂K⊂f^{-1}(V). Zbiór [K,V]×W zapewnia otoczenie w przestrzeni produktu, całkowicie odwzorowywane do V. Założenia są poprawne.
7. **Prawo wykładnicze**. Dla F:Z×X→Y dowolnego ciągłość wszystkich przekrojów F_z nie jest zakładana przed dowodem. Gdy F jest ciągłe, zwartym K można objąć skończenie wieloma prostokątami, co daje ciągłość \hat F na podbazie. W przeciwnym kierunku F jest złożeniem ciągłego \hat F×id_X z ewaluacją. Zwięzłe sformułowanie bijekcji zbiorów ciągłych odwzorowań nie twierdzi bez dowodu silniejszego homeomorfizmu przestrzeni takich odwzorowań.
8. **Kontrprzykład na Q**. Zwarte K_j⊂Q mają puste wnętrza, podobnie ich skończona suma K. Każde otoczenie zera i każda otwarta okolica 0 w Q dopuszczają r∉K. Funkcja min(1,d(q,K)/d(r,K)) jest ciągła, zeruje się na K, ale przyjmuje wartość 1 w r. Dla K pustego funkcja stała 1 pełni tę samą rolę. Stąd ewaluacja nie jest ciągła w (0,0).
9. **Metryka z wyczerpania zwartego**. Wagi 2^{-n}, ograniczenie min(1,d) i pokrycie X przez K_n dają właściwą, skończoną metrykę D. Dwa kierunki równości topologii wynikają z kontroli pojedynczych poziomów K_n oraz ogona zbieżnego szeregu wag. Wykorzystana współkońcowość K_n dla zwartych K pochodzi z rozdziału 14.
10. **Zupełność**. Ciąg Cauchy'ego względem D jest jednostajnie Cauchy'ego na każdym K_n, ponieważ 2^{-n}ρ_n≤D. Każda wartość funkcji ma granicę w zupełnym Y. Po przejściu do granicy k→∞ w oszacowaniu dla par f_j,f_k otrzymujemy jednolitą nierówność d(f_j(x),f(x))≤ε. W audycie 02 doprecyzowano wybór dowolnego η>0 i 0<ε<min(1,η); wspólny indeks j_0 dla wszystkich x∈K_n zapewnia jednostajną zbieżność. Ponieważ wnętrza K_n pokrywają X, f jest ciągła, a następnie D(f_j,f)→0.
11. **Przykłady graniczne**. Przesuwane „górki” f_n mają sup normę 1, ale dla każdego ustalonego zwartego K⊂R znikają na nim ostatecznie. Dla nieprzeliczalnej dyskretnej X zbiory zwarte są skończone, więc C_k(X,R)=R^X z topologią produktową. Przeliczalna rodzina bazowych otoczeń zera zależałaby łącznie od co najwyżej przeliczalnej rodziny współrzędnych, co przeczy potrzebie kontroli dowolnej dodatkowej współrzędnej. Dowód braku pierwszego aksjomatu przeliczalności jest kompletny.
12. **Język i formalny zapis**. Nagłówek „Charakteryzacja zbieżności sieci” zmieniono na „Charakterystyka zbieżności sieci”. Utrzymano terminologię „zbieżność jednostajna na zbiorach zwartych” i „przestrzeń spełnia pierwszy aksjomat przeliczalności”, bez niepożądanych zamienników.

## Poprawki w iteracji 02

- Poprawiono argument „W jest otwartym otoczeniem funkcji g” przez jawne oszacowanie na K_j.
- Rozpisano ilościowo krok przejścia od oszacowania Cauchy'ego do jednostajnej zbieżności granicy na K_n.
- Ujednolicono nagłówek charakterystyki zbieżności sieci.
- Rozszerzono test ch18: weryfikacja wszystkich 29 topologii na trzyelementowym zbiorze, w tym nie-Hausdorffa, dla funkcji ciągłych do dwuelementowej metrycznej przestrzeni dyskretnej; kontrola, że zarówno otoczenie zwarto-otwarte, jak i jednostajne na całym zwartym X izoluje tę samą funkcję. Zachowano sprawdzanie metryki z wyczerpania, modeli górek, struktury, etykiet, odsyłaczy i terminologii.

Commity:
- TeX: c16355aef6f1ec48255f9bc067b2cec31f7107c8.
- Test: 49d93f5ba964402d829c1b4485376e46c64bd58f.

Porównano sformułowanie głównego twierdzenia z opracowaniem topologii zwarto-otwartej z Uniwersytetu w Nijmegen oraz formalizacją compact-open = compact-convergence w Mathlib 4. Nie zmieniono hipotez, ponieważ obejmują one dowolne X i metryczne Y.

## Wynik

| Warstwa | Stan |
| --- | --- |
| Pełna kontrola matematyczna | PASS po doprecyzowaniach |
| Kontrprzykłady i przypadki brzegowe | PASS |
| Terminologia, oznaczenia i odsyłacze | PASS |
| Testy regresji i CI | Do potwierdzenia po zmianach |
| PDF i logi LaTeX | Do potwierdzenia po zmianach |
| Decyzja | W AUDYCIE — nowy niezależny audyt 03 po walidacji |

Pierwszy audyt pozostaje w audits/general_topology/18-przestrzenie-odwzorowan-iteracja-01.md. Nie należy oznaczać rozdziału stabilnym bez czystej, niezależnej iteracji po nowych poprawkach.
