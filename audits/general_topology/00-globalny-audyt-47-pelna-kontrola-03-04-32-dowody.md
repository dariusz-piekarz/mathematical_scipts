# Topologia ogólna — globalny audyt 47: pełna niezależna kontrola 32 dowodów rozdziałów 03–04

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Bloby źródeł:** 03 `b571753b5ab9a8777424fc32f6c4a54a4048af77`; 04 `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081`. Weryfikowano pełną aktualną treść **15 + 17 = 32 środowisk `proof`** oraz hipotezy wyników, bez przepisywania ustaleń z historycznych raportów 12–17. **Żadne źródło matematyczne nie było zmieniane.**

## Rozdział 03 — wszystkie 15 dowodów

| ID | Etykieta | Niezależna kontrola |
|---|---|---|
| 03-01 | `thm:topog-ciaglosc-kryteria-globalne` | Weryfikacja pełnego cyklu (i)⇒(ii)⇒(iii)⇒(iv)⇒(ii)⇒(i) przez domknięcia, obraz i przeciwobrazy; nie założono T1. |
| 03-02 | `prop:topog-ciaglosc-wnetrze` | Przeciwobraz otwartego int B jest otwartym podzbiorem przeciwobrazu B; wymagana jest inkluzja, nie równość. |
| 03-03 | `thm:topog-ciaglosc-punktowa-globalna` | Przejście między otwartymi zbiorami a dowolnymi otoczeniami wykorzystuje mniejsze otwarte otoczenie; pusty przeciwobraz jest otwarty. |
| 03-04 | `thm:topog-ciaglosc-eps-delta` | Dwa kierunki wynikają dokładnie z bazy kul w obu metryzowanych przestrzeniach; kwantyfikator δ zależy od ε i x. |
| 03-05 | `thm:topog-ciaglosc-bazy-podbazy` | Przeciwobrazy zachowują dowolne sumy i skończone przecięcia; pusta suma ma przeciwobraz ∅, puste przecięcie podbazy to Y. |
| 03-06 | `prop:topog-porownanie-przez-ciaglosc` | Dla identyczności odwzorowanie odwrotne na podzbiorach jest identycznością, więc ciągłość (X,τ₁)→(X,τ₂) odpowiada inkluzji τ₂⊂τ₁ (nie odwrotnej). |
| 03-07 | `thm:topog-skladanie-ciaglych` | Przeciwobraz otwartego W przez g∘f jest f⁻¹(g⁻¹(W)); ciągłość każdego czynnika daje otwartość kolejno w Y i X. |
| 03-08 | `prop:topog-ograniczanie-ciaglosci` | Dla dziedziny A: A∩f⁻¹(V) jest względnie otwarty. Dla przeciwdziedziny B: f(X)⊂B jest hipotezą konieczną dla identyczności przeciwobrazów. |
| 03-09 | `thm:topog-ciaglosc-lokalna-pokrycie` | Otwartość każdego U_i w X umożliwia przeniesienie względnej otwartości przeciwobrazów na X; dla I=∅ mamy X=∅. |
| 03-10 | `thm:topog-sklejanie-domkniete` | Dla domkniętego C⊂Y przeciwobraz przecina każde domknięte F_j w zbiorze domkniętym X. Skończona suma jest domknięta; dla nieskończonej rodziny dowód zawodzi, kontrprzykład źródłowy jest poprawny. |
| 03-11 | `prop:topog-otwarte-domkniete-kryteria` | Dla otwartego U, f(U)⊂int f(U) wraz z odwrotnym zawieraniem daje otwartość. Dla domkniętego F, cl f(F)⊂f(F) daje domkniętość. |
| 03-12 | `prop:topog-skladanie-otwartych-domknietych` | Złożenie obrazu zbioru otwartego (odpowiednio domkniętego) zachowuje tę własność na każdym etapie. |
| 03-13 | `thm:topog-homeomorfizm-kryteria` | Dla bijekcji f ciągłość odwrotności h jest równoważna otwartości f przez h⁻¹(U)=f(U), analogicznie przez kryterium zbiorów domkniętych. |
| 03-14 | `prop:topog-homeomorfizm-operacje` | Równości wnętrz i domknięć wymagają zarówno f, jak i f⁻¹; bijektywność zabezpiecza obrazy dopełnień/przecięć oraz warunek U∩(A\{x}). |
| 03-15 | `prop:topog-zanurzenie-kryterium` | Ciągła iniekcja X→Y pozostaje ciągła do f(X). Otwartość względna obrazu każdego otwartego U czyni ją homeomorfizmem na obraz; bez niej iniekcja ciągła nie wystarcza. |

**Werdykt 03: 15/15 PASS.** Szczególną uwagę poświęcono brakowi założeń T1 w kryteriach ciągłości, właściwej orientacji inkluzji topologii przy identyczności, skończoności pokrycia domkniętego i względnej otwartości zanurzenia. Raport 17 potwierdza też tę samą wersję źródła po korekcie wcześniejszego wydania.

## Rozdział 04 — wszystkie 17 dowodów

| ID | Etykieta | Niezależna kontrola |
|---|---|---|
| 04-01 | `prop:topog-podprzestrzen-topologia` | Tożsamości A∩∪U_i=∪(A∩U_i) oraz (A∩U)∩(A∩V)=A∩(U∩V) dowodzą aksjomatów także dla rodziny pustej. |
| 04-02 | `prop:topog-podprzestrzen-domkniecie` | Względnie domknięte B mają postać A∩F dla F domkniętego w X; minimalność cl_X B daje cl_A B=A∩cl_X B. |
| 04-03 | `prop:topog-podprzestrzen-wnetrze` | Wzór int_A B=A\cl_X(A\B) i brzeg_A B=A∩cl_X B∩cl_X(A\B) wynika z domknięcia względnego i dopełnień w A. |
| 04-04 | `prop:topog-podprzestrzen-przechodniosc` | B∩(A∩U)=B∩U daje przechodniość topologii; iota⁻¹(U)=A∩U daje ciągłość włożenia. |
| 04-05 | `thm:topog-do-podprzestrzeni` | Wszystkie zbiory otwarte w A mają postać A∩V; przy f(X)⊂A ich przeciwobrazy są równe (iota∘f)⁻¹(V). |
| 04-06 | `thm:topog-iloczyn-baza` | Skończone przecięcia cylindrów podbazowych są dokładnie prostokątami z ograniczonymi skończenie wieloma współrzędnymi. Powtórzone indeksy wymagają przecięcia U_i; I=∅ daje P. |
| 04-07 | `thm:topog-iloczyn-uniwersalnosc` | Warunek ciągłości wszystkich rzutów odpowiada otwartości przeciwobrazów cylindrów podbazowych. Dla pustej rodziny iloczyn to singleton. |
| 04-08 | `prop:topog-rzutowania-otwarte` | Obraz pustego prostokąta to ∅; dla niepustego wybór jednego punktu pozwala dowolnie zmienić j-tą współrzędną, otrzymując π_j(W)=U_j. Brak surjekcji przy innych pustych czynnikach nie jest używany. |
| 04-09 | `prop:topog-iloczyn-domkniecie` | Przy pustym A lub B obie strony puste. W pozostałym przypadku każdy otwarty prostokąt spotyka A×B wtedy i tylko wtedy, gdy osobno oba jego czynniki spotykają A,B. |
| 04-10 | `prop:topog-suma-rozlaczna-topologia` | Suma/przecięcie zbiorów w sumie rozłącznej bada się po przekrojach; komponent i jego dopełnienie są otwarte, zaś iota_i jest homeomorfizmem na otwarto-domknięty obraz. |
| 04-11 | `thm:topog-suma-uniwersalnosc` | Dla każdego V otwartego w Y wszystkie przekroje f⁻¹(V) są odwrotnościami (f∘iota_i)⁻¹(V); definicja sumy rozłącznej domyka dowód, także przy I=∅. |
| 04-12 | `thm:topog-poczatkowa-uniwersalnosc` | Przeciwobrazy przez g podbazowych f_i⁻¹(U) są przeciwobrazami przez f_i∘g; topologia początkowa jest najsłabszą umożliwiającą ciągłość wszystkich f_i. |
| 04-13 | `prop:topog-koncowa-topologia` | Przeciwobrazy zbiorów przez f_i zachowują ∅, całość, sumy dowolne i przecięcia skończone; topologia końcowa jest najmocniejszą topologią zachowującą ciągłość wszystkich f_i. |
| 04-14 | `thm:topog-koncowa-uniwersalnosc` | Dla h:Y→Z warunek (h∘f_i)⁻¹(W) otwarty dla wszystkich i jest dokładnie definicją otwartości h⁻¹(W) w topologii końcowej. |
| 04-15 | `prop:topog-iloraz-nasycone` | Z definicji ilorazu q(A) otwarty wtedy i tylko wtedy, gdy jego pełny nasycony przeciwobraz jest otwarty; dla domkniętości przechodzi się do dopełnienia. |
| 04-16 | `thm:topog-iloraz-uniwersalnosc` | Niezależność h(y)=g(x) od reprezentanta wynika ze stałości g na włóknie, a jednoznaczność z surjektywności q. Ciągłość odzwierciedla topologia końcowa. |
| 04-17 | `prop:topog-otwarta-surjekcja-iloraz` | Ciągła otwarta surjekcja lub ciągła domknięta surjekcja jest ilorazowa: V=q(q⁻¹V); dla przypadku domkniętego używa się dopełnienia V i domkniętego przeciwobrazu. |

**Werdykt 04: 17/17 PASS.** Kontrola obejmowała puste iloczyny, puste czynniki, powtarzanie się indeksów we współrzędnych, rozróżnienie topologii początkowej i końcowej oraz konieczność surjektywności w ilorazie.

## Uzgodnienie z globalną macierzą 325/325 i ograniczenia

- Wszystkie **32 etykiety** są zgodne z wierszami `03-01…03-15` i `04-01…04-17` globalnego audytu 33. Użyto **aktualnych** blobów, a nie starszych SHA raportów sprzed zmian wydawniczych.
- Raport 46 już dokumentuje indywidualnie **21/21** dowodów rozdziałów 01–02. Łącznie raporty 46–47 dają **53/53 odrębne, jawnie opisane audyty dowodów 01–04**, niezmienione źródła.
- Historyczne raporty 12, 13 i 17 oraz testy CI pozostają odrębnymi kontrolami wydawniczymi i rozdziałowymi; nie zaliczano ich jako 32 nowe kontrole w tym dokumencie.
- Przegląd matematyczny nie jest formalizacją Lean ani nowym wizualnym oglądem wszystkich rysunków. Nie znaleziono błędu wymagającego edycji `.tex`.

**Następny etap:** szczegółowe przypisanie i ewentualny nowy reaudyt dowodów 05–13, następnie odrębne uzgodnienie 24–26 oraz ostateczny CI końcowego HEAD. Raporty globalne 15–25 pokrywają indywidualnie 106 dowodów 14–23, natomiast obecne źródła 06 i 21 mają osobno zamknięte 2+1 po korekcie rysunków. Nie wyłączać automatyzacji, dopóki końcowy audyt globalny nie uzyska uzasadnionego PASS.
