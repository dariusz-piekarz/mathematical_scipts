# Teoria grafów i węzłów — audyt globalny 21: 25–27, drugie przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Poprzednie **pierwsze przejście**:
[raport audytu 20](41-globalny-audyt-20-rozdzialy-25-27-pierwsze-przejscie.md).
Cel: drugi niezależny audyt matematyczno-redakcyjny
przed lokalną stabilizacją rozdziałów 25–27.

## Powtórnie kontrolowane twierdzenia i konstrukcje

- **Rozdział 25:** przesunięcia uchwytów; całkowita kongruencja macierzy;
  poprawiony warunek dla reguły `slam-dunk` (`r\in Z`, `s\in Q^* `);
  dodatnie i ujemne kontrakcje składowych `±1`;
  grupy i formy splecenia brzegów; różnica między
  trzeciowymiarową chirurgią a czterowymiarową zmianą formy;
  pełne twierdzenie Kirby'ego jako wynik zewnętrzny.
- **Rozdział 26:** definicja `C_p`, określoność formy,
  `L(p²,1-p)`, istnienie `B_p`, dokładny ciąg
  `H_1(∂B_p)→H_1(B_p)`, metabolizer formy brzegowej,
  liczenie `e,σ,b_2^±`, prosta spójność po sklejeniu.
- **Rozdział 27:** jednoznaczność ujemnych ułamków łańcuchowych,
  `C_{p,q}`, `L(p²,1-pq)`, forma splecenia,
  wymierne wypełnienia `B_{p,q}`, uogólniona kontrakcja,
  grupa fundamentalna oraz poprawność porównań różnych `q`.

## 25 — kolejna wykryta luka w przykładzie kontrakcji `+1`

**Rzeczywista korekta matematyczna:**
w przykładzie `ex:tg-kirby-positive-blowdown`
pierwszego przejścia wyprowadzono cykliczność
`coker Q` z samego faktu, że całkowita macierz
ma wpis równy `1`. Rozumowanie w tej postaci
jest **niepoprawne**.

Macierz `diag(1,2,2)` również
zawiera wpis `1`, ale jej cokernel to
`Z/2 ⊕ Z/2`, nie `Z/4`.
Pierwszy dzielnik elementarny równy `1`
nie oznacza, że pozostałe nietrywialne
czynniki postaci Smitha są tylko jednym.

Poprawiono dowód dla rzeczywistej macierzy
`B'=[[-3,-1],[-1,-4]]`: 
`|det B'|=11`, a każda skończona grupa
abelowa rzędu pierwszego `11`
jest izomorficzna z `Z/11`.
Forma splecenia na wybranym generatorze
wciąż ma wartość `4/11` mod `Z`;
weryfikacja jej współczynnika nie
zależy od błędnej przesłanki.

Sprawdzono ponownie poprawiony w audycie 20
lemat `slam-dunk`: wymaganie całkowitości
ramowania pozostającej składowej jest konieczne
dla tej postaci eliminacji. Przykład
`r=1/2,s=4` różni się już
rzędem `H_1` od błędnie przewidywanej
pojedynczej chirurgii. Zewnętrzne objaśnienie
w standardowych notatkach o rachunku Kirby'ego:
[Kirby Calculus and Surgery Theory](https://web.ma.utexas.edu/users/gdavtor/notes/4manifolds.pdf).
Dopóki topologiczna część ruchu jest
przyjmowana jako lokalny lemat chirurgii,
rachunek wyznacznika ani sam test homologi
nie jest pełnym dowodem geometrycznej
równoważności.

## 26 — kryterium prostej spójności bez silnego założenia `π1(W)=1`

Dodano stwierdzenie
`prop:tg-rb-pi1-general`
z pełnym dowodem przez eliminację
generatorów w iloczynie
wolnym z utożsamieniem podgrupy.
Niech `Y_p=∂B_p` będzie
brzegiem po ustaleniu identyfikacji,
a `i_B:π1(Y_p)→π1(B_p)`
i `i_W:π1(Y_p)→π1(W)`
odwzorowaniami brzegowymi.
W standardowej wymiernej kuli
`i_B` jest surjekcją.
Wtedy
`π1(X_(p)) ≅ π1(W)/<<i_W(ker i_B)>>`,
gdzie `<<...>>` oznacza
domknięcie normalne. 
Otrzymana rozmaitość jest
po prostu spójna **wtedy i tylko wtedy**,
gdy obraz jądra `i_B`
normalnie generuje grupę `π1(W)`.
Poprzedni warunek `π1(W)=1` jest
szczególnym przypadkiem wystarczającym,
lecz niekoniecznym.

**To rozdziela rzeczywistą kontrolę grupy
fundamentalnej dopełnienia od samej
prostej spójności rozmaitości wyjściowej.**
Dowód nie zakłada, że grupa `π1(W)`
jest przemienna.

## 27 — izometria form splecenia nie klasyfikuje przestrzeni soczewkowych

Dodano uwagę
`rem:tg-general-linking-iso`,
która naprawia potencjalnie
mylącą interpretację wcześniejszego
porównania konfiguracji `C_{5,1}`
i `C_{5,2}`.

Wybrane generatory pierwszych homologii
mają wartości samosplecenia
odpowiednio `4/25` i `9/25`.
Wartości są różne, ale **abstrakcyjne
formy splecenia są izometryczne**:
`11` jest odwracalne mod `25`,
a `4·11²=484≡9 (mod 25)`.
Zmiana generatora `x→11x`
przenosi jedną formę na drugą.

Z drugiej strony orientowane przestrzenie
soczewkowe w tym modelu mają parametry
`L(25,-4)=L(25,21)`
i `L(25,-9)=L(25,16)`.
W klasyfikacji orientowanej warunkiem
dyfeomorfizmu jest
`q'≡q^±1 (mod p)`.
Ponieważ `21^(-1)≡6 (mod 25)`,
a `16≠21,6 (mod 25)`,
te przestrzenie **nie są dyfeomorficzne**.
Zatem równość `H_1` i izometria
form splecenia nie wystarczają
do klasyfikacji trójrozmaitości.
Twierdzenie o klasyfikacji
przestrzeni soczewkowych przyjmujemy
jako zewnętrzne; podstawowa arytmetyka
jest przeprowadzona jawnie.

Uwaga `rem:tg-general-pi1-normal-closure`
przenosi kryterium z rozdziału 26
na uogólnione wypełnienie
`B_{p,q}`: także tutaj
`π1(W)=1` jest warunkiem
wystarczającym, lecz niekoniecznym.

## Nowe regresje drugiego przejścia

Rozszerzono istniejący test
`tools/tests/test_graph_and_knot_kirby_rational_blowdowns.py`
o trzy kontrole:
- **6032** niezależne prezentacje
  amalgamowanego produktu cyklicznych
  grup skończonych:
  sprawdzono rząd grupy wyznaczany
  przez gcd minorów prezentacji
  i przez iloraz `π1(W)`
  względem obrazu `ker i_B`;
- **625** par elementów
  `Z/25` dla dwóch form
  splecenia: dokładnie
  `4(11x)(11y)≡9xy (mod 25)`,
  a także kontrola różnicy
  parametrów w twierdzeniu
  klasyfikacyjnym `21,6,16`;
- **jeden** dodatkowy kontrprzykład
  do nieuprawnionego wniosku
  z obecności wpisu `1`
  w macierzy do cykliczności
  jej całkowitego cokernela.

Oznacza to **6658 nowych kontroli**
drugiego przejścia i łącznie
**10 686 kontroli** w teście
rozdziałów 25–27, wobec
**4028** pierwszego przejścia.

Żaden test skończonej grupy
czy macierzy nie formalizuje
istnienia wymiernej kuli homologii
ani twierdzeń klasyfikujących
czterorozmaitości.

## Końcowy przebieg CI i kontrola złożonego tomu

Po wszystkich poprawkach rozdziałów 25–27 oraz
aktualizacji testu końcowy przebieg
[GitHub Actions 45222364768](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45222364768),
dla commitu źródłowego
`906a180e1f6f1638c73b67d28c2ea63b98fbb482`,
zakończył **oba zadania** ze statusem **success**:
`structural-audit` i `full-book-pdf`.

Potwierdzono:
- **44/44** źródła rozdziałów;
- **0** powtórzonych etykiet,
  **0** nierozwiązanych odsyłaczy,
  **0** błędów środowisk,
  **0** terminów niedozwolonych;
- **10 686** dokładnych przypadków
  w sześciu grupach testów rozdziałów
  25–27, **wszystkie PASS**;
- **trzy udane przebiegi `pdflatex`**
  na wszystkich 44 rozdziałach;
- rzeczywisty PDF z **282 stronami A4**;
- plik `graph_and_knot_full_warnings.txt`
  pusty (**0 bajtów**), bez ostrzeżeń
  LaTeX i zgłoszonych przepełnień.

Pobrano PDF z **tego przebiegu**, nie starszy
artefakt. Wygenerowano renderingi i
sprawdzono wizualnie **wszystkie strony
210–227**, czyli cały blok:

- **210–214:** rozdział 25 —
  poprawiony lemat `slam-dunk`,
  obydwie kontrakcje `±1`,
  nowy kontrprzykład postaci Smitha,
  rysunek grafu i podpisy;
- **215–221:** rozdział 26 —
  konfiguracja `C_p`, rysunki
  `C_2,C_3,C_4`, ciąg dokładny
  wypełnienia, warunek normalnego
  generowania `π1(W)`, diagram
  wymiany `C_p` na `B_p`;
- **222–227:** rozdział 27 —
  ułamki łańcuchowe, grafy
  `C_{5,1},C_{5,2}`, przykład
  `C_{7,3}`, uogólnione
  kryterium `π1`, rozróżnienie
  izometrii form splecenia
  i dyfeomorfizmu przestrzeni
  soczewkowych, diagram sklejenia.

Nie wykryto na tych stronach
uciętych wzorów, naruszeń marginesów,
nachodzenia tekstu na rysunki
ani błędów łamania podpisów.
Kontrola wizualna dotyczy
renderingu po **ostatniej**
zmianie w rozdziale 27.

## Werdykt audytu 21

**ROZDZIAŁY 25–27 — LOKALNIE STABILNE (PASS).**

Dwa szczegółowe przejścia, audyty
20 i 21, doprowadziły do:
- naprawy fałszywej hipotezy
  o wymiernym `slam-dunk`;
- naprawy nieuprawnionego
  wniosku o postaci Smitha;
- ścisłego kryterium prostej
  spójności po wymiernej kontrakcji;
- rozróżnienia kanonicznych
  współczynników form splecenia,
  izometrii całych form i
  klasyfikacji przestrzeni
  soczewkowych;
- niezależnej regresji
  arytmetycznej i homologicznej,
  trzykrotnej kompilacji
  pełnego tomu i inspekcji
  rzeczywistego PDF.

Twierdzenia geometryczne
Cassona–Harera, Kirby'ego,
Fintushela–Sterna, Parka i
Symington pozostają jawnie
przyjęte z literatury.
Testy nie są ich
formalną weryfikacją.

**Stan tomu: rozdziały 01–27 lokalnie stabilne.**
**Następny etap: audyt 22,
pierwsze przejście rozdziałów 28–30**,
następnie ich drugi audyt
przed dalszą rozbudową.
Całościowy audyt wszystkich
44 rozdziałów pozostaje
otwarty.
