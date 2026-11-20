# Topologia algebraiczna — audyt matematyczny AT-05 i AT-06

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** dwa kolejne rozdziały `chapters/pl/algebraic_topology/05-homologia-przestrzeni.tex` i `06-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex`.  
**Standard:** szczegółowość dowodów, przykładów, kontrprzykładów, rysunków i wyjaśnień terminologicznych na poziomie pierwszego rozdziału geometrii różniczkowej. Zachować oryginalne nazwy `\label` i istniejące odsyłacze; nie scalać niezależnych skryptów i nie zmieniać `main`.

## AT-05 — homologia przestrzeni

Przejrzano: orientacje i brzeg symplicjalny, tożsamość `∂²=0`, singularne grupy łańcuchów i operator pryzmatyczny, długi ciąg pary, homologię zredukowaną, lematu o małych łańcuchach i wycinanie, sekwencję Mayera–Vietorisa, homologię sfer, porównanie modeli symplicjalnych i singularnych, związek z homologią komórkową i stopniem map, przykłady torusa, przestrzeni rzutowej i homologię lokalną.

### Uzupełnienia i kontrola

1. **Łączące odwzorowanie Mayera–Vietorisa bez przeskoku na poziomie klas.** W nowym przykładzie `prz:mv-sfera-dwie-polkul` rozłożono sferę na otwarte zbiory `U=S²\\{S}` i `V=S²\\{N}`. Zgodnie triangulowane półkule dają łańcuchy `a∈C₂(U)`, `b∈C₂(V)` i zorientowany cykl `γ∈C₁(U∩V)` z `∂a=γ=-∂b`. Obliczenie `δ[a+b]=[γ]` wykazuje jawnie, że generator `H₂(S²)` odpowiada generatorowi `H₁(S¹)` (ze znakiem zależnym od orientacji).
2. **Nowy nietrywialny przykład z torsją:** butelka Kleina `K`, `prz:homologia-butelka-kleina`. Objaśniono iloraz kwadratu i słowo dołączające `aba^{-1}b`. Mamy `C₂=Z`, `C₁=Za⊕Zb`, `C₀=Z` oraz `∂₂(1)=2b`, `∂₁=0`; stąd `H₀(K)=Z`, `H₁(K)=Z⊕Z/2Z`, `H₂(K)=0`. Kontrast z torusem: taka sama liczba komórek w każdym wymiarze i charakterystyka Eulera `0`, lecz inne grupy homologii. Po zmianie współczynników na `Z/2Z` powstaje klasa w `H₂(K;Z/2Z)`, niewidoczna nad `Z`.
3. **Ilustracja geometryczna:** `fig:homologia-butelka-kleina`, samodzielny TikZ; strony kwadratu z dwoma przeciwległymi kierunkami pionowymi i zgodnymi kierunkami poziomymi. Zgodność kierunków i słowa `aba^{-1}b` sprawdzona matematycznie.
4. **Terminologia:** usunięto formę niewłaściwego w polskim skrypcie terminu z opisu zmiany współczynników, zastępując ją precyzyjną nazwą funktora iloczynu tensorowego.

## AT-06 — wyższe grupy homotopii i związek z homologią

Przejrzano: `π_n`, Eckmanna–Hiltona, zmianę bazy, względne grupy homotopii i ich długi ciąg, przedłużanie homotopii dla par CW, przybliżenie komórkowe, niezmienniczość `π_n` przy nakryciach, stopień pierwszy twierdzenia Hurewicza, twierdzenie Whiteheada, względne i bezwzględne twierdzenia Hurewicza oraz kryterium homologiczne Whiteheada.

### Uzupełnienia i kontrola

1. **Nowy przykład łączący `π₁` z `H₁`:** abelianizacja grupy podstawowej butelki Kleina `prz:pi1-klein-hurewicz`. Prezentacja `⟨a,b|aba^{-1}b=1⟩` przechodzi w addytywną relację `2b=0`. Otrzymano `π₁(K)_{ab}≅Z⊕Z/2Z≅H₁(K;Z)`; porównanie z przykładem homologii butelki Kleina w AT-05 pozwala śledzić każdą relację.
2. **Dwa przyłączenia do `S²` o stopniach `2` i `3`:** `prz:pi-2-3-komorki`. Różniczka `∂₃:Z²→Z` ma postać `(a,b)↦2a+3b`, obraz całe `Z`, jądro `Z(3,-2)`. Dlatego `H₂=0`, `H₃≅Z`. Przestrzeń jest jednospójna, zatem pierwszy Hurewicz daje `π₂=0`, a kolejny Hurewicz daje `π₃≅Z`. Wzmocnienie: odwzorowanie generatora `S³→X` jest równoważnością homologiczną pomiędzy jednospójnymi CW, więc z homologicznego kryterium Whiteheada `X≃S³`. Każdy etap argumentu jest wyprowadzony z wcześniej udowodnionych twierdzeń.
3. **Nowy diagram różniczki komórkowej** `fig:pi-2-3-komorki`. Pokazuje osobno jądro i obraz `∂₃`; kontrast „zabicie klasy w stopniu 2, powstanie w stopniu 3” jest opisany matematycznie w podpisie.
4. Dodano wcześniejsze objaśnienie rozróżnienia grupy `π₁` od przemiennych `π_n` dla `n≥2`, aby nie sugerować nieuzasadnionego utożsamienia wyższych homotopii z homologią.

## Kontrola techniczna i odsyłacze

- Wszystkie historyczne `\label` zachowano. W AT-01–06 nie występują powielone nazwy etykiet. Przed aktualizacją dokumentacji przejrzano łącznie **116** standardowych wystąpień `\ref` i `\eqref` w AT-05/06; każdy cel jest zadeklarowany w jednym z rozdziałów AT-01–06. Nowe etykiety mają niekolidujące, lokalne nazwy.
- AT-05 ma **4**, a AT-06 **5** rysunków TikZ. Obejrzano ich położenie i podpisy w finalnym, skompilowanym PDF na stronach: **46, 47, 57, 58, 61, 62, 69, 74, 75**. Nie stwierdzono kolizji napisów ani obciętych elementów. Szczególną uwagę poświęcono nowym ilustracjom na stronach 58 i 74.
- Rozdziały nie odwołują się do zewnętrznych obrazów, plików danych ani podprogramów. Nowe rysunki są w pełni osadzone w TeX. Zachowano modułowy książkowy `\input` i dotychczasowe źródła.
- Nowe regresje `application/tests/test_topology_chapters_05_06.py` kontrolują zachowanie dotychczasowych etykiet, obecność sześciu rozdziałów w książce, odsyłacze, brak zewnętrznych zależności, poprawne zbilansowanie środowisk, brak niepreferowanej terminologii oraz obliczenia z dwóch nowych przykładów.
- Osobny workflow `.github/workflows/algebraic-topology-audit-ch05-06.yml` kompiluje **AT-01–06** dwukrotnie, aby wszystkie wewnętrzne odsyłacze do wcześniejszych rozdziałów mogły się rozwiązać. Obejmuje kontrolę błędów TeX, nierozwiązanych cytowań i przepełnionych wierszy.

## Retest — potwierdzony

- [GitHub Actions: aplikacja #44762101029](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44762101029) — **SUCCESS**, **139** testów Pythona, `OK (skipped=1)`; testy Chromium, podglądu odsyłaczy i indeksowania zaliczone.
- [GitHub Actions: LaTeX #44762171825](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44762171825) — **SUCCESS**, **76 stron A4**, dwa przebiegi `pdflatex`, bez niezdefiniowanych odsyłaczy i bez `Overfull \hbox`. Artefakt `algebraic-topology-audit-ch05-06-pdf` obejmuje PDF i logi.
- Audyt merytoryczny dotyczy wyłącznie **AT-05 i AT-06**; AT-01–04 są uwzględnione w PDF jedynie dla zależności matematycznych i odsyłaczy. Nie oznacza to ponownego globalnego audytu poprzednich rozdziałów.
- Status obu rozdziałów: **`zaakceptowany`**, zarejestrowany w `application/data/AUDYT_ROZDZIALOW.csv`. W bieżącej partii nie poprawiano nierozwiązanych odsyłaczy geometrii różniczkowej; w indeksie pozostaje **14** takich wystąpień, związanych z niekompletnym importem DG.

**Następna iteracja (dokładnie dwa rozdziały): AT-07 — fibracje i długi ciąg homotopii; AT-08 — kohomologia singularna i iloczyn kubkowy.**

Nie zmieniano `main` ani historycznych etykiet i nie wykonano nieuzgodnionego scalania innych skryptów.
