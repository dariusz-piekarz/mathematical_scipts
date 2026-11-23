# Topologia ogólna — audyt globalny 44: 22 niezależne kontrole w rozdziałach 01–09 i 13–15

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zamrożony commit źródeł:** `4b65edb4fdc9848e46b03adc7398c2956629b34f`.

**Cel:** przeprowadzić rzeczywisty, selektywny audyt matematyczny 22 istotnych dowodów pominiętych w niedawnych audytach globalnych 42–43, w szczególności próbować obalić implikacje w konstrukcjach topologicznych i dowodach wieloetapowych. Każdy poniższy dowód sprawdzono z tekstu aktualnego `.tex` i jego hipotez, nie tylko z etykiety w rejestrze 325/325. **Nie jest to nowy pełny audyt każdego środowiska proof 01–26.**

## 1. Wersje źródeł

| Rozdział | SHA bloba źródła | Sprawdzone dowody |
|---|---|---:|
| 01 — Przestrzenie topologiczne | `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6` | 3 |
| 02 — Operacje na zbiorach | `53a8dc7e62590a9011bd5858eedb4141c5f38162` | 3 |
| 03 — Ciągłość odwzorowań | `b571753b5ab9a8777424fc32f6c4a54a4048af77` | 1 |
| 04 — Konstrukcje topologiczne | `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` | 3 |
| 07 — Zwartość | `0c31028e8fd301d805781b676c6713a2572501cf` | 2 |
| 09 — Aksjomaty przeliczalności | `f483271af93842198c094c95f73a68584e835215` | 1 |
| 13 — Zupełność jednostajna | `c9078636452731e42a56196e84b5ed9831120e6b` | 3 |
| 14 — Zwartość lokalna | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | 3 |
| 15 — Parazwartość | `82e0fb5be75489017c8ea1844c698c87ce580901` | 3 |
| **Suma** | — | **22** |

Rozdziały 05, 06 i 08 mają odrębne niedawne kontrole w audytach 36–41 i nie naliczamy ich ponownie jako nowych audytów w tym raporcie. Źródła wszystkich dziewięciu powyższych rozdziałów mają niezmienione SHA względem globalnego rejestru 31.

## 2. Fundamenty konstrukcji topologicznych — 01–04 (10 dowodów)

1. **01, `thm:topog-kryterium-bazy` (proof od wiersza 548): PASS.** Dla dowolnego x∈U∩V warunek (B2) daje element bazowy zawarty w U∩V. Dzięki sumowaniu *wszystkich* odpowiednich elementów bazy nie potrzeba funkcji wyboru dla każdego x. Pokrywanie (B1) włącznie z X=∅, suma pustej rodziny i przypadek pustego przecięcia są ujęte.
2. **01, `thm:topog-podbaza-konstrukcja` (681): PASS.** Uwzględnienie przecięcia pustej podrodziny jako X usuwa konieczność wymagania, żeby podbaza pokrywała X. Każda topologia zawierająca podbazę zawiera też jej skończone przecięcia i dowolne sumy, więc konstrukcja jest minimalna, a nie tylko jedną z dopuszczalnych.
3. **01, `thm:topog-przeciecia-topologii` (812): PASS.** Przecięcie dowolnej *niepustej* rodziny topologii zachowuje odpowiednie operacje, a dla I=∅ poprawnie otrzymujemy `𝒫(X)`. Rodzina topologii zawierających wskazaną rodzinę zbiorów jest niepusta dzięki topologii dyskretnej.
4. **02, `thm:topog-domkniecie-pochodny` (404): PASS.** Kluczowa równość `cl A=A∪A'` nie potrzebuje T1: w kierunku od `cl A\\A` punkt x jest automatycznie różny od wszystkich elementów A. Równość `Iso(A)=A\\A'` sprawdza się dla izolacji względnej w A.
5. **02, `thm:topog-pochodny-t1` (468): PASS.** Przy x∉A' można wybrać otwarty U z `U∩(A\\{x})=∅`. Dla każdego y∈U\\{x}, T1 gwarantuje otwartość `U\\{x}`, który nie spotyka A. Zatem U⊂X\\A'. Bez T1 rozumowanie naprawdę zawodzi (w źródle znajduje się dwupunktowy kontrprzykład antydyskretny).
6. **02, `thm:topog-kuratowski` (690): PASS.** Monotoniczność operatora wynika z `c(A∪B)=c(A)∪c(B)`; domknięcie rodziny zbiorów stałych `c(F)=F` na dowolne przecięcia wymaga tej monotoniczności i `A⊂c(A)`, natomiast na skończone sumy — (K3). Sam operator odtworzonej topologii jest równy c z jego idempotentności, a jednoznaczność wynika z identycznych zbiorów domkniętych.
7. **03, `thm:topog-sklejanie-domkniete` (410): PASS.** W dowodzie używa się *skończoności* pokrycia przez domknięte F_j. Dla każdego domkniętego C⊂Y przeciwobrazy w F_j są domknięte w X, gdyż F_j są domknięte; ich skończona suma jest domknięta w X. Argument nie rozszerza tego błędnie na dowolne rodziny.
8. **04, `thm:topog-iloczyn-uniwersalnosc` (263): PASS.** Ciągłość do produktu jest równoważna ciągłości wszystkich rzutów z powodu podbazy `π_i^{-1}(U)`; dla I=∅ produkt jest jednoelementowy i twierdzenie działa bez wyjątków.
9. **04, `prop:topog-rzutowania-otwarte` (282): PASS.** W otwartym niepustym prostokącie produktowym istnieje punkt bazowy, który pozwala ustalić wszystkie współrzędne poza j; obraz rzutu jest dokładnie U_j. Jeśli prostokąt jest pusty, jego obraz jest pusty i otwarty. Dowód nie przypisuje surjektywności rzutom, gdy inne czynniki są puste.
10. **04, `thm:topog-iloraz-uniwersalnosc` (574): PASS.** Istnienie i jednoznaczność h:Y→Z używają surjektywności q i stałości g na włóknach. Równoważność ciągłości `h∘q` i h wynika z *topologii ilorazowej*, a nie jest automatyczną własnością dowolnej surjekcji ciągłej.

## 3. Zwartość, wybór, przeliczalność — 07 i 09 (3 dowody)

11. **07, `lem:topog-zwartosc-ultrafiltr-zorn` (523): PASS.** Suma rosnącego łańcucha filtrów właściwych jest filtrem właściwym: dla dwóch jego elementów wybiera się większy z dwóch filtrów łańcucha. Pusty łańcuch ma górne ograniczenie w postaci filtru wyjściowego. Użycie lematu Zorna i zasady wyboru jest jawne.
12. **07, `thm:topog-tychonoff-iloczyny` (606): PASS.** W przypadku pustej rodziny produkt jest singletonem, a przy pustym czynniku produkt jest pusty. W pozostałym przypadku AC zapewnia niepustość produktu i jednoczesny wybór granic współrzędnych ultrafiltru. Filtr obrazu przez rzutowanie jest ultrafiltrem, a skończone przecięcia cylindrów zapewniają zbieżność do wybranego punktu produktu. Nie ma wymogu Hausdorffowości czynników.
13. **09, `thm:topog-sorgenfrey-wlasnosci-przeliczalnosc` (406): PASS.** Przeliczalne bazy otoczeń `[x,x+1/n)` i gęstość Q są poprawne; funkcja `x↦n(x)` byłaby iniekcją R→N przy drugim aksjomacie przeliczalności. W trudniejszej części Lindelöfa zbiór `G=⋃(a,b)` ma przeliczalne pokrycie euklidesowe, a `F=R\\G` jest przeliczalny: dla x<y w F przedział `(x,q_x)⊂G` zmusza `q_x≤y<q_y`. Iniekcja `x↦q_x∈Q` domyka argument bez nieuprawnionego utożsamienia topologii euklidesowej i Sorgenfreya.

## 4. Zupełność jednostajna — 13 (3 dowody)

14. **13, `lem:topog-uzupelnienia-minimalizacja` (258): PASS.** Bazę filtra `𝔽°` tworzą zbiory E[A]; wspólny element bazy dla dwóch należy do relacji `(E∩D)[A∩B]`. Użycie relacji symetrycznej D i trzeciej potęgi `D³⊂V` jest niezbędne do warunku Cauchy'ego. Z bliskości 𝔽 i 𝔾 dostajemy B∈𝔾 zawarty w dowolnym E[A], skąd `𝔽°⊂𝔾`; to jednocześnie daje minimalność i jednoznaczność.
15. **13, `thm:topog-uzupelnienia-istnienie` (329): PASS.** Sprawdzono zwłaszcza orientację par w `B(H,E)`, która była źródłem wcześniejszej poprawki: dla bliskości `(𝔽,ι(x))∈D̂` należy odwrócić parę przez symetrię D, zanim stwierdzi się `(ι(x),𝔽)∈Ê`. W części zupełności symetryczne `D⁴⊂E` umożliwia złożenie dwóch relacji `D̂²`; wybór `T[x]` i `C∈𝔽₀` faktycznie daje `(ι(x),𝔽₀)∈D̂²`. Nie zastąpiono tu bliskości filtrów samą zbieżnością punktową.
16. **13, `lem:topog-uzupelnienia-rozszerzenie` (585): PASS.** Gęstość A zapewnia niepustość bazowych `A∩E[z]`; jednostajna ciągłość f przenosi ich warunek Cauchy'ego na filtr obrazowy. W dowodzie jednostajnej ciągłości rozszerzenia użyto *domknięcia* relacji W w produkcie Y×Y; dla symetrycznego T z `T³⊂V` otrzymuje się `cl(T)⊂T³⊂V`, ponieważ przekroje T[y], T[y'] są otoczeniami punktów, niekoniecznie otwartymi. Jednoznaczność wymaga Hausdorffowości Y i jest wskazana.

## 5. Zwartość lokalna i parazwartość — 14–15 (6 dowodów)

17. **14, `thm:topog-baire-lokalnie-zwarte` (61): PASS.** Rekurencja `K_{n+1}⊂W_n∩G_{n+1}` zapewnia zstępujące *niepuste zwarte* domknięcia. Wszystkie K_n są domknięte w Hausdorffowej X i zawierają się w zwartym K₁, więc własność skończonych przecięć daje niepustą część wspólną. Nie potrzeba żadnej metryki ani zwartości domkniętych kul.
18. **14, `thm:topog-lokalna-dowolny-iloczyn` (157): PASS w ZFC.** Przy lokalnej zwartości produktu bazowy cylinder w zwartym K wymusza zwartość wszystkich czynników poza skończonym zbiorem F, ponieważ `p_i(B)=X_i=p_i(K)` dla i∉F. Lokalna zwartość każdego czynnika pochodzi ze zwartego `p_i(K)` zawierającego otwarte otoczenie wybranego punktu. Przesłanka niepustości wszystkich czynników i AC pozwala wybierać punkty produktu; dla pustego indeksu wynik jest prawdziwy dla singletonu.
19. **14, `thm:topog-lokalna-wyczerpanie` (268): PASS.** W lokalnie zwartej Hausdorffowej przestrzeni dowolny kompakt C jest zawarty we wnętrzu pewnego większego kompaktu K: otwarte wnętrza H_x pokrywają C i mają podpokrycie skończone. Indukcja wciąga `K_n∪C_{n+1}` do wnętrza K_{n+1}. Rosnące wnętrza wyczerpują X i pochłaniają każdy kompakt przez podpokrycie skończone; przypadek X=∅ jest zgodny z K_n=∅.
20. **15, `thm:topog-parazwartosc-lindelof` (185): PASS.** Z regularności i Lindelöfa uzyskuje się przeliczalne otwarte W_n, V_n o `cl W_n⊂V_n⊂cl V_n⊂U_n`. Lemat Urysohna daje f_n=1 na cl W_n oraz nośnik w U_n. Teleskopowe funkcje `φ_n=f_n∏_{j<n}(1-f_j)` spełniają sumę 1. Kluczowa lokalna skończoność nośników wynika z f_N≡1 **na całym otwartym W_N**: wszystkie φ_n, n>N, zerują się na tym otoczeniu, nie tylko w samym punkcie.
21. **15, `thm:topog-parazwartosc-stone` (341): PASS.** Pokrycie jest dobrze uporządkowane i każdemu z przypisuje się pierwszy α(z); dzięki temu dla β<γ punkt środka z∈E_{γ,i} nie należy do U_β, a z `B(y,3r_i)⊂U_β` wynika odległość między różnymi rodzinami tego poziomu >r_i. Dla danego punktu x po znalezieniu `x∈V_{α,n}` małe otoczenie O nie spotyka *żadnego* poziomu i≥M, bo ich środki muszą leżeć poza wcześniejszym V_{α,n}; na każdym z finitely many poziomów i<M O spotyka najwyżej jeden zbiór. Jest to rzeczywista lokalna skończoność całej rodziny, nie tylko punktowa.
22. **15, `thm:topog-parazwartosc-nagata-smirnow` (507): PASS.** Konieczność używa twierdzenia Stone'a do lokalnie skończonych uszczegółowień pokryć przez kule. W wystarczalności lokalna skończoność każdej `𝓑_n` zapewnia domkniętość sum domknięć, konieczną do normalności i do konstrukcji `g_G>0 ⇔ x∈G`. Z wagami 2⁻ⁿ i lokalną skończonością na skończenie wielu poziomach mapa `F:X→ℓ∞(J)` jest ciągła w **normie supremum**, nawet dla nieprzeliczalnego J. Bazowość i dodatniość `f_{n,B}` wykazują ciągłość odwrotnej na F(X); konstruowana metryka rzeczywiście indukuje wyjściową topologię.

## 6. Rozliczenie usterek i stanu technicznego

**22/22 sprawdzone dowody — PASS.** Nie znaleziono nowej luki matematycznej wymagającej edycji źródeł. Jest to osobny, rzeczywisty odczyt i ponowne uzasadnienie wskazanych dowodów, nie formalizacja w Lean ani mechaniczne potwierdzenie całych 325/325. Każdy omawiany wynik ma etykietę w rejestrach globalnych 33–35 i wskazany SHA źródła.

**Weryfikacja poprzedniego CI:** workflow [45136528206](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136528206) dotyczący raportu globalnego 43, commit `a32078b7f197827b2d60dbc609b7055deca62da7`, ma faktyczny stan `completed/success`. Ponieważ źródła 26 rozdziałów nie zmieniły się, nie ma potrzeby unieważnienia wcześniejszych 2+1. Nowy workflow wywołany zapisem niniejszego raportu wymaga odrębnego zakończenia.

**Następny etap:** finalna weryfikacja źródłowych zależności od zewnętrznych twierdzeń (np. Brouwer w rozdziale 23) i ich rzeczywistej dostępności w bibliotece, kontrola raportów o ograniczonym zakresie, finalny CI HEAD i decyzja czy globalny audyt można zamknąć bez nadmiernych twierdzeń o kompletności niezależnych audytów.
