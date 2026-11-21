# Topologia algebraiczna — TOP-18, audyty stabilizacyjne I–V

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`. Nie tworzono nowej gałęzi; `main` pozostawiono bez zmian.  
**Rozdział:** `chapters/pl/algebraic_topology/18-homologia-morse-a-od-punktow-krytycznych-do-homologii-singular.tex`.  
**Aktualna zawartość:** blob `ffb0646a80ed00c583f887262522827d514aab9b`, 683 wiersze, 13 unikalnych etykiet.
**Zasada audytu:** wielokrotna kontrola obecnego materiału bez wprowadzania nowych twierdzeń lub lematów. Weryfikacja hipotez, dowodów, orientacji trajektorii, przykładów, języka, LaTeX, rysunków, referencji, regresji i CI.

## Audyt I — pełna lektura, brakujące kwantyfikatory i kompaktyfikacja

Rozdział został odczytany w całości wraz z raportem `TOP_17_18_ITERACJA_19_2026-11-21.md`. Sprawdzono: gładki lemat Morse'a w postaci blokowej (Schur i dodatnie pierwiastki macierzowe), izolowanie punktów krytycznych, zupełny przepływ ujemnego gradientu, rozmaitości stabilne i niestabilne, przekrój trajektorii na poziomie regularnym, orientacje, kompaktyfikację przestrzeni trajektorii, `∂²=0`, uchwyty, wiele punktów krytycznych na tym samym poziomie, porównanie Morse–CW–singular, kontynuację, nierówności Morse'a, a także wszystkie cztery przykłady.

W twierdzeniu kompaktyfikacyjnym wcześniej występowały niewprowadzone w hipotezach symbole p,q,r. Dodano jawne kwantyfikatory `p,q,r∈Crit(f)` i orientacje rozmaitości niestabilnych. Dowód uzupełniono o ścisły rachunek: z niepustości `M(a,b)` i transwersalności wynika `λ(a)−λ(b)−1≥0`; każdy odcinek łamanej trajektorii zmniejsza indeks przynajmniej o jeden. Gdy całkowity spadek indeksu wynosi jeden, łamanie jest niemożliwe, a przy spadku dwa składa się dokładnie z dwóch odcinków o spadku jeden. Nadal **nie** przypisuje się samemu oszacowaniu energii pełnego analitycznego dowodu sklejania.

W twierdzeniu o silnych nierównościach Morse'a zdefiniowano jawnie wymiar `n≥0` występujący w sumach. Doprecyzowano sformułowanie naturalności względem odwzorowań kontynuacji: ich zgodność z identyfikacjami przez CW wymaga znanej wersji porównania, a nie samej równości grup homologii.

**Commit:** `59f74ed2f86dd948edb6bef39ce318c0d06740af`.

## Audyt II — indeksy skrajne, modele uchwytów i rachunki

Sprawdzono skrajne indeksy w twierdzeniu o doczepianiu uchwytu: dla k=0 wyrażenie `S^{k−1}` wymaga konwencji `S^{-1}=∅`, `D^0={*}`; dołącza się nową składową. Dla k=n dołącza się n-wymiarowy dysk. Uzupełniono dowód, nie zmieniając twierdzenia.

Doprecyzowano, że w przykładzie sfery S¹ liczenie dwóch trajektorii o przeciwnych znakach opisuje standardową metrykę. Zrewidowano związek incydencji Morse’a z komórkową: w tekście przytaczany jest konieczny wynik geometryczny o zgodności znaków, a nie tylko utożsamienie rang grup.

Wprowadzono niezależne regresje:
- Rachunek orientacji na RP² dla 117 regularnych wartości poziomu, dla trzech wyborów uporządkowanych wartości własnych. Dwa przecięcia każdego poziomu ze stabilną rozmaitością p₁ dają **oba znak −1**, zgodnie z `n(p₂,p₁)=−2` przy przyjętej orientacji.
- Sprawdzenie rozróżnienia możliwych pośrednich indeksów dla łącznego spadku 1 i 2.
- Weryfikacja wielomianowej postaci nierówności Morse'a w trzech konkretnych kompleksach: funkcji wysokości na S², przykładzie RP² (różniczka 2) i okręgu z dwiema parami ekstremów.

**Commity:** `3deadfba90d5306659ee86b65a1a3ca368786dfd`, `832cad4cc39e27a4f38fc6c63b487036b817bff0`.

## Audyt III — samodzielność definicji kompleksu i orientacji

W definicji `CM_k(f,g)` zapisano wprost konieczny wybór orientacji wszystkich `W^u(p)` przed użyciem znaku `ε(γ)`. Doprecyzowano kwantyfikator `k∈Z` i konwencję zerowej grupy dla indeksów niewystępujących. W twierdzeniu `∂²=0` wskazano, że obowiązuje dla **dowolnego** takiego układu orientacji. Zaznaczono też ich wybór we wstępie do twierdzenia o kompaktyfikacji.

**Commit:** `779b5e11ee3f2a93bda27320ff758f956e5e8121`.

## Audyt IV — niezależna kontrola struktury i pełnego materiału

Ponownie pobrano aktualny plik, po wszystkich poprawkach, i niezależnie sprawdzono:
- 683 wiersze, **13 historycznych unikalnych etykiet**; 6 poprawnie domkniętych odsyłaczy.
- **Dwa oryginalne diagramy TikZ** zachowane.
- Prawidłowo zagnieżdżone wszystkie środowiska LaTeX, brak niedomkniętych referencji.
- Brak niedozwolonej terminologii („mapa” jako odwzorowanie, „sekwencja”, „tensorowanie”, „injekcja”, „unia”) i roboczych komentarzy iteracyjnych.
- Przedstawione zewnętrzne zależności pozostają jawne: teoria rozmaitości stabilnych, kompaktyfikacja i sklejanie z orientacjami, twierdzenie o uchwytach, porównanie incydencji Morse–CW i parametryczna kontynuacja.
- Przykład RP² zachowuje dokładnie trzy punkty krytyczne, dwa przecięcia o zgodnych znakach i różniczki `∂₂=2`, `∂₁=0`, stąd `HM₁=Z/2Z`.
- Kontrolę algebraicznej części nierówności wykonano na kilku kompleksach i porównano z `m(t)-b(t)=(1+t)Q(t)`.

## Audyt V — testy ochronne, ponowne otwarcie źródła

Dodano regresję testującą samodzielność definicji `CM_k`, wymienienie orientacji `W^u(p)`, poprawny zakres k, brak terminologii potocznej i komentarzy iteracyjnych. Kolejna ponowna kontrola całego źródła nie wykazała potrzeby dalszej zmiany treści. W `application/tests/test_topology_chapters_17_18.py` jest 18 metod testowych (wspólnych dla TOP-17 i TOP-18).

**Commit testów:** `c75d06189cc5c70f7fff4f6d6582a3c54ea8d75e`.

## Weryfikacja CI

Dla commita `832cad4c`:
- [Kompilacja TOP-01–18](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932861013) — **success**.
- [Testy aplikacji i regresji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932861024) — **success**.

Dla późniejszego commita źródła `779b5e11`:
- [Zależności AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932926473) — **success**.

**Końcowa weryfikacja najnowszej wersji:**
- [Kompilacja TOP-01–18, dwa przebiegi LaTeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44933012278) — **completed / success**, commit `c75d0618`.
- [Testy aplikacji i wszystkie regresje po ostatniej poprawce](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44933012261) — **completed / success**, commit `c75d0618`.
- [Kontrola zależności AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932926473) — **completed / success**, commit `779b5e11` (ostatni commit **źródła** TOP-18).
- [Specjalny audyt TOP-18 ↔ DG-18: porównanie dowodów, kontrola zależności i kompilacje obu skryptów](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932926474) — **completed / success** w obu zadaniach; pełny kontekst AT-01–30 i DG-01–20 skompilowany. Commit `779b5e11` (aktualne źródło).
- W niezależnej symulacji arytmetycznej: **117 poziomów regularnych**, **234 sprawdzenia znaków przecięć**, **3 przykłady wielomianowych nierówności Morse'a**; brak niezgodności.

**Decyzja końcowa:** **TOP-18 STABILNY PO AUDYCIE V.** Pięć audytów, ostatnia kontrola matematyczna i strukturalna czysta, zachowane 13 etykiet i dwa diagramy, wszystkie kontrole CI zakończone sukcesem. Nie dodano nowych twierdzeń ani lematów. Następny rozdział w cyklu: **TOP-19**. Nie włączono automatyzacji.
