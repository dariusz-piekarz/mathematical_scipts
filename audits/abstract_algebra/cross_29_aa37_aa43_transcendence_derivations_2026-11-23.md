# Algebra abstrakcyjna — AA-X29: bazy transcendencji a derywacje (AA-37 × AA-43)

**Data:** 23 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Status początkowy:** audyt matematyczny ukończony, stabilizacja CI otwarta.

## Zakres i niepowtarzalność

AA-X28 (AA-25 × AA-26) został zamknięty po sprawdzeniu rzeczywistego logu GitHub Actions #45275923867, commit bc27417de3da58f3383e8abb82a12afed7dcd7f1, 6/6 nowych testów i zielona kompilacja pełnego tomu. AA-X29 jest nowym interfejsem: AA-37 (bazy transcendencji i wymiana) × AA-43 (derywacje i ich jednoznaczne przedłużanie). Nie powtarza AA-X07 (AA-37–40, normalizacja i wymiar) ani AA-X12 (AA-43–45, całkowanie elementarne).

Źródła:
- AA-37: chapters/pl/abstract_algebra/37-algebraiczna-niezaleznosc-i-bazy-transcendencji.tex, blob b710ae2447d41aef8681de6d55f4c6d3709616c1, 470 wierszy, definicja aa:def:alg-independent i twierdzenie aa:tw:transcendence-existence; przykład aa:prz:transcendence-inseparable.
- AA-43: chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex, blob c6563f402b7890e5e0c8f02796ebf649f4336906, 540 wierszy, twierdzenie aa:tw:algebraic-derivation-extension oraz przykład aa:prz:zero-derivation-and-positive-characteristic.
- AGENTS.md i główny plik books/pl/abstract_algebra.tex. Rozdziały są zatwierdzone i nie zostały zmienione; etykiety pozostały stabilne.

## 1. Zgodność dwóch twierdzeń: pochodne bazy transcendencji determinują derywację

**Twierdzenie przekrojowe.** Niech (K,D_K) będzie ciałem różniczkowym charakterystyki zero, L/K dowolnym rozszerzeniem ciał i B⊆L bazą transcendencji rozszerzenia L/K. Oznaczmy F=K(B). Dla **dowolnej** funkcji h:B→F istnieje dokładnie jedna derywacja D_L:L→L spełniająca D_L|_K=D_K oraz D_L(b)=h(b) dla każdego b∈B.

**Dowód (istnienie na F).** Algebraiczna niezależność B nad K (AA-37) utożsamia pierścień K[B] z pierścieniem wielomianów w zmiennych B. Dla dowolnego P w tym pierścieniu definiujemy D_F(P) jako sumę pochodnych współczynników (z zastosowaniem D_K) oraz skończoną sumę h(b)∂_b P. Każdy wielomian zawiera jedynie skończenie wiele elementów B, więc wzór jest poprawny również dla bazy nieskończonej. Współczynniki wartości h(b) są elementami F, zatem D_F(P)∈F. Jednoznaczny zapis wielomianu zapewnia niezależność od przedstawienia. Z reguły iloczynu dla pochodnych formalnych i Leibniza dla D_K wynika addytywność oraz D_F(PQ)=P D_F(Q)+Q D_F(P).

Dla P,Q∈K[B], Q≠0, określamy D_F(P/Q)=(Q D_F(P)-P D_F(Q))/Q². Wzór jest dobrze określony: jeśli P/Q=R/S, to PS=RQ, a różniczkując tożsamość PS−RQ=0, uzyskujemy równość dwóch formuł na pochodną. D_F jest zatem derywacją F→F przedłużającą D_K, z zadanymi wartościami na B.

**Dowód (przejście do L).** Z definicji bazy transcendencji (AA-37) rozszerzenie L/F jest algebraiczne. Ponieważ char F=0, na mocy twierdzenia aa:tw:algebraic-derivation-extension (AA-43) istnieje dokładnie jedno przedłużenie D_F do derywacji L→L. Jeśli α∈L ma wielomian minimalny m(T)=∑ a_j T^j∈F[T], to
\[
D_L\alpha=-\frac{\sum_j D_F(a_j)\alpha^j}{m'(\alpha)}.
\]
Mianownik jest niezerowy przez rozdzielczość w charakterystyce zero. Każda derywacja spełniająca warunki twierdzenia musi na K[B], a potem na F, być równa opisanej derywacji przez reguły działań i ilorazu; jednoznaczność na L wynika z AA-43. Koniec dowodu.

**Ważne ograniczenie sformułowania:** przepisane wartości h(b) należą do F=K(B), nie są arbitralną funkcją o wartościach poza F. Takiej silniejszej wersji nie przypisuje się bez dowodu twierdzeniu AA-43.

## 2. Zmiana bazy transcendencji a wymuszone pochodne

**Przykład jednowymiarowy.** W L=Q(t) zarówno {t}, jak i {u=t²} są bazami transcendencji L/Q, gdyż t jest algebraiczny stopnia dwa nad Q(u). Derywacja na Q(u) zadana przez D(u)=1 musi po przedłużeniu do L spełniać
\[
1=D(t^2)=2tD(t),\quad\text{więc }D(t)=\frac1{2t}.
\]
Odwrotnie D(t)=1 wymusza D(u)=2t. Wartości pochodnych **nie są niezależnymi wyborami po zmianie bazy**; są powiązane równaniami algebraicznymi.

**Przykład dwuwymiarowy.** W L=Q(x,y), niech D(x)=1 i D(y)=x. Wprowadzamy u=x+y², v=y. Z AA-37 wynika, że {u,v} jest bazą transcendencji, ponieważ x=u−v² i zmiana ma odwrotność wielomianową. Z Leibniza:
\[
D(u)=1+2xy=1+2(u-v^2)v,\qquad D(v)=x=u-v^2.
\]
Dla każdego P∈Q(u,v) obliczona pochodna jest więc równa
\[
D(P)=(1+2(u-v^2)v)\partial_u P+(u-v^2)\partial_v P.
\]
Równość po podstawieniu wynika z reguły łańcuchowej, a nie z niezależnego ponownego wyboru D(u) i D(v).

## 3. Dokładnie gdzie zawodzi charakterystyka dodatnia

**Kontrprzykład.** Niech p będzie liczbą pierwszą, K=F_p, L=F_p(t), u=t^p. Zbiory {t} i {u} są bazami transcendencji L/K: L jest algebraiczne nad K(u), ponieważ t spełnia T^p−u. Na F_p(u) można zadać poprawną derywację D(u)=1 i D(c)=0 dla c∈F_p. Jednak nie istnieje derywacja na L przedłużająca tak zadane D, gdyż dla każdej derywacji w charakterystyce p musi zachodzić
\[
D(u)=D(t^p)=p t^{p-1}D(t)=0,
\]
co przeczy D(u)=1. Wielomian minimalny T^p−u ma pochodną formalną równą zero; nie wolno użyć wzoru dzielącego przez m'(t). To odpowiada wyjątkowi opisanemu w AA-37 oraz ostrzeżeniu AA-43.

**Werdykt merytoryczny:** brak sprzeczności między twierdzeniami. Niezależność algebraiczna nie zapewnia rozdzielczości algebraicznego rozszerzenia. Hipoteza char K=0 w AA-43 jest merytoryczna i nie może zostać pominięta po dołączeniu baz transcendencji.

## 4. Testy odtwarzalne i status techniczny

Utworzono tools/tests/test_abstract_algebra_cross_aa37_43.py z 7 funkcjami regresyjnymi (dokładna symbolika SymPy): zmiana bazy dwóch zmiennych i reguła łańcuchowa; Leibniz i iloraz dla Q(t); spójność różniczkowania w pierścieniu ilorazowym przy z²=t²+1; wymuszenie D(t)=1/(2t) z D(t²)=1; niedopuszczalność przedłużenia w charakterystykach 2,3,5,7,11; wybór racjonalnych wartości pochodnych dwóch zmiennych; inwentaryzacja 50 rozdziałów i integralność najważniejszych etykiet AA-37/43. Testy obliczeniowe są kontrolą przykładów, nie dowodem twierdzenia ogólnego.

Commit utworzenia testów: bb94b1aa7156935598e587740f94210a3c952f33. Commit podłączenia do .github/workflows/abstract-algebra-chapter.yml: 39da3bfd6e263e4b264c62444966a9401cd1ced9. Nowy krok: Run AA-X29 transcendence bases and derivation extensions. Workflow zachowuje testy wcześniejszych audytów, kompilację AA-01–AA-50 i automatyczną kontrolę odsyłaczy.

**Status przy zapisaniu raportu: AA-X29 W STABILIZACJI CI.** Sukces testów lub kompilacji nie jest domniemywany. Do zamknięcia wymagany jest dokładny ukończony zielony run, 7/7 testów w logu, kompilacja i kontrola PDF/odsyłaczy. Nie wykonano nowej wizualnej inspekcji stron PDF. Źródłowe rozdziały nie zostały zmienione.

**Opcjonalna propozycja, nie dodana do wcześniej zatwierdzonych źródeł:** w AA-43, bezpośrednio po twierdzeniu aa:tw:algebraic-derivation-extension, dodać krótki wniosek: dla charakterystyki zero derywację na L można jednoznacznie wyznaczyć przez derywację na K i dowolne wartości w K(B) na bazie transcendencji B. Wprowadza to przydatny pomost do AA-37, lecz rozszerzenie zakresu wymaga osobnego zatwierdzenia zgodnie z AGENTS.md.

**Dalej:** najpierw stabilizacja AA-X29, dopiero po niej niezależny AA-X30.


## Zamknięcie AA-X29 — dowody stabilizacji

**Dokładny przebieg CI:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45279816765, przypięty do SHA 39da3bfd6e263e4b264c62444966a9401cd1ced9, wynik **completed / success**; job validate-cli **138060998987** także **completed / success**.

Zweryfikowano pełny dekodowany log. Wydzielony krok **Run AA-X29 transcendence bases and derivation extensions** ukończył wszystkie 7 regresji z wynikiem ok (sekcja logu wiersze około 10126–10137: `Ran 7 tests in 0.507s`, `OK`). Osobno potwierdzono sukces kroków Run repository tool tests, Compile AA-01 to AA-50 book with latexmk oraz Verify PDF and references (no undefined refs).

**Werdykt końcowy AA-X29: ZAMKNIĘTY / STABILNY** w sprawdzonym interfejsie AA-37 × AA-43. Źródła zatwierdzonych rozdziałów nie zostały zmienione, a nowe testy nie zastępują ogólnych dowodów ani formalizacji Lean. Nie przeprowadzono niezależnej wizualnej inspekcji stron PDF; zielony krok kompilacyjny i kontrola logów tego nie poświadczają.

Dalszy etap: osobny AA-X30, dopiero po powyższej stabilizacji.
