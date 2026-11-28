# RRC 16 — iteracja 278: druga lektura 025–032

Źródło przed 90aed7ea025d16024d4af738c3e3ebda8a1e642a (1855 wierszy), po 2706553196921128d41b9651f96828cead72654f (1871 wierszy), commit a3f6ba7926e7392294a1566c0d1b810288c1ee9e.

025–026: globalne oszacowanie dla zwartego nośnika, tożsamość splotu z laplasjanem testu, wygładzanie w W^{2,p}, konstrukcja odcięcia ze skalą (R-r)/4, reguła Leibniza i przedłużenie zerowe — poprawne. Zweryfikowano lemat RRC 07 o różniczkowaniu splotu i RRC 09 o odcięciach i wygładzaniu. Poprawiono terminologię „zwarty nośnik”.

027: rachunek całkowy na odcinku, Minkowski, translacja, całka z wagi h²/2, zbieżność wygładzeń w W^{2,p} na B_{R'}, dobór h — poprawne.

028–029: transformacja Hessianu przez pierwiastek A_0, ślad, wyznacznik i jego skrócenie, stała C_0=C_{d,p}/lambda, jednolity promień z ciągłości i odległości od brzegu, pochłonięcie różnicy współczynników, reguła Leibniza — poprawne. Jawnie ustalono wspólne stałe eliptyczności na domknięciu V i środek w domknięciu U przed rachunkiem.

030–031: ponownie sprawdzono współczynniki 4+4d/kappa, theta=1/8, s_n=L(1-2^(-n-1)), czynnik 16 oraz iloraz 4theta=1/2. Reszta zanika dzięki założonej regularności. Oszacowanie gradientu i skończone pokrycie — poprawne.

032: poprzednia uwaga nie dość precyzyjnie opisywała zakres kontroli gradientu z H². Dodano rzeczywisty zakres zanurzeń z thm:pde10-domain-embed: d=2 wszystkie skończone q>=2; d>2 q<=2d/(d-2). W tych zakresach prawa strona po rozwinięciu dywergencji należy do L^p, gdy f należy do L^p. Dla większych p w d>2 sama regularność H² nie wystarcza do kontroli gradientu. Nadal rozróżniono uzyskanie W^{2,p} od oszacowania a priori. Znak równania, symetryzacja i hipotezy RRC 15 sprawdzone.

Zachowano wszystkie 30 etykiet. 79/79 odsyłaczy do 42 celów w RRC 03,07,08,09,10,15,16,17, bez brakujących i wieloznacznych w sprawdzonych plikach. Stos środowisk poprawny przed zapisem. PDF i CI nadal niepotwierdzone. Druga lektura 32/64 z poprawkami. Następna iteracja 279: 033–042.
