# Algebra abstrakcyjna — AA-X19: wyróżnik formy śladu, wielomianu i wypadkowa (AA-23 × AA-32 × AA-33)

**Data:** 2026-11-23. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Status wejściowy:** AA-X18 zamknięty po 6/6 testów i 96/96 kroków CI; treści 50 zatwierdzonych rozdziałów nie modyfikowano.
**Przeczytane źródła:** \`23-slad-norma-i-wyroznik.tex\` (blob \`69f5f2c35c3e7179055e0acc06fe95e041d0bc24\`), \`32-wyroznik-i-grupa-galois.tex\` (blob \`f8c525aff1093478dcd8b1083387a42a37078086\`), \`33-wypadkowa-wielomianow-i-macierz-sylvestera.tex\` (blob \`40f339a13b5890418869a12ef27881d29233ffe7\`).
**Odrębność od AA-X04 i AA-X08:** AA-X04 badał wielomiany cyklotomiczne i wypadkowe; AA-X08 sprawdzał ślad/normę w teorii Galois. Teraz sprawdzamy **identyczność trzech różnych konstrukcji** na rozszerzeniu prostym, łącznie z rachunkiem macierzy mnożenia i zdegenerowanymi przypadkami.

## 1. Samodzielna identyfikacja trzech wyróżników

**Twierdzenie.** Niech \`K\` będzie ciałem, \`m\in K[X]\` monicznym nierozkładalnym wielomianem stopnia \`n\ge2\`, \`L=K(\alpha)\cong K[X]/(m)\` i \`m(\alpha)=0\`. W bazie potęgowej \`b=(1,\alpha,\ldots,\alpha^{n-1})\` mamy
\[
\det\bigl(\operatorname{Tr}_{L/K}(\alpha^{i+j})\bigr)_{0\le i,j<n}
=\operatorname{disc}(m)
=(-1)^{n(n-1)/2}R_{n,n-1}(m,m'),
\]
gdzie \`R_{n,n-1}\` jest dokładnie podpisaną w AA-33 wypadkową z **formalnym** stopniem \`n-1\` dla drugiego argumentu. Równości zachodzą nad dowolnym ciałem, również dla nierozdzielczego \`m\`, gdy obie strony znikają.

**Dowód, przypadek rozdzielczy.** Oznaczmy przez \`\sigma_1,\ldots,\sigma_n:L\hookrightarrow\overline K\` różne \`K\`-zanurzenia. Dla \`V=(\sigma_i(\alpha)^{j-1})_{1\le i,j\le n}\` i formy \`B(x,y)=\operatorname{Tr}_{L/K}(xy)\` wzór na ślad przez zanurzenia z AA-23 daje macierz Grama \`G_b=V^{\mathsf T}V\`. Stąd \`\det G_b=(\det V)^2=\prod_{i<j}(\sigma_i(\alpha)-\sigma_j(\alpha))^2\`. Z definicji AA-32 jest to \`\operatorname{disc}(m)\`. Dla pochodnej mamy
\[
N_{L/K}(m'(\alpha))=\prod_{i=1}^n m'(\sigma_i(\alpha))
=(-1)^{n(n-1)/2}\operatorname{disc}(m).
\]
Z AA-33 i moniczności \`m\` wynika \`N_{L/K}(m'(\alpha))=R_{n,n-1}(m,m')\`, również jeżeli rzeczywisty stopień \`m'\` jest mniejszy od \`n-1\`. To kończy przypadek rozdzielczy.

**Przypadek nierozdzielczy i charakterystyka dodatnia.** Ponieważ \`m\` jest nierozkładalny, nierozdzielczość zachodzi dokładnie wtedy, gdy \`m'=0\`. Wtedy wypadkowa formalna \`R_{n,n-1}(m,0)=0\` i wyróżnik AA-32 również wynosi zero. Aby uzasadnić zerowy wyróżnik formy śladu, przyjmijmy \`K_s\subset L\` jako maksymalne podrozszerzenie rozdzielcze. Stopień \`[L:K_s]\` jest potęgą \`p=\operatorname{char}K\` większą od 1. Wielomian charakterystyczny każdego \`a\in L\` nad \`K_s\` ma ślad \`0\` (równoważnie \`\operatorname{Tr}_{L/K_s}=0\` dla nierozdzielczego rozszerzenia czysto nierozdzielczego). Z przechodniości śladu \`\operatorname{Tr}_{L/K}=0\`. Forma śladu jest więc identycznie zerowa, stąd jej wyznacznik jest zerem. Nie próbuje się używać wzoru z \`n\` różnymi zanurzeniami w przypadku nierozdzielczym.

**Ważne ograniczenie.** Równość wyróżnika bazy z wyróżnikiem wielomianu dotyczy właśnie **bazy potęgowej dla wielomianu minimalnego**. W AA-23 inna baza \`c=bS\` ma wyróżnik \`(\det S)^2\operatorname{disc}(b)\`; nie wolno utożsamiać dowolnego wyróżnika bazy z wielomianowym. Dla niemonicznego wielomianu definiowanego wyłącznie przez swoje pierwiastki należy najpierw odpowiednio ustalić normalizację; AA-32 definiuje wyróżnik wielomianowy tylko dla wielomianów monicznych.

## 2. Niezależne rachunki i przypadki brzegowe

- **\`m=X²-5\` nad \`\mathbb Q\`:** forma śladu w \`(1,\sqrt5)\` ma macierz \`\begin{psmallmatrix}2&0\\0&10\end{psmallmatrix}\` i wyróżnik \`20\`; po zmianie bazy na \`(1,(1+\sqrt5)/2)\` otrzymujemy macierz \`\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\` i wyróżnik \`5\`. Wyróżnik wielomianu minimalnego pozostaje \`20\`. Sprawdzono kwadrat wyznacznika macierzy przejścia.
- **Stopień trzeci i czwarty:** dla \`X³-2\`, \`X³-3X+1\`, \`X⁴-2\` wyznaczniki macierzy Grama są odpowiednio \`-108\`, \`81\`, \`-2048\`, zgodnie z wyróżnikami wielomianowymi i podpisaną wypadkową pochodnej. W stopniu \`4\` szczególnie ważny jest ujemny znak \`(-1)^6=1\` w formule, ale sam wyróżnik może być ujemny.
- **Norma jako wypadkowa:** dla trzech wymienionych przykładowych wielomianów monicznych oraz \`h=2X+3\`, \`h=X²+X+1\`, \`h=X-1\` porównano wyznacznik macierzy mnożenia przez \`h(\alpha)\` z \`R(m,h)\` i niezależnym algorytmem \`sympy.resultant\`.
- **Wielomian z pierwiastkiem wielokrotnym:** dla \`f=(X-1)²\` i \`g=X+2\` mamy \`R(f,g)=9\`, lecz \`R(f,f')=0\` i wyróżnik \`0\`. \`K[X]/(f)\` nie jest ciałem, toteż to jedynie test tożsamości w skończonej algebrze, **nie** kontrprzykład w rozszerzeniu ciał.
- **Formalne stopnie AA-33:** dla \`f=2X+1\` i \`g=X+3\` otrzymano odpowiednio \`R_{1,1}(f,g)=5\`, \`R_{1,2}(f,g)=10\` oraz \`R_{2,1}(f,g)=-5\`. Nie wolno pominąć stopni formalnych przy pochodnej.
- **Charakterystyki \`2\` i \`3\`:** dokładne rachunki modulo \`p\` obejmują \`(p,f)=(2,X²+X+1),(2,X²+1),(3,X²+1),(3,X³+1)\`. Wartości wyróżników to odpowiednio \`1,0,2,0\`. Przykłady obejmują wielomiany rozdzielcze i takie, dla których pochodna po redukcji ma niższy stopień bądź znika.
- **Nierozdzielcze rozszerzenie ciała:** w \`\mathbb F_2(t)[X]\` wielomian \`X²+t\` jest nierozkładalny, ale ma pochodną zerową. Macierz mnożenia przez \`\alpha\` spełnia \`M_\alpha²=tI_2\`, a \`\operatorname{Tr}(I_2)=\operatorname{Tr}(M_\alpha)=\operatorname{Tr}(M_\alpha²)=0\` w charakterystyce \`2\`. Macierz formy śladu jest więc zerowa, zgodnie z dwiema pozostałymi konstrukcjami.

Niezależnie wykonano powyższe rachunki przez kod SymPy w sesji analitycznej; wyniki porównań zgadzały się dokładnie. Nie podstawiano tolerancji numerycznych.

## 3. Nowa trwała regresja i integralność LaTeX

Utworzono \`tools/tests/test_abstract_algebra_cross_aa23_32_33.py\` z **6 testami \`unittest\`**:
1. forma śladu w bazie potęgowej, wyróżnik oraz ślad/norma elementu \`\alpha\`;
2. \`N(h(\alpha))=R(m,h)\` i porównanie z algorytmem \`sympy.resultant\`;
3. podpisana wypadkowa pochodnej, stopnie formalne, pierwiastki wielokrotne;
4. transformacja wyróżnika przy zmianie bazy;
5. rachunki w charakterystykach \`2\`, \`3\`, w tym \`\mathbb F_2(t)\`;
6. etykiety, założenia źródłowe i odsyłacze.

Przeczytano źródła AA-23, AA-32, AA-33 i rozdziały z ich zewnętrznymi odsyłaczami: AA-03, AA-11, AA-20, AA-21, AA-22, AA-29, AA-31. W trzech głównych rozdziałach odnotowano **49 etykiet** (30+9+10), a także **26 odsyłaczy**; wszystkie celują w istniejące etykiety w tej grupie dziesięciu rozdziałów, bez kolizji.

Workflow \`.github/workflows/abstract-algebra-chapter.yml\` rozszerzono o wyzwalacz ścieżki testowej oraz oddzielny krok \`Run AA-X19 trace discriminant resultant crosschecks\`.

**Uruchomienie CI:** [45213530134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45213530134), commit workflow \`904bcebcbe6a867ac5ce26c2c68b756dba77586e\`. Przy zapisaniu raportu status \`in_progress\`, bez końcowego wyniku.

## 4. Status i granice

**AA-X19: W STABILIZACJI.** W kontrolowanych zależnościach nie wykryto sprzeczności matematycznej ani koniecznej korekty zatwierdzonych rozdziałów. Nie zmieniono źródeł AA-23, AA-32, AA-33; dodatkowe twierdzenie identyfikujące formę śladu z podpisaną wypadkową można później dodać za zgodą użytkownika jako wzbogacenie, lecz nie jest to naprawa.

Do zamknięcia wymagane są odczyt rzeczywistych wyników **6/6 testów** w nowym kroku CI, \`completed/success\` całego workflow, pozytywna kompilacja AA-01–AA-50 i kontrola PDF/odsyłaczy. Kompilacja nie oznacza osobnej wizualnej inspekcji stron PDF. Testy konkretnych wielomianów nie zastępują dowodu podanego w punkcie 1. AA-51 pozostaje nieotwarty.
