# Topologia ogólna — rozdział 13, czysty audyt 1/2 po korekcie

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`.
**Badany blob:** `c9078636452731e42a56196e84b5ed9831120e6b`.
**Cel:** niezależna kontrola sformułowań, kwantyfikatorów, obu kierunków każdej implikacji i kompletności dowodów; brak edycji rozdziału.

## Kontrola dowodów 1–5

1. `thm:topog-uzupelnienia-filtry-sieci`: relacja na indeksach (A,a) jest zwrotna, przechodnia i skierowana, choć nieantysymetryczna. Dla dowolnego otoczenia O granicy sieci wybrany indeks (A,a) zapewnia, że wszystkie b∈A odpowiadają indeksom (A,b) późniejszym, czyli A⊆O. W drugą stronę filtr ogonów sieci Cauchy'ego jest Cauchy'ego.
2. `prop:topog-uzupelnienia-metryczna`: z warunku Cauchy'ego filtra buduje się malejące niepuste A_n o średnicy <2^{-n}; wybrane x_n mają oszacowanie d(x_m,x_n)<2^{-n} dla m≥n. Jeśli x_n→x, wówczas A_n⊂B(x,ε) dla odpowiedniego n. Kierunek metryczny → jednostajny nie używa własności przeliczalności bazy ogólnej struktury, tylko metryki.
3. `thm:topog-uzupelnienia-metryczne`: przechodniość relacji na ciągach Cauchy'ego; istnienie i niezależność granicy d(x_n,y_n); gęstość klas stałych; kompletność przez aproksymację ciągu (z_k) punktami i(x_k) i oszacowanie trójkątne. Sprawdzono także X=∅, gdzie jedynym uzupełnieniem o gęstym obrazie jest przestrzeń pusta.
4. `lem:topog-uzupelnienia-rownowaznosc`: przechodniość bliskości filtrów opiera się na B∩B'≠∅ dla dwóch zbiorów właściwego filtra pośredniego, nie na bezpodstawnym utożsamieniu ich świadków.
5. `lem:topog-uzupelnienia-minimalizacja`: E[A] są bazą właściwego filtra F°⊆F; dla Cauchy'ego wybór symetrycznego D³⊆V i A×A⊆D daje D[A]×D[A]⊆V. Jeśli G~F, to z A'×B⊆D⊆E i a∈A∩A' otrzymuje się B⊆E[A], a więc F°⊆G. W szczególności F° jest minimalny w swojej klasie i reprezentant jest jedyny.

## Kontrola dowodów 6–9

6. `thm:topog-uzupelnienia-istnienie`: dla relacji E-hat sprawdzono diagonalność, przecięcia bazowe, odwracanie i złożenia; rozdzielanie wynika z jednoznaczności minimalnych filtrów bliskich. Filtry N_x są minimalne i Cauchy'ego; porównanie struktur w obie strony wymaga trzech złożeń D³. Gęstość wynika z A×A⊆D i x∈A. **Poprawiony krok:** dla B(H,E) niepustość otrzymujemy przez symetryczne D⊆E, aby z (F,i(x))∈D-hat dostać (i(x),F)∈D-hat⊆E-hat. Dalej B(H∩H', E∩E')⊆B(H,E)∩B(H',E'); oszacowanie D³ daje Cauchy'ego filtra G. Wybranie D⁴⊆E, A×C⊆D, H=H₀∩H₁ i x∈B(H,W) prowadzi do (F₀,K)∈E-hat dla każdego K∈H.
7. `lem:topog-uzupelnienia-rozszerzenie`: filtr z A∩E[z] jest właściwy i Cauchy'ego przez gęstość A. Istnieje dokładnie jedna granica w zupełnym, rozdzielającym Y. Dla jednostajnej ciągłości rozszerzenia użyto E³⊆D i W o domknięciu relacyjnym zawartym w V. Własność `cl(W)⊆V` jest wyprowadzona, a nie założona dla dowolnego W.
8. `thm:topog-uzupelnienia-uniwersalnosc`: izomorfizm na gęsty obraz zapewnia jednostajną ciągłość f∘i⁻¹. Dla dwóch uzupełnień złożenia przedłużeń są identycznościami na gęstych podzbiorach; rozdzielanie przeciwdziedzin zapewnia identyczność wszędzie.
9. `thm:topog-uzupelnienia-podprzestrzenie`: przy domkniętym A każdy filtr Cauchy'ego na A ma granicę w X i z faktu A=cl(A) także w A. Gdy A jest zupełna, filtr sąsiedztw punktu x∈cl(A) ograniczony do A zbiega jednocześnie do a∈A i do x w X; Hausdorffowość daje a=x.

## Wynik

**Czysta kontrola 1/2:** 9/9 środowisk proof, wszystkie hipotezy i oba kierunki istotnych implikacji zweryfikowane bez nowej korekty. Nie znaleziono kolejnego błędu.
CI po poprawce dowodu: [45070022093](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070022093), completed/success. Po dodaniu testu regresyjnego: [45070070493](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070070493), completed/success; log zawiera PASS dla 113 modeli otoczeń jednostajnych, w tym 92 niesymetrycznych. Obejrzany osobny PDF rozdziału 13 ma 6 stron, cała książka 188; brak ostrzeżeń LaTeX i widocznych usterek składu. Wymagany dalszy audyt 2/2 oraz osobna kontrola potwierdzająca.
