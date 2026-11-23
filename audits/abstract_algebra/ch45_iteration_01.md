# AA-45 — audyt I: plan matematyczny i kontrola wstępna

**Data:** 23 listopada 2026 r.  **Stan: AUDYT — NIE STABILNY.**

## Źródła i zakres
- Źródło robocze: sources/pl/galois(2).tex, rozdział „Cztery ważne całki nieelementarne”, przeredagowany z etykietami, bez odwołań do numerów starego monolitu.
- Zależności: stabilne AA-43 (pochodne śladu, normy, kryteria stałych) i AA-44 (twierdzenie Liouville'a, formalne części wielomianowe pochodnych).
- Nowy rozdział: kryterium dla st, pełne kryterium dla skończonych sum Laurenta, dokładne przeszkody biegunowe i stopniowe, cztery przykłady nieelementarne oraz kontrprzykłady elementarne.

## Kontrola I — zobowiązania dowodowe
1. Wykazano algebraicznie przestępność e^{p(x)} dla niestałego p i brak nowych stałych przy pomocy normy, śladu i części właściwych pochodnych logarytmicznych.
2. Dla st: z AA-44 przejście do porównania współczynnika przy t w części wielomianowej Dv; pochodne logarytmiczne nie mają dodatnich potęg.
3. Dla potęg ujemnych t: użyto generatora w=t^{-1}; nie zakłada się błędnej niezależności t i t^{-1}.
4. Przeszkoda biegunowa wymaga regularności h; kontrprzykład pokazuje jej niezbędność.
5. Całka Gaussa: równanie r'-2xr=1 wykluczone stopniem; całka oznaczona policzona niezależnie.
6. Sin(x)/x: dodatnia potęga e^{ix} daje niemożliwe r'+ir=1/(2ix); obliczenie całki Dirichleta zawiera oszacowanie ogonów jednostajne w parametrze tłumienia.
7. 1/log(x): podstawienie x=e^u redukuje do e^u/u; nieelementarność tego ostatniego z przeszkody bieguna prostego.
8. Całka eliptyczna: nierozkładalność T²-(1-x⁴), lokalne współrzędne na gładkiej krzywej i dwa punkty nad nieskończonością; forma dx/y bez biegunów; funkcje bez biegunów są stałe; residua pochodnych logarytmicznych są całkowitymi rzędami; niezależność nad Q wymusza stałość kombinacji.
9. Kontrast: wymierne funkcje mają lokalne elementarne pierwotne; dodatnie przykłady testu r'+hr=s.

## Integracja
Rozdział ma wejść do książki i katalogu jako AA-45, a bramka źródeł ma sprawdzać 45 rozdziałów z osobnymi raportami 43–45, zachowując historyczny audyt przekrojowy AA-01–AA-42. Dwa zestawy regresyjne: model SymPy oraz niezależny model na liczbach wymiernych bez SymPy.

## Niezakończone
Nie nadano werdyktu STABILNY. Pozostają rzeczywiste zdalne CI, drugi audyt, oględziny wszystkich nowych stron PDF, log i kontrola poprzednich stron. AA-46 zablokowany.
