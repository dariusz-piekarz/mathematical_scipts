# AA-X08 — audyt przekrojowy AA-19–AA-24: konstrukcje ciał, teoria Galois, ślad, norma, pierwiastniki

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; **istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6`.

## 1. Kontrolowany zakres i źródła

| Rozdział | Zakres dowodów | SHA Git blob |
|---|---|---|
| AA-19 | Konstrukcja ciała ułamków, własność uniwersalna, charakterystyka i Frobenius | `344b191306257f7a3c4ced24d0ef561cbcae1ac4` |
| AA-20 | Rozszerzenia skończone, wielomian minimalny, ciało rozkładu, rozdzielczość | `8aa1aedc2c07fe032527d2a0b276cf50b0a6dbfd` |
| AA-21 | Przedłużanie zanurzeń, normalność, ciała skończone i ich automorfizmy | `ef1f7e0be18ea612e3ee9dd38df4be84c853b400` |
| AA-22 | Twierdzenie Artina i podstawowe twierdzenie teorii Galois | `f85f71d7121b986b610558db164c2ee0816e200e` |
| AA-23 | Ślad, norma, wyróżnik, wzory przez zanurzenia i przechodniość w wieży | `69f5f2c35c3e7179055e0acc06fe95e041d0bc24` |
| AA-24 | Rozwiązywalność przez pierwiastniki, grupy rozwiązalne, twierdzenie Abela–Ruffiniego | `f492d30a03a19e256001d0a983dd29a9ddde39bb` |

Wszystkie oryginalne pliki TeX pozostały **niezmienione**. Audyt AA-X08 weryfikuje przejścia między rozdziałami i sprawdza konkretne modele niezależnymi obliczeniami. Nie jest równoważny formalizacji w Lean ani nie zastępuje już wykonanych audytów pojedynczych rozdziałów.

## 2. Kontrola założeń i przejść dowodowych

### AA-19 → AA-20: od ciała ułamków do prostego rozszerzenia

W AA-19 równoważność ułamków ((a,b)sim(c,d)Longleftrightarrow ad=bc) zakłada **dziedzinę całkowitości**, a dowód przechodniości skraca niezerowy czynnik. To założenie jest istotne: bez niego należy stosować bardziej ogólną relację lokalizacyjną z AA-12. Własność uniwersalna wymaga **różnowartościowości** (R\to L), ponieważ mianowniki muszą przejść na elementy odwracalne. AA-19 wyraźnie odróżnia te przypadki.

AA-20 konstruuje (K(\alpha)\cong K[X]/(m_{\alpha,K})) po ustaleniu, że wielomian minimalny jest nierozkładalny. Dopiero nierozkładalność zapewnia, że otrzymany iloraz jest ciałem. Twierdzenie o wieży ma dokładnie założenia ([E:K],[L:E]<\infty); dowód przez iloczyny baz sprawdza zarówno rozpinanie, jak i niezależność. Przykład (X^p-t\in\mathbb F_p(t)[X]) wyraźnie oddziela **nierozkładalność** od **rozdzielczości**.

### AA-20 → AA-21 → AA-22: ciała rozkładu, automorfizmy i odpowiedniość Galois

W AA-21 istnienie (\mathbb F_{p^n}) wynika z rozdzielczego wielomianu (X^{p^n}-X), a grupa Galois jest generowana przez Frobeniusa rzędu dokładnie (n). Dowód wyklucza niższy rząd, gdyż wielomian (X^{p^r}-X) dla (r<n) ma stopień mniejszy niż liczność całego ciała.

W AA-22 twierdzenie Artina o ciele elementów stałych nie zakłada z góry skończoności ([L:L^G]): najpierw wyprowadza ograniczenie (\le |G|) z minimalnego niezerowego rozwiązania układu równań i jego niezmienniczości, a potem nierówność odwrotną przez niezależność różnych automorfizmów ciała. W podstawowym twierdzeniu teorii Galois sprawdzono obie strony odpowiedniości (E\leftrightarrow H), odwracanie inkluzji, formuły ([L:E]=|H|), ([E:K]=[G:H]) oraz rozróżnienie normalności (E/K) od normalności (L/E). Nie można automatycznie przypisać normalności dowolnemu ciału pośredniemu; w tekście założenie (H\triangleleft G) jest jawne.

### AA-21/22 → AA-23: ślad i norma

AA-23 **definiuje** ślad i normę jako ślad i wyznacznik (K)-liniowego operatora mnożenia; formuły jako suma i iloczyn obrazów przez zanurzenia dotyczą tylko rozszerzeń **rozdzielczych**. Natomiast przechodniość
[
\operatorname{Tr}_{L/K}=\operatorname{Tr}_{F/K}\circ\operatorname{Tr}_{L/F},\qquad
N_{L/K}=N_{F/K}\circ N_{L/F}
]
jest poprawnie sformułowana dla wszystkich skończonych wież, również nierozdzielczych, i dowiedziona przez bloki macierzy po ograniczeniu skalarów.

Sprawdzono osobno znak w formule dla wielomianu minimalnego (m_{\alpha,K}=T^n+a_{n-1}T^{n-1}+\cdots+a_0):
[
\operatorname{Tr}_{K(\alpha)/K}(\alpha)=-a_{n-1},
\qquad N_{K(\alpha)/K}(\alpha)=(-1)^n a_0.
]
Dla (a\in L\supseteq K(a)) stopień ([L:K(a)]) występuje jako krotność wielomianu minimalnego w wielomianie charakterystycznym. To zabezpiecza przed błędnym pominięciem krotności. W przykładach ciał skończonych rozdzielczość wynika z faktu, że rozszerzenia (\mathbb F_{p^n}/\mathbb F_p) są Galois.

### AA-22/23 → AA-24: pierwiastniki i grupy rozwiązalne

Kryterium rozwiązywalności przez pierwiastniki w AA-24 jest sformułowane nad ciałem **charakterystyki zero**. Dowód odróżnia wieżę przez pierwiastniki od wieży rozszerzeń Galois: dopiero po dołączeniu potrzebnych pierwiastków z jedynki konstruowane są kolejne rozszerzenia z abelowymi grupami Galois.

Dla konkretnego wielomianu (f=X^5-4X+2) kontrolowano trzy niezależne ogniwa:
1. nierozkładalność przez kryterium Eisensteina przy (2);
2. dokładnie trzy pierwiastki rzeczywiste (pochodna (5x^4-4) ma dwa rzeczywiste zera i ekstremalne wartości odpowiednich znaków);
3. przechodnia podgrupa (S_5) zawierająca transpozycję jest całą (S_5), ponieważ graf jej sprzężonych transpozycji ma składowe tej samej liczności dzielącej (5).

Wniosek o nierozwiązywalności wykorzystuje fakt, że (S_5\) nie jest grupą rozwiązalną; nie należy mylić tego z brakiem rozwiązań równania ani z twierdzeniem, że *każdy* wielomian stopnia pięć jest nierozwiązywalny przez pierwiastniki. Obie subtelności są poprawnie ujęte w AA-24.

## 3. Pierwszy test niezależny: algebra ilorazowa i Frobenius

**Nowy plik:** `tools/tests/test_abstract_algebra_cross_aa19_24.py`. **Wynik wykonania lokalnego:** **2136/2136 PASS**.

Test **nie używa SymPy**. Samodzielnie buduje ciała (\mathbb F_{p^n}) jako ilorazy (\mathbb F_p[T]/(f)), wyszukuje nierozkładalne wielomiany przez dzielenie z resztą oraz wykonuje arytmetykę w bazie (1,T,\ldots,T^{n-1}). Zbadano osiem par:
[
(p,n)\in\{(2,2),(2,3),(2,4),(2,6),(3,2),(3,3),(3,4),(5,2)\}.
]

Dla wszystkich elementów porównano:
- ślad i normę policzone z macierzy mnożenia przez eliminację modularną;
- te same wielkości wyliczone niezależnie jako sumę i iloczyn sprzężeń Frobeniusa;
- surjektywność śladu oraz normy na grupie niezerowych elementów;
- niezdegenerowanie parowania (\operatorname{Tr}(ab)) w badanych modelach;
- liczbę elementów ciała stałego (\operatorname{Fix}(\mathrm{Fr}^d)) dla każdego (d\mid n), jego zamkniętość na działania, rozmiar odpowiadającej grupy automorfizmów;
- oba wzory przechodniości w rzeczywistych wieżach (\mathbb F_p\subseteq\mathbb F_{p^d}\subseteq\mathbb F_{p^n}).

| Grupa kontroli | Liczba |
|---|---:|
| Ślad = suma Frobeniusa | 234 |
| Norma = wyznacznik mnożenia | 234 |
| Surjektywność śladu i normy | 16 |
| Niezdegenerowanie parowania śladu | 226 |
| Ciała elementów stałych i grupy Galois | 40 |
| Przechodniość śladu | 693 |
| Przechodniość normy | 693 |
| **Łącznie** | **2136** |

## 4. Drugi test niezależny: grupy pochodne i konkretne równanie piątego stopnia

**Nowy plik:** `tools/tests/test_abstract_algebra_cross_aa19_24_confirming.py`. **Wynik wykonania lokalnego:** **22 656/22 656 PASS**.

Model ten nie używa arytmetyki ilorazowych ciał skończonych. Jego punktem wyjścia są jawne permutacje:
- pełne grupy (S_3,S_4,S_5);
- iloczyny, odwrotności i wszystkie komutatory elementów;
- rzeczywiście wyznaczane podgrupy pochodne (domknięcia podgrup generowanych przez komutatory).

Odtworzono kolejno:
[
S_3\supset A_3\supset\{1\},\quad
S_4\supset A_4\supset V_4\supset\{1\},\quad
S_5\supset A_5=A_5',
]
co wyraźnie oddziela rozwiązalność (S_3,S_4) od nierozwiązalności (S_5).

Niezależnie wygenerowano **wszystkie 24 pięciocykle** i **wszystkie 10 transpozycji** pięciu elementów. W każdym z 240 przypadków podgrupa przez nie generowana miała dokładnie 120 elementów, potwierdzając kombinatoryczne ogniwo dowodu AA-24.

Dla (X^5-4X+2) sprawdzono nierozkładalność w (\mathbb Q[X]), dokładną liczbę rzeczywistych pierwiastków metodą izolujących przedziałów wymiernych, brak wielokrotnych pierwiastków i faktoryzacje wielomianu modulo liczb pierwszych (3,5,7,11,13,17,19,23,29) jako osobny test typów cykli Frobeniusa.

| Grupa kontroli | Liczba |
|---|---:|
| Wszystkie pary do obliczania komutatorów | 22 381 |
| Liczności kolejnych grup pochodnych | 11 |
| Pięciocykle i transpozycje generują (S_5) | 240 |
| Nierozkładalność, pierwiastki rzeczywiste, redukcje modulo (p) | 24 |
| **Łącznie** | **22 656** |

**Dwa osobne zestawy: 24 792/24 792 PASS.** Liczby reprezentują konkretne sprawdzenia i pary grupowe, nie liczbę niezależnych dowiedzionych twierdzeń.

## 5. Struktura LaTeX i odsyłacze

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-19 | 20 | 6 | 9 | 5 |
| AA-20 | 25 | 11 | 12 | 7 |
| AA-21 | 20 | 18 | 10 | 5 |
| AA-22 | 12 | 21 | 5 | 4 |
| AA-23 | 30 | 16 | 11 | 7 |
| AA-24 | 23 | 16 | 9 | 3 |
| **Razem** | **130** | **88** | **56** | **31** |

Wszystkie **130 etykiet są unikatowe**; **88** odsyłaczy wskazuje na istniejące cele. Siedem celów zewnętrznych potwierdzono wprost w rozdziałach AA-05, AA-11 i AA-17:
`aa:tw:eisenstein`, `aa:wn:abelian-fg-structure`, `aa:ch:szeregi`, `aa:tw:solvable-series`, `aa:lem:solvable-extension`, `aa:tw:a5-simple`, `aa:wn:a5-not-solvable`. Wszystkie wystąpienia środowisk `\begin{...}` i `\end{...}` są poprawnie zagnieżdżone, a główny plik książki dołącza AA-19–AA-24.

## 6. Zapis i warunki stabilności

Nowe testy zapisano na dotychczasowej gałęzi:
- `tools/tests/test_abstract_algebra_cross_aa19_24.py`, commit `14e72f634e75050047f1cd9afd459880bf0a548b`;
- `tools/tests/test_abstract_algebra_cross_aa19_24_confirming.py`, commit `81380f358a993113d54faf96df2723c6a9eb0623`;
- oba kroki CI i ich wyzwalacze dodano do `.github/workflows/abstract-algebra-chapter.yml`, commit `283f1bb2e2382e880c7282c5443f60f5fc507b4f`.

Odtworzenie testów:

```bash
python tools/tests/test_abstract_algebra_cross_aa19_24.py
python tools/tests/test_abstract_algebra_cross_aa19_24_confirming.py
```

Przeprowadzono lokalnie kontrolę składu **wszystkich 36 stron** AA-19–AA-24, na podstawie ostatniego wcześniej zakończonego z sukcesem artefaktu PDF, włączając rysunek AA-24. Oględziny nie ujawniły widocznych kolizji i ucięć. Dopiero potwierdzony wynik nowego GitHub Actions oraz porównanie z pobranym z niego artefaktem PDF pozwalają oznaczyć bieżącą iterację jako ostatecznie stabilną.

**Wstępny werdykt merytoryczny:** nie stwierdzono konieczności zmian sześciu plików źródłowych. **AA-X08 nie zostaje jeszcze uznany za zamknięty**, dopóki jego nowe testy, pełna kompilacja książki i rzeczywisty artefakt nie przejdą potwierdzonych kontroli końcowych.
