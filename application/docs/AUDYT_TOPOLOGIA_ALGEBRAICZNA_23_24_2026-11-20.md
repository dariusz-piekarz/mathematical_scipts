# Topologia algebraiczna — szczegółowy audyt AT-23 i AT-24

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, bez zmian w `main`.  
**Zakres:** dwa kanoniczne rozdziały:
`chapters/pl/algebraic_topology/23-kohomologia-snopow-z-nosnikami-i-podstawy-dualnosci-verdiera.tex`
i `chapters/pl/algebraic_topology/24-homologia-przeciec-snopy-perwersyjne-i-twierdzenie-o-rozkladzi.tex`.
**Standard:** DG-01 — poprawne kwantyfikatory i hipotezy, szczegółowe uzasadnienia, pełne rachunki przykładów, kontrprzykłady, terminologia polska, PDF z wizualną kontrolą diagramów, zachowanie oryginalnych etykiet i odsyłaczy.

## 1. AT-23: kohomologia snopów i dualność Verdiera

Sprawdzono definicję i warunki sklejania snopu, włókna (kiełki), dokładność na włóknach, przedłużenie przez zero `j_!`, obraz bezpośredni `j_*`, sekcje o nośnikach zwartych i pochodne funktory sekcji. Przejrzano długi ciąg Mayera–Vietorisa dla nośników zwartych, warunki acyklicznego pokrycia dla twierdzenia Leraya, podwójny kompleks Czecha, rezolwentę de Rhama, różnicę między typami kohomologii, definiowanie `a^!`, globalną dualność Verdiera, przypadek rozmaitości z systemem orientacji i właściwy obraz. Ostatnie części dotyczą lokalizacji, `O(m)` na `P¹` oraz rozgraniczenia twierdzeń przyjętych od udowodnionych.

**Nowe opracowanie rachunkowe:**
1. `prz:p1-serre-residue` — dla `m≤−2`, `N=−m−2` i klas Czecha `[z^{m+1}],...,[z^{-1}]` zdefiniowano
   `⟨[h],p⟩ = Res_{z=0}(h(z)p(z) dz)`
   dla wielomianu `p∈H⁰(P¹,O(N))`. Sprawdzono, że dodanie kobrzegu `f₀−z^m f∞(1/z)` nie zmienia residuum: część `p f₀` nie ma potęg ujemnych, a `z^m p f∞(1/z)` ma wyłącznie potęgi co najwyżej `−2`.
2. Sprawdzono bazę dualną: `⟨[z^{m+1+i}],z^ℓ⟩=δ_{ℓ,N−i}`. Macierz jest antydiagonalna, stąd parowanie niedegenerujące i izomorfizm `H¹(P¹,O(m))≅H⁰(P¹,O(−m−2))^∨`. Przy `m=−3` macierz to `((0,1),(1,0))`. Oddzielnie omówiono `m≥−1`, gdy obie strony znikają. Jest to dowód \emph{konkretnego} przypadku dualności Serre'a, nie ogólny dowód na dowolnej zwartej rozmaitości.
3. Nowa figura `fig:p1-serre-residue` przedstawia dwie przestrzenie i wybór parowań bazowych. Zweryfikować jej ostateczny skład na PDF.
4. **Odsyłacz między skryptami:** przy sześciu operacjach i `⊗^L` dołączono ściśle uzasadniony link do istniejącego rozdziału DG03 `03-algebra-tensorowa-i-zewnetrzna.tex`, z kanonicznymi etykietami `ch:algebra-tensorowa`, `sec:iloczyn-tensorowy`, `thm:tensor-hom`. Płaskość `k`-przestrzeni wektorowych wyjaśnia, dlaczego `⊗^L=⊗` w zakresie obecnych współczynników; nie wyciąga się takiej równości dla modułów nad dowolnym pierścieniem. Nie skopiowano deklaracji `\label` z DG.

**Granica samodzielności:** formalizm `a^!` i jego adjunkcja z `Ra_!`, ogólna dualność względna Verdiera, porównanie snopowej i singularnej teorii z nośnikami oraz twierdzenie B Cartana dla obliczeń pokrycia Steina pozostają \emph{jawnie przyjętymi wynikami}. Weryfikacja przykładu Serre'a nie zastępuje ich dowodów. Status AT-23 powinien zatem zachować zastrzeżenie.

## 2. AT-24: homologia przecięć, snopy perwersyjne i twierdzenie o rozkładzie

Sprawdzono definicję warstwowej pseudorozmaitości PL bez kowymiaru 1, perwersyjności dolnej i górnej, klasyczną dopuszczalność PL dla łańcucha **i jego brzegu**, wzór stożkowy przy jawnie przyjętym lemacie dopuszczalnego stożkowania, przykład stożka na torusie i zawieszenia torusa (różne środkowe perwersyjności i ich dualność). Przejrzano warunki podpory i kopodpory na kiełkach i kopiełkach, przesunięcie `[d]` w kompleksie przecięcia, jego normalizację na gładkiej części, przykład węzła, semismall/small, projektowe twierdzenie o rozkładzie, blow-up i względne twarde Lefschetz.

**Nowe uzupełnienia i korekty:**
1. **Rachunek z dokładnego ciągu normalizacji** `prz:node-normalization-exact-sequence`: dla nieredukowalnej krzywej rzutowej `C` z jednym węzłem `p` i normalizacją `ν:P¹→C`, z dwoma punktami `p_+,p_-` nad węzłem, skonstruowano krótki ciąg snopów
   `0→k_C→ν_*k_{P¹}→k_{\{p\}}→0`.
   Na kiełku nad węzłem jest to dokładny ciąg `0→k→k²→k→0`, gdzie mapy są `a↦(a,a)` i `(a_+,a_-)↦a_+−a_-`; poza węzłem środkowa strzałka jest izomorfizmem. Sprawdzono dokładność dla dowolnego ciała, także charakterystyki `2`.
2. `R^qν_*k_{P¹}=0` dla `q>0` z lokalnych modeli dwóch dysków. Po długim ciągu kohomologii snopów uzyskano `H⁰(C;k)=H¹(C;k)=H²(C;k)=k`; zerowość strzałki z globalnych stałych do różnicy gałęzi wynika z ich równych wartości w `p_+,p_-`. Z kolei `IC_C(k)=ν_*k_{P¹}[1]`, więc `IH¹(C;k)=0`. To jest \emph{rzeczywisty rachunek}, pokazujący różnicę między `H¹` a `IH¹`.
3. `fig:node-normalization-exact-sequence` ilustruje kiełkowy ciąg i konsekwencję dla kohomologii. Pierwsza wersja PDF wykazała **kolizje długich podpisów strzałek**. Poprawiono je bezpośrednio w źródle na krótkie `η_p`, `Δ_p`; pełne wzory pozostają w tekście matematycznym. Ponowna kompilacja i kontrola wizualna potwierdziły brak kolizji.
4. `prz:small-node-normalization` — wykazano, że powyższa normalizacja jest właściwa i **mała** (włókna skończone, więc `X_r=∅` dla `r≥1`, nierówności kowymiarów ostre), a jako biracjonalna rozdzielczość nieredukowalnej krzywej spełnia warunki `cor:small-map-ic-xiii`. Porównano ją z rozdmuchaniem punktu w `C²`, które jest \emph{półmałe, lecz nie małe}: `codim_C{0}=2=2dim_C(P¹)`.
5. Usunięto wadliwy podwójny znak ukośnika w końcowej komendzie `\\emph{...}`, zastępując go poprawnym `\emph{...}`. Błąd miał charakter techniczno-redakcyjny i nie zmienia treści twierdzeń.

**Jawne zastrzeżenia:** pełny lemat dopuszczalnego stożkowania PL, ciąg Mayera–Vietorisa dla `IH`, istnienie i własności perwersyjnej struktury `t`, porównanie wersji łańcuchowej z `IC`, dualność Goresky'ego–MacPhersona, projektowe twierdzenie o rozkładzie i względne twarde Lefschetz są w tym rozdziale **głębokimi wynikami przyjętymi**. Nowe obliczenia węzła i małego odwzorowania nie stanowią niezależnych dowodów ogólnych twierdzeń. Status AT-24 powinien zachować zastrzeżenie.

## 3. Integralność i kontrola

- Wszystkie historyczne etykiety w AT-23/24 pozostały. Dodano wyłącznie nowe etykiety przykładów i diagramów, a biblioteka DG03 zachowała swoje etykiety. Korzystamy z linku dokumentacyjnego między tomami, nie z nieaktywnego `\ref` do oddzielnie kompilowanej książki.
- W bieżącym zakresie nie dodano żadnych grafik ani kodu z plików zewnętrznych — diagramy są osadzone w TeX.
- Dodano `application/tests/test_topology_chapters_23_24.py`: 11 testów nowej pary — integralność rozdziałów 01–24, oryginalne etykiety, odsyłacze, poprawność TeX, rachunek macierzy reszt w przykładzie Serre'a i niezależność od reprezentanta Czecha, dokładność na kiełkach normalizacji, różnica `H¹/IH¹`, właściwości small/semismall i jawny status twierdzeń głębokich.
- Workflow `.github/workflows/algebraic-topology-audit-ch23-24.yml` kompiluje dwa razy dokument AT-01–24, w tym rzeczywiste zależności obu audytowanych rozdziałów, oraz odrzuca niezdefiniowane odsyłacze i `Overfull \hbox`.
- **Końcowa aplikacja:** [GitHub Actions #44801691914](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44801691914) — **SUCCESS**, **239 testów Pythona (1 pominięty)**, Chromium zaliczone, indeks 355 rozdziałów. Wzrost liczby testów względem poprzedniej iteracji: 11 nowych regresji AT-23/24.
- **Końcowa kompilacja:** [GitHub Actions #44801692504](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44801692504) — **SUCCESS**, **248 stron A4**, dwa przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i przepełnień `Overfull \\hbox`. Zaktualizowany PDF został pobrany z artefaktu CI i sprawdzony.
- **Audyt wizualny czterech ilustracji:** AT-23: ilustracja `j_!` na stronie 231 i nowe parowanie Serre'a na stronie 238; AT-24: diagram krótkiego ciągu dokładnego normalizacji i wcześniejszy schemat gałęzi krzywej, oba na stronie 245. Pierwszy PDF wykazał na diagramie nowym zbyt długie podpisy strzałek. Zastąpiono je `η_p`, `Δ_p`. Na starym rysunku tekst „dwie gałęzie” nachodził na kontury; przesunięto go ponad gałęzie. Ostateczny PDF nie zawiera tych kolizji.
- **Integralność:** regresje sprawdzają niepowielanie deklaracji etykiet w AT-01–24 i poprawną rozwiązywalność wszystkich standardowych odsyłaczy AT-23/24. Żadnych historycznych etykiet nie przemianowano. Dwa audytowane rozdziały nie wprowadzają nowych zależności od plików graficznych ani kodu.

## 4. Stan i kolejne kroki

**Stan końcowy:** AT-23 — `zaakceptowany_z_zastrzezeniem` (istnienie i właściwości `a^!`, formalizm sześciu operacji, twierdzenie B Cartana, pełna dualność względna i globalne porównania); AT-24 — `zaakceptowany_z_zastrzezeniem` (lemat stożkowania PL, struktura perwersyjna `t`, dualność przecięć, rozkład BBDG i względne twarde Lefschetz). Obliczenia Serre'a, normalizacji i małości są wykonane i zweryfikowane, ale nie stanowią niezależnych dowodów tych ogólnych twierdzeń.

**Następna para:** AT-25 — kategorie pochodne, struktury Hodge'a i cykle zanikające; AT-26 — wariacje struktur Hodge'a, koneksja Gaussa–Manina i degeneracje. Nie obejmowano ich merytorycznym audytem AT-23/24.
