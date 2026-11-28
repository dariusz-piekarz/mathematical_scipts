# RRC 15 — iteracja 261: trzecia lektura 025–036

Źródło b4952ce41cfeb61edb446c84bd59948940bed4f6 (1457 wierszy), bez zmian. Odczytano pełne sekcje Caccioppolego i bootstrapu, tezy RRC 09 o iloczynie i absolutnej ciągłości, RRC 10 o zanurzeniach oraz pełny dowód Caccioppolego w RRC 14.

| Kryterium | Wynik trzeciej lektury |
|---|---|
| 025 | r>0, ograniczoność operatorowa i eliptyczność, u-k spełnia to samo równanie z f, ponieważ operator nie ma członu zerowego rzędu — poprawne. |
| 026 | Jawne odcięcie radialne z RRC 14: zakres [0,1], nośnik w domkniętej kuli 3r/2 i gradient <=C0/r; test eta²(u-k) przez RRC 09, ciągłość obu stron — poprawne. |
| 027 | Rozwinięcie gradientu; oszacowania eliptyczne i Cauchy–Schwarz dają lambda X²<=FY+2Lambda C0 XY/r; symetria A zbędna — poprawne. |
| 028 | Young: FY<=r²F²/2+Y²/(2r²), człon mieszany <=lambda X²/2+2Lambda²C0²Y²/(lambda r²), po pochłonięciu dokładne współczynniki; wspólna stała C — poprawne. |
| 029 | Średnia minimalizuje Y² z rozkładu kwadratów w RRC 14; stała niezależna od k,r,x0 — poprawne. |
| 030 | Indukcja jednocześnie regularności i oszacowania, m=0 z H², przejście m-1 przez zagnieżdżenie założeń — poprawne. |
| 031 | Na ograniczonym W mnożnik a z W^{1,infty} należy do H¹, reguła iloczynu dla p=q=2 daje słabą pochodną, oba składniki w L² przez ograniczenia, norma H¹ kontrolowana — poprawne. |
| 032 | Dla |gamma|<m gradient pochodnej rzędu |gamma-beta| ma H¹ z H^{m+1}, pochodne współczynników W^{1,infty}; iteracja Leibniza z Pascalem bez użycia H^{m+2} — poprawne. |
| 033 | Zróżniczkowane równanie i dodatni znak div Q_alpha po przeniesieniu, |beta|>=1 zapewnia H^{|beta|} gradientu; oszacowanie Q w H¹ przez normy A,u — poprawne. |
| 034 | Norma dywergencji <=sqrt(d) normy macierzy pochodnych, F_alpha w L², zastosowanie H² do v_alpha, każdy wielowskaźnik rzędu m+2 rozkładalny na m i 2 — poprawne. |
| 035 | U<<W<<V, lokalne H² dla v_alpha i indukcja norm na W, skończona liczba wielowskaźników i oszacowanie niższych pochodnych, kontrola stałych — poprawne. |
| 036 | Dla d>=2 iteracja zanurzeń na relatywnie zwartej kuli dla wszystkich rzędów: 1/p zmniejsza się o 1/d, w krytycznym przypadku wybór d+1, następnie Morrey; d=1 absolutna ciągłość i podstawowe twierdzenie rachunku całkowego. Ciągłe reprezentanty jednoznaczne na otwartych przecięciach i klasyczne równanie — poprawne. |

Trzecia lektura 36/64, dotychczas bez nowych usterek w iteracjach 259–261. Nie zmieniano źródła. Kompilacja PDF i CI nieuruchamiane. Następna iteracja 262: III/037–043, spłaszczanie brzegu i słabe reguły łańcuchowe.
