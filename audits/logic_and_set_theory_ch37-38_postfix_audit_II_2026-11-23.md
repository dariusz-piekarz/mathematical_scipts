# Logika matematyczna i teoria mnogości — audyt II po korektach rozdziałów 37–38

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Weryfikowane źródła:** rozdział 37: `6c495beddc92e39b6885171e6415f0efe21d5b59`, rozdział 38: `28d73acfcc3a6db9519822df210aa66391c51628`.  
**Metoda:** odrębna kontrola kontrprzykładów, przypadków granicznych i ukrytych założeń w kolejnych wnioskowaniach; nie korzysta z wyników testów skończonych jako dowodu twierdzeń nieskończonych.

## 1. Próby zakwestionowania dowodów rozdziału 37

**1. Czy można usunąć regularność w dowodzie `V_κ ⊨ ZFC`?** Nie: przy nieograniczonym poniżej κ zbiorze rang `<κ` schemat zastępowania mógłby dać zbiór wartości spoza `V_κ`. Tekst poprawnie używa regularności dopiero po stwierdzeniu, że `|a|<κ`. Na poziomach granicznych dowód mocy `V_α` również jawnie wykorzystuje regularność, a na następczych silną graniczność. Stwierdzenie zależy od obu hipotez.

**2. Czy `κ` może być mierzalna, lecz singularna?** Założenie `cf(κ)=μ<κ` daje rozbicie κ na `μ` przedziałów mocy `<κ`. Każdy przedział jest poza ultrafiltrem z jednorodności; przecięcie `μ` dopełnień powinno należeć do miary, ale jest puste. Sprzeczność działa także dla nieprzeliczalnej `μ`, gdyż zupełność dotyczy **wszystkich** `μ<κ`, nie tylko ciągów przeliczalnych.

**3. Czy w kroku silnej graniczności potrzebne jest `λ` nieskończone?** Jeśli `λ` jest skończone, hipoteza `2^λ≥κ` jest niemożliwa dla nieprzeliczalnej κ; dowód może więc zakładać istnienie iniekcji `κ→P(λ)` tylko w realnym przypadku przeciwnym. Dla `λ=0` przecięcie pustej rodziny ma wartość κ i iniekcja w jednoelementowy zbiór również nie może istnieć. Nie wykryto luki wymagającej zmiany.

**4. Czy krok egzystencjalny Łosia wymaga wyboru ze zbioru właściwego?** Nie. Dla każdego `α∈D` minimalna ranga świadka istnieje jako liczba porządkowa; świadków tej rangi można ograniczyć do zbioru. AC wybiera ich jednocześnie tylko dla zbioru indeksów `D⊆κ`. Twierdzenie o Łosiu jest schematem dla ustalonej formuły, nie wyrażeniem „prawdy dla V” jako jednego predykatu pierwszego rzędu.

**5. Czy brak nieskończonych łańcuchów malejących wystarcza w kolapsie klasowym?** W rozważanym kontekście relacja jest zbiorolokalna, a w ZFC można dla *zbiorowej* rodziny potencjalnych poprzedników uzyskać odpowiednie minimalne elementy z zasady wyboru zależnego. Właśnie dlatego dowód osobno wykazuje zbiorolokalność relacji; nie stosuje bez uzasadnienia setowego twierdzenia Mostowskiego do dowolnej klasy właściwej.

**6. Czy `[i]` jest automatycznie równe κ?** Nie przy dowolnym nienormalnym ultrafiltrze. Tekst słusznie nie używa tej równości: do dowodu punktu krytycznego wystarcza `α<[i]<j(κ)` dla każdego `α<κ`. Późniejsza normalizacja `W` jest osobnym konstrukcyjnym twierdzeniem.

## 2. Próby zakwestionowania dowodów rozdziału 38

**1. Czy przecięcie mniej niż κ klubów może stać się ograniczone?** Dla `μ<κ` i każdego `β<κ` można zbudować ciąg `β_n` tak, że dla każdego ustalonego `ξ<μ` punkty `d_ξ(β_n)` są współkońcowe w `δ=sup_n β_n`. Regularność nieprzeliczalnej κ gwarantuje `δ<κ`, a domkniętość zapewnia `δ∈C_ξ` dla wszystkich `ξ`. Dla `μ=0` przecięcie wynosi κ. Podział na przypadki jest prawidłowy.

**2. Czy diagonalne przecięcie i lemat Fodora obejmują poziom zero?** Definicja `ξ<α` czyni warunek dla `α=0` pustym; w lemacie Fodora pomija się 0 poprzez przecięcie zbioru stacjonarnego z klubowym ogonem. Nie założono nieistniejącej wartości regresywnej `<0`.

**3. Czy zbiór liczb kardynalnych silnie nieosiągalnych może być nieograniczony i niestacjonarny?** Tak, sam fakt bycia nieograniczonym nie wystarcza do stacjonarności w ogólności; tekst **nie** wykorzystuje tego błędnego przejścia. Stacjonarność `I_κ` uzyskuje przez przynależność `I_κ` i każdego klubu do tej samej miary normalnej.

**4. Czy wewnętrzna potęga `P^M(λ)` może zakłócić dowód silnej nieosiągalności κ wewnątrz M?** Nie: hipotetyczna iniekcja `κ→P^M(λ)` należałaby do V i byłaby iniekcją w `P^V(λ)`. Byłaby sprzeczna z `2^λ<κ` obliczanym w V. Tranzytywność M oraz jego zawieranie w V są istotne i wynikają z konstrukcji w rozdziale 37.

**5. Czy z węzła na poziomie κ w `j(T)` da się wybrać oryginalnych poprzedników?** Tak, ponieważ `j(T_α)={j(s):s∈T_α}` wyłącznie dla `|T_α|<κ`, a każdy poprzednik węzła `t` na poziomie `α<κ` należy do `j(T_α)`. Nie potrzebujemy rozmiarów poziomów `j(T)` powyżej κ.

**6. Czy konstrukcja zbioru jednorodnego błędnie przecina κ wiele włókien?** Nie. W kroku `ξ` występuje dokładnie `ξ<κ` poprzednio wybranych parametrów. Z `κ`-zupełności otrzymujemy duże przecięcie. Z jednorodności ultrafiltru wynika jego nieograniczoność, więc rekurencja długości κ jest uzasadniona.

## 3. Kontrola struktury

Nowe pliki w aktualnym drzewie zachowują odpowiednio **775** i **640** wierszy, **26+26** etykiet, **18+19** odsyłaczy. Nie zmieniły się definicje ani środowiska dowodów. Wszystkie odsyłacze rozdziału 38 są realizowane w rozdziałach 37–38, a pięć zewnętrznych z rozdziału 37 było zweryfikowanych wobec rozdziałów 22, 25, 31, 35 i 36.

W odróżnieniu od weryfikacji matematycznej, [CI 45081007565](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007565) dowodzi wyłącznie prawidłowego przejścia reguł i testów repozytorium dla obu aktualnych blobów; kompilacja PDF i testy regresyjne w tym przebiegu mają status **SUCCESS**. Źródła rozdziałów są niezmienione względem audytu I.

## 4. Werdykt

- **Rozdział 37: drugi czysty audyt (2/2) po korektach językowych.**
- **Rozdział 38: drugi czysty audyt (2/2) po korektach językowych.**
- **Następny krok: niezależny audyt III potwierdzający (+1)**, po sprawdzeniu zgodności bloba, odsyłaczy, składni i rzeczywistego statusu CI. Nie przyznaje się jeszcze końcowego statusu stabilnego.

**Granice:** brak nowego audytu wzrokowego PDF, brak niezależnej kompilacji Lean; bez modyfikacji rozdziałów i bez poszerzania zatwierdzonego zakresu.
