# Analiza funkcjonalna — rozdział 02 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex`.  
**Wynik:** pierwotny audyt zakończony poprawkami; rozdział **NIEUSTABILIZOWANY**, wymagane kolejne czyste audyty.

## Zakres

Kontrola wszystkich 14 dowodów, 7 przykładów, sformułowań definicji, wymaganego warunku Hausdorffa, przypadków pustych rodzin, nieskończonych produktów, ilorazów przez podprzestrzenie niedomknięte, ciągłości łącznej działań, normy ilorazowej, topologii początkowej i końcowej, ograniczoności, odsyłaczy do 01 i 05 oraz terminologii `AGENTS.md`.

## Macierz dowodów: 14/14 sprawdzonych

1. **Podprzestrzeń z topologią indukowaną:** równość przeciwobrazów otwartych zbiorów dla dodawania i mnożenia przez skalar oraz dziedziczenie Hausdorffa — **PASS**.
2. **Domknięcie podprzestrzeni:** `cl(M)=∩_{U∋0}(M+U)`, symetryczne otoczenia i ciągłość mnożenia przez niezerowe skalary — **PASS**.
3. **Uniwersalna własność podprzestrzeni:** ciągłość `f:Z→M` równoważna ciągłości `i∘f` — **PASS**.
4. **Produkt TVS:** ciągłość i otwartość rzutów; ciągłość działań z własności produktu; rozdzielanie punktów współrzędnie — **PASS**.
5. **Ograniczoność w produkcie:** ograniczoność projekcji w obie strony, skończona liczba kontrolowanych współrzędnych i zrównoważone otoczenia; sprawdzono `I=∅` — **PASS**.
6. **Funkcjonały ciągłe na `K^I`:** liniowe funkcjonały mogą zależeć tylko od skończonej liczby współrzędnych; argument ze skalowaniem wektora z zerami na `F` — **PASS**.
7. **Iloraz jako TVS:** rzut `q` jest otwarty; `q×q` i `id×q` są otwartymi surjekcjami ilorazowymi; ciągłość działań; Hausdorff wtedy i tylko wtedy, gdy `M` domknięta — **PASS**.
8. **Uniwersalna własność ilorazu:** charakterystyka topologii ilorazowej poprzez preobrazy i jednoznaczne faktoryzowanie liniowych `T` zerujących `M` — **PASS**.
9. **Pierwsze twierdzenie o izomorfizmie (topologiczne):** ciągła bijekcja `X/ker(T)→T(X)` jest homeomorfizmem dokładnie przy otwartości `T` na swój obraz — **PASS**.
10. **Norma ilorazowa:** niezmienniczość wyboru reprezentanta, norma przy domkniętej `M`, równość kul, zgodność topologii, zupełność przez wybór podciągu i reprezentantów z sumowalnymi przyrostami — **PASS**.
11. **Topologia początkowa liniowa:** ciągłość działań z uniwersalnej własności, charakterystyka ciągłości odwzorowań do `X`, Hausdorff przy `∩ker(T_i)={0}` gdy `Y_i` Hausdorffa — **PASS**.
12. **Końcowa topologia liniowo-topologiczna:** istnienie największej dopuszczalnej topologii przez połączenie wszystkich dopuszczalnych topologii; ciągłość działań na podbazie; własność uniwersalna względem liniowych `S` — **PASS**.
13. **Skończone sumy proste:** uniwersalna własność i złożenie `S=\sum_i(S∘j_i)∘π_i` — **PASS**.
14. **Hausdorffyzacja:** `N=cl({0})` jest podprzestrzenią domkniętą, `X/N` jest Hausdorffa, a `N⊂ker(T)` dla każdego ciągłego liniowego `T` do TVS Hausdorffa — **PASS**.

## Przykłady: 7/7

1. Wielomiany gęste w `C([0,1])`, ale bez zupełności normy indukowanej.
2. Zbieżność punktowa funkcji typu `max(0,1-n²|t-1/n|)` przy zachowanej normie supremum 1.
3. Identyczność na `C([0,1])` między normą supremum a całkową jako ciągła bijekcja nieotwarta.
4. Iloraz przez jądro funkcjonału wartościowania: `[f]↦f(0)` z ciągłym prawym odwrotnym.
5. Produkt i podprzestrzeń jako przykłady topologii początkowej.
6. Końcowa topologia na `R²` po włożeniach obu osi: `{(1,1)}` otwarty, `{(0,0)}` nie; złamanie ciągłości przesunięcia.
7. `φ=⊕_n K e_n`: zbieżność `e_n→0` w topologii odziedziczonej z produktu, brak takiej zbieżności dla seminorm `p_a`; końcowa własność w kategorii lokalnie wypukłej.

Wszystkie przykłady merytorycznie poprawne; ilustracja ilorazu `R²/M` objęta osobną kontrolą PDF.

## Wprowadzone korekty

- Zastąpiono samodzielne wyrażenia „dual topologiczny” i „dualu algebraicznego” poprawnym opisem przestrzeni funkcjonałów, pozostawiając historyczną etykietę `thm:product-dual`.
- Wyrażenie „rodziny map” (w znaczeniu mapping) zastąpiono „rodziny odwzorowań”.
- W przykładzie `φ` wzmocniono krok dowodu ciągłości `S`: otwarte otoczenie `{x:p_a(x)<ε}` zawiera się w przeciwobrazie `{z:p(z)<ε}`. Rozumowanie dotyczy funkcjonałów seminormowych definiujących topologię docelową; wykorzystuje liniowość i kryterium ciągłości w zerze.
- Zachowano wszystkie 15 etykiet, 14 dowodów, 7 przykładów, historyczne identyfikatory odsyłaczy i materiał tematyczny.

## Kontrole techniczne

- Dodano `tools/tests/test_functional_analysis_ch02.py` — 9 testów strukturalnych, terminologicznych, matematycznych modeli i realnych odsyłaczy do rozdziałów 01, 02 oraz 05.
- Dodano `.github/workflows/functional-analysis-ch02.yml`: buduje PDF z aktualnych rozdziałów 01, 02 i 05 z oryginalną preambułą książki; rozdziały 01 i 05 stanowią rzeczywisty kontekst odsyłaczy.
- Pierwszy przebieg CI [45152469928](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152469928) wykrył pięć nierozwiązanych odsyłaczy w rozdziale 05, wynikających wyłącznie z niepełnego wrappera (brak rozdziałów 03 i 04); kompilacja PDF sama w sobie zakończyła się sukcesem. **Poprawiono workflow bez wyłączania testu odsyłaczy**: kontekst obejmuje rzeczywiste źródła 01–05.
- [Końcowy przebieg 45152793250](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152793250): **9/9 testów PASS**, kompilacja LaTeX PASS, 0 nierozwiązanych odsyłaczy i brak przepełnionych wierszy — **PASS**; artefakt PDF i log załączone do przebiegu. PDF kontekstowy ma **33 strony A4**, rozdział 02 zajmuje strony **7–15** (na stronie 15 kończy się tekst rozdziału 02, po czym rozpoczyna się rozdział 03). Wszystkie strony 7–14 obejrzano wizualnie, w tym rysunek 2.1 ilorazu; nie znaleziono kolizji napisów ani ucięć. Dodatkowo sprawdzono treść początku strony 15.

## Propozycje nieobowiązkowe

- Przedstawić na rysunku jednocześnie topologię początkową i końcową przez diagram uniwersalnej własności. Nie dodawać bez akceptacji.
- Osobno rozbudować porównanie końcowej topologii zwykłej i końcowej topologii liniowo-topologicznej na `R²` (dwa włożenia osi). Nie jest niezbędne do poprawności istniejącego argumentu.

## Decyzja

**Audyt 02/01: wykonany z poprawkami, NIE jest czystym audytem.** Kolejne iteracje mają pozostać przy rozdziale 02 aż do co najmniej dwóch kolejnych czystych audytów, a dopiero potem przejść do 03.
