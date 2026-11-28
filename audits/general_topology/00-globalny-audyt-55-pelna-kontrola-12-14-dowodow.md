# Topologia ogólna — globalny audyt 55: pełna niezależna kontrola 14 dowodów rozdziału 12

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Źródło:** `chapters/pl/general_topology/12-przestrzenie-jednostajne.tex`; blob `13597073db07742089b82ae3fc9878733dea5e88`; 662 wiersze.

## Zakres

Przeczytano wszystkie 14 środowisk `proof` wraz z twierdzeniami i hipotezami; niezależnie sprawdzono składanie i odwracanie relacji, przypadki graniczne pustych zbiorów, przechodzenie od przekrojów do otwartych otoczeń, produkty oraz definicje filtrów i sieci Cauchy'ego. Zgodność statycznych etykiet z aktualnym źródłem podlega odrębnemu odczytowi po zapisie. Ta kontrola nie jest formalizacją Lean i nie zastępuje CI ani sprawdzenia PDF.

## Macierz wszystkich 14 dowodów

| ID | Etykieta; początek proof (wiersz) | Niezależna weryfikacja |
|---|---|---|
| 12-01 | `lem:topog-jednostajne-symetryczne`, 62 | Z V∘V⊂E i F=V∩V⁻¹∩E∩E⁻¹ otrzymujemy F symetryczne, należące do struktury i F∘F⊂E. Poprawne także dla X=∅. |
| 12-02 | `thm:topog-jednostajne-topologia`, 100 | Kluczowy niejawny warunek: przekrój E[x] nie musi być otwarty. W dowodzie skonstruowano otwarty W={y:∃D∈𝒰, D[y]⊂E[x]}; dla y∈W, F∘F⊂D i z∈F[y] dają F[z]⊂E[x], więc z∈W. Zatem x∈W⊂E[x], a przekroje są bazą otoczeń. Aksjomaty topologii wynikają z filtrowania przecięć. |
| 12-03 | `thm:topog-jednostajne-hausdorff`, 146 | Rozdzielenie topologiczne wyklucza każdą parę (x,y), x≠y, z pewnego E. Odwrotnie z (x,y)∉E i F=F⁻¹ oraz F∘F⊂E wynika F[x]∩F[y]=∅. Ponieważ przekroje są otoczeniami, zawierają rozłączne otwarte otoczenia. Nie utożsamia się przekroju z otwartym zbiorem. |
| 12-04 | `cor:topog-jednostajne-skrajne-topologie`, 175 | U_ind={X×X} wyznacza wyłącznie otwarte ∅ i X; U_dysk zawiera Δ_X, więc singletonowe otoczenia dają wszystkie zbiory otwarte. Przy |X|≤1 topologia antydyskretna i dyskretna są identyczne: nazwa «niedyskretna» oznacza w tekście typ struktury, a nie formalne zaprzeczenie dyskretności. |
| 12-05 | `thm:topog-jednostajne-pseudometryka`, 202 | Relacje E_ε są symetryczne, zawierają przekątną, a E_{ε/2}∘E_{ε/2}⊂E_ε. Nadrodzina tych relacji jest strukturą jednostajną, jej przekroje są kulami p i indukują τ_p. Przecięcie wszystkich E_ε to p⁻¹({0}), zatem warunek rozdzielania jest równoważny metryczności p. |
| 12-06 | `thm:topog-jednostajne-podprzestrzen`, 285 | Relacje E∩A² zachowują wszystkie aksjomaty; (F∩A²)∘(F∩A²)⊂E∩A², jeśli F∘F⊂E. Przekroje E[a]∩A są bazą otoczeń względnych; puste A otrzymuje jedyną strukturę jednostajną. |
| 12-07 | `thm:topog-jednostajne-iloczyn`, 323 | W produkcie ograniczenia dotyczą wyłącznie skończenie wielu współrzędnych: dla przecięć bierze się sumę nośników, dla złożenia jednocześnie H_i z H_i²⊂E_i. Przekroje relacji bazowych i otwarte cylindry produktu są wzajemnie współkońcowe w bazach otoczeń. Rzutowania są jednostajnie ciągłe. Puste produkty nie wymagają punktu bazowego. |
| 12-08 | `thm:topog-jednostajne-ciaglosc-wlasnosci`, 398 | Dla V[f(x)]⊂O jednostajna ciągłość daje E[x] z f(E[x])⊂V[f(x)]; E[x] jest otoczeniem, więc f jest ciągłe. Kompozycja f,g kolejno sprowadza relację na Z do relacji na Y, następnie do relacji na X — kwantyfikatory poprawne. |
| 12-09 | `lem:topog-jednostajne-zwarta-ciagowa`, 436 | Zstępujące niepuste domknięcia F_N ogonów ciągu mają FIP i wspólny punkt x przez zwartość K. Z x∈F_{n_{k-1}+1} wybiera się n_k>n_{k-1}, d(x_{n_k},x)<1/k. Nie używa się zwartości kul w K ani pierwszego aksjomatu przeliczalności dowolnej przestrzeni. |
| 12-10 | `thm:topog-jednostajne-heine-cantor`, 471 | Negacja jednostajnej ciągłości daje pary x_n,y_n o d(x_n,y_n)<1/n i odległości obrazów ≥ε₀. Zwartość metryczna dostarcza x_{n_k}→x, więc y_{n_k}→x, a ciągłość f powoduje e(f(x_{n_k}),f(y_{n_k}))→0. To sprzeczność; pusta K spełnia twierdzenie pusto. |
| 12-11 | `thm:topog-jednostajne-ogony`, 524 | Ogony są niepuste i tworzą bazę filtra, ponieważ D jest skierowany. Sieć Cauchy'ego daje ogon A_{α₀}×A_{α₀}⊂E; gdy filtr ogonów jest Cauchy'ego, zawiera A z A×A⊂E, a A zawiera pewien ogon. Równoważność nie zakłada metryzowalności. |
| 12-12 | `thm:topog-jednostajne-zbiezna-cauchy`, 549 | Dla E wybiera się symetryczne F z F∘F⊂E. Ze zbieżności x_α→x mamy x_α∈F[x] w ogonie. Symetria zapewnia właściwą orientację (x_α,x),(x,x_β)∈F, skąd (x_α,x_β)∈E; Hausdorffowość zbędna. |
| 12-13 | `prop:topog-jednostajne-f-cauchy`, 572 | Dla docelowego V jednostajna ciągłość dostarcza E z (f×f)(E)⊂V. Od pewnego indeksu wszystkie pary sieci należą do E; ich obrazy do V. Sama ciągłość punktowa nie wystarczyłaby. |
| 12-14 | `thm:topog-jednostajne-produkt-cauchy`, 591 | Zbieżność Cauchy'ego produktu daje warunek dla każdej współrzędnej przez jednostajną ciągłość rzutowań. Odwrotnie skończony nośnik F relacji produktu daje skończenie wiele progów α_i i wspólny górny indeks dzięki skierowaniu. F=∅ automatycznie. |

## Weryfikacja ryzyk i wynik

1. **Nie-Hausdorffowość:** żaden dowód istnienia struktury jednostajnej, ciągłości jednostajnej ani Cauchy'ego nie zakłada skrycie jednoznaczności granicy. Warunek rozdzielania jest osobno scharakteryzowany.
2. **Otoczenia vs zbiory otwarte:** `E[x]` jest otoczeniem, niekoniecznie zbiorem otwartym. Konstrukcja `W` w dowodzie topologii jest niezbędna i poprawna.
3. **Nazwa struktury skrajnej:** słowo „niedyskretna” oznacza strukturę `{X×X}`; w przestrzeni pustej albo jednoelementowej topologia ta jest jednocześnie dyskretna. Przejście przy przyszłym audycie terminologii na „antydyskretna” byłoby mniej dwuznaczne, ale nie zmienia matematycznej treści dowodu.
4. **Rozmiar nośnika:** iloczynowe warunki Cauchy'ego sprawdzają wyłącznie skończenie wiele współrzędnych, jak wymaga topologia i struktura produktu.

**Werdykt: 14/14 PASS.** Nie znaleziono błędów matematycznych wymagających korekty LaTeX; źródło pozostało bez zmian. Wraz z poprzednim raportem 54 bilans indywidualnej pełnej dokumentacji rośnie z **258 do 272/325**. Do ujednolicenia pozostaje **53** dowodów: rozdział 13 (9) i 24–26 (44). Zielony CI tego raportu należy potwierdzić dopiero po faktycznym zakończeniu workflow; automatyzacja pozostaje aktywna.
