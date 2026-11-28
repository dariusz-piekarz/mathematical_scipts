# AA-54 — audyt IV: niezmienniczość, hesjan, jakobian i osobliwości

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob a6942da66e2e9c7d6b60e38e54fac589022c0536, niezmieniony po audycie II.

## Wykonana niezależna weryfikacja niezmienniczości
Pierwsza próba w kontenerze z SymPy przekroczyła limit czasu; także druga próba w kontenerze nie zwróciła wyniku. Nie zaliczono ich jako wykonanych testów. Następnie wykonano niezależny kod JavaScript z BigInt, reprezentując liczby a+b sqrt(D)+i(c+d sqrt(D)) jako czwórki całkowite, D=2 lub 5. Macierze generatorów pomnożono przez 4, aby usunąć mianowniki. Dla formy jednorodnej P stopnia d sprawdzono P(4M(1,j))=4^d P(1,j) dla wszystkich j=0,...,d. Ponieważ różnica po dehomogenizacji ma stopień co najwyżej d, te d+1 różnych punktów wystarczają do wykazania tożsamości. Współczynniki hesjanu i jakobianu obliczono przez dokładne różniczkowanie tablic współczynników i ich sploty.
- 2T: f,g,t oraz h,i,j: 9 tożsamości, 87 podstawień.
- 2O: f²,g,ft oraz h,r: 6 tożsamości, 82 podstawienia.
- 2I: F,H,K oraz h,i,u: 9 tożsamości, 195 podstawień.
Wynik 24/24 tożsamości, 364/364 dokładnych podstawień. Kontrola bez arytmetyki zmiennoprzecinkowej.

## Kontrola matematyczna
Reguła łańcuchowa dla liniowego L daje D²P(v)=L^T D²P(Lv)L; wyznacznik jest zachowany, ponieważ det(L)=1. Dla jakobianu pary (P,Q) pojawia się jeden czynnik det(L), więc również jest zachowany. Rachunek stopni 12,20,30 jest poprawny. Dla E6 i E8 gradienty wymuszają X=Y=Z=0. Dla E7 po zniknięciu X mamy 3Y²+Z³=0 oraz 3YZ²=0; przypadki Y=0 i Z=0 prowadzą do początku. Wszystkie trzy równania zawierają początek i są gładkie poza nim na mocy kryterium jakobianowego dla hiperpowierzchni. Nie znaleziono nowej luki w ustalonym zakresie.

## Propozycja dalszego uzupełnienia (nie wprowadzono do rozdziału)
Algebry Jacobiego i liczby Milnora 6,7,8 są naturalnym krótkim przykładem łączącym rozdział z teorią osobliwości. Dla E6 i E8 bazy to Y^a Z^b, a=0,1 oraz b=0,...,2 lub 3. Dla E7 ideał pochodnych jest (X,3Y²+Z³,YZ²), skąd Z⁵ należy do ideału. W porządku leksykograficznym Y>Z baza Gröbnera w dwóch zmiennych składa się z Y²+Z³/3,YZ²,Z⁵ (S-wielomiany redukują się do zera), zatem normalne monomy to 1,Z,Z²,Z³,Z⁴,Y,YZ. To rachunek matematyczny, nie wykonany test SymPy. Ewentualne włączenie wymaga decyzji o zakresie.

## CI
Run 45350623875, job 138295845759, commit 9ad6e1d2c2134bd985118fb8df5625ceeeec8201: in_progress, conclusion brak, kroki {"success":68,"in_progress":1,"pending":48}. Nie wykonano oględzin PDF.

## Werdykt
Drugi czysty audyt matematyczny po II (2/2). Bez zmian źródła i workflow. AA-54 nadal W AUDYCIE do pełnego CI i oględzin PDF; AA-55 nieotwarty.
