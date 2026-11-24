# AA-66 — etap D, pierwszy audyt stabilizacyjny

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Rozdział utworzony w b903f58df6c9fb97992e7bf97aef35460a1612de, uściślony w a74ae25edab77b68c3592b9b18f8ea327d40ae6b, blob 6d89ca42f09cd0c43a1a0bd64c3594d60861a3e6. Integracja książki, katalogu i planu 4e226d5600ac5147eaf7edd42b895c54748a4d09.

Zakres: niezdegenerowanie formy śladu wiernej reprezentacji algebry półprostej, niezależność operatora Casimira od bazy i komutowanie z działaniem, kocykle i kobrzegi, pierwszy lemat Whiteheada, rozszczepianie rozszerzeń i twierdzenie Weyla nad dowolnym ciałem charakterystyki zero. Diagram korekty przekroju, dwa przykłady: rozkład End(K^n) na macierze skalarne i bezśladowe, nierozszczepialny moduł jednowymiarowej algebry abelowej.

Audyt matematyczny czterech dowodów:
1. Jądro formy śladu jest ideałem dzięki niezmienniczości, liniowe kryterium Cartana daje rozwiązalność jego obrazu, wierność daje rozwiązalność ideału. Nie użyto klasyfikacji reprezentacji.
2. Izomorfizm tensorowy oparty na niezdegenerowanej formie wysyła element Casimira na identyczność; niezmienniczość B daje skasowanie dwóch składników po działaniu dołączonym. Znak w tożsamości komutatora poprawny.
3. Dla nieprzywiedlnego M i działania trywialnego perfekcyjność daje f=0. Dla działania nietrywialnego rozkład na jądro i komutujący ideał półprosty pozwala zejść do wiernego działania. Kocykl na jądrze znika przez perfekcyjność jądra. Casimir dla formy śladu ma skalar dim(l)/dim(M), niezerowy w charakterystyce zero; nie przyjęto tego dla dowolnej formy. Wzór u=sum x_i f(y_i) daje z u=C_B f(z), z poprawnym znakiem. Przejście do modułu dowolnego przez indukcję po wymiarze, bez zakładania rozszczepialności; odjęcie kobrzegu podniesionego z ilorazu pozostawia kocykl o wartościach w podmodule.
4. Działanie na Hom(W,U) jest reprezentacją, defekt przekroju s ma wartości w U, lemat Whiteheada pozwala odjąć T, uzyskując homomorfizm s-T. Jego obraz dopełnia U. Rozszerzenie skalarów zachowuje półprostotę przez macierz formy Killinga, a zgodny układ liniowy dla rzutu ma rozwiązanie nad K dzięki eliminacji Gaussa. Indukcja po wymiarze daje sumę prostą modułów prostych; uwzględniono V=0. W przykładzie algebry abelowej obraz każdego przekroju nie jest niezmienniczy. Żaden z dowodów nie używa twierdzenia Weyla przed jego wykazaniem.

Regresje wykonane rzeczywiście w JS (BigInt, eliminacja całkowitoliczbowa):
- d40b73694d6584e3b3891cd1deea12cf2acb5bfe: 13 modułów L(m) sl2, 16 modułów sl2+sl2 (7 z nieczynnym ideałem), zgodność wymiarów Z^1 i B^1, suma wymiarów 189, 90 kontroli skalaru Casimira. PASS.
- c012d3a83a225efd3d978c6962f1788f6683173a: 27 modeli blokowych dla sl_n n=2..4 z naturalnymi, sprzężonymi i trywialnymi ilorazami; 2682 relacje komutatorowe, 2682 tożsamości kocyklu, 234 kontrole niezmienniczego przekroju, 261 kontroli rzutu i jego jądra, 228 niezerowych defektów, 298 kontroli śladu, 25 parametrów nierozszczepialnego przykładu. PASS. Są to regresje modeli, nie formalizacja Lean.

Zaktualizowano 12 testów przekrojowych na 66 rozdziałów. Pełny CI i oględziny PDF pozostają warunkami zamknięcia etapu D. P i AA-67 nieotwarte.
