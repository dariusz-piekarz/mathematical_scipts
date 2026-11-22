# Logika matematyczna i teoria mnogości — rozdział 32, audyt II

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Podstawy wymuszania i modele generyczne”.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/32-podstawy-wymuszania-i-modele-generyczne.tex`.

## Zakres niezależnej ponownej kontroli

Przeanalizowano po kolei definicje, wnioski i dowody dotyczące: kierunku porządku warunków, zgodności, filtrów i zbiorów gęstych, generyczności, lematu Rasiowej–Sikorskiego, ciągu Cohena, gęstego podporządku, hierarchii nazw, interpretacji nazw kanonicznych i zbioru $M[G]$. Kontrola obejmuje również hipotezy i kwantyfikatory, zależności od ZFC w metateorii, zewnętrzną przeliczalność modelu, etykiety i odsyłacze LaTeX, testy regresyjne oraz wizualną jakość poprzednio skompilowanego PDF.

## Wykryte i naprawione braki

### 1. Za mocne ograniczenie lematu Rasiowej–Sikorskiego

Dotychczasowa wersja zakładała, że samo pojęcie wymuszania $\mathbb P$ jest przeliczalne. **Założenie to jest zbędne w ZFC.** Twierdzenie zostało wzmocnione do dowolnego niepustego $\mathbb P$ oraz *przeliczalnej rodziny* gęstych podzbiorów $(D_n)_{n\in\omega}$.

W nowym dowodzie ustala się za pomocą AC dobre uporządkowanie $\prec$ zbioru warunków i wybiera $p_{n+1}$ jako $\prec$-najmniejszy element $D_n$ spełniający $p_{n+1}\le p_n$. Jest on określony dzięki gęstości. Filtr $G=\{q:\exists n\ (p_n\le q)\}$ zawiera warunek początkowy, jest skierowany, domknięty ku słabszym warunkom oraz przecina każde $D_n$. Nie wymaga się enumeracji samego $\mathbb P$.

Wniosek dla przeliczalnego tranzytywnego $M\models\mathrm{ZFC}$ zapisano ze sprecyzowaną rodziną $\mathcal D_M$ wszystkich gęstych podzbiorów $\mathbb P$ należących do $M$; jest ona zewnętrznie przeliczalna i niepusta. Zwrócono uwagę, że w tym zastosowaniu $\mathbb P\subseteq M$ jest przeliczalne zewnętrznie, lecz nie jest to dodatkowy warunek ogólnego twierdzenia.

### 2. Uzasadnienie, że zbiory par nazw i warunków rzeczywiście są nazwami

Pierwsza wersja podawała $\dot G=\{(\check p,p):p\in\mathbb P\}$ oraz nazwę $\dot C$ i stwierdzała, że należą do modelu wyjściowego, ale **nie wyjaśniała dostatecznie wyraźnie, dlaczego są nazwami** w uprzednio zdefiniowanej hierarchii $N_\alpha$.

Dopisano do uwagi o rangach argument: rodzina $(N_\alpha)$ jest rosnąca; dla dowolnego zbioru par $(\sigma,p)$ z pierwszymi współrzędnymi będącymi nazwami schemat zastępowania pozwala zebrać minimalne poziomy $\rho(\sigma)$ w zbiór liczb porządkowych; ich kres górny wyznacza poziom $N_\alpha$ zawierający wszystkie pierwsze współrzędne. Stąd sam zbiór par jest elementem $N_{\alpha+1}$. Zastosowano to wprost do $\dot G$ i $\dot C$.

To potrzebne doprecyzowanie formalne: bez niego sama definicja $M[G]$ nie uzasadniałaby jeszcze stwierdzenia, że $G=(\dot G)^G$ pochodzi od nazwy należącej do $M$.

### 3. Suma warunków jest funkcją

W dowodzie nowości ciągu Cohena doprecyzowano, że każdy *dwa* warunki z generycznego filtru mają wspólne wzmocnienie, więc są zgodne na przecięciu dziedzin. Dzięki zastosowaniu tego argumentu do każdej pary suma całego filtru $c_G=\bigcup G$ jest funkcją, nie tylko suma dwóch ustalonych warunków.

## Zbadane argumenty, które pozostały poprawne

- **Filtry i kierunek porządku:** w pojęciu wymuszania $q\le p$ oznacza wzmocnienie. Domknięcie filtru ku słabszym warunkom i skierowanie ku silniejszym zastosowano zgodnie z tą konwencją.
- **Rozstrzyganie zgodności:** zbiór $D_p=\{q:q\le p\lor q\perp p\}$ jest gęsty i należy do $M$ przez wyróżnianie, ponieważ $p\in M$ i relacja zgodności jest absolutna dla zbiorowych warunków. Przypadki $p\in G$ i istnienia $q\in G$ niezgodnego z $p$ są rozłączne.
- **Nowość $c_G$:** rodziny $D_n$ i $E_x$ są gęste i należą do $M$ dla odpowiednich parametrów; odpowiednio zapewniają całkowitość $c_G$ i różność od każdego ciągu binarnego z $M$.
- **Odtwarzanie filtru:** dla każdego skończonego $p\subseteq c_G$ wspólne wzmocnienie skończonej rodziny warunków z $G$ przedłuża $p$, więc $p\in G$.
- **Gęsty podporządek:** zbiór $D_{\mathbb Q}$ jest gęsty w $\mathbb Q$ i należy do $M$, co zapewnia generyczność filtru przeniesionego na $\mathbb P$.
- **Wartości nazw:** rekurencja po poziomach nazw jest poprawna; filtr zawiera element największy, dlatego $(\check x)^G=x$. Zbiór $M[G]$ jest tranzytywny i zawiera $M,G$, ale **nie dowiedziono jeszcze $M[G]\models\mathrm{ZFC}$** — trafnie zastrzeżono zakres do rozdziału 33.
- **Zależności aksjomatyczne:** istnienie przeliczalnego tranzytywnego modelu ZFC jest dodatkowym założeniem względem samej syntaktycznej niesprzeczności teorii. Nie mylono generyczności nad $M$ z przecinaniem wszystkich zewnętrznych zbiorów gęstych.

## Kontrole automatyczne i skład

- Źródło po poprawkach zachowuje **33 różne etykiety i 11 odsyłaczy**, 8 sekcji oraz niezmieniony inwentarz środowisk: 11 definicji, 7 lematów, 4 twierdzenia, 1 wniosek, 4 przykłady, 4 uwagi, 12 dowodów, jeden rysunek TikZ.
- Testy `tools/tests/test_logic_and_set_theory_ch32.py` rozszerzono o wymóg poprawnej, ogólnej tezy lematu Rasiowej–Sikorskiego; prostą instancję numeryczną na uporządkowaniu skończonych ciągów binarnych; oraz obliczenie wartości $\check x$ i $\dot G$ w skończonym modelu testowym.
- Ostatnie skompilowane PDF po **audycie I** miało sześć stron rozdziału 32, obejrzanych ponownie w audycie II; układ rysunku i wzorów nie wykazywał kolizji. **Nie stanowi to jeszcze wizualnej kontroli nowego PDF po poprawkach II.**
- [GitHub Actions — audyt II, wersja po poprawkach](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45015692156). Wynik zostanie dopisany po zakończeniu tego przebiegu; raport nie przypisuje z góry statusu PASS.

## Werdykt wstępny

**Audyt II wykrył niepotrzebne ograniczenie ważnego twierdzenia i dwa miejsca z pominiętymi uzasadnieniami. Wszystkie trzy poprawiono bez dodawania nowych twierdzeń lub zmieniania etykiet.** Ocena techniczna zmienionego źródła jest uzależniona od aktualnej kompilacji CI i kontroli nowego PDF. Kolejnym krokiem po zakończeniu audytu II pozostaje niezależny audyt III.
