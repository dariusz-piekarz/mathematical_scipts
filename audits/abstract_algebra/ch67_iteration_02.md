# AA-67 — audyt II, etap P (otwarty)

24 listopada 2026 r. Audyt odczytanego źródła a79a86a0b97e7482f1f392bdeeb3f0633d87658f na gałęzi biblioteka-matematyczna-iteracja-6, HEAD odczytu 44232152ec8a46a9be82537a3eff92643a30a01d. AA-66 zamknięty według ch66_iteration_04.md. AA-68 nieotwarty.

## Niezależna kontrola matematyczna
- Własność uniwersalna: jednorodny ideał Serre'a nie zawiera stopnia zerowego; rekurencja e_i i h_i jest zgodna z relacjami, a obraz zawiera cykliczny generator. Nie zakłada się skończonego wymiaru V.
- Największy właściwy podmoduł: interpolacja dotyczy wyłącznie skończonego nośnika pojedynczego wektora; suma dowolnej rodziny podmodułów oznacza skończone sumy elementów i nadal nie zawiera najwyższej składowej.
- Lokalna nilpotentność: dla singularnego wektora wykładnik m_i+1 zeruje współczynnik e_i; dla i≠j komutator znika. W formule dwumianowej granica p≥b+m_i jest poprawna, bo k<b implikuje p−k≥m_i+1. Poprawiono zbyt skrótowe przejście od rozkładu podmodułu N do rozkładu Q: jawny izomorfizm sumy prostej ilorazów, surjekcja, iniekcja i identyfikacja przestrzeni wagowych.
- Symetria wag: skończoność rozpiętości f^a e^b u wynika kolejno z lokalnej nilpotentności e i f, a komutator ef^a daje stabilność bez założenia, że u jest wektorem najwyższej wagi. Rozkład h=Kh_i⊕ker α_i przenosi zmianę znaku wartości własnej do odbicia prostej wagi.
- Skończoność: średnia po W jest zerowa, gdyż h_i tworzą bazę; współczynniki |W|λ w bazie prostych korzeni są ustalone i nieujemne całkowite, ponieważ λ jest wagą Q. Ograniczenie k_j≤b_j obejmuje układy redukowalne. Nie porządkuje się ciała K.
- Prostota Q: pełna redukowalność stosowana dopiero po dowodzie skończoności; rzuty generatora na wszystkie składniki muszą być niezerowe, a jednowymiarowa najwyższa przestrzeń dopuszcza tylko jeden składnik. Przykład sl2 obejmuje m=0 i poprawnie wykorzystuje niezerowość współczynników w charakterystyce zero.

Nie stwierdzono błędnej tezy. Poprawka dowodu oraz zdania językowego: cb4d90d1e66d6f130d7fe1b861636aa29e156466, nowy blob a9826b69f53405b297cba48deb368088ed447036; zachowano wszystkie etykiety.

## Wykonane regresje
Oba istniejące skrypty pobrano z przypiętego HEAD i rzeczywiście wykonano w środowisku JavaScript:
- test_abstract_algebra_ch67.js, blob d9bd1b68e98e810cc31925ee8d8ee63b73df583d: PASS (21 modeli sl2, 231 kontroli komutatora, 231 jąder, 15 modeli A2, 182 łączny wymiar, 155 przestrzeni wagowych, 310 symetrii, 30 relacji najwyższej wagi).
- test_abstract_algebra_ch67_independent.js, blob ae760b53bd8774a1937eb2f33de5a71d4c837fa4: PASS (7 układów, 104 elementy grup, 196 wag dominujących, 5096 elementów orbit z krotnościami, 16087 zaakceptowanych i 30981 odrzuconych kandydatów, 138012 kontroli współczynników).
- AA-67-QW-01, aa:lem:verma-integrable: nowa regresja w pierwszym z powyższych plików, commit e9de9e27fa521d6a28af375f6f7bf6373b99af22, blob c0b8ba0f08e218b870555011654d881a8d2c1a4d. Kryteria: dokładne projekcje Lagrange'a na skończonych nośnikach, zachowanie projekcji przez rzut ilorazowy, znikanie odrzuconych wag i odtworzenie wektora jako sumy składowych. Wykonano cały rozszerzony skrypt: PASS, w tym 81 nośników, 405 projekcji, 2565 kontroli współrzędnych. Jest to test modelu rzędu jeden, nie dowód ogólny ani formalizacja Lean. Istniejący workflow wywołuje oba skrypty.

## Bramka stabilizacyjna
CI 45453883918 był w toku dla head 70029c02508334fef83515d59a2fb0c286c458d7 przed poprawkami; brak potwierdzonego pełnego CI dla poprawionego źródła. Nie oglądano nowego PDF ani nie uruchamiano Lean. Nie deklarować stabilizacji AA-67. Następny krok: potwierdzić pełny CI na poprawionym źródle, sprawdzić wszystkie strony AA-67 w PDF i przeprowadzić niezależny audyt potwierdzający po korekcie przed otwarciem AA-68.
