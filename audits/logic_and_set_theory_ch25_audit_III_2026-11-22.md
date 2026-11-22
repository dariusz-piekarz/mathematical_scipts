# Logika matematyczna i teoria mnogości — rozdział 25, audyt III (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/25-aksjomaty-zf-zfc-i-konstrukcje-zbiorowe.tex`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Zakres:** tylko rozdział 25; bez dodawania nowych twierdzeń, definicji, przykładów i dygresji.

## Niezależna kontrola matematyczna po poprawkach audytu II

1. **ZF i składnia:** zrewidowano dokładność kwantyfikatorów aksjomatów ekstensjonalności, istnienia zbioru pustego, pary, sumy, zbioru potęgowego, schematów separacji i zastępowania, nieskończoności i ufundowania. Zastępowanie wymaga jednoznacznej wartości dla każdego elementu zbioru wyjściowego; separacja ma ustalony zbiór ograniczający. Paradoks Russella nie jest błędnie traktowany jako poprawna definicja zbioru uniwersalnego.
2. **Konstrukcje:** zweryfikowano istnienie iloczynu kartezjańskiego przez dwukrotne użycie zbioru potęgowego i separację, a także przecięcia niepustej rodziny bez wyboru z rodziny zbiorów. W dowodzie Cantora rozpisano diagonalizację oraz oddzielny przypadek zbioru pustego.
3. **Konstrukcja $\omega$:** skontrolowano niepustość rodziny indukcyjnych podzbiorów wskazanego zbioru $I$, istnienie jej przecięcia, indukcyjność tego przecięcia oraz zawieranie się w każdym indukcyjnym zbiorze.
4. **Następnik von Neumanna:** potwierdzono indukcję dowodzącą przechodniości, osobne wykorzystanie ufundowania do $n\notin n$ i iniekcyjności $S$, zamknięcie $S[\omega]$, przechodniość $\omega$ i jawne $0\in S(n)$ potrzebne dalej.
5. **Rekursja:** przeanalizowano istnienie i jednoznaczność przybliżeń $f_n:S(n)\to B$, w tym warunek przy $k=n$ i zgodność ograniczeń; wykazano formalną definiowalność pojedynczych wartości $f_n(n)$ oraz stosowność schematu zastępowania w konstrukcji globalnego wykresu $F$. Dowód nie zakłada AC ani wcześniej istnienia nieskończonego wykresu.
6. **Arytmetyka:** przeanalizowano wszystkie równania definiujące dodawanie, mnożenie i potęgowanie; dowody łączności, przemienności, rozdzielności i prawa wykładników wykorzystują wyłącznie wcześniejsze wyniki oraz indukcję.
7. **Porządek i dzielenie:** sprawdzono dowód $m<n\iff m\in n$ dopiero po zdefiniowaniu arytmetycznego $\le$, dowód liniowości i dobrego uporządkowania przez ufundowanie, indukcję silną, monotoniczność oraz pełny dowód istnienia i jednoznaczności ilorazu z resztą, szczególnie nierówności $0<b$, $t<t+b$, $bq+b\le bq'\le a$.
8. **Zakres modeli:** indukcja obejmuje zbiory $X\subseteq\omega$ rozważane w ZF; rozróżniono je od wszystkich zewnętrznych podzbiorów wewnętrznego $\omega$ w dowolnym modelu ZF.
9. **Porównanie ze źródłami:** zweryfikowano, że materiał o arytmetyce von Neumanna, obecny w pełniejszej wersji opracowania, nie został pominięty na rzecz krótszej wersji pliku TeX.

**Wynik audytu matematycznego III:** nie wykryto dodatkowej nieuzasadnionej formuły ani nieprecyzyjnego warunku wymagającego kolejnej zmiany. Nie wprowadzono zmian do treści rozdziału w tej iteracji.

## Walidacja struktury, języka i składu

- Inwentarz bez zmian: 16 definicji, 14 przykładów, 6 lematów, 11 twierdzeń, 2 wnioski, 5 uwag, 19 dowodów i 1 rysunek.
- Zachowano unikatowe 46 etykiet; 25 odsyłaczy rozdziału ma istniejące cele. Sprawdzenie to jest objęte regresją oraz CI całej książki.
- Testy rozdziału 25, w tym testy uzasadnienia rekurencji i dzielenia: **PASS**.
- GitHub Actions dla źródła o identycznym SHA bloba: **SUCCESS**, workflow [45004356090](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45004356090); porównanie SHA potwierdza brak zmian rozdziału pomiędzy tym przebiegiem a audytem III.
- Kompilacja pełnego skryptu: **202 strony**. Sam rozdział 25: **10 stron**.
- Obejrzano wyrenderowane wszystkie 10 stron, w tym diagram następnika; bez kolizji tekstów, ilustracji, marginesów i nagłówków.
- Log: **0** przepełnień `Overfull \hbox` i **0** niezdefiniowanych odsyłaczy.
- Terminologia i kolejność wywodu zachowane.

## Werdykt

**Rozdział 25 — STABILNY po audycie III.** Druga iteracja wykryła i poprawiła luki uzasadnień; trzecia, niezależna iteracja nie wykazała nowych usterek, a testy i skład przeszły kontrolę. Można zakończyć kolejne audyty tego rozdziału do czasu uzyskania nowej przesłanki do zmian. Rozdział 26 i kolejne rozdziały nie były przedmiotem tej iteracji.
