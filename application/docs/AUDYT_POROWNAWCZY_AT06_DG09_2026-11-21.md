# Audyt porównawczy AT-06 / DG-09 — etap IV

**Data:** 21 listopada 2026 r.  
**Repozytorium:** dariusz-piekarz/mathematical_scipts.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez zmian w main).  
**Zakres:** dokładnie dwa całe rozdziały:
- AT-06: chapters/pl/algebraic_topology/06-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex
- DG-09: chapters/pl/differential_geometry_and_topology/09-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex.

Audyt obejmuje zgodność matematyczną definicji, hipotez, dowodów, przykładów, rysunków, kodu, etykiet i odsyłaczy. Wzorzec szczegółowości: DG-01. Jest to kontrola porównawcza, a **nie fizyczne scalanie** ani deklaracja automatycznego utożsamienia twierdzeń o tej samej nazwie.

## 1. Wynik inwentaryzacji i źródłowy rejestr

Z rzeczywistych źródeł TeX po poprawkach:
- AT-06: 45 unikalnych etykiet;
- DG-09: 43 unikalne etykiety;
- wspólne nazwy etykiet: **42**;
- etykiety tylko w AT-06: prz:pi1-klein-hurewicz, prz:pi-2-3-komorki, fig:pi-2-3-komorki;
- etykieta tylko w DG-09: prz:dwiekrotne-dolaczenie-stopnie-dg09 (nowe obliczenie ogólne).

Wspólne etykiety nie są automatycznie wspólnymi dowodami o tej samej granularności. Wszystkie różnice istotne dla przyszłego scalania zapisano w
application/config/KANDYDACI_SCALEN_AT_DG_ETAP_04.json, ze stanem approved_to_merge=false.

## 2. Dokładne porównanie fragmentów matematycznych

### Grupy pi_n, przemienność i grupy względne

Oba rozdziały definiują pi_n(X,x_0) za pomocą odwzorowań sfer z punktem bazowym i równoważnego modelu kostkowego, dowodzą abelowości dla n>=2 przez argument Eckmanna–Hiltona, a następnie wprowadzają pi_n(X,A,x_0) i długi ciąg homotopii pary. W porównaniu weryfikowano rozdzielenie: pi_1(X,A) jest zbiorem wyróżnionym, pi_2(X,A) może być nieprzemienna w ogólności, pi_n(X,A) dla n>=3 jest abelowa. Warunki spójności i bazy są niezbędne dla poprawnego zastosowania lematu pięciu w późniejszych dowodach.

### Przybliżenie komórkowe i modele CW

Dowody używają względnego HEP, lokalności zwartego obrazu w CW i komórkowego przesuwania map z dysków i sfer. DG-09 jawniej uzasadnia, jak dobiera się regularne punkty, rozciąga radialnie wybrane małe dyski i rozcina dopełnienie dysku na sumę generatorów względnej pi_n. Te konstrukcje muszą zostać zachowane w kanonicznym wspólnym dowodzie. AT-06 zawiera zgodne sformułowania w bardziej skróconej postaci.

### Hurewicz w stopniu pierwszym — poprawka AT-06

Twierdzenie thm:hurewicz-h1 identyfikuje abelianizację pi_1(X) z H_1(X;Z). W AT-06 brakowało jawnej realizacji trójkąta uzasadniającego zgodność konkatenacji pętli z dodawaniem singularnych łańcuchów. Wprowadzono dla dróg alpha i beta konkretny singularny sympleks
T_(alpha,beta)=(alpha*beta)∘q, q(t0,t1,t2)=t1/2+t2,
którego brzeg jest beta-(alpha*beta)+alpha. Sprawdzono wartości q na trzech bokach, zachowując znak operatora brzegowego. Na końcu dopisano dowód naturalności h_1 dla dowolnego opartego odwzorowania, w tym przejście na abelianizacje.

DG-09 dodatkowo rozpisuje dokładnie rachunek odwrotności: pomocnicze drogi u_x nie są oddzielnymi cyklami, lecz ich współczynniki znoszą się dla całego cyklu z=Σm_sigma sigma dzięki warunkowi dz=0. Ta część jest cennym uzupełnieniem przy późniejszym bezstratnym scalaniu.

### Whitehead — zakres i dowód

Obie wersje thm:whitehead dotyczą konkretnego odwzorowania CW f:X→Y indukującego bijekcję na pi_0 i izomorfizmy na wszystkich pi_n w każdej bazie. Nie wystarczy istnienie abstrakcyjnych izomorfizmów grup; ważna jest naturalność względem jednego f. Wersja DG szczegółowiej rozpisuje:
- rozpatrzenie pi_1(Y,X) jako zbioru wyróżnionego, a nie grupy abelowej;
- ściskanie komórek względem podkompleksu i nieruchomego brzegu dysku;
- ciągłość przy nieskończenie wielu etapach, za pomocą słabej topologii CW;
- właściwą strukturę CW cylindra odwzorowania i cztery złożenia sprawdzające odwrotność.

Nie utożsamiono tych fragmentów z powtarzającymi się linijkami tekstu; trzeba zachować pełną kontrolę konstrukcyjną w kanonicznym wariancie.

### Względne twierdzenie Hurewicza — poprawka AT-06

W dowodzie thm:hurewicz-wzgledny AT-06 wcześniej przechodziło za szybko do modelu pary (Z,A), bez wykazania jednospójności X i dokładnego uzasadnienia stopnia drugiego. Dla n>=2, A jednospójnej i pary (n−1)-spójnej dopisano:
- pi_0 i względna pi_1 zapewniają łukową spójność X, a z ciągu pi_1(A)→pi_1(X)→pi_1(X,A) i pi_1(A)=0 wynika pi_1(X)=0;
- stopień i>=3 można traktować przez odpowiednie diagramy abelowych grup i lemat pięciu;
- w stopniu 2 grupa względna ma teraz jawne postaci pi_2(Z,A)=pi_2(Z)/im(pi_2(A)→pi_2(Z)), analogicznie po stronie X, bo pi_1(A)=0;
- gdy F identyfikuje pi_2(Z) z pi_2(X) i jest identycznością na A, te ilorazy są izomorficzne;
- stopień 1 należy rozpatrzyć osobno, a homologiczne grupy względne porównać zwykłym lematem pięciu.

Hipoteza jednospójności A nie jest dekoracją: bez niej pojawia się działanie pi_1(A) na wyższych grupach i nie wolno bez dodatkowej analizy zastosować podanego izomorfizmu całych grup względnych.

### Absolutne twierdzenie Hurewicza i model bez niskich komórek

Dla (n−1)-spójnego X i n>=2 obie wersje budują homotopijnie równoważny kompleks bez komórek wymiarów 1,...,n−1, a następnie utożsamiają najniższą niezerową pi_n z H_n poprzez odpowiednie ilorazy wolnej grupy na n-komórkach. DG-09 dodatkowo jawnie tłumaczy użycie pierwszego twierdzenia o izomorfizmie grup przy zabijaniu jądra i stabilizację dla nieskończenie wielu etapów. Te szczegóły są źródłową, unikalną treścią argumentu.

### Przykłady wymagające zachowania

AT-06 ma unikalny przykład abelianizacji grupy butelki Kleina z relacją aba⁻¹b=1, skąd pi_1(K)_ab≈Z⊕Z/2, oraz przykład dwóch trójkomórek dołączonych do S² stopniami 2 i 3: d_3=(2,3), H_2=0, H_3≈Z z klasą (3,-2), pi_3≈Z i X≃S³. Obliczenie ma osobny rysunek z jądrem i obrazem macierzy.

DG-09 rozwija analogiczne zjawisko i dodał ogólny nowy przykład z dwiema 3-komórkami o stopniach a,b, nie jednocześnie zerowych:
- d=gcd(|a|,|b|)>0;
- H_2(X_{a,b};Z)=Z/d;
- H_3(X_{a,b};Z)=Z(b/d,-a/d);
- pi_2(X_{a,b})≈Z/d, bo przestrzeń jest jednospójna;
- dla d=1 przestrzeń jest 2-spójna, pi_3≈Z i X≃S³ na podstawie homologicznego kryterium Whiteheada;
- dla a=4, b=6 grupa pi_2≈Z/2, a H_3≈Z z generatorem (3,-2), więc nie wolno wnioskować pi_3≈Z z H_3 przez zastosowanie Hurewicza bez wymaganego zerowania pi_2.

Dowód używa równości au+bv=0, skrócenia przez d i tożsamości Bézouta, aby wykazać, że wszystkie rozwiązania całkowite są t(b/d,-a/d). Przykład pokazuje bardzo konkretną granicę stosowalności twierdzenia.

Uzupełnienia DG-09: bardziej rozpisana analiza kompleksu Moore'a, podnoszenie bazy i rachunek sumowania współczynników w pi_2(S¹∨S²)→H_2(S¹∨S²). Odrębny przykład AT butelki Kleina oraz rysunek syzygii 2/3 mają zostać zachowane bez kopiowania tylko na podstawie zgodności tematu.

## 3. Testy i niezależna kompilacja

Zmieniono rzeczywiste źródła AT-06 i DG-09 oraz dodano:
- application/config/KANDYDACI_SCALEN_AT_DG_ETAP_04.json;
- application/tests/test_at_dg_pairwise_06_09.py — osiem regresji, w tym sprawdzenie liczbowych par (a,b) z zakresu [-8,8]²\{(0,0)}, pierwotności generatora jądra, wartości operatora q na wierzchołkach Δ², jawnych danych n=2, historii etykiet i bilansu otoczeń TeX;
- .github/workflows/paired-at-dg-higher-homotopy-hurewicz-audit.yml — trzy przebiegi kompilacji AT01–30 i DG01–10 w osobnych zadaniach, osobna walidacja kodu i stabilności odsyłaczy.

Pojedyncze kontrole AT05/06 i walidator aplikacji po poprawkach także wykazały SUCCESS.

**Końcowa walidacja wykonana**, GitHub Actions run:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44836409596.
Obydwa zadania są ukończone ze statusem SUCCESS:
- matematyczne regresje 8/8 OK, w tym sprawdzenie 288 niezerowych par liczb całkowitych a,b w przedziale [-8,8];
- kompletne AT-01–30 z oryginalnych źródeł: **296 stron A4**, trzy przebiegi pdflatex, brak niestabilnych etykiet, niezdefiniowanych odsyłaczy i poziomych przepełnień;
- kontrolny podtom DG-01–10: **271 stron A4**, trzy przebiegi pdflatex, brak niestabilnych etykiet i poziomych przepełnień; cztery jawnie dopuszczone odsyłacze do dalszych rozdziałów (sec:kolnierz-15, sec:uchwyt-morse-17, thm:holonomia-lokalny-produkt, thm:poincare-hopf-16).

Pobrano oba rzeczywiste PDF z artefaktów tego przebiegu GitHub Actions.
Zrenderowano i wizualnie sprawdzono m.in. strony AT 74–76, 78–81 oraz DG 246–247;
w nowym przykładzie DG wzory na gcd, całkowite jądro i dwa przypadki spójności
są czytelne i prawidłowo złamane na stronie. W nowych fragmentach nie widać
obciętych formuł, nałożeń ani przesuniętych podpisów.
Oględziny wskazanych stron nie są deklaracją manualnego obejrzenia wszystkich 567 stron obu dokumentów.

## 4. Decyzja i dalsza kolejność

**Fizyczne scalanie odłożone.** Zachowano wszystkie 45 i 43 oryginalne nazwy etykiet, a nowe przykłady mają nowe, osobne identyfikatory. Nie ustanowiono kanonicznego właściciela dla żadnej z 42 nazwy powielonych między tomami.

Następna iteracja ma sprawdzić rzeczywisty katalog dalszych nakładek (np. AT-11 z DG-17, AT-18 z DG-18), bez arbitralnego utożsamiania numerów rozdziałów. W szczególności nie wolno powtarzać ukończonych AT-03/04/05/06/09 bez nowej przesłanki matematycznej.
