# Teoria grafów i węzłów — audyt globalny 14: rozdziały 16–18, pierwsze przejście

Data: 2026-11-23.
Gałąź: `biblioteka-matematyczna-iteracja-6`.
Kontynuacja audytu 13, po lokalnej stabilizacji rozdziałów 13–15.

## Zakres i status

- Historyczny **16**: `Od triangulacji do topologii i geometrii rozmaitości`;
- Historyczny **17**: `Grafy Cayleya, działania na drzewach i teoria Bassa–Serre'a`;
- Historyczny **18**: `Teoria węzłów: od diagramów do rozmaitości czterowymiarowych`.

Przeczytano całe rozdziały 16 i 17 (przed zmianami 214 oraz 334
wiersze) oraz przejrzano kolejne sekcje rozdziału 18 (pierwotnie
1821 wierszy). Audyt uwzględnia definicje i zakres hipotez,
argumenty matematyczne, konwencje znaków, przykłady,
terminologię, odsyłacze i testy numeryczno-algebraiczne.

**Werdykt: pierwsze przejście ukończone po naprawie
rzeczywistego błędu matematycznego; rozdziały 16–18
pozostają W STABILIZACJI.** Nie jest to formalny dowód
wszystkich twierdzeń ani zakończenie globalnego audytu
wszystkich 44 rozdziałów.

## 16 — triangulacje, rekonstrukcja, Hodge

1. W definicji sklejania trójkątów jawnie określono:
   skończoną rodzinę, parowanie różnych *wystąpień* boków,
   homeomorfizmy zachowujące zbiór końców, brak koniecznej
   spójności. Powierzchnia bez brzegu powstaje wtedy i tylko
   wtedy, gdy każde ogniwo wierzchołka jest pojedynczym okręgiem.
   Osobno uzasadniono, że spójność odpowiada spójności
   grafu dualnego. Bez warunku parowania wszystkich boków
   sformułowanie byłoby zbyt ogólne.
2. Rozwinięto dowód kryterium: wnętrza trójkątów i
   sklejone krawędzie mają otoczenia dyskowe, a gwiazda
   wierzchołka jest stożkiem nad ogniwem.
   Zaznaczono sprowadzenie homeomorfizmów boków do
   sklejeń odcinkami afinicznymi oraz argument
   zwartości i własności Hausdorffa.
3. Poprawiono **różnicę między transpozycją macierzy
   operatora brzegowego a sprzężeniem operatorowym**.
   Kobrzeg `d_p` zapisujemy w bazach dualnych
   do zorientowanych sympleksów, natomiast
   `d_p^*` zależy od późniejszego wyboru dodatnich
   iloczynów skalarnych. Dowód skończeniewymiarowego
   twierdzenia Hodge'a korzysta z
   `d_p d_{p-1}=0`, ortogonalności obrazów
   i rozkładu względem dopełnienia ortogonalnego.
4. Usunięto historyczne sformułowania „ostatni rozdział
   tej iteracji” i „do iteracji piątej”, niepasujące
   do zintegrowanego podręcznika.

## 17 — grafy Cayleya i teoria Bassa–Serre'a

1. Sprawdzono twierdzenie o spójności Cayleya
   `Cay(G,S)` i generowaniu grupy przez symetryczny
   zbiór `S`; kierunek odwrotny używa iloczynu
   różnic kolejnych wierzchołków spaceru.
2. Ujednolicono twierdzenie o grafie Cayleya grupy
   wolnej: stopień wynosi `2r` już dla `r=1`,
   gdzie graf jest prostą. W dowodzie brak
   cykli wynika z nieistnienia niepustych
   zredukowanych słów reprezentujących jedność.
3. Doprecyzowano **dowód, że swobodne działanie
   bez inwersji na drzewie daje nakrycie grafów**.
   Wykazano surjektywność i injektywność mapy
   gwiazd nad konkretnym wierzchołkiem, a następnie
   identyfikację grupy automorfizmów pokładowych z
   działającą grupą. Rząd wolnej grupy dla
   skończonego ilorazu wynosi `e-v+1`.
4. Przejrzano przypadki amalgamacji i HNN poprzez
   twierdzenie van Kampena, z jawnym
   monomorfizmem grupy `π₁(Z)` i dodatkowym
   generatorem stabilnym.
5. Do przykładów stopni drzewa Bassa–Serre'a
   dodano `BS(1,2)=<a,t|tat^{-1}=a²>`.
   Indeksy obu obrazów grupy krawędzi w
   `Z` to 1 i 2, więc stopień wierzchołków
   drzewa wynosi 3. Reprezentacja afiniczna
   `a(x)=x+1`, `t(x)=2x` pokazuje,
   że grupa jest nieprzemienna.
6. **Fundamentalne twierdzenie Bassa–Serre'a**
   nadal jest jawnie przyjętym twierdzeniem,
   a nie wynikiem kompletnego dowodu w tekście.

## 18 — rzeczywisty błąd stabilizacji macierzy Seiferta

W oryginalnym stwierdzeniu dotyczącym
elementarnego powiększenia macierzy Seiferta
obie postacie zawierały **niedozwolone niezerowe
wektory**. W ogólności wyznacznik macierzy
`tV'-V'^T` nie był już powiązany z
`det(tV-V^T)` czynnikiem `±t^k`.

Jawny kontrprzykład:
`V=[[1,0],[-1,1]]`, `u=v=(1,0)^T`.
Dla dawnych postaci:
`det(tV-V^T)=t²-t+1`, a
`det(tV'-V'^T)=t²`, co nie jest
równoważne mnożeniu przez jednostkę.

**Poprawione dozwolone postacie**:
`[[V,u,0],[v^T,z,0],[0,1,0]]` oraz
`[[V,u,0],[v^T,z,1],[0,0,0]]`,
gdzie `u,v` są wektorami kolumnowymi,
`z` liczbą całkowitą.
Rozwinięcie wyznacznika wzdłuż ostatniej
kolumny i ostatniego wiersza daje w obu
przypadkach **dokładnie**
`det(tV'-V'^T)=t det(tV-V^T)`.
Dowód zapisano w rozdziale.
Dopuszczenie dawnych wektorów usuwałoby
potrzebne zera i zmieniało niezmiennik.

## 18 — definicje i inne dowody

1. Wprowadzono pełną definicję
   `g_4^{sm}(K)`: minimum rodzajów
   właściwie, gładko zanurzonych
   powierzchni w `B⁴` z brzegiem `K`.
   Zdefiniowano węzły gładko typu slice
   oraz `g_4^{sm}(K)≤g(K)`.
2. Dawne wystąpienie niezdefiniowanego
   `g_4^{sm}(T)` w przykładzie
   trójlistnika wskazuje teraz jawnie
   **przyjmowaną** nierówność
   `|σ(K)|≤2g_4^{sm}(K)`.
   Podano zakres jej zaawansowanego
   czterowymiarowego uzasadnienia.
   Podobnie stwierdzenie o slicowości
   i niezmienniku Arfa odsyła do definicji.
3. Wzmocniono dowód niezmienniczości
   nawiasu Kauffmana pod ruchami R II
   i R III. W algebrze Temperleya--Lieba
   stosujemy
   `e_i²=δe_i`, `e1e2e1=e1`,
   `e2e1e2=e2`, `δ=-A²-A⁻²`.
   Wypisano pełną redukcję
   `b_i b_i⁻¹=1`,
   `b1b2b1=b2b1b2` dla
   `b_i=A1+A⁻¹e_i`.
   Rachunek działa lokalnie przy
   dowolnym zamknięciu pasm.
4. Pozostałe klasyczne twierdzenia
   wykorzystywane w rozdziale obejmują
   między innymi Reidemeistera, dualność
   Alexandera, niezależność danych Seiferta,
   prezentację Artina, twierdzenia
   Alexandera i Markowa, rozkład Schuberta
   i nieściśliwość powierzchni Seiferta
   minimalnego rodzaju. Nie należy
   utożsamiać szkiców ich dowodów
   z formalną weryfikacją wszystkich kroków.
   To pozostaje celem następnego przejścia.

## Nowa niezależna regresja

Dodano
`tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py`
i podłączono ją do
`.github/workflows/graph-and-knot-global-audit.yml`.

Wyniki z przebiegu
[45181849098](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181849098)
dla zadania `structural-audit`: **PASS**.

- Laplasjan Hodge'a: dla trójkątnego cyklu,
  pełnego trójkąta i sfery czworościanu
  dokładne rzędy macierzy nad `Q`
  przy dwóch wyborach dodatnich wag,
  sprawdzenie `d²=0`, samosprzężoności
  w wagowym iloczynie skalarnym,
  nieujemności i zgodności jądra z `b₁`;
- Graf Cayleya grupy wolnej:
  kule promienia 3 dla `r=1,2,3`,
  odpowiednio 7, 53 i 187 wierzchołków;
- Drzewo `C₂*C₃`: 35 wierzchołków,
  34 krawędzie i wewnętrzne stopnie
  odpowiednio 2 i 3;
- **120** symbolicznych sprawdzeń obu
  poprawionych powiększeń macierzy Seiferta
  (w tym różne `u,v,z`) i jawne
  wykrycie błędu dawnych postaci;
- Kolorowania Foxa trójlistnika
  dla modułów 2–13, w tym
  `9` kolorowań modulo 3
  i `18` modulo 6;
- rachunek Temperleya--Lieba
  trójlistnika, nawias
  `-A⁵-A⁻³+A⁻⁷`, normalizacja
  wielomianu Jonesa `t+t³-t⁴`;
- dokładna algebraiczna weryfikacja
  relacji R II i R III w pięcioelementowej
  bazie `TL₃`;
- **20** przypadków sum Gaussa
  form kwadratowych w wymiarach 2 i 4
  nad `F₂`.

Globalny test strukturalny zgłasza
`44/44` źródła, `0` duplikatów
etykiet, `0` nierozwiązanych odsyłaczy,
`0` błędów zagnieżdżenia
środowisk i `0` zakazanych terminów.
Testy skończonych przypadków
nie zastępują dowodów twierdzeń.

## Bramka stabilizacji

**Rozdziały 16–18: OTWARTE — po pierwszym przejściu.**
Do kolejnej iteracji:
1. drugie niezależne przejście szczególnie
   długiego rozdziału 18, z weryfikacją
   założeń prezentacji Wirtingera,
   dwuznaczności konwencji znaków,
   własności Arfa i długości oraz dowodu
   addytywności rodzaju;
2. wyniki pełnego PDF dla ostatniego
   commitu, przegląd obrazów stron
   zmienionych sekcji i rysunków;
3. potwierdzenie stabilności
   po kontrolach CI przed przejściem do 19–21.

Audyt matematyczny **44-rozdziałowego
tomu pozostaje otwarty**.
