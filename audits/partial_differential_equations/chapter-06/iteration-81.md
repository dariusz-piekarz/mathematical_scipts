# PDE-06 — iteracja 81: druga lektura 6.5–6.6

Data: 2026-11-25. Źródło 4adf037b29fc0e09a95fb435557bde958b761d09, rejestr 6293e2798c2b66b9a7fd126670bea0988b76ba00, testy ccbb8b39902904365b1403df5eefa10ff40d2134. Druga kontrola semantyczna bez rozszerzania materiału.

| ID | Wynik | Uzasadnienie |
|---|---|---|
| PDE-06-022 | PASS | Wspólny zwarty nośnik daje zgodność danych na brzegu, także dla wszystkich pochodnych czasowych. Współczynniki w nieunormowanej bazie mają czynnik 2/L. |
| PDE-06-023 | PASS | Ciągłość u_t pozwala różniczkować całkę; oba składniki brzegowe znikają dzięki zerowaniu u i X_n. Znak równania modalnego i czynnik całkujący są poprawne; podstawienie t=0 daje g_n. |
| PDE-06-024 | PASS | Konstrukcja nie zakłada istnienia rozwiązania. Całkowanie przez części dowolną liczbę razy jest dozwolone dzięki wspólnemu nośnikowi, a stałe są jednostajne w czasie. Indukcja z równania modalnego kompensuje czynnik lambda_n przez wybór m+2. |
| PDE-06-025 | PASS | Pochodna przestrzenna rzędu r kosztuje n^r, wybór m>=r+2 daje sumowalną majorantę wszystkich mieszanych pochodnych. Zupełność i ciągłość identyfikują dane i wymuszenie. Jednoznaczność różnicy na 0<t<T wynika z zasady maksimum na cylindrach kończących się w T'<T, a w T przez ciągłość; także dla części rzeczywistej i urojonej. |
| PDE-06-026 | PASS | P_0 jest identycznością dla rozpatrywanych danych; jednostajna majoranta n^(-2) na całym trójkącie czasowym pozwala całkować szereg, także przy s=t. |
| PDE-06-027 | PASS | Dodatnie minimum i skończone maksimum ciągłej wagi dają równoważność norm i zupełność. p klasy C¹, dodatnie, q ciągłe i nieujemne; dopuszczone zespolone funkcje. |
| PDE-06-028 | PASS | Całkowanie przez części daje właściwy znak wyrazu brzegowego Lagrange'a. Energia nietrywialnej funkcji Dirichleta jest ściśle dodatnia, więc lambda jest rzeczywista i dodatnia. Dla dwóch różnych wartości własnych różnica lambda-mu mnoży ważony iloczyn skalarny. |
| PDE-06-029 | PASS | Układ v'=z/p, z'=qv ma ciągłe współczynniki. Energia wyklucza nietrywialne rozwiązanie z dwoma zerowymi końcami. Wrońskian C jest stały i C=p(L)v_1(L) niezerowy. Znak skoku pochodnej jądra daje dokładnie 1 po pomnożeniu przez -p(s). |
| PDE-06-030 | PASS | Cauchy–Schwarz daje L¹ względem nu i ograniczoność T ze stałą M. Interpolacja na siatce jest kombinacją wypukłą, błąd jednostajny dąży do zera, obrazy operatorów przybliżających są skończenie wymiarowe. Symetria rzeczywistego jądra i bezwzględna całkowalność uzasadniają Fubiniego i samosprzężoność. |
| PDE-06-031 | PASS | F=wf jest całkowalna; A,B absolutnie ciągłe. Składniki od ruchomej granicy znoszą się w y', ciągły reprezentant pochodnej daje C¹. Drugi rachunek daje (py')'=qy-F z właściwym znakiem. Dla ciągłego F otrzymujemy py' klasy C¹, a następnie y klasy C². |
| PDE-06-032 | PASS | Całkowanie przez części z py' absolutnie ciągłą jest dozwolone. Zerowa energia wymusza y=0 i f=0, zatem T jest ściśle dodatni i iniektywny. Twierdzenie spektralne dla zwartego operatora samosprzężonego daje pełną bazę; nieskończony wymiar i skończone krotności wymuszają nieskończoność dodatnich mu_n dążących do zera. Sprzężenie komutuje z T, więc można wybrać rzeczywistą bazę. |
| PDE-06-033 | PASS | Reprezentant y_n=Ty_n/mu_n ma warunki Dirichleta i regularność C² po użyciu ciągłego wymuszenia. Równanie różniczkowe daje lambda=1/mu; odwrotnie jednoznaczność zagadnienia dla ciągłego wymuszenia daje Ty=y/lambda. Jednoznaczność liniowego ODE z y(0)=0 i ustaloną pochodną początkową daje prostotę; zupełność przechodzi z bazy T. |

Nie wykryto nowych błędów matematycznych ani istotnych luk dowodowych w 6.5–6.6. Nie zmieniono źródła, rejestru, testów ani workflow. Potwierdzono treść thm:pde4-max w rozdziale 04 i zgodność zastosowania do różnicy rozwiązań. Zweryfikowano ponownie status przebiegu 45572681202, job 139062917083: completed/success, wszystkie kroki zaliczone. Wynik 10/10 testów, kompilacji i diagnostyki dotyczy niezmienionych wersji źródła, rejestru i testów. Nie uruchomiono nowych testów, nie kompilowano całego tomu, nie wykonano kolejnych oględzin PDF ani formalizacji Lean.

Druga lektura: 6/9 sekcji, 33/42 kryteriów łącznie. Następna iteracja 82: 6.7–6.9, geometria widma, zagadnienie odwrotne i podsumowanie. Następnie niezależny audyt kontrolny przed decyzją o stabilizacji rozdziału.
