# AA-X24 — niezależny audyt przekrojowy AA-11 → AA-28: kryterium Eisensteina i wielomiany cyklotomiczne potęg liczb pierwszych

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD odczytany ponownie bezpośrednio przed zapisem:** `c9d64b59609da87a8638392f293a4494128b3427`.

## Stan i zakres

W aktualnym katalogu `chapters/pl/abstract_algebra` jest 50 źródeł AA-01–AA-50; AA-51 nie istnieje. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, `books/pl/abstract_algebra.tex` oraz listę wcześniejszych raportów. Audyt X24 jest odrębny od X04 (wyróżniki i wypadkowe) i X10 (Gauss/Eisenstein w ogólnej sytuacji): dotyczy **interfejsu** kryterium Eisensteina AA-11 z konstrukcją `Phi_n` AA-28, szczególnie podstawienia `X↦X+1` dla `n=p^k`.

Źródła: AA-11 blob `62eb6a239ddcae2958c10b923b50a30dcb528ecc` (818 wierszy); AA-28 blob `2e24a69608aeab7856acf40f882480a97eb455bc` (328 wierszy). Nie zmieniono zatwierdzonych rozdziałów.

## Kontrola matematyczna

1. AA-11 podaje kryterium Eisensteina nad dziedziną z jednoznacznym rozkładem: `p∤a_n`, `p|a_j` dla `j<n`, `p²∤a_0`. AA-28 konstruuje moniczne `Phi_n∈Z[X]` i dowodzi nierozkładalności nad `Q` niezależnym argumentem modularnym. Hipotezy są zgodne; zastosowanie Eisensteina **po przesunięciu argumentu** nie wymaga dopisania nowego twierdzenia do zatwierdzonego tekstu.
2. Dla liczby pierwszej `p` i `k≥1` zachodzi `Phi_{p^k}(X)=Σ_{j=0}^{p-1}X^{jp^{k-1}}` oraz `Phi_{p^k}(X)≡(X-1)^{φ(p^k)} (mod p)`. Zatem `Phi_{p^k}(X+1)≡X^{φ(p^k)} (mod p)`. Jest moniczny, a jego wyraz wolny `Phi_{p^k}(1)=p`; spełnia więc wszystkie warunki Eisensteina przy `p`. Ponieważ podstawienie `X↦X+1` jest automorfizmem `Q[X]`, nierozkładalność wielomianu przesuniętego implikuje nierozkładalność oryginału. To **niezależna kontrola matematyczna** dla rodziny potęg liczb pierwszych, nie dowód nierozkładalności wszystkich `Phi_n` na tej drodze.
3. Przypadki brzegowe: `p=2,k=1` daje `Phi_2(X+1)=X+2`; `p=2,k=3` daje `(X+1)^4+1`, stały wyraz 2. Dla `n=1` nie ma pierwszej `p` w formule i należy korzystać z `Phi_1=X-1`. Dla ogólnego `n` złożonego z różnych liczb pierwszych nie wolno bez dowodu stosować tego samego argumentu (np. `Phi_6(X+1)=X²+X+1`, wyraz wolny 1).
4. Rachunek niezależny w Python/SymPy, wykonany **w bieżącym uruchomieniu**: dla `p∈{2,3,5,7,11}`, `1≤k≤3` i `φ(p^k)≤120` zweryfikowano dokładnie **13/13** wielomianów: moniczność, podzielność wszystkich niewiodących współczynników przez `p`, wyraz wolny równy `p`, brak podzielności tego wyrazu przez `p²` oraz stopień `φ(p^k)`. To test skończonej rodziny, nie zamiennik ogólnego dowodu powyżej.
5. Struktura: AA-11 ma 37 etykiet, 18 odsyłaczy, 19 środowisk dowodu i 11 przykładów; AA-28 ma 10 etykiet, 6 odsyłaczy, 4 dowody i 2 przykłady. **47 etykiet unikatowych**, 24 odsyłacze; wszystkie 6 celów zewnętrznych odczytano bezpośrednio w AA-09, AA-10, AA-19, AA-26. Nie stwierdzono duplikatu etykiet w parze. Kontrola ta nie jest pełną kontrolą wszystkich etykiet całej książki.

## Statusy niezależne

- **Matematyka (ściśle wybrany interfejs AA-11/AA-28):** 13/13 dokładnych testów PASS, dodatkowy ogólny argument opisany powyżej; nie wykryto błędu w badanym interfejsie. Nie deklaruje się pełnego przeglądu 23 dowodów.
- **Terminologia, odsyłacze i skład źródeł:** zgodność sprawdzonych sformułowań; 47 etykiet bez duplikatów, 24 odsyłacze z odnalezionymi celami. Brak zmian źródeł, więc licznik czystych audytów nie jest resetowany.
- **Nowa kompilacja LaTeX:** NIE WYKONANO. **Wizualna inspekcja PDF:** NIE WYKONANO. **Nowy CI na tym HEAD:** NIE URUCHOMIONO / NIEZWERYFIKOWANO. Nie wolno przenosić wcześniejszego zielonego CI na nowy audyt.
- **Stabilność:** ten raport nie stanowi nowej deklaracji stabilności całego tomu.

## Propozycja (bez wprowadzania do źródeł)

Opcjonalnie w AA-28 po dowodzie nierozkładalności dodać przykład alternatywnego zastosowania kryterium Eisensteina do `Phi_{p^k}(X+1)`; wymaga odrębnej zgody, gdyż jest to nowe uzupełnienie zatwierdzonego rozdziału.

**Następny krok:** ponownie sprawdzić HEAD i istnienie AA-51; jeśli nadal brak, wybrać nową, niepowtórzoną kontrolę przekrojową i przeprowadzić ją w osobnym numerowanym raporcie. Przy dostępie do artefaktów CI wykonać osobną inspekcję PDF i weryfikację workflow.

## Kontynuacja AA-X24 — pełne uogólnienie, testy trwałe i bramka CI

Uzupełniono dotychczasowy raport o niezależny dowód ogólny i **7 trwałych testów**. Źródła AA-11 i AA-28 nie zostały zmienione. Weryfikacja obejmuje 50 rozdziałów przy kontrolowaniu etykiet i odsyłaczy.

### 1. Wartość wielomianu cyklotomicznego w punkcie 1

**Twierdzenie.** Dla każdego \(n\ge2\) zachodzi
\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\quad p\text{ pierwsza},\ k\ge1,\\
1,&n\text{ nie jest potęgą liczby pierwszej}.
\end{cases}
\]
Dla \(n=1\) mamy natomiast \(\Phi_1(1)=0\).

**Dowód.** Dla \(n=p^k\) wzór
\(\Phi_{p^k}(X)=1+X^{p^{k-1}}+\cdots+X^{(p-1)p^{k-1}}\)
daje bezpośrednio \(\Phi_{p^k}(1)=p\).
Dla ogólnego \(n>1\) z AA-28 wynika
\((X^n-1)/(X-1)=\prod_{d\mid n,\ d>1}\Phi_d(X)\).
Wstawiając \(X=1\) (do wielomianu ilorazowego, nie do nieokreślonej wartości \(0/0\)), otrzymujemy
\(n=\prod_{d\mid n,\ d>1}\Phi_d(1)\).
Przeprowadźmy indukcję po \(n\). Jeśli \(n\) nie jest potęgą jednej liczby pierwszej, wśród jego właściwych dzielników pierwsze potęgi mają postać \(p^j\), gdzie \(1\le j\le v_p(n)\). Iloczyn ich wartości w \(1\), obliczonych w pierwszym kroku, jest równy
\(\prod_{p\mid n}p^{v_p(n)}=n\).
Wszystkie pozostałe właściwe dzielniki \(d>1\) również nie są potęgami jednej liczby pierwszej, więc na mocy założenia indukcyjnego ich \(\Phi_d(1)=1\). Ponieważ \(\Phi_n(1)\) jest liczbą całkowitą i iloczyn całkowitych wartości dla właściwych dzielników już wynosi \(n\), otrzymujemy \(\Phi_n(1)=1\). Dla \(n=1\) z definicji \(\Phi_1=X-1\), zatem wartość wynosi \(0\). **Koniec dowodu.**

**Konsekwencja.** Dla \(n>1\), które nie jest potęgą liczby pierwszej, przesunięcie \(\Phi_n(X+1)\) ma wyraz wolny \(1\), więc **nie spełnia kryterium Eisensteina względem żadnej liczby pierwszej** w tej konkretnej postaci. Nie przeczy to nierozkładalności \(\Phi_n\) nad \(\mathbb Q\), udowodnionej ogólnie w AA-28. Na przykład \(\Phi_6(X+1)=X^2+X+1\).

### 2. Uogólnienie na dowolną liczbę \(n\) podzielną przez \(p\)

**Twierdzenie.** Niech \(p\) będzie liczbą pierwszą, \(n=p^k m\), \(k\ge1\), \(\gcd(m,p)=1\), \(m\ge1\). W \(\mathbb F_p[X]\) zachodzi
\[
\overline{\Phi_n}(X)=\overline{\Phi_m}(X)^{\,\varphi(p^k)}
\quad\text{gdzie}\quad\varphi(p^k)=p^{k-1}(p-1).
\]
W szczególności \(\overline{\Phi_n}\) jest bez powtórzonych czynników **dokładnie wtedy**, gdy \(p=2\) i \(k=1\).

**Dowód.** W charakterystyce zero pierwiastki wielomianu \(\Phi_m(X^{p^k})\) są dokładnie pierwiastkami z jedynki rzędu \(mp^j\) dla \(0\le j\le k\). Rzeczywiście, jeśli \(z^{p^k}\) ma rząd dokładnie \(m\) względnie pierwszy z \(p\), to rząd \(z\) ma część pierwszą do \(p\) równą \(m\), a część \(p\)-potęgową \(p^j\) z \(j\le k\); i odwrotnie każda taka liczba spełnia warunek. Pierwiastki są proste, a obie strony moniczne. Dlatego
\[
\Phi_m(X^{p^k})=\prod_{j=0}^k \Phi_{mp^j}(X).
\]
Dzieląc przez analogiczną tożsamość dla \(k-1\), otrzymujemy
\(\Phi_m(X^{p^k})=\Phi_m(X^{p^{k-1}})\Phi_{mp^k}(X)\).
Współczynniki są całkowite. Redukując modulo \(p\) i stosując tożsamość Frobeniusa, dostajemy
\(\overline{\Phi_m}(X)^{p^k}=\overline{\Phi_m}(X)^{p^{k-1}}\overline{\Phi_n}(X)\).
Moniczny wielomian \(\overline{\Phi_m}\) jest niezerowy, więc możemy go skrócić w dziedzinie \(\mathbb F_p[X]\); stąd \(\overline{\Phi_n}=\overline{\Phi_m}^{p^k-p^{k-1}}\).

Ponieważ \(p\nmid m\), pochodna \(X^m-1\) jest względnie pierwsza z \(X^m-1\) w \(\mathbb F_p[X]\). Wielomian \(\overline{\Phi_m}\) jest jego monicznym dzielnikiem na mocy tożsamości cyklotomicznej redukowanej modulo \(p\), więc również jest bez powtórzonych czynników. Jego dodatnia potęga jest bez powtórzonych czynników wtedy i tylko wtedy, gdy wykładnik \(\varphi(p^k)\) wynosi \(1\), a to zachodzi dokładnie dla \(p=2,k=1\). **Koniec dowodu.**

Jest to ważny przypadek brzegowy: **nie każda liczba pierwsza dzieląca \(n\) jest złą liczbą pierwszą dla \(\Phi_n\)**. Dla \(n=6\) i \(p=2\) otrzymujemy \(\overline{\Phi_6}=X^2+X+1\), wielomian rozdzielczy, mimo że \(2\mid6\). Dla \(n=8,p=2\) otrzymujemy \(\overline{\Phi_8}=(X-1)^4\), więc redukcja jest nierozdzielcza.

### 3. Zautomatyzowana kontrola dokładna

Dodano plik tools/tests/test_abstract_algebra_cross_aa11_28.py z **7 testami**:
1. trzynaście modeli \(p^k\) i wszystkie współczynniki kryterium Eisensteina po przesunięciu;
2. tożsamość \(\prod_{d\mid n}\Phi_d=X^n-1\) dla \(1\le n\le45\) i algebraiczne odwrócenie przesunięcia;
3. kompletną kontrolę \(\Phi_n(1)\) dla \(1\le n\le100\), z przypadkami nienależącymi do potęg liczb pierwszych;
4. ogólne równanie \(\overline{\Phi_{mp^k}}=\overline{\Phi_m}^{\varphi(p^k)}\) dla \(2\le n\le85\), dla każdej liczby pierwszej \(p\mid n\), wraz z wymiarem NWD wielomianu i jego pochodnej;
5. niezależny wzór dwumianowy na wszystkie współczynniki \(\Phi_{p^k}(X+1)\), bez użycia bezpośredniego rozwijania wielomianu cyklotomicznego;
6. przypadki brzegowe \(n=1,2,6,8\) i jednostronność kryterium Eisensteina;
7. globalną zgodność etykiet i odsyłaczy w 50 rozdziałach, w tym **47 etykiet i 24 odsyłacze** badanej pary.

Podłączono plik do wyzwalacza i osobnego kroku Run AA-X24 Eisenstein and prime-power cyclotomic crosschecks w .github/workflows/abstract-algebra-chapter.yml. **Bramka:** [GitHub Actions 45247774608](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45247774608), commit 902a93fe7da2c839f6ce898e083fab8177667473. Na etapie wpisania tego uzupełnienia przebieg był w toku; wynik można zatwierdzić dopiero po 7/7 pozytywnych testach, całym zakończonym workflow, sukcesie kompilacji AA-01–AA-50 i automatycznej kontroli PDF/odsyłaczy.

**Wstępny werdykt:** nie wykryto matematycznego błędu wymagającego zmiany zatwierdzonych źródeł. Wskazane dwa twierdzenia są opcjonalnym rozszerzeniem tekstu AA-28, pozostawionym do decyzji użytkownika, a nie zmianą w rozdziałach. Nie utożsamiamy kompilacji i sprawdzenia ostrzeżeń w logu z niezależną wizualną kontrolą stron PDF. Testy nie są formalną weryfikacją Lean.

## Zamknięcie AA-X24 — stabilizacja PASS i zapis nieudanej próby

**Pierwsza próba:** [GitHub Actions 45247774608](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45247774608), commit 902a93fe7da2c839f6ce898e083fab8177667473 — **failure**, wyłącznie w globalnym uruchomieniu regresji, przed osobnym krokiem AA-X24 i przed kompilacją LaTeX. Log potwierdził **34 nieudane podprzypadki** testu test_general_modp_prime_part_cyclotomic_identity. Przyczyną było błędne oczekiwanie \(\deg\gcd(g,g')=(e-1)\deg h\) przy \(g=h^e\in\mathbb F_p[X]\) także dla \(p\mid e\). Jeżeli \(p\mid e\), pochodna \(g'\) jest identycznie zerowa i \(\gcd(g,g')=g\), więc poprawna wartość wynosi \(e\deg h\), nie \((e-1)\deg h\). Jeżeli \(p\nmid e\) oraz \(h\) jest bez powtórzonych czynników, wtedy \(\gcd(g,g')=h^{e-1}\). Błąd dotyczył regresji, a nie sformułowanego twierdzenia o redukcji. Poprawiono go w commicie **52e61f76fe7e507b2f36ff634b7bc2586d2d0650**. Nie zmieniono źródeł AA-11 i AA-28.

**Powtórzona walidacja:** [GitHub Actions 45248127387](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45248127387), dokładnie commit 52e61f76fe7e507b2f36ff634b7bc2586d2d0650 — **completed / success**. Job validate-cli ID **137950221561**, **102/102 ukończone kroki**, bez awarii. Rzeczywisty log potwierdza **7/7 nowych testów AA-X24 jako ok**, każdy zarówno w globalnym odkrywaniu testów, jak i w osobnym kroku Run AA-X24 Eisenstein and prime-power cyclotomic crosschecks.

**LaTeX i referencje:** kroki Compile AA-01 to AA-50 book with latexmk oraz Verify PDF and references (no undefined refs) zakończone **success**. Artefakt abstract-algebra-aa01-aa50: ID **14854444663**, ZIP **2 289 387 bajtów**. Nie wykonano odrębnej wizualnej inspekcji stron PDF; automatyczna kompilacja i sprawdzenie odsyłaczy nie są z nią utożsamiane.

**Werdykt AA-X24: ZAMKNIĘTY / STABILNY w badanym zakresie AA-11 × AA-28.** Nie ujawniono usterki matematycznej wymagającej modyfikacji zatwierdzonych rozdziałów. Wyniki ogólne zostały udowodnione matematycznie; ich przykłady, modele arytmetyczne i regresje są osobnymi kontrolami, a nie formalizacją w Lean. Źródła AA-01–AA-50 oraz historyczne statusy pozostają niezmienione; AA-51 nie otwierano. Dwa opcjonalne uzupełnienia przedstawiono do decyzji użytkownika, bez automatycznego wprowadzania ich do tekstu.

**Następny zakres:** dopiero po tym zamknięciu można rozpocząć AA-X25 jako nowy, niepowtórzony audyt przekrojowy.
