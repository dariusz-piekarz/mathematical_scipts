# AA-47 — audyt II: niezależna kontrola dowodów, kompletności lokalnej i testów

**Data:** 23 listopada 2026 r.
**Status:** AUDYT W TOKU, **NIE STABILNY**, do końcowego CI i PDF.
**Źródło:** chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex.
**Zakres:** docs/pl/zakres_aa47_risch_kovacic.md.

## 1. Niezależne wyprowadzenie testów matematycznych

### 1.1. Całkowanie wymierne i redukcja Hermite'a

Dla f=P+∑_a∑_{k≥1} b_{a,k}(x-a)^{-k} wystarczy odjąć pochodną wielomianu i pochodne -b_{a,k}(x-a)^{1-k}/(k-1) (k≥2). Pozostała część to ∑_a b_{a,1}/(x-a). Pochodna funkcji wymiernej ma zawsze zerową resztę w każdym skończonym punkcie: jedyny potencjalny wkład do (x-a)^{-1} pochodzi z różniczkowania stałej, które jest zerowe. Odwrotnie, brak residuów usuwa wszystkie człony logarytmiczne, co daje wymierną funkcję pierwotną. Nie należy mylić istnienia pierwotnej wymiernej z elementarną: elementarna zawsze istnieje nad C dla f wymiernego.

### 1.2. Rothstein–Trager, wypadkowa i NWD

Jeżeli B jest unormowany i bez pierwiastków wielokrotnych, to w każdym jego pierwiastku a zachodzi B'(a)≠0 i reszta A/B jest c_a=A(a)/B'(a). Wypadkowa T(z)=Res_x(B,A-zB') wynosi ∏_{B(a)=0}(A(a)-zB'(a)); rzeczywiste wartości pierwiastków to dokładnie c_a (z krotnościami). P_c=gcd(B,A-cB') ma jako pierwiastki dokładnie te a, dla których c_a=c. Wtedy Σ_c cP'_c/P_c ma te same części główne co A/B. Obie funkcje są właściwe, więc ich różnica to zerowy wielomian. Nie jest potrzebny rozkład B na czynniki liniowe przed obliczeniem T, ale trzeba rozwiązać pomocniczy problem rozkładu T lub skutecznie obsłużyć jego pierwiastki algebraiczne.

Dwa niezależne modele: A=1, B=x²+1 daje T=1+4z² i reszty ±i/2; A=x+1, B=x(x-1) daje T=(1+z)(2-z), reszty -1 oraz 2 i rozkład (x+1)/(x(x-1))=-1/x+2/(x-1).

### 1.3. Równanie r'+hr=s przy h∈C[x]

W punkcie a, jeśli r ma biegun j≥1, r' ma rząd j+1 i niezerowy współczynnik -j b_{-j}, a hr co najwyżej j. Dlatego s ma dokładnie ten rząd; nie jest możliwe otrzymanie bieguna prostego. Nie ma też biegunów r w punktach regularności s. Dla każdego bieguna s rzędu m≥2 współczynniki r od r_{-(m-1)} do r_{-1} są jednoznacznie wyliczane kolejno z potęg z^{-m},...,z^{-2}; pozostałe równanie przy z^{-1} stanowi niezależną przeszkodę. Po jej przejściu cała reszta S=s-R'-hR jest wielomianem.

Dla wielomianu P i h dodatniego stopnia d, o ile P≠0, stopień P'+hP jest równy deg P+d, więc dla S≠0 konieczny jest deg P=deg S-d. Dla h=c≠0 stałego formuła P=∑_{k=0}^{deg S}(-1)^k S^{(k)}/c^{k+1} teleskopuje dokładnie. Obydwie gałęzie kończą się skończonym układem równań. W połączeniu z AA-45 to pełny algorytm decyzyjny *dla tej klasy*, nie dla wszystkich rozszerzeń elementarnych.

### 1.4. Normalna postać Kovacica

Podstawienie y=z exp(-1/2 ∫a) do y''+ay'+by=0 daje q=a'/2+a²/4-b. Po podstawieniu r=z'/z otrzymujemy Riccatiego r'+r²=q. Te dwie równoważności są wykazane przez różniczkowanie i nie korzystają z klasyfikacji grup algebraicznych.

### 1.5. Równanie Riccatiego dla q wielomianowego

Skończony biegun r dla r'+r²=q musi mieć rząd 1 i współczynnik 1: dla m≥2 wyraz r² jest wyższego rzędu niż r', a dla m=1 współczynnik z^{-2} daje c²-c=0 i c≠0. Stąd r=ω+P'/P, gdzie ω wielomian, P monic i bez powtarzających się pierwiastków.

Niech deg q=2d≥2. Na nieskończoności część wielomianowa r'+r² ma stopień 2 deg ω, więc q dodatniego stopnia nieparzystego wyklucza wymierne r. Dla parzystego stopnia dwa wybory wiodącego współczynnika ω wynikają z a_d²=q_{2d}; porównanie kolejnych współczynników stopni ≥d jednoznacznie wyznacza ω. Dla P monic stopnia n rozwinięcie P'/P=n/x+O(x^{-2}) daje przy x^{d-1} współczynnik 2a_d n. Dlatego n=[x^{d-1}](q-ω²-ω')/(2a_d), co musi być nieujemną liczbą całkowitą. Przy dopuszczalnym n podstawiamy P=x^n+∑_{j<n}p_j x^j do liniowego ODE P''+2ωP'+(ω'+ω²-q)P=0. Jeżeli P ma pierwiastek wielokrotny rzędu m≥2, w P'' pojawiłby się niekasowalny wyraz rzędu m−2, więc takie rozwiązanie nie występuje. Każdy pozytywny wynik daje dokładne rozwiązanie Riccatiego; każde racjonalne rozwiązanie zostało uwzględnione. Dla q=0 poprawną stałą odpowiedzią jest r=0.

**Ograniczenie:** test tej gałęzi nie dowodzi nieistnienia kwadratowego algebraicznego rozwiązania. Kontrprzykład q=x+5/(16x²), r=√x−1/(4x) ma r'+r²=q, chociaż wymiernego r nie ma. Klasyfikacja Kovacica i poprawność wszystkich jej gałęzi są wyraźnie oznaczone jako cytowany wynik, nie samodzielny dowód.

## 2. Rzeczywista poprawka po pierwszym CI

Pierwszy pełny przebieg CI dla integracji AA-47 (GitHub Actions #45159930396) zakończył się failure w ogólnym kroku „Run repository tool tests”. Przyczyną była nowa asercja dla q=0: funkcja testowa zwracała None, ponieważ w SymPy stopień wielomianu zerowego jest -∞. To przypadek brzegowy implementacji testowej. Poprawka: sprawdzenie q.is_zero przed rozgałęzieniem według stopnia i zwrócenie r=0. W tym samym commicie poprawiono dwa sformułowania językowe („imprymitywnej” i „numeryczne”). **Commit poprawki:** 5a0cc7b19fc2f6c5834e243b6c5271cf4d696a85.

## 3. Kryteria stabilizacji

Konieczne są: pełny drugi zielony przebieg ogólnych testów; oba zestawy testów AA-47 (11 na SymPy i 10 na fractions.Fraction), integralność 47 rozdziałów z osobnymi audytami AA-43–AA-47; kompilacja całego PDF i brak błędów/ostrzeżeń; oględziny każdej nowej strony. Nie wpisywać „STABILNY” bez tych danych. AA-48 nadal nie otwierać.
