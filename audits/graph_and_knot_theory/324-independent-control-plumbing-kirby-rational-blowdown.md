# GT — audyt kontrolny 324

GT23: sprawdzono dowody homologii brzegu oraz wyznacznika i formy splecenia D_n. Uzupełniono rozróżnienie dwóch klas izometrii dla parzystego n: forma alternująca dla n=0 mod 4, diagonalna z wpisami 1/2 dla n=2 mod 4. Commit bd78cae4867d0aed52b88010b6cbfec55c051e83.
GT24: sprawdzono kongruencję Schura dla gwiazdy, bezwładność, pierwotny generator całkowitego jądra i identyfikację H2 brzegu. Bez nowych luk w sprawdzonych dowodach; źródło bez zmian.
GT25: sprawdzono całkowitą kongruencję przy kontrakcji +/-1 i zachowanie formy splecenia dla nieosobliwych macierzy. Dodano jawny izomorfizm kokernów [(x,t)] -> [x-epsilon*t*ell], działający również w przypadku osobliwym. Commit 18ab2923d5dbe1238897274aac9e57ce534221cf.
GT26: sprawdzono ciąg homologii pary wymiernej kuli i zmiany niezmienników wymiernych. Dodano stwierdzenie z pełnym dowodem Mayera–Vietorisa: H1(X)=H1(W)/<a>, H1(X_(p))=H1(W)/<pa>, naturalna surjekcja ma cykliczne jądro o rzędzie dzielącym p. Commit 1d17a2d24c2549bf98012baf723f349626cb9a15.
GT27: sprawdzono formę splecenia i metabolizer, rachunek niezmienników i warunek normalnego generowania. Przeniesiono wzór całkowitej H1 na C_pq, z odsyłaczem do GT26 i ostrzeżeniem, że H1=0 nie oznacza prostej spójności. Commity a086186438475650b0a5ddef421ec9a4212de2d7 i eee79a89c7aee6dd7398f540e1e1da82714b9ea6.

Walidacja: 942/942 przypadków ilorazu dla H1(W)=Z/nZ, 1<=n<=30, 2<=p<=12, wszystkich a z p²a=0 (enumeracja orbit relacji (a,-1), kontrola mapy oraz rzędu jądra); 49/49 kontroli klasy formy dla parzystego n od 4 do 100. 4/4 cele odsyłaczy i nowa etykieta unikatowe w sprawdzonych plikach. Zagnieżdżenie środowisk LaTeX poprawne w czterech zmienionych rozdziałach; potwierdzono ponownym odczytem bloby. Testy są kontrolami wybranych modeli algebraicznych, nie dowodami topologicznymi.

CI pełne 45986880611, algorytmy 45986880460, aplikacja 45986880347, terminologia 45986880382 — queued przy odczycie. Brak wizualnego odbioru PDF i ponownego odbioru wszystkich twierdzeń GT23–27. Następny etap: GT28–34 (Seiberg–Witten, Park, chirurgia wzdłuż węzła). Stabilizacja pozostaje otwarta.
