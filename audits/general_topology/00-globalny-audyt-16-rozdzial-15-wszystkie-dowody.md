# Topologia ogólna — globalny audyt 16: rozdział 15, wszystkie siedem dowodów

**Data:** 2026-11-22.
**Badany blob źródła:** `82e0fb5be75489017c8ea1844c698c87ce580901`.
**Źródło:** `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`.
**Metoda:** niezależna kontrola wszystkich 7 środowisk `proof`, osobno podziałów jedności, konstrukcji Stone'a i twierdzenia Nagaty–Smirnowa; weryfikacja przykładów i realnego PDF, bez ingerencji w stabilne źródło.

## 1. Wszystkie dowody

1. **Domknięcia rodzin lokalnie skończonych — `prop:topog-parazwartosc-domkniecia`.** Jeśli otwarty O przecina tylko A_i dla i w skończonym F, to jest rozłączny także z domknięciami A_i dla i∉F. Stąd domknięcia pozostają lokalnie skończone. Równość `cl(∪A_i)=∪cl(A_i)` jest wykazana przez usunięcie skończenie wielu domkniętych zbiorów z O; ten krok rzeczywiście wymaga lokalnej skończoności, nie tylko punktowej skończoności.
2. **Podział jedności daje uszczegółowienie — `prop:topog-parazwartosc-jednosc-pokrycie`.** Zbiory `V_i={φ_i>0}` są otwarte i pokrywają X przez sumę równą 1. W każdym punkcie otoczenie spotykające skończenie wiele nośników spotyka nie więcej odpowiednich V_i, a każdy V_i jest zawarty w wybranym elemencie pokrycia. Nie użyto Hausdorffowości.
3. **Funkcja odcinająca — `lem:topog-parazwartosc-odciecia`.** Urysohn oddziela domknięte F i X\\W funkcją ciągłą f; z f=0 na X\\W wynika `supp f⊆cl W⊆V`. Warunek dodatkowego otwartego W jest jawny, dzięki czemu nie ma nieuprawnionego utożsamienia `f=0` poza V z `supp f⊆V`.
4. **Lindelöf i podziały jedności — `thm:topog-parazwartosc-lindelof`.** Regularność daje `x∈W_x⊆cl W_x⊆V_x⊆cl V_x⊆U_x`. Lindelöf daje rodzinę przeliczalną (W_n), a normalność regularnej przestrzeni Lindelöfa (z rozdz. 10) umożliwia funkcje f_n=1 na cl W_n i z nośnikami w U_n. Dla `φ_n=f_n∏_{j<n}(1−f_j)`, jeśli x∈W_N, wszystkie φ_n z n>N znikają na *całym otwartym* W_N, więc także ich nośniki są z nim rozłączne. To jest poprawny dowód lokalnej skończoności, nie wyłącznie punktowej. Teleskopowanie sum `Σ_{n≤m}φ_n=1−∏_{n≤m}(1−f_n)` i f_N=1 daje sumę równą 1. Pusty X i skończone podpokrycie są osobno obsłużone.
5. **Dwie klasy przestrzeni — `cor:topog-parazwartosc-klasy`.** W pierwszej metryzowalność i drugi aksjomat przeliczalności zapewniają regularność T1 i Lindelöfa. W drugiej lokalna zwartość + Hausdorff umożliwiają lokalne zwężanie otoczeń, a σ-zwartość daje Lindelöfa przez zsumowanie skończonych podpokryć kompaktów.
6. **Stone — `thm:topog-parazwartosc-stone`.** Dla każdego środka z∈E_{α,n} mamy z∉ wcześniejsze poziomy, α(z)=α i B(z,3r_n)⊆U_α. Zatem V_{α,n}⊆U_α. Każdy punkt x należy albo do wcześniejszego poziomu, albo jest środkiem na dostatecznie drobnym poziomie. Przy α<β środki y∈E_{α,i}, z∈E_{β,i} spełniają z∉U_α, a więc d(y,z)≥3r_i. Punkty p∈V_{α,i}, q∈V_{β,i} spełniają d(p,q)>r_i; kula o średnicy ≤r_i spotyka co najwyżej jeden zbiór na poziomie i. Dla x∈V_{α,n} wybór B(x,ρ)⊆V_{α,n}, M>n z 2r_M<ρ, O=B(x,r_M) eliminuje wszystkie poziomy i≥M: ich środki pozostają poza V_{α,n}. Dla i<M średnica O jest ≤r_i, więc na każdym z skończenie wielu poziomów O spotyka najwyżej jeden V_{β,i}. W efekcie całe uszczegółowienie jest lokalnie skończone. Nie używa się zupełności, ośrodkowości ani założenia przeliczalności; użyty jest dobry porządek indeksów pokrycia.
7. **Nagata–Smirnow — `thm:topog-parazwartosc-nagata-smirnow`.** Kierunek metryczny korzysta ze Stone'a do rozdrobnienia pokryć kulami 2⁻ⁿ; czynnik `2^{1−n}` kontroluje średnicę wybranego elementu i daje bazę. W kierunku odwrotnym lokalna skończoność B_n daje `cl(∪B)=∪cl B`, co pozwala oddzielić dowolne rozłączne domknięte A,C przez otwarte P,Q, zdefiniowane przez skończone odejmowanie domknięć Q_j i P_j. Z normalności przez Urysohna konstruuje się dla każdego otwartego G funkcję g_G ciągłą i dodatnią dokładnie na G. Funkcje `f_{n,B}=2^{-n}g_B` definiują F:X→ℓ∞(J) przy ewentualnie nieprzeliczalnym J. Ogon n≥N ma jednostajnie małą normę supremum, a lokalna skończoność B_n na skończenie wielu poziomach n<N zapewnia skończenie wielu aktywnych współrzędnych w otoczeniu x. Zatem F jest ciągłe **w normie supremum**. T1 i własność bazy dają rozdzielanie punktów; dla otwartego G i x∈G pojedyncza dodatnia współrzędna f_{n,B}(x) kontroluje otoczenie w przestrzeni obrazowej, dając ciągłość odwrotności. Rzeczywiście otrzymuje się metrykę `d(x,y)=sup_J|f_{n,B}(x)−f_{n,B}(y)|`.

## 2. Niezależne sprawdzenie przykładów, hipotez i kontrprzykładów

- Rodzina przedziałów `(n−1/3,n+1/3)`, n∈Z, jest lokalnie skończona: w każdym ograniczonym otoczeniu można spotkać tylko skończenie wiele środków całkowitych. Przedziały `(−1/n,1/n)` nie spełniają lokalnej skończoności w 0.
- Funkcje „namiotowe” `h_n(x)=max(0,1−|x−n|)` mają nośniki [n−1,n+1] i sumują się do 1; lokalna skończoność nośników jest jawna. Każdy nośnik mieści się w otwartym `(n−3/2,n+3/2)`.
- Każda nieprzeliczalna przestrzeń dyskretna jest parazwarta przez singletony i ma odpowiedni podział jedności z funkcji charakterystycznych `χ_{\{x\}}`, ale nie jest Lindelöfa. Dzięki temu żadna z równoważności nie myli parazwartości z przeliczalnością bazy.
- W Nagacie–Smirnowie każda rodzina B_n może być nieprzeliczalna, co jest zgodne z przestrzenią `ℓ∞(J)`. Nie zastąpiono normy supremum topologią produktową.
- W przypadku X=∅ wszystkie twierdzenia zachowują sens. Wybór dobrego porządku pokrycia Stone'a korzysta z aksjomatu wyboru, jawnie dopuszczonego w kontekście Tychonoffa.

## 3. Wykonane testy i oględziny

- Zapisany workflow [45070070493](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070070493) zakończył się `completed/success`; kontrolowany blob rozdziału 15 nie zmienił się między nim a bieżącą gałęzią.
- Z artefaktu `14773205627` wypakowano samodzielny `general_topology_ch15.pdf` i jego log. PDF ma **6 stron A4**; wyrenderowano i przejrzano wszystkie sześć stron. W logu nie występują `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`. Nie ma ilustracji wymagających osobnej kontroli TikZ.
- Istniejący `tools/tests/test_general_topology_ch15.py` testuje tożsamość teleskopową, podział „namiotowy” i skończone przypadki konstrukcji Stone'a; takie testy są kontrolą regresji, a nie formalnym dowodem twierdzenia dla dowolnej przestrzeni metrycznej.
- Przy kontroli wszystkich siedmiu dowodów nie znaleziono nienazwanej zależności od późniejszego rozdziału. Urysohn, Lindelöf, regularność i zwężanie otoczeń są udowodnione wcześniej.

## Werdykt

**PASS — 7/7 środowisk dowodowych, przykłady i hipotezy, wszystkie 6 stron samodzielnego PDF.** Brak nowej usterki. Rozdział 15 zachowuje status stabilny i niezmieniony blob `82e0fb5be75489017c8ea1844c698c87ce580901`.
Globalny audyt pełnego zbioru dowodów 01–26 nie jest jeszcze zamknięty. Następnym blokiem będzie rozdział 16 i niezależna kontrola jego siedmiu dowodów, bez ograniczania się do wcześniej sprawdzanej charakterystyki uzwarceń.
