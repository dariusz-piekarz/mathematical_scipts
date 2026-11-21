# Algebra liniowa — rozdział 02, audyt 3

Data: 2026-11-21  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
Commit treści po audycie: `35f1caee8f1832e478785dd53e078bbdf0cc46e1`

## Zakres

Trzeci audyt dotyczy **wyłącznie poprawności i luk już istniejącego materiału**. Ponownie oceniono twierdzenia o wymiarze kardynalnym, sumie algebraicznej, sumach prostych, ilorazach, dopełnieniach i ich dowody. Nie dodawano nowych tematów, definicji, lematów ani twierdzeń. Szczególną uwagę zwrócono na przypadek pustej rodziny indeksów, rozróżnienie skończonych sum wektorowych i sum kardynalnych, zależność od aksjomatu wyboru oraz znaczenie „naturalności” i „jednoznaczności” rozkładów.

## Poprawki

### 1. Pominięta rodzina zerowa w dowodzie o sumie zewnętrznej

W dowodzie Twierdzenia `thm:lin2-zewn-wewn` stwierdzano, że zewnętrzna suma prosta jest podprzestrzenią produktu, wskazując jedynie skończoność nośnika kombinacji liniowych. Brakowało jawnego uzasadnienia niepustości, zwłaszcza dla pustego zbioru indeksów.

Dodano rodzinę zerową \((0_{U_i})_{i\in I}\), która ma pusty nośnik i należy do sumy zewnętrznej. Następnie wykazano skończoność nośnika dowolnej kombinacji dwóch rodzin o skończonych nośnikach. Kryterium podprzestrzeni można teraz zastosować bez przemilczanego kroku.

### 2. Jawne przestawienie składników sum kardynalnych

W dowodzie Twierdzenia `thm:lin2-wzor-wymiarowy` po otrzymaniu
\[
\dim(U+W)=|C|+|A|+|D|,\quad
\dim(U\cap W)=|C|,\quad
\dim U=|C|+|A|,\quad
\dim W=|C|+|D|
\]
dopisano pełne uzasadnienie pierwszego wzoru:
\[
(|C|+|A|+|D|)+|C|=(|C|+|A|)+(|C|+|D|).
\]
Korzystamy wyłącznie z przemienności i łączności dodawania kardynalnego. W szczególności nie dokonujemy nieuprawnionego odejmowania nieskończonych liczb kardynalnych.

### 3. Tytuł przykładu dopełnień a rzeczywiście udowodniona teza

Nagłówek przykładu `prz:lin2-dopelnienia` miał tytuł „Niekanoniczność dopełnienia”, choć dwa przedstawione dopełnienia dowodzą bezpośrednio **niejednoznaczności**, a nie osobnego formalnego twierdzenia o braku konstrukcji naturalnej.

Zmieniono jedynie tytuł na „Niejednoznaczność dopełnienia algebraicznego”. Zachowano stabilną etykietę i zawartość przykładu.

### 4. Jednoznaczne założenia we wzorze wymiarowym dla ilorazu

W Twierdzeniu `thm:lin2-iloraz-dopelnienie` zastąpiono nieprecyzyjny zwrot „w przypadku skończenie wymiarowym” jawnym założeniem, że **\(V\) jest skończenie wymiarowa**. W takim przypadku zarówno \(U\), jak i \(V/U\) mają skończony wymiar; uzasadnia to przejście do odejmowania liczb naturalnych i wzoru
\(\dim_K(V/U)=\dim_KV-\dim_KU\).

## Przegląd pozostałych wyników

- **Równoliczność baz Hamela:** rozdział poprawnie wyprowadza ograniczenie mocy z nośników skończonych i twierdzenia Cantora–Bernsteina. Użyty wynik \(|I\times\mathbb N_0|=|I|\) dla nieskończonego \(I\) jest jawnie rozpoznanym importem z arytmetyki kardynalnej ZFC.
- **Sumy podprzestrzeni i wzór wymiarowy:** sprawdzono rozłączność skonstruowanych fragmentów baz, rozpinanie i zastosowanie warunku niezależności liniowej.
- **Suma prosta:** warunek prostości dla każdej skończonej podrodziny jest równoważny jednoznaczności rodzin składników o skończonym nośniku; dla \(I=\varnothing\) twierdzenie jest poprawne.
- **Ilorazy:** równość warstw, dobrze określone działania, własność uniwersalna i izomorfizm \(U/(U\cap W)\cong(U+W)/W\) zostały ponownie sprawdzone. Nie wykryto w nich nowej usterki.
- **Dopełnienia:** dowód istnienia korzysta z rozszerzenia bazy, a w przypadku skończenie wymiarowym ze skończonego algorytmu. Przykład z \(\mathbb R^2\) poprawnie dowodzi niejednoznaczności.

## Walidacja techniczna

- Rozdziały 01–02: łącznie **108 unikalnych etykiet**, brak duplikatów i brak nierozwiązanych odsyłaczy `\\ref`, `\\eqref`.
- Zachowano poprawne parowanie środowisk LaTeX.
- Nie ma niedozwolonych wystąpień „unia” i „relacja liniowa” w treści (poza historycznymi nazwami etykiet).
- Nie dodano plików graficznych ani zależności zewnętrznych.
- Ostatnia poprawiona wersja: CI [44896266670](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44896266670), **success**. Wszystkie etapy: walidacja obu rozdziałów, sprawdzenie terminologii i odsyłaczy, pełna kompilacja LaTeX, kontrola końcowego PDF oraz eksport artefaktu — zakończone powodzeniem. Końcowy PDF ma **27 stron**. W finalnym `linear_algebra.log` nie ma `LaTeX Warning`, `Overfull`, `Underfull`, `Undefined control sequence` ani `Missing character`. Wizualnie sprawdzono strony **20, 22, 25 i 26**, w tym fragmenty poprawionych dowodów i tytuł przykładu; nie stwierdzono kolizji lub ucięć tekstu.
- Dawne niepowiązane błędy globalnej walidacji pozostałych skryptów są nadal raportowane osobno, poza zakresem audytu rozdziału 02.

## Status

**Audyt 3 wykrył drobne luki dowodowe i nieprecyzyjne sformułowania; wszystkie zostały poprawione. Rozdział 02 pozostaje otwarty.** Kolejny audyt powinien ponownie sprawdzić obecne treści bez rozszerzania zakresu, a zamknięcie rozdziału może nastąpić dopiero po cyklu bez istotnych poprawek i udanym CI.
