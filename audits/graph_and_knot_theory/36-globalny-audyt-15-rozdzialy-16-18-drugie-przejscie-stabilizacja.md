# Teoria grafów i węzłów — audyt globalny 15: rozdziały 16–18, drugie przejście i stabilizacja

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Poprzednik:** [audyt 14](35-globalny-audyt-14-rozdzialy-16-18-pierwsze-przejscie.md).

## Werdykt

**Rozdziały 16–18: LOKALNIE STABILNE (PASS)** po dwóch przejściach
matematycznych i redakcyjnych, poprawkach źródeł, niezależnych
regresjach algebraicznych oraz rzeczywistym złożeniu i obejrzeniu PDF.
Weryfikacja jest **lokalna**: nie oznacza zakończenia szczegółowego
audytu matematycznego wszystkich 44 rozdziałów.
Zaawansowane twierdzenia z literatury, jawnie przyjęte w tekście,
nie są nazywane dowiedzionymi z wcześniejszych rozdziałów.
Stabilizacja dotyczy sprawdzonych obecnie wersji plików i
nie zastępuje formalnej weryfikacji w Lean.

## 16–17 — kontrola drugiego przejścia

- Rozdział 16: ponownie skontrolowano kryterium ogniw
  sklejonych trójkątów, potrzebę parowania wystąpień boków,
  spójność przez graf dualny, dodatniość dyskretnego Laplasjanu
  Hodge'a i rozkład ortogonalny kołańcuchów. Szczególną uwagę
  zwrócono na różnicę między transpozycją macierzy operatora
  brzegowego a operatorem sprzężonym zależnym od iloczynu
  skalarnego. Aktualny tekst zawiera wszystkie warunki.
- Rozdział 17: kontrola stopnia `2r` grafu Cayleya `F_r`,
  także `r=1`, lokalnej bijekcji gwiazd w dowodzie
  o wolnym działaniu na drzewie, generatora stabilnego
  w rozszerzeniu HNN, indeksów w drzewie Bassa–Serre'a
  i przykładu `BS(1,2)` o stopniu 3.
  Fundamentalne twierdzenie Bassa–Serre'a pozostaje
  świadomie przyjęte, wraz z osobną uwagą o zakresie dowodu.
- Niezależne modele z audytu 14 sprawdzają dokładne
  liczby Bettiego w trzech kompleksach przy dwóch
  ważonych iloczynach skalarnych oraz małe fragmenty
  grafów Cayleya i drzewa `C_2*C_3`.

## 18 — dowód niezmienniczości Arfa

**Uzupełnienie rzeczywistego przeskoku.**
Dla każdej z poprawionych w audycie 14 postaci
elementarnego powiększenia macierzy Seiferta zapisano
dokładnie formę kwadratową nad `F_2`:

`q_V'(x,s,t)=q_V(x)+s(u+v)^Tx+zs²+st`.

Zamiana współrzędnych
`t'=t+(u+v)^Tx+zs`
jest liniowym automorfizmem i sprowadza
nową formę do sumy `q_V(x)+st'`.
Płaszczyzna hiperboliczna `st'` ma Arfa zero.
Połączenie tego rachunku z udowodnionym już
lematem o sumie Gaussa i jawnie przyjętą
`S`-równoważnością macierzy Seiferta
uzasadnia niezależność niezmiennika od powierzchni.

Dla twierdzenia `thm:kt-arf-conway-slice`
oddzielono dwie przyjmowane przesłanki:
- klasyczne kryterium Arfa poprzez wartość
  symetrycznie znormalizowanego wielomianu
  Alexandera przy `t=-1` modulo 8;
- istnienie metabolizera dla formy Seiferta
  węzła typu slice.

Dokładnie wyprowadzono kongruencję
`Δ_sym(-1)≡1-4a_2 (mod 8)`
z `z²=t+t⁻¹-2=-4` i wniosek o Arf.
Dodatkowo wyjaśniono, dlaczego
forma kwadratowa zerująca się na
podprzestrzeni lagranżowskiej ma Arfa zero.
**Kryterium modulo 8 i twierdzenie
o metabolizerze pozostają jawnie przyjęte**:
rachunek kongruencji nie jest ich dowodem.

## 18 — addytywność rodzaju węzła

Poprzedni dowód nazbyt skrótowo eliminował okręgi
przecięcia minimalnej powierzchni Seiferta `F`
ze sferą dekomponującą `S`.
W nowym dowodzie dla każdego
`C⊂F∩S` pokazano, że
`lk(C,K)=0`, bo `C` można
przesunąć z `F` bez jej przecinania.
Gdyby `C` był istotną krzywą
na dwukrotnie nakłutej sferze `S∖K`,
rozdzielałby oba nakłucia i dawał
`lk(C,K)=±1` — sprzeczność.

Zatem każdy okrąg przecięcia ogranicza
dysk w `S∖K`. Najbardziej wewnętrzny
z tych dysków jest albo dyskiem
kompresującym `F`, co przeczy
minimalności rodzaju, albo ma brzeg
ograniczający także dysk na `F`
i może zostać usunięty przez standardową
izotopię w kuli rozłącznej z `K`.
Pozostaje jeden właściwie zanurzony łuk.
Po rozcięciu i domknięciu powierzchni
otrzymujemy
`χ(F_1')+χ(F_2')=χ(F)+1`,
a stąd
`g(F)=g(F_1')+g(F_2')`.
Dowód korzysta z klasycznej
nieściśliwości powierzchni
Seiferta minimalnego rodzaju,
której argument przez kompresję
został wyjaśniony.

Jedyność rozkładu węzła na czynniki
pierwsze (twierdzenie Schuberta)
nadal jest jawnie przyjmowana;
nie wyprowadza się jej z faktoryzacji
wielomianu Alexandera.

## 18 — prezentacja Wirtingera

Usunięto nieprecyzyjne uzasadnienie,
że sama suma komórek dwuwymiarowych
automatycznie tworzy powierzchnię zamkniętą
i wyjaśnia redundancję relatora.
Nowy tekst wskazuje wymaganą
**sferyczną tożsamość między relacjami**
w komórkowym dowodzie van Kampena:
iloczyn sprzężonych relatorów
`∏_j w_j r_j^{ε_j} w_j^{-1}=1`
w grupie wolnej, przy wystąpieniu
każdego relatora dokładnie raz.
Stąd jeden relator leży w domknięciu
normalnym pozostałych. Konstrukcja
tożsamości jako standardowego lematu
geometrycznego jest jawnie zaznaczona
jako przyjęty krok; nie przypisuje się
wcześniejszemu skrótowi statusu
samodzielnego dowodu.

## 18 — dane peryferyjne

Dodano definicję `def:kt-peripheral`
meridianu, preferowanej długości
i pary peryferyjnej oraz
stwierdzenie `thm:kt-peripheral-homology`.
Dowód wykorzystuje torus
`∂N(K)`, powierzchnię Seiferta
i algebraiczne przecięcie:
klasy meridianu i długości
tworzą bazę `H_1(∂X_K;Z)`,
a odwzorowanie do `H_1(X_K;Z)`
wysyła je na generator i zero.
Pozwala to poprawnie korzystać
z danych peryferyjnych w późniejszej
chirurgii Dehna.

## 18 — kontrola diagramów Reidemeistera

Przeanalizowano rzeczywisty render
PDF przed i po poprawce. Na starym
rysunku R I samoprzecięcie nie miało
czytelnej przerwy pasma dolnego,
a w R II dwa przecięcia nie
były jednoznacznie oddzielone
jako przejścia górą i dołem.
Wprowadzono maskowanie białym tłem
i ponowne narysowanie odpowiednich
fragmentów. W rezultacie R I
ma lokalne rozróżnienie pasm,
a w R II czerwone pasmo
przechodzi ponad niebieskim
w dwóch przecięciach o przeciwnych znakach.
Ponownie obejrzano rysunek
na stronie PDF 145; brak kolizji
rysunków z podpisem.
Zachowano wyprowadzenie
tożsamości algebry Temperleya–Lieba
`b_i b_i^{-1}=1` i
`b_1b_2b_1=b_2b_1b_2`
dla ruchów R II i R III.

## Niezależne regresje

W `tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py`
rozszerzono testy o:

1. **67 600** sprawdzeń
   `q_V'(x,s,t)=q_V(x)+st'`
   dla obu postaci powiększenia,
   różnych `u,v,z`, macierzy
   o rozmiarach 0, 2 i 4 oraz
   wszystkich wektorów nad `F_2`;
2. **189** przypadków
   kongruencji Arf–Conwaya
   `Δ_sym(-1)≡1-4a_2 (mod 8)`;
3. regresję odsyłaczy do
   `thm:kt-arf-conway-slice`,
   `def:kt-peripheral` oraz
   `thm:kt-peripheral-homology`.

Utrzymano wcześniejsze 120
testów stabilizacji macierzy Seiferta,
modele Hodge'a, Cayleya, Bassa–Serre'a,
kolorowania Foxa, wielomianu Jonesa,
sumy Gaussa i dokładne tożsamości
R II/R III. Testy algebraiczne są
niezależnym sprawdzeniem konkretnych
rachunków, a nie formalizacją
wszystkich twierdzeń o węzłach.

## CI i PDF — finalna bramka

[GitHub Actions 45184301466](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45184301466)
na commicie `8743da3cd22b450145a4431d4612e12363e2b9c6`
zakończył oba zadania
`structural-audit` i `full-book-pdf`
ze statusem **success**.

- **44/44** źródeł katalogu; **0** brakujących odsyłaczy
  i **0** zduplikowanych etykiet;
- nowe testy matematyczne **PASS**;
- pobrano artefakt PDF z przebiegu:
  **274 strony**, trzy udane przebiegi `pdflatex`;
- `graph_and_knot_full_warnings.txt`:
  **0 bajtów**, bez ostrzeżeń LaTeX;
- obejrzano render strony **145** (R I/R II),
  stron **147–148** (Wirtinger i peryferia),
  stron **155–157** (Arf i Conway)
  oraz **161–163** (suma spójna, rodzaj, węzły torusowe).
  Nie wykryto nakładania rysunków i tekstu,
  przeciętych wzorów ani uciętych marginesów.
- Inspekcja dotyczy geometrii **narysowanych**
  przejść górą/dołem i czytelności,
  nie jest pełnym dowodem twierdzenia
  Reidemeistera z transwersalności.

## Dalszy plan

Zgodnie z zasadą stabilizacji:
**lokalny blok 16–18 zamknięto.**
Następna jednostka: **19–21**,
z kolejnymi szczegółowymi audytami
matematycznymi, językowymi,
rysunkowymi, strukturalnymi oraz
kontrolą końcowego PDF.
Nie zmienia się status globalnego,
wciąż niezakończonego audytu
44-rozdziałowego tomu.
