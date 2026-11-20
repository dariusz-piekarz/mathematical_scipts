# Topologia algebraiczna — szczegółowy audyt AT-19 i AT-20

**Data:** 20 listopada 2026 r.  
**Gałąź robocza:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Zakres:** dokładnie dwa kanoniczne pliki `chapters/pl/algebraic_topology/19-stopien-indeks-punktu-stalego-i-twierdzenie-lefschetza.tex` i `20-zwartosc-i-sklejanie-trajektorii-morse-a-podstawy-analityczne.tex`.  
**Metoda:** szczegółowość matematyczna, przykłady, poprawna polska terminologia, samodzielne hipotezy twierdzeń i weryfikacja rysunków w standardzie DG-01. Wszystkie oryginalne `\label` oraz istniejące odsyłacze zachowano.

## 1. AT-19 — stopień, indeks i twierdzenie Lefschetza

### Materiał poddany kontroli

Przejrzano definicję liczby Lefschetza z racjonalnej homologii, całkowitość jej wartości, lemat śladu Hopfa i jego dowód przez dwa krótkie ciągi dokładne; twierdzenie Lefschetza dla skończonych CW-kompleksów (w tym rozdzielenie dowodu symplicjalnego od narzędzi ANR), twierdzenie Brouwera, lokalny indeks punktu stałego jako stopień Brouwera, wzór dla nieosobliwego punktu stałego i formułę Lefschetza–Hopfa z dualnością Poincarégo.

### Zmiany merytoryczne

1. **Dwie ujemne lokalne liczby indeksowe.** Dodano `prz:lefschetz-torus-dwa-indeksy`. Dla odwzorowania `f_A:T²→T²` o macierzy całkowitej `A=((2,1),(1,0))` mamy `det A=-1`, `tr A=2` oraz `L(f_A)=1-tr A+det A=-2=det(I-A)`. Równanie punktu stałego to `(A-I)x∈Z²`. Podgrupa `(A-I)Z²` składa się dokładnie z par liczb całkowitych o jednakowej parzystości, więc ma indeks `2`. Jedynymi klasami rozwiązań są `[(0,0)]` i `[(1/2,1/2)]`. W obydwu `Df=A` i `det(I-Df)=-2`, więc lokalne indeksy wynoszą `−1` i `−1`. Suma `−2` zgadza się z liczbą Lefschetza. Wszystkie etapy zostały uzasadnione w tekście.
2. **Wizualizacja** `fig:lefschetz-torus-dwa-indeksy`: kwadrat fundamentalny torusa, dwa czerwone punkty stałe oraz wyraźnie zaznaczona wspólna wartość indeksów.
3. **Wykorzystanie gotowej algebry tensorowej:** w rachunku `det(I-tA)=Σ_k(-t)^k tr(Λ^k A)` dodano bezpośredni odsyłacz do `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`, z oryginalnymi etykietami `thm:potega-zewn-operatora` oraz `thm:minory-lambda`. Nie kopiowano dowodu potęg zewnętrznych.
4. **Zakres dowodu:** twierdzenie Lefschetza dla skończonych CW-kompleksów zostało w tekście udowodnione, przy wyraźnie nazwanym twierdzeniu ANR. Formuła indeksowa dla rozmaitości orientowalnych wykorzystuje klasyczną dualność Poincarégo; dla rozmaitości nieorientowalnych opiera się na osobnym przytoczonym wyniku z lokalnymi współczynnikami. Oznacza to, że **AT-19 nie zawiera samodzielnego pełnego dowodu przypadku nieorientowalnego**, choć zakres twierdzenia i zależności są nazwane. Ta zależność jest jawna i nie może zostać błędnie uznana za dowiedzioną.

## 2. AT-20 — analityczna zwartość i sklejanie trajektorii Morse'a

### Materiał poddany kontroli

Sprawdzono dokładne hipotezy: zwarta rozmaitość bez brzegu, funkcja Morse'a, metryka riemannowska i przepływ ujemnego gradientu; dodatkowy warunek Morse'a–Smale'a dla przestrzeni moduli. Przejrzano równanie energii, zwartość zbiorów granicznych, jednolite ograniczenie czasu z dala od punktów krytycznych, argument z przekrojami poziomów regularnych, granice łamane, zanik wykładniczy blisko punktu hiperbolicznego, warunkowy schemat gluing i orientacje brzegów jednowymiarowych przestrzeni moduli.

### Zmiany merytoryczne

1. **Jawny operator Greena.** Nowy `lem:morse-scalar-green` rozwiązuje na całej prostej liniowe równanie `u'+λu=h` dla `λ≠0` i ograniczonej funkcji ciągłej `h`. Dla `λ>0` rozwiązanie to `Q_λh(t)=∫_{−∞}^t e^{−λ(t-s)}h(s)ds`, a dla `λ<0` całka z ujemnym znakiem od `t` do `∞`. Dowiedziono istnienia całek, równania przez różniczkowanie, jednoznaczności spośród rozwiązań ograniczonych i oszacowania `||Q_λh||_∞≤||h||_∞/|λ|`, niezależnego od translacji czasu. Dodano odrębną uwagę, że ten stałowspółczynnikowy przypadek **nie dowodzi** jednostajnego odwracania zmiennowspółczynnikowego operatora `D_T` w ogólnym gluing.
2. **W pełni obliczony model sklejania na torusie.** Nowy `prz:morse-torus-gluing-explicit` traktuje `f(θ,φ)=cosθ+cosφ` i ujemny gradient `(sinθ,sinφ)`. Dokładnie opisano maksimum `p=(0,0)`, minimum `r=(π,π)` i dwa siodła `q_θ=(π,0)`, `q_φ=(0,π)`; obie wartości siodłowe są równe, co nie przeszkadza konstrukcji. Rozwiązanie każdej zmiennej uzyskano przez `z=tan(θ/2)`, stąd `θ_{ε,a}(t)=2ε arctan e^{t-a}`. Każda trajektoria `p→r` ma dwa przesunięcia `a,b` i dwa znaki `ε,δ∈{−1,1}`; po ilorazowaniu translacji czasu pozostaje parametr `s=b-a∈R`. Zatem `M(p,r)` ma **cztery** składowe homeomorficzne z `R`.
3. **Granice łamane i parametry kołnierzowe, bez luk w szczególnym modelu.** Gdy `s→+∞`, granica łamie się przez `q_θ`; gdy `s→−∞`, przez `q_φ`. Każda składowa kompaktuje się do przedziału `[−∞,+∞]`. Zdefiniowano `ρ_+=e^(−s)`, `ρ_−=e^s`. Rozpisano `θ` i `φ` w dwóch przesuniętych przekrojach czasowych przy `s→+∞`, aby bezpośrednio sprawdzić gładką zależność od `ρ` także przy `ρ=0`; dla drugiego końca działa zamiana ról zmiennych. Wyjaśniono też dwa anulujące się przepływy w różnicy indeksów jeden, prowadzące do `∂_2=0` i `∂_1=0`.
4. **Diagram** `fig:morse-torus-gluing-explicit` pokazuje parametr `s` i dwa końce składowej moduli odpowiadające różnym trajektoriom łamanym. Pozostawiono wcześniejszy schemat `p→q→r`; oba rysunki zostały sprawdzone na PDF.
5. **Odsyłacz do DG:** przy wprowadzeniu dodano link do już istniejącego `chapters/pl/differential_geometry_and_topology/18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex` (etykieta `ch:teoria-morsea`), bez dublowania podstaw geometria–Morse.

### Czy zastrzeżenie AT-18 zostało zamknięte?

**Nie w pełni.** W AT-20 istnieje nadal ogólna teza `thm:morse-gluing-v11`, której dowód przyjmuje lemat o istnieniu `Q_T` z `D_TQ_T=id` i normą `||Q_T||≤C` **jednostajną w parametrze długości szyjki**. Nie wyprowadzono w skrypcie pełnej konstrukcji tych prawych odwrotności dla zmiennowspółczynnikowego operatora i parametrycznej zgodności orientacji liniaryzacji. Dodany operator skalarny i model torusa są ścisłymi rezultatami, lecz nie zastępują brakującego twierdzenia ogólnego. **W konsekwencji AT-18 oraz AT-20 zachowują zastrzeżenie**, zamiast deklarować nieprawdziwe pełne domknięcie sklejania.

## 3. Zależności i walidacja

- W zakresie AT-01–20 testy integralności stwierdziły brak zduplikowanych etykiet oraz kompletność standardowych odsyłaczy `\ref`, `\eqref` dla audytowanej pary. Zachowano nazwy wszystkich istniejących etykiet; nowe to `prz:lefschetz-torus-dwa-indeksy`, `fig:lefschetz-torus-dwa-indeksy`, `lem:morse-scalar-green`, `prz:morse-torus-gluing-explicit`, `fig:morse-torus-gluing-explicit`.
- Nie dodano zewnętrznych plików rysunków ani kodu. AT-19 i AT-20 mają po **dwa** diagramy TikZ; linki do DG są odsyłaczami dokumentacyjnymi i nie wymagają `xr-hyper` podczas osobnej kompilacji.
- Nowe testy `application/tests/test_topology_chapters_19_20.py` obejmują 10 regresji: integralność książki, zachowanie oryginalnych etykiet, odsyłacze, środowiska TeX, polskie słownictwo, etykiety DG, rachunek macierzy i punktów stałych, operator Greena, dokładne rozwiązania ODE i parametry sklejania.
- **Wykryta i poprawiona usterka testu:** pierwszy przebieg aplikacji [#44793900910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44793900910) — FAILURE, ponieważ nowy test wymagał `len(refs)>3`, a w AT-20 są dokładnie trzy poprawne odsyłacze. Poprawiono warunek na `len(refs)>=3` w commicie `001eb10c`, nie modyfikując merytoryki rozdziału.
- **Końcowa walidacja aplikacji:** [GitHub Actions #44794340600](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44794340600) — **SUCCESS**, **208** testów Pythona (1 pominięty), również testy Chromium, indeks 355 rozdziałów.
- **Końcowa walidacja PDF:** [GitHub Actions #44794340616](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44794340616) — **SUCCESS**, **217 stron** A4, **dwa przebiegi** `pdflatex`, brak niezdefiniowanych odsyłaczy i `Overfull \\hbox`.
- **Oględziny finalnego PDF:** sprawdzono wszystkie cztery rysunki AT-19/20: schemat grafu i diagonali na stronie **208**, dwa punkty stałe torusa na stronie **210**, a na stronie **216** oba schematy trajektorii i ich granic łamanych. Rysunki są czytelne i nie zawierają nałożonych podpisów ani obciętych elementów.

## 4. Stan końcowy

**AT-19:** `zaakceptowany_z_zastrzezeniem` — rachunki i bezpośrednio udowodnione twierdzenia sprawdzone; formuła Lefschetza–Hopfa dla nieorientowalnych rozmaitości wykorzystuje odrębne, przyjęte twierdzenie z lokalnymi współczynnikami.  
**AT-20:** `zaakceptowany_z_zastrzezeniem` — ogólne gluing i zgodność orientacji zależą od wymienionych narzędzi analitycznych; pełny szczególny przykład torusa i lemat skalarny są udowodnione.  
**AT-18:** utrzymać uprzednie zastrzeżenie o brakującym ogólnym gluing, mimo nowych uzupełnień AT-20.

**Następna para:** AT-21 i AT-22 (po zweryfikowaniu rzeczywistych nazw i zawartości plików): indeks pól wektorowych, twierdzenie Poincarégo–Hopfa z brzegiem oraz kohomologia z nośnikami zwartymi i homologia Borela–Moore’a.
