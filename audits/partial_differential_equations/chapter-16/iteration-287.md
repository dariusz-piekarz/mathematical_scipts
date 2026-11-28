# RRC 16 — iteracja 287: trzecia lektura 043–052

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano pełny dowód lem:pde16-schauder-apriori.

| Kryterium | Wynik kontroli |
|---|---|
| 043 | Normy skalowane z ustaloną skalą rho również na podzbiorach. Reguła iloczynu i kontrola kontrakcji przez stałe wymiarowe. Poprawne. |
| 044 | Transformacja x=x0+rho Sz i w(z)=w(x0+rho Sz), S=A0^{1/2}: Hessian z czynnikiem rho², ślad rho² A0:D²w; nośnik i obraz kuli zawarte w B_{lambda^{-1/2}}. Poprawne. |
| 045 | Tożsamość Gamma*F=w dla F=-Delta w po transformacji przez wygładzenie w C² i lokalną całkowalność Gamma. Zerowe przedłużenie G zachowuje półnormę dzięki przecięciu odcinka ze sferą. Transformacja półnormy F daje czynnik rho^{2+alpha}Lambda^{alpha/2}; odwrotna transformacja Hessianu i odległości daje rho^{-2}, rho^{-alpha} oraz kontrolę przez lambda. Zastosowanie lematu Newtona na kuli o ustalonym promieniu usuwa zależność stałej od rho. Poprawne. |
| 046 | Przesunięcie x_t do wnętrza B_1, odcinek długości t/2, reszta całkowa daje 4Y/t+(t/4)H. Różnica gradientów wzdłuż odcinka x_t–x nie przekracza tH, stąd G<=C_d(t^{-1}Y+tH). Poprawne. |
| 047 | Półnorma gradientu z minimum H|x-y| i 2G, półnorma funkcji analogicznie. Ważona nierówność Younga i wybór kolejno tau=epsilon/2 oraz t dają mały współczynnik wyłącznie przy supremum Hessianu. Skalowanie do dowolnej kuli poprawne. |
| 048 | Odcięcie z konstrukcji lokalizacyjnej, kontrola pochodnych do trzeciego rzędu i skalowanych półnorm do drugiego rzędu przez średnicę kuli. Zerowe przedłużenie w=eta v jest C^{2,alpha} dzięki znikaniu w otoczeniu sfery i kontroli par przecinających brzeg. Poprawne. |
| 049 | Tożsamość A0:D²w po rozwinięciu iloczynu: poprawne znaki członów b,c, symetria A w członie mieszanym. Norma A-A0 ograniczona przez 2rho^alpha[A]_alpha. Czynniki przy normach gradientu i funkcji po przemnożeniu przez rho² są odpowiednio O(rho), O(1); niższe rzędy mieszczą się w tych ograniczeniach dla rho<=1. Poprawne. |
| 050 | Pochłonięcie X przy C1rho0^alpha[A]_alpha<=1/2, następnie interpolacja z parametrem epsilon/(2C2). Otrzymane oszacowanie na B_{rho/2} ma mały składnik rho²||D²v||_infty, bez półnormy Hessianu po prawej. Poprawne. |
| 051 | delta(x)=(1/8)min(rho0,dist(x,brzeg)) jest 1/8-Lipschitzowska; kula o promieniu 2delta leży wewnątrz B_R i delta(y)>=3delta(x)/4. M skończona z hipotezy a priori. Podstawienie rho=2delta i podzielenie przez 4 daje współczynnik epsilon(4/3)^2=2/9 dla epsilon=1/8, umożliwiający pochłonięcie. Poprawne. |
| 052 | Wewnętrzne dolne ograniczenie delta_* > 0, kontrola supremum Hessianu przez delta_*^{-2}, kontrola półnormy dla par bliskich przez lokalne oszacowanie z rho>=2delta_*, dla dalekich przez 2delta_*^{-alpha} razy supremum. Gradient z interpolacji, przejście na domknięcie przez ciągłość. Pełne oszacowanie zależy jedynie od deklarowanych danych. Poprawne. |

Nie wykryto nowych błędów ani luk wymagających zmiany źródła. Ósma kolejna czysta iteracja (280–287). Trzecia lektura 52/64. PDF i CI nadal niepotwierdzone. Następna iteracja 288: kryteria 053–058 — komutator i regularyzacja w twierdzeniu Schaudera.
