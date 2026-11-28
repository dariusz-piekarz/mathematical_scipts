# Topologia ogólna — globalny audyt 42: niezależna kontrola 17 trudnych dowodów w rozdziałach 24–26

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Odczyt źródeł:** commit `2f15155b46f17ba0bedb1d5f9ffae2304e65efa7`.
**Bloby rozdziałów:** 24 — `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`; 25 — `7b772123870296af95d3ce951ccddb65685af7aa`; 26 — `161d04d779ae86554f81c11bb24daa842c8dd363`.

**Metoda:** odczytano w źródłach pełne stwierdzenia, odpowiednie dowody i argumenty pomocnicze. Niezależnie skontrolowano **17 określonych środowisk proof**, ze szczególnym uwzględnieniem kwantyfikatorów, brakujących założeń, przypadków granicznych i kierunków implikacji. Pozostałych 27 środowisk proof w tym bloku nie przedstawiamy jako ponownie skontrolowanych w tej iteracji. Zmian w LaTeX nie dokonywano.

## Rozdział 24 — sześć kontroli

1. **`thm:topog24-coset-hausdorff`, proof 452–485: PASS.** Domkniętość H i g=x⁻¹y∉H pozwalają dobrać V tak, że V⁻¹gV∩H=∅. Gdyby q(xV) i q(yV) się przecinały, zachodziłoby v⁻¹gw=h₁h₂⁻¹∈H. Odwrotna implikacja używa domkniętości włókna H. **Normalność H nie jest potrzebna.**
2. **`thm:topog24-normal-quotient`, 505–555: PASS.** Ciągłość działań na G/N wynika z tego, że **otwarta** surjekcja q ma produkt q×q również otwarty i ilorazowy; sam produkt dowolnych odwzorowań ilorazowych nie wystarczałby. Domkniętość N jest użyta do T1/Hausdorffowości, a normalność do działań.
3. **`thm:topog24-isomorphism`, 597–623: PASS.** Wnioskowanie, że G/ker f i H są homeomorficzne, używa wyraźnego założenia otwartości f. Ciągła bijekcja grupowa bez tego założenia nie wystarczy (R dyskretna → R zwykła).
4. **`thm:topog24-identity-component`, 765–830: PASS.** G⁰ jest podgrupą przez ciągły obraz G⁰×G⁰ przy (x,y)↦xy⁻¹ i normalną przez sprzężenia. Przeciwobraz spójnego C⊂G/G⁰ jest spójny dzięki spójności włókien i otwartości q; nasycenie obu członów hipotetycznego rozdzielenia jest jawnie uzasadnione.
5. **`thm:topog24-uniformities`, 894–951: PASS.** Dla relacji x⁻¹y∈U oraz xy⁻¹∈U konstrukcje lewego i prawego układu otoczeń spełniają składanie po symetrycznym V z V²⊂U. Odwracanie zamienia struktury, nie zakładając ich równości w grupie nieprzemiennej.
6. **`thm:topog24-birkhoff-kakutani`, 987–1159: PASS.** W kluczowej indukcji dla S=∑ρ(g_j)<2⁻ⁿ podział na przypadki S<h i h≤S<2h (h=2⁻⁽ⁿ⁺¹⁾) daje odpowiednio dwa lub trzy bloki należące do U_{n+1}. Dyskretność dodatnich wartości ρ (potęgi 2⁻ᵏ) zapewnia, że środkowy czynnik ma wagę ≤h. Z własności iloczynu (*) i ∩U_n={e} wynika dodatnia określoność metryki łańcuchowej; inkluzje U_{n+1}⊂B_d(e,2⁻ⁿ)⊂U_n dają zgodność topologii.

## Rozdział 25 — sześć kontroli

7. **`thm:topog25-nested`, 101–138: PASS.** Przecięcie zstępujących niepustych kompaktów jest niepuste. Gdyby było niespójne, normalność zwartego Hausdorffa pozwala oddzielić jego części otwartymi U,V, a pewien K_N musi być zawarty w U∪V; w przeciwnym razie zstępujące K_n\(U∪V) miałyby wspólny punkt.
8. **`lem:topog25-chain-intersection`, 149–180: PASS.** Dla dowolnego (niekoniecznie przeliczalnego) łańcucha continuów skończone przecięcie równa się jednemu członowi łańcucha. Dzięki temu ewentualne rozdzielenie wspólnego przecięcia przenosi się na jeden spójny zbiór.
9. **`thm:topog25-inverse-connected`, 341–424: PASS.** Niepustość i surjektywność rzutowań używają wyboru zależnego. Dla hipotetycznego rozdzielenia X=A∪B zbiory F_n={(a,b)∈A×B:p_n(a)=p_n(b)} są zstępującymi kompaktami. Ich wspólny punkt oznaczałby a=b, sprzeczność. Domknięcie warunków granicy używa Hausdorffowości.
10. **`thm:topog25-knaster`, 515–604: PASS.** Niepuste wnętrze właściwego podcontinuum C daje cylinder p_k⁻¹(U)⊂C. Dla dużego r iteracje T^r odwzorowują skrajne dyadyczne przedziały na cały [0,1], co wymusza [1/4,3/4]⊂p_m(C). Ponieważ T²([1/4,3/4])=[0,1], wszystkie rzuty C stają się pełne, co przeczy istnieniu otwartego cylindra w dopełnieniu C.
11. **`lem:topog25-solenoid-local`, 696–752: PASS.** Dla łuku U o parametrze J długości <1 jedyny t₀ i dwa wybory pierwiastka kwadratowego na każdym poziomie kodują punkt solenoidu. Ciągłość odwrotności wynika z lokalnego rozdzielenia gałęzi pierwiastka na każdej **skończonej** liczbie poziomów.
12. **`thm:topog25-solenoid-not-locally-connected`, 761–799: PASS.** Rzut spójnego zbioru J×{0,1}^N na całkowicie niespójny zbiór Cantora jest singletonem. Taka warstwa nie ma niepustego wnętrza; nie istnieje więc małe otwarte spójne otoczenie.

## Rozdział 26 — pięć kontroli

13. **`thm:topog26-small-paths`, 100–295: PASS.** Drobne łańcuchy w małych spójnych zbiorach C_{n,j} tworzą zgodne podziały czasu o długości maksymalnej ≤2⁻ⁿ. Oscylacja wartości na jednym przedziale jest ≤2S_n, na dwóch sąsiednich ≤4S_n. To zapewnia jednostajną ciągłość na gęstym zbiorze parametrów i przedłużenie dzięki zupełności X. Nie założono wcześniej istnienia dróg w samych zbiorach C_{n,j}.
14. **`lem:topog26-excursion`, 339–405: PASS.** Skończoność zbioru docelowego E umożliwia wybór rozłącznych przedziałów J_i także przy t_y=0 lub 1. Pętle do punktów przypisanych temu samemu t_y łączą się w h(t_y), zachowując ciągłość i oba końce; jednostajny błąd jest mniejszy niż 2ε.
15. **`thm:topog26-hm-sufficient`, 444–561: PASS.** Kolejne drogi f_n mają δ_n/2-gęste obrazy, a przyrosty o koszcie ≤2ε_n tworzą szereg zbieżny. Granica jest jednostajna i ciągła. Surjektywność nie wymaga zbieżności czasów t_n: wystarczy d(x,f(t_n))→0 oraz domkniętość zwartego obrazu f([0,1]).
16. **`lem:topog26-image-second-countable`, 592–651: PASS.** Zwarte włókna f⁻¹({x}) pozwalają objąć je skończoną sumą V elementów przeliczalnej bazy odcinka. Zbiór W_V=X\f([0,1]\V) jest otwarty dzięki Hausdorffowości X i spełnia x∈W_V⊂O.
17. **`lem:topog26-image-locally-connected`, 661–738: PASS.** Skończone obrazy przedziałów I_j zawierają x, więc ich suma K jest spójna. Otwarte W=X\f([0,1]\V) z włókna zawartego w V spełnia x∈W⊂K⊂O. Stąd składowe spójne dowolnego otwartego O są otwarte, jak wymaga lokalna spójność.

## CI, wynik i zakres

Po poprzednim cyklu 2+1 rozdziałów 06 i 21 sprawdzono rzeczywiste `completed/success` workflow [45135106888](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45135106888) (raport 40) i [45135234281](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45135234281) (raport 41). Stan CI po zapisaniu **tego** raportu wymaga ponownego sprawdzenia.

**Werdykt:** **PASS selektywnej niezależnej kontroli 17/17 wybranych dowodów**. Nie znaleziono nowej luki ani nie zmieniono źródeł matematycznych; bloby rozdziałów 24–26 są nadal takie jak w poprzednich raportach stabilizacyjnych. Łącznie zawierają 44 proof, zatem pozostałych 27 nie zaliczamy jako nowo sprawdzonych.

Otwarte: finalny audyt ryzyk w rozdziałach niewłączonych do ostatnich reaudytów, ścisła ocena zależności od zewnętrznych wyników oraz CI ostatniego HEAD. Automatyzacja pozostaje aktywna.
