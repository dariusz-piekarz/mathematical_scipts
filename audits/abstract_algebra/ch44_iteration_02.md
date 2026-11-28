# AA-44 — audyt II: niezależny przegląd przypadków brzegowych

**Data:** 23 listopada 2026 r. **Werdykt: NIE STABILNY** — czekamy na rzeczywiste bramki kompilacji i PDF ostatecznej wersji; AA-45 nie rozpoczęto.

## Matematykę sprawdzono niezależnie od pierwszego audytu

1. **Charakterystyka zero:** przejście przez ślad dzieli przez stopień rozszerzenia; przejście logarytmiczne dzieli przez niezerowy wykładnik całkowity. Obie operacje są uzasadnione wyłącznie w charakterystyce zero.
2. **Formalna część wielomianowa:** dla R=P+A/B z deg A<deg B=d zachodzi D(A/B)=((DA)B-A(DB))/B². Przy Dt=a oraz Dt=ht mamy deg DA<=deg A i deg DB<=d, więc wynik jest funkcją właściwą. Nie wymagamy rozkładu mianownika nad ciałem bazowym.
3. **Krok algebraiczny:** dla f w F zachodzi Tr(f)=[L:F]f; norma niezerowego U jest niezerowa. Normalność L/F nie jest założona. Tożsamości pochodnych śladu i normy pochodzą z AA-43.
4. **Krok logarytmiczny:** przy m=0 zostaje element F; przy m=1 zostaje składnik cDt=c Db/b z c w C; przy m>=2 dwa najwyższe współczynniki prowadzą do nowej stałej t-w i sprzeczności z C_L=C.
5. **Krok wykładniczy:** współczynniki przy każdej potędze dodatniej t porównuje się osobno. Gdy p_k!=0, element p_k t^k jest nową stałą. Pozostałe A Da= D(Aa) dla A w C.
6. **Przestępność:** dla generatora algebraicznego zawsze wolno użyć zejścia algebraicznego nawet wtedy, gdy spełnia jednocześnie warunek logarytmiczny lub wykładniczy. Wykorzystanie braku nowych stałych dotyczy całej skończonej wieży i każdego pośredniego piętra.
7. **Dostateczność:** jeżeli pierwotna pochodnej logarytmicznej już istnieje w bieżącym ciele, korzystamy z niej bez dołączania nowej zmiennej. Jeśli jej nie ma, dołączenie przestępnego elementu pierwotnego nie daje nowych stałych na mocy lematu AA-43. Obejmuje to n=0 i przypadki z zerowymi współczynnikami.
8. **Ujemne potęgi Laurenta:** pochodne logarytmiczne mogą posiadać ujemne potęgi przy t nieskończonym. Dowód porównuje tylko części wielomianowe, więc nie korzysta z błędnego założenia ich braku.
9. **Stałe niedomknięte algebraicznie:** dla K=Q(x) element 1/(x²+1) nie ma przedstawienia z współczynnikami w Q: przy x=i ma resztę 1/(2i), podczas gdy pochodne funkcji wymiernych mają resztę 0, a pochodne logarytmiczne funkcji z Q(x) mają reszty całkowite. Złożony wzór przez logarytmy korzysta z i jako nowej stałej.
10. **Nowe stałe:** jeśli Dt=Dx=1, wtedy D(t-x)=0; nie wolno stosować do takiej wieży lematu logarytmicznego bez dodatkowych warunków.

## Rzeczywiście naniesione poprawki

- W niezależnych testach AA-44 usunięto tautologiczne sprawdzenia i zastąpiono je obliczeniami pochodnej w modelu fractions.Fraction, niezależnym od SymPy.
- W rozdziale dodano przykład nad Q(x), rozróżniający brak nowych stałych od dowolnego dołączania stałych algebraicznych.

## Niezamknięte kryteria

Oba niezależne audyty matematyczne mają źródłowe raporty, ale nadal trzeba uzyskać PASS obu zestawów regresyjnych i pełnego CI na aktualnej wersji, sprawdzić log LaTeX, odsyłacze i obejrzeć każdą nową stronę PDF. Dopiero wtedy możliwa jest decyzja STABILNY.
