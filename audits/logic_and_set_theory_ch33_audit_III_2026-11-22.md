# Logika matematyczna i teoria mnogości — audyt III rozdziału 33

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex`.  
**Cel:** niezależny, szczegółowy przegląd po dwóch poprzednich audytach: klauzul rekurencyjnego wymuszania, definowalności w modelu $M$, lematu prawdy, założeń twierdzeń, konstrukcji nazw dla ZFC oraz języka i składni LaTeX.

## Usterki znalezione i usunięte

### 1. Niekompletna lista parametrów lematu definiowalności

Poprzednia wersja pisała o formule
$\operatorname{Force}_\varphi(p,\vec\tau,\mathbb P)$
bez parametru określającego porządek $\leq$ na $\mathbb P$.
To **nieprecyzyjne matematycznie**: na jednym zbiorze warunków mogą istnieć różne relacje porządku i inne odpowiedzi na pytanie, czy $p\Vdash\varphi$.

**Korekta:** formuła ma teraz postać
$\operatorname{Force}_\varphi(p,\vec\tau,\mathbb P,\leq)$.
Lemat definiowalności, jego dowód i podsumowujące twierdzenie o wymuszaniu jawnie wskazują oba parametry: zbiór warunków i relację wzmacniania. Konstrukcja nie wymaga dodatkowego parametru $1_{\mathbb P}$ dla samych klauzul wymuszania, choć taki warunek jest zakładany dla nazw kanonicznych i rozszerzenia generycznego w tej wersji książki.

### 2. Konflikt oznaczenia rangi z oznaczeniem nazwy

Symbol $\rho$ jest używany w całym rozdziale dla nazw wymuszania, a w uwadze o dobrze ufundowanej rekurencji występował również jako nazwa funkcji rang $\rho(\tau)$.

**Korekta:** w uwadze o rangach konsekwentnie zastosowano $\operatorname{rk}(\tau)$, zachowując sumę naturalną $\operatorname{rk}(\sigma)\mathbin{\#}\operatorname{rk}(\tau)$ jako miarę malejącą w obu wzajemnie rekurencyjnych klauzulach. To zmiana oznaczenia, nie metody dowodu.

### 3. Niewystarczająco jawne hipotezy pięciu lematów

Korzystanie ze stałych założeń na początku rozdziału pozostawiało kilka stwierdzeń niesamodzielnych, np. lemat o lokalnej generyczności zawierał $M,G,\mathbb P$ bez jawnych określeń w samej tezie.

**Korekta:** w lemacie lokalnej generyczności, monotoniczności atomowej, domknięcia atomowego na gęstość, monotoniczności i regularności formuł oraz gęstości rozstrzygnięć wskazano explicite model $M$, pojęcie wymuszania, role nazw, warunków i filtrów. Zapewnia to możliwość prawidłowego odczytania każdego lematu niezależnie od uwagi wstępnej.

### 4. Niejednoznaczność w przykładzie wymuszania jednoelementowego

Dla krotki parametrów zapis $\check{\vec a}$ nie definiował, czy operator sprawdzania nazwy działa na całej krotce, czy składowo. 

**Korekta:** formułę sformułowano dla każdej ustalonej $\varphi(x_1,\ldots,x_n)$ i każdego $a_1,\ldots,a_n\in M$, zapisując oddzielnie wszystkie nazwy $\check a_i$ w relacji wymuszania.

## Niezależna kontrola dowodów

1. **Atomowa rekurencja.** Wszystkie zależności mają mniejszą sumę naturalną rang nazw; dziedziczne zbieranie nazw składowych jest operacją zbiorową w $M$. Monotoniczność i domknięcie na gęstość wynikają z klauzul bez zamiany kierunku wzmacniania warunków.
2. **Lemat definiowalności.** Dla każdej ustalonej formuły definiujemy osobną formułę wymuszania. Kwantyfikacja po nazwach w klauzuli egzystencji jest kwantyfikacją pierwszego rzędu po definiowalnej klasie, nie po nieistniejącym zbiorze wszystkich nazw. Nie formułuje się wewnętrznego predykatu prawdy sprzecznego z twierdzeniem Tarskiego.
3. **Atomowy lemat prawdy.** Sprawdzono cztery kierunki dla przynależności i równości. Zbiór $E$ w dowodzie równości jest gęsty i definiowalny; lokalna generyczność pozwala z niego wybrać odpowiedni warunek.
4. **Pełny lemat prawdy.** Negacja jest obsługiwana przez zbiór rozstrzygnięć $D_\varphi\in M$, zaś dla egzystencji zbiór warunków z nazwanym świadkiem jest gęsty poniżej warunku wymuszającego egzystencję. Nie korzysta się przy tym z założenia $M[G]\models\mathrm{ZFC}$.
5. **Schematy ZFC.** Ponownie przeanalizowano konstrukcje nazw $U_\tau$ (suma), $S_{\tau,\chi}$ (wyróżnianie), $\Pi_\tau$ (zbiór potęgowy), $R$ (zastępowanie) i $\dot f$ (aksjomat wyboru). W szczególności:
   - $B_\tau$ i $A_\tau$ ograniczają konstrukcje do zbiorów należących do $M$;
   - zbiór $\mathcal S_\tau$ zawiera nazwy podzbiorów $\tau^G$ w całym rozszerzeniu, a $\theta_\rho$ reprezentuje dowolne $b=\rho^G\subseteq\tau^G$;
   - w schemacie zastępowania minimalne rangi $\alpha_{\sigma,t}$ zbiera się ze zbioru $J$ i ogranicza przez $\gamma$, przed zastosowaniem AC w $\mathbb P\times N_{\gamma+1}^M$.
6. **Metamatematyka.** Założenie o przeliczalnym tranzytywnym modelu zbiorowym ZFC nie zostało utożsamione z samą niesprzecznością ZFC. Zwykłe CI i testy Python nie są formalnymi dowodami w Lean.

Nie wykryto dalszej sprzeczności w konstrukcjach nazwy zbioru potęgowego ani zastępowania po poprawkach z audytu II.

## Nowe testy regresyjne

Dodano dwa niezależne testy (łącznie w rozdziale **16**):
- **Porządek jest istotnym parametrem.** Dwa różne preordery na tym samym trójelementowym zbiorze warunków, mające ten sam warunek największy, dają różne wartości atomowego wymuszania dla ustalonej pary nazw. Jest to skończony kontrprzykład przeciw pominięciu $\leq$ jako parametru definiowalności.
- **Wyczerpujący mały lemat prawdy.** Dla 8 nazw rangi pierwszej, wszystkich 64 uporządkowanych par nazw, dwóch generycznych gałęzi skończonego drzewa i obu relacji atomowych porównano **256 przypadków** relacji wymuszania z wartościami nazw. Wszystkie przypadki były zgodne z lematem prawdy. Są to tylko testy skończonych przypadków, a nie dowód ogólnego twierdzenia.

Dodatkowa asercja chroni rozróżnienie symboli $\operatorname{rk}(\tau)$ i $\rho$.

**Inwentarz matematyczny:** bez zmian: 4 definicje, 6 lematów, 6 twierdzeń, 3 przykłady, 5 uwag, 12 dowodów; 25 etykiet i 26 odsyłaczy. Książka: 33 rozdziały, 828 etykiet, 616 odsyłaczy.

## CI, PDF i werdykt

- [GitHub Actions #45021115326](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021115326): **SUCCESS** — 16 testów regresyjnych rozdziału 33 (w tym 256 skończonych przypadków lematu prawdy), komplet pozostałych testów rozdziałów 01–32, kontrola inwentarza i odsyłaczy, kompilacja LaTeX oraz kontrola skompilowanego PDF.
- [GitHub Actions #45021176300](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021176300): **SUCCESS** także po dodaniu raportu audytu III; źródła matematyczne były niezmienione między przebiegami.
- **Aktualny PDF:** 288 stron, rozdział 33 zajmuje strony PDF **281–288**. Wszystkie osiem stron wyrenderowano i obejrzano, ze szczególną uwagą na rekurencję atomową, definicję wymuszania formuł, schemat zastępowania oraz końcowe przykłady. Rysunki nie występują w tym rozdziale; nie stwierdzono nakładania się tekstu z formułami, utraconych znaków ani ucięć.
- **Log LaTeX:** 0 błędów, 0 ostrzeżeń `Overfull \\hbox`, 0 nierozwiązanych odsyłaczy, 0 nierozwiązanych cytowań; 1 ostrzeżenie `Underfull \\hbox` w całej książce.
- **Uwaga o składzie:** końcowa strona rozdziału jest częściowo niezapełniona, ale zawiera merytoryczny przykład i końcową uwagę; nie zastosowano agresywnego ścieśniania dowodów.

**Werdykt po audycie III:** wykryto rzeczywistą nieścisłość w parametrach formuły definiowalności oraz trzy problemy jednoznaczności/ścisłości sformułowań. Wszystkie poprawiono w kodzie źródłowym. **Kontrola matematyczna po poprawkach, 16 testów, kompilacja i przegląd PDF: PASS.** Rozdział 33 pozostaje **w trakcie audytowania, nie jest jeszcze oznaczony jako stabilny**, ponieważ audyt III wymagał rzeczywistych korekt. Następny etap to niezależny **audyt IV**.
