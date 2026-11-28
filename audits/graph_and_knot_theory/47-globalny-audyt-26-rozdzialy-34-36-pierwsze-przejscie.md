# Teoria grafów i węzłów — audyt globalny 26: rozdziały 34–36, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Audyt 25 uznał **01–33 za lokalnie stabilne**.
Przedmiot obecnego audytu: źródłowe rozdziały
**34 (synteza egzotycznych struktur),
35 (nowoczesne niezmienniki i zastosowania)
oraz 36 (literatura i podsumowanie)**.

## Zakres kontroli i niezależność od poprzednich przejść

- 34: dokładny bilans homotopijno-homologiczny
  plumbingu i wymiernej kontrakcji, formy przecięcia,
  konwencje formy splecenia, skutki reguł sklejania,
  hipotezy twierdzeń Freedmana i Fintushela–Sterna.
- 35: gradacja oraz algebra Frobeniusa dla homologi Khovanova,
  przemienność ścian kostki, znaki, konstrukcja
  zredukowanej homologii, właściwe warunki dla
  różniczki Heegaarda–Floera, próg twierdzeń
  zewnętrznych, obliczenia Temperleya–Lieba.
- 36: autentyczność bibliografii, weryfikowalne
  identyfikatory i przypisanie źródeł do
  konkretnych etapów dowodów.

Poniższe zmiany zapisano w trzech niezależnych
plikach `.tex`, a nie tylko w raporcie.

## Rozdział 34 — poprawa zakresu bilansu wymiernej kontrakcji

Dodano wniosek
`cor:tg-syn-rational-homological`
i **pełny dowód nad współczynnikami wymiernymi**.
Zachodzą tożsamości:
`b_1(X_(p))=b_1(X)`,
`b_2^+(X_(p))=b_2^+(X)`,
`b_2^-(X_(p))=b_2^-(X)−(p−1)`
**bez uprzedniego założenia `b_1=0`**.
Co więcej,
`Q_X≅_Q Q_X_(p)⊥Q_Cp`.

Dla `Y=∂C_p` mamy
`H_1(Y;Q)=H_2(Y;Q)=0`.
Po zapisaniu
`X=A∪_Y C_p` i
`X_(p)=A∪_Y B_p`
ciągi Mayera–Vietorisa dają
`H_2(X;Q)≅H_2(A;Q)⊕H_2(C_p;Q)`
i
`H_2(X_(p);Q)≅H_2(A;Q)`.
W stopniu pierwszym oba
ciągi utożsamiają `H_1(X;Q)`
i `H_1(X_(p);Q)`
z `H_1(A;Q)`.
Przecięcia klas z obu rozłącznych
części zerują się, a forma
`Q_Cp` jest ujemnie określona
rzędu `p−1`.
Stąd dokładny bilans
dodatnich i ujemnych kierunków.

Podkreślono, że **rozkład
wymierny nie implikuje
ortogonalnego rozkładu
całkowitej unimodularnej
formy**. Zastąpiono
anglicyzm „kodimension”
polskim **„kowymiar”**.

### Konwencja znaku formy splecenia

W syntezie przyjęto
`λ_{∂P}=−Q^{-1} mod Z`,
natomiast wcześniejszy
rozdział Parka definiuje
w swoim rachunku
`λ_{Y7}=+Q_7^{-1} mod Z`.
Jawnie wskazano, że są to
**przeciwne konwencje znaku**;
przy porównaniu ułamka
`±6/49` trzeba
odwrócić znak jednej formy.
Metabolizer
`7 Z/49` pozostaje
izotropowy przy obu znakach.

## Rozdział 35 — precyzja algebry i konstrukcji analitycznych

### Algebra Frobeniusa

Dodano lemat
`lem:kt-khovanov-frobenius`
z samodzielnym sprawdzeniem:
- łączności `m`;
- współłączności `Δ`;
- wszystkich trzech postaci
  tożsamości Frobeniusa.

Dla algebry
`A=Z[X]/(X²)`
sprawdzono obliczenia na bazach
`(1,X)` i
`(1⊗1,1⊗X,X⊗1,X⊗X)`.
W ten sposób jawnie uzasadniono
algebraiczny krok potrzebny
w dowodzie `d²=0`
dla kostki stanów Khovanova.

### Zredukowana homologia Khovanova

Zastąpiono ogólnikowe hasło
„redukcja jednego czynnika”
precyzyjną konstrukcją:
wybór punktu bazowego `p`,
w każdym stanie oznaczonego
czynnika `A`,
ograniczenie go do ideału
`XA` i przesunięcie
stopnia kwantowego o jeden.
Wprowadzono podkompleks
`~C(D,p)⊂C(D){1}`.

Dowiedziono, że jest stabilny
względem różniczki:
przy łączeniu okręgów
`m(X⊗A)⊂XA`,
przy rozdzielaniu okręgu
z punktem bazowym
`Δ(X)=X⊗X`.
Dla węzła niezmienniczość
względem punktu bazowego
i ruchów Reidemeistera
pozostaje odrębnym,
zewnętrznym twierdzeniem.
W przypadku splotów z wieloma
składowymi zaznaczono
znaczenie wyboru składowej.

### Różniczka Floera węzła

Poprawiono istotną
nieprecyzyjność pierwotnej
definicji `CFK^−`.
Dyski Whitney'a uwzględniane
w różniczce muszą mieć:
- indeks Maslova równy jeden;
- **`n_z(φ)=0`**;
- wagę `U^{n_w(φ)}`.

Podano znaczenie `n_w,n_z`
i osobno wyjaśniono,
dlaczego warunku
`n_z=0` nie
można pominąć przy tej
konwencji kompleksu.
Niezmienniczość kompleksu
i analiza przestrzeni
dysków pseudoholomorficznych
pozostają zewnętrzną
treścią teorii Ozsvátha–Szabó.

## Rozdział 36 — weryfikacja bibliografii i zależności twierdzeń

Poprawiono opis czterech
podstawowych artykułów:

1. Ozsváth–Szabó,
   *Holomorphic disks and knot invariants*,
   Adv. Math. **186** (2004), 58–116,
   DOI `10.1016/j.aim.2003.05.001`.
2. Khovanov,
   *A categorification of the Jones polynomial*,
   Duke Math. J. **101** (2000), 359–426,
   DOI `10.1215/S0012-7094-00-10131-7`.
3. Rasmussen,
   *Khovanov homology and the slice genus*,
   Invent. Math. **182** (2010), 419–447.
4. Kronheimer–Mrowka,
   *Khovanov homology is an unknot-detector*,
   Publ. Math. IHÉS **113** (2011), 97–208,
   DOI `10.1007/s10240-010-0030-y`.

Dodano sekcję
`sec:kt-bibliografia-mapa`
z mapą relacji między metodami:
- graf i jego macierz → homologia brzegu;
- realizacja geometrii Parka
  → zewnętrzne twierdzenia
  o symplektycznym zanurzeniu;
- forma przecięcia + fundamenty
  → Freedman;
- kompleks Khovanova → tylko
  po dodatkowej niezmienniczości
  Reidemeistera uzyskujemy
  niezmiennik splotu;
- `CFK^−` i
  pseudoholomorficzne dyski
  → twierdzenia Ozsvátha–Szabó i Ni;
- chirurgia torusowa +
  dane topologiczne
  → formuła Seiberga–Wittena
  dopiero z twierdzenia
  Fintushela–Sterna.

Zapobiega to fałszywemu
wnioskowaniu, że sama
kompilacja lub elementarny
rachunek macierzowy
dowodzi głębokich twierdzeń
geometrycznych.

## Nowe, niezależne testy regresyjne

Dodano moduł
`tools/tests/test_graph_and_knot_synthesis_modern_bibliography.py`
oraz nowy krok do
`.github/workflows/graph-and-knot-global-audit.yml`.

Nowe kontrole:
- **27 566** przypadków
  łańcuchów `C_p` dla
  `2≤p≤180`,
  liczonych dokładnie nad `Q`.
  Obejmują rekurencję
  wyznaczników, ułamki łańcuchowe,
  niezmienniczość `b_1`
  i zmianę `b_2^±,χ,σ`,
  również gdy `b_1>0`.
- **21** kontroli
  łączności, współłączności,
  tożsamości Frobeniusa,
  zachowania ideału `XA`
  i elementarnego przykładu węzła trywialnego.
- **9** dokładnych sprawdzeń
  odwracalności generatorów
  `A1+A^{-1}e_i`
  oraz relacji Artina
  w `TL_3` dla
  różnych niezerowych wymiernych `A`.
- Niezależne kontrole obecności
  kluczowych warunków `CFK^−`,
  etykiet i zweryfikowanych DOI.

Łącznie **27 596 przypadków**
algebraicznych: **PASS**.

Wynik strukturalny
[GitHub Actions 45251930683](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45251930683)
dla commitu testowo-źródłowego
`1c6205f83180e4a372b04a64b9a0777a482cfe4d`:
- 44/44 źródła;
- 0 zduplikowanych etykiet;
- 0 nierozwiązanych odsyłaczy;
- 0 błędów środowiska;
- 0 terminów zakazanych;
- nowy pakiet regresji PASS.

Po tym przebiegu dodatkowo
doprecyzowano konwencję
znaku formy splecenia
w źródłowym rozdziale 34
(commit `5e831c27adc3eeb12ff016f1fa068764cf65e2a2`).
Dla **pełnego** końcowego
wyniku należy weryfikować
późniejszy przebieg
[GitHub Actions 45252104140](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45252104140).

## Bramka i status: wykonane kontrole

### Kontrola matematyczna i testy — PASS

W końcowym przebiegu źródłowym
[GitHub Actions 45252104140](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45252104140)
dla commitu `5e831c27adc3eeb12ff016f1fa068764cf65e2a2`
zadanie `structural-audit` zakończyło się **success**,
zawierając m.in. **27 596** nowych regresji (PASS)
i wszystkie pakiety starszych rozdziałów:
**44/44** źródła, **0** duplikatów etykiet,
**0** niezwiązanych odsyłaczy,
**0** błędów środowiska,
**0** terminów zakazanych.

### Pełna kompilacja i przegląd PDF — PASS dla bazowego stanu matematycznego

[GitHub Actions 45251930683](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45251930683)
dla commitu źródłowo-testowego
`1c6205f83180e4a372b04a64b9a0777a482cfe4d`
zakończył się **success** w zadaniach
`structural-audit` i `full-book-pdf`.
Pobrano artefakt PDF **14856492888**:
kompletne **287 stron A4**, trzy
pomyślne kompilacje `pdflatex`,
plik ostrzeżeń LaTeX o rozmiarze **0 bajtów**.

Wyrenderowano i **obejrzano wszystkie strony 272–287**,
zawierające łącznie cały audytowany blok:
- **272–278** — drukowany rozdział 41
  (źródłowy 34): graf plumbingowy, formy
  przecięcia i splecenia, nowy wniosek
  o wymiernym bilansie, diagram dwóch
  chirurgii, tabela warunków;
- **279–284** — drukowany rozdział 42
  (źródłowy 35): algebra Frobeniusa,
  nowy lemat i dowód, kompleks
  zredukowany, warunek `n_z(φ)=0`,
  przykład Whiteheada, Temperley–Lieb;
- **285–287** — drukowany rozdział 43
  (źródłowy 36): bibliografia z
  uzupełnionymi DOI i nowa mapa
  zależności dowodów.

W tych stronach **nie zauważono**
uciętych wzorów, nachodzących podpisów
ani kolizji diagramów. Zmiana dodana
**po** przebiegu 45251930683 to tylko
dodatkowe 11 wierszy tekstu o
przeciwnych konwencjach znaku
formy splecenia w źródle 34.
Dla tej właśnie końcowej wersji
zadanie strukturalne jest PASS,
ale dodatkowy skład PDF z
przebiegu **45252104140**
był jeszcze w toku podczas
ostatniej kontroli.

### Status i kolejna iteracja

Matematyczne poprawki **34–36**
i regresje pierwszego przejścia
są zakończone. Pełny PDF wersji
sprzed ostatniego doprecyzowania
znaku skompilował się bez ostrzeżeń
i przeszedł oględziny wszystkich stron.
**Do formalnego zamknięcia pierwszego
przejścia pozostaje potwierdzenie
końcowej kompilacji wersji zawierającej
również dopisek o konwencji.**

Blok **34–36 nadal jest W STABILIZACJI**,
także po udanym pierwszym przejściu,
aż do odrębnego audytu 27.
**01–33 pozostają lokalnie stabilne.**
Globalny audyt 44-rozdziałowego
tomu pozostaje otwarty.
