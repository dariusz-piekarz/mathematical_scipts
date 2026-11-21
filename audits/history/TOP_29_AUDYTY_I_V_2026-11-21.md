# Topologia algebraiczna — TOP-29: audyty I–V

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian na `main`).  
**Rozdział:** `chapters/pl/algebraic_topology/29-dalsze-narzedzia-homotopii-granice-odwrotne-przeszkody-operacj.tex`.  
**Końcowy blob TOP-29:** `a860202ab911195bffe564097289e7cd4c28f553`.  
**Zasada:** pięć iteracji audytu istniejącego rozdziału, bez rozszerzania zbioru twierdzeń i lematów; szczegółowość DG-01, kontrola dowodów, sformułowań, przykładów, LaTeX, ilustracji, odsyłaczy i CI.

## Audyt I — granice odwrotne i kryterium Mittaga–Lefflera

1. W definicji `lim¹` jawnie określono układ `(A_j,u_j)`, produkt `∏ A_j` oraz operator `T((a_j))=(u_j(a_{j+1}))`. Odnotowano identyfikację kokernelu z pierwszym prawym funktorem pochodnym granicy w kategorii przeliczalnych układów grup abelowych.
2. Lemat `ker(1−T)=lim A_j` otrzymał pełne założenia, zamiast odsyłania do kontekstu.
3. W dowodzie warunku Mittaga–Lefflera dopisano fragment sześciowyrazowego ciągu dokładnego uzyskanego lematem o wężu z krótkiego ciągu układów `0→B→A→Q→0`, wskazując które dwa krańcowe wyrazy `lim¹` znikają.
4. W twierdzeniu `lim¹(Z,×p) ≅ Z_p/Z` wskazano liczbę pierwszą `p` i homomorfizmy każdego stopnia.

Commit źródła `c7406693357749902faed0c0f02696a954a1bf66`.

## Audyt II — konkretny kontrprzykład w istniejącym przykładzie

Dotychczasowy „Przykład: Dlaczego granicy nie można przestawiać z homologią” opisano tylko przez różniczkę `×p^j`, bez odwzorowań przejścia; sam nie definiował układu odwrotnego. Poprawiono **ten sam przykład**, bez dodawania nowego:
- w stopniu 1: `C_1^(j)=Z`, `u_{j,1}=×2`;
- w stopniu 0: `C_0^(j)=Z`, `u_{j,0}=id`;
- różniczka `d_j=×2^j`, z obliczeniem `d_j u_{j,1}=u_{j,0} d_{j+1}`;
- `lim C_1^(j)=0`, `lim C_0^(j)=Z`, stąd `H_0(lim C)=Z`;
- `H_0(C^(j))=Z/2^j Z`, więc `lim H_0(C^(j))=Z_2`. Wcześniej obliczony element `−1/3∈Z_2\Z` wykazuje nieodwracalność mapy `Z→Z_2`;
- jawnie wyjaśniono, że nie jest to kontrprzykład do twierdzenia Milnora, bo `×2:Z→Z` w stopniu 1 nie jest surjektywne.

Commit `a5809d458f0cbdcd3061be634aec7bca9acc7382`.

## Audyt III — precyzja teorii przeszkód i relacji Adema

W twierdzeniu o kołańcuchu przeszkody określono `q≥2`, bazę CW `B` z punktem bazowym, fibrację `p:E→B`, włókno `F` i jego `(q−1)`-spójność, przekrój `s_q:B^(q)→E`, oraz lokalny system `π_q(F)` otrzymany z transportu wzdłuż fibracji. W twierdzeniu o relacjach Adema wskazano jawnie liczby całkowite `a,b`, warunek `0<a<2b`, współczynniki `F_2` i uniwersalny charakter operacji. W przykładzie z kompleksami wybrano `p=2`, aby niepowtarzalność porównać z wcześniej policzoną resztą 2-adyczną.

Commit `3f053f1ae81e0c2cc5fdca251b579648e962a2aa`.

## Audyt IV — sklejanie Morse'a bez nieuprawnionego dodawania punktów rozmaitości

- Zastąpiono skrót `F(γ_R+ξ)` (niedefiniowalny intrinsycznie na rozmaitości) poprawnym `exp_{γ_R}(ξ)`.
- Wartość reszty przenoszona jest równolegle wzdłuż krótkiej geodezyjnej do ustalonej przestrzeni `Y_δ`; w ten sposób powstaje rzeczywiste odwzorowanie Banachowskie `F_R`.
- Zdefiniowano `e_R=F_R(0)`, `D_R=DF_R(0)` i `F_R(ξ)=e_R+D_Rξ+N_R(ξ)`.
- Lemat o jednostajnym prawym odwrotnym — **nadal przyjmowany, nieudowodniony w tym rozdziale** — otrzymał explicite `Q_R:Y_δ→X_δ`, `D_RQ_R=id`, obraz w dopełnieniu jądra i `||Q_R||≤C`.
- Dowód Banacha uzasadnia równoważność równania pierwotnego i równania punktu stałego na wybranym dopełnieniu jądra przez `D_RQ_R=id` i `Q_RD_R=id`; wskazano jednowymiarowe oszacowanie Sobolewa i jednostajne oszacowania funkcji odcinających przy reszcie nieliniowej.

Commit `6558efdb9e158a49823771c8986a99a43a685620`.

## Audyt V — regresje, LaTeX i PDF

Do `application/tests/test_topology_chapters_29_30.py` dodano trzy testy kontrolujące:
- zgodność odwzorowań łańcuchowych w 125 parach `(j,x)`, redukcje mod `2^j` i 49 precyzji `−1/3` w `Z_2`;
- relację `Sq²Sq²=Sq³Sq¹` na `t^m` dla `0≤m<100`; wszystkie współczynniki zgodne modulo dwa;
- definicję mapy Banacha przez wykładnik i transport, hipotezę `D_RQ_R=id` i usunięcie niedozwolonego `F(γ_R+ξ)`.
Pierwotny test zawierał literówkę polegającą na porównywaniu matematyki wyświetlanej z linią inline; usunięto błąd w asercji, bez zmieniania treści matematycznej.

Commity `3436243652555fe3b9e6c1c7f4fcdcb7119b5d12`, `bc472e2c2e54253de2723fba798d6c8a0ab4e252`.

Kontrola źródła: **13 unikatowych etykiet**, **11 lokalnych odsyłaczy**, wszystkie mają właścicieli; **6 definicji, 6 twierdzeń, 3 lematy, 2 stwierdzenia, 1 wniosek, 7 przykładów, 10 dowodów, 7 uwag**; środowiska `\begin/\end` poprawnie domknięte. Brak niedozwolonych wariantów terminologii.

**PDF:** w zielonym przebiegu kompilacyjnym `44947543985` z końcowym blobem źródła TOP-29 `a860202ab911195bffe564097289e7cd4c28f553` złożono 30 rozdziałów w 321-stronicowy plik; TOP-29 zajmuje strony PDF 310–318 (9 stron A4) i został wyodrębniony osobno. Obejrzano wszystkie strony, w tym diagram redukcji 2-adycznych: brak nakładania napisów i obcięć. Trzeci przebieg pdfLaTeX: 0 błędów, 0 niezdefiniowanych odsyłaczy, 0 przepełnionych wierszy, 0 ostrzeżeń o niestabilności etykiet.

## CI i zależności

- [AT-29/30, kompilacja całej książki — **SUCCESS**](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947543985) dla commita źródła `6558efdb9`.
- [Kontrola międzytomowa AT–DG–AG — **SUCCESS**](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947544027) dla tego samego źródła.
- [Ogólna kontrola aplikacji dla tego samego źródła — **SUCCESS**](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947544040).
- [Po dodaniu regresji pojawił się błąd testu formatowania — failure](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947588697); został poprawiony przez `bc472e2`. [Końcowa walidacja aplikacji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947675503) i [końcowa walidacja AT-29/30](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947675442) wymagają odczytania ostatecznego statusu.

**Decyzja matematyczna:** TOP-29 po pięciu audytach bez dalszych otwartych luk w *udowadnianych w rozdziale* twierdzeniach. Głębokie wyniki o ekscyzji homotopijnej, Ademie, przeszkodach komórkowych i lemacie Fredholma nadal wskazano jawnie jako zależności zewnętrzne. Zamknięcie CI wymaga potwierdzenia ostatniego biegu; następny krok TOP-30.
