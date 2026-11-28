# GT — audyt kontrolny 325

GT28: sprawdzono rachunek indeksu Diraca, operatora samodualnego, parzystość indeksu i związek z charakterystyką Eulera; bez nowych luk w sprawdzonych fragmentach.
GT29: sprawdzono równanie ściany, charakterystykę obrazu d+ i torus klas redukowalnych; bez zmian.
GT30: sprawdzono dokładność i macierz symbolu oraz rachunek pełnej krzywizny. Rozróżniono normę współrzędnych od normy form samodualnych, podano macierz w bazach ortonormalnych, jej wartości singularne i ostre dwustronne oszacowanie symbolu. Commit 8c5457a2dfdb251e7da385dda602096bd3208713.
GT31: sprawdzono wzór odwrotności Q7 i argument z formą splecenia. Dodano niezależny dowód przez eliminację relacji meridianów: mu_i=(8i+1)mu_0 i 49mu_0=0. Commit 499bab9326c69e64f1f337c3c55a0a83c699ca35.
GT32: sprawdzono rozkład parowania na dopełnieniu i konfiguracji, macierz w bazie sprzężonej i zgodność klasy kanonicznej przy założonej identyfikacji symplektycznej; bez nowych luk w tym dowodzie.
GT33: sprawdzono mapy homologii brzegu, rozszczepienie ciągów Mayera–Vietorisa, sygnaturę, rachunek klas podstawowych i ich wymiarów; bez zmian.
GT34: sprawdzono bilans wymierny i indeksy krat w przypadku H1(A)=0. Dodano związek z GT26: naturalna surjekcja H1 po kontrakcji na H1 przed kontrakcją ma jądro <a>/<pa>. Gdy H1(X)=0, grupa po kontrakcji jest cykliczna o rzędzie dzielącym p; bilans wymierny sam nie rozstrzyga zanikania torsji. Commit dfb25fdac7069f201167cd734806f8bbc27a6c5d.

Walidacja: 2401/2401 całkowitych wektorów xi z [-3,3]^4, dokładny rachunek iloczynu macierzy wierszowej po usunięciu mianowników; 6/6 mnożników meridianów C7, kontrola relacji i względnej pierwszości z 49; 3/3 cele odsyłaczy występują dokładnie raz w sprawdzonych plikach. Zagnieżdżenie środowisk LaTeX poprawne w trzech zmienionych rozdziałach, bloby potwierdzone ponownym odczytem. Kontrole algebraiczne nie zastępują dowodów analitycznych ani geometrycznych.

CI pełne 45987521620, algorytmy 45987521594, aplikacja 45987521616, terminologia 45987521629 — queued przy odczycie. Brak wizualnego odbioru PDF; nie jest to ponowny odbiór wszystkich twierdzeń GT28–34. Następny etap: GT37–43, audyt algorytmów grafowych, kombinatoryki i ekspanderów; potem kontrola stabilizacyjna zmienionych fragmentów i CI.
