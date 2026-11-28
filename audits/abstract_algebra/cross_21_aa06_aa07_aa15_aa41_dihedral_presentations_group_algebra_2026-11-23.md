# Algebra abstrakcyjna — AA-X21: prezentacje grup diedralnych, algebry grupowe i reprezentacje (AA-06 × AA-07 × AA-15 × AA-41)

**Data:** 2026-11-23. **Repozytorium:** \`dariusz-piekarz/mathematical_scipts\`; **istniejąca gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Poprzedni audyt:** AA-X20 zamknięty po 6/6 testach i 98/98 ukończonych krokach [CI 45222177294](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45222177294).
**Źródła odczytane:** AA-06 blob \`e504d9d70bc66e0307c466e4be1a0fb2d33dfe30\`, AA-07 blob \`931eb83323a543e55cc9e4c439ab864111d65264\`, AA-15 blob \`b055965112ca86a86e6d0a88213a8274b9d09a68\`, AA-41 blob \`05d87a9b95117069879b58e5c6ea40d71ad4a29c\`. Przestrzegano \`AGENTS.md\`.

## 1. Odrębny zakres audytu

W AA-X16 badano pierścień grupowy i centralne projektory w \(\mathbb C[S_3]\); w AA-X21 przedmiotem jest **równoważność prezentacji grup przez generatory i relacje, prezentacji ich algebr grupowych przez nieprzemienne wielomiany oraz realizacji liniowych przez macierze**. Porównano też semidirect product z AA-06 z prezentacją z AA-07, bez nadpisywania zatwierdzonych rozdziałów.

### Twierdzenie przekrojowe z pełnym dowodem

Niech \(n\ge3\), \(K\) dowolnym ciałem, a \(D_{2n}\) grupą diedralną rzędu \(2n\) z prezentacją
\[
D_{2n}=\langle r,s\mid r^n=1,\ s^2=1,\ srs^{-1}=r^{-1}\rangle.
\]
Wówczas
\[
K[D_{2n}]\cong
K\langle u,v\rangle/
(u^n-1,\ v^2-1,\ vu-u^{n-1}v),
\]
gdzie nawias w mianowniku oznacza **ideał dwustronny**, a \(K\langle u,v\rangle\) jest wolną algebrą łączną nad \(K\).

**Dowód.** Odwzorowanie wolnej algebry z AA-15 wysyłające \(u\mapsto[r]\), \(v\mapsto[s]\) jest surjekcją na \(K[D_{2n}]\): wyrażenia \([r]^i[s]^j=[r^is^j]\), \(0\le i<n\), \(j\in\{0,1\}\), generują ją jako przestrzeń wektorową, ponieważ w AA-06 i AA-07 sprawdzono, że każde \(g\in D_{2n}\) ma taką jednoznaczną postać. Z relacji diedralnych elementy \(u^n-1\), \(v^2-1\) i \(vu-u^{n-1}v\) należą do jądra, więc otrzymujemy surjekcję z ilorazu \(A_n\).

W \(A_n\) mamy \(u^{n-1}=u^{-1}\) i \(v^{-1}=v\), ponieważ \(u^n=v^2=1\). Relacja \(vu=u^{n-1}v\) pozwala przenosić każde wystąpienie \(v\) w prawo: dla potęgi \(u^k\) indukcja daje \(vu^k=u^{-k}v\). W konsekwencji każde słowo w \(u,v\) jest równe pewnemu \(u^iv^j\) dla \(0\le i<n\), \(j=0,1\); dowolna kombinacja liniowa słów jest kombinacją co najwyżej \(2n\) tych monomów. Dlatego \(\dim_K A_n\le2n\). Jednocześnie \(\dim_K K[D_{2n}]=|D_{2n}|=2n\), zatem surjekcja \(A_n\to K[D_{2n}]\) między przestrzeniami o wymiarze co najwyżej i dokładnie \(2n\) jest izomorfizmem. Nie wymaga to założenia dotyczącego charakterystyki \(K\). **Koniec dowodu.**

**Wniosek (macierze).** Dla dowolnej \(K\)-przestrzeni \(W\) reprezentacja \(\rho:D_{2n}\to\mathrm{GL}_K(W)\) jest jednoznacznie określona parą operatorów \(U,V\in\mathrm{End}_K(W)\) spełniających \(U^n=V^2=I\) i \(VU=U^{n-1}V\). W obu kierunkach korzystamy z własności uniwersalnej prezentacji AA-07 i korespondencji reprezentacje–lewe moduły AA-41. Równania automatycznie gwarantują odwracalność \(U,V\), ponieważ \(U^{-1}=U^{n-1}\) i \(V^{-1}=V\). **Sam fakt spełniania relacji nie oznacza, że reprezentacja jest wierna.**

## 2. Kontrole konkretnych modeli

Dla każdego \(n\in\{3,4,5,6\}\) modelujemy iloczyn półprosty z AA-06 przez pary \((i,j)\in(\mathbb Z/n)\times(\mathbb Z/2)\), z mnożeniem
\[
(i,j)(k,l)=(i+(-1)^jk\bmod n,\ j+l\bmod2).
\]
Sprawdzono normalne postacie, działania na \(n\) wierzchołkach i zgodność składania permutacji. Reprezentacja permutacyjna jest wierna dla \(n\ge3\).

Dla \(n=3\) dostajemy \(D_6\cong S_3\) oraz dokładne macierze
\[
U=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
V=\begin{pmatrix}-1&1\\0&1\end{pmatrix}.
\]
Spełniają \(U^3=V^2=I\), \(VU=U^2V\); sześć macierzy \(U^iV^j\) jest różnych. Dla \(n=4\) odpowiadające macierze obrotu i odbicia kwadratu są
\[
U=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
V=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Spełniają \(U^4=V^2=I\), \(VU=U^3V\); osiem macierzy \(U^iV^j\) jest różnych. Porównano wszystkie pary iloczynów \(U^iV^jU^kV^l\) z prawem grupy.

**Pułapka modularna:** redukcja drugiej reprezentacji \(2\times2\) modulo \(2\) spełnia wszystkie relacje, ale \(V=I\) i \(U\) ma rząd \(2\), więc obraz ma tylko **dwa** elementy; reprezentacja przestaje być wierna. Tymczasem reprezentacja regularna na \(\mathbb F_2[D_8]\) pozostaje wierna, ponieważ elementy bazy \([g]\) są różnymi wektorami i \([g]\cdot[1]=[g]\). Pokazuje to różnicę między twierdzeniem o prezentacji, istnieniem reprezentacji, jej wiernością i półprostotą. Nie używamy twierdzenia Maschkego w charakterystyce dzielącej \(2n\). Standardowe macierze \(S_3\) pozostają wierne po redukcji modulo \(2\) i \(3\), mimo że półprostota nie jest wtedy gwarantowana.

**Abelianizacja:** z równości \(srs^{-1}=r^{-1}\) po narzuceniu przemienności wynika \(r^2=1\). Dla nieparzystego \(n\), dodatkowe \(r^n=1\) wymusza \(r=1\), więc \(D_{2n}^{\mathrm{ab}}\cong C_2\). Dla parzystego \(n\) otrzymujemy \(D_{2n}^{\mathrm{ab}}\cong C_2\times C_2\); niezależność dwóch generatorów wynika z surjekcji na \(C_2\times C_2\), która respektuje wszystkie relacje. W charakterystyce różnej od \(2\) daje to dokładnie odpowiednio \(2\) i \(4\) jednowymiarowe charaktery nad dowolnym ciałem \(K\), gdyż ich wartości \(r,s\) należą do \(\{\pm1\}\); w charakterystyce \(2\) oba znaki są równe i tych charakterów jest tylko \(1\). **Test nie utożsamia** tej liczby z wymiarem przestrzeni funkcji klasowych w dodatniej charakterystyce.

## 3. Trwała regresja i integralność źródeł

Dodano \`tools/tests/test_abstract_algebra_cross_aa06_07_15_41.py\` — **8 testów**:
1. łączność i normalne postacie \(D_6,D_8,D_{10},D_{12}\);
2. wierne permutacyjne działanie na wierzchołkach;
3. relacje i niezależność \(2n\) elementów bazy w algebrze grupowej oraz łączność przykładowych kombinacji;
4. wierność modułu regularnego bez założenia o charakterystyce;
5. macierze \(S_3,D_8\) nad \(\mathbb Z\), pełne tabele iloczynów;
6. kontrast pomiędzy redukcją \(D_8\) modulo \(2\) a modułem regularnym oraz \(S_3\) nad \(\mathbb F_2,\mathbb F_3\);
7. jednowymiarowe reprezentacje i abelianizacja dla parzystego i nieparzystego \(n\);
8. źródła LaTeX, etykiety i odsyłacze wszystkich 50 rozdziałów.

Bezpośredni odczyt czterech badanych rozdziałów dał **93 unikatowe etykiety** (21+28+25+19), **41 odsyłaczy** (20+9+2+10). W odsyłaczach AA-06 są prawidłowe cele zewnętrzne (inne rozdziały), dlatego test sprawdza je wobec **całej** 50-rozdziałowej książki, a nie tylko czterech plików.

Rozszerzono \`.github/workflows/abstract-algebra-chapter.yml\` o wyzwalacz pliku testowego i osobny krok \`Run AA-X21 dihedral presentation group algebra representations\`. Bieżący workflow [45224658006](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45224658006) uruchomiono na dokładnym commicie \`3f6991c0ac6d28a86fe1b09a0c9c183d2b71ab48\`.

**AA-X21: W STABILIZACJI CI.** Niezależna kontrola macierzy \(2\times2\) i źródeł została przeprowadzona; ostateczny wynik zestawu ośmiu testów musi zostać potwierdzony odczytem ukończonego GitHub Actions, podobnie jak kompilacja PDF i kontrola odsyłaczy. Nie wpisano dodatków do żadnego zatwierdzonego rozdziału.

## 4. Werdykt matematyczny i propozycja redakcyjna

Przegląd wymienionych czterech źródeł nie ujawnił koniecznej korekty matematycznej. Dodanie powyższej tożsamości
\(K[D_{2n}]\cong K\langle u,v\rangle/(u^n-1,v^2-1,vu-u^{n-1}v)\)
po własności uniwersalnej wolnej algebry w AA-15 byłoby użytecznym **opcjonalnym** uzupełnieniem, lecz wymaga decyzji użytkownika zgodnie z \`AGENTS.md\`; bez aprobaty nie zmieniamy gotowych rozdziałów.

Testy skończone nie zastępują ogólnego dowodu, nie są formalną kompilacją Lean i nie oznaczają wizualnego przeglądu wszystkich stron PDF. **AA-01–AA-50 pozostają niezmienione; AA-51 nie otwierano.**

## 5. Zamknięcie AA-X21 — końcowa bramka PASS

Rzeczywisty przebieg [GitHub Actions 45224658006](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45224658006) na dokładnie commicie workflow \`3f6991c0ac6d28a86fe1b09a0c9c183d2b71ab48\` zakończył się **completed/success**. Job \`validate-cli\` wykonał **99/99 kroków**, bez awarii. Odczytano log jobu \`137867800100\` i potwierdzono **8/8 testów AA-X21 = ok**, każdy zarówno przy globalnym odkrywaniu \`unittest\`, jak i w osobnym kroku \`Run AA-X21 dihedral presentation group algebra representations\`.

Krok \`Compile AA-01 to AA-50 book with latexmk\`: **success**. Krok \`Verify PDF and references (no undefined refs)\`: **success**. Artefakt \`abstract-algebra-aa01-aa50\` ID \`14842782171\`, ZIP **2 289 388 bajtów**. Nie wykonano dodatkowej niezależnej inspekcji wizualnej stron PDF; status kompilacji i automatycznej integralności referencji nie jest tym samym co taka inspekcja.

**AA-X21: ZAMKNIĘTY / STABILNY** w zakresie wskazanej kontroli przekrojowej. Nie ujawniono błędu wymagającego zmian zatwierdzonych rozdziałów. Ogólny dowód izomorfizmu prezentowanej algebry grupowej jest odrębny od testów skończonych przykładów; nie deklarujemy formalnej weryfikacji Lean. Wszystkie dotychczasowe statusy AA-01–AA-50 zachowano; rozdziałów nie modyfikowano i nie otwierano AA-51.

**Następna iteracja:** wybrać inny zakres i otworzyć AA-X22 dopiero po powyższym zamknięciu, nadal bez automatycznego dopisywania opcjonalnych uzupełnień do zatwierdzonych źródeł.
