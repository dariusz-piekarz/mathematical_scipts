# Algebra liniowa — rozdział 04, audyt 1

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex`  
**Temat:** Macierze odwzorowań liniowych i zmiana bazy  
**Commit z pierwszego audytu:** `fd362376b676164c6c4e8260c260168f441b5d05`  
**Status:** wersja rozdziału utworzona i poddana pierwszemu audytowi; rozdział **nie jest jeszcze zamknięty**.

## Przygotowanie i zależności od wcześniejszych rozdziałów

Sprawdzono bieżącą gałąź GitHuba. Istniały trzy zatwierdzone rozdziały algebry liniowej:
1. Przestrzenie wektorowe — podprzestrzenie, niezależność liniowa, bazy, współrzędne.
2. Wymiar, sumy proste i przestrzenie ilorazowe.
3. Odwzorowania liniowe, jądro i obraz — izomorfizmy, twierdzenie o wymiarze jądra i obrazu, przestrzenie \(\operatorname{Hom}\), projekcje.

Nowy rozdział 04 korzysta bezpośrednio z wymienionych wyników. Unika ich ponownego przepisywania i rozwija reprezentację odwzorowań liniowych w uporządkowanych bazach. Eliminację Gaussa i ogólną teorię obliczeń na wierszach można opracować w następnym rozdziale; obecny jedynie przygotowuje interpretację macierzową układów.

Zastosowano standard szczegółowości analogiczny do rozdziału 01 skryptu „Geometria różniczkowa”: każdy istotny krok dowodu jest uzasadniony, a przykłady zawierają rachunki, nie same wyniki.

## Utworzona treść

Rozdział zawiera dziewięć części i końcowe podsumowanie:

1. **Macierze jako tablice skalarów:** definicja \(\operatorname{Mat}_{m\times n}(K)\), działania punktowe, baza macierzy \(E_{ij}\), wymiar \(mn\), również przypadki \(m=0\), \(n=0\).
2. **Działanie macierzy na kolumnach:** formuła \((Ax)_i=\sum_j a_{ij}x_j\), jej liniowość i interpretacja kolumn jako obrazów wektorów bazy standardowej.
3. **Macierz odwzorowania:** definicja \([T]_{C\leftarrow B}\), wzór \([T(v)]_C=[T]_{C\leftarrow B}[v]_B\), istnienie i jednoznaczność reprezentacji; izomorfizm \(\operatorname{Hom}_K(V,W)\cong\operatorname{Mat}_{m\times n}(K)\).
4. **Mnożenie macierzy:** interpretacja iloczynu jako złożenia odwzorowań, dowód łączności, rozdzielności i roli \(I_n\), kontrprzykład do przemienności.
5. **Rząd macierzy:** obraz jako przestrzeń rozpięta przez kolumny, jądro jako zbiór zerowych kombinacji kolumn, nierówność rzędu i kryteria iniektywności oraz surjektywności.
6. **Macierze odwracalne:** równoważność odwracalności, bijektywności operatora, bazy z kolumn, jądra zerowego i surjektywności. Jednoznaczność macierzy odwrotnej i odwracanie iloczynu.
7. **Zmiana bazy:** macierze przejścia \(P_{B\leftarrow B'}\), wzór \([v]_B=P[v]_{B'}\), zmiana reprezentacji \([T]_{C'\leftarrow B'}=Q^{-1}AP\), podobieństwo \(P^{-1}AP\) dla endomorfizmu, przykład liczbowy.
8. **Transpozycja:** definicja i dowody \((A^{\mathsf T})^{\mathsf T}=A\), \((AD)^{\mathsf T}=D^{\mathsf T}A^{\mathsf T}\), liniowość transpozycji i przykład.
9. **Układy równań:** \(Ax=b\), warunek rozwiązalności \(b\in\operatorname{im}A\), opis wszystkich rozwiązań jako \(x_0+\ker A\), przykład z parametrem.

## Pierwszy audyt — wprowadzone poprawki

### 1. Jawne założenia i kwantyfikatory

W twierdzeniu o izomorfizmie \(\operatorname{Hom}_K(V,W)\cong\operatorname{Mat}_{m\times n}(K)\) dopisano, że \(V,W\) są **przestrzeniami wektorowymi nad \(K\)**, mającymi określone wymiary \(n,m\in\mathbb N_0\).

W twierdzeniu o działaniach macierzowych jawnie określono dodatkowe macierze \(A'\in\operatorname{Mat}_{m\times n}(K)\) i \(B'\in\operatorname{Mat}_{n\times p}(K)\). Nie pozostają ukryte w sformułowaniu „macierze odpowiednich rozmiarów”.

W stwierdzeniu o transpozycji zadeklarowano **wszystkie** parametry \(m,n,p\in\mathbb N_0\), używane w tezie.

### 2. Rozróżnienie bazy standardowej i macierzy bazowych

Ustalono globalnie w obrębie rozdziału notację \(E_n=(e_1,\ldots,e_n)\) dla uporządkowanej bazy standardowej \(K^n\). Dzięki temu symbole \(E_2,E_3,E_n\) występujące w przykładach i dowodach mają jawne znaczenie. Ustalono, że \(E_0\) jest bazą pustą.

Macierze \(E_{ij}\) o pojedynczym niezerowym wyrazie nazwano **macierzami bazowymi**, a nie „macierzami elementarnymi”. Te drugie określenie rezerwujemy do ewentualnej teorii operacji elementarnych na wierszach, aby uniknąć dwuznaczności terminologicznej.

### 3. Samodzielny diagram współrzędnych

Dodano diagram TikZ ilustrujący zależność
\([T(v)]_C=[T]_{C\leftarrow B}[v]_B\) jako przemienny kwadrat
\(V\to W\), \(V\to K^n\), \(W\to K^m\), \(K^n\to K^m\).
Etykieta `fig:lin4-wspolrzedne`; rysunek nie zależy od zewnętrznego pliku.

## Pierwsza kontrola matematyczna

- **Zapis macierzowy:** definicja odczytu współrzędnych przez kolumny jest zgodna z kolejnością baz i dobrze określona. Każda macierz odpowiada dokładnie jednemu odwzorowaniu przy ustalonych bazach; dowód obejmuje przestrzenie zerowe.
- **Mnożenie:** formuła \((AB)_{ik}=\sum_j a_{ij}b_{jk}\) odpowiada \([T\circ S]\). Łączność i rozdzielność wynikają ze skończonych sum; uwzględniono wszystkie przypadki z wymiarem zero.
- **Rząd:** przestrzeń rozpięta przez kolumny jest dokładnie obrazem \(L_A\), a jądro to wszystkie współczynniki dające zero. Wzór \(n=\dim\ker A+\operatorname{rk}A\) nie wymaga tu aksjomatu wyboru.
- **Odwracalność:** bijektywność \(L_A\) jest równoważna istnieniu dwustronnej macierzy odwrotnej, a odwracalność w skończenie wymiarowym \(K^n\) jest równoważna iniektywności lub surjektywności. Wzory są poprawne także dla \(n=0\).
- **Zmiana bazy:** orientacja \(P_{B\leftarrow B'}\) i \(Q_{C\leftarrow C'}\) jest poprawna. Wzór \([T]_{C'\leftarrow B'}=Q^{-1}AP\) ma właściwą kolejność czynników, a przykład nad \(\mathbb R^2\) potwierdza go na bazach.
- **Transpozycja:** wyrazy \((AD)^{\mathsf T}\) i \(D^{\mathsf T}A^{\mathsf T}\) są zgodne przy przemienności mnożenia skalarów w ciele \(K\), również dla pustych wymiarów.
- **Układy:** warunek \(Ax=b\iff b\in\operatorname{im}A\) oraz opis \(x_0+\ker A\) wynikają bezpośrednio z liniowości; przykład \(2\times3\) daje pełną parametryzację.

Nie stwierdzono fałszywej tezy, niepoprawnej macierzy przykładowej ani luki unieważniającej główne dowody. Poprawki pierwszego audytu dotyczą samodzielności twierdzeń, terminologii i wizualizacji.

## Niezależne testy obliczeniowe

Dla wszystkich \(81\) macierzy \(2\times2\) nad \(\mathbb F_3\):
- Sprawdzono **531441** uporządkowanych trójek macierzy pod kątem łączności mnożenia;
- **6561** par pod kątem \((AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}\);
- **81** przypadków kryterium odwracalności (48 macierzy odwracalnych);
- **3888** par \((A,P)\) z odwracalną macierzą \(P\) pod kątem formuły podobieństwa i działania na współrzędnych.

Ponadto dla wszystkich **689** macierzy nad \(\mathbb F_2\) o rozmiarach \(m\times n\), \(0\leq m,n\leq3\), sprawdzono:
- równość wymiarową \(|\ker A|\cdot|\operatorname{im}A|=|K^n|\);
- równość obrazu z przestrzenią rozpiętą przez kolumny;
- **5054** par \((A,b)\) pod kątem warunku rozwiązalności \(Ax=b\);
- **3138** niepustych zbiorów rozwiązań pod kątem postaci \(x_0+\ker A\).

**We wszystkich tych testach: 0 rozbieżności.** Testy są kontrolą pomocniczą, nie zastępują dowodów w skrypcie.

## Integracja z Biblioteką i kontrola statyczna

- Plik `chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex` zawiera **1192 wiersze i 49 etykiet**.
- W rozdziałach 01–04: **199 unikalnych etykiet**, bez kolizji.
- Wszystkie **88 odsyłaczy** `\\ref` i `\\eqref` mają istniejące cele.
- Nie stwierdzono niedomkniętych lub błędnie zagnieżdżonych środowisk LaTeX.
- Zachowano globalne zasady „suma zbiorów” i „warunek niezależności liniowej”; brak niedozwolonego słownictwa w treści.
- W rozdziale 04 nie użyto zewnętrznych grafik ani kodu; diagram jest wewnętrznym TikZ.
- Rozdział 04 wpisano do `books/pl/linear_algebra.tex`, `catalog/books.json` i `.github/workflows/linear-algebra-chapter.yml` z zachowaniem kolejności 01–04.
- CI po pierwszym audycie: [44905548745](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44905548745) — **wynik do uzupełnienia**.
- W całym repozytorium wcześniej występowały 24 zgłoszenia nieblokującego globalnego walidatora innych skryptów; nie są one traktowane jako rozstrzygnięte.

## Stan i kolejny krok

**Rozdział 04 utworzony, zintegrowany z książką i poddany pierwszemu audytowi. Pozostaje otwarty.**
Kolejne iteracje powinny już dotyczyć wyłącznie istniejącej treści rozdziału 04: poprawności matematycznej, języka, przykładów i rysunków, bez dodawania kolejnych tematów. Zamknięcie dopiero po audycie bez istotnych usterek i po pomyślnym CI.
