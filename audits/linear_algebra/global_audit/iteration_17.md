# Algebra liniowa — audyt globalny, iteracja 17: indywidualny przegląd wszystkich dowodów LA01–02

**Data:** 22 listopada 2026. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Kontynuacja:** [iteracja 16](iteration_16.md).
**Decyzja:** **CZYSTY W ZBADANYM ZAKRESIE**; żaden z 40 przeczytanych dowodów LA01–02 nie wymagał korekty matematycznej. **Pełny audyt globalny 382 dowodów pozostaje otwarty**.

## 1. Zamrożony zakres

| Rozdział | Blob SHA | Wiersze | Dowody \`proof\` | Etykiety | Odsyłacze | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LA01 — Przestrzenie wektorowe | \`374e74dfa46f72597abcb8f5721268fed2245c4a\` | 1722 | **24 / 24 przejrzane** | 69 | 27 | 2 |
| LA02 — Wymiar, sumy i ilorazy | \`1e59c0d13379ee7851f3a6386172640b02f9fa75\` | 1089 | **16 / 16 przejrzanych** | 39 | 17 | 1 |
| **Łącznie** | | **2811** | **40 / 40** | **108** | **44** | **3** |

Dla każdego z **40 dowodów** odczytano pełne sformułowanie twierdzenia oraz całe odpowiadające środowisko \`proof\`, porównano założenia i kolejne wnioskowania, sprawdzono wymagane przypadki brzegowe i odsyłacze do użytych wyników. Szczegółowa imienna ewidencja, z etykietami i zakresami wierszy, jest w [rejestrze iteracji 17](iteration_17_proof_review_01_02.csv). Kolumna \`Lean_formalization_assessed_here=NIE\` oznacza, że nie badano w tej iteracji uruchomień ani zgodności formalizacji Lean. **Nie jest to certyfikat formalny każdego twierdzenia, mimo indywidualnej niezależnej lektury dowodów.**

Wytyczne \`AGENTS.md\` pozostają zachowane: nie rozszerzano żadnego zatwierdzonego rozdziału, nie zmieniano historycznych \`\\label\`, odróżniano sumę mnogościową zbiorów od sumy algebraicznej podprzestrzeni i nie nazywano równości z warunku niezależności „relacją liniową”.

## 2. Niezależna kontrola 24 dowodów LA01

1. **Aksjomaty i podprzestrzenie:** lemat o konsekwencjach aksjomatów rozdziela \(0_K\) i \(0_V\); kryterium podprzestrzeni wykorzystuje konieczną niepustość. Przecięcie pustej rodziny przy przyjętej konwencji daje \(V\), podczas gdy suma mnogościowa skierowanej rodziny wymaga indeksu \`I\` niepustego. Oba twierdzenia o sumach zbiorów podprzestrzeni nie są mylone z ich sumą algebraiczną.
2. **Skończone pokrycie przez właściwe podprzestrzenie:** minimalne podpokrycie zapewnia wektory \(x,y\) należące do różnych właściwych składników; dla każdego pozostałego składnika co najwyżej jeden parametr \(t\) może należeć do niego. **Założenie, że ciało jest nieskończone, jest konieczne**: w \(\mathbb F_2^2\) suma mnogościowa trzech prostych jest całą przestrzenią. Ten kontrprzykład **już jest** w LA01 (\`prz:lin-unia-trzech-f2\`), nie proponujemy niepotrzebnego powtórzenia.
3. **Rozpinanie i niezależność:** \`thm:lin-span-minimalny\`, \`prop:lin-span-reguly\`, \`lem:lin-niezaleznosc-kryteria\`, \`prop:lin-skonczony-charakter\`, \`cor:lin-podrodziny\` rozdzielają reprezentacje ze skończonym nośnikiem od reprezentacji rodzin indeksowanych. W tezie o dokładnie jednym zestawie współczynników indeksy są ustalone, a w dowodzie duplikujące się indeksy są łączone przed użyciem niezależności.
4. **Wymiar skończony bez AC:** \`lem:lin-usuwanie-generatorow\`, \`thm:lin-steinitz\`, \`thm:lin-uzupelnianie-skonczone\`, \`cor:lin-baza-kryteria\`, \`thm:lin-skonczona-wymiarowosc\`, \`thm:lin-wymiar-podprzestrzeni\` używają tylko skończonych wyborów. W wymianie Steinitza po \(k\) krokach konieczny niezerowy współczynnik przy jeszcze niewymienionym generatorze jest jawnie uzasadniony niezależnością \(v_1,\ldots,v_{k+1}\). Uwzględniono \(m=0\), \(r=0\), \(n=0\).
5. **Bazy Hamela i AC:** \`lem:lin-lancuchy\`, \`thm:lin-istnienie-bazy-zorn\`, \`thm:lin-baza-z-generatorow-zorn\` sprawdzają niepustość częściowo uporządkowanej rodziny, także ograniczenie górne pustego łańcucha, oraz argument rozszerzenia maksymalnej rodziny spoza jej rozpiętości. AC jest jawne. \`thm:lin-wspolrzedne-hamela\` dowodzi bijektywności i liniowości \(V\to K^{(I)}\), także dla \(I=\varnothing\). \`thm:lin-charakterystyki-bazy\` poprawnie łączy maksymalną niezależność z minimalnym rozpinaniem.

**Wniosek LA01:** wszystkie **24/24** sformułowania i dowody objęte indywidualnym audytem; nie stwierdzono luki powodującej konieczność poprawki źródła.

## 3. Niezależna kontrola 16 dowodów LA02

1. **Dowolne bazy:** \`lem:lin2-nosnik\` pozwala odzyskiwać podprzestrzeń z nośników współrzędnych. \`lem:lin2-moce-nosnikow\` poprawnie wykorzystuje AC i dobre uporządkowanie do iniekcji sumy skończonych zbiorów w \(I\times\mathbb N_0\), gdy \(I\) jest nieskończony. \`thm:lin2-jednakowa-moc-baz\` osobno analizuje przypadek skończony i nieskończony, a w tym drugim używa dwóch oszacowań i Cantora–Bernsteina.
2. **Suma algebraiczna:** \`thm:lin2-suma-minimalna\` i \`prop:lin2-rachunek-sum\` są prawdziwe również przy rodzinie pustej dzięki przyjętej konwencji. \`thm:lin2-wzor-wymiarowy\` konstruuje bazę z dwóch rozszerzeń bazy \(U\cap W\); przy wymiarach nieskończonych stosuje wyłącznie **dodawanie kardynalne**, a nie odejmowanie.
3. **Suma prosta:** \`thm:lin2-kryteria-sumy-prostej\` prawidłowo odróżnia \(\bigcap\) od warunku \(U_j\cap\sum_{i\ne j}U_i=\{0\}\); zerowe przecięcia par **nie wystarczają** dla trzech składników (gotowy kontrprzykład jest w LA02). \`thm:lin2-zewn-wewn\` opisuje dokładnie jądro sumowania, a \`thm:lin2-wymiar-sumy-prostej\` liczy indeksy baz jako rozłączne pary.
4. **Warstwy i ilorazy:** \`lem:lin2-warstwy\`, \`thm:lin2-struktura-ilorazu\`, \`prop:lin2-iloraz-przypadki\`, \`thm:lin2-wlasnosc-ilorazu\` sprawdzają dobrą określoność przez równoważność \(v+U=w+U\iff v-w\in U\), a w ostatnim dowodzie także jednoznaczność odwzorowania indukowanego. Brak konieczności AC przy samej własności uniwersalnej.
5. **Dopełnienia, wzory wymiarowe i drugi izomorfizm:** \`thm:lin2-istnienie-dopelnienia\` używa AC tylko w wymiarze dowolnym; wersja skończona go nie potrzebuje. \`thm:lin2-iloraz-dopelnienie\` dowodzi bijektywności \(\Theta:W\to V/U\) i rozdziela odejmowanie wymiarów naturalnych od kardynalnych. \`thm:lin2-iloraz-sumy\` konstruuje naturalną mapę \(U/(U\cap W)\to(U+W)/W\) i sprawdza jądro oraz surjektywność.

**Wniosek LA02:** wszystkie **16/16** sformułowań i dowodów objęte indywidualnym audytem; brak nieprawidłowości wymagających zmiany.

## 4. Nowy wyczerpujący kontrtest nad małymi ciałami

Wykonano rzeczywiście nowy skrypt \`tools/test_linear_algebra_la01_la02_exhaustive.py\` (ten sam kod badawczy uruchomiony lokalnie jako \`/mnt/data/la_global17_finite_checks.py\`; SHA256 lokalnego pliku \`b7772749302d1c0ad2bdacf0f664750272f738f5b8e1a6a9a3627546ce39fbdd\`).

| Przestrzeń | Liczba wszystkich podprzestrzeni | Liczba uporządkowanych par |
| --- | ---: | ---: |
| \(\mathbb F_2^2\) | 5 | 25 |
| \(\mathbb F_2^3\) | 16 | 256 |
| \(\mathbb F_2^4\) | 67 | 4489 |
| \(\mathbb F_3^2\) | 6 | 36 |
| \(\mathbb F_3^3\) | 28 | 784 |
| **Razem** | | **5590** |

Regresja generuje **wszystkie podprzestrzenie** każdego z tych pięciu modeli przez enumerację niezależnych rodzin. Dla wszystkich **5590 par** sprawdza:
- zamknięcie sumy i przecięcia na działania;
- równość \(\dim(U+W)+\dim(U\cap W)=\dim U+\dim W\);
- kryterium \(U\oplus W\iff U\cap W=\{0\}\);
- równość liczności odpowiadającą drugiemu twierdzeniu o izomorfizmie;
- dobrze określoną i bijektywną mapę \(U/(U\cap W)\to(U+W)/W\).

Dodatkowo sprawdza konstrukcję baz przez dołączanie generatorów, klasy warstw i ich rozłączność, jednoznaczność współrzędnych bazowych oraz kontrprzykład z trzema prostymi w \(\mathbb F_2^2\).

**Wynik lokalnego wykonania: 44 904 / 44 904 PASS, 0 FAIL**; zestaw zawiera **10 567** osobnych testów niezależności wartości mapy ilorazowej od przedstawiciela warstwy.

Testy są skończonymi modelami, nie dowodem twierdzenia o dowolnych nieskończonych bazach ani formalizacją AC.

## 5. LaTeX, terminologia, rysunki i CI

- Źródła LA01–02 i ich stabilne SHA **nie zostały zmienione**. W sumie **108 etykiet i 44 odsyłacze**; w zbadanych plikach brak powtórzonych etykiet i nieprawidłowo domkniętych środowisk. Globalna spójność 32 rozdziałów była osobno kontrolowana w iteracjach 10 i 15, a w tej iteracji nie powtarzano skanowania wszystkich 32 plików.
- W LA01 dawne słowo \`unia\` występuje tylko we **wcześniej istniejących stabilnych identyfikatorach** \`\\label\` / \`\\ref\`, nie w polskiej narracji. Rozróżnienie sumy mnogościowej i algebraicznej zachowano.
- Przejrzano źródła **3 rysunków TikZ** (podprzestrzeń a przesunięta prosta, niezależność w \(\mathbb R^2\), warstwy w ilorazie); opis odpowiada przedstawianym konstrukcjom. **Nie wykonano nowego renderingu ani nowej pełnej inspekcji wizualnej PDF** w tej iteracji.
- [GitHub Actions run 45056637221](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45056637221) ma **completed/success** na commicie \`e1b6c3add7fe58679e7eae0b1285f4952b0c8ef8\`, po iteracji 16. W szczególności kroki testów LA01–32, budowa książki PDF w dwóch przebiegach, rozstrzygnięcie odsyłaczy i eksport aktualnego rozdziału miały status **success**. To był CI dla **niezmienionych źródeł rozdziałów**, ale przed dodaniem tego raportu i nowego testu. Nie przypisujemy nowemu testowi sukcesu CI bez nowego przebiegu workflow.
- Nie zmieniano zatwierdzonych rozdziałów i nie resetowano stabilizacji LA12–32.

## 6. Status końcowy i następne kroki

**Iteracja 17: zakończona, czysta dla LA01 i LA02.** W [osobnym rejestrze 40 dowodów](iteration_17_proof_review_01_02.csv) każde sformułowanie i środowisko dowodu ma status indywidualnego przeglądu matematycznego **CZYSTY**. Jest to konkretny postęp w audycie globalnym i nie należy go utożsamiać z certyfikacją Lean.

**Iteracja 18:** analogiczny, szczegółowy i sceptyczny audyt pozostałych **42 dowodów LA03–05** (17 + 15 + 10), z niezależnymi testami rzędu, ilorazów, permutacji pivotów i przypadków zerowych. Potem indywidualny audyt LA12–13, a dopiero po ukończeniu globalnego rejestru jeden dodatkowy sceptyczny przegląd dla pewności. Nie dodawać opcjonalnych tematów do zamkniętych rozdziałów bez zgody użytkownika.
