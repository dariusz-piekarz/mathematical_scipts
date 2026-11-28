# RRC 16 — iteracja 285: trzecia lektura 025–032

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano pełne dowody lem:pde16-localization, lem:pde16-gradinterp, thm:pde16-variable oraz uwagę o postaci dywergencyjnej. Zestawiono z rzeczywistymi tezami lem:pde9-compact-product, thm:pde9-mollify, thm:pde10-domain-embed, thm:pde15-h2 i thm:pde15-bootstrap.

| Kryterium | Wynik kontroli |
|---|---|
| 025 | Globalne oszacowanie D²v przez Delta v dla testów wynika z Gamma*(-Delta v)=v i oszacowania Calderóna–Zygmunda. Przejście do W^{2,p} o zwartym nośniku przez wygładzanie w obu normach; lokalna zbieżność wystarcza z uwagi na wspólny zwarty nośnik. Poprawne. |
| 026 | Odcięcie eta=chi_{B_{(r+R)/2}}*rho_sigma ze skalą sigma=(R-r)/4: jest równe 1 na otoczeniu domknięcia B_r, nośnik zawarty w B_R; normy pochodnych rzędu k kontrolowane przez (R-r)^(-k). Zerowe przedłużenie eta u i wzór na laplasjan bez składników brzegowych zgodne z lematem RRC 09. Poprawne. |
| 027 | Dwukrotne całkowanie na odcinku x+[0,h]e_j, waga h-t, Minkowski i translacja do B_{r+h}; całka wagi h²/2, zsumowanie po j daje 2d/h i dh/2. Wygładzanie na B_{R'} z r+h<R'<R i dobór h=min((R-r)/2,2epsilon/d) poprawne. |
| 028 | Zamiana zmiennych x=x_0+Sz, S=A_0^{1/2}, normy S i S^{-1} kontrolowane wspólnymi stałymi eliptyczności. Hessian przekształca się przez S^T i S, ślad jest A_0:D²v, czynniki |det S|^{1/p} znoszą się. Stała C_0=C_{d,p}/lambda niezależna od środka. Poprawne. |
| 029 | Wspólny promień L z jednostajnej ciągłości A na domknięciu V i dodatniego odstępu domknięcia U od dopełnienia V. Pochłonięcie różnicy przez normę Frobeniusa <=1/(2C_0); reguła Leibniza z symetrią A i pochodnymi odcięcia, stała niezależna od promieni s,t. Poprawne. |
| 030 | Promień pośredni m=(s+t)/2 i krok h=kappa(t-s)<t-m. Współczynnik C_1 d kappa przy H(t), współczynnik C_1(4+4d/kappa) przy (t-s)^(-2)Y. Wybór kappa zapewnia theta=1/8; s_n=L(1-2^(-n-1)), odwrotność kwadratu odstępu 16 L^{-2}4^n. Iteracja i granica dzięki H(L)<infty; 4theta=1/2. Poprawne. |
| 031 | Kontrola gradientu na B_{L/4} z h=L/8, pełna norma W^{2,p}, skończone pokrycie domknięcia U przez kule o wspólnym promieniu. Sumowanie całek daje stałą zależną od geometrii U,V i danych współczynników, nie od u,f. Poprawne. |
| 032 | Rozwinięcie postaci dywergencyjnej po uzyskaniu H² w RRC 15: poprawny znak f i członu (partial_i a_ij)partial_j u. Zanurzenia gradientu w L^q: wszystkie skończone q>=2 dla d=2, 2<=q<=2d/(d-2) dla d>2, zgodne z RRC 10. Uwaga nie utożsamia całkowalności prawej strony z uzyskaniem W^{2,p}; symetryzacja głównej macierzy dzięki symetrii Hessianu prawie wszędzie poprawna. |

Nie wykryto nowych błędów ani luk wymagających zmiany źródła. Szósta kolejna czysta iteracja (280–285). Trzecia lektura 32/64. PDF i CI nadal niepotwierdzone. Następna iteracja 286: 033–042 — przestrzenie Höldera i potencjał Newtona.
