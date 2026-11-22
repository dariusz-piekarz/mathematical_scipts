# Logika matematyczna i teoria mnogości — audyt XI rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Badany plik:** `chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex`.  
**Nieprzerwany identyfikator bloba rozdziału:** `1d510628d52469ef8aa00ad021125192c54ec439`.  
**Werdykt końcowy: audyt XI CZYSTY — drugi czysty audyt (2/2).** Nie było konieczności modyfikowania treści rozdziału. Pełna walidacja CI oraz niezależna inspekcja rzeczywistego PDF potwierdziły wynik.

## 1. Ponowna kontrola założeń i przypadków brzegowych

1. **Niezerowość algebry regularnie otwartych podzbiorów.** Hipoteza \(X\ne\varnothing\) jest zgodna z konwencją \(0\ne1\). Nie utożsamia się iloczynu boolowskiego z topologiczną sumą regularnie otwartych zbiorów. Z definicji \(i(p)=\operatorname{int}\overline{\mathbb P_{\le p}}\) wynika \(i(p)\ne0\) również dla nieantysymetrycznego preorderu.
2. **Hierarchia nazw i klasy właściwe.** Każdy \(\operatorname{dom}\tau\) jest zbiorem nazw niższej rangi; w klauzuli egzystencji bierze się kres wartości leżących w *zbiorze* \(\mathbb B\), uzyskanym przez wyróżnianie. Nie bierze się nieistniejącego w ZFC „kresu klasy właściwej”.
3. **Podstawianie i lemat o pełności.** Sprawdzono, że dowód używa zupełnej rozdzielności \(b\wedge\bigvee_i c_i=\bigvee_i(b\wedge c_i)\), a na etapie wyboru świadków najpierw ogranicza rangi kandydatów dla indeksów należących do zbioru; nie stosuje aksjomatu wyboru do klasy właściwej.
4. **Aksjomat nieskończoności.** Przejście od \(\llbracket\eta\in\check\omega\rrbracket=\bigvee_n\llbracket\eta=\check n\rrbracket\) do domknięcia na następniki jest poprawne: na każdym fragmencie \(\llbracket\eta=\check n\rrbracket\) nazwa \(\eta\cup\{\eta\}\) jest równa \(\check{n+1}\), a \(\llbracket\check{n+1}\in\check\omega\rrbracket=1\). Wykorzystano wcześniejsze nazwy pary i sumy, a nie samą deklarację o induktywności.
5. **Zastępowanie i ufundowanie.** W zastępowaniu równość definiująca dziedzinę nazwy obrazu jest rzeczywistą równością funkcji (nie równością boolowską). W ufundowaniu minimalizowana jest ranga *wszystkich* świadków przynależności na dodatnim fragmencie, nie wyłącznie rang elementów dosłownej dziedziny nazwy.
6. **Wybór, iloraz i pełność modelowa.** Surjekcja z podzbioru nazwy liczby porządkowej na dowolną nazwę zbioru wystarcza do dobrego uporządkowania przez najmniejszy przeciwobraz. W lematach ilorazowych stosuje się dowolny **zewnętrzny** ultrafiltr, w tym niegeneryczny; rozumowanie egzystencjalne korzysta z pełności nazw i nie zakłada zachowania nieskończonych kresów przez ultrafiltr.
7. **Dwa rozstrzygnięcia CH.** Wersja ccc dla \(\operatorname{Add}(\omega,\omega_2)\) zachowuje oba pierwsze nieprzeliczalne kardynały, a odrębne nazwy podzbiorów \(\omega\) dają iniekcję \(\omega_2\to\mathcal P(\omega)\). W \(\operatorname{Coll}(\omega_1,2^{\aleph_0})\) przeliczalna domkniętość wyklucza nowe podzbiory \(\omega\) i zachowuje \(\omega_1\), natomiast gęste warunki nadają nazwanej funkcji z \(\omega_1\) wszystkie stare wartości z \(\lambda=2^{\aleph_0}\); stąd CH. Wszystkie argumenty mają charakter twierdzeń w ZFC, a nie twierdzeń wyłącznie o modelu tranzytywnym.

## 2. Niezależna, świeża próba semantyczna

Wykonano lokalnie *od zera*, bez użycia modułu testowego repozytorium, semantykę atomową w \(\mathcal P(\{0,1,2\})\), kodowaną maskami 3-bitowymi. Indukcja po rangach nazw implementuje obie klauzule atomowe. Na wygenerowanych nazwach zawierających elementy o różnych rangach wykonano:

- **2500** losowych prób refleksyjności, symetrii, przechodniości równości i podstawiania w *obu* argumentach relacji przynależności;
- **300** losowych prób budowy świadka dla formuły \(\exists x\,x\in\sigma\) przez mieszanie nazw wybranych oddzielnie na trzech atomach; każdorazowo sprawdzono dokładną równość wartości świadka i całej egzystencji, także na fragmencie pustym.

**Wynik lokalny: PASS 2500/2500 i 300/300.** Jest to kontrola semantyki dla algebr skończonych; nie stanowi dowodu pełnego twierdzenia w nieskończonych algebrach ani weryfikacji w Lean.

## 3. Kontrola języka, odsyłaczy i składu

Nie znaleziono nowych koniecznych poprawek językowych, znaczeniowych ani niezgodności z regułami terminologicznymi. Zachowano wszystkie etykiety i strukturę rozdziału. Poprzedni audyt X zweryfikował 28 unikalnych etykiet, 34 odsyłacze i 16 stron rozdziału (strony 296–311 PDF, cała książka 311 stron); w audycie XI źródło pozostało identyczne.

Pełne GitHub Actions **[45062047392](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062047392): SUCCESS** dla commitu `d345409659806d4915d728118e0936ae5ba571e7`. Wszystkie kroki w tym testy rozdziału 35, skład LaTeX i walidacja PDF zakończyły się sukcesem. Pobrano artefakt **14770295070** z faktycznego przebiegu. PDF ma **311 stron**, A4; rozdział 35 obejmuje strony **296–311**. Wyrenderowano nowy zestaw 16 stron i oceniono montaż wszystkich stron pod kątem widocznych kolizji, obcięć i czytelności; problemów nie stwierdzono. W logu było **0** błędów LaTeX, **0** `Overfull \\hbox`, **0** nierozwiązanych odsyłaczy, **0** brakujących znaków; jedno `Underfull \\hbox` bez znaczenia dla układu.

## 4. Następny etap

**Audyt XI = drugi czysty (2/2)** dla niezmienionego bloba `1d510628d52469ef8aa00ad021125192c54ec439`. Następnie wykonać **audyt XII potwierdzający** na dokładnie tym samym źródle, z osobną kontrolą dowodów i techniki. Dopiero po czystym audycie XII rozdział 35 otrzyma status stabilny.
