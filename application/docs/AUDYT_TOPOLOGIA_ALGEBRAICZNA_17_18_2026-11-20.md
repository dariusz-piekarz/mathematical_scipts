# Topologia algebraiczna — audyt AT-17 i AT-18

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** dokładnie dwa kanoniczne rozdziały `chapters/pl/algebraic_topology/17-konstrukcja-pontriagina-thoma-i-podstawy-teorii-kobordyzmow.tex` oraz `18-homologia-morse-a-od-punktow-krytycznych-do-homologii-singular.tex`.  
**Standard:** szczegółowe dowody DG-01, kontrola hipotez, rachunków, języka, przykładów i rysunków, bez przemianowywania wcześniejszych `\label` i bez zmian w `main`.

## A. Powiązanie z istniejącą Geometrią różniczkową

Na prośbę użytkownika **nie powielano zdefiniowanej już algebry tensorowej**. Zweryfikowano istnienie dokładnego kanonicznego źródła `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`, w tym oryginalnych etykiet `ch:algebra-tensorowa`, `sec:iloczyn-tensorowy`, `thm:tensor-istnienie` i `thm:tensor-hom`. W AT-17 zastosowano izomorfizm `Hom(ℓ,ℓ⊥) ≅ ℓ* ⊗ ℓ⊥`, w AT-18 iloczyn tensorowy kompleksu Morse'a nad `Z` z `Q` przy obliczaniu liczb Bettiego.

Sprawdzono również rozdziały geometrii różniczkowej `18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex` (etykieta `ch:teoria-morsea`) oraz `19-kobordyzmy-i-rachunek-uchwytow.tex` (etykieta `ch:rachunek-uchwytow`). Oba audytowane rozdziały topologii algebraicznej zawierają odsyłacze do właściwych kanonicznych źródeł, zamiast powtarzać wszystkie definicje i dowody geometryczne.

**Ważne ograniczenie techniczne:** książki `books/pl/algebraic_topology.tex` oraz `books/pl/differential_geometry_and_topology.tex` kompilują się obecnie niezależnie. Wprowadzenie zwykłego `\ref{ch:algebra-tensorowa}` bez `xr-hyper` i skompilowanego `.aux` geometrii różniczkowej tworzyłoby błędny, niezdefiniowany odsyłacz. Dlatego użyto czytelnego `\href` do źródła DG z dokładną identyfikacją oryginalnej etykiety w komentarzu źródłowym. Nie skopiowano deklaracji `\label` do AT i nie powstały konflikty. Po ewentualnym scaleniu tomów należy przejść na mechanizm odsyłaczy międzytomowych z zachowaniem oryginalnych nazw.

## B. AT-17 — Pontriagin–Thom i kobordyzmy

**Zweryfikowane zależności:** wartości regularne, uramowanie normalne, odwzorowanie ściągające, przestrzeń Thoma, konstrukcje dla uramowanych podrozmaitości i grup `π*(MO)`/`π*(MSO)`, izomorfizm Thoma z dualnością Poincarégo oraz klasy charakterystyczne jako przeszkody do bycia brzegiem. Istniejące obszerne dowody utrzymano; narzędzia geometryczne (Whitney, otoczenia tubularne, transwersalność) są nazwane i mają odpowiedniki w DG.

1. **Dodatkowe objaśnienie algebraiczno-geometryczne:** w obliczeniu wiązki stycznej `RPⁿ` uzupełniono naturalne utożsamienie `Hom(ℓ,ℓ⊥)≅ℓ*⊗ℓ⊥` oraz bezpośredni link do pełnej konstrukcji w DG03. Dołączono też odsyłacz do DG19 przy rozkładach kobordyzmów na uchwyty.
2. **Niezerowy element torsyjny w kobordyzmie:** nowy `prz:bordism-rp2-product` oblicza dla `X=RP²×RP²` pierścień `H*(X;F₂)=F₂[a,b]/(a³,b³)` i całkowitą klasę `w(TX)=(1+a+a²)(1+b+b²)`. Wynik `w₂(TX)=a²+ab+b²`, `w₄(TX)=a²b²` daje `w₂(TX)²=a²b²` oraz dwie niezerowe liczby Stiefela–Whitneya w stopniu 4. Ponieważ liczby charakterystyczne zanikają na brzegu, `[X]≠0` w `Ω₄^O`; z `2[X]=0` wynika, że klasa ma **dokładnie rząd 2**.
3. **Dwie rozmaitości o tej samej charakterystyce Eulera, ale różnych klasach kobordyzmu:** nowy `prz:bordism-rp4-versus-rp2-square` porównuje `X=RP²×RP²` z `Y=RP⁴`. Obydwie mają `χ=1`, jednak `w(TY)=(1+t)^5=1+t+t⁴`, więc pary liczb `(⟨w₂²,[M]⟩,⟨w₄,[M]⟩)` wynoszą odpowiednio `(1,1)` i `(0,1)`. Wektory są liniowo niezależne nad `F₂`, co dowodzi istnienia podgrupy `(Z/2)²` w `Ω₄^O`. Nie wyciągnięto stąd nieuprawnionego wniosku o kompletnej klasyfikacji `Ω₄^O`.
4. **Wizualizacja:** dodano `fig:bordism-rp2-product`, pokazujący przejście od klas czynników przez wzór Whitney'a do liczb charakterystycznych i niezerowej klasy kobordyzmu.

## C. AT-18 — homologia Morse'a

**Zweryfikowane zależności:** lemat Morse'a, lokalna liniaryzacja przepływu, monotoniczność funkcji, wymiar przestrzeni niezparametryzowanych trajektorii, kompaktyfikacja złamań w różnicy indeksów 1 i 2, definicja kompleksu i `∂²=0`, uchwyty, zgodność z homologią singularną, silne nierówności Morse'a i przykłady torusa, sfery i okręgu.

1. **Źródło geometrii i algebra tensorowa:** dodano link do DG18 przy wprowadzeniu lematu Morse'a i teorii uchwytów. Przy silnych nierównościach Morse'a zastąpiono niepreferowane słowo przez jawną konstrukcję `CM_*(f,g)⊗_Z Q`, wskazano źródłowy DG03 i uzasadniono użycie płaskości `Q` oraz fakt, że `CM_k⊗_Z Q` ma wymiar równy liczbie punktów krytycznych stopnia `k`.
2. **Nowy szczegółowy przykład torsji w homologii Morse'a:** `prz:morse-rp2-torsja`. Na `RP²` wprowadzono funkcję kwadratową ilorazową `f([x])=(λ₀x₀²+λ₁x₁²+λ₂x₂²)/(∑xᵢ²)` z `λ₀<λ₁<λ₂`, wykazano istnienie dokładnie trzech punktów krytycznych indeksów 0,1,2 i zapisano **jawny wzór na przepływ ujemnego gradientu** `xᵢ(t)=e^(−2λᵢt)xᵢ(0)/sqrt(∑ e^(−4λⱼt)xⱼ(0)²)`.
3. **Ścisłe utożsamienie komórek niestabilnych:** wykazano `W^u(p_k)=RP^k\RP^{k−1}`, z lokalnymi współrzędnymi `xᵢ/x_k`, a stąd filtrację komórkową `RP⁰⊂RP¹⊂RP²`. Przez opis `RP²=D²/(x~−x na ∂D²)` mapą przyłączającą drugiej komórki jest odwzorowanie stopnia `±2`.
4. **Rzeczywisty kompleks Morse'a:** po wyborze orientacji generatorów `0→Z --2→ Z --0→ Z→0`. Obliczono `HM₀=Z`, `HM₁=Z/2Z`, `HM₂=0` i pokazano, że liczby krytyczne `(1,1,1)` nie są równe liczbom Bettiego nad `Q`, czyli `(1,0,0)`. Przykład uzupełnia wcześniejsze przykłady o niezerową różniczkę wykrywającą torsję.
5. **Wizualizacja:** dodano `fig:morse-rp2-torsja`, schemat kompleksu Morse'a z różniczkami `2` i `0`.

## D. Integralność i retesty

- Zachowano wszystkie historyczne etykiety. W zbiorze **AT-01–18** nie znaleziono powielonych deklaracji `\label`. **17/17** standardowych odsyłaczy `\ref/\eqref` z AT-17 i AT-18 ma zadeklarowany cel w tej samej osiemnastorozdziałowej książce.
- AT-17 i AT-18 mają teraz po **dwa** rysunki TikZ. Nie dodano plików zewnętrznych, grafik, danych ani skryptów potrzebnych do kompilacji. Linki do DG mają charakter dokumentacyjny i nie są wymagane do składu.
- Utworzono `application/tests/test_topology_chapters_17_18.py`, w tym regresje obliczeń klasy charakterystycznej produktu i porównania z `RP⁴`, gradientu Morse'a, różniczki `2`, etykiet, brakujących zasobów i kanonicznych odsyłaczy DG.
- Utworzono `.github/workflows/algebraic-topology-audit-ch17-18.yml` z dwukrotną kompilacją AT-01–18 i surową kontrolą błędów, niezdefiniowanych odsyłaczy i przepełnionych wierszy.
- **Testy źródłowe i aplikacja:** [GitHub Actions #44782170923](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44782170923) — **SUCCESS**, **198 testów Pythona (1 pominięty)** oraz pomyślny test przeglądarkowy Chromium; indeks aplikacji obejmuje 355 rozdziałów.
- **Ostateczna kompilacja LaTeX:** [GitHub Actions #44782979521](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44782979521) — **SUCCESS**, **203 strony**, 2 przebiegi `pdflatex`, bez niezdefiniowanych odsyłaczy i bez przepełnień `Overfull \\hbox`. W kompilacji umieszczono AT-01–18 dla pełnej rozwiązywalności odsyłaczy; audyt merytoryczny dotyczył tylko AT-17–18.
- **Wizualizacja i korekta:** skontrolowano wszystkie 4 rysunki TikZ w AT-17/18 na stronach **187, 192, 203 i 203**. W pierwszym renderze (CI #44782109016) napis „Whitney” leżał zbyt blisko obramowań; został przesunięty w AT-17, commit `0e4568e0`, a końcowy PDF ponownie skompilowany i obejrzany. Diagram liczb charakterystycznych na s. 192 oraz diagram różniczki Morse'a i wykres na s. 203 są czytelne, bez obciętych elementów i kolizji napisów.
- **Status po retestach:** AT-17 — `zaakceptowany` w zakresie wykazanych konstrukcji i świadomie przywołanych narzędzi geometrii różniczkowej; AT-18 — `zaakceptowany_z_zastrzezeniem`, ponieważ szczegółowy analityczny dowód kompaktyfikacji/sklejania trajektorii oraz identyfikacji liczb incydencji z trajektoriami należy domknąć przy audycie AT-20. Wyniki CI nie zastępują tego brakującego dowodu.

## E. Jawne ograniczenia i następna iteracja

**AT-17:** pełne twierdzenie Pontriagina–Thoma wykorzystuje zweryfikowane i jawnie wskazane narzędzia z geometrii różniczkowej (aproksymacja, transwersalność, tubularność, stabilizacja osadzeń). Nie wyprowadzano od początku obliczenia całego pierścienia `Ω_*^O`; uzupełnione przykłady dotyczą elementów i liczb Stiefela–Whitneya.

**AT-18:** twierdzenie o kompaktyfikacji niesparametryzowanych trajektorii i zgodności orientacji przy sklejaniu oraz identyfikacja liczb incydencji z trajektoriami odwołują się do głębszych wyników geometryczno-analitycznych. Szczegółowy audyt niezależnych dowodów sklejania jest zarezerwowany dla **AT-20**. Nie należy uważać tych zależności za zamknięte po sprawdzeniu samych przykładów czy `∂²=0`.

**Następna para:** AT-19 (stopień, indeks punktu stałego i twierdzenie Lefschetza) oraz AT-20 (zwartość i sklejanie trajektorii Morse'a — podstawy analityczne). Przy AT-20 sprawdzić i ewentualnie zmienić status zastrzeżenia AT-18.
