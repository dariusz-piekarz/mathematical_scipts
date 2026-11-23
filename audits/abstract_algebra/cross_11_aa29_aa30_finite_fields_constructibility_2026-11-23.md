# AA-X11 — przekrojowy audyt AA-29–AA-30: ciała skończone i konstruowalność

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Materiał źródłowy

| Rozdział | Treść | SHA źródła |
|---|---|---|
| AA-29 | Struktura ciał skończonych, wielomiany Frobeniusa, odwrócenie Möbiusa | `9cefafacbb9b857af9ebfa90af25462680a02f07` |
| AA-30 | Wieże rozszerzeń kwadratowych, wielokąty foremne, przykład niekonstruowalnej liczby stopnia 4 | `f9d6e4e96d41e3faba57f9c9f895c99611c12998` |

Kontrola wykorzystuje rzeczywiste źródła LaTeX i sprawdza ich związki z AA-03 (orbita i stabilizator), AA-21 (ciała skończone i normalność rozszerzeń), AA-27 (charakterystyka dodatnia), AA-28 (ciała cyklotomiczne i grupa Galois), AA-32/35 (wyróżnik i redukcja wielomianu modulo liczbę pierwszą). **Nie modyfikowano oryginalnych źródeł matematycznych**.

## AA-29: dowody i zależności

Twierdzenie o czynnikach wielomianu \(X^{q^n}-X\), gdzie \(q=p^m\), rozdziela:
1. zamkniętość zbioru pierwiastków \(X^q-X\) na działania ciała;
2. rozdzielczość \(X^q-X\), ponieważ jego pochodna formalna to \(-1\);
3. fakt, że pierwiastek monicznego wielomianu nierozkładalnego stopnia \(d\) należy do ciała \(q^d\)-elementowego;
4. minimalny okres Frobeniusa równy dokładnie \(d\);
5. równoważność \(\deg f\mid n\iff f\mid X^{q^n}-X\), bez powtarzania czynników.

Wzór \(q^n=\sum_{d\mid n}d N_q(d)\) rzeczywiście liczy **stopnie czynników**, nie ich liczbę. Odwrócenie Möbiusa daje \(N_q(n)=n^{-1}\sum_{d\mid n}\mu(d)q^{n/d}\). Osobny dowód dodatniości \(N_q(n)\) wykorzystuje ścisłe oszacowanie liczby elementów leżących we właściwych podciałach; nie zakłada już istnienia wielomianu nierozkładalnego stopnia \(n\).

**Test niezależny:** `tools/tests/test_abstract_algebra_cross_aa29_30_finite_fields.py`. Zaimplementowano własną arytmetykę w \(\mathbb F_{p^m}\), mnożenie wielomianów, resztę z dzielenia, NWD, kryterium nierozkładalności Rabina, sprawdzanie dzielników wielomianu Frobeniusa i bezpośrednie faktoryzacje dla mniejszych stopni. Badane ciała to \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_4,\mathbb F_8,\mathbb F_9\), w szczególności **nie tylko ciała o liczbie elementów będącej liczbą pierwszą**. Sprawdzenie faktycznie wykonane w GitHub Actions (pierwszy przebieg): **19 395/19 395 PASS**; m.in. 14 693 klasyfikacje nierozkładalności wielomianów i 4 602 weryfikacje dzielników wielomianów Frobeniusa.

## AA-30: dowody i zależności

Przy wyznaczaniu izolowanego punktu przecięcia dwóch prostych współrzędne pozostają w tym samym ciele współczynników. Dla przecięcia prostej z okręgiem otrzymuje się równanie **stopnia co najwyżej dwa**, a dla dwóch okręgów o różnych środkach ich odejmowanie redukuje przypadek do prostej i okręgu. To uzasadnia implikację „konstruowalność \(\Rightarrow\) rzeczywista wieża kwadratowa”.

W kierunku przeciwnym każde rzeczywiste rozszerzenie kwadratowe powstaje przez dołączenie pierwiastka kwadratowego elementu już istniejącego ciała; działania arytmetyczne i dodatni pierwiastek kwadratowy można uzyskać cyrklem i linijką. **Sama podzielność stopnia przez potęgę 2 nie jest wystarczającym kryterium konstruowalności**.

Sprawdzono kontrprzykład \(f=X^4-X-1\):
- nierozkładalność modulo \(2\), więc stopień pierwiastka nad \(\mathbb Q\) wynosi \(4\);
- obliczenie rezolwenty \(R(Y)=Y^3+4Y-1\) i równość wyróżników \(\Delta(f)=\Delta(R)=-283\);
- nierozkładalność rezolwenty, a więc obecność czynnika \(3\) w rzędzie grupy Galois;
- dokładnie dwa pierwiastki rzeczywiste, a więc transpozycję pochodzącą ze sprzężenia zespolonego;
- wniosek o grupie \(S_4\) i **niekonstruowalności** rzeczywistych pierwiastków \(f\), mimo stopnia \(4\).

W twierdzeniu Gaussa–Wantzela kluczową dodatkową hipotezą jest to, że \(\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^\times\) jest **abelową** \(2\)-grupą, gdy \(\varphi(n)\) jest potęgą \(2\). Łańcuch podgrup z kolejnymi indeksami \(2\), kończący się na podgrupie generowanej przez sprzężenie zespolone, odpowiada wieży **rzeczywistych** rozszerzeń kwadratowych. Wniosek \(\varphi(n)\) jest potęgą \(2\iff n=2^a p_1\cdots p_s\) dla różnych liczb pierwszych Fermata został sprawdzony ze wzorem multiplikatywnym na funkcję Eulera.

**Drugi niezależny test:** `tools/tests/test_abstract_algebra_cross_aa29_30_constructibility.py`. Dla wszystkich \(3\le n\le520\) porównuje bezpośrednio obliczone \(\varphi(n)\) z kryterium liczb Fermata, konstruuje podgrupy Gal(\(\mathbb Q(\zeta_n)/\mathbb Q\)) zawierające sprzężenie zespolone i kolejne indeksy \(2\) dla przypadków konstruowalnych; sprawdza stopnie odpowiednich wielomianów cyklotomicznych. Niezależny fragment enumeruje **wszystkie 30 podgrup \(S_4\)**, potwierdza klasę dopuszczalnych grup Galois na podstawie przechodniości, transpozycji i podzielności rzędu przez \(3\). Osobno sprawdza dokładne współrzędne regularnego pięciokąta.

**Uwaga o CI:** pierwszy przebieg (45144204606) zakończył się niepowodzeniem **samego testu** AA-30, ponieważ w wywołaniu `sympy.cyclotomic_poly(n)` użyto domyślnego symbolu innego niż zadany następnie w `sympy.degree(...,x)`. Nie wykryto w ten sposób błędu matematycznego źródła. Błąd testowy naprawiono w commicie `56aad8facf726de03b61ee792a2f767d207161aa`, przekazując ten sam symbol obu wywołaniom. **Nie uznajemy pierwszego, czerwonego przebiegu za potwierdzenie stabilności**.

## Struktura i dokument

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady | Strony PDF |
|---|---:|---:|---:|---:|---|
| AA-29 | 11 | 5 | 4 | 4 | 197–200 (4) |
| AA-30 | 12 | 7 | 5 | 4 | 201–206 (6) |
| **Razem** | **23** | **12** | **9** | **8** | **10** |

Wszystkie 23 etykiety są unikatowe. Trzy odsyłacze do rozdziałów zewnętrznych mają istniejące cele: `aa:ch:embeddings-normal-separable` (AA-21), `aa:tw:orbita-stabilizator` (AA-03), `aa:tw:cyclotomic-galois` (AA-28). Środowiska `\begin` i `\end` są zbilansowane. Oba rozdziały są dołączone do głównego tomu AA-01–AA-42.

Na ostatnim zatwierdzonym PDF (269 stron) wyrenderowano i przejrzano wszystkie 10 stron obu rozdziałów, w tym rysunek pięciokąta w AA-30. Brak widocznych kolizji, obcięć i niewłaściwych podpisów. To źródłowe wydanie będzie porównane z **rzeczywistym PDF** powstałym po zakończeniu CI z poprawionym testem.

## Werdykt warunkowy

Przegląd matematyczny obu rozdziałów nie wykazał konieczności korekty źródeł. **Zamknięcie AA-X11 jako STABILNY** wymaga jednak pomyślnego uruchomienia **obu** testów na aktualnym commicie, kompilacji całego tomu i weryfikacji odsyłaczy, pobrania końcowego artefaktu PDF oraz porównania 10 stron. Wyniki te powinny zostać dołączone do tego raportu, a następnie wykorzystane w audycie globalnym.
