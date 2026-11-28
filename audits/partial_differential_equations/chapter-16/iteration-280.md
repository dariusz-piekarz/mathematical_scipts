# RRC 16 — iteracja 280: druga lektura 043–052

Źródło: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Ponownie odczytano pełny dowód lem:pde16-schauder-apriori oraz jego zależności: lem:pde16-localization, thm:pde16-variable, def:pde16-holder, lem:pde16-newton-holder i lem:pde7-convolution-derivatives.

| Kryterium | Wynik kontroli |
|---|---|
| 043 | Normy skalowane: ta sama skala rho po ograniczeniu do mniejszej kuli, reguła iloczynu i kontrakcje skończenie wymiarowe. Poprawne. |
| 044 | Transformacja x=x0+rho S z: Hessian przekształca się przez rho² S^T i S, ślad jest rho² A0:D²w; kontrola obrazu nośnika promieniem lambda^{-1/2}. Poprawne. |
| 045 | Tożsamość Gamma*(-Delta w)=w przez wygładzanie w C² o wspólnym zwartym nośniku; lokalna całkowalność Gamma. Zerowe przedłużenie G zachowuje półnormę dzięki przecięciu odcinka ze sferą. Zmiana skali i normy przez ||S||<=sqrt(Lambda), ||S^{-1}||<=lambda^{-1/2}; lemat Newtona na kuli o ustalonym promieniu daje stałą niezależną od rho. Poprawne. |
| 046 | Przesunięcie x_t=(1-t)x do wnętrza, B_{t/2}(x_t) w B_1, wzór Taylora daje 4Y/t+(t/4)H dla każdej składowej; różnica gradientów <=tH. Poprawne. |
| 047 | Półnormy z minimum oszacowań Lipschitzowskich i supremum, Young z parametrem tau=epsilon/2, następnie wybór t; mały składnik zawiera wyłącznie supremum Hessianu. Skalowanie do B_rho zgodne dla wszystkich składników. Poprawne. |
| 048 | Odcięcie z lematu lokalizacyjnego daje także pochodną rzędu trzy przez różniczkowanie splotu; z wypukłości i średnicy 2rho wynikają skalowane półnormy do rzędu dwa. Zerowe przedłużenie eta v zachowuje klasę C^{2,alpha}. Poprawne. |
| 049 | Tożsamość A0:D²w: sprawdzono znaki b,c, symetrię A, oba składniki pochodnych odcięcia, normę A-A0 <=2rho^alpha[A]_alpha i jednolite ograniczenia współczynników dla rho<=1. Poprawne. |
| 050 | Pochłonięcie X=rho²|D²w|_{alpha,rho} przy C1rho0^alpha[A]_alpha<=1/2; po interpolacji parametr zmniejszony przez 2C2. Stałe niezależne od środka, promienia i v. Poprawne. |
| 051 | delta=(1/8)min(rho0,dist do brzegu) jest 1/8-Lipschitzowska; na B_{2delta(x)} delta(y)>=3delta(x)/4. M jest skończona z hipotezy a priori. Po podzieleniu przez 4 współczynnik epsilon(4/3)^2 przy M dla epsilon=1/8 wynosi 2/9<1/2. Pochłonięcie poprawne. |
| 052 | Na B_r delta>=delta_*>0, kontrola supremum Hessianu, ponowne lokalne oszacowanie półnormy na B_{delta(x)} dla par bliskich, dla dalekich kontrola przez supremum; gradient z interpolacji, domknięcie przez ciągłość. Poprawne. |

Nie wykryto błędów ani luk wymagających zmiany źródła w sprawdzonym zakresie. Rozdział pozostaje na 1900 wierszach i 30 etykietach. Druga lektura 52/64, z wcześniejszymi poprawkami w iteracjach 276–279. PDF i CI nadal niepotwierdzone. Następna iteracja 281: 053–058 — komutator i regularyzacja w twierdzeniu Schaudera.
