# AA-X05 — audyt przekrojowy AA-16–AA-18: moduły, postać Smitha i iloczyn tensorowy

**Data:** 23 listopada 2026 r.  
**Repozytorium:** \`dariusz-piekarz/mathematical_scipts\`.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Zakres:** AA-16 — homomorfizmy modułów, ciągi dokładne i rzutowość; AA-17 — moduły nad dziedzinami ideałów głównych, postać Smitha; AA-18 — iloczyn tensorowy, dokładność i płaskość.

## 1. Niezmieniona baza źródłowa

Sprawdzono źródła LaTeX na docelowej gałęzi:

| Rozdział | Ścieżka | Git blob |
|---|---|---|
| AA-16 | \`chapters/pl/abstract_algebra/16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex\` | \`319cbac9af83a819e0d375fc282284c62638c3ac\` |
| AA-17 | \`chapters/pl/abstract_algebra/17-moduly-nad-dziedzinami-idealow-glownych-i-postac-smitha.tex\` | \`07d654dab3b20ad7016d160b86914f541d8273a5\` |
| AA-18 | \`chapters/pl/abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex\` | \`faaa972f8d1a7625d42c856d78c6f58ee7ad3564\` |

Ten audyt kontroluje **mosty między trzema rozdziałami**; nie zastępuje historycznych audytów każdego ich twierdzenia.

## 2. Niezależna kontrola matematyczna

### AA-16 — homomorfizmy, ilorazy, dokładność i rozszczepienie

Sprawdzono, że dowody pierwszego twierdzenia o izomorfizmie, kryteriów rozszczepienia oraz charakterystyki modułów rzutowych zachowują założenia o lewych modułach nad pierścieniem z jedynką, także nieprzemiennym. W dowodzie rzutowości modułu wolnego o dowolnej bazie jawnie zaznaczono użycie aksjomatu wyboru dla nieskończonej rodziny przedobrazów.

**Modele skończone.** Dla wszystkich \(1\le n\le30\), \(0\le k\le30\) przetestowano pierwsze twierdzenie o izomorfizmie dla \(\mathbb Z/n\to\mathbb Z/n\), \(x\mapsto kx\), przez niezależne wyliczenie jądra i obrazu. Dla wszystkich \(1\le a,b\le18\) sprawdzono dokładny ciąg
\[
0\to\mathbb Z/a\xrightarrow{[x]\mapsto[bx]}\mathbb Z/(ab)
\xrightarrow{[y]\mapsto[y]}\mathbb Z/b\to0.
\]
Rzeczywiście rozszczepia się on wtedy i tylko wtedy, gdy \(\gcd(a,b)=1\): homomorfizm przekrojowy wysyłający \(1\bmod b\) na \(y\bmod ab\) musi spełniać jednocześnie \(y\equiv1\bmod b\) i \(by\equiv0\bmod ab\). Sprawdzono wszystkie dopuszczalne obrazy generatora, nie sam wzór na kryterium.

### AA-17 — postać Smitha i przedstawienia skończone

Dla macierzy \(A=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)\) nad \(\mathbb Z\) wyznaczono z ideałów minorowych
\(d_1=\gcd(a,b,c,d)\) oraz \(d_2=|\det A|/d_1\), gdy odpowiednie rangi są dodatnie, z osobnym traktowaniem zer. Dla **625** macierzy o współczynnikach \(-2,-1,0,1,2\) i każdego \(2\le n\le11\) niezależnie wyliczono obraz \((\mathbb Z/n)^2\xrightarrow{A\bmod n}(\mathbb Z/n)^2\) i jego iloraz. Jego liczność zgadzała się ze wzorem
\[
|\operatorname{coker}(A\bmod n)|
=\prod_{j=1}^2\begin{cases}
\gcd(d_j,n),&d_j\ne0,\\
n,&d_j=0.
\end{cases}
\]
Ta równość łączy postać Smitha z konstrukcją iloczynu tensorowego z AA-18: \(\operatorname{coker}(A)\otimes_\mathbb Z\mathbb Z/n\cong\operatorname{coker}(A\bmod n)\).

W dowodzie AA-17 nad ogólną dziedziną ideałów głównych nie zastąpiono bez uzasadnienia tej hipotezy silniejszą hipotezą euklidesowości: użyto stabilizacji łańcuchów ideałów i odwracalnych bloków \(2\times2\) z lematu Bézouta. Lematy o ideałach minorowych uzasadniają jednoznaczność z dokładnością do stowarzyszenia.

### AA-18 — iloczyn tensorowy, dokładność i płaskość

Weryfikowano rzeczywistą treść izomorfizmów \(\mathbb Z/m\otimes_\mathbb Z\mathbb Z/n\cong\mathbb Z/\gcd(m,n)\), prawostronną dokładność, zgodność z sumą prostą oraz związek iloczynu tensorowego z modułami homomorfizmów. Model skończony uwzględnia **900** par \(1\le m,n\le30\), **3375** trójek \(1\le m,n,k\le15\) i **2197** trójek \(1\le a,b,n\le13\).

Kolejne przykłady wyraźnie rozdzielają płaskość i rzutowość: dla każdego \(2\le m\le30\) iniekcja \(\mathbb Z\xrightarrow{\cdot m}\mathbb Z\) po zastosowaniu \(-\otimes\mathbb Z/m\) staje się odwzorowaniem zerowym i traci iniektywność. Jednocześnie \(\mathbb Z/m\) nie jest rzutowy jako \(\mathbb Z\)-moduł, bo \(\mathbb Z\twoheadrightarrow\mathbb Z/m\) nie rozszczepia się. Dowód płaskości ciała ułamków korzysta w tekście z lokalizacji, a nie z nieuzasadnionego wniosku, że każdy moduł bez torsji jest automatycznie płaski nad dowolnym pierścieniem.

Dla iloczynu tensorowego nad pierścieniem nieprzemiennym AA-18 konsekwentnie zaczyna od **prawego** i **lewego** modułu, a strukturę modułu i izomorfizmy symetrii/łączności formułuje dalej po jawnym założeniu **przemienności** pierścienia. Nie wykryto w sprawdzonych twierdzeniach niejawnej zmiany strony działania.

## 3. Pierwszy zestaw odtwarzalnych testów — 15 559/15 559 PASS

Nowy moduł: \`tools/tests/test_abstract_algebra_cross_aa16_18.py\` (stdlib Python, bez zależności od wcześniejszych modułów).

| Grupa sprawdzeń | Liczba |
|---|---:|
| Jądro/obraz i pierwszy izomorfizm | 930 |
| Kryterium rozszczepienia | 324 |
| Iloczyny tensorowe modułów cyklicznych | 900 |
| Prawostronna dokładność | 900 |
| Izomorfizm Hom–iloczyn tensorowy (liczność map) | 3375 |
| Rozdzielność względem sum prostych | 2197 |
| Liczności ilorazów macierzy po redukcji modulo \(n\) | 6250 |
| Warunki minorowe macierzy \(2\times2\) | 625 |
| Przykłady niepłaskości i nierzutowości | 58 |
| **Suma** | **15 559** |

## 4. Niezależny audyt potwierdzający — 78 732/78 732 PASS

Dodatkowo utworzono osobny \`tools/tests/test_abstract_algebra_cross_aa16_18_confirming.py\` sprawdzający **wszystkie \(3^9=19\,683\) macierze \(3\times3\)** o współczynnikach w \(\{-1,0,1\}\). W odróżnieniu od pierwszego modułu dla każdej macierzy obliczono:
- \(\Delta_1\) jako NWD dziewięciu wpisów;
- \(\Delta_2\) jako NWD **wszystkich dziewięciu** minorów \(2\times2\);
- \(\Delta_3\) jako moduł wyznacznika \(3\times3\);
- niezmienniki \(d_1=\Delta_1\), \(d_2=\Delta_2/\Delta_1\), \(d_3=\Delta_3/\Delta_2\), z poprawnymi wyjątkami dla rangi poniżej \(3\).

Liczności \(\operatorname{coker}(A\bmod n)\) wyliczono następnie z **bezpośredniego zbioru obrazów** na \((\mathbb Z/n)^3\) dla \(n\in\{2,3,4\}\). We wszystkich **59 049** przypadkach były identyczne z iloczynem \(\gcd(d_j,n)\) (z czynnikiem \(n\) dla zera). Kolejne **19 683** kontrole dotyczyły poprawności łańcucha minorów i rang. Profil rang: \(1\) macierz rangi \(0\), \(338\) rangi \(1\), \(7536\) rangi \(2\), \(11\,808\) rangi \(3\).

**Łącznie oba odrębne zestawy: 94 291/94 291 poprawnych warunków.** Licznik odnosi się do konkretnych sprawdzeń obliczeniowych, nie do liczby niezależnych twierdzeń.

Odtworzenie:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa16_18.py
python tools/tests/test_abstract_algebra_cross_aa16_18_confirming.py
\`\`\`

Kod zapisano w commitach \`494c00e8e63d3af431cef0fa78d2ea474d7a574a\` oraz \`457e31016b8944b3d1ef748b7d464b7d825b9af1\`. Oba kroki i ich wyzwalacze dodano do \`.github/workflows/abstract-algebra-chapter.yml\` (końcowy commit integracyjny \`5c441354a822f8bc079ee5616918c66f41fece85\`).

## 5. Źródła, odsyłacze i LaTeX

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-16 | 26 | 6 | 10 | 7 |
| AA-17 | 16 | 11 | 9 | 4 |
| AA-18 | 20 | 11 | 12 | 7 |
| **Suma** | **62** | **28** | **31** | **18** |

Wszystkie **62 etykiety są unikatowe**; każda z 28 referencji ma cel lokalny lub w innej sprawdzonej części książki. Cztery zewnętrzne etykiety zweryfikowano wprost: \`aa:tw:euclidean-pid\`, \`aa:tw:pid-ufd\`, \`aa:tw:crt-ring\` (AA-09/10) oraz \`aa:ch:grupy-abelowe\` (AA-08). Domknięcie i zagnieżdżenie wszystkich środowisk \`\\begin\`/\`\\end\` było poprawne.

## 6. Ograniczenia i bramka stabilizacyjna

**Wynik matematyczny:** w badanych zależnościach AA-16–AA-18 nie wykryto błędów wymagających korekty źródeł. Zatwierdzone pliki TeX pozostawiono bez zmian. Dwa odrębne zestawy testów wykonano **rzeczywiście lokalnie** i opublikowano z integrowaną kontrolą CI.

Nowy pełny przebieg walidacji książki AA-01–AA-42, obejmujący oba testy, jest uruchamiany z commitu \`5c441354a822f8bc079ee5616918c66f41fece85\`. **Nie uznajemy AA-X05 za finalnie stabilny, dopóki nie zostanie potwierdzone \`completed/success\`** dla dedykowanych testów, kompilacji całego PDF i kontroli odsyłaczy oraz przeprowadzona kontrola składu. Wyniki te należy dopisać do raportu po ich faktycznym uzyskaniu.
