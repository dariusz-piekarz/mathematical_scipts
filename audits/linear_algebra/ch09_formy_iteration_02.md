# Algebra liniowa — rozdział 09 „Formy dwuliniowe i kwadratowe”, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/09-formy-dwuliniowe-i-kwadratowe.tex`  
**Blob sprawdzony:** `979ce687c677125aeb8304e9d13cb8e7af842602`

## Reuse materiału zamiast duplikowania

Rozdział 09 korzysta z udowodnionych już twierdzeń rozdziału 08 `08-odwzorowania-wieloliniowe.tex` (definicja formy, zmiana macierzy przez kongruencję, radykał, polaryzacja). Te definicje i dowody nie są rozwijane ponownie. Z istniejącego skryptu geometrii różniczkowej, `chapters/pl/differential_geometry_and_topology/11-tensor-metryczny-dlugosc-i-miara.tex`, zaadaptowano model dodatnio określonej metryki, wyjaśnienie baz ortonormalnych oraz rysunek elipsy/okręgu jednostkowego. Geometria różniczkowa posługuje się włóknami stycznymi, natomiast nowy rozdział przedstawia odpowiadające im zagadnienia w czystej algebrze liniowej. Nie przenoszono twierdzeń o rozmaitościach ani strukturach spinowych.

## Niezależna weryfikacja matematyczna

1. **Dopełnienie ortogonalne i radykał:** dla symetrycznej `b`, `U^⊥` jest podprzestrzenią, `U⊂(U^⊥)^⊥`, a `Rad(b|_U)=U∩U^⊥`. Wzór `dim U^⊥=dim V-dim U+dim(U∩Rad(b))` wynika z równości rzędów odwzorowań dualnych `M:U→V*` oraz `L:V→U*`; wszystkie przestrzenie są skończenie wymiarowe. Poprawiono odsyłacz do istniejącego `thm:lin7-jadro-obraz-dualnego`.
2. **Rozkład ortogonalny:** jeśli ograniczenie do `U` jest niezdegenerowane, wtedy `U∩U^⊥=0`, `dim U^⊥=n-dim U`, stąd `V=U⊕U^⊥`. Nie potrzeba niezdegenerowania `b` na całej przestrzeni.
3. **Forma kwadratowa:** definicja przez jednorodność stopnia dwa i dwuliniową polaryzację działa w dowolnej charakterystyce. Z niej wynikają `q(-v)=q(v)` i `b_q(v,v)=2_Kq(v)`. Dla charakterystyki różnej od dwóch symetryczne formy dwuliniowe odpowiadają kwadratowym przez `q(v)=b_q(v,v)/2_K`.
4. **Współrzędne:** jednoznaczne współczynniki `a_i=q(e_i)` i `c_ij=b_q(e_i,e_j)` wyznaczają funkcję kwadratową także nad ciałami skończonymi; w charakterystyce 2 składniki `x_i²` mogą znikać podczas polaryzacji, co wyjaśnia jej nieiniektywność.
5. **Diagonalizacja:** przy `char K≠2` niezerowa symetryczna forma posiada wektor `w` z `b(w,w)≠0`. Ograniczenie do `Kw` jest niezdegenerowane, a indukcja na `w^⊥` daje bazę ortogonalną. W charakterystyce 2 ten krok może zawieść; zamieszczono kontrprzykład.
6. **Prawo bezwładności Sylvestera:** każdą rzeczywistą formę kwadratową sprowadzono przez skalowanie wektorów bazy do współczynników `+1,-1,0`. Liczba dodatnich składników jest maksymalnym wymiarem podprzestrzeni dodatniej, a ujemnych — maksymalnym wymiarem podprzestrzeni ujemnej. Ich niezmienniczość jest w pełni uzasadniona.
7. **Kryterium Sylvestera:** kierunek konieczny wynika z dodatniej określoności każdego ograniczenia do pierwszych `k` wektorów bazy. Dla dostateczności użyto uzupełnienia kwadratu i dopełnienia Schura `C-rr^T/a` oraz dodatnich wiodących minorów; dowód działa przez indukcję, także dla `n=0`.
8. **Nierówność Cauchy'ego–Schwarza i ortogonalizacja:** minimalizując `b(u-tv,u-tv)` uzyskano nierówność, następnie normę. Algorytm Grama–Schmidta ma w każdym kroku niezerowy wektor `w_j` dzięki niezależności danych. Wzór na rzut i jego własność minimalizacyjną dowiedziono przez rozkład ortogonalny i kwadraty norm.
9. **Formy naprzemienne nad dowolnym ciałem:** niezerowa forma daje parę `u,v` o `a(u,v)=1_K`; jawne rozbicie `V=span(u,v)⊕span(u,v)^⊥` umożliwia indukcję i budowę bloków `J`. Dowód nie używa dzielenia przez 2. Rząd musi być parzysty. Przykłady `q_1,q_2` w charakterystyce 2 wykazują, że klasyfikacja polaryzacji nie klasyfikuje samej funkcji kwadratowej.
10. **Wizualizacja:** schemat elipsy i okręgu opisuje transformację współrzędnych `(x_1,x_2)↦(x_1,2x_2)` dla tej samej dodatnio określonej formy `x_1²+4x_2²`; ilustracja jest algebraiczną adaptacją rysunku z DG 11.

## Kontrola migracji i CI

- Nowy porządek to: `08-odwzorowania-wieloliniowe.tex`, `09-formy-dwuliniowe-i-kwadratowe.tex`, `10-iloczyny-tensorowe.tex`, `11-algebry-tensorowa-symetryczna-i-zewnetrzna.tex`. Oba poprzednie rozdziały tensorowe zachowano bezstratnie z techniczną zamianą przestrzeni nazw etykiet.
- Sprawdzono skład całej książki po migracji: **465 unikalnych etykiet**, **196 odsyłaczy do istniejących etykiet**, brak błędów środowisk LaTeX, zgodne importy w książce i katalogu.
- W pierwszym commicie migracyjnym odkryto jeden brakujący odsyłacz w nowym rozdziale 09: `thm:lin7-rzad-dualnego`. Zastąpiono go właściwym, istniejącym `thm:lin7-jadro-obraz-dualnego`. Po poprawce kontrola statyczna i CI walidacji struktury przechodzą bez błędu.
- Włączono osobne testy `tools/test_linear_algebra_quadratic_forms.py` do `.github/workflows/linear-algebra-chapter.yml`. Obejmują skończone ciała `F_2, F_3` (polaryzacja, ortogonalność, parzystość rzędu form naprzemiennych) oraz rzeczywiste przykłady określoności i kongruencji. Nowy test przeszedł we wstępnym przebiegu CI.
- Pełny wynik kompilacji wersji z nowym testem należy zweryfikować po zakończeniu GitHub Actions; nie deklarujemy sukcesu przed sprawdzeniem. Dotychczasowy CI poprawionej migracji z dnia 21 listopada zakończył się powodzeniem.

## Decyzja

**Audyt II — bez nowych usterek matematycznych; jeden brakujący odsyłacz naprawiony w iteracji migracyjnej.** Nie dodano nowych twierdzeń ani nie zmieniono dowodów w tej iteracji. Przed końcowym zamknięciem zmienionego porządku zalecana jest dodatkowa czysta kontrola stabilizacyjna oraz potwierdzenie ostatniego przebiegu CI.
