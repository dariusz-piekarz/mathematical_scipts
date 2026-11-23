# Algebra abstrakcyjna — AA-X20: postać Smitha formy śladu i lokalizacja (AA-12 × AA-17 × AA-23)

**Data:** 2026-11-23. **Istniejąca gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Stan wejściowy:** AA-X19 zamknięty (6/6 testów, 97/97 kroków i zielona kontrola PDF, [CI 45213530134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45213530134)); indywidualne statusy AA-01–AA-50 bez zmian.
**Źródła przeczytane bezpośrednio:** AA-12 \`f64ec91a7fcc58557dba8b13f75b74f6b2ca788d\`; AA-17 \`07d654dab3b20ad7016d160b86914f541d8273a5\`; AA-23 \`69f5f2c35c3e7179055e0acc06fe95e041d0bc24\`. Zweryfikowano też aktualne \`AGENTS.md\`.

## 1. Istotnie nowa granica między rozdziałami

Audyt przekrojowy AA-X05 dotyczył modułów/Smitha/iloczynu tensorowego, a AA-X19 — wyróżnika formy śladu i wypadkowej. Niniejszy audyt bada inny problem: **co mówi postać Smitha całkowitej macierzy formy śladu o jej degeneracji modulo liczby pierwsze i o stawaniu się doskonałą po lokalizacji?**

Uwaga terminologiczna: w AA-23 niezdegenerowanie formy nad **ciałem** oznacza różnowartościowość odpowiadającego odwzorowania do przestrzeni funkcjonałów liniowych, automatycznie będącego izomorfizmem dla skończonego wymiaru. Nad \`\mathbb Z\` wyznacznik niezerowy daje jedynie różnowartościowość, **nie** surjektywność \`\mathbb Z^n\to\operatorname{Hom}_{\mathbb Z}(\mathbb Z^n,\mathbb Z)\`. O doskonałości formy całkowitej (izomorfizmie na moduł funkcjonałów) decyduje **odwracalność wyznacznika**, a nie sama jego niezerowość. Te dwa pojęcia nie zostały utożsamione.

## 2. Niezależne twierdzenie i dowód przez AA-12, AA-17 i AA-23

**Twierdzenie (o niezmiennikach Smitha i lokalizacji formy śladu).** Niech \`f\in\mathbb Z[X]\` będzie monicznym i nierozkładalnym nad \`\mathbb Q\` wielomianem stopnia \`n\ge1\`. Niech \`\alpha\` będzie jego pierwiastkiem, \`L=\mathbb Q(\alpha)\` oraz \`O=\mathbb Z[\alpha]\`. W bazie \`b=(1,\alpha,\ldots,\alpha^{n-1})\` określmy \`G=(\operatorname{Tr}_{L/\mathbb Q}(\alpha^{i+j}))_{0\le i,j<n}\in M_n(\mathbb Z)\`. Niech \`d_1,\ldots,d_n>0\`, \`d_i\mid d_{i+1}\`, będą współczynnikami postaci Smitha \`G\`. Dla dowolnej liczby pierwszej \`p\` oraz \`N\ge1\` zachodzą:

1. \`\det G=\operatorname{disc}(f)\ne0\`, \`|\det G|=\prod_i d_i\`, a \`\operatorname{coker}(G:\mathbb Z^n\to\mathbb Z^n)\cong\bigoplus_i\mathbb Z/(d_i)\` jest grupą skończoną rzędu \`|\det G|\`.
2. Dla redukcji \`\bar G\in M_n(\mathbb F_p)\` mamy \`\dim_{\mathbb F_p}\ker\bar G=\#\{i:p\mid d_i\}\`. W szczególności \`\bar G\` jest odwracalna wtedy i tylko wtedy, gdy \`p\nmid\operatorname{disc}(f)\`. Jest to twierdzenie o **redukcji formy śladu całkowitego rzędu**, a nie wprost o grupie Galois redukcji wielomianu.
3. Po lokalizacji \`\mathbb Z[1/N]\` odpowiadająca macierz \`G_N\` wyznacza doskonałe parowanie na \`O\otimes_{\mathbb Z}\mathbb Z[1/N]\` dokładnie wtedy, gdy **każdy** dzielnik pierwszy \`\operatorname{disc}(f)\` dzieli \`N\`. Równoważnie wszystkie \`d_i\` stają się jednostkami w \`\mathbb Z[1/N]\`.

**Dowód.** Moniczność \`f\` gwarantuje, że \`O\` jest wolnym \`\mathbb Z\`-modułem z podaną bazą: gdyby niezerowy wielomian całkowity stopnia \`<n\` zerował \`\alpha\`, przeczyłby minimalności \`f\` nad \`\mathbb Q\`, a każda potęga \`\alpha^k\` dla \`k\ge n\` redukuje się przy użyciu \`f(\alpha)=0\` do kombinacji całkowitej potęg niższych. Mnożenie przez element \`O\` w tej bazie ma macierz całkowitą, więc jego ślad jest całkowity i wszystkie \`G_{ij}\in\mathbb Z\`. Ponieważ charakterystyka \`\mathbb Q\` wynosi zero, \`f\` jest rozdzielczy. Wzór AA-23 przez zanurzenia daje macierz formy \`V^{\mathsf T}V\`, skąd \`\det G=\operatorname{disc}(f)\ne0\` (to samo przejście badano wcześniej w AA-X19).

Na mocy postaci Smitha z AA-17 istnieją \`U,V\in\operatorname{GL}_n(\mathbb Z)\` takie, że \`UGV=\operatorname{diag}(d_1,\ldots,d_n)\`, z ewentualnymi zmianami znaków przekątnych. \`U,V\` indukują izomorfizmy obrazów i ilorazów, stąd wskazany rozkład \`\operatorname{coker}G\`; iloczyn współczynników to wartość bezwzględna wyznacznika, która jest niezerowa. Macierze unimodularne pozostają odwracalne modulo \`p\`; po redukcji diagonalnej postaci Smitha jądro ma po jednym wymiarze dla każdego \`d_i\equiv0\pmod p\`. To dowodzi (2).

Dla \`S=\{N^k:k\ge0\}\` lokalizacja z AA-12 daje \`S^{-1}\mathbb Z=\mathbb Z[1/N]\`. Te same macierze \`U,V\` są odwracalne po lokalizacji, więc \`G_N\` jest odwracalna dokładnie wtedy, gdy każdy \`d_i\` jest jednostką w \`\mathbb Z[1/N]\`. Liczba całkowita niezerowa \`d\` jest jednostką w \`\mathbb Z[1/N]\` dokładnie wtedy, gdy wszystkie jej dzielniki pierwsze dzielą \`N\`: wystarczalność wynika z wielokrotności odpowiednich potęg w \`N^k\`; dla konieczności równość \`1/d=a/N^k\` implikuje \`da=N^k\` i podzielność każdego czynnika pierwszego \`d\` przez \`N\`. Z (1) i \`\prod d_i=|\det G|\` otrzymujemy (3). **Koniec dowodu.**

## 3. Niezależne modele i kontrprzykład interpretacyjny

Rachunki wykonano **dokładnie** nad \`\mathbb Z\` z \`SymPy\`, porównując macierze operatora mnożenia, wyróżniki wielomianowe, postacie Smitha i wyznaczniki. Dla \`G\` w kolejności bazy potęgowej:

| \`f(X)\` | \`G\` | \`(d_1,\ldots,d_n)\` | \`\det G\` | pierwsze dzielniki |
|---|---|---|---:|---|
| \`X^2-5\` | \`\mathrm{diag}(2,10)\` | \`(2,10)\` | \`20\` | \`2,5\` |
| \`X^2-2\` | \`\mathrm{diag}(2,4)\` | \`(2,4)\` | \`8\` | \`2\` |
| \`X^3-2\` | \`\begin{psmallmatrix}3&0&0\\0&0&6\\0&6&0\end{psmallmatrix}\` | \`(3,6,6)\` | \`-108\` | \`2,3\` |
| \`X^3-3X+1\` | \`\begin{psmallmatrix}3&0&6\\0&6&-3\\6&-3&18\end{psmallmatrix}\` | \`(3,3,9)\` | \`81\` | \`3\` |
| \`X^4-2\` | \`\begin{psmallmatrix}4&0&0&0\\0&0&0&8\\0&0&8&0\\0&8&0&0\end{psmallmatrix}\` | \`(4,8,8,8)\` | \`-2048\` | \`2\` |

Każdy zestaw współczynników Smitha skontrolowano niezależnie przez NWD wszystkich minorów kolejnych stopni, zgodnie z AA-17; rangi modulo \`2,3,5,7,11\` przez osobną eliminację Gaussa nad \`\mathbb F_p\`. Dla małych rozmiarów (\`n\le3\`, \`p\le5\`) liczebności jąder policzono również przez enumerację wszystkich wektorów. Warunek lokalizacji sprawdzono dla \`N\in\{1,2,3,5,6,10,15,30,210\}\`.

**Szczególnie ważny przypadek \`\mathbb Q(\sqrt5)\`.** Dla rzędu \`O=\mathbb Z[\sqrt5]\` forma śladu w bazie \`(1,\sqrt5)\` ma \`G=\operatorname{diag}(2,10)\`, wyróżnik \`20\` i degenerację modulo \`2\`. Tymczasem \`\beta=(1+\sqrt5)/2\` jest całkowity, ponieważ spełnia \`\beta^2-\beta-1=0\`; w większym rzędzie \`\mathbb Z[\beta]\` baza \`(1,\beta)\` ma macierz \`H=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\`, wyróżnik \`5\` i postać Smitha \`(1,5)\`. Macierz przejścia ma wyznacznik \`1/2\` i **nie** jest unimodularna nad \`\mathbb Z\`; indeks \`[\mathbb Z[\beta]:\mathbb Z[\sqrt5]]=2\`. Dlatego redukcja \`H\` modulo \`2\` jest odwracalna, choć \`G\bmod2\` jest zerowa. **Nie wolno uznawać dzielników wyróżnika dowolnego niemaksymalnego rzędu za automatyczny wykaz liczb pierwszych rozgałęziających się w całym ciele liczbowym.** Ta kontrola dotyczy różnicy między rzędami, bez założenia, że rozdział AA-23 omawia arytmetykę pierścienia wszystkich liczb całkowitych.

## 4. Trwała regresja, kontrole źródeł i granice

Dodano plik \`tools/tests/test_abstract_algebra_cross_aa12_17_23.py\` z **6 testami**:
1. dokładny rachunek macierzy Grama z operatora mnożenia i wyróżnika;
2. postać Smitha niezależnie kontrolowana ideałami minorowymi;
3. rangi modulo liczby pierwsze oraz jawne zliczanie jąder;
4. kryterium lokalizacji i jednostek \`\mathbb Z[1/N]\`;
5. dwie różne całkowite bazy/rzędy \`\mathbb Q(\sqrt5)\`;
6. źródłowe etykiety i odsyłacze AA-12, AA-17, AA-23.

Wykonano lokalnie **5/5 rachunkowych** testów \`ok\` (przy sprawdzaniu pierwszej wersji skryptu bez pełnego repozytorium); jedyny test źródłowy wymaga rzeczywistego checkoutu i nie jest w tej sesji przedstawiany jako potwierdzony. Liczniki źródłowe z bezpośredniego odczytu GitHub: **82 etykiety** (36+16+30) oraz **34 odsyłacze** (7+11+16) w trzech rozdziałach. Regresja weryfikuje ponadto unikatowość etykiet i istnienie celów na pełnym drzewie 50 rozdziałów; wynik potwierdzi dopiero GitHub Actions.

Uzupełniono \`.github/workflows/abstract-algebra-chapter.yml\` o wyzwalacz dla testu AA-X20 i osobny krok \`Run AA-X20 trace Smith localization crosschecks\`. Uruchomiony workflow: [45222177294](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45222177294), commit \`497ea71f410eb02037430c8e2810f3dcf687491d\`. Przy otwarciu raportu: \`in_progress\`; nie ma jeszcze podstaw do zatwierdzenia pełnej stabilizacji.

**AA-X20: W AUDYCIE / STABILIZACJI CI.** W kontrolowanym zakresie nie wykryto sprzeczności między zatwierdzonymi rozdziałami. Nie zmieniano żadnego źródła AA-01–AA-50. Nowe teoretyczne połączenie może zostać zaproponowane do dodania po AA-17 jako przykład zastosowania postaci Smitha, jednak nie wstawiano go automatycznie bez zgody użytkownika.

**Bramka zamknięcia:** zweryfikować \`6/6\` testów \`ok\`, zakończony sukcesem cały workflow, kompilację pełnego tomu przez \`latexmk\`, a także kontrolę PDF i odsyłaczy. Sama kompilacja nie oznacza niezależnych oględzin wizualnych stron.

## 5. Zamknięcie AA-X20 po pełnej weryfikacji CI

**AA-X20: ZAMKNIĘTY — PASS w określonym zakresie przekrojowym.** Niezależnie od wcześniejszych pięciu lokalnych testów rachunkowych odczytano ostateczny wynik [GitHub Actions 45222177294](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45222177294) dla dokładnie \`497ea71f410eb02037430c8e2810f3dcf687491d\`. Przebieg ma \`completed / success\`; job \`validate-cli\` — **98/98 kroków ukończonych**, bez awarii.

Z rzeczywistego logu jobu \`137859065780\` zweryfikowano wszystkie **6/6 testów AA-X20 = ok** — każdy zarówno w globalnym odkrywaniu testów, jak i w kroku \`Run AA-X20 trace Smith localization crosschecks\`. W szczególności na pełnym checkoutcie przeszedł test unikatowości etykiet całej 50-rozdziałowej książki oraz 34 odsyłaczy trzech badanych rozdziałów.

\`Compile AA-01 to AA-50 book with latexmk\`: **success**. \`Verify PDF and references (no undefined refs)\`: **success**. Przesłano artefakt \`abstract-algebra-aa01-aa50\`, ID \`14842500747\`, ZIP **2 289 390 B**. Nie wykonano odrębnej wizualnej inspekcji poszczególnych stron PDF; kompilacja i automatyczna kontrola odsyłaczy nie są z nią utożsamiane.

**Werdykt:** w badanych zależnościach nie wykryto błędu matematycznego wymagającego zmiany zatwierdzonych rozdziałów. Dowód twierdzenia przekrojowego i modele skończone są odrębnymi warstwami uzasadnienia; testy nie stanowią formalizacji w Lean. **Treść AA-01–AA-50 i ich historyczne statusy pozostały bez zmian; AA-51 nie otwierano.** Opcjonalny nowy przykład Smith–lokalizacja–forma śladu pozostaje propozycją do decyzji użytkownika.
