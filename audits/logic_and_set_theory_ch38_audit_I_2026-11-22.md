# Logika matematyczna i teoria mnogości — audyt I rozdziału 38

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/38-kardynaly-mahla-i-slaba-zwartosc.tex.  
**Blob źródła:** d0d176bf1d4cbb8426cedcf02fbbd3a28510a152.  
**Werdykt:** **NIECZYSTY TECHNICZNIE**. Pierwsze CI wykryło zbyt restrykcyjną asercję w nowym teście. Kontrola matematyczna nie wykazała konieczności zmiany treści rozdziału. Licznik czystych audytów: 0.

## 1. Kontrola matematyczna

1. **Zbiory klubowe.** Definicja zawiera osobno domkniętość i nieograniczoność. W lemacie o przecięciu mniej niż κ klubów regularność κ gwarantuje ograniczenie supremów wszystkich etapów konstrukcji. W lemacie o przecięciu diagonalnym przy ustalonym ξ<δ wszystkie dostatecznie późne wyrazy należą do Cξ, co uzasadnia domkniętość i nieograniczoność.
2. **Lemat Fodora.** Dla niestacjonarnych włókien regresywnej funkcji wybiera się kluby Cξ rozłączne z każdym włóknem. Stacjonarność i diagonalne przecięcie klubów dają α∈S∩D, a f(α)<α sprzeczność α∈C_{f(α)} i α∉C_{f(α)}. Punkt 0 można usunąć przez przecięcie z klubowym ogonem.
3. **Kardynały Mahla.** Poprawnie odróżniono stacjonarność zbioru nieosiągalnych od jego samej nieograniczoności; dowód, że kardynał Mahla jest granicą nieosiągalnych, stosuje klubowe ogony.
4. **Własność drzewa.** Dla κ mierzalnego i κ-drzewa T zanurzenie j daje węzeł na poziomie κ drzewa j(T). Małość każdego poziomu Tα pozwala zapisać j(Tα) jako obrazy jego węzłów. Z poprzedników wybranego węzła odtwarza się gałąź wszystkich poziomów T. Wykorzystanie zastępowania przy zebraniu gałęzi jest jawne.
5. **Normalność a kluby.** Jeżeli dopełnienie klubu byłoby duże, funkcja α↦sup(C∩α) na odpowiednim ogonie byłaby regresywna; normalność wymusza stałe duże włókno, sprzeczne z nieograniczonością C.
6. **Mierzalność implikuje Mahlę.** Sprawdzono osobno fakt, że κ jest silnie nieosiągalny także w tranzytywnej klasie M: wewnętrzne świadectwo singularności, niekardynalności albo braku silnej graniczności byłoby świadectwem również w V. Z elementarności κ∈j(Iκ), zatem Iκ należy do normalnej miary zawierającej wszystkie kluby.
7. **Relacja podziałowa.** Każdy ogon rozdziela się na dwa zbiory kolorów, z których dokładnie jeden jest w ultrafiltrze; jeden kolor dominuje na dużym zbiorze indeksów. κ-zupełność i uniformność pozwalają wybrać przez rekurencję długości κ jednorodny zbiór.

## 2. Testy i usterka CI

Rozdział wpisano jako 38. pozycję katalogu i zaimportowano do książki. Nowy workflow sprawdza pełną kompilację, 952 etykiety i 738 odsyłaczy oraz dziewięć metod testowych rozdziału 38. W pierwszym przebiegu **[GitHub Actions 45068599036](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068599036)** wystąpił błąd: test wymagał dosłownego odsyłacza do konkretnego twierdzenia o normalnym ultrafiltrze z rozdziału 37, podczas gdy tekst odsyłał do poprawnej sekcji źródłowej. Usterka była wyłącznie w teście. Asercję zastąpiono sprawdzeniem rzeczywiście występującej referencji do twierdzenia o nieosiągalności kardynałów mierzalnych, commit **1f388905f167fb1b10faf8864e43b0387b81b41b**. Nowy przebieg: [45068706353](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068706353); status końcowy trzeba potwierdzić przed zaliczeniem technicznym.

W regresjach sprawdza się również **32768** dwukolorowań par zbioru sześcioelementowego w celu potwierdzenia R(3,3)=6, a kolorowanie pięciokąta jest kontrprzykładem dla pięciu wierzchołków. To skończone przykłady, nie dowód twierdzeń o dużych kardynałach.

## 3. Inwentarz i następny krok

Inwentarz: **641 wierszy, 26 etykiet, 19 odsyłaczy, 8 definicji, 4 lematy, 5 twierdzeń, 1 wniosek, 5 uwag, 2 przykłady i 10 dowodów**. Terminologia zgodna ze standardem projektu; bez niezatwierdzonych rozszerzeń o pełne charakterystyki słabej zwartości.

Ponieważ wykryto konieczną korektę regresji, audyt I pozostaje technicznie nieczysty. Po zielonym CI wykonać audyty II i III oraz dodatkowy audyt IV dla pewności na niezmienionym źródle. Kompilacja Python i LaTeX nie jest formalizacją w Lean.
