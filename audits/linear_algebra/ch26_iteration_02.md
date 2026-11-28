# Algebra liniowa — rozdział 26, audyt II (matematyczny, niezależny)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/26-uogolnione-twierdzenia-riccatiego.tex`.  
**Blob końcowego tekstu do kontroli:** `8ae57f3905cf88bc24d94fe1fd8d89f107a353e9`.

## Warunki twierdzeń

- Macierze mają wymiary A∈M_n(C), B∈M_{n×m}(C), Q=Q*≥0, R=R*>0; Q=C*C z C=Q^{1/2}. Konstrukcja C oraz równość ker C=ker Q są poprawne także dla Q=0 i Q osobliwej. Kryterium wykrywalności pary (C,A) zależy tylko od ker C, toteż jest niezależne od faktoryzacji Q.
- Założenia „para (A,B) stabilizowalna” i „para (C,A) wykrywalna” przyjęto osobno dla czasu ciągłego i dyskretnego. Nie korzysta się z założenia o stabilności A. Wskazano, że Q=0 i niestabilna A wyklucza wykrywalność, nawet jeśli para (A,B) jest sterowalna.
- Dla K_0 stabilizującego macierz D_0=A-BK_0 oraz H=Q+K_0*R K_0≥0, zbieżność sumy/calki daje W_d/W_c≥0 i jednolite ograniczenie kosztu. Słabsza wersja niż W>0 jest konieczna; w dowodzie nie wyprowadzano stabilności D_0 z półokreślonego równania Lapunowa, ponieważ stabilność D_0 jest założeniem.

## DARE

1. Dla każdego N koszt etapu jest nieujemny, M_N=R+B*P_NB>0, a minimalizator u=−M_N^{−1}B*P_NAx jest jedyny. Po uzupełnieniu kwadratu otrzymuje się dokładnie podaną rekurencję P_N.
2. P_N jest niemalejąca i ograniczona przez W_d. Granica P istnieje poprzez polaryzację form kwadratowych; 0≤P≤W_d, M_N^{-1}→M^{-1}, więc P spełnia DARE.
3. Po zdefiniowaniu K=M^{-1}B*PA i D=A−BK tożsamość `P−D*PD=Q+K*RK` jest algebraicznie poprawna: w jej rozwinięciu dwa ujemne wyrazy mieszane zostają skompensowane przez K*MK.
4. Jeśli Dv=λv i |λ|≥1, to `(1−|λ|²)v*Pv=||Cv||²+(Kv)*R(Kv)`; z P≥0 i R>0 obie strony muszą zniknąć, skąd Cv=Kv=0 i Av=λv. Jest to dokładna sprzeczność z kryterium PBH wykrywalności.
5. Dla dwóch stabilizujących hermitowskich rozwiązań P_1,P_2 z odwracalnymi M_i poprawna jest tożsamość `P_1−P_2=(A−BK_1)*(P_1−P_2)(A−BK_2)`. Iteracja i zanik potęg obydwu zamkniętych macierzy daje równość. W dowodzie nie przemyca się dodatkowego założenia M_2>0.
6. Dowolne rozwiązanie P_2≥0 jest automatycznie stabilizujące na podstawie tego samego argumentu PBH; stąd jedyność w klasie półokreślonej.

## CARE i czas ciągły

1. Lokalna jednoznaczność równania S'=F(S) jest następstwem lokalnej lipschitzowskości. Sprzężenie hermitowskie i warunek początkowy zapewniają S=S*. Różniczkując x*S(T−t)x, otrzymujemy poprawny znak przy −S'; po użyciu ODE wynik jest dokładnym kwadratem (u+R^{−1}B*Sx)*R(u+R^{−1}B*Sx).
2. Sprzężenie zależne od czasu osiąga minimalny koszt na skończonym horyzoncie; Q≥0 zapewnia S(T)≥0. Porównanie z zerowym sterowaniem na każdym skończonym przedziale daje lokalne ograniczenie S i wyklucza wybuch ODE. Porównanie przez ograniczenie sterowania z dłuższego horyzontu zapewnia monotoniczność; stabilizujące K_0 daje ograniczenie globalne W_c.
3. Z S(T)↑P oraz S'=F(S), ciągłości F i zbieżności S wynika F(P)=0. Gdyby niezerowa składowa F(P) istniała, odpowiednia składowa pochodnej S'(T) nie mogłaby całkować się do ograniczonej zbieżnej S(T).
4. Zamknięte równanie `D*P+PD=−(Q+K*RK)` i wektor własny D o Re λ≥0 dawałyby `2Re λ v*Pv=−||Cv||²−(Kv)*R(Kv)`, co wymusza Cv=Kv=0 i Av=λv, wbrew wykrywalności. Dokładnie tu używa się wykrywalności, nie dodatniości Q.
5. Porównanie dwóch stabilizujących hermitowskich rozwiązań przez całki kosztowe z każdym z dwóch sprzężeń daje P_1≥P_2 i P_2≥P_1 bez założenia znaków drugiej macierzy. Każde P_2≥0 jest stabilizujące na mocy PBH.

## Nieskończony horyzont

- Wartości `u∈ell²` i `Cx∈ell²` wynikają ze skończonego dyskretnego kosztu. Wykrywalność daje L z D=A−LC Schur; dla w_k=Bu_k+LCx_k mamy w∈ell². Rozkład splotu na skończony początek i ogon ograniczony przez `M /sqrt(1−r²) ||w_tail||_2` prowadzi do x_k→0.
- W czasie ciągłym wykrywalność daje D=A−LC Hurwitz, a w=Bu+LCx∈L². Oszacowanie ogona splotu przez `M/sqrt(2α)||w_tail||_{L²}` i zanik części początkowej przy t→∞ uzasadniają x(t)→0. Nie zakłada się fałszywie, że sama półokreślona Q daje x∈L².
- W obu rodzajach czasu warunek brzegowy x(T)*Px(T)→0 jest udowodniony, a nie pomijany. Ścisłość R>0 (i M>0 w DARE) daje jedyność optymalnego sterowania; w czasie ciągłym jest ona rozumiana prawie wszędzie.

## Kontrola przykładów

- Skalarny DARE: A=2, B=1, Q=4/5, R=1, P=4, K=8/5, D=2/5; drugi pierwiastek −1/5 i D=5/2. CARE: A=1, B=1, Q=3, R=1, P=3, K=3, D=−2; drugi pierwiastek −1 i D=2.
- Półokreślone Q i osobliwe P: w DARE A=diag(2,1/2), B=e1, Q=diag(4/5,0), P=diag(4,0) i D=diag(2/5,1/2); w CARE A=diag(1,−2), B=e1, Q=diag(3,0), P=diag(3,0) i D=diag(−2,−2). Oba przykłady spełniają dokładne tożsamości.
- Kontrprzykłady bez wykrywalności Q=0: monotoniczne P_N i S(T) pozostają zerowe, pomimo istnienia innych stabilizujących algebraicznych pierwiastków. Bez stabilizowalności B=0 przy niestabilnym A nie istnieje nieujemne rozwiązanie ARE.

## Wynik

**Pierwsza niezależna kontrola merytoryczna czysta; bez zmian źródła.** Nowy test `tools/test_linear_algebra_general_riccati.py` przeszedł w części testowej CI, ale pełna walidacja składu i samodzielnego PDF jeszcze w toku; raport nie uznaje rozdziału za stabilny.
