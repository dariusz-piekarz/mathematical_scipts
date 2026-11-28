# Topologia ogólna — globalny audyt 07: rozdział 13, konstrukcja uzupełnienia jednostajnego

**Data:** 2026-11-22.
**Badany plik:** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex`.
**Blob bez zmian:** `33200912c034f3f946909f00b9e4068deeca4ed0`.
**Zakres:** ponowna, techniczna weryfikacja wcześniejszej
kontroli przekrojowej 04, która pozostawiła otwarte
szczegóły minimalizacji filtrów i zupełności
konstruowanego uzupełnienia.
Niniejszy raport sprawdza **pełną konstrukcję
minimalnych filtrów Cauchy'ego i uzupełnienia**
(środowiska na liniach 203–505) oraz związany z nią
lemat o rozszerzeniu (570–635).
Pozostałe wyniki rozdziału, np. o uzupełnieniu
metrycznym, nie zostały tu osobno reaudytowane.

## 1. Relacja bliskości filtrów

Dla Cauchy'ego filtrów F,G definiuje się F~G
przez: dla każdego E istnieją A∈F, B∈G
z A×B⊂E.
- Zwrotność wynika z warunku Cauchy'ego.
- Symetria używa E∩E^{-1}.
- Przechodniość: dobieramy symetryczne D
  z D∘D⊂E; dla A×B⊂D i B'×C⊂D
  przecięcie B∩B' jest niepuste,
  gdyż oba zbiory należą do tego samego
  **właściwego** filtra G.
  Jeden b∈B∩B' daje A×C⊂E.
  Nie trzeba zakładać metryzowalności.

## 2. Konstrukcja minimalnego filtra

Zbiory E[A] dla A∈F, E∈U są
niepuste, a ich rodzina jest bazą
filtra F° przez
(E∩D)[A∩B] ⊂ E[A]∩D[B].
Z A⊂E[A] mamy F°⊂F
(przy porządku zbiorowym filtrów).

Dla V wybiera się symetryczne D
z D³⊂V, a następnie A∈F
z A×A⊂D. Jeśli u,v∈D[A],
istnieją a,b∈A z uDa, aDb, bDv,
więc uD³v⊂V.
Stąd F° jest filtrem Cauchy'ego.

Relacja F°~F ma świadka D[A]×A⊂D²⊂V.
Dla dowolnego G~F i bazowego E[A] filtr G
zawiera E[A]: z A'×B⊂D⊂E,
gdzie A'∈F, B∈G, wybieramy
a∈A∩A'; wówczas B⊂D[a]⊂E[A].
To jest istotny krok dowodu
F°⊂G. Jeżeli H⊂F° jest
filtrem Cauchy'ego, to H~F°,
a wcześniejsze włączenie wymusza H=F°.
Jednoznaczność minimalnego
przedstawiciela wynika z
obu inkluzji dla dwóch minimalnych filtrów.

## 3. Struktura jednostajna na zbiorze przedstawicieli

Baza otoczeń na \hat X składa się z
\(\widehat E=\{(F,G):\exists A∈F,B∈G,\ A×B⊂E\}\).
Przekątną daje warunek Cauchy'ego;
dla przecięć wystarczy \widehat{E∩F}.
Odwrotność jest \widehat{E^{-1}}.
Warunek złożenia:
przy A×B⊂D i B'×C⊂D
przecięcie B∩B' ma element b;
stąd A×C⊂D²⊂E.
Struktura jest rozdzielająca,
ponieważ każde dwa minimalne
filtry bliskie są równe.

## 4. Kanoniczne zanurzenie

Dla x∈X filtr otoczeń N_x
jest Cauchy'ego: sekcja
D[x]×D[x]⊂D²⊂E.
Własność minimalności ma jawnego
świadka: dla A∈N_x
wybiera się symetryczne D
z D²[x]⊂A i bazowy element
D[D[x]]⊂A.
Rozdzielanie X zapewnia
iniektywność x↦N_x.
Oba kierunki porównania struktur
jednostajnych są wykazane:
- gdy (N_x,N_y)∈\hat E, to (x,y)∈E;
- gdy (x,y)∈D i D³⊂E,
  to D[x]×D[y]⊂E, więc
  (N_x,N_y)∈\hat E.
Gęstość obrazu pochodzi z
A∈F o małej średnicy i
dowolnego x∈A.

## 5. Zupełność — najtrudniejszy fragment

Niech H będzie filtrem Cauchy'ego na \hat X.
Dla H_0∈H oraz E∈U konstruujemy zbiór
B(H_0,E) punktów x, dla których
istnieje F∈H_0 bliski N_x względem \hat E.
Niepustość wynika z gęstości i
niepustości elementów H.
Skończone przecięcia są kontrolowane
przez B(H_0∩H_1,E_0∩E_1).

Dla V wybiera się symetryczne D
z D³⊂V i element H_0∈H
o H_0×H_0⊂\hat D.
Jeśli x,y∈B(H_0,D),
to istnieją F,G∈H_0 połączone z N_x,N_y
przez \hat D. W konsekwencji
(N_x,N_y)∈\widehat{D³},
a więc (x,y)∈D³⊂V.
Zatem zbiory B(H,E) generują
filtr Cauchy'ego G na X.

Niech F_0=G°.
Dla dowolnego symetrycznego E
wybieramy D z D⁴⊂E;
bliskość G i F_0 daje
A∈G,C∈F_0 z A×C⊂D.
Wybieramy B(H_0,V)⊂A
i W⊂V∩D, a także H_1∈H,
H_1×H_1⊂\hat D.
Dla K∈H_0∩H_1 wybieramy
x∈B(H_0∩H_1,W),
L∈H_0∩H_1 świadczącego
(N_x,L)∈\hat W⊂\hat D.
Wtedy (L,K)∈\hat D,
a więc (N_x,K)∈\widehat{D²}.
Z x∈A i A×C⊂D oraz
symmetricznym T⊂D
dostajemy T[x]×C⊂D²,
czyli (N_x,F_0)∈\widehat{D²}.
Po symetrii i złożeniu:
(F_0,K)∈\widehat{D⁴}⊂\hat E.
Cały H_0∩H_1 należy zatem
do \hat E[F_0], co dowodzi zbieżności
H do F_0. Nie wykryto w tym
łańcuchu przejść zależnych
od ukrytej metryki czy
przeliczalnej bazy.

## 6. Własność uniwersalna

Dla gęstego A⊂Z filtr na A
generowany przez A∩E[z]
jest Cauchy'ego.
Jednostajna ciągłość f:A→Y
przenosi ten filtr na Cauchy'ego,
który zbiega w zupełnej Y;
Hausdorffowość Y daje jednoznaczność.

Jednostajną ciągłość przedłużenia
udowodniono przez wybranie W
takiego, że domknięcie W
w Y×Y zawiera się w zadanym V.
Istnienie takiego W wynika
z odpowiednio małego symetrycznego
T z T³⊂V, nie z nieuprawnionego
założenia, że każde entourage jest domknięte.
Gęstość A oraz jednoznaczność
granicy zapewniają wyłączność
otrzymanego rozszerzenia.

## 7. Dodatkowy test skończonych modeli

Dodany `tools/tests/test_general_topology_cross_dependencies.py`
obejmuje wszystkie partycje zbioru
o liczności do 5.
Dla jednostajności zadanej relacją
równoważności R testuje:
- filtr główny F_A jest Cauchy'ego
  wtedy, gdy A leży w jednej klasie R;
- filtry główne Cauchy'ego F_A i F_B
  są bliskie dokładnie wtedy,
  gdy A,B należą do tej samej klasy;
- minimalny bliski filtr to filtr
  główny na pełnej klasie R;
- dla R=Δ w skończonym zbiorze
  model sprowadza się do singletonów.

To jedynie regresja na skończonych
modelach, nie dowód twierdzenia
w ogólnej przestrzeni jednostajnej.

## Wynik i dalsze zadania

W sprawdzonych fragmentach
minimalizacji i istnienia
uzupełnienia nie znaleziono
istotnego błędu matematycznego.
Nie zmieniano stabilnego
źródła rozdziału 13.
Dla zamknięcia globalnego audytu
nadal potrzebna jest kontrola
pozostałych dowodów rozdziału 13
i innych rozdziałów 01–26,
a także szczegółowa inspekcja
rysunków w całym wydaniu.
