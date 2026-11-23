# Teoria grafów i węzłów — audyt 33: rozdział 43 (ekspandery), drugie niezależne przejście

Data: 2026-11-24. Repozytorium: dariusz-piekarz/mathematical_scipts.
Gałąź istniejąca: `biblioteka-matematyczna-iteracja-6`.
Poprzedni audyt: 32, pierwsze przejście tego samego źródłowego rozdziału 43, **PASS** z potwierdzonym structural-audit, pełną książką PDF i oględzinami stron 84–89.
Przedmiot: `chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex`.

## Drugi, niezależny przegląd matematyczny

1. **Ekspansja a przekroje.** Dla każdego niepustego `S⊆V` o `|S|≤n/2` zachodzi `|∂_V S|≤|∂_E S|≤d|∂_V S|` dla grafu `d`-regularnego. Po wzięciu minimów we właściwej kolejności otrzymujemy `Φ≤h_V≤dΦ`. Samo przenoszenie minimum przez iloczyn nierówności mogłoby prowadzić do nieuprawnionego wniosku; sprawdzono rzeczywisty argument z wyborem zbioru realizującego minimum.

2. **Cheeger, górna granica luki.** Dla niepustego `S` realizującego minimum ekspansji, wektor `f=χ_S−(|S|/n)1` ma średnią zero, normę kwadratową `|S|(n−|S|)/n` i energię `|∂_E S|`. Rayleigh daje `λ₂≤Φ·n/(n−|S|)≤2Φ`. Przypadki grafu niespójnego, gdy `λ₂=Φ=0`, nie wymagają dzielenia przez te liczby.

3. **Cheeger, dolna granica luki.** Dla niezerowego wektora własnego `f⊥1` obydwa znaki występują, a jeden z dwóch zbiorów dodatnich lub ujemnych ma liczność co najwyżej `n/2`. Po wyborze znaku dodatnia część `g=f_+` jest niezerowa. Elementarna nierówność `(a−b)(a_+−b_+)≥(a_+−b_+)²`, lemat współpowierzchniowy, Cauchy–Schwarz i `(a+b)²≤2(a²+b²)` dają `dλ₂∑g²≥∑(Δg)²≥(dΦ²/2)∑g²`. Ten argument obejmuje także grafy niespójne.

4. **Własność Markowa i mieszanie.** Dla regularnego grafu `P=A/d` jest symetryczną macierzą stochastyczną, `Q=(I+P)/2` ma widmo w `[0,1]`; spójność zapewnia prostą wartość własną `1`. Na podprzestrzeni prostopadłej do stałych operator ma normę `1−λ₂/2<1`. Nie należy wnioskować o mieszaniu zwykłego `P` bez nieokresowości: na `K₂` rozkład co krok przeskakuje między dwoma stanami. Granica wariacji całkowitej w rozdziale używa jawnie `Q` i jest poprawna.

5. **Średnica.** Dopóki kula ma co najwyżej połowę wierzchołków, jej liczność wzrasta co najmniej `(1+h_V)` razy. Promień `R=ceil(log n/log(1+h_V))+1` wystarcza do przekroczenia połowy, więc dwie takie kule mają wspólny wierzchołek; `diam(G)≤2R` jest poprawne.

6. **Kontrola obiektów szczególnych.** Dla `K_n` luka wynosi `n/(n−1)`, dla `C_n` luka wynosi `1−cos(2π/n)`, a dla hipersześcianu `Q_d` luka znormalizowanego Laplasjanu wynosi `2/d`. Dla `K_{m,m}` (m≥2) wynosi `1`; dla `K₂` wynosi `2`. Każdy z tych przypadków spełnia opisane oszacowania, włącznie z ekstremalnymi `K₂` i `C₃`.

**Wynik drugiego przeglądu źródła:** nie znaleziono nowego błędu matematycznego ani nieuzasadnionej luki wymagającej zmiany zatwierdzonych twierdzeń. Nie poszerzano treści bez odrębnej zgody. Opcjonalna propozycja dopuszczenia stopni `d_j≤D` zamiast wspólnego `d` pozostaje wyłącznie propozycją z raportu 32.

## Nowe, niezależne regresje skończone

Dodano `tools/tests/test_graph_and_knot_expanders_second_pass.py` i osobny krok `Second independent coarea hypercube bipartite and lazy mixing audit (43)` do `.github/workflows/graph-and-knot-global-audit.yml`; dopisano też plik testu do wyzwalaczy `push.paths`.

Użyto innych rodzin i algorytmów niż w audycie 32:
- 20 rodzin strukturalnych: `Q_d` dla 1≤d≤4, `K_{m,m}` dla 1≤m≤6, `C_n` dla 3≤n≤12. Każda ma niezależną formułę ekspansji lub widma, kontrolowaną z pełnym wyliczeniem przekrojów;
- 1500 funkcji o nośniku nieprzekraczającym połowy wierzchołków: całkowicie dokładna tożsamość warstwowa `Σ|g(u)²−g(v)²|=∫|∂_E{g²>t}| dt` z arytmetyką wymierną; oddzielnie nierówności Cauchy’ego–Schwarza i oszacowanie Cheegera;
- 1326 przypadków mieszania: dokładne iteracje `Q` w arytmetyce wymiernej, kontrola normalizacji, nieujemności i granicy TV z widmem znanym analitycznie; odrębny kontrprzykład okresowości zwykłego spaceru na `K₂`;
- strażnik źródłowych hipotez: etykiety Cheegera, lematu współpowierzchniowego i mieszania, spójność, regularność i jawne użycie `Q`.

Przebieg początkowy [45290716797](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45290716797) ujawnił **błąd testowego dopasowania tekstu**, nie błąd matematyczny: skrypt wymagał `d-regularnym`, a LaTeX zgodnie z zapisem matematycznym zawierał `$d$-regularnym`. Wszystkie trzy grupy kontroli liczbowych wcześniej przeszły. Poprawiono dopasowanie w commicie `edde0e47136b5385b80a5bc26ef5ff146ddacf9c` (bez modyfikacji rozdziału).

Ponowiony przebieg [45290837906](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45290837906) z dokładnego SHA `edde0e47136b5385b80a5bc26ef5ff146ddacf9c`: krok drugiego audytu 43 ma już wynik **completed / success**, a cały job `structural-audit` uzyskał **completed / success**. Liczby potwierdzone w logach pierwszego uruchomienia przed strażnikiem: 20, 1500 i 1326; ponowienie potwierdza przejście również strażnika.

## Kontrola składu i odsyłaczy

Potwierdzono, że pierwszy przebieg CI dla rozdziału 43 (#45289361352) zakończył się sukcesem całego workflow i wygenerował 298-stronicowy PDF bez ostrzeżeń. Z tego dokładnego artefaktu obejrzano wizualnie strony 84–89 w jednym arkuszu sześciu stron; nie stwierdzono kolizji rysunków, urwanych wzorów ani napisów wychodzących poza marginesy. Przy drugim przejściu nie zmieniano źródła rozdziału 43 (SHA blobu `d02bda242d51fa11ae470d1a8d1822f5d8ceccbb`), tylko testy i raporty.

**Werdykt w chwili utworzenia raportu:** drugie przejście matematyczne i `structural-audit` **PASS**. Ostateczne zamknięcie rozdziału 43 wymaga sprawdzenia sukcesu `full-book-pdf` ponowionego przebiegu #45290837906 oraz kontroli jego artefaktów. Dopiero wtedy możliwe jest przejście do końcowego audytu globalnego wszystkich 44 plików źródłowych.
