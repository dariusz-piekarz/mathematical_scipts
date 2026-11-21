# Algebra liniowa — rozdział 01, audyt 7

Data: 2026-11-21  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`  
Commit treści po audycie: `9510097c6ec53b50149e0a084f5ad7a1b4fb1126`

## Zakres

Siódma iteracja audytu dotyczy wyłącznie rozdziału 01. Sprawdzono wszystkie aksjomaty i przykłady przestrzeni wektorowych, kryterium podprzestrzeni, sumy i przecięcia, warunki pokrywania przestrzeni przez podprzestrzenie, przestrzenie rozpięte przez zbiory i rodziny indeksowane, skończony charakter niezależności, przypadki o charakterystyce \(2\), lemat Steinitza, niezmienniczość wymiaru, wybór i rozszerzanie baz metodą Zorna, w tym puste łańcuchy i puste bazy.

W szczególności przeanalizowano logiczną zgodność twierdzeń o współrzędnych dla baz skończonych z twierdzeniami o bazach Hamela dla dowolnego zbioru indeksów \(I\).

## Wykryte luki i poprawki

### 1. Brak ogólnego twierdzenia o współrzędnych bazy Hamela

Dotychczasowe twierdzenie `thm:lin-wspolrzedne` konstruowało współrzędne tylko dla \(n\)-elementowych baz skończonych. W rozdziale zdefiniowano następnie bazy Hamela dowolnego wymiaru, ale nie udowodniono analogicznego opisu przez funkcje o skończonym nośniku.

Dodano **twierdzenie `thm:lin-wspolrzedne-hamela`**:

Dla dowolnej bazy Hamela \(B=(b_i)_{i\in I}\) istnieje liniowy izomorfizm
\[
V\xrightarrow{\ \cong\ }K^{(I)},\qquad
K^{(I)}=\{a:I\to K:\#\operatorname{supp}(a)<\infty\}.
\]
Ujęcie obejmuje także \(I=\varnothing\). Dowód:
1. weryfikuje, że \(K^{(I)}\) jest podprzestrzenią przestrzeni \(K^I\) funkcji \(I\to K\);
2. konstruuje dobrze określone odwzorowanie \(\Phi_B(a)=\sum_{i\in\operatorname{supp}(a)}a_ib_i\);
3. sprawdza liniowość na wspólnym skończonym nośniku;
4. dowodzi surjektywności z warunku rozpinania;
5. dowodzi iniektywności z niezależności liniowej;
6. wyprowadza liniowość odwrotnego odwzorowania współrzędnych;
7. rozpatruje przestrzeń zerową odpowiadającą pustej bazie.

### 2. Brak definicji izomorfizmu przed użyciem terminu

Przed nowym twierdzeniem doprecyzowano, że odwzorowanie liniowe \(T:U\to W\) zachowuje wszystkie kombinacje \(T(au+bv)=aT(u)+bT(v)\), a **izomorfizm przestrzeni wektorowych to bijekcja liniowa**. Szczegółowa teoria odwzorowań liniowych pozostaje w dalszej części skryptu.

### 3. Przykład konkretnych współrzędnych nieskończonych

Dodano **przykład `prz:lin-wspolrzedne-hamela-wielomiany`**:
\[
K[X]\cong K^{(\mathbb N_0)},\qquad
\sum_{j=0}^d a_jX^j\longmapsto(a_0,\ldots,a_d,0,0,\ldots).
\]
Zaznaczono różnicę między przestrzenią ciągów o skończonym nośniku a przestrzenią wszystkich ciągów: ciąg stały \((1,1,\ldots)\) nie jest współrzędną wielomianu w bazie jednomianów.

### 4. Dwuznaczność sformułowania jednoznaczności reprezentacji

Końcowe podsumowanie stwierdzało dosłownie, że istnieje „dokładnie jedno przedstawienie jako skończona kombinacja liniowa”. Bez ustalonego porządku i konwencji zapisywania zerowych współczynników jest to sformułowanie mylące: tę samą kombinację można przestawiać lub dopisywać wyrazy zerowe.

Zastąpiono je ścisłym twierdzeniem o **jednej rodzinie współczynników \((a_b)_{b\in B}\) o skończonym nośniku** przy ustalonych elementach bazy \(B\), której kombinacja daje dany wektor. Wskazano, że porządek wyrazów nie jest elementem tej jednoznaczności.

## Wynik kontroli strukturalnej

Po zmianach:
- 68 różnych etykiet lokalnych `\\label`, bez powtórzeń;
- wszystkie odsyłacze `\\ref` oraz `\\eqref` mają cele w rozdziale;
- środowiska `\\begin`/`\\end` są zrównoważone;
- liczba figur TikZ nadal wynosi 2; nowych plików zewnętrznych nie dodano;
- CI poprzedniej iteracji: [44892015946](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892015946) — zaliczone;
- CI aktualnego tekstu: [44892390182](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892390182) — **weryfikacja wyniku do uzupełnienia**.

Kontrola globalna Biblioteki nadal raportuje wcześniejsze niepowiązane błędy importów i kopii skryptów. Nie są one liczone jako błędy rozdziału 01 i nie zostały w tej iteracji poprawione.

## Status

**Audyt 7 wykrył rzeczywiste uzupełnienia i je wdrożył. Rozdział 01 pozostaje otwarty.**
Kolejna iteracja: audyt 8 tej samej treści, szczególnie nowo dopisanego twierdzenia o współrzędnych oraz jego składu; bez tworzenia rozdziału 02.
