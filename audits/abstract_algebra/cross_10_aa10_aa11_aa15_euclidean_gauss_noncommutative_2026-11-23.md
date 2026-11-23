# AA-X10 — audyt przekrojowy AA-10, AA-11, AA-15

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; **gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Zakres i niezmienione źródła

| Rozdział | Obszar | Git blob SHA |
|---|---|---|
| AA-10 | Dziedziny euklidesowe, dziedziny ideałów głównych, rozkład na czynniki | `dc78db8e24255ef0bdc3a17289f31a19842ea15b` |
| AA-11 | Wielomiany, lemat Gaussa, kryterium Eisensteina, redukcja modulo \(p\) | `62eb6a239ddcae2958c10b923b50a30dcb528ecc` |
| AA-15 | Pierścienie nieprzemienne, ideały macierzowe, algebry grupowe i wolne pierścienie | `b055965112ca86a86e6d0a88213a8274b9d09a68` |

Wszystkie oryginalne pliki matematyczne pozostawiono bez zmian. To nowa kontrola zależności między AA-10/11 a AA-15, a nie powtórzenie audytów indywidualnych rozdziałów.

## Audyt matematyczny i ryzyka

### AA-10 → AA-11

- W implikacji „dziedzina euklidesowa \(\Rightarrow\) dziedzina ideałów głównych” minimalizuje się normę euklidesową **niezerowego elementu ideału**, nie wykonuje dzielenia przez zero. Algorytm Euklidesa musi zakończyć się po skończonej liczbie ściśle malejących wartości normy, a NWD jest jednoznaczny tylko z dokładnością do stowarzyszenia.
- Dowód „PID \(\Rightarrow\) UFD” rozdziela istnienie rozkładu (stabilizacja wstępujących ciągów ideałów) od jego jednoznaczności (nierozkładalny jest pierwszy). W AA-11 lemat Gaussa używa właśnie założenia, że współczynniki należą do **dziedziny z jednoznacznym rozkładem**; bez niego redukcja przez element pierwszy i usuwanie mianowników nie miałyby tego samego uzasadnienia.
- Zawartość \(c(f)\) jest określona z dokładnością do stowarzyszenia; wzór \(c(fg)\sim c(f)c(g)\) nie jest prawem dla wszystkich dowolnych pierścieni. Sprawdzono szczególny przypadek dodatniej zawartości wielomianów całkowitych i wielomianów stałych.
- W kryterium nierozkładalności przez redukcję modulo \(p\) wymagane jest \(p\nmid\operatorname{lc}(f)\). Bez tego warunku kontrprzykład z tekstu \(f=(2x+1)(x+1)=2x^2+3x+1\) redukuje się modulo \(2\) do liniowego, nierozkładalnego \(x+1\), chociaż \(f\) jest rozkładalny nad \(\mathbb Q\).
- Kryterium Eisensteina osobno wymaga \(p\nmid a_n\), \(p\mid a_i\) dla \(i<n\) i \(p^2\nmid a_0\). Nie utożsamiono jego dowodu z wystarczającym warunkiem dla każdej redukcji modulo \(p\).
- Konstrukcja ciała ułamków w AA-11 wykorzystuje **brak dzielników zera** do skrócenia niezerowego mianownika w relacji równoważności; jest zgodna z dokładniejszym ujęciem AA-19.

### AA-11/AA-09 → AA-15

- W pierścieniu nieprzemiennym iloraz pierścieniowy wymaga ideału **dwustronnego**. Twierdzenie AA-15 „każdy ideał dwustronny \(M_n(R)\) jest \(M_n(I)\)” ma poprawne założenia również dla nieprzemiennego \(R\). W dowodzie jednostki macierzowe wyodrębniają dokładnie współczynnik macierzy, bez zamiany kolejności współczynników nieprzemiennych.
- Prostota \(M_n(K)\) dotyczy **ideałów dwustronnych**, nie jednostronnych. Bezpośrednio wyliczono wszystkie podprzestrzenie addytywne \(M_2(\mathbb F_2)\) i \(M_2(\mathbb F_3)\) oraz sprawdzono osobno mnożenie z lewej i prawej przez jednostki macierzowe.
- Definicja \(R[G]\) zakłada przemienność \(R\). Dla homomorfizmu z \(R[G]\) do potencjalnie **nieprzemiennego** pierścienia \(S\) potrzebna jest centralność obrazu współczynników \(f(R)\subseteq Z(S)\). Własność uniwersalna wolnego pierścienia nieprzemiennego ma analogiczne zabezpieczenie.
- Przykład \(K[C_n]\cong K[t]/(t^n-1)\) zależy od podstawowej konstrukcji pierścienia wielomianów. W \(K[C_p]\), gdy \(K=\mathbb F_p\), element \([g]-[e]\) jest niezerowy i nilpotentny; to kontrprzykład przeciwko fałszywemu przenoszeniu własności dziedziny na wszystkie algebry grupowe.
- Utożsamienie \(K\langle x,y\rangle/(xy-yx)\cong K[x,y]\) oznacza iloraz przez **ideał dwustronny** i jest potwierdzone zarówno rachunkiem słów, jak i uniwersalnością.

## Test A — dziedziny i nierozkładalność

Ścieżka: `tools/tests/test_abstract_algebra_cross_aa10_11_15.py`. Niezależny algorytm arytmetyczny dla \(\mathbb Z[i]\), całkowitoliczbowe sploty wielomianowe i modularne testy nierozkładalności; `sympy` służy tylko jako niezależny orakl w \(\mathbb Q[x]\).

**Lokalny wynik 60 556/60 556 PASS**:
- \(14\,400\) par niezerowych liczb Gaussa o obu współrzędnych z \([-5,5]\): **14 400** tożsamości Bézouta, **14 400** wspólnych dzielników, **14 400** poprawnych zakończeń algorytmu;
- **15 376** par niezerowych wielomianów stopnia najwyżej 2 o współczynnikach z \([-2,2]\), test multiplikatywności dodatniej zawartości;
- **1822** świadectwa nierozkładalności po redukcji do \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) porównane z niezależną kontrolą nad \(\mathbb Q\);
- **156** przypadków kryterium Eisensteina, **2** kontrole kontrprzykładu przy utracie stopnia.

## Test B — niezależny model nieprzemienny

Ścieżka: `tools/tests/test_abstract_algebra_cross_aa15_confirming.py`. Tylko standardowa biblioteka Python, bez narzędzi Testu A.

- Enumeracja **67** podprzestrzeni \(\mathbb F_2^4\) i **212** podprzestrzeni \(\mathbb F_3^4\). W obu przypadkach dokładnie **dwa ideały dwustronne** pełnego pierścienia macierzy oraz nietrywialne ideały lewostronne i prawostronne.
- Kontrola łączności, rozdzielności, jedynki i odwracalnych bazowych elementów w dziesięciu małych \(\mathbb F_p[C_n]\), wraz z nilpotentnością \(([g]-[e])^p\) w charakterystyce \(p\).
- Odrębna kontrola nieprzemienności \(\mathbb F_2[S_3]\) oraz rzeczywistych reprezentacji \(\mathbb F_2[C_3]\) i \(\mathbb F_3[C_2]\) w pierścieniach macierzy.
- Ewaluacja wszystkich słów długości do 5 w dwóch niekomutujących macierzach oraz sprawdzenie zgodności iloczynu słów z iloczynem ich obrazów; po przejściu do komutujących obrazów sprawdzono zanik różnicy między permutacjami liter.

**Lokalny wynik niezależnego pierwotnego prototypu: 16 174/16 174 PASS**; dokładny wynik wersji zapisanej na GitHubie należy odczytać z jej logu CI.

## Struktura LaTeX, odsyłacze, skład

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-10 | 26 | 1 | 9 | 9 |
| AA-11 | 37 | 18 | 19 | 11 |
| AA-15 | 25 | 2 | 11 | 7 |
| **Razem** | **88** | **21** | **39** | **27** |

Wszystkie **88** etykiet są unikatowe. Wszystkie **21** odsyłaczy mają istniejący cel; dwa zewnętrzne: `aa:ch:pierscienie` i `aa:tw:prime-max-quotient` potwierdzono przez bezpośredni odczyt AA-09. Każde środowisko `\begin`/`\end` jest poprawnie zagnieżdżone. Trzy pliki dołączono do głównego tomu w poprawnej kolejności.

Na wcześniejszym zweryfikowanym PDF (269 stron) obejrzano wszystkie **21 stron** tych rozdziałów: **AA-10 strony 79–84 (6)**, **AA-11 strony 85–93 (9)**, **AA-15 strony 115–120 (6)**. Nie stwierdzono widocznych kolizji ani ucięć. Wynik odniesie się do nowego wydania dopiero po porównaniu z artefaktem zakończonego CI.

## Integracja i bramka stabilizacji

Nowe skrypty opublikowano na istniejącej gałęzi. Dwa kroki oraz wyzwalacze GitHub Actions zostały dodane do `.github/workflows/abstract-algebra-chapter.yml`, commit `925874480ded0ee979fa4e4125e6e9111e6ce1eb`.

**Werdykt merytoryczny:** w badanym zakresie nie wykryto potrzeby zmian źródeł AA-10, AA-11 i AA-15. **Formalne zamknięcie AA-X10 wymaga jeszcze potwierdzenia końca pełnego CI, inspekcji logu i porównania 21 stron z nowym artefaktem PDF**; same lokalne testy nie są równoznaczne z przejściem tej bramki.

## Pozostały zakres

Po AA-X10 priorytetem jest **AA-X11: AA-29–AA-30** w połączeniu z AA-25–AA-28 i AA-31–AA-36. Następnie końcowa synteza audytów AA-01–AA-42, bez utożsamiania kontroli skończonych modeli z formalnym dowodem twierdzeń.
