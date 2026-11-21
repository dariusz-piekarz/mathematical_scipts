# Algebra liniowa — rozdział 09 „Formy dwuliniowe i kwadratowe”, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-formy-dwuliniowe-i-kwadratowe.tex`  
**Zbadany blob:** `979ce687c677125aeb8304e9d13cb8e7af842602`  
**Raporty poprzednie:** `ch09_formy_iteration_01.md`, `ch09_formy_iteration_02.md`.

## Przedmiot niezależnej kontroli

Ponownie przeanalizowano nowy rozdział 09 i kolejność rozdziałów 08–11. Oceniono kwantyfikację założeń i oznaczeń w każdym twierdzeniu, kompletność dowodów, przypadki `dim V=0`, warunki na charakterystykę ciała, poprawność przykładów, język i terminologię, zgodność wzorów z materiałem wcześniejszych rozdziałów i z geometrią różniczkową. Nie dodano nowych twierdzeń, sekcji ani przykładów i nie zmieniono pliku matematycznego.

## Audyt matematyczny — wynik czysty

1. **Ortogonalność:** definicja dopełnienia ortogonalnego dla symetrycznej formy oraz wzór `dim U^⊥=dim V-dim U+dim(U∩Rad(b))` są poprawne. Dowód oparty jest na równości rzędów odwzorowania `U→V*` i jego dualnego. Odsyłacz do `thm:lin7-jadro-obraz-dualnego` jest obecny i prawidłowy.
2. **Ortogonalna suma:** założenie niezdegenerowania ograniczenia `b|_U` jest wystarczające; niezdegenerowanie na całym `V` nie jest potrzebne. Wyprowadzona suma `V=U⊕U^⊥` uwzględnia wymiar i trywialne przecięcie.
3. **Kwadratowość i polaryzacja:** definicja przez jednorodność stopnia 2 i dwuliniowość polaryzacji jest poprawna nad dowolnym ciałem. Zależności `b_q(v,v)=2q(v)`, `q(v)=b_q(v,v)/2` przy `char K≠2` i rozwinięcie na współczynniki są prawidłowe także w przypadku zerowego wymiaru. W charakterystyce 2 rozróżniono formę kwadratową od jej polaryzacji.
4. **Diagonalizacja:** dowód indukcyjny używa `char K≠2` wyłącznie w uzyskaniu wektora o niezerowej wartości `b(w,w)`. Następnie można przeprowadzić rozkład ortogonalny i indukcję. Wymiar radykału i liczba niezerowych współczynników są zgodne.
5. **Prawo bezwładności:** maksymalny wymiar podprzestrzeni dodatniej to liczba dodatnich składników, a maksymalny wymiar podprzestrzeni ujemnej to liczba ujemnych składników w postaci normalnej. Dowód oparty na wymiarze przecięcia z komplementarną podprzestrzenią nie wymaga teorii spektralnej, a liczba zerowych elementów wynika z `n-p-m`.
6. **Kryterium Sylvestera:** kierunek konieczny sprawdzony przez ograniczenia formy, dostateczność przez uzupełnienie kwadratu i dodatniość dopełnienia Schura. Równość wyznaczników wiodących bloków jest poprawna; argument ma odrębny przypadek `n=0`.
7. **Iloczyn skalarny i ortogonalizacja:** minimalizacja kwadratowej funkcji `t↦b(u-tv,u-tv)` daje nierówność Cauchy'ego–Schwarza wraz z warunkiem równości. Konstrukcja Grama–Schmidta jest dobrze określona dzięki niezależności wektorów, a rzut ortogonalny jednoznaczny dzięki ortogonalnej sumie i spełnia własność minimalizacyjną.
8. **Naprzemienność w każdej charakterystyce:** wybór pary `u,v` z `a(u,v)=1` i jawny wzór `x_U=a(x,v)u-a(x,u)v` realizują rozkład z blokiem `J`; po iteracji rząd formy jest parzysty. Nie ma niedozwolonego dzielenia przez 2 w dodatniej charakterystyce.
9. **Przykłady i grafika:** rozkład `2x²+4xy+5y²=2(x+y)²+3y²` jest prawidłowy; minory macierzy `3×3` w kryterium Sylvestera mają wartości 2, 3, 4; przykłady degeneracji i niejednoznaczności polaryzacji w `F_2` działają. Adaptacja elipsy jednostkowej z geometrii różniczkowej jest zgodna z kongruencją form.

## Kontrola oszczędności materiału

Rozdział 08 pozostaje miejscem podstawowych definicji i pierwszych dowodów dotyczących odwzorowań wieloliniowych oraz macierzy form dwuliniowych. Rozdział 09 nie przepisuje tych dowodów; przedstawia ortogonalność, kwadratowość i klasyfikację. Z istniejącego rozdziału 11 skryptu geometrii różniczkowej (`11-tensor-metryczny-dlugosc-i-miara.tex`) wykorzystano argumentację dotyczącą metryki i ortonormalnych współrzędnych oraz schemat elipsy i okręgu. Rozdziały 10 i 11 zachowały wszystkie fragmenty poprzednich, zaudytowanych rozdziałów tensorowych — poza zmianą numeracji/etykiet nie zmieniono ich twierdzeń, przykładów ani dowodów.

## Kontrola CI i liczby

- Struktura 11 rozdziałów: **465 różnych etykiet**, **196 odsyłaczy do istniejących etykiet**, zgodne `\\input` i katalog, brak niezrównoważonych środowisk, brak terminów niezgodnych ze standardami.
- W przebiegu [GitHub Actions 44918096223](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44918096223) dla kompletnej, przenumerowanej książki: **SUCCESS**, 118 stron PDF, zero ostrzeżeń typu `LaTeX Warning`, `Overfull`, `Underfull`, `Undefined control sequence` ani nierozwiązanych odsyłaczy.
- Test `tools/test_linear_algebra_quadratic_forms.py` zaliczył **2331** kontroli polaryzacji, **68746** kontroli wymiarów dopełnień ortogonalnych, **833** kontrole parzystości rzędów form naprzemiennych, **1613** kontrole dodatniej określoności/kongruencji, razem **73523**.
- Zachowano także komplet automatycznych testów iloczynów tensorowych i algebry zewnętrznej z wcześniejszych rozdziałów.
- Każdy kolejny commit dokumentacyjny uruchamia własny CI; jego powodzenie trzeba potwierdzić po zakończeniu, nie zakładać go w chwili commitu.

## Decyzja

**Audyt III — czysty.** Nie wykryto nowych usterek w samodzielnych twierdzeniach ani dowodach, żadnych brakujących odsyłaczy i żadnych problemów z charakterystyką (2). Treść nowego rozdziału 09 pozostaje bez zmian. Poprawna, zmieniona kolejność jest zamknięta: **rozdziały 01–11 stabilne po audytach**. Historyczne raporty tensorowe zachowano bez ingerencji i opisano w raporcie migracji.
