# Teoria grafów i węzłów — audyt 27: rozdziały 34–36, drugie niezależne przejście

Data: 2026-11-23. Gałąź: biblioteka-matematyczna-iteracja-6.
Pierwsze przejście: [audyt 26](47-globalny-audyt-26-rozdzialy-34-36-pierwsze-przejscie.md).
Zasada: dwa rzeczywiste przejścia, nowe poprawki matematyczne, niezależne regresje, potrójny skład pełnego PDF i przegląd wizualny — dopiero potem stabilizacja lokalna.

## Rozdział 34 — grupa dyskryminantowa i metabolizer ogólnej konfiguracji C_p

Dodano lemat o etykiecie lem:tg-syn-cp-metabolizer, dla każdej liczby całkowitej p≥2 oraz łańcucha wag (−(p+2),−2,…,−2). Dla brzegu Y_p=∂C_p:

* H_1(Y_p;Z) jest **cykliczna**, rzędu p², a meridian pierwszej składowej μ_0 ją generuje.
* W konwencji formy splecenia λ=−Q_Cp^−1 mod Z otrzymujemy λ(μ_0,μ_0)=(p−1)/p² mod Z.
* Podgrupa M_p=p<μ_0> ma rząd p oraz M_p=M_p^⊥.
* Jeżeli wypełnienie B_p ma H_1(B_p;Z)=Z/p i mapę surjektywną z brzegu, to jądrem mapy jest dokładnie M_p. **Istnienie wypełnienia nie jest wnioskiem z samej formy.**

Dowód: prezentacja przez macierz Q pozwala wyeliminować relacje ogona, otrzymując x_i=(p−1−i)x_{p−2} i pierwszą relację −p²x_{p−2}=0. Dla p=2 przypadek macierzy (−4) rozpatrzono osobno. Ze znanej wartości wyznacznika p² wynika cykliczność. Kofaktor pierwszego elementu jest wyznacznikiem łańcucha p−2 wag −2, skąd (Q^−1)_{00}=−(p−1)/p². Ortogonalność do generatora pμ_0 zachodzi wtedy i tylko wtedy, gdy p dzieli współczynnik elementu grupy. Dla p=7 odzyskujemy metabolizer Z/49 z rozdziału Parka po uwzględnieniu różnicy konwencji znaków.

## Rozdział 35 — pełne stopniowanie algebraicznego kompleksu Khovanova

Dodano stwierdzenie prop:kt-kh-graded-euler oraz przykład ex:kt-kh-reidemeister-one-euler.

Jeżeli A=Z[X]/(X²), deg(1)=1, deg(X)=−1, a przesunięcie stanu wynosi |s|+n_+−2n_−, to różniczka ma bistopień (1,0). Wynika to z kwantowego stopnia −1 obu operatorów m i Δ i przesunięcia o +1 wzdłuż każdej krawędzi kostki. Gradująca charakterystyka Eulera homologii ma więc postać

χ_q(Kh(D)) = Σ_s (−1)^(|s|−n_−) q^(|s|+n_+−2n_−) (q+q^−1)^(k(s)).

Uzasadnienie korzysta z zasady Eulera–Poincarégo dla skończonego kompleksu grup wolnych, oddzielnie w każdym stopniu kwantowym. Rangi nie uwzględniają torsji jako składowej liczbowej.

Dla f(q)=q+q^−1 obie formy skrętu Reidemeistera typu I dają χ_q=f:
* dodatni: q f² − q² f = f;
* ujemny: −q^−2 f + q^−1 f² = f.

Obliczenia stopni i charakterystyki Eulera **nie zastępują** głębokiego dowodu niezmienniczości homologii pod ruchami Reidemeistera. Ponownie skontrolowano konstrukcję zredukowaną z punktem bazowym, warunek n_z=0 w różniczce CFK^− i zakres twierdzeń Ni, Ozsvátha–Szabó.

## Rozdział 36 — dane źródłowe weryfikowane niezależnie

Dodano pierwotne pozycje:
* E. S. Lee, *An endomorphism of the Khovanov invariant*, Adv. Math. 197 (2005), 554–586; DOI https://doi.org/10.1016/j.aim.2004.10.015 .
* Y. Ni, *Knot Floer homology detects fibred knots*, Invent. Math. 170 (2007), 577–608; DOI https://doi.org/10.1007/s00222-007-0075-9 , oraz sprostowanie w Invent. Math. 177 (2009), 235–238.
* M. Symington, *Symplectic rational blowdowns*, J. Differential Geom. 50 (1998), 505–518; DOI https://doi.org/10.4310/jdg/1214424968 .
* DOI pracy J. Rasmussena: https://doi.org/10.1007/s00222-010-0275-6 .

Źródła zweryfikowano w bibliografiach instytucjonalnych i artykułach pierwotnych, m.in. Caltech (Ni), ScienceDirect (Lee) i arXiv (Symington).

## Nowe niezależne regresje

Utworzono tools/tests/test_graph_and_knot_synthesis_modern_second_pass.py i włączono go do .github/workflows/graph-and-knot-global-audit.yml. Moduł nie zastępuje pakietu audytu 26.

Wyniki w zadaniu structural-audit przebiegu
[45254635859](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45254635859):

1. **691 131** kontroli: ogólna rodzina C_p, p=2,…,127, wyznaczniki, kofaktory, cykliczność, forma splecenia, ortogonalność i izotropowość metabolizera dla wszystkich elementów Z/p².
2. **4368** kontroli: stopień kwantowy lokalnych mnożeń i komnożeń Khovanova przy różnych stopniach homologicznych i liczbach skrzyżowań dodatnich/ujemnych.
3. **114 687** kontroli: znaki dwóch ścieżek na każdej dopuszczalnej ścianie kostki o wymiarach 2–12.
4. **45 438** kontroli: gradująca charakterystyka Eulera dla splotów trywialnych, dodatni i ujemny skręt Reidemeistera typu I oraz elementarna zasada Eulera–Poincarégo.
5. Kontrole obecności nowych lematów i czterech zweryfikowanych DOI.

Łącznie **855 624** NOWYCH przypadków arytmetycznych, wszystkie PASS.
Poprzedni moduł audytu 26 zawierał 27 596 przypadków.
W dwóch niezależnych audytach 26–27 sprawdzono łącznie **883 220 przypadków**.

Końcowa kontrola strukturalna źródeł (commit 4fd017d45e72a197896b4b666eab3d68c407681d): 44/44 rozdziały, 0 duplikatów etykiet, 0 nierozwiązanych odsyłaczy, 0 błędów środowiska i 0 zakazanych terminów.

## Bramka PDF i werdykt

Po sprawdzeniu nowej matematyki i regresji należy:
1. potwierdzić sukces full-book-pdf dla końcowej wersji źródeł;
2. zweryfikować trzy przebiegi pdflatex i pusty plik ostrzeżeń;
3. obejrzeć nowe strony rozdziałów 34–36, w tym długi lemat C_p, wzór charakterystyki Eulera i nową bibliografię.

**Do czasu spełnienia wszystkich tych warunków 34–36 pozostają w stabilizacji.** W razie powodzenia drugi niezależny audyt będzie zakończony PASS, a lokalnie stabilne staną się rozdziały 01–36. Następny blok: audyt 28, pierwsze przejście rozdziałów 37–39. Ogólny audyt 44 rozdziałów nadal pozostaje otwarty.
