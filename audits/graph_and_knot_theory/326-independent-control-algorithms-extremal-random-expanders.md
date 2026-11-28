# GT — audyt kontrolny 326

GT37: sprawdzono dowód kryteriów mostów i punktów artykulacji w multigrafach, rozróżnienie krawędzi równoległych i niezmiennik low. Bez nowych luk w sprawdzonym dowodzie.
GT38: sprawdzono kryterium zakończenia dwukierunkowej Dijkstry, inicjalizację s=t, przypadek pustej kolejki i podział najkrótszej ścieżki na fronty. Bez zmian.
GT39: sprawdzono certyfikat optymalności i jednoznaczności MSF oraz oszacowanie odporności. Dodano dowód ostrości: przy zaburzeniu o normie maksimum gamma/2 można wymusić drugi MSF, przy większym zaburzeniu można utracić optymalność T. Commit d12772c3bcef7b85e8ce010f1a16c4b435d65ffa.
GT40: sprawdzono ścisły wzrost odległości do ujścia po fazie Dinica i rachunek złożoności z current arc; bez zmian.
GT41: dotychczasowy dowód symetryzacyjny ustalał wartość ekstremalną, nie jednoznaczność wszystkich grafów ekstremalnych. Dodano osobny dowód jednoznaczności przez indukcję po r, rozkład na sąsiedztwo wierzchołka maksymalnego stopnia i jego dopełnienie, analizę równości oraz wyrównanie liczności części. Commit 221b281808c9b7a2e64fc39abca08dbfb934740c.
GT42: sprawdzono próg ustalonego podgrafu przez maksymalną gęstość, liczenie par iniekcji i oszacowanie wariancji; bez nowych luk.
GT43: sprawdzono ważone nierówności Cheegera, obcięcie części dodatniej, wzór współpowierzchniowy i mieszanie leniwego spaceru dla grafu nieregularnego; bez nowych luk w sprawdzonych fragmentach.

Walidacja: 135131/135131 dopuszczalnych par (graf prosty na 0..6 wierzchołkach, r od 1 do max(1,n)), w tym 144/144 przypadki równości Turána z kontrolą struktury i równowagi części. 1956/1956 jednoznacznych MST dla K4 i wag z {-1,0,1,2}: enumeracja wszystkich drzew i sprawdzenie ostrości zaburzenia gamma/2, z rachunkiem całkowitym po pomnożeniu wag przez dwa. 3/3 etykiety unikatowe w sprawdzonych źródłach; zagnieżdżenie środowisk LaTeX poprawne w obu zmienionych rozdziałach, bloby potwierdzone ponownym odczytem. Konflikt równoległego zapisu rozwiązano. Testy są kontrolami skończonych modeli, nie zastępują dowodów.

CI pełne 45987739543, algorytmy 45987739615, aplikacja 45987739557, terminologia 45987739560 — queued przy odczycie. Brak wizualnego odbioru PDF. Zakończono przebieg kontroli wybranych dowodów w rozdziałach GT01–34 i GT37–43 (318–326), nie pełny odbiór wszystkich twierdzeń. Następny etap: stabilizacja zmian z kontroli 319–326, kontrola odsyłaczy i struktury całej książki, stan CI.
