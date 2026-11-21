# Algebra liniowa — rozdział 21, audyt IV (stabilizacyjny)

**Data:** 21 listopada 2026.  
**Źródło:** `chapters/pl/linear_algebra/21-komutant-operatora-i-centralizatory-macierzy.tex`.  
**Zatwierdzony blob źródła:** `6527ae1a6daca48717e6a5f5e83958271abb16f5`.  
**Poprzednie audyty:** `ch21_iteration_01.md`, `02.md`, `03.md`.

## Powtórny audyt twierdzeń, dowodów i przykładów

1. **Komutant i odwracalność:** dowód domknięcia algebry, działania podobieństwa oraz przemienności odwrotności jest kompletny; definicja grupy centralizatora nie zakłada istnienia wartości własnych.
2. **Tożsamość algebr:** `C(T) = End_{K[t]}(V_T)` zachowuje sumy, składanie, jedynkę i skalary; założenie `K` dowolnego ciała jest wystarczające.
3. **Cykliczne Hom:** każdy homomorfizm opisuje obraz klasy 1; warunek `g|fy` prowadzi do modułu `K[t]/gcd(f,g)`. Zweryfikowano dobrze określoność i obie strony bijekcji; przypadki względnej pierwszości i jednakowych wielomianów są uwzględnione.
4. **Cykliczny komutant:** `C(T)=K[T]` i kryterium `gcd(p,m_T)=1` wynikają z właściwego ilorazu pierścienia, nie tylko z porównania wymiarów. Operator cykliczny wymaga `n≥1`, co zapisano jawnie.
5. **Czynniki niezmiennicze:** suma `deg gcd(f_i,f_j)` obejmuje wszystkie uporządkowane pary i przekształca się do `sum_i(2(r-i)+1)deg f_i`. Oszacowania `n≤dim C(T)≤n²` są ostre, a oba warunki równości udowodnione.
6. **Dzielniki elementarne i filtracje:** `deg(p)min(a,b)` daje dokładnie wymiar komponentu Hom; suma `deg(p)sum_k B_{p,k}²` wynika ze zliczania trójek i poprawnie odtwarza wzór z różnic wymiarów jąder. W szczególności wszystkie sumy są skończone.
7. **Ciała skończone:** liczba jednostek `F_q[t]/(p^a)` jest `q^{a deg p}-q^{(a-1)deg p}`; z CRT otrzymujemy wzór dla dowolnego cyklicznego operatora. Nie stosuje się go bez założenia cykliczności.
8. **Przypadki graniczne:** przestrzeń zerowa, wymiar 1, pojedynczy blok, wielomian nierozkładalny stopnia większego niż 1 i dodatnia charakterystyka nie prowadzą do wyjątków poza już opisanymi w tezach.
9. **Przykłady:** ponownie zweryfikowano parametry centralizatora `J_2(0)⊕J_1(0)`, jego wyznacznik i liczbę jednostek nad `F_q`, diagonalną `diag(1,1,2)`, rzeczywisty obrót, parę sześciowymiarowych nilpotentnych macierzy i blok `C((t²+t+1)²)` nad `F_2`.

## Weryfikacja techniczna

- 25 unikatowych etykiet, 37 odsyłaczy, 9 kompletnych środowisk `proof`; brak niezgodnych terminów z `AGENTS.md`.
- [CI 44943843171](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943843171): **SUCCESS** dla aktualnego źródła, w tym regresje, kompilacja pełnej książki, kontrola logu LaTeX i odsyłaczy, eksport samodzielnego PDF rozdziału.
- Samodzielny PDF skorygowanej wersji ma **7 niepustych stron**; render wszystkich stron skontrolowany. PyMuPDF: 0 bloków tekstowych wychodzących poza stronę; w całym PDF znajduje się nagłówek rozdziału 21 i wszystkie końcowe przykłady.
- Finalne źródło rozdziału ma 899 linii. Audyt IV nie wymagał żadnej zmiany w tekście.

## Decyzja

**Audyt IV czysty** — druga kolejna pełna iteracja bez poprawek po audycie II. Rozdział 21 uznano za **STABILNY po czterech audytach**, przy zielonym CI i sprawdzonym PDF. Nie dodano nowych twierdzeń do wcześniej zatwierdzonych rozdziałów 01–20. Następnym etapem jest osobne przygotowanie rozdziału 22.
