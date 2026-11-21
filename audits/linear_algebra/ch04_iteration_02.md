# Algebra liniowa — rozdział 04, audyt 2

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex`  
**Commit końcowej poprawki treści:** `af94b6bdf6911591fcd2af6f888f9e6668b84ad0`

## Cel i ograniczenia

Drugi audyt objął **wyłącznie poprawność już istniejących definicji, twierdzeń, dowodów, przykładów i diagramów**. Nie wprowadzono nowych tematów, lematów ani twierdzeń. Zachowano wszystkie istniejące nazwy etykiet oraz porządek rozdziału. Sprawdzano zgodność ze standardem pełnych, samodzielnych założeń i uzasadnionych kroków dowodowych.

## Stwierdzone i poprawione niepełne założenia

### 1. Wzór współrzędnych i jednoznaczność macierzy (`thm:lin4-wspolrzedne-macierz`)

Dotychczasowe „Niech \(V,W,B,C,T\) będą jak w Definicji...” nie podawało samodzielnie ani ciała skalarów, ani wymiarów, ani uporządkowania baz, ani liniowości \(T\). Tezę sformułowano ponownie z jawnymi:
- przestrzeniami \(V,W\) nad \(K\), o wymiarach \(n,m\in\mathbb N_0\);
- uporządkowanymi bazami \(B=(b_1,\ldots,b_n)\) i \(C=(c_1,\ldots,c_m)\);
- liniowym odwzorowaniem \(T\colon V\to W\).

Formuła \([T(v)]_C=[T]_{C\leftarrow B}[v]_B\) i dowód pozostały niezmienione.

### 2. Twierdzenie i wniosek o rzędzie (`thm:lin4-rzad-kolumn`, `cor:lin4-kryteria-kolumn`)

Do obu sformułowań dopisano jawne \(m,n\in\mathbb N_0\). Wymiary zerowe są więc formalnie uwzględnione w założeniach, zgodnie z dowodami. Nie zmieniono wyników o przestrzeni rozpiętej przez kolumny, jądrze, rzędzie ani kryteriach iniektywności i surjektywności.

### 3. Twierdzenie o współrzędnych przy zmianie bazy (`thm:lin4-zmiana-wspolrzednych`)

Zastąpiono odwołanie do definicji jako jedyne źródło hipotez samodzielnym wskazaniem \(V\) nad \(K\), wymiaru \(n\in\mathbb N_0\), dwóch uporządkowanych baz \(B,B'\). Wzory
\([v]_B=P_{B\leftarrow B'}[v]_{B'}\) oraz
\(P_{B'\leftarrow B}=P_{B\leftarrow B'}^{-1}\)
i dowód pozostały bez zmian.

### 4. Definicje działań punktowych i macierzy przejścia

W `def:lin4-dzialania-punktowe` dopisano \(m,n\in\mathbb N_0\), co zamyka zakres dwóch parametrów w definicji \(A+B\) i \(cA\). W `def:lin4-przejscie` jawnie podano \(n\in\mathbb N_0\), zgodnie z istnieniem pustej bazy przy wymiarze zerowym.

**Wszystkie sześć miejsc to luki formalne w kwantyfikacji i samodzielności sformułowań, nie fałszywe twierdzenia.**

## Powtórna kontrola poprawności istniejącego materiału

- **Macierze i działania na kolumnach:** poprawność struktury wektorowej \(\operatorname{Mat}_{m\times n}(K)\), konstrukcji bazy \(E_{ij}\), wzoru \((Ax)_i=\sum_j a_{ij}x_j\), z uwzględnieniem pustych indeksów.
- **Macierz liniowego odwzorowania:** kolumny to współrzędne obrazów bazowych. Dowód \([T(v)]_C=A[v]_B\) korzysta tylko z sum skończonych i jednoznaczności współrzędnych. Przy ustalonych bazach każda macierz wyznacza dokładnie jedno \(T\).
- **Iloczyn i składanie:** skontrolowano kolejność \([T\circ S]_{C\leftarrow D}=[T]_{C\leftarrow B}[S]_{B\leftarrow D}\), łączność, rozdzielność i obie jednostki \(I_m,I_n\). Dowody działają w wymiarze zero, ponieważ odpowiednie sumy są puste.
- **Rząd i odwracalność:** obraz \(L_A\) jest rozpięty przez kolumny; jądro odpowiada zerowym kombinacjom. Wzór \(n=\dim\ker A+\operatorname{rk}A\) jest poprawny. Pięć kryteriów odwracalności macierzy kwadratowej pozostaje równoważnych, także przy \(n=0\).
- **Zmiana bazy:** macierz \(P_{B\leftarrow B'}\) przelicza współrzędne z \(B'\) do \(B\). Dla dwóch niezależnych zmian baz dziedziny i przeciwdziedziny poprawna jest kolejność \(Q^{-1}AP\). Dla endomorfizmu uzyskujemy podobieństwo \(P^{-1}AP\), bez utożsamiania operatora z jego reprezentacją.
- **Transpozycja:** sprawdzono \((AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}\), poprawność indeksów, brak sprzężenia zespolonego i dowód dla macierzy o zerowych rozmiarach.
- **Układy liniowe:** rozwiązalność \(Ax=b\iff b\in\operatorname{im}A\), wszystkie rozwiązania \(x_0+\ker A\), przypadek jednorodny i przykład parametryzacji są poprawne.

Ponownie obliczono liczbowo przykłady: odwrotności macierzy \(2\times2\), przejścia między bazami, macierzy podobnych oraz działania prostokątnej macierzy na wskazaną kolumnę. Uzyskano dokładnie wyniki zapisane w rozdziale. Nie wykryto błędu merytorycznego w istniejących wynikach.

## Niezależny test wzoru zmiany dwóch baz

Przeprowadzono wyczerpujący test nad \(\mathbb F_2\) dla odwzorowań \(T\colon\mathbb F_2^2\to\mathbb F_2^3\):
- wszystkie \(64\) macierze \(A\in\operatorname{Mat}_{3\times2}(\mathbb F_2)\);
- wszystkie \(6\) macierzy \(P\in\operatorname{GL}_2(\mathbb F_2)\);
- wszystkie \(168\) macierzy \(Q\in\operatorname{GL}_3(\mathbb F_2)\).

Dla wszystkich **64512** trójek \((A,P,Q)\), a następnie wszystkich wektorów \(x\in\mathbb F_2^2\), porównano wynik działania \(Q^{-1}APx\) z \(Q^{-1}(A(Px))\).

**Wynik: 0 niezgodności**. Te obliczenia wspierają kontrolę, ale nie zastępują ogólnego dowodu.

## Spójność książki i kontrola techniczna

- Cztery rozdziały mają łącznie **199 unikalnych etykiet**, bez duplikatów. Rozdział 04 zachował **49 etykiet**.
- Wszystkie **86** wystąpień `\\ref` i `\\eqref` w aktualnej treści czterech rozdziałów mają istniejące cele. Liczba zmniejszyła się względem audytu 1 o dwa odsyłacze, zastąpione pełnymi założeniami w dwóch twierdzeniach.
- Wszystkie `\\begin`/`\\end` są prawidłowo zagnieżdżone; brak niedomkniętych środowisk.
- Nie wprowadzono niedozwolonych określeń „unia” oraz „relacja liniowa”.
- Zachowano diagramy TikZ, katalog rozdziałów i importy w kolejności 01–04; brak nowych zewnętrznych grafik.
- CI dla ostatniej zmiany treści: [44906175706](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44906175706) — **success**. Wszystkie kroki walidacji rozdziałów 01–04, importów, katalogu, terminologii, kompilacji dwukrotnej i weryfikacji odsyłaczy oraz zapis artefaktu zakończyły się sukcesem. Końcowy PDF ma **49 stron A4**. W końcowym `linear_algebra.log` nie występują `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `Undefined control sequence`, `Fatal error` ani `There were undefined references`. Wyrenderowano i wizualnie obejrzano strony **38, 40, 41, 44, 46 i 49**, obejmujące zmienione definicje, twierdzenia, diagram współrzędnych i podsumowanie. Nie wykryto ucięć, nakładania napisów ani uszkodzonych symboli.
- Poprzedni przebieg po pierwszej partii poprawek: [44906054316](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44906054316) — **success**.
- W nieblokującym, globalnym walidatorze innych skryptów utrzymują się **24 wcześniejsze problemy** (potwierdzone w logu tego przebiegu), niezwiązane z algebrą liniową; nie deklarujemy ich naprawy.

## Status

**Audyt 2 rozdziału 04 zakończony z poprawkami formalnymi. Rozdział pozostaje otwarty**, zgodnie z zasadą wymagającą ponownej iteracji bez istotnych błędów przed zamknięciem. Następny audyt ma sprawdzać tylko aktualną treść, bez nowych tematów.
