# Topologia ogólna — rozdział 12, audyt niezależny 04 (dowód po dowodzie)

**Data:** 2026-11-22.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/12-przestrzenie-jednostajne.tex`.
**Audytowany blob:** `13597073db07742089b82ae3fc9878733dea5e88`.
**Zakres:** niezależna kontrola wszystkich **14 środowisk `proof`**, hipotez twierdzeń, ważnych przypadków brzegowych, przykładów, zależności i ilustracji 12.1. Rozdział pozostaje bez zmian.

## Kontrola wszystkich dowodów (14/14)

| Nr | Etykieta | Niezależna kontrola |
|---:|---|---|
| 1 | `lem:topog-jednostajne-symetryczne` | Dla `V ∘ V ⊆ E` relacja `F=V∩V⁻¹∩E∩E⁻¹` jest symetryczna, należy do filtra jednostajnego, zawiera przekątną i spełnia `F∘F⊆E`; istotne jest jednoczesne przecięcie z odwrotnością. |
| 2 | `thm:topog-jednostajne-topologia` | Sprawdzone ∅, X, sumy i przecięcia skończone. Dla `W={y: ∃D∈U, D[y]⊆E[x]}` mamy `x∈W⊆E[x]`; gdy `y∈W` i `F∘F⊆D`, to dla `z∈F[y]` zachodzi `F[z]⊆E[x]`, więc `z∈W`. Dowód poprawnie rozróżnia bazę *otoczeń* i bazę zbiorów otwartych. |
| 3 | `thm:topog-jednostajne-hausdorff` | Hausdorff ⇒ rozdzielanie wynika z otwartego zbioru zawierającego x, lecz nie y. W drugą stronę wybór symetrycznego F z `F∘F⊆E` daje `F[x]∩F[y]=∅`; przejście do rozłącznych *otwartych* otoczeń jest jawne. |
| 4 | `cor:topog-jednostajne-skrajne-topologie` | Przekroje jedynej relacji niedyskretnej mają postać X, zaś przekroje przekątnej są singletonami; przypadek X pustego nie tworzy wyjątku. |
| 5 | `thm:topog-jednostajne-pseudometryka` | Aksjomaty struktury wynikają z bazowych `E_ε`, przecięć i nierówności trójkąta `E_(ε/2)∘E_(ε/2)⊆E_ε`. Przekroje są kulami pseudometrycznymi; przecięcie całego filtra relacji odpowiada warunkowi `p(x,y)=0`. |
| 6 | `thm:topog-jednostajne-podprzestrzen` | Struktura śladowa zachowuje przekątną, symetrię, przecięcia oraz warunek małego złożenia. Równość przekrojów `(E∩(A×A))[a]=E[a]∩A` daje obie inkluzje baz otoczeń dla topologii względnej, również gdy A jest puste. |
| 7 | `thm:topog-jednostajne-iloczyn` | Przecięcia relacji kontrolują sumę dwóch skończonych zbiorów współrzędnych; złożenia kontroluje się współrzędnie. Przekroje są skończonymi cylindrami, z których w obu kierunkach odzyskuje się topologię produktową. Przeciwobraz każdej relacji jednostajnej przez `π_i×π_i` należy do struktury produktu. |
| 8 | `thm:topog-jednostajne-ciaglosc-wlasnosci` | Z `f(E[x])⊆V[f(x)]` i faktu, że `E[x]` jest otoczeniem, wynika ciągłość. Przy składaniu relacje dobiera się od przeciwdziedziny Z przez Y do X, zachowując kwantyfikatory. |
| 9 | `lem:topog-jednostajne-zwarta-ciagowa` | Domknięcia ogonów `F_N` są niepuste, domknięte i zstępujące; zwartość daje punkt w ich przecięciu. Rekurencja `n_k>n_(k-1)` i `d(x_(n_k),x)<1/k` rzeczywiście tworzy zbieżny podciąg. |
| 10 | `thm:topog-jednostajne-heine-cantor` | Negacja warunku jednostajnego dostarcza par oddalonych o mniej niż 1/n, których obrazy pozostają oddalone o co najmniej ε₀. Podciąg x_(n_k) ma granicę, y_(n_k) ma tę samą, co przeczy ciągłości f. |
| 11 | `thm:topog-jednostajne-ogony` | Niepustość i skierowanie D zapewniają, że zbiory ogonowe stanowią bazę właściwego filtra; każda inkluzja `A_α⊆A` jest używana we właściwym kierunku. |
| 12 | `thm:topog-jednostajne-zbiezna-cauchy` | Symetria F pozwala przejść od `x_α,x_β∈F[x]` do `(x_α,x_β)∈F∘F⊆E`; niepotrzebna jest Hausdorffowość. |
| 13 | `prop:topog-jednostajne-f-cauchy` | Dla dowolnej relacji V w Y dobiera się E w X z `(f×f)(E)⊆V`; ogon sieci Cauchy'ego w X przechodzi na ogon w Y. |
| 14 | `thm:topog-jednostajne-produkt-cauchy` | W kierunku prostym działa jednostajna ciągłość rzutowań; w odwrotnym skończoność F pozwala znaleźć wspólną górną granicę indeksów `α_i`. Dla F pustego warunek jest automatyczny. |

## Kontrola przykładów, hipotez i granic

- Dwie skrajne struktury są zgodne z przyjętą definicją również na zbiorze pustym; dla niepustego zbioru struktura dyskretna jest filtrem wszystkich relacji zawierających przekątną.
- Metryki `d(x,y)=|x−y|` i `e(x,y)=|arctan x−arctan y|` mają tę samą topologię, ale nie tę samą strukturę jednostajną: pary (n,n+2) obalają inkluzję wymaganą do równoważności struktur.
- Dla `f(x)=x²`, pary `(n,n+1/n)` mają odległość argumentów zbieżną do 0, ale odległość obrazów nie mniejszą niż 2.
- W przykładzie na (0,1) ciąg `1/(n+1)` jest Cauchy'ego, lecz nie ma granicy we wskazanej przestrzeni.
- W niedyskretnej strukturze na zbiorze co najmniej dwupunktowym sieci mogą mieć wiele granic. Nie używa się niejawnie T1.
- W strukturze od metryki `e` ciąg n jest Cauchy'ego, chociaż nie jest Cauchy'ego dla `d`. To poprawnie pokazuje, że topologia nie wyznacza pojęcia Cauchy'ego.
- Produkt pustej rodziny ma jeden punkt; produkt zawierający czynnik pusty jest pusty. Oba są uwzględnione bez sztucznego założenia niepustości wszystkich czynników.
- Zależność od twierdzenia o własności skończonych przecięć w rozdziale 07 jest dostępna; lemat o zwartości ciągowej nie opiera się na przyszłych wynikach z rozdziału 13.

## Kontrola kompilacji i ilustracji

Dla artefaktu GitHub Actions `45068776546`, commit `0fd629c07b0366c238720db3d4253f2ec7103122` (zakończenie `success`), pobrano artefakt `14771719456` (`general-topology-ch01-ch26`).
Samodzielny `general_topology_ch12.pdf` liczy 6 stron; pełne wydanie liczy 188 stron. Na stronie 96 pełnej książki sprawdzono ilustrację 12.1: pas `|x−y|<0,8`, przekątna, przerywane brzegi, podpis i oznaczenia są czytelne. W logach PDF nie wykryto `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning` ani `Undefined control sequence`.

Drzewa Git commitu artefaktu oraz bieżącej gałęzi porównano w obrębie wszystkich 26 rozdziałów topologii ogólnej — identyfikatory blobów źródłowych są takie same. Wynik oględzin dotyczy zatem obecnego źródła książki, mimo że jego najnowszy commit gałęzi może mieć inny SHA z powodu równoległych prac.

## Wynik

**PASS: 14/14 dowodów, skontrolowane przykłady, hipotezy i przypadki brzegowe, ilustracja 12.1 oraz skład rozdziału 12.**
W tej iteracji nie znaleziono błędu wymagającego zmiany tekstu ani nie zmodyfikowano źródła rozdziału 12. Jest to **czwarty, niezależny audyt** niezmienionego bloba; nie należy go mylić z automatyczną formalną weryfikacją dowodów.

**Dalszy etap:** analogiczna niezależna kontrola wszystkich dowodów rozdziału 13 (w szczególności minimalizacja filtrów Cauchy'ego, konstrukcja uzupełnienia i własność uniwersalna), następnie kolejnych rozdziałów.
