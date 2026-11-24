# MA1-13 — trwałe kryteria regresyjne
Testy Python sprawdzają skończone tożsamości dokładną arytmetyką; dowody granic podlegają audytowi semantycznemu.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-13-001 | ma1:def:cesaro | Indeksowanie od zera, średnie sum częściowych, wagi trójkątne | semantyczna + Python |
| MA1-13-002 | ma1:lem:cesaro-means, ma1:cor:cesaro-regular | Podział na skończony początek i ogon, regularność | semantyczna |
| MA1-13-003 | ma1:ex:grandi-cesaro, ma1:ex:cesaro-fails | Obie klasy indeksów, granica 1/2, rozbieżność dla jedynek | semantyczna + Python |
| MA1-13-004 | ma1:thm:cesaro-term | a_n/n do zera, warunek niewystarczający | semantyczna |
| MA1-13-005 | ma1:def:abel-summation, ma1:lem:polynomial-geometric | Zbieżność dla każdego r w [0,1), r=0, suma geometryczna i jej kwadrat | semantyczna + Python |
| MA1-13-006 | ma1:lem:abel-weights | Wagi nieujemne, suma 1, zanik każdej ustalonej wagi, ograniczoność i ogon | semantyczna + Python |
| MA1-13-007 | ma1:thm:abel-regular, ma1:ex:grandi-abel | Uzasadniona zbieżność bezwzględna, sumowanie przez części, granica 1/2 | semantyczna + Python |
| MA1-13-008 | ma1:thm:cesaro-implies-abel | Liniowy wzrost b_n,s_n,a_n, dwukrotne sumowanie przez części i granica średniej ważonej | semantyczna + Python |
| MA1-13-009 | ma1:ex:abel-not-cesaro | Granice średnich 1/2 i 0, suma Abela 1/4 | semantyczna + Python |
| MA1-13-010 | ma1:thm:summability-linear-shift | Liniowość, oba kierunki przesunięcia, m=0 i r=0 | semantyczna + Python |
