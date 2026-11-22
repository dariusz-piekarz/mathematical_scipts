# Topologia ogólna — rozdział 18, audyt iteracja 03

Data: 2026-11-22. Gałąź: biblioteka-matematyczna-iteracja-6.
Audytowane źródło: chapters/pl/general_topology/18-przestrzenie-odwzorowan-i-topologia-zwarto-otwarta.tex.
SHA źródła: f7340514548ed3dfb5d98793bf7068fd84276c30.
SHA testu: 206e55aa176b7f5789dae5d2779ef6d72736260b.

## Metoda i zakres

Przeprowadzono trzeci, niezależny audyt wszystkich istniejących twierdzeń, definicji, przykładów i kontrprzykładów rozdziału 18, bez dodawania wyników ani zmiany treści matematycznej i LaTeX. Ponownie oceniono każde użycie zwartości, metryzowalności i Hausdorffowości oraz poprawność przejść do granicy. Przejrzano również strukturę publikacji, język matematyczny i wszystkie zależności od wcześniejszych rozdziałów.

## Kontrola matematyczna

1. **Definicja C_k(X,Y).** Dla dowolnych przestrzeni X,Y przestrzeń odwzorowań ciągłych ma topologię generowaną przez zbiory [K,U] jako podbazę; K jest dowolnym zwartym podzbiorem X, U jest otwartym w Y. Dla K pustego [K,U] jest pełnym C(X,Y). Nie ma niejawnego założenia Hausdorffowości X ani Y.
2. **Relacja z topologią punktową i aksjomat Hausdorffa.** Każdy singleton {x} jest zwarty bez warunków oddzielania; podbazowe [ {x},U ] dają ciągłość ewaluacji w ustalonym x i zawieranie topologii punktowej. Dla Hausdorffa Y różne funkcje rozdzielamy otoczeniami ich różnych wartości w ustalonym punkcie x.
3. **Prekompozycja i postkompozycja.** Obrazy zwarte u(K') są zwarte, a przeciwobrazy otwartych v^{-1}(V) są otwarte. To wystarcza do obliczenia przeciwobrazów [K,U] i ciągłości obu operatorów na C_k. Nie użyto tutaj lokalnej zwartości.
4. **Definicja jednostajnej zbieżności na zwartych.** B_K(f,ε) zawierają f, skończone przecięcia kontroluje K_1∪K_2 (zwarty), a dla g∈B_K(f,ε) funkcja ciągła x↦d(f(x),g(x)) osiąga na niepustym zwartym K maksimum m<ε. Wówczas B_K(g,ε−m)⊂B_K(f,ε). Przypadek pustego K jest jawny.
5. **Równość topologii zwarto-otwartej i jednostajnej na zwartych.** W pierwszym kierunku dodatnia odległość od domkniętego Y\U ma dodatnie minimum na zwartym f(K), zatem małe jednostajne otoczenie mieści się w [K,U]. W drugim kierunku dla dowolnego g∈B_K(f,ε), przy δ=ε−max_K d(f,g)>0, otrzymujemy skończone pokrycie g(K) kulami promienia δ/4. K_j=K∩g^{-1}(closedball(y_j,δ/4)) są zwartymi podzbiorami K, choć X może nie być Hausdorffa. Otoczenie W=∩_j[K_j,B(y_j,δ/2)] **zawiera g** dzięki nierówności d(g(x),y_j)≤δ/4; dla h∈W mamy d(f(x),h(x))<m+3δ/4<ε. Dowód daje całą topologiczną równość, a nie tylko kryterium zbieżności ciągów; nie wymaga lokalnej zwartości X.
6. **Charakterystyka zbieżności sieci.** Wynika bezpośrednio z lokalnej bazy B_K(f,ε); dozwolone są dowolne skierowane zbiory indeksów, więc nie dochodzi do nieuzasadnionej zamiany sieci na ciągi.
7. **Przykład uciekających górek.** Podpora f_n(x)=max(1−|x−n|,0) przesuwa się w prawo, poza każdy ustalony ograniczony zwarty K⊂R. Wartość w n pozostaje równa 1, co dowodzi braku jednostajnej zbieżności globalnej.
8. **Ciągłość ewaluacji.** Dla lokalnie zwartej Hausdorffa X z rozdziału 14 dostępne jest otwarte W i zwarty K z x_0∈W⊂K⊂f_0^{-1}(V). Otoczenie [K,V]×W należy do przeciwobrazu V przez ev. Nie ma założeń metryczności Y ani X.
9. **Prawo wykładnicze.** Przy F:Z×X→Y dowolnym najpierw określamy przekroje F_z:X→Y, a dopiero po sprawdzeniu ich ciągłości można uważać \hat F:Z→C_k(X,Y) za odwzorowanie. Gdy F jest ciągłe, zwartość K pozwala dobrać skończoną rodzinę prostokątów otwartych zawartych w F^{-1}(U), zapewniając ciągłość \hat F na zbiorach podbazowych [K,U]. K pusty jest uwzględniony. Odwrotnie F=ev∘(\hat F×id_X), a ev jest ciągłe przy podanych warunkach X. Wynik stwierdza bijekcję zbiorów ciągłych odwzorowań, nie wymaga dodatkowego twierdzenia o homeomorfizmie przestrzeni funkcji.
10. **Nieciągłość ewaluacji dla Q.** Każdy zwarty K⊂Q ma puste wnętrze (wynik z rozdziału 14); skończona suma takich K również. Dla dowolnej bazowej okolicy zerowej funkcji i dowolnego otwartego V∋0 wybiera się r∈V\K. Funkcja g(q)=min(1,d(q,K)/d(r,K)) jest ciągła, ma g|_K=0 i g(r)=1; przypadek K pustego jest rozwiązany oddzielnie. Zatem ev nie jest ciągłe w (0,0).
11. **Metryka wyznaczona przez wyczerpanie zwarte.** Dla lokalnie zwartej σ-zwartej Hausdorffa X rozdział 14 daje K_n o zwartych domknięciach, rosnące w sensie K_n⊂int K_{n+1}, których wnętrza pokrywają X, i każdy zwarty K mieści się w pewnym K_N. Pseudometryki ρ_n(f,g)=sup_{K_n}min(1,d(f(x),g(x))) są ograniczone przez 1 i spełniają nierówność trójkąta. Szereg D=Σ2^{-n}ρ_n jest skończony, spełnia nierówność trójkąta i oddziela różne funkcje, gdyż K_n pokrywają X. Zbieżność względem D zachodzi dokładnie przy zbieżności jednostajnej na wszystkich K_n, równoważnej zbieżności jednostajnej na wszystkich zbiorach zwartych. Rozumowanie jest ważne także dla sieci (kontrola skończenie wielu poziomów plus mały ogon szeregu).
12. **Zupełność.** Cauchy'owskość w D daje dla każdego K_n równomierny warunek Cauchy'ego f_j|K_n. Zupełność metryczna Y zapewnia granicę punktową f:X→Y. Dla dowolnego η>0 wybór 0<ε<min(1,η) i wspólnego j_0, a następnie k→∞ w nierówności d(f_j(x),f_k(x))<ε, daje d(f_j(x),f(x))≤ε<η dla wszystkich x∈K_n jednocześnie. Stąd zbieżność jednostajna na każdym K_n. Ponieważ wnętrza K_n pokrywają X, f jest ciągła w otoczeniu każdego punktu i należy do C(X,Y); wreszcie D(f_j,f)→0. Nie wymaga się zupełności X ani jego metryzowalności.
13. **Nieprzeliczalny dyskretny X.** Zwarte podzbiory są skończone, więc C_k(X,R)=R^X z topologią produktową. Każde bazowe otoczenie zera ogranicza tylko skończenie wiele współrzędnych. Dla hipotetycznej przeliczalnej bazy otoczeń łączny zbiór kontrolowanych współrzędnych byłby przeliczalny; pozostałe x_0 prowadzi do otoczenia, którego nie zawiera żaden element bazy. Przestrzeń nie spełnia pierwszego aksjomatu przeliczalności, w szczególności nie jest metryzowalna.
14. **Terminologia, etykiety, testy.** Brak niedozwolonych terminów „zwartościowanie” i „zbieżność zwarta”; używano „zbieżność jednostajna na zbiorach zwartych”, „ciąg”, „sieć” i pełnych sformułowań aksjomatów przeliczalności. Weryfikacja testem ch18 sprawdza 29 topologii na zbiorze trzyelementowym, 82 odwzorowania do dyskretnego zbioru dwuelementowego, 19683 trójki funkcji w skończonym modelu ważonej metryki, modele uciekających górek, etykiety i zamknięcie odsyłaczy.

## Sprawdzenie techniczne

Treść LaTeX i plik testu **nie zostały zmienione w iteracji 03**. Weryfikacja dotyczy dokładnie wersji, która przeszła workflow [45016403410](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45016403410): completed/success, w tym test rozdziału 18, kompilację pełnej książki, samodzielnego rozdziału 18 oraz kontrolę logów.

Oryginalny artefakt 14752340712 ma samodzielny plik general_topology_ch18.pdf: **5 stron A4**. Ponownie sprawdzono istnienie i metadane PDF, obejrzano zestawienie wszystkich pięciu stron i potwierdzono czytelność dowodów i brak nachodzących elementów. Logi general_topology.log i general_topology_ch18.log nie zawierają Overfull, Underfull, Missing character, LaTeX Warning, Undefined control sequence ani Fatal error. Po dodaniu wyłącznie raportu i aktualizacji planu nie zachodzi potrzeba ponownej kompilacji niezmienionego źródła.

## Werdykt audytu 03

| Kryterium | Wynik |
| --- | --- |
| Topologia zwarto-otwarta i jednostajna na zbiorach zwartych | PASS |
| Ciągłość ewaluacji i prawo wykładnicze | PASS |
| Kontrprzykłady i warunki brzegowe | PASS |
| Metryzacja i zupełność przestrzeni odwzorowań | PASS |
| Terminologia, założenia, etykiety i odsyłacze | PASS |
| Testy, pełna książka i samodzielny PDF | PASS |
| Poprawki konieczne w iteracji 03 | **BRAK** |
| Decyzja | **ROZDZIAŁ 18 STABILNY — audyt 03 zamknięty** |

Po audytach 01–03 rozdział 18 spełnia przyjęte kryteria stabilizacji. Następny rozdział: 19 — przestrzenie polskie i zbiory borelowskie.
