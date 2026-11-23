# AA-X07 — audyt przekrojowy AA-37–AA-40: transcendencja, normalizacja Noether, wymiar Krulla, całkowitość

**Data:** 23 listopada 2026 r.  
**Repozytorium:** \`dariusz-piekarz/mathematical_scipts\`. **Istniejąca gałąź:** \`biblioteka-matematyczna-iteracja-6\`.

## 1. Źródła i dokładny zakres

| Rozdział | Główne wyniki | SHA Git blob źródła |
| --- | --- | --- |
| AA-37 | Bazy transcendencji, wymiana algebraiczna, niezmienniczość stopnia transcendencji | \`b710ae2447d41aef8681de6d55f4c6d3709616c1\` |
| AA-38 | Trójkątne zmiany zmiennych, lemat normalizacyjny Noether, także nad ciałami skończonymi | \`2edea1072ab0b052f492e88f9dd508ba5c938d3a\` |
| AA-39 | Wymiar Krulla, ideały pierwsze ilorazów i lokalizacji, \(\dim K[U,V]=2\) | \`1b8990241d26cbf461a0e7b4a07546a3ef77fa9e\` |
| AA-40 | Rozszerzenia całkowite, wznoszenie i nieporównywalność ideałów, wymiar \(K[X_1,\ldots,X_n]\) | \`101cd301f88c9e1cc84e89d2ce3cb57bc7c8fe2b\` |

Audyt opiera się na **faktycznych aktualnych plikach** rozdziałów, nie na streszczeniu z wcześniejszych iteracji. Wszystkie cztery pliki są dołączone przez \`\\input\` do \`books/pl/abstract_algebra.tex\`. Nie zmieniono ich treści matematycznej.

## 2. Niezależna kontrola matematyczna zależności

### AA-37 → AA-38: algebraiczna niezależność i konstrukcja normalizacji

Sprawdzono krok wymiany w AA-37: z algebraiczności \(x\) nad \(F(b)\), transcendentalności \(x\) nad \(F=K(B\setminus\{b\})\) i niezależności \(B\) otrzymuje się niezerowy wielomian \(Q(U,x)\in F(x)[U]\) zerujący się w \(b\). Wykorzystany jest fakt, że niezerowe współczynniki \(q_j(T)\in F[T]\) nie znikają po podstawieniu \(T=x\). Zależności potrzebne do wymiany baz nie wymagają separowalności rozszerzeń.

W AA-38 sprawdzono konstrukcję \(\mathbb N\)-wag \(w(\alpha)=\alpha_n+\sum_{i<n}\alpha_iM^i\) dla \(M>d+1\). Różne jednomiany stopnia całkowitego nieprzekraczającego \(d\) mają różne wagi, a po \(X_i=Y_i+Y_n^{M^i}\) najwyższa potęga \(Y_n\) ma niezerowy **stały** współczynnik z \(K\). Nie stosuje się dzielenia przez współczynniki dwumianowe, dlatego argument zachowuje ważność w charakterystykach \(2,3,5\).

W dowodzie AA-38 należy odróżnić:
1. skończone generowanie \(A\) jako \(K\)-algebry;
2. całkowitość pojedynczego elementu \(a_n\) nad \(B=K[b_1,\ldots,b_{n-1}]\), uzyskaną z równania monicznego;
3. wynikające stąd skończone generowanie \(A=B[a_n]\) jako **\(B\)-modułu**;
4. przechodniość skończoności modułowej w kroku indukcyjnym, która daje normalizację.

Te cztery przejścia w AA-38 są uzasadnione; hipoteza, że \(A\) jest dziedziną, nie jest używana. Osobno zbadano jawny przykład nad \(\mathbb F_2\) z relacją \(X^2+XY+Y\), dla którego \(u=x+y^4\) daje moniczne równanie ósmego stopnia dla \(y\).

### AA-38 → AA-39/AA-40: całkowitość i niezmienniczość wymiaru

Normalizacja dostarcza włączenia \(K[y_1,\ldots,y_r]\subseteq A\), w którym \(A\) jest modułem skończenie generowanym. Wynik AA-40 o całkowitości skończenie generowanego modułu, a następnie **istnienie ideału leżącego nad danym, wznoszenie łańcuchów oraz nieporównywalność ideałów o tej samej kontrakcji** pozwalają na równość \(\dim A=r\). Rozdział AA-40 nie zakłada automatycznie, że surjektywny obraz pierścienia wielomianów jest dziedziną; rozdziela te przypadki.

W AA-39 kluczowy wzór dla ideałów pierwszych ilorazu dotyczy **ideałów zawierających jądro**; po lokalizacji — ideałów pierwszych rozłącznych ze zbiorem mianowników. Przy przejściu do wymiaru użyto rzeczywistych ścisłych łańcuchów ideałów, a nie tylko nieścisłych zawierań.

Sprawdzono dowód \(\dim K[U,V]=2\) w AA-39, łącznie z redukcją pary niestowarzyszonych wielomianów nierozkładalnych do ilorazu skończenie wymiarowego nad \(K\). Dowód \(\dim K[X_1,\ldots,X_n]=n\) w AA-40 opiera się na lemacie moniczności AA-38 i indukcji po \(n\): po wybraniu niezerowego \(f\in\mathfrak p_1\) quotient \(K[X_1,\ldots,X_n]/(f)\) jest skończonym modułem nad \(K[Y_1,\ldots,Y_{n-1}]\), a ten pierścień **wstrzykuje się** do ilorazu, ponieważ wielomian moniczny dodatniego stopnia względem \(Y_n\) nie może dzielić niezerowego wielomianu niezależnego od \(Y_n\). Dopiero wtedy stosuje się niezmienniczość wymiaru przy rozszerzeniu całkowitym.

### AA-40: włókna, rozgałęzienie i zakres hipotez

Rozdział poprawnie odróżnia **rozszerzenie całkowite** od rozszerzenia **skończonego modułowo**. Pierwsze wystarcza do istnienia ideałów nad danym, wznoszenia i nieporównywalności; ograniczenie liczby ideałów nad danym do \(m\) wykorzystuje silniejsze założenie, że \(B\) ma \(m\) generatorów jako \(A\)-moduł. Przykład lokalizacji \(K[t]\hookrightarrow K[t,t^{-1}]\) pokazuje, że bez całkowitości ideał \((t)\) nie musi mieć ideału leżącego nad nim.

Dla algebraicznej krzywej z ostrzem \(K[t^2,t^3]\subseteq K[t]\) kontrolowano relację \(y^2=x^3\), skończoność modułową i rolę ciała ułamków. Nie utożsamiono algebraiczności ciała ułamków z całkowitością elementu nad podpierścieniem.

## 3. Test I — moniczność i niezależne rachunki nad ciałami skończonymi

**Ścieżka:** \`tools/tests/test_abstract_algebra_cross_aa37_40.py\`; **3085/3085 PASS**.

- Wyliczono wszystkie jednomiany niestałe stopnia całkowitego \(\le3\) w \(2\) albo \(3\) zmiennych i dodatkowe deterministycznie wybrane kombinacje dwu- i trójmianowe, nad \(\mathbb F_2,\mathbb F_3,\mathbb F_5\).
- Dla każdego sprawdzono różność wag, dokładny stopień po trójkątnym podstawieniu, zgodność współczynnika wiodącego z przewidzianym niezerowym skalarem i równość po podstawieniu odwrotnym.
- Z użyciem **niezależnej redukcji Gröbnera** sprawdzono jawne relacje moniczne dla algebry \(\mathbb F_p[X,Y]/(X^2+XY+Y)\), zachowanie klas \(1,v,\ldots,v^7\) oraz redukcję wyższych potęg.
- Sprawdzono bazę \(1,v\) dla ilorazu z relacją \(v^2=u^3\), a także sześć klas jednomianowych algebry z elementami nilpotentnymi \(\mathbb F_p[u,v]/(u^2,v^3)\).

Dodatkowe testy nad ciałami skończonymi są istotne, ponieważ niepoprawna wersja argumentu normalizacyjnego mogłaby milcząco wykorzystywać nieskończoność \(K\).

## 4. Niezależny test II — rzeczywiste włókna skończonych rozszerzeń całkowitych

**Ścieżka:** \`tools/tests/test_abstract_algebra_cross_aa37_40_confirming.py\`; **4752/4752 PASS**.

Rozpatrzono zupełnie inny typ konstrukcji niż w teście I:
\[
\mathbb F_p[T]\hookrightarrow\mathbb F_p[U],
\qquad T\longmapsto U^e,\quad 2\le e\le5.
\]
Jest to rozszerzenie całkowite i wolne rangi \(e\) jako moduł nad \(\mathbb F_p[T]\), z bazą \(1,U,\ldots,U^{e-1}\).

Dla wszystkich monicznych nierozkładalnych \(f(T)\) stopnia do \(3\) nad \(p=2,3,5\), oraz do \(2\) dla \(p=7\), rozłożono \(f(U^e)\) na czynniki nierozkładalne. Test niezależnie sprawdza:
- bezpośrednio faktoryzację z krotnościami i równość całkowitego stopnia \(e\deg f\);
- co najmniej jedno i co najwyżej \(e\) **różnych** ideałów pierwszych w włóknie nad \((f)\);
- kontrakcję każdego czynnika \(g(U)\) równą dokładnie \((f(T))\), nie tylko zawierającą ten ideał; minimalność wielomianu sprawdzono **eliminacją Gaussa** dla klas \(1,U^e,\ldots,U^{e(\deg f-1)}\) w \(\mathbb F_p[U]/(g)\);
- \(\mathbb F_p\)-wymiar \(e\deg f\) ilorazu \(\mathbb F_p[U]/(f(U^e))\) oraz jawnie wyznaczoną bazę modułu po zmianie ciała współczynników;
- istnienie rozgałęzionych włókien, w tym całkowicie nieredukowanego włókna nad \((T)\), gdzie \(f(U^e)=U^e\);
- brak ideału nad \((T)\) w **niecałkowitej** lokalizacji \(\mathbb F_p[T,T^{-1}]\).

Wynik: **4752/4752** zaliczonych kontroli, **682** wystąpienia czynników pierwszych (zliczone z powtórzeniami między przykładami) i **91** przypadków czynników o krotności większej niż \(1\). Te trzy liczby opisują różne wielkości.

**Łącznie: 7837/7837 konkretnych kontroli obliczeniowych PASS.** Nie oznacza to formalnego dowodu wszystkich twierdzeń.

## 5. Struktura LaTeX, referencje, kompletność

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
| --- | ---: | ---: | ---: | ---: |
| AA-37 | 15 | 6 | 7 | 7 |
| AA-38 | 9 | 4 | 3 | 7 |
| AA-39 | 20 | 12 | 10 | 7 |
| AA-40 | 23 | 23 | 11 | 9 |
| **Razem** | **67** | **45** | **31** | **30** |

Wszystkie 67 etykiet są unikatowe. Spośród 45 wystąpień odsyłaczy tylko trzy wskazują poza badany blok; potwierdzono ich istnienie przez osobne odczytanie odpowiednich plików:
- \`aa:tw:fundamental-symmetric\` — AA-31;
- \`aa:ch:pierscienie\` — AA-09;
- \`aa:ch:lokalizacja\` — AA-12.

Wszystkie środowiska \`\\begin{...}\` i \`\\end{...}\` są poprawnie sparowane, a AA-37–AA-40 występują we właściwej kolejności w głównym pliku książki.

## 6. Integracja CI i warunek zamknięcia

Oba skrypty (SymPy + standardowa biblioteka Pythona) wykonano **lokalnie** i zapisano bajtowo identyczne wersje w repozytorium:
- test I: commit \`23a89c094ab5906cf685c64871b0cd84d42ab16c\`;
- test II: commit \`3fa7e008e41f87fffb2c1edb25a355e0fd12c108\`;
- integracja obu kroków i ścieżek wyzwalających w \`.github/workflows/abstract-algebra-chapter.yml\`: commit \`b0e1b09ebbbcf1839f3859d7136a4165abd01077\`.

Polecenia odtwarzające:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa37_40.py
python tools/tests/test_abstract_algebra_cross_aa37_40_confirming.py
\`\`\`

**Stan matematyczny:** dla sprawdzonego zakresu nie znaleziono koniecznej poprawki źródeł AA-37–AA-40. **Formalną stabilność AA-X07** potwierdzamy dopiero po zakończeniu zdalnego CI (dwa nowe zestawy, pełne PDF AA-01–AA-42, weryfikacja odsyłaczy), pobraniu rzeczywistego artefaktu i wizualnej kontroli stron czterech rozdziałów. Dopóki te kroki nie zostały wykonane, **AA-X07 pozostaje w trakcie zamykania**.
