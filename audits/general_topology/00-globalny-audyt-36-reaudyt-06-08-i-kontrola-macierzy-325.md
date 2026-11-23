# Topologia ogólna — audyt globalny 36: niezależna kontrola aktualnych 06 i 08, weryfikacja macierzy 325/325

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródłowy punkt odniesienia:** commit `c75d73d091d7967487c221724cb76db3c1bc288e` (26 źródeł niezmienionych względem wspólnego wydania z audytu 31).
**Cel:** rozstrzygnąć faktyczną zmianę bloba dla rozdziałów 06 i 08 po historycznej stabilizacji i wykonać selektywną, nową kontrolę matematyczną trudnych argumentów. Dodatkowo w sposób niezależny ponownie odczytać trzy pełne nowe macierze 33–35 i sprawdzić kompletność identyfikatorów.

## 1. Rzeczywiste źródło różnic kryptograficznych

Suma SHA-256, którą raport lokalny umieszcza przy źródle, jest kryptograficzną sumą **bajtów pliku**, a SHA bloba Git jest innym identyfikatorem opartym na obiekcie Git. Nie można porównywać ich ze sobą bez przeliczenia.

Dla rozdziałów 01–10 przeprowadzono **rzeczywiste przeliczenie SHA-256 bieżącej treści UTF-8**, a następnie porównanie do wartości historycznych:

| Rozdziały | Wynik i znaczenie |
|---|---|
| **01, 02, 05, 07, 09, 10** | Bieżące SHA-256 są **dokładnie takie same**, jak podane przez ostatni lokalny audyt stabilizacyjny. |
| **03** | SHA-256 różny; istnieje późniejszy niezależny audyt globalny 17 wszystkich 15 dowodów na aktualnym blobie `b571753b5ab9a8777424fc32f6c4a54a4048af77` i kontrola PDF. |
| **04** | SHA-256 różny; późniejsze audyty 12–13 badały aktualny blob `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` (17 dowodów), a audyt 14 sprawdził finalny PDF. |
| **06** | SHA-256 historyczny `f93d19b39fd4cbdf0ee2db32cdd1bfc6b183ea5d46baf31e986b0f93af93eeae`; bieżący `835da9fca2d2929f50824d0d373aaf3869a54741f0201bd8c5d72fce15a6f687`; obecny blob Git `365204000d0d5b21f213132e58b71aa48db3910e`. |
| **08** | SHA-256 historyczny `aaa328d2bb0f9410128f108722eb9f7502cca5bc385ff3d5df86424818c96f31`; bieżący `574dac643783fbf03e4d9a23fb822e55be2ecb223564320fbd44ab67aaee6c49`; obecny blob Git `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1`. |

Z GitHub API pobrano listę commitów zmieniających `06-zbieznosc-topologiczna.tex` oraz `08-spojnosc.tex` i następnie **patch całego commitu** `5461638e212bb0efcb60e7cf136fea65bae84b8f` („docs(topology): enforce first/second countability axiom terminology across scripts”).

- W **06** patch wymienia 17 dodanych / 14 usuniętych wierszy; wszystkie zmiany to stylistyka i sformułowania „spełnia pierwszy aksjomat przeliczalności” w celu rozdziału, definicji, hipotezach, przykładzie, podsumowaniu i tytułach. **Znaczenie hipotez jest równoważne poprzedniemu. Żaden krok dowodu matematycznego nie został dodany ani usunięty.**
- W **08** patch wymienia 3 dodane / 2 usunięte wiersze w przykładzie krzywej sinusowej topologa; zastąpiono odwołanie do „przestrzeni pierwszo przeliczalnej” zdaniem, że przestrzeń metryczna spełnia pierwszy aksjomat przeliczalności. To ta sama implikacja i ten sam dowód.

**Wniosek:** starsze raporty nie dotyczą dokładnie obecnych bajtów; ale to **korekta terminologiczna**, a nie aktualnie niedowiedzione nowe twierdzenie. Aby uniknąć przeniesienia statusu jedynie po nazwie pliku, dokonano ponownego niezależnego odczytu poniższych argumentów.

## 2. Nowa kontrola trudniejszych dowodów w aktualnym rozdziale 06

1. **`thm:topog-pierwsza-przeliczalnosc-domkniecie`:** z przeliczalnej bazy `B_n` budujemy malejącą `W_n=∩_{k≤n}B_k`; przy `x∈cl(A)` każdy `A∩W_n` jest niepusty i wybór `a_n` daje zbieżność. Żadne ukryte wymaganie T1 nie występuje.
2. **`thm:topog-ciagowe-kryterium-ciaglosci`:** zanegowanie ciągłości w x dostarcza otwartego V wokół f(x), a z malejącej bazy W_n wybiera się punkty `x_n∈W_n\setminus f^{-1}(V)`. Zbieżność x_n→x przeczy zbieżności obrazów, co wykazuje właściwy kierunek implikacji.
3. **`thm:topog-siec-domkniecie`:** indeksy `(U,a)` spełniają relację skierowania „później = mniejszy U”, dzięki czemu nie wymaga się jednoczesnego wyboru punktów z nieskończenie wielu otoczeń. Argument działa także bez metryzowalności.
4. **`thm:topog-sieci-hausdorff`:** w nie-Hausdorffowej przestrzeni indeksujemy wszystkie trójki `(U,V,z)` z `z∈U∩V`. Zmniejszanie obu otoczeń daje dwie granice. Warunek skierowania uzyskuje się przez przecięcie otoczeń i wybór jednego świadka, a nie przez nieuprawnioną współkońcowość.
5. **`thm:topog-punkt-skupienia-podsiec`:** indeksy `E={(d,U):x_d∈U}` uporządkowane wzrostem d i malejącym U są skierowane dokładnie dzięki warunkowi punktu skupienia. Projekcja `φ(d,U)=d` jest ostatecznie współkońcowa w znaczeniu przyjętej definicji podsieci, a otrzymana podsieć zbiega do x. Nie potrzeba monotonicznego wybranego `φ` poza takim kryterium.
6. **`thm:topog-siec-iloczyn`:** dla skończonego zestawu ograniczonych współrzędnych istnieje wspólna górna granica indeksów. Dla `F=∅` wystarcza dowolny indeks skierowanej niepustej rodziny.
7. **`def:topog-filtr`, nazwane uzasadnienie bazy filtra:** ten osobny `proof` rzeczywiście uzasadnia bazę właściwego filtru; nie jest drugim dowodem poprzedniego twierdzenia o iloczynie. Macierz 33 wiąże go z definicją poprawnie.
8. **`thm:topog-filtr-domkniecie` i `thm:topog-sieci-filtry`:** bazę tworzą niepuste przecięcia A∩U oraz odpowiednio wszystkie pary `(F,a)`. Krytyczny kierunek: zbieżność sieci `x_{(F,a)}` oznacza, że dla *każdego* b∈F indeks (F,b) jest późniejszy niż (F,a), więc `F⊆U` i `U∈𝔽`; nie wolno wnioskować jedynie z jednego punktu.
9. **`cor:topog-filtr-ciaglosc-hausdorff`:** `V∈f_*𝔽 ⇔ f^{-1}(V)∈𝔽`; brak niejawnej zamiany obrazu na przeciwobraz. Własność Hausdorffa odpowiada jednoznaczności granic filtrów przez wykorzystanie sieci ogonów.

**Werdykt bieżącej ponownej kontroli wybranych trudnych argumentów 06: PASS**, bez zmiany źródła.

## 3. Nowa kontrola argumentów rozdziału 08

1. **`thm:topog-spojnosc-przedzialy`:** argument kresu górnego dla domkniętego i otwartego rozdzielenia odcinka, z rozróżnieniem pustego i jednopunktowego odcinka, jest spójny; dla zbioru niebędącego przedziałem liczba c pomiędzy a,b daje rozdzielenie.
2. **`thm:topog-spojnosc-iloczyn`:** dla niepustego produktu wybór **jednego** p umożliwia skonstruowanie gęstej sumy spójnych skończeniewspółrzędnych podprzestrzeni `Y_J` z p jako wspólnym punktem. Gęstość przez cylindry bazowe, bez wybierania niezależnie nowego punktu z wszystkich czynników; dla produktu pustego twierdzenie zachodzi z definicji.
3. **`thm:topog-spojnosc-skladowe`:** suma wszystkich spójnych podzbiorów zawierających x jest spójna; jej domknięcie także, a maksymalność wymusza domkniętość składowej. Dwie składowe o niepustej części wspólnej są równe.
4. **`lem:topog-spojnosc-skladanie-drog`:** sklejanie na dwóch domkniętych półodcinkach i równość wartości przy 1/2 zapewniają ciągłość wynikowej drogi; odwrócenie parametru zachowuje ciągłość.
5. **`thm:topog-spojnosc-lokalna-komponenty` i `cor:topog-spojnosc-lokalna-drogowa`:** lokalna spójność zapewnia otwarte spójne otoczenia w danym otwartym U, a maksymalność składowych wymusza ich otwartość. W wersji drogowej złożenie dwóch dróg przez wspólny punkt daje argument analogiczny. Otwarte składowe drogowe są także domknięte dzięki otwartości pozostałych składowych; nie trzeba wcześniej założyć domkniętości składowych drogowych.
6. **`ex:topog-spojnosc-cantor`:** przedziały odpowiadające różnym prefiksom ternarnym są rozłączne i oddzielone dodatnimi odstępami, co daje względnie otwarto-domknięte cylindry i całkowitą niespójność. Z `C=∩K_n` i zwartym [0,1] wynika zwartość Cantora.
7. **`ex:topog-spojnosc-sinus`:** w nowym sformułowaniu odwołanie do rozdziału 06 jest prawidłowe. Wykazanie `T=cl(G)` korzysta z ciągłości sin(1/x) przy x>0 i ciągów `x_n=1/(θ+2πn)` dla odcinka pionowego. W argumentacji przeciw istnieniu drogi od pionowego odcinka do G użyto *ostatniego* czasu `t_0` zerowania współrzędnej poziomej. W każdym przedziale `(t_0,t_0+δ]` własność wartości pośredniej wymusza wartości sin(1/u)=1 i −1; przeczy to ciągłości drugiej współrzędnej przy `t_0`. Założenie metryzowalności zostało użyte tylko do charakterystyki punktu domknięcia przez ciągi.

**Werdykt bieżącej ponownej kontroli wybranych trudnych argumentów i zmienionego akapitu 08: PASS**, bez zmiany źródła.

## 4. Niezależna kontrola trzech macierzy 33–35

Po utworzeniu raportów 33, 34 i 35 **ponownie pobrano wszystkie trzy raporty z GitHuba** i z każdego policzono rzeczywiste wiersze identyfikatorów proof o wzorcu `NN-NN`.
- 33 (01–10): **144**;
- 34 (11–18): **71**;
- 35 (19–26): **110**.
- Suma: **325/325**, liczba **unikatowych ID również 325**; nie znaleziono braków ani dziur w numerowaniu 01, 02, ... w żadnym z 26 rozdziałów. Zgodność liczb na poziomie rozdziału z globalnym audytem 31: PASS.
- Tabele wiążą proof z etykietą i raportem; **nie** oznacza to, że pełny tekst dowodów został mechanicznie sformalizowany czy że każdy raport referencyjny literalnie przywołuje wszystkie etykiety. Tam, gdzie starsze raporty obejmowały pełny rozdział tylko opisowo, trzeba oddzielnie ocenić zakres ich dowodowej kontroli.

## 5. CI i warunki końcowe

Przebiegi po raportach 31 i 32 mają rzeczywiste wyniki `completed/success`:
- [45131452709](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131452709),
- [45131743114](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131743114).

Na etapie rozpoczęcia tego raportu przebiegi po raportach 33–35 były jeszcze `in_progress`; ich ostateczny wynik **należy ponownie sprawdzić**. W tej iteracji nie wykonywano nowej kompilacji lokalnej ani ponownego pełnorozdzielczego renderingu PDF.

**Rezultat:** rozbieżności 06 i 08 są wyjaśnione z rzeczywistego patcha; aktualna wersja kluczowych dowodów i przykładów przechodzi niezależny przegląd. Cały rejestr 325/325 jest kompletny i spójny. Do ogłoszenia globalnego PASS pozostają: próba obalenia szczególnie ryzykownych dowodów 01–26, konfrontacja treści dowodów z zakresem raportów (nie tylko indeksów), końcowa inspekcja wizualna wszystkich diagramów i CI finalnego HEAD. Nie wyłączać automatyzacji.
