# Logika matematyczna i teoria mnogości — audyt V rozdziału 32

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/logic_and_set_theory/32-podstawy-wymuszania-i-modele-generyczne.tex`.  
**Cel:** niezależna piąta kontrola matematyczna i końcowa walidacja stabilności przed przejściem do rozdziału 33.

## Podsumowanie ustaleń

**W audycie V nie stwierdzono nowego błędu matematycznego ani potrzeby poprawiania źródła LaTeX rozdziału 32.** Nie dopisano twierdzeń, lematów, definicji ani rysunków; wszystkie etykiety i odsyłacze zachowano. Aby nie poprzestawać na ponownym przeczytaniu tych samych dowodów, rozszerzono testy regresyjne o wyczerpujące sprawdzenie wszystkich małych preporządków.

## Ponowna kontrola matematyczna — wyniki

### 1. Preporządki, zgodność i filtry

Definicja pojęcia wymuszania nie wymaga antysymetrii ani warunku największego. Wszystkie dowody wykorzystują poprawny kierunek $q\le p$ („$q$ jest silniejszym warunkiem”), również dla warunków równoważnych w nieantysymetrycznym preporządku. Wykazanie wzajemnej niezgodności warunków w generycznym filtrze ma postać dowodu nie wprost: elementy filtru posiadają wspólne wzmocnienie, więc nie mogą być niezgodne. Formuła gęstego zbioru $D_p=\{q:q\le p\text{ lub }q\perp p\}$ daje dokładnie jedno z dwóch rozstrzygnięć dla $p$, bez założenia separatywności.

### 2. Rasiowa–Sikorski i modele przeliczalne

Ogólny lemat dla dowolnego niepustego pojęcia wymuszania w ZFC i przeliczalnej rodziny gęstych podzbiorów pozostaje poprawny. Dobre uporządkowanie $\mathbb P$ pozwala wskazać $p_{n+1}\in D_n$ z $p_{n+1}\le p_n$ bez zakładania przeliczalności $\mathbb P$. Skierowanie skonstruowanego filtru wynika z warunku $p_{\max(m,n)}\le p_n,p_m$, a nie z arbitralnego przecięcia dwóch zbiorów gęstych.

Wniosek o istnieniu filtru generycznego nad przeliczalnym tranzytywnym modelem $M$ korzysta ze **zewnętrznej** enumeracji rodziny $\mathcal D_M$ gęstych podzbiorów należących do $M$. Nie utożsamia jej z obiektem wewnętrznym $M$ ani nie wyprowadza istnienia przeliczalnego tranzytywnego modelu z samego $\operatorname{Con}(\mathrm{ZFC})$.

### 3. Cohen, gęsty podporządek i nowy obiekt

Zgodność skończonych funkcji jest równoważna zgodności wartości na wspólnej dziedzinie, a każda para warunków generycznego filtru ma wspólne wzmocnienie. Dlatego $c_G=\bigcup G$ jest funkcją. Gęste zbiory $D_n$ gwarantują jej całkowitość, a zbiory $E_x$ różność od każdego starego ciągu binarnego $x\in M$. Warunki $\operatorname{Fn}(\omega,2)$ są absolutne między tranzytywnym $M$ i otaczającym uniwersum, ponieważ są skończonymi zbiorami uporządkowanych par liczb naturalnych.

Dowód przenoszenia generyczności z gęstego podporządku $\mathbb Q$ do $\mathbb P$ poprawnie wprowadza gęsty zbiór $D_{\mathbb Q}$ z parametrami należącymi do $M$. Przykład $2^{<\omega}\subseteq\operatorname{Fn}(\omega,2)$ jest zgodny z porządkiem przez przedłużanie.

### 4. Hierarchia nazw i rozszerzenie $M[G]$

Hierarchia $N_\alpha$ jest rosnąca; dla zbioru par nazw i warunków rangi pierwszych współrzędnych mają wspólne ograniczenie porządkowe, więc sam zbiór par jest nazwą. Przy tranzytywnym $M$ rozpoznawanie nazwy $\tau\in M$ jest absolutne; dowód opiera się na indukcji po zwykłej randze zbioru i wewnętrznym zastępowaniu w $M$. Rekurencja dla $\tau^G$ jest dobrze ufundowana.

Nazwa kanoniczna $\check x$ interpretuje się jako $x$, ponieważ niepusty filtr zawiera warunek największy. Nazwa $\dot G$ interpretuje się jako $G$. Twierdzenie o $M[G]$ dowodzi **tylko** jego istnienia jako zbioru, tranzytywności, $M\subseteq M[G]$ i $G\in M[G]$. Nie twierdzi jeszcze, że $M[G]\models\mathrm{ZFC}$, dlatego nie zakłada z góry twierdzenia o wymuszaniu przewidzianego do rozdziału 33.

## Dodatkowe testy — wyczerpujące małe modele

W pliku `tools/tests/test_logic_and_set_theory_ch32.py` dodano **jeden nowy test** z enumeracją **wszystkich 34 zwrotnych i przechodnich relacji** na oznaczonych zbiorach o mocy 1, 2 lub 3; uwzględniono relacje nieantysymetryczne i brak warunku największego. Dla tych relacji sprawdzono:

- 84 przypadki filtru; 49 przypadków filtru przecinającego każdy gęsty podzbiór — w każdym działa dychotomia rozstrzygania zgodności;
- 110 wystąpień gęstego podporządku i 140 przeniesień filtru generycznego — w każdym otrzymuje się filtr generyczny w wyjściowym preporządku;
- **1276 konstrukcji Rasiowej–Sikorskiego**: każdy warunek początkowy i każda uporządkowana para gęstych podzbiorów; za każdym razem otrzymany filtr zawiera warunek początkowy i przecina obydwa wskazane zbiory.

Obliczenia zweryfikowano niezależnym lokalnym przeglądem skończonych przypadków. Testy **nie zastępują dowodów dla nieskończonych pojęć wymuszania ani nie stanowią formalizacji w Lean**, ale stanowią niezależną kontrolę braku łatwo przeoczonych kontrprzykładów.

## Inwentarz i status walidacji

- Źródło matematyczne rozdziału **bez zmian** w audycie V.
- Inwentarz bez zmian: **8 sekcji, 11 definicji, 7 lematów, 4 twierdzenia, 1 wniosek, 4 przykłady, 4 uwagi, 12 dowodów, 1 rysunek TikZ, 33 etykiety i 11 odsyłaczy**.
- Testów regresyjnych rozdziału 32 jest obecnie **15**.
- [GitHub Actions — testy V](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017853388). **Wynik zostanie odnotowany po zakończeniu kompilacji.**
- Ponieważ plik LaTeX rozdziału nie uległ zmianie, inspekcja siedmiu stron PDF po audycie IV pozostaje aktualna dla treści rozdziału 32. Nowa kompilacja całej książki jest dodatkową kontrolą po rozszerzeniu zestawu testów.

## Werdykt warunkowy

**Audyt matematyczny V: bez nowych usterek.** Po potwierdzeniu pomyślnego CI rozdział 32 może otrzymać status **STABILNY PO V AUDYTACH**; dalszym planowym zadaniem będzie nowy rozdział 33 (relacja wymuszania, lemat definiowalności, lemat prawdy i twierdzenie o wymuszaniu), którego nie należy mylić z brakami rozdziału 32.
