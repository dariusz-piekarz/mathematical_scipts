# Topologia ogólna — rozdział 13: niezależny audyt 06, wszystkie dowody i korekta kierunku relacji

**Data:** 2026-11-22.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`.  
**Blob przed poprawką:** `33200912c034f3f946909f00b9e4068deeca4ed0`.  
**Blob po poprawce:** `c9078636452731e42a56196e84b5ed9831120e6b`.  
**Zakres:** niezależny przegląd dziewięciu środowisk `proof` (łącznie z całym długim dowodem uzupełnienia), uwagi o ilorazie nierozdzielającej przestrzeni jednostajnej, przykładów i uwagi o zwartości.

## Wynik szczegółowy: 9/9 dowodów przeanalizowanych

| Nr | Dowód / etykieta | Kontrola |
|---:|---|---|
| 1 | `thm:topog-uzupelnienia-filtry-sieci` | Równoważność zupełności przez filtry i sieci: filtr ogonów odpowiada sieci Cauchy'ego, zaś sieć `(A,a)` ma skierowaną relację `(A,a)≼(B,b) ⇔ B⊆A`. Antysymetria nie jest potrzebna i zgodnie z definicją z rozdziału 06 nie jest wymagana. Każdy `b∈A` daje indeks późniejszy od `(A,a)`, więc zbieżność sieci przekłada się na `A⊆O` i zbieżność filtra. |
| 2 | `prop:topog-uzupelnienia-metryczna` | W kierunku metrycznym malejąca baza `A_n` o średnicy mniejszej niż `2^{-n}` daje ciąg Cauchy'ego `x_n∈A_n`. Jeżeli `x_n→x`, to dla każdej kuli `B(x,ε)` zawiera ona odpowiednie `A_n`; filtr zbiega do x. Kierunek odwrotny wykorzystuje filtry ogonów ciągów. |
| 3 | `thm:topog-uzupelnienia-metryczne` | Relacja `(x_n)~(y_n) ⇔ d(x_n,y_n)→0` jest równoważnością. Granica `d(x_n,y_n)` istnieje i nie zależy od przedstawicieli. Klasy ciągów stałych dają izometrię; aproksymowanie dowolnego punktu przez elementy `X` daje gęstość. Dla ciągu Cauchy'ego `z_k` w uzupełnieniu przybliżenia `i(x_k)` z błędem `2^{-k}` tworzą ciąg Cauchy'ego w X, którego klasa jest granicą `z_k`. Sprawdzono także pustą przestrzeń. |
| 4 | `lem:topog-uzupelnienia-rownowaznosc` | Bliskość filtrów jest zwrotna i symetryczna. Dla przechodniości wspólny punkt `b∈B∩B'` istnieje, ponieważ B i B' należą do właściwego filtra pośredniego, a `D²⊆E` zapewnia żądaną parę relacji. |
| 5 | `lem:topog-uzupelnienia-minimalizacja` | Rodzina `E[A]` tworzy bazę właściwego filtra, `F°⊆F`; dla symetrycznego `D` o `D³⊆V` filtr `F°` jest Cauchy'ego. Z `F~G` i `A×B⊆D` otrzymujemy `B⊆E[A_0]` dla dowolnego bazowego `E[A_0]`, co dowodzi `F°⊆G`. Stąd minimalność i jednoznaczność przedstawiciela. |
| 6 | `thm:topog-uzupelnienia-istnienie` | Sprawdzono aksjomaty relacji na minimalnych filtrach, rozdzielanie, zanurzenie jednostajne `x↦N_x`, gęstość oraz zupełność. **Wykryto i poprawiono lukę w argumencie niepustości bazy `B(H,E)`**: gęstość dawała parę w kierunku `(F,i(x))`, podczas gdy definicja `B` wymaga kierunku `(i(x),F)`. Poprawka wybiera symetryczne `D⊆E`, z gęstości uzyskuje `(F,i(x))∈D-hat`, po symetrii `(i(x),F)∈D-hat⊆E-hat`. Dalsza kontrola `B(H,D)²⊆V` i zbieżności `H→G°` z użyciem `D⁴⊆E` nie ujawniła kolejnego błędu. |
| 7 | `lem:topog-uzupelnienia-rozszerzenie` | Gęstość A gwarantuje niepustość `A∩E[z]`; relacje `D²⊆V` dają filtr Cauchy'ego. Ciągłość jednostajna f przenosi go do zupełnej Y. Jednoznaczność granicy daje rozdzielanie Y. W dowodzie jednostajnej ciągłości przedłużenia kontrola `E³⊆D` i wybór `W` z domknięciem zawartym w V są wystarczające; nie przyjmuje się fałszywie, że wszystkie entourages są domknięte. |
| 8 | `thm:topog-uzupelnienia-uniwersalnosc` | Lemat o rozszerzeniu działa po utożsamieniu X z gęstym obrazem przez izomorfizm jednostajny. Złożenia jednoznacznych przedłużeń dwóch uzupełnień są identycznościami na gęstych obrazach, a zatem na całych przestrzeniach. |
| 9 | `thm:topog-uzupelnienia-podprzestrzenie` | Filtr Cauchy'ego z domkniętego A rozpatrywany w X ma granicę w `cl(A)=A`. W odwrotną stronę dla `x∈cl(A)` filtr sąsiedztw punktu x przeciętych z A jest Cauchy'ego, więc zbiega w A; rozdzielanie X wymusza, że granicą jest x. |

## Dokładnie wskazana i wykonana poprawka

W dowodzie `thm:topog-uzupelnienia-istnienie`, przy definiowaniu

```tex
B(H,E)=\{x\in X:\exists\mathcal F\in H,(\iota(x),\mathcal F)\in\widehat E\},
```

poprzednio podano jedynie, że gęstość `iota(X)` zapewnia `iota(x)∈E-hat[F]`.
Dla niesymetrycznego E oznacza to `(F,iota(x))∈E-hat`, a **nie** automatycznie `(iota(x),F)∈E-hat`.

Nowy dowód:

```tex
Są one niepuste: dla $\mathcal F\in H$
wybieramy symetryczne $D\in\mathcal U$
z $D\subseteq E$. Gęstość $\iota(X)$
daje $x\in X$ takie, że
$(\mathcal F,\iota(x))\in\widehat D$.
Symetria $\widehat D$ zapewnia
$(\iota(x),\mathcal F)\in\widehat D
\subseteq\widehat E$, więc $x\in B(H,E)$.
```

**Charakter błędu:** luka w jednym kroku dowodu, nie kontrprzykład dla twierdzenia i nie zmiana przyjętej konstrukcji.

## Uwaga o przestrzeniach nierozdzielających

Sprawdzono relację `R=∩U`: jest równoważnością, ponieważ warunek złożenia pozwala wykazać przechodniość, a odwracanie relacji — symetrię. Obrazy `E_q=(q×q)(E)` tworzą bazę struktury jednostajnej na klasach R; relację składaną kontroluje symetryczne `D³⊆E`, gdzie punkty reprezentujące tę samą klasę są D-bliskie. Rozdzielanie ilorazu wynika z `D³⊆E` i wyboru E, które nie zawiera danej pary. Jednostajnie ciągłe odwzorowanie do przestrzeni rozdzielającej jest stałe na klasach R, bo obrazy par należą do każdego otoczenia jednostajnego przekątnej.

## Pozostałe przykłady i uwaga końcowa

- Metryki `|x−y|` i `|arctan x−arctan y|` mają tę samą topologię, ale tylko pierwsza jest zupełna na R. Uzupełnieniem drugiej jest przedział `[-π/2,π/2]`.
- Q ze zwykłą metryką uzupełnia się do R.
- Produkt przestrzeni zupełnych jest zupełny: filtry Cauchy'ego przenoszą się przez rzutowania, a ich granice wyznaczają granicę w topologii produktowej przez skończone cylindry. W zwykłym ZFC wykorzystuje się tu zasadę wyboru dla rodziny granic. Pusty czynnik daje przestrzeń pustą, która również jest zupełna.
- Zwarta przestrzeń jednostajna jest zupełna. Punkt skupienia filtra istnieje dzięki własności skończonych przecięć; bliskość punktu skupienia i elementów zbioru filtra daje zbieżność filtra. Nie wymaga Hausdorffowości.
- Rozdział 13 nie zawiera środowisk `figure`. Globalna kontrola 27 ilustracji dotyczy rysunków w innych rozdziałach.

## Regresja asymetrycznych relacji i techniczne granice potwierdzenia

Do `tools/tests/test_general_topology_ch13.py` dodano `finite_entourage_orientation_checks`.
Enumeracja dla wszystkich podziałów trzyelementowego zbioru i wszystkich relacji E zawierających najmniejszą relację jednostajną R daje **113 modeli**, w tym **92 przypadki z niesymetrycznymi E**. W niezależnym przeglądzie tych 113 modeli sprawdzono istnienie symetrycznego `D=E∩E^{-1}` oraz poprawność obu kierunków relacji dla wybranego przedstawiciela klasy. Ten model pokazuje zarazem, dlaczego nie wolno po prostu odwracać pary dla dowolnego E.

Wcześniejszy udany CI `45068776546` z artefaktem pełnego wydania (188 stron) dotyczył **starego bloba rozdziału 13**. Po korekcie powstały commity:
- `14b76d4a2c79fec83e8421bd01d6ef71f13281f7` — poprawa dowodu,
- `e50c28dc3174a2be9d5096ace51055a549911ba7` — test regresyjny.

**Nowego CI i nowego PDF po zmianie nie potwierdzono na etapie spisania tego raportu.** Nie wolno oznaczać ich jako PASS na podstawie wcześniejszych wyników. Nie zmieniono etykiet ani sformułowań twierdzeń; zmiana dotyczy uzasadnienia niepustości bazy.

## Status

- **Kontrola matematyczna: 9/9 dowodów i uwagi — wykonana.**
- **Jedna nowo wykryta luka — poprawiona; pozostała część sprawdzonego materiału bez kolejnych uwag wymagających edycji.**
- **Regresja: test dodany; logika 113 modeli dodatkowo sprawdzona niezależnie.**
- **Stabilność po zmianie źródła: OTWARTA**, dopóki nie zakończy się rzeczywisty CI/LaTeX i cykl czystych audytów + dodatkowa kontrola potwierdzająca na aktualnym blobie.
- Następny etap: rewalidacja rozdziału 13 po zmianie, później niezależna kontrola wszystkich dowodów rozdziału 14.
