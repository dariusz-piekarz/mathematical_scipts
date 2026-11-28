# Algebra liniowa — rozdział 09, audyt V

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**Blob wejściowy (po audycie IV):** `36cc8dc64ae88beea31db953417a192a0e2e10af`  
**Blob końcowy po audycie V:** `0dc33d1aafb0d24e1346295bc2f6bf33e3455fea`  
**Tekst porównawczy:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`, blob `7ab3f15ced06e8233f978471c779e343ac5902ca`.

## Zasada audytu

Przeprowadzono niezależną kontrolę wszystkich istniejących twierdzeń, stwierdzeń, dowodów, przykładów i odsyłaczy rozdziału 09. Skupiono się na formalnych przesłankach, kwantyfikatorach, niezależności dowodów od niejawnych założeń i spójności z geometrią różniczkową. **Nie dodano nowych twierdzeń, sekcji ani nowego zakresu materiału.**

## Wykryte luki i wprowadzone korekty

### 1. Rozpiętość dowolnej realizacji iloczynu tensorowego

**Usterka:** w dowodzie twierdzenia `thm:lin9-jednoznacznosc` rozpiętość uzasadniono tylko bezpośrednio dla realizacji skonstruowanej jako `F/N`, a twierdzenie dotyczy dowolnych par `(T_1,τ_1)` oraz `(T_2,τ_2)` spełniających własność uniwersalną. Tak sformułowany argument nie obejmował wprost wszystkich kwantyfikatorów twierdzenia.

**Naprawa:** niech `(T,τ)` będzie dowolną realizacją i `S=span(τ(V×W))`. Kanoniczne `q:T→T/S` i zerowe `z:T→T/S` spełniają `q∘τ=z∘τ=0`. Z jednoznaczności w własności uniwersalnej dla zerowego odwzorowania dwuliniowego `V×W→T/S` wynika `q=z`; surjektywność `q` wymusza `T/S=0`, zatem `S=T`. Dowód działa także w nieskończonym wymiarze i przy wymiarze zero, bez wyboru bazy. Konstrukcja izomorfizmu `J` z własności uniwersalnej pozostaje bez zmiany.

### 2. Jawne bazy w twierdzeniu o minimalnej liczbie tensorów prostych

**Usterka:** w `thm:lin9-rzad` współczynniki `c_ij` mnożyły `v_i⊗w_j`, lecz wektory `v_i,w_j` nie były zadeklarowane w sformułowaniu samego twierdzenia (pojawiały się w poprzednim twierdzeniu).

**Naprawa:** jawnie przyjęto uporządkowane bazy `B=(v_1,...,v_n)` i `C=(w_1,...,w_m)`, ustalono wymiar każdej przestrzeni i zapisano granice sum. Dowód równości `r_min(t)=rank(C_t)` zachowano.

### 3. Jawne kwantyfikatory rozmiarów macierzy Kroneckera

**Usterka:** w `thm:lin9-rzad-kronecker` nie ustalono wprost, do jakich liczb należą `r,n,s,m`.

**Naprawa:** dodano założenie, że wszystkie cztery liczby są nieujemnymi liczbami całkowitymi. Wciąż obejmuje ono puste macierze i przypadki rzędu zero, a teza `rank(A⊗B)=rank(A)rank(B)` nie uległa zmianie.

## Kontrola pozostałych argumentów

- Konstrukcja `K^(V×W)/N` poprawnie używa wolnej przestrzeni funkcji o skończonym nośniku i czterech rodzin generatorów. Własność uniwersalna jest udowodniona przez `N⊂ker L_b`, a wartości odwzorowania indukowanego na klasach są niezależne od przedstawiciela.
- Tensor prosty jest zerowy dokładnie wtedy, gdy któryś jego czynnik jest zerowy. Dowód korzysta z funkcjonałów wyznaczonych na bazach Hamela, których istnienie dla wymiaru nieskończonego zostało wcześniej uzasadnione z przyjęciem aksjomatu wyboru.
- Rodzina tensorów bazowych jest niezależna, ponieważ można skonstruować funkcjonały `L_pq` wyodrębniające współczynniki. Rozkład macierzy `C_t=Σ a_l b_l^T` dowodzi obu nierówności dla rzędu tensora.
- Wzór na macierz `S⊗T`, kolejność par indeksów i działanie iloczynu Kroneckera są zgodne. Reguły składania, transpozycji i rzędu mają poprawne założenia dla dowolnych, również prostokątnych macierzy.
- Kanoniczne izomorfizmy zamiany czynników, łączności, czynnika jednostkowego, linearyzacji wielu argumentów i rozdzielności względem sum prostej są wyprowadzone z własności uniwersalnej; nie utożsamia się obiektów tylko dlatego, że istnieje między nimi izomorfizm.
- `W⊗V*→Hom(V,W)` jest iniektywne i reprezentuje dokładnie odwzorowania o skończonym rzędzie. Izomorfizm `(V⊗W)*≅Hom(V,W*)` nie wymaga skończonego wymiaru; drugi izomorfizm `V*⊗W*≅(V⊗W)*` ma wyraźne założenie skończonego wymiaru.
- W dowodzie dla podprzestrzeni i ilorazów użycie dopełnienia algebraicznego jest legalne dzięki wcześniejszemu twierdzeniu o dopełnieniach; izomorfizm końcowy jest kanoniczny. Kontrakcja daje ślad i nie wymaga utożsamienia `V` z `V*`.
- Porównanie z rozdziałem 03 geometrii różniczkowej potwierdziło zgodność konstrukcji iloczynu tensorowego, reprezentacji odwzorowań, rozkładu współrzędnych i kontrakcji. Nie przeniesiono wzorów z dzieleniem przez `k!` bez warunku na charakterystykę ciała.

## Walidacja

Statyczna kontrola rozdziałów 01–09: **387 unikalnych etykiet**, **154 odsyłacze z istniejącymi celami**, brak błędów zagnieżdżenia środowisk, brak brakujących importów i rozbieżności katalogu, brak niedozwolonej terminologii. Rozdział 09: **1434 wiersze**, **41 etykiet**, **14 odsyłaczy**.

Uruchomione workflow dla sprawdzonej treści: [walidacja i kompilacja](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44914384898), [testy aplikacji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44914384835). W chwili tworzenia raportu kroki walidacji struktury i testów tensorowych ukończyły się pomyślnie; ostateczny wynik obu przebiegów należy zatwierdzić po zakończeniu, a nie deklarować z góry.

## Decyzja

**Audyt V — zakończony korektami.** Naprawiono jedną lukę w dowodzie i dwa braki w założeniach/oznaczeniach twierdzeń. Nie dodano nowych wyników. Ponieważ tekst został zmieniony, przed ostatecznym uznaniem tej wersji za zamkniętą wymagany jest następny niezależny, czysty audyt rozdziału 09.
