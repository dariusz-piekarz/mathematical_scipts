# Logika matematyczna i teoria mnogości — audyt III rozdziału 36

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex.  
**Blob rozdziału:** 6891b26609ccf77a0aaddc28653bb872f05a1701 (niezmieniony od audytu I).  
**Werdykt matematyczno-redakcyjny:** czysty — bez nowej koniecznej poprawki; do zatwierdzenia jako drugi czysty audyt po wyniku CI.

## 1. Kontrola semantyki wymuszania

Ponownie rozpisano właściwe kwantyfikatory w definicji relacji dla HS. Dla negacji zachodzi
\[
 p\Vdash_{\mathrm{HS}}\neg\varphi
 \iff\neg\exists q\le p\ (q\Vdash_{\mathrm{HS}}\varphi).
\]
Rozstrzygające warunki, wymuszające formułę albo jej negację, tworzą zbiór gęsty w modelu wyjściowym, więc argument prawdy nie używa nieuzasadnionego założenia, że każde hipotetyczne wzmocnienie należy do ustalonego filtru. Dla egzystencji gęstość świadków HS poniżej p pozwala wybrać świadka w *tym samym* filtrze generycznym. Obie zasady zachowują automorfizmy permutujące indeksy.

Sprawdzono rozróżnienie (i) dosłownej równości nazw przy nośniku, (ii) równości wymuszanej oraz (iii) równości wartości nazw w ilorazie nad nietranzytywnym modelem. Nie utożsamia się tych trzech pojęć. W dowodzie relatywnej niesprzeczności model zbiorowy jest konstruowany z klas nazw i relacji określanych przez standardowe formuły, nie przez rekursję po zewnętrznie nieufundowanym porządku.

## 2. ZF: próba adversarialna dla zbioru potęgowego i zbierania

Przy zbiorze potęgowym zweryfikowano osobno kierunki:
- każda nazwa w zbiorze kandydatów ma wartość będącą podzbiorem wartości argumentu;
- każdy podzbiór argumentu należący do HS^G ma przedstawiciela z ograniczonego *zbioru* nazw, którego dziedzina jest zawarta w iloczynie dom(tau)×P.

Konstrukcja \(\sigma_*\) zawiera warunki wymuszające jednocześnie \(\rho\in\sigma\) oraz \(\rho\in\tau\), a zatem reprezentuje przecięcie semantyczne, niezależnie od literalnej postaci dziedzin. Zbieranie wymaga ograniczenia rang dla wszystkich par (p,rho) z jednego zbioru oraz własności gęstości wzmocnień *poniżej dowolnego* warunku wyjściowego; oba kroki występują w dowodzie. Dobór minimalnej rangi jest wykonywany w ZFC modelu wyjściowego, co nie zakłada aksjomatu wyboru wewnątrz modelu końcowego.

## 3. Niezależna regresja działania grupy

Dodatkowo wykonano niezależny lokalny rachunek na 729 częściowych tablicach z trzech wierszy i dwóch kolumn (trzy stany każdej współrzędnej: 0, 1, nieokreślona). Wszystkie 6 permutacji wierszy zachowało wartości atomowego rozstrzygania bitów: **52488/52488 sprawdzeń**. Osobno każde z trzech połączeń par wierszy dało możliwość przedłużenia w świeżej kolumnie: **2187/2187 przypadków**. Nowy test zapisano do modułu testowego rozdziału 36 (commit f2c3971945eaaacafb97608977b7f398f26bb2e6). Metody testowe rozdziału: **8**.

Kontrolowany argument o braku iniekcji \(\omega\to A\) używa świeżej zamiany indeksów k i ell, z kompatybilnymi warunkami r i pi(r). Obejmuje każdą nazwę HS posiadającą skończony nośnik, więc nie ogranicza się do konkretnej enumeracji danych Cohenów.

## 4. Inwentarz i CI

Wciąż ten sam blob źródła: **938 wierszy, 21 unikalnych etykiet, 27 odsyłaczy, 5 definicji, 7 lematów, 4 twierdzenia, 3 uwagi, 1 przykład, 12 dowodów**. W kontrolowanych miejscach środowiska LaTeX są poprawnie zamknięte, a odsyłacze prowadzą do istniejących etykiet.

Punktem odniesienia jest ukończone pełne GitHub Actions **[45064877027](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064877027): SUCCESS**, PDF 320 stron, rozdział 36 na stronach PDF 313–320. Wykonano wizualną kontrolę wszystkich ośmiu stron, bez kolizji. Dodatkowy test z tego audytu wymaga kolejnego zielonego CI; nie należy przedstawiać go jako zaliczonego w GitHub Actions, zanim przebieg testowy się zakończy.

## 5. Werdykt

Audyt III **czysty merytorycznie**, nie zmieniono tekstu rozdziału. Po potwierdzonym CI audytu II i nowego testu do zaliczenia **2/2 czystych audytów**. Następnie dodatkowy audyt IV potwierdzający z własną kontrolą techniczną i PDF. Formalizacja w Lean pozostaje niezależnym zadaniem; testy i kompilacja LaTeX nie dowodzą poprawności w jądrze Lean.
